# GEAP 103 Week 8 Lesson Plan: When Things Go Wrong

**Context:** 3 x 55 min (150 min instruction + 15-min break), B1 learners, BYOD, Office 365 + Copilot
**Week 8 of 14** | Phase 2: Building (assessment week)
**First week back from reading week.**

**Learning Objectives (Week 8):**
1. Parse error messages and diagnose what went wrong (CLO 2 assessed)
2. Write a help request that gives someone else enough information to help you (CLO 5 assessed)
3. Demonstrate oral explanation of technical work in Micro-Defence 2, simultaneous triads (CLOs 2, 5)
4. Practise the language of risk assessment and conditional reasoning in the Goal Document

**New vocabulary (5 AWL terms):** process, sequence, outcome, resolve, anticipate

*Error message, troubleshoot, debug, help request, and log are introduced contextually during the worked examples — they are genre/tool terms, not AWL vocabulary. Students learn them by seeing them in action.*

**No session review this week.** The diagnostic, triad defence, and peer feedback are the reflection activities (same as Week 4). Session reviews resume in Week 9.

**Goal Thread -- Risk Assessment:**
Students have been describing what they want (Weeks 1-4) and what they plan to build (Weeks 5-7). This week adds a new language skill: anticipating what might go wrong. "If X happens, I would..." "The riskiest part is..." This is conditional and hypothetical language, a key B1 development area. Writing a help request for a problem that hasn't happened yet requires students to imagine failure, describe the conditions that would trigger it, and propose what they'd try.

---

## Segment A: Vocabulary + Worked Examples (0:00--0:40)

### 0:00--0:10 | Vocabulary Pre-Training: The Language of Failure
**Format:** Instructor-led, then task-based pair activity
**Language skills:** Academic vocabulary building

**5 AWL terms:** process, sequence, outcome, resolve, anticipate

1. **Process:** "The steps you follow to do something. When you troubleshoot, you follow a process: read the error, check what happened, try a fix, check the result. Today, describing your process is the core skill."

2. **Sequence:** "The order things happen in. A help request tells someone the sequence: first I did X, then Y happened, then I tried Z. If the sequence is wrong, the help is wrong."

3. **Outcome:** "What actually happened. Compare the outcome with what you expected. 'I expected the formula to show the average. The outcome was #REF!.' That gap is the problem."

4. **Resolve:** "To fix or settle a problem. 'I resolved the error by correcting the formula range.' More formal than 'fix' -- the word you'd use in a help request or a professional email."

5. **Anticipate:** "To think about what might happen before it does. 'I anticipate a problem with file permissions.' Your Goal Document today is about anticipating what might go wrong with your project."

**Pair task** (3 min): Display a bad help request:

> "It doesn't work. Can you help?"

Pairs rewrite it using at least 3 of the 5 vocabulary terms. Share 1-2 examples.

### 0:10--0:32 | Worked Examples: Three Error Scenarios
**Format:** Instructor demonstration with think-aloud + one pair diagnostic task
**Language skills:** Listening, reading (error messages, system output), critical evaluation

Three scenarios (not four -- first week back from break, sustained attention is limited).

**Scenario 1 -- Copilot reformatted everything (instructor think-aloud):**
"I asked Copilot to fix the headings in my document. Instead, it changed all the fonts, removed the bullet points, and reformatted everything."
- Think aloud: "What's the process here? First, what happened? Copilot interpreted 'fix' too broadly. I said 'fix the headings' but the outcome was a complete reformat. Where's the mismatch? In my prompt."
- Fix: Undo, then revise: "Change the bold text on lines 3, 7, and 12 to Heading 2 style. Don't change anything else."
- "The error here isn't a computer error. It's a communication error. Same problem as Week 2."

**Scenario 2 -- Excel formula returns an error (pair prediction first):**
Display a spreadsheet where a SUM formula returns `#REF!`.

Before the think-aloud: "Look at this error. Turn to your partner: what do you think went wrong? You have 2 minutes." Pairs discuss. 1-2 volunteers share predictions.

Then instructor think-aloud: "What does this say? #REF! means a reference is wrong. The sequence: someone deleted rows, the formula still points to the old range. The expected outcome was a sum. The actual outcome is an error."
- Fix: Correct the range.
- "The error message told us exactly what was wrong. Most people panic and ignore the message. Read it first."

*The pair prediction resets attention after Scenario 1 and gives students a task-based entry point before the instructor's model.*

