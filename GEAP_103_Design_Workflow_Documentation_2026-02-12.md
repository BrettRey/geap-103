# GEAP 103: AI-Assisted Curriculum Design Workflow

**For:** Catherine, Michael DiPetta, Patricia Glogowski
**Project:** GEAP 103 Basic Computer Skills (Foundation Semester, B1)
**Date:** 2026-02-12
**Designer:** Brett Reynolds, with Claude (Anthropic) as design partner

---

## What Was Produced

A complete course package for GEAP 103, a 14-week, 3-hours/week course for B1-level EAP students learning to use computers as a workspace they control. The package includes:

| Document | Purpose |
|----------|---------|
| CLOs (8 course learning outcomes) | What students can do by the end |
| Assessment Framework v4 | How learning is assessed (weights, rubrics, feedback architecture) |
| 14-Week Topic Sequence v4 | Week-by-week challenges, vocabulary, Goal Document prompts |
| 14 Lesson Plans (Weeks 1-14) | Timed activities, instructor talk, prep checklists |
| Instructor Orientation | Helps faculty understand the design philosophy |

All documents are internally consistent (cross-referenced, aligned terminology, matched timing).

---

## The Design Sequence

The order matters. Each document constrains the next.

```
CLOs
 ↓
Assessment Framework (how do we know students achieved the CLOs?)
 ↓
Topic Sequence (what challenges develop toward those CLOs, week by week?)
 ↓
Lesson Plans (what happens in each 165-minute session?)
 ↓
Instructor Orientation (how do we communicate the design to faculty?)
```

**Why this order:** Starting with lesson plans or topic sequences leads to activities that don't connect to assessment, or assessment that doesn't measure what was taught. Starting with CLOs and assessment forces every activity to justify its existence: "What CLO does this develop? How will we know?"

---

## How AI Was Used at Each Stage

### Stage 1: Assessment Framework (v1 through v4)

**What happened:** Brett described the course constraints (B1 learners, BYOD, Office 365 + Copilot, 3 hrs/week) and his design philosophy. Claude drafted an assessment framework. Brett reviewed it, identified problems, and pushed back. Four iterations.

**What AI was good at:** Generating complete, structurally coherent frameworks quickly. Connecting assessment components to CLOs. Identifying gaps (e.g., "CLO 8 has no assessment vehicle").

**What AI needed the human for:** Design principles. Brett's core insight -- "English is the control layer; the artifact is a vehicle, not the destination" -- shaped every design decision. AI-generated frameworks that organized around artifacts or tools were rejected because they violated this principle. The human's job was to supply the organizing logic and reject output that looked plausible but was conceptually wrong.

**Key example:** Early drafts assessed "artifact quality" (how good is the spreadsheet?). Brett redirected to "communicative package" (can you document what you built, explain your decisions, and share it with someone?). This changed the assessment from a product evaluation to a language assessment. AI would never have made this move on its own.

### Stage 2: Topic Sequence (v1 through v4)

**What happened:** Claude drafted a 14-week sequence based on the CLOs and assessment framework. Three major revisions, driven by Brett identifying conceptual problems.

**Critical shift (v3 to v4):** v3 organized weeks around tools ("Week 5: Documents with AI + Accessibility," "Week 6: Spreadsheets with AI"). Brett identified this as incoherent: it turned the course into an Office 365 tour, which contradicts the CLOs (about articulating goals, evaluating AI output, communicating, collaborating). v4 reorganized around challenges ("Week 5: Making Something Others Can Read and Use," "Week 6: Making Sense of Numbers"). The tools appear in the same weeks but as means, not ends.

**Lesson for other designers:** AI defaults to organizing around tools or content topics because that's what most curriculum documents do. If your design philosophy is different, you need to catch this and redirect explicitly. Saying "don't organize around tools" once is not enough; the tendency recurs in every draft.

### Stage 3: Simulated Expert Reviews

**What they are:** We asked Claude to review the assessment framework and topic sequence from the perspective of specific named scholars. Each "reviewer" was given the scholar's known theoretical commitments and asked to evaluate the design through that lens.

**Assessment Framework reviewers:**
- Constant Leung (language assessment)
- Mark Guzdial (computing education)
- David Boud (assessment design)

**Topic Sequence reviewers:**
- Rod Ellis (task-based language teaching)
- Greg Wilson (computing for non-programmers)
- Richard Mayer (cognitive load theory)

**Lesson Plan reviewers (Weeks 5-14):**
- Rod Ellis (TBLT)
- Mark Guzdial (computing education)
- Richard Mayer (cognitive load theory)

**How they worked:** Each reviewer received the full document set and was asked to write a detailed, week-by-week review from their theoretical perspective. Reviews were generated by independent AI agents (one per reviewer, per batch of weeks) to prevent cross-contamination.

