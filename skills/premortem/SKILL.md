---
name: premortem
description: "Run a premortem on any plan, launch, product, hire, strategy, partnership, commitment, or high-cost decision by assuming it failed 6 months from now and working backward to expose failure modes, hidden assumptions, and concrete revisions. Mandatory triggers: 'premortem this', 'premortem my', 'run a premortem', 'what could kill this', 'future-proof this', 'stress test this plan', 'what am i missing here', 'find the blind spots'. Strong triggers: 'what could go wrong', 'am i missing anything', 'poke holes in this', 'where will this break', 'devil's advocate this'. Do not trigger on simple feedback requests, factual questions, or LLM Council requests. Do trigger when the user has a plan or commitment where the cost of being wrong is high."
---

# Premortem

A premortem assumes the plan has already failed and works backward to explain why. Use this frame to break agreeable, optimistic evaluation and produce concrete failure analysis before the user commits.

## Use And Non-Use

Good targets:

- Product or feature launches
- Launch plans with money, credibility, or reputation on the line
- Pricing or business-model changes
- Hiring or partnership decisions
- Strategic or positioning pivots
- Research, publication, career, workflow, or operational plans with high cost of being wrong

Bad targets:

- Vague ideas with no concrete plan yet; help plan first, then premortem
- Questions with one right answer; answer directly
- Creative feedback on a draft; treat as editing or review
- Irreversible decisions; use a postmortem/mitigation frame instead
- LLM Council requests; use the council if the user wants multiple perspectives rather than failure analysis

## Context Minimum

Before running the premortem, gather enough context to answer:

1. **What is it?** Describe the plan, decision, launch, hire, or strategy in one sentence.
2. **Who is it for / who does it affect?** Identify audience, customers, team, stakeholders, collaborators, or affected parties.
3. **What does success look like?** State the desired outcome so failure can be defined by inversion.

First scan available context before asking questions:

- Current conversation.
- Workspace guidance such as `CLAUDE.md`, `AGENTS.md`, `STATUS.md`, `README.md`, project briefs, plans, or files the user referenced.
- Relevant `memory/`, `notes/`, `plans/`, `docs/`, or project tracking files.

Keep this scan quick, around 30 seconds. Use file search and short reads; do not perform a broad research project before the premortem.

If any of the three minimum items are missing, ask only the most important missing question. Ask one question at a time, and stop once the minimum threshold is met. Infer from context when reasonable.

## Workflow

### 1. Set The Frame

Explicitly state the prospective-hindsight frame:

> It is 6 months from now. This plan has failed. It is done. We are looking back to understand what went wrong.

Then restate the plan, audience/stakeholders, and success criteria in compact form.

### 2. Generate Raw Failure Reasons

Produce the raw premortem as a single comprehensive analysis:

- Generate every genuine reason the plan could have died.
- Be specific to the actual plan and context.
- Do not pad with weak risks.
- Do not stop early when more real failure modes exist.
- Keep each failure reason to 1-2 sentences.

Use the number of failure reasons that is real for the plan. Four may be enough; nine may be necessary.

Each failure reason must be:

- Specific to this plan.
- Grounded in provided or discovered details.
- A real threat, not a minor inconvenience or implausible edge case.

### 3. Run Deep-Dive Agents In Parallel

Spawn one sub-agent per raw failure reason, all in parallel. If multi-agent tools are not already available, use tool discovery for multi-agent/sub-agent tools first. If sub-agent tools are unavailable, tell the user that independent-agent deep dives cannot be run in this environment; do not falsely present a single-agent analysis as agent output.

Use this prompt template for each sub-agent:

```text
You are an investigator in a premortem analysis. You've been assigned one specific failure reason to analyze in depth.

The plan:
---
[full context: what it is, who it's for, what success looks like, plus relevant workspace context]
---

PREMORTEM FRAME: It is 6 months from now. This plan has failed.

YOUR ASSIGNED FAILURE REASON: [the specific failure reason from step 2]

Your job is to go deep on this one failure. Write the story of how it actually played out. Be specific. Use details from the plan. Make it feel real, like a case study of something that actually happened.

Your output should include:

1. THE FAILURE STORY: A 2-3 paragraph narrative of how this specific failure played out. Use details from the plan. Name specific moments where things went wrong and why.

2. THE UNDERLYING ASSUMPTION: The one thing the user was taking for granted that made this failure possible. State it in one sentence.

3. EARLY WARNING SIGNS: 1-2 concrete, observable signals the user could watch for that would indicate this failure mode is starting to play out. These should be things you can actually see or measure, not vague feelings.

Keep the total response under 300 words. Be direct. Don't hedge. Don't sugarcoat.
```

### 4. Synthesize

Read every deep dive and produce a synthesis with these sections:

1. **The Most Likely Failure** - The most probable failure scenario and why it should be addressed first.
2. **The Most Dangerous Failure** - The highest-damage scenario even if less likely, and why it deserves insurance.
3. **The Hidden Assumption** - The biggest unexamined assumption across the analyses.
4. **The Revised Plan** - Concrete changes that make the plan more resilient. Each revision must map to a failure mode.
5. **The Pre-Launch Checklist** - 3-5 specific things to verify, test, or put in place before executing.

The synthesis is the main product. Make it direct, specific, and actionable.

## Required Files

Every premortem session produces two files in the current workspace or the project folder most relevant to the plan:

```text
premortem-report-[timestamp].html
premortem-transcript-[timestamp].md
```

Use a filesystem-safe timestamp such as `2026-06-30-184500`.

### HTML Report

Create a single self-contained HTML file with inline CSS, then open it with the local default browser using `open`.

Design requirements:

- Dark background, e.g. `#0a0e1a`, with clean typography and high contrast.
- Put the synthesis at the top: most likely failure, most dangerous failure, hidden assumption, revised plan, checklist.
- Include one visual card per failure reason.
- Each card shows the failure reason, failure story, underlying assumption, and early warning signs.
- Use distinct accent colors for scannability.
- Include a severity/likelihood indicator for each failure mode.
- Include a grid or card layout showing how many agents ran and their findings.
- Add a footer with timestamp and what was premortemed.

### Markdown Transcript

Save the full transcript with:

- Context gathered: what, who, success criteria, and sources consulted.
- Raw premortem failure reasons.
- All sub-agent deep dives.
- Full synthesis.

## Chat Output

After generating and opening the report, reply in chat with at most three sentences:

1. The most likely failure.
2. The hidden assumption.
3. The single most important revision.

Mention the report and transcript paths if useful.

## Standards

- Always set the "this already failed" frame explicitly.
- Always run deep-dive failure agents in parallel when the environment supports sub-agents.
- Be comprehensive but not padded.
- Be direct; do not sugarcoat serious risks.
- Make the revised plan concrete enough to do this week.
- Respect the context minimum; one clarifying question is better than a generic premortem.
- Keep failure modes grounded in the actual plan, not generic risk advice.