**Scenario 3 -- A failed operation with an error message:**
Display "Permission denied" or "File not found."
- Think aloud: "Read the message. What does each word mean? 'Permission denied' means I'm not allowed. Let me check: am I logged in? Do I own this repository? The sequence: I tried to push, the outcome was 'permission denied,' the expected outcome was success."
- Fix: Diagnose from the message, try one thing, check the result.
- "Error messages are written for you to read. They almost always tell you what went wrong."

Quick vocabulary check: "Which of our five words describes what I just did in these three scenarios? I followed a _____, described the _____, and _____ the problem."

### 0:35--0:40 | The Help Request as a Genre
**Format:** Instructor-led
**Language skills:** Listening, reading (genre structure)

"When you can't resolve it yourself, you write a help request. This is one of the most useful things you can write in a professional setting."

Display the help request template:

| Section | What to write |
|---------|--------------|
| **Context** | What I was trying to do and why |
| **Problem** | What went wrong (exact error message or description) |
| **What I tried** | The sequence of steps I took |
| **Expected outcome** | What should have happened |

Show a bad help request: "It doesn't work. Can you help?"

Show a good help request: "I'm trying to push my portfolio to GitHub. When I ask Copilot to push, I get 'Permission denied (publickey).' I've checked that I'm logged in and tried logging out and back in. I expected the push to succeed because it worked last week."

"Which one can someone actually help with? The good one gives the full sequence: what you're doing, what happened, what you tried, what you expected."

---

## Segment B: Diagnostic + Triad Defences (0:40--1:35)

### 0:40--0:50 | Pre-Task Planning for Micro-Defence
**Format:** Individual reflection

Students review their portfolio and recent work (Weeks 5-7). Prepare to explain one artifact:

> "Choose one piece of work from the last few weeks: an accessible document, a spreadsheet, a PR, an Issue, a Decision Log entry."
>
> "Think about: What did you do? What was the challenge? What tools did you use? What error or problem did you encounter? How did you resolve it?"
>
> "The two NEW criteria this week are 'shows what was tried' and 'interprets an error.' Pick something where you can demonstrate those."

### 0:50--1:00 | In-Class Written Diagnostic
**Format:** Individual, unmediated (whole class, simultaneous)
**Language skills:** Writing (unmediated, ~50-100 words)

**Prompt** (displayed): "Describe a problem you had with a computer tool this semester. What happened? What did you try? What was the outcome?"

Rules:
- No AI assistance (Copilot closed, no chat tools)
- No notes, no partner
- Handwritten on paper (recommended) or locked-down device
- 10 minutes, visible timer

Collect when done. This provides unmediated written evidence of the student's independent language use.

### 1:00--1:02 | Recovery Buffer

Collect diagnostic papers. Students sit quietly for 2 minutes. This bridges the mode switch from silent, high-stakes writing to public oral performance. Do not rush into triad formation immediately.

### 1:02--1:09 | Triad Formation + Setup

Announce pre-assigned triad groups.

Explain the format (same as Week 4, expanded criteria):

> "Same format as Week 4: three people, everyone presents. Each person gets 4 minutes. Your partners listen, then give feedback. I'll come around and listen to each group."

Display the 5 criteria:

> | Criterion | What the instructor is looking for |
> |-----------|-----------------------------------|
> | Clear description of what was done + context | You explain what and why |
> | Correct use of essential terminology | You use course vocabulary accurately |
> | Explains a decision or choice (why, not just what) | You justify something |
> | **Shows what was tried** (not just "it doesn't work") | **NEW: You describe your process** |
> | **Interprets instruction/error message accurately** | **NEW: You read and explain an error** |

Display the rotation plan:

> **Round 1** (1:09--1:18): Student A presents → B and C give feedback
> **Round 2** (1:18--1:27): Student B presents → A and C give feedback
> **Round 3** (1:27--1:35): Student C presents → A and B give feedback

**Attendance contingency (first week back):** If attendance is low (14-16 of 20), some pre-assigned triads will break. Have a backup: leftover students form ad hoc triads or join existing groups as a 4th member. For groups of 4, add one extra round or have the 4th student present during the feedback window of Round 3. Decide quickly -- don't let regrouping consume more than 2 minutes.

### 1:09--1:35 | Simultaneous Triad Defences
**Format:** All groups run simultaneously. Three rounds of ~9 minutes each.
**Language skills:** Speaking (sustained technical explanation), listening (active, with feedback responsibility)

**Peer feedback frame** (displayed):

> After the presenter finishes:
> - Partner 1: "One thing you explained clearly was _____."
> - Partner 2: "One question I have is _____."

Instructor circulates with scoring sheets. For each group:
1. Arrive, listen to the current presenter for 2-3 minutes
2. Ask one follow-up question focused on the new criteria: "What did you try when that went wrong?" or "What did the error message say?"
3. Score the 5-criterion checklist and fluency band
4. Move to the next group