**What they were good for:**
- **Stress-testing ideas.** When three independent "reviewers" flag the same concern (e.g., "the Goal Document is always scheduled at session end when fatigue is highest"), that's a signal worth attending to.
- **Identifying assumptions.** Reviewers asked questions the designer hadn't considered (e.g., "What happens to students who finish their micro-defence early? 40 minutes of unstructured waiting?").
- **Checking internal consistency.** Reviewers caught places where the assessment framework promised something the topic sequence didn't deliver.

**What to watch for:**
- **These are simulations, not real reviews.** The "Ellis" review draws on Claude's knowledge of Rod Ellis's published work. It is not what Rod Ellis would actually say. Use them as intellectual sounding boards, not as authorities.
- **Reviewers can be wrong about context.** All three topic sequence reviewers flagged Git in Week 3 as too early, assuming traditional command-line Git difficulty. Brett pushed back: with AI handling commands, Git is simple. The reviewers' theoretical frameworks were sound, but their factual assumptions about the tool didn't match the course's AI-assisted context. The human must judge whether the reviewer's concern reflects the actual situation.
- **Reviewers tend to agree too readily with the overall design.** They critique details but rarely challenge the fundamental approach. If you want a genuine challenge to your design philosophy, you need to ask for it explicitly.

### Stage 4: Lesson Plans

**What happened:** Weeks 1-4 were written iteratively (three rounds of revision as the design philosophy crystallized). Weeks 5-14 were drafted in parallel batches by specialized AI agents, each given the complete document set (CLOs, assessment framework, topic sequence, format model from Week 4) as context.

**Batching:**
- Batch 1: Weeks 5-6, 7-8, 9-10 (three parallel agents)
- Batch 2: Weeks 11-12, 13-14 (two parallel agents)

**Verification:** All 14 plans were checked against a 12-point checklist:
1. Timing adds up to 165 min
2. Topic sequence activities accounted for
3. CLOs match activation timeline
4. Vocabulary pre-trained in Segment A
5. Pre-task planning in every Segment B
6. Goal Document prompt + sentence frames present
7. Assessment alignment matches framework v4
8. "Artifact Packages" terminology consistent
9. Tool-independence maintained
10. Instructor prep checklist is actionable
11. Language development summary covers all skills
12. Assessment weeks follow micro-defence pattern

**Post-drafting:** Simulated expert reviews (30 total: 3 reviewers x 10 weeks), followed by targeted revisions where reviewer convergence was strongest.

### Stage 5: Alignment Passes

**What happened:** After all documents were drafted, a systematic check for internal consistency across the full document set. This caught:
- CLO timing table with wrong columns (fixed)
- Inconsistent assessment terminology ("artifact" vs. "Artifact Package")
- Prompt schedule missing sentence frames for some weeks
- Pair work descriptions that didn't match lesson plan activities

**Lesson for other designers:** AI-generated documents are internally coherent within a single document, but cross-document consistency requires explicit checking. If the assessment framework says "feedback returned by Week 6" and the topic sequence says "Week 5," only a systematic pass catches this.

### Stage 6: Instructor Orientation

**What happened:** Brett identified five common traps that faculty might fall into when teaching this course. Claude drafted the orientation document around these traps.

