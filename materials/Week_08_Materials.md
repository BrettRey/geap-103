# GEAP 103 Week 8: Instructor Materials Package

**Title:** When Things Go Wrong
**Phase:** Building (Week 8 of 14) — Assessment Week
**Contact time:** 3 x 55 min (165 min total: 150 min instruction + 15 min break)
**First week back from reading week.**
**Date prepared:** 2026-03-28

This file contains everything you need to prepare slides and run the class for Week 8. The lesson plan (`lesson-plans/week-08.md`) has the pedagogical rationale.

**Week 8 design note:** Two things happen this week: content (troubleshooting, error diagnosis, help requests) and assessment (Micro-Defence 2, triads, 5 criteria). The triad format handles defences in ~30 min, freeing Segment C entirely for troubleshooting practice and Goal Documents. No session review this week — the triad defence is the reflection activity.

**New vocabulary (5 AWL terms):** process, sequence, outcome, resolve, anticipate

**AI tools:** AI handles Git commands and formula explanations. Students handle the diagnosis: reading the error, identifying the mismatch between expected outcome and actual outcome, describing the process they followed.

---

## Before Class

### Materials to Prepare

| Material | Description | How to share |
|----------|-------------|-------------|
| **4 error scenarios** (worked examples) | Copilot reformat gone wrong, #REF! formula, bad Git commit, "Permission denied" error | Display on projector |
| **3-4 staged error scenarios** (pair practice) | Broken formula, accessibility issues, confusing commit history, AI-generated wrong output | Share via OneDrive |
| **Bad help request** | "It doesn't work. Can you help?" | Display on slide |
| **Good help request** | Full example with context/problem/tried/expected | Display on slide |
| **Help request template** | 4-field template | Display on slide |
| **Scoring sheets** | 5 criteria + fluency band + evidence basis, one per student | Print |

### Triad Preparation

- Pre-assign groups of 3 (consider mixing strong/weak based on Week 4 data)
- Identify students with partial/deferred observation from Week 4 — their groups are visited first
- Plan circulation route: you need 2-3 min per group across 3 rotations
- With ~7 groups, you'll hear ~15 of ~21 presentations substantively

---

## Segment A: Vocabulary + Worked Examples (0:00-0:40)

### Vocabulary (0:00-0:10)

**Vocabulary reference slide:**

| Term | Meaning |
|------|---------|
| **process** | The steps you follow to do something — describing your process is today's core skill |
| **sequence** | The order things happen in — a help request narrates the sequence |
| **outcome** | What actually happened — compare it with what you expected |
| **resolve** | To fix or settle a problem — more formal than "fix" |
| **anticipate** | To think about what might happen before it does |

Brief definitions (4 min), each connected to today's work.

**Pair task** (3 min): Display:

> **Bad help request:** "It doesn't work. Can you help?"
>
> Rewrite this using at least 3 of the 5 vocabulary terms. Make it specific.

Share 1-2 examples. Quick check: "Which vocabulary terms did you use? Did your version give enough information to actually help?"

---

### Worked Examples: Three Error Scenarios (0:10-0:32)

Three scenarios (not four — first week back from break, sustained attention is limited).

**Scenario 1 — Copilot reformatted everything (instructor think-aloud):**

> "I asked Copilot to fix the headings. Instead, it changed all the fonts and removed the bullet points."

| Think-aloud | Vocabulary |
|-------------|-----------|
| "What happened? Copilot interpreted 'fix' too broadly." | "The process: I gave a vague prompt. The outcome was a complete reformat." |
| Undo, revise prompt: "Change bold text on lines 3, 7, 12 to Heading 2. Don't change anything else." | "I resolved it by being more specific." |

> "This isn't a computer error. It's a communication error."

**Scenario 2 — Excel formula returns #REF! (pair prediction first):**

Display the spreadsheet with the #REF! error.

> "Look at this error. Turn to your partner: what do you think went wrong? You have 2 minutes."

Pairs discuss. 1-2 volunteers share predictions. Then think aloud:

| Think-aloud | Vocabulary |
|-------------|-----------|
| "#REF! means a reference is wrong. Something the formula points to doesn't exist." | "The sequence: someone deleted rows. The formula still points to the old range." |
| Correct the range. | "The expected outcome was a sum. The actual outcome was an error. I resolved it by fixing the reference." |

