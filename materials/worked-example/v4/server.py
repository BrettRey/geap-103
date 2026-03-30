#!/usr/bin/env python3
"""
Pixel Art Agent Dashboard - Server
===================================
A lightweight Python server that:
  - Serves index.html on http://localhost:8080
  - Provides SSE (Server-Sent Events) for real-time agent output
  - Spawns and manages CLI sub-processes (AI agents)
  - Accepts POST commands to launch, stop, and send input to agents

Uses ONLY the Python standard library (no pip installs).

Usage:
    python server.py
    Then open http://localhost:8080
"""

import asyncio
import json
import os
import signal
import subprocess
import sys
import time
import uuid
from http.server import HTTPServer, BaseHTTPRequestHandler
from socketserver import ThreadingMixIn
from threading import Thread, Lock
from pathlib import Path
from collections import deque

# ---------------------------------------------------------------------------
# Global state
# ---------------------------------------------------------------------------

agents: dict = {}          # agent_id -> AgentProcess
agents_lock = Lock()
sse_clients: list = []     # list of SSEClient wrappers
sse_lock = Lock()
activity_log: deque = deque(maxlen=500)


class AgentProcess:
    """Wraps a subprocess representing an AI agent."""

    def __init__(self, agent_id: str, name: str, command: str):
        self.agent_id = agent_id
        self.name = name
        self.command = command
        self.process: subprocess.Popen | None = None
        self.output_buffer: deque = deque(maxlen=2000)
        self.status = "idle"          # idle | working | done | error | stopped
        self.current_task: str | None = None
        self.task_started: float | None = None
        self.reader_thread: Thread | None = None

    def to_dict(self):
        return {
            "agent_id": self.agent_id,
            "name": self.name,
            "command": self.command,
            "status": self.status,
            "current_task": self.current_task,
            "pid": self.process.pid if self.process and self.process.poll() is None else None,
            "output_lines": len(self.output_buffer),
        }


# ---------------------------------------------------------------------------
# SSE helpers
# ---------------------------------------------------------------------------

def broadcast_sse(event: str, data: dict):
    """Send an SSE event to every connected client."""
    payload = format_sse(event, data)
    with sse_lock:
        dead = []
        for client in sse_clients:
            try:
                client.wfile.write(payload.encode("utf-8"))
                client.wfile.flush()
            except Exception:
                dead.append(client)
        for d in dead:
            sse_clients.remove(d)


def format_sse(event: str, data: dict) -> str:
    json_str = json.dumps(data)
    return f"event: {event}\ndata: {json_str}\n\n"


def log_activity(message: str):
    entry = {"time": time.time(), "message": message}
    activity_log.append(entry)
    broadcast_sse("activity", entry)


# ---------------------------------------------------------------------------
# Agent subprocess management
# ---------------------------------------------------------------------------

def _reader_thread(agent: AgentProcess):
    """Background thread that reads stdout/stderr and broadcasts via SSE."""
    proc = agent.process
    try:
        for raw_line in iter(proc.stdout.readline, b""):
            try:
                line = raw_line.decode("utf-8", errors="replace").rstrip("\n\r")
            except Exception:
                line = repr(raw_line)
            agent.output_buffer.append(line)
            broadcast_sse("agent_output", {
                "agent_id": agent.agent_id,
                "line": line,
            })
    except Exception:
        pass

    # Process ended
    exit_code = proc.wait()
    if agent.status == "working":
        elapsed = time.time() - (agent.task_started or time.time())
        if exit_code == 0:
            agent.status = "done"
            log_activity(f"{agent.name} finished task in {elapsed:.1f}s")
        else:
            agent.status = "error"
            log_activity(f"{agent.name} exited with code {exit_code} after {elapsed:.1f}s")
        broadcast_sse("agent_status", agent.to_dict())