**The traps:**
1. Organizing around tools (teaching "how to use Word" instead of "can someone else read what you made?")
2. Organizing around artifacts (framing the course as "build a project" instead of "develop your English")
3. Setting the ceiling too low (assuming B1 learners can't do ambitious projects)
4. Teaching steps instead of judgment (demonstrating click-by-click procedures instead of modelling decision-making)
5. Treating the Goal Document as a project plan (it's a language exercise)

**Key line from the orientation:** "You are a language teacher. The computer is the context."

---

## Design Principles That Emerged

These weren't all present at the start. Some crystallized through the iterative process.

1. **"English is the control layer."** The course teaches English. The computer is the context. Assessment measures articulation, evaluation, documentation, and communication, not technical skill.

2. **Challenge-focused, not tool-focused.** Each week poses a question ("Can someone else read what you made?" not "Learn Word styles"). Tools appear because the challenge needs them.

3. **The Goal Document is a language exercise.** It develops from "I wish my computer could..." to "My goals changed from... to... because..." across 13 written entries. It is not a project plan. It is where students practise articulating desires, evaluating results, speculating about possibilities, and reflecting on change.

4. **Artifacts are vehicles, not destinations.** Students build things, but the assessment is on the communicative package (product + documentation + verification + sharing), not on the product alone.

5. **Tool-independent assessment.** The framework assesses articulation, evaluation, documentation, and communication regardless of which AI tools students use. A student who builds a game and a student who writes a novel are assessed on the same criteria.

6. **Changing your mind is learning.** The Goal Document celebrates revision. Dropping a weak idea and trying something new is evidence of language development.

7. **Ambition calibrated to B1.** The language level is B1. The project ambition can be high. A student who builds something complex but documents it in simple, clear English is meeting the course objectives.

---

## What Worked Well

**Speed.** The full course package (CLOs through 14 lesson plans) was designed in a concentrated period. Without AI, this would have taken months. With AI, the bottleneck was design thinking, not drafting.

**Iteration cost.** Going from v1 to v4 of the assessment framework meant discarding and rebuilding. With AI, the cost of starting over was low, which made it easier to recognize when a draft was conceptually wrong and needed to be rebuilt rather than patched.

**Simulated expert reviews as stress tests.** The reviews identified real structural concerns (e.g., Goal Document positioning, instructor bandwidth during simultaneous activities, time compression on high-value writing tasks). Cross-reviewer convergence was a reliable signal of genuine issues.

**Internal consistency.** The alignment pass caught real problems that would have surfaced during teaching. Having one system hold the full document set and check cross-references was valuable.

**Parallel drafting.** Writing 10 lesson plans through parallel agents, each given the same constraints and context, produced remarkably consistent output. This wouldn't work without a strong format model (Week 4's lesson plan served as the template).

---

## What to Watch For

**AI defaults to plausible conventions.** It will organize around tools, structure assessment around products, and frame courses around "what students will build." If your design logic is different, you must supply it and enforce it. AI doesn't push back. It generates what looks right based on patterns in its training data.

**Design principles must be explicit and repeated.** Saying "this course teaches English, not technology" in one prompt is not enough. The principle needs to be restated whenever AI generates new content, or it drifts back to tool-focused or artifact-focused framing.

**Simulated reviews are not real reviews.** They are useful for identifying structural concerns and testing ideas against theoretical frameworks. They are not a substitute for having actual colleagues or experts read your work. Use them as a design tool, not as validation.

**Cross-document consistency requires deliberate checking.** AI is good at internal coherence within a single document. It is not good at maintaining consistency across five or six documents written at different times. An explicit alignment pass is necessary.

**The human supplies the design logic.** In this project, Brett's insight that "English is the control layer" shaped every decision. Without that organizing principle, the AI would have produced a competent but conventional computer skills course. The AI elaborated and tested the principle; it did not generate it.

**Watch for fabrication in reviews.** Simulated expert "reviewers" may attribute positions to scholars that the scholars don't hold, or may construct theoretical arguments that sound authoritative but aren't grounded. The reviews are useful for the quality of the critique, not for the accuracy of the attribution.

---

## Replicating This Process

If you want to use a similar workflow for a different course:

### 1. Start with your design philosophy.
What is the course actually teaching? What's the organizing logic? Write this down in 2-3 sentences before you start. This is the constraint that keeps AI output on track.

### 2. Work top-down: CLOs → Assessment → Sequence → Plans.
Each level constrains the next. Don't start with activities and work backward to outcomes.

### 3. Use simulated expert reviews after each major component.
Choose 2-3 scholars whose theoretical frameworks are relevant to your course. Have AI generate independent reviews from each perspective. Look for convergence (the same concern from multiple reviewers). Push back where the reviewer's assumptions don't match your context.

### 4. Enforce your design principles at every stage.
When AI generates output, check it against your principles. If it drifts (and it will), redirect. Don't patch; redesign.

### 5. Do an alignment pass after all documents are drafted.
Check terminology, timing, assessment weights, CLO references, and cross-document promises. This is tedious but catches real errors.

### 6. Write an instructor orientation last.
Once the design is complete, identify the 3-5 traps that faculty might fall into. Structure the orientation around avoiding those traps.

### 7. Budget your time for design thinking, not drafting.
AI handles the drafting. Your time goes to: defining principles, evaluating output, pushing back on plausible-but-wrong suggestions, and maintaining consistency. If you're spending most of your time writing, you're not using AI effectively. If you're spending most of your time thinking, you are.

---

## Tools and Setup

- **AI:** Claude (Anthropic), accessed through Claude Code (CLI)
- **Workflow:** Conversational design sessions with persistent context across the full document set
- **Parallel agents:** Used for batch-drafting lesson plans and running simultaneous expert reviews
- **File format:** Markdown (.md) for all design documents; convertible to Word/PDF for institutional submission
- **Version control:** Date-stamped filenames (e.g., `Assessment_Framework_Draft_v4_2026-02-12.md`); older versions preserved for design history

---

## Questions?

Brett Reynolds, brett.reynolds@humber.ca