> "The error message told us exactly what was wrong. Read it first."

**Scenario 3 — Permission denied:**

Display the error message.

| Think-aloud | Vocabulary |
|-------------|-----------|
| "'Permission denied' — what does each word mean?" | "The expected outcome was a successful push. The actual outcome was a denied permission." |
| Check login status, try again. | "The sequence: push, error, check login, push again. Resolved." |

> "Error messages are written for you to read."

Quick vocabulary check:

> "Which of our five words describes what I just did? I followed a _____, described the _____, and _____ the problem."

---

### The Help Request as a Genre (0:35-0:40)

> "When you can't resolve it yourself, you write a help request."

Display the template:

> | Section | What to write |
> |---------|--------------|
> | **Context** | What I was trying to do and why |
> | **Problem** | What went wrong (exact error message or description) |
> | **What I tried** | The sequence of steps I took |
> | **Expected outcome** | What should have happened |

Display good vs. bad:

> **Bad:** "It doesn't work. Can you help?"
>
> **Good:** "I'm trying to push my portfolio to GitHub. When I ask Copilot to push, I get 'Permission denied (publickey).' I've checked that I'm logged in and tried logging out and back in. I expected the push to succeed because it worked last week."

> "Which one can someone actually help with?"

---

## Segment B: Diagnostic + Triad Defences (0:40-1:35)

### Pre-Task Planning (0:40-0:50)

> "Choose one piece of work from the last few weeks: an accessible document, a spreadsheet, a PR, an Issue, a Decision Log entry."
>
> "Think about: What did you do? What was the challenge? What error or problem did you encounter? How did you resolve it?"
>
> "The two NEW criteria this week: 'shows what was tried' and 'interprets an error.' Pick something where you can demonstrate those."

---

### Written Diagnostic (0:50-1:00)

> "Write about a problem you had with a computer tool this semester. What happened? What did you try? What was the outcome?"
>
> No AI. No notes. No partner. 10 minutes.

Collect papers when done.

---

### Recovery Buffer (1:00-1:02)

Collect papers. Students sit quietly for 2 minutes. This bridges the mode switch from silent writing to public speaking. Do not rush into triads.

---

### Triad Formation (1:02-1:09)

Announce pre-assigned groups. Students move to sit together.

Display:

> **Format:** Three people. Everyone presents. Each person gets 4 minutes. Partners listen, then give feedback.
>
> **After the presenter finishes:**
> - Partner 1: "One thing you explained clearly was _____."
> - Partner 2: "One question I have is _____."

Display the 5 criteria:

> | Criterion | What the instructor looks for |
> |-----------|------------------------------|
> | Clear description of what was done + context | You explain what and why |
> | Correct use of essential terminology | You use course vocabulary accurately |
> | Explains a decision or choice | You justify something |
> | **Shows what was tried** | **NEW: You describe your process** |
> | **Interprets instruction/error accurately** | **NEW: You read and explain an error** |

Display rotation plan:

> **Round 1** (1:09-1:18): Student A presents → B and C give feedback
> **Round 2** (1:18-1:27): Student B presents → A and C give feedback
> **Round 3** (1:27-1:35): Student C presents → A and B give feedback

**Attendance contingency (first week back):** If attendance is low, some triads will break. Leftover students form ad hoc triads or join existing groups as 4th member. Decide quickly — don't let regrouping take more than 2 minutes.

---

### Triad Defences (1:09-1:35)

All groups run simultaneously. Instructor circulates.

**What to do at each group:**
1. Arrive, listen for 2-3 min
2. Ask one follow-up question targeting the new criteria:
   - "What did you try when that went wrong?"
   - "What did the error message say? What does it mean?"
   - "What was the sequence — what happened first?"
3. Score 5-criterion checklist + fluency band + evidence basis (full/partial/deferred)
4. Move to next group

**Priority order:** Visit Week 4 partial/deferred students first.

At 1:35:

> "Two new criteria this week: 'shows what was tried' and 'interprets an error.' If those were hard to talk about, that tells you what to practise. Those criteria stay for Week 11."

---