def launch_agent_process(agent: AgentProcess, task: str):
    """Spawn a subprocess for the agent's CLI command, feeding it the task."""
    if agent.process and agent.process.poll() is None:
        # Already running
        return False

    agent.current_task = task
    agent.task_started = time.time()
    agent.status = "working"
    agent.output_buffer.clear()

    # Build command: pass task as argument or via stdin depending on command
    # We run through the shell so users can type natural commands
    full_cmd = f'{agent.command} "{task}"' if task else agent.command

    try:
        agent.process = subprocess.Popen(
            full_cmd,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            stdin=subprocess.PIPE,
            preexec_fn=os.setsid if sys.platform != "win32" else None,
        )
    except Exception as e:
        agent.status = "error"
        agent.output_buffer.append(f"[ERROR] Failed to launch: {e}")
        broadcast_sse("agent_output", {
            "agent_id": agent.agent_id,
            "line": f"[ERROR] Failed to launch: {e}",
        })
        broadcast_sse("agent_status", agent.to_dict())
        return False

    agent.reader_thread = Thread(target=_reader_thread, args=(agent,), daemon=True)
    agent.reader_thread.start()

    log_activity(f"Launched {agent.name} (PID {agent.process.pid}): {task[:80]}")
    broadcast_sse("agent_status", agent.to_dict())
    return True


def stop_agent_process(agent: AgentProcess):
    """Kill an agent's subprocess."""
    if agent.process and agent.process.poll() is None:
        try:
            if sys.platform != "win32":
                os.killpg(os.getpgid(agent.process.pid), signal.SIGTERM)
            else:
                agent.process.terminate()
        except Exception:
            try:
                agent.process.kill()
            except Exception:
                pass
        agent.status = "stopped"
        log_activity(f"Stopped {agent.name}")
        broadcast_sse("agent_status", agent.to_dict())
        return True
    return False


def send_input_to_agent(agent: AgentProcess, text: str):
    """Write text to the agent process's stdin."""
    if agent.process and agent.process.poll() is None and agent.process.stdin:
        try:
            agent.process.stdin.write((text + "\n").encode("utf-8"))
            agent.process.stdin.flush()
            log_activity(f"Sent input to {agent.name}: {text[:60]}")
            return True
        except Exception:
            pass
    return False


# ---------------------------------------------------------------------------
# HTTP Request Handler
# ---------------------------------------------------------------------------

