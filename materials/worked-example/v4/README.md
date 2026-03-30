# Pixel Art Agent Dashboard v4

A real project management tool with a pixel art office interface.
You are the PM. Your AI agents are your team. Manage them from one place.

## How to run

1. Open a terminal
2. cd to this folder
3. `python server.py`
4. Open http://localhost:8080 in your browser

## What it does

- **Pixel art office** with desks, workers, a break room, clock, bookshelves, and coffee machine
- **Add AI agents** by name and CLI command (e.g., "claude", "gh copilot")
- **Assign tasks** that actually run as subprocesses on your machine
- **Watch real terminal output** stream into each worker's monitor in real time
- **Drag workers** between desks to set priority
- **Task board** on the wall: To Do, In Progress, Done
- **Activity log** tracks everything
- **Persistent state** saved in your browser (survives refresh)

## Requirements

- Python 3.9+ (uses only standard library, no pip installs)
- A modern web browser

## Architecture

- `server.py`: Python HTTP server with SSE (Server-Sent Events) for real-time streaming
- `index.html`: Self-contained HTML/CSS/JS with canvas-based pixel art rendering
- Communication: SSE for server-to-client, fetch POST for client-to-server