## Break (1:35-1:50)

---

## Segment C: Troubleshooting Practice + Goal Document (1:50-2:45)

### Troubleshooting Practice: Staged Errors (1:50-2:15)

> "Now you practise. I've prepared some broken things. With your partner, diagnose the problem and write a help request."

Display:

> Choose 2 scenarios from the shared folder. For each one:
>
> 1. **Partner A diagnoses** while Partner B watches (5 min): What's the error? What does the message mean? What's the sequence that led to this?
> 2. **Partner B writes a help request** using the template (3 min)
> 3. **Switch roles** for the second scenario
>
> When done: read your partner's help request. "Could you actually help based on what they wrote?"
>
> **AI check:** Paste your help request into AI. Ask: "Based on this description, what do you think the problem is?" Does AI's diagnosis match yours?

**What to say while circulating:**

| What you see | What to say |
|-------------|------------|
| Student staring at error message | "Read it aloud. What does each word mean?" |
| Student diagnosed correctly | "Good. Now: what's the sequence? First ___, then ___." |
| Help request is vague | "Read this as if you've never seen this problem. Could you help?" |
| Student resolved the error | "Nice. If this was a Git error, save a screenshot — that's your Error Recovery episode." |
| Strong pair finished both | "Write a help request for a problem you anticipate in your project." |

**Git Episodes reminder:**

> "If you diagnosed and fixed a Git error, save a screenshot of the error and what you did. That's your Error Recovery episode."

---

### Goal Document: Risk Assessment (2:15-2:35)

> "Today was about things going wrong. Now: think forward. What might go wrong with YOUR project?"

**Prompt** (display):

> What's the riskiest part of your project? What's most likely to not work? Write a help request for a problem you anticipate might happen.