**Week 8 scoring (5 criteria):**

| Criterion | Evidence |
|-----------|----------|
| Clear description of what was done + context | ✓ / partial / ✗ |
| Correct use of essential terminology | ✓ / partial / ✗ |
| Explains a decision or choice (why, not just what) | ✓ / partial / ✗ |
| Shows what was tried (not just "it doesn't work") | ✓ / partial / ✗ |
| Interprets instruction/error message accurately | ✓ / partial / ✗ |

**Observation tracking:** Record evidence basis (full / partial / deferred). Students with "partial" or "deferred" from Week 4 are visited first this round. After this round, every student should have at least one full observation across the two rounds.

**Make-up for absent students:** Write diagnostic next class, do ad hoc triad (instructor + 2 volunteers) during independent work.

At 1:35, brief whole-class check:

> "Two new criteria this week: 'shows what was tried' and 'interprets an error.' Were you able to talk about those? If you struggled, that tells you what to practise. Those criteria stay for Week 11."

---

## Break (1:35--1:50)

---

## Segment C: Troubleshooting Practice + Goal Document (1:50--2:45)

### 1:50--2:15 | Troubleshooting Practice: Staged Errors
**Format:** Pair work with structured A/B turn-taking
**Language skills:** Reading (error messages), writing (help requests), speaking (explaining diagnosis)