class DashboardHandler(BaseHTTPRequestHandler):
    """Handles GET (HTML, SSE) and POST (commands) requests."""

    # Suppress default logging to keep terminal clean
    def log_message(self, format, *args):
        pass

    def _send_json(self, data, status=200):
        body = json.dumps(data).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(body)

    def _send_cors_headers(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")

    def do_OPTIONS(self):
        self.send_response(200)
        self._send_cors_headers()
        self.end_headers()

    # ---- GET routes ----
    def do_GET(self):
        if self.path == "/" or self.path == "/index.html":
            self._serve_html()
        elif self.path == "/events":
            self._serve_sse()
        elif self.path == "/api/agents":
            self._api_list_agents()
        elif self.path.startswith("/api/agent/") and self.path.endswith("/output"):
            agent_id = self.path.split("/")[3]
            self._api_agent_output(agent_id)
        elif self.path == "/api/log":
            self._api_log()
        else:
            self.send_error(404)

    def _serve_html(self):
        html_path = Path(__file__).parent / "index.html"
        try:
            content = html_path.read_bytes()
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(content)))
            self.end_headers()
            self.wfile.write(content)
        except FileNotFoundError:
            self.send_error(404, "index.html not found")

    def _serve_sse(self):
        """Open an SSE stream to the client."""
        self.send_response(200)
        self.send_header("Content-Type", "text/event-stream")
        self.send_header("Cache-Control", "no-cache")
        self.send_header("Connection", "keep-alive")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()

        # Send initial state
        with agents_lock:
            for agent in agents.values():
                payload = format_sse("agent_status", agent.to_dict())
                self.wfile.write(payload.encode("utf-8"))
        self.wfile.flush()

        with sse_lock:
            sse_clients.append(self)

        # Keep the connection alive
        try:
            while True:
                time.sleep(15)
                # Send keep-alive comment
                self.wfile.write(b": keepalive\n\n")
                self.wfile.flush()
        except Exception:
            pass
        finally:
            with sse_lock:
                if self in sse_clients:
                    sse_clients.remove(self)

    def _api_list_agents(self):
        with agents_lock:
            data = [a.to_dict() for a in agents.values()]
        self._send_json(data)

    def _api_agent_output(self, agent_id):
        with agents_lock:
            agent = agents.get(agent_id)
        if not agent:
            self._send_json({"error": "Agent not found"}, 404)
            return
        self._send_json({
            "agent_id": agent_id,
            "name": agent.name,
            "output": list(agent.output_buffer),
            "status": agent.status,
            "current_task": agent.current_task,
        })

    def _api_log(self):
        self._send_json(list(activity_log))

    # ---- POST routes ----
    def do_POST(self):
        content_len = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(content_len) if content_len else b"{}"
        try:
            data = json.loads(body)
        except json.JSONDecodeError:
            self._send_json({"error": "Invalid JSON"}, 400)
            return

        if self.path == "/api/agent/create":
            self._api_create_agent(data)
        elif self.path == "/api/agent/launch":
            self._api_launch_agent(data)
        elif self.path == "/api/agent/stop":
            self._api_stop_agent(data)
        elif self.path == "/api/agent/input":
            self._api_send_input(data)
        elif self.path == "/api/agent/remove":
            self._api_remove_agent(data)
        else:
            self.send_error(404)

    def _api_create_agent(self, data):
        name = data.get("name", "").strip()
        command = data.get("command", "").strip()
        if not name or not command:
            self._send_json({"error": "name and command required"}, 400)
            return
        agent_id = str(uuid.uuid4())[:8]
        agent = AgentProcess(agent_id, name, command)
        with agents_lock:
            agents[agent_id] = agent
        log_activity(f"Added agent: {name} ({command})")
        broadcast_sse("agent_status", agent.to_dict())
        self._send_json(agent.to_dict())

    def _api_launch_agent(self, data):
        agent_id = data.get("agent_id", "")
        task = data.get("task", "")
        with agents_lock:
            agent = agents.get(agent_id)
        if not agent:
            self._send_json({"error": "Agent not found"}, 404)
            return
        if not task:
            self._send_json({"error": "task required"}, 400)
            return
        ok = launch_agent_process(agent, task)
        self._send_json({"launched": ok, **agent.to_dict()})

    def _api_stop_agent(self, data):
        agent_id = data.get("agent_id", "")
        with agents_lock:
            agent = agents.get(agent_id)
        if not agent:
            self._send_json({"error": "Agent not found"}, 404)
            return
        ok = stop_agent_process(agent)
        self._send_json({"stopped": ok, **agent.to_dict()})

    def _api_send_input(self, data):
        agent_id = data.get("agent_id", "")
        text = data.get("text", "")
        with agents_lock:
            agent = agents.get(agent_id)
        if not agent:
            self._send_json({"error": "Agent not found"}, 404)
            return
        ok = send_input_to_agent(agent, text)
        self._send_json({"sent": ok})

    def _api_remove_agent(self, data):
        agent_id = data.get("agent_id", "")
        with agents_lock:
            agent = agents.get(agent_id)
        if not agent:
            self._send_json({"error": "Agent not found"}, 404)
            return
        stop_agent_process(agent)
        with agents_lock:
            del agents[agent_id]
        log_activity(f"Removed agent: {agent.name}")
        broadcast_sse("agent_removed", {"agent_id": agent_id})
        self._send_json({"removed": True})


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    port = int(os.environ.get("PORT", 8080))
    class ThreadingServer(ThreadingMixIn, HTTPServer):
        daemon_threads = True
    server = ThreadingServer(("", port), DashboardHandler)
    print(f"  ____  _          _    _            _    ")
    print(f" |  _ \\(_)_  _____| |  / \\   __ _  _| |_ ")
    print(f" | |_) | \\ \\/ / _ \\ | / _ \\ / _` |/ _` __|")
    print(f" |  __/| |>  <  __/ |/ ___ \\ (_| | (_| |_ ")
    print(f" |_|   |_/_/\\_\\___|_/_/   \\_\\__, |\\__,_\\__|")
    print(f"                            |___/          ")
    print(f"")
    print(f"  Agent Dashboard Server v4")
    print(f"  Listening on http://localhost:{port}")
    print(f"  Press Ctrl+C to stop")
    print(f"")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down...")
        # Kill all agent processes
        with agents_lock:
            for agent in agents.values():
                stop_agent_process(agent)
        server.shutdown()


if __name__ == "__main__":
    main()