**Sentence frames** *(optional — use if you're stuck)*:

> - "The riskiest part of my project is _____ because _____."
> - "If _____ goes wrong, I would try _____."
> - "I anticipate a problem with _____ because _____."
> - "I need help with _____. I tried _____, but _____. The expected outcome was _____."

**Writing** (12 min): Entry 8 in the Goal Document.

**Pair exchange with A/B turn-taking** (8 min): Partner A reads their help request aloud (3 min), Partner B responds: "Could you resolve this? What would you try?" Switch.

---

### Closing (2:35-2:45)

> "Today you practised two skills: diagnosing problems and explaining them clearly. Both are language skills."
>
> "You used five new words: process, sequence, outcome, resolve, anticipate. These apply to any problem in any course, any job."
>
> "Next week you start building your project in earnest. You've been thinking about it for eight weeks. You have the tools and the vocabulary. Start making it real."
>
> "I'll read your Goal Documents this week and give you feedback on clarity, feasibility, and how your thinking has developed since Week 4."
>
> "Decision Log entries 3-5: I'm collecting them this week. I'll return feedback by Week 10 — including a note on whether you addressed your Round 1 improvement target."

---

## After Class

### Instructor Tasks

| Task | Deadline | Notes |
|------|----------|-------|
| Read Goal Documents (entries 1-8) | Before Week 10 | Return 1-3 sentence comments on clarity, feasibility, development since Week 4 |
| Score micro-defences | Within 1 week | Note patterns: which criteria are strong/weak across class |
| Collect DL entries 3-5 | This week | Return feedback by Week 10 with confirmation signal ("target addressed" / "still developing") |
| Update observation tracking | After scoring | Confirm every student has ≥1 full observation across Weeks 4-8 |
| Note Git Episode evidence | Ongoing | Which students resolved Git errors during troubleshooting? |

---

## Catch-Up Instructions for Latecomers

### If You Missed Week 8

**1. Learn these 5 terms:**

| Term | Meaning |
|------|---------|
| **process** | The steps you follow to do something |
| **sequence** | The order things happen in |
| **outcome** | What actually happened (compare with what you expected) |
| **resolve** | To fix or settle a problem |
| **anticipate** | To think about what might happen before it does |

**2. Practise reading error messages.** Open any tool (Excel, Word, GitHub). Try to do something that produces an error. Read the error message. What does it say? What does each word mean?

**3. Write a help request.** Use this template:
- Context: What I was trying to do
- Problem: What went wrong (exact error)
- What I tried: Steps I took
- Expected outcome: What should have happened

**4. Update your Goal Document.** Write entry 8: What's the riskiest part of your project? What might go wrong? Write a help request for a problem you anticipate.

**5. Micro-Defence make-up.** Write the diagnostic (describe a technical problem, 10 min, no AI). Schedule an ad hoc triad with your instructor during any independent work period.

---

## Instructor Prep Checklist

- [ ] Triad groups pre-assigned (mix strong/weak based on Week 4 data)
- [ ] Students with partial/deferred from Week 4 identified — their groups visited first
- [ ] Scoring sheets printed (5 criteria + fluency band + evidence basis)
- [ ] Written diagnostic prompt on slide
- [ ] Paper or locked-down devices for diagnostic
- [ ] 4 error scenarios for worked examples:
  - [ ] Copilot reformat gone wrong
  - [ ] #REF! formula error in Excel
  - [ ] Git commit with wrong file
  - [ ] "Permission denied" or "File not found"
- [ ] 3-4 staged error scenarios shared via OneDrive for pair practice
- [ ] Help request template on slide
- [ ] Good vs. bad help request on slide
- [ ] Vocabulary slides: process, sequence, outcome, resolve, anticipate
- [ ] 5-criterion checklist on slide (2 new criteria highlighted)
- [ ] Triad rotation plan on slide (3 rounds with times)
- [ ] Peer feedback frame on slide
- [ ] Goal Document prompt + sentence frames on slide (frames labelled "optional")
- [ ] DL entries 3-5 collection plan

---

## Assessment Alignment

| Assessment component | What happens this week | Weight | CLOs |
|---------------------|----------------------|--------|------|
| **Micro-Defence 2** | Triads (5 criteria); written diagnostic; peer feedback | Part of 25% component | 2, 5 |
| **Decision Log** | Entries 3-5 collected for Round 2 feedback | Part of 30% component | 3, 4 |
| **Goal Document** | Entry 8: risk assessment (ungraded) | Instructor reads + comments | — |
| **Git Episodes** | Error Recovery opportunity during troubleshooting | Part of 10% component | 1 |

---

## Language Development Summary

| Skill | Activity |
|-------|----------|
| **Vocabulary** | 5 AWL terms (process, sequence, outcome, resolve, anticipate) via bad-help-request rewriting. Error message, troubleshoot, debug, help request, log introduced contextually. |
| **Speaking** | Triad defence (4 min, 5 criteria, 2 new); peer feedback x2; pair diagnosis discussion; pair help request exchange |
| **Reading** | Error messages (4 worked examples + staged errors); help request genre (good/bad); partner's help request; 5-criterion checklist |
| **Writing** | Diagnostic (~50-100 words, unmediated); help request for staged error (template); Goal Document entry 8 (conditional/hypothetical) |
| **Listening** | Worked example think-alouds; two partners' triad defences; instructor follow-up questions; partner's help request |

---

## Timing Summary

| Segment | Time | Minutes | Notes |
|---------|------|---------|-------|
| Vocabulary | 0:00-0:10 | 10 | 5 AWL terms + pair rewriting task |
| Worked examples | 0:10-0:32 | 22 | 3 scenarios (pair prediction at Scenario 2) |
| Help request genre | 0:32-0:40 | 8 | Template + good/bad examples |
| Pre-task planning | 0:40-0:50 | 10 | Review portfolio, choose artifact |
| Written diagnostic | 0:50-1:00 | 10 | Unmediated, no AI |
| Recovery buffer | 1:00-1:02 | 2 | Mode switch from writing to speaking |
| Triad formation | 1:02-1:09 | 7 | Groups + criteria + rotation plan |
| Triad defences | 1:09-1:35 | 26 | 3 rounds, all groups simultaneous |
| **Break** | **1:35-1:50** | **15** | |
| Troubleshooting practice | 1:50-2:15 | 25 | Staged errors, pair A/B diagnosis + help requests |
| Goal Document | 2:15-2:35 | 20 | Writing (12 min) + pair exchange (8 min) |
| Closing | 2:35-2:45 | 10 | Summary, DL collection reminder |
| **Total** | | **150 min instruction** | |