Instructor has prepared 3-4 staged error scenarios (shared via OneDrive or Blackboard):
- A spreadsheet with a broken formula (#REF! or #VALUE!)
- A document with accessibility issues (no headings, images without alt text)
- A repository where the most recent commit message says "Updated stuff" and the student must find which earlier commit has the version they need (reading commit messages to navigate history)
- An AI prompt that produces confidently wrong output

Pairs work through 2 scenarios (choose from the set). For each:

1. **Partner A diagnoses** while Partner B watches (5 min): "What's the error? What does the message mean? What's the sequence that led to this?"
2. **Partner B writes a help request** as if they couldn't fix it (3 min): Use the template (context / problem / what I tried / expected outcome)
3. **Switch roles for the second scenario**

After writing the help request, **AI evaluation step:** "Now paste your help request into AI. Ask: 'Based on this description, what do you think the problem is?' Compare AI's diagnosis with yours. Did AI agree? Did it catch something you missed?"

Instructor circulates:
- "What does the error message say? Can you read it aloud?"
- "What's your diagnosis? What do you think went wrong?"
- "Read your partner's help request. Could you actually help based on what they wrote?"
- "What did AI say when you pasted your help request? Did it match your diagnosis?"

**Git Episodes -- Error Recovery opportunity:** Students who diagnose and resolve a Git error (Scenario 3) can document this as their Error Recovery episode. Remind: "If you fixed a Git problem, save a screenshot of the error and what you did."

### 2:15--2:35 | Goal Document: Risk Assessment
**Format:** Individual writing, then pair exchange
**Language skills:** Writing (conditional, hypothetical, anticipatory)

"Today was about things going wrong. You practised reading error messages and writing help requests for real problems. Now: think forward. What might go wrong with YOUR project?"

**Prompt** (displayed): "What's the riskiest part of your project? What's most likely to not work? Write a help request for a problem you anticipate might happen."

**Sentence frames** *(optional -- use if you're stuck)*:
- "The riskiest part of my project is _____ because _____."
- "If _____ goes wrong, I would try _____."
- "I anticipate a problem with _____ because _____."
- "I need help with _____. I tried _____, but _____. The expected outcome was _____."

**Writing** (12 min): Students write entry 8 in their Goal Document. This entry practises anticipation: conditional and hypothetical structures that are a key B1 development target.

**Pair exchange with A/B turn-taking** (8 min): Partner A reads their help request aloud (3 min). Partner B responds: "Could you resolve this? What would you try?" Then switch. If Partner B doesn't know what to try, they ask: "What did you try first?" or "What outcome were you expecting?" — the response scaffold keeps the exchange alive.

### 2:35--2:45 | Closing
**Format:** Whole class

- "Today you practised two skills: diagnosing problems and explaining them clearly. Both are language skills. Reading an error message is reading comprehension. Writing a help request is professional writing."
- "You used five new words: process, sequence, outcome, resolve, anticipate. These apply to any problem in any course, any job."
- "Next week you start building your project in earnest. You've been thinking about it for eight weeks. You have the tools and the vocabulary. Start making it real."
- "I'll read your Goal Documents this week and give you feedback on clarity, feasibility, and how your thinking has developed since Week 4."
- DL feedback round 2 reminder: "I'm collecting Decision Log entries 3-5 this week. I'll return feedback by Week 10, including a note on whether you addressed your Round 1 improvement target."

---

## After Class

- **Instructor reads all Goal Documents (entries 1-8)** and returns brief comments (1-3 sentences per student). Focus: Is the project plan becoming clear and feasible? Has the student's thinking developed since Week 4?
- **Micro-defence scoring:** Return written scores within one week. Note patterns across the class: which criteria are strong, which are weak.
- **Decision Log feedback round 2:** Collect entries 3-5. Return feedback by Week 10 with **confirmation signal**: note whether the Round 1 improvement target was addressed ("target addressed" or "target still developing"). This closes the feedback loop.
- **Staged error materials:** Save for potential reuse or reference in Weeks 9-10.
- **Observation tracking update:** After this round, confirm that every student has at least one full observation across Weeks 4 and 8. Students with two deferred observations need priority attention at Week 11.

---

## Instructor Prep Checklist

- [ ] Triad groups pre-assigned (list of groups of 3, consider mixing strong/weak from Week 4 data)
- [ ] Scoring sheets printed: one per student (5 criteria + fluency band + evidence basis)
- [ ] Students with partial/deferred from Week 4 identified — their groups visited first
- [ ] Written diagnostic prompt on slide
- [ ] Paper or locked-down devices for diagnostic (no AI access)
- [ ] 4 error scenarios prepared for Segment A worked examples:
  - [ ] Word document with Copilot reformatting gone wrong
  - [ ] Excel spreadsheet with a #REF! or similar formula error
  - [ ] Git repository with a bad commit (wrong file included)
  - [ ] A real error message (permission denied, file not found)
- [ ] 3-4 staged error scenarios for pair troubleshooting practice (shared via OneDrive)
- [ ] Help request template on slide (context / problem / what I tried / expected outcome)
- [ ] Good vs. bad help request examples on slide
- [ ] Vocabulary slides: process, sequence, outcome, resolve, anticipate (AWL terms; error message, troubleshoot, debug, help request, log introduced contextually)
- [ ] 5-criterion checklist on slide (with 2 new criteria highlighted)
- [ ] Triad rotation plan on slide (3 rounds with times)
- [ ] Peer feedback frame on slide
- [ ] Goal Document prompt + sentence frames on slide (frames labelled "optional")
- [ ] DL entries 3-5 collection plan ready

## Language Development Summary

- **Vocabulary:** 5 AWL terms (process, sequence, outcome, resolve, anticipate) pre-trained with bad-help-request rewriting task. Error message, troubleshoot, debug, help request, log introduced contextually during worked examples. "Process" and "outcome" are high-transfer terms that connect troubleshooting to the verification cycle from earlier weeks.
- **Speaking:** Triad defence (4 min sustained technical explanation with 2 new criteria); peer feedback delivery x2 (structured frames); pair diagnosis discussion during troubleshooting practice; pair exchange of help requests from Goal Document
- **Reading:** Error messages (4 scenarios); help request examples (good and bad); staged error scenarios; partner's help request; 5-criterion checklist
- **Writing:** In-class diagnostic (~50-100 words, unmediated); help request for staged error (~3-5 sentences using template); Goal Document entry 8 (~75-100 words, conditional/hypothetical, anticipatory language)
- **Listening:** Worked example think-alouds (4 scenarios); two partners' triad defences; instructor follow-up questions; partner's help request read-aloud

## Assessment Alignment

- **Oral Micro-Defence 2 (part of 25% component):**
  - In-class written diagnostic (10%): unmediated writing about a technical problem
  - Oral triad defence (30% fluency + 50% task = 80%): sustained explanation, 5 criteria
  - Peer feedback (10%): quality of the peer's feedback
  - **CLOs 2 and 5 assessed** (first formal assessment of both; Week 4 was diagnostic baseline)
  - **5 criteria** (3 from Week 4 + 2 new: "shows what was tried," "interprets error accurately")
- **Decision Log entries 3-5:** Collected this week for feedback round 2 (returned by Week 10 with confirmation signal)
- **Goal Document:** Entry 8 (ungraded; instructor reads after this week and returns comments on clarity, feasibility, development)
- **Git Episodes -- Error Recovery opportunity:** Students who resolve a Git error during troubleshooting practice have evidence for this required episode
- **Observation tracking:** Every student should now have at least 1 full observation across Weeks 4 and 8

**DL/GD distinction this week:** The Decision Log (if written) records a specific AI interaction and the student's evaluation (backward-looking: what happened, what I decided). The Goal Document records anticipated risks (forward-looking: what might happen, what I would try). Different registers, different temporal orientation.
