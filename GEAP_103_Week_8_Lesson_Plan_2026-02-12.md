# GEAP 103 Week 8 Lesson Plan: When Things Go Wrong

**Context:** 3 x 55 min (150 min instruction + 15-min break), B1 learners, BYOD, Office 365 + Copilot
**Week 8 of 14** | Phase 2: Building (assessment week)

**Learning Objectives (Week 8):**
1. Parse error messages and diagnose what went wrong (CLO 2 assessed)
2. Write a help request that gives someone else enough information to help you (CLO 5 assessed)
3. Demonstrate oral explanation of technical work in Micro-Defence 2 (CLOs 2, 5)
4. Practise the language of risk assessment and conditional reasoning in the Goal Document

**New vocabulary (5):** error message, troubleshoot, debug, help request, log

**Goal Thread -- Risk Assessment:**
Students have been describing what they want (Weeks 1-4) and what they plan to build (Weeks 5-7). This week adds a new language skill: anticipating what might go wrong. "If X happens, I would..." "The riskiest part is..." This is conditional and hypothetical language, a key B1 development area. Writing a help request for a problem that hasn't happened yet requires students to imagine failure, describe the conditions that would trigger it, and propose what they'd try. This is harder than describing what already happened (which is what Decision Logs do). The Goal Document prompt this week is forward-looking: not "what went wrong?" but "what MIGHT go wrong?"

---

## Segment A: Vocabulary + Worked Examples (0:00--0:40)

### 0:00--0:10 | Vocabulary Pre-Training: The Language of Failure
**Format:** Instructor-led, interactive
**Language skills:** Academic vocabulary building, listening

**5 terms:**

| Term | What it means |
|------|--------------|
| **Error message** | What the computer tells you when something went wrong. It usually says what happened and where. |
| **Troubleshoot** | Figure out why something went wrong and fix it. A process, not a single step. |
| **Debug** | Find and fix a specific problem. Originally from computing, but applies to any systematic error-fixing. |
| **Help request** | A piece of writing that gives someone else enough information to help you. A professional genre. |
| **Log** | A record of what happened, in order. Error logs, activity logs, troubleshooting logs. |

For each term: define it, show it in context (an actual error message, a help request template), ask a volunteer to use it in a sentence.

"Today is about a skill you'll use every day for the rest of your life: something broke, and you need to figure out what happened and explain it to someone who can help. The skill isn't fixing the problem. The skill is describing the problem clearly enough that help becomes possible."

### 0:10--0:35 | Worked Examples: Four Error Scenarios
**Format:** Instructor demonstration with think-aloud
**Language skills:** Listening, reading (error messages, system output), critical evaluation

Instructor presents 4 real error scenarios, thinking aloud through the troubleshooting process for each:

**Scenario 1 -- Copilot reformatted everything:**
"I asked Copilot to fix the headings in my document. Instead, it changed all the fonts, removed the bullet points, and reformatted the whole thing."
- Think aloud: "What happened? Copilot interpreted 'fix' too broadly. I said 'fix the headings' but it heard 'fix the formatting.' Where's the mismatch? In my prompt."
- Fix: Undo, then revise the prompt to be specific: "Change the bold text on lines 3, 7, and 12 to Heading 2 style. Don't change anything else."
- "The error here isn't a computer error. It's a communication error. Same problem as Week 2."

**Scenario 2 -- Excel formula returns an error:**
Display a spreadsheet where a SUM formula returns `#REF!`.
- Think aloud: "What does this say? #REF! means a reference is wrong. Something the formula points to doesn't exist. Let me look at the formula... It says SUM(B2:B15), but column B only goes to B10. Someone deleted rows."
- Fix: Correct the range.
- "The error message told us exactly what was wrong. Most people panic and ignore the message. Read it first."

**Scenario 3 -- Git commit included the wrong file:**
"I committed my file to the portfolio repository. But I accidentally included a file I didn't mean to commit: my personal notes with private information."
- Think aloud: "This is a real problem. The file is now in the repository's history. I need to restore the previous version."
- Fix: Use Copilot to restore the previous commit. "Show me the commit before this one. Go back to that version."
- "This is why commit messages matter. If my last commit message said 'Added portfolio file,' I can find the right snapshot. If it said 'Updated stuff,' I can't tell which version to go back to."

**Scenario 4 -- A failed operation with an error message:**
Display a real error message (e.g., "Permission denied" when trying to push to a repository, or "File not found" when trying to open a path).
- Think aloud: "Read the message. What does each word mean? 'Permission denied' means I'm not allowed. Why? Maybe I'm not logged in, or I don't own this repository. 'File not found' means the path is wrong. Let me check."
- Fix: Diagnose from the message, try one thing, check the result.
- "Error messages are written for you to read. They almost always tell you what went wrong. The skill is: slow down and read them."

### 0:35--0:40 | The Help Request as a Genre
**Format:** Instructor-led
**Language skills:** Listening, reading (genre structure)

"When you can't fix it yourself, you write a help request. This is the most useful thing you can write in a professional setting."

Display the help request template:

| Section | What to write |
|---------|--------------|
| **Context** | What I was trying to do and why |
| **Problem** | What went wrong (exact error message or description) |
| **What I tried** | Steps I took to fix it |
| **What I expected** | What should have happened |

Show a bad help request: "It doesn't work. Can you help?"

Show a good help request: "I'm trying to push my portfolio to GitHub. When I ask Copilot to push, I get the error 'Permission denied (publickey).' I've checked that I'm logged in to GitHub in my browser, and I tried logging out and back in. I expected the push to succeed because it worked last week."

"Which one can someone actually help with? The good one gives me everything I need: what you're doing, what happened, what you tried, and what you expected. The bad one tells me nothing."

---

## Segment B: Diagnostic + Micro-Defences + Practice (0:40--1:35)

### 0:40--0:50 | Pre-Task Planning for Micro-Defence
**Format:** Individual reflection

Students review their portfolio and recent work (Weeks 5-7). Prepare to explain one artifact:
- "Choose one piece of work from the last few weeks: an accessible document, a spreadsheet, a PR you wrote, an Issue, a Decision Log entry."
- "Think about: What did you do? What was the challenge? What tools did you use? What did you learn? What would you do differently?"

This is preparation to talk, not writing a script. Students organize their thoughts, open the artifact they want to show.

### 0:50--1:00 | In-Class Written Diagnostic
**Format:** Individual, unmediated (whole class, simultaneous)
**Language skills:** Writing (unmediated, ~50-100 words)

**Prompt** (displayed): "Describe a problem you had with a computer tool this semester. What happened? What did you try? What would you do differently now?"

Rules:
- No AI assistance (Copilot closed, no chat tools)
- No notes, no partner
- Handwritten or on a locked-down device (instructor's call based on setup)
- 10 minutes

Collect when done. This provides unmediated written evidence of the student's independent language use (CLOs 2, 5).

### 1:00--1:35 | Oral Micro-Defences Begin + Troubleshooting Practice
**Format:** Individual presentations (instructor + 1 peer) while others work independently
**Language skills:** Speaking (sustained technical explanation), listening (peer), evaluative language (peer feedback)

**~5-6 students** in this segment (at ~6 min each).

Per student:
1. Student walks through ONE artifact, explaining what they did, what the challenge was, and what they learned (3-4 min)
2. Instructor asks 1-2 follow-up questions (1 min)
3. One designated peer gives structured feedback: one strength and one question (1 min)

**Peer feedback guidance** (on screen for the peer): "Tell your partner one thing they explained clearly. Then ask one question about something you didn't understand or want to know more about."

Instructor uses the task checklist to score each defence:

| Criterion | Evidence |
|-----------|----------|
| Clear problem statement + context | check / partial / missing |
| Correct use of essential terminology | check / partial / missing |
| Shows what was tried (not just "it doesn't work") | check / partial / missing |
| Interprets instruction/error accurately | check / partial / missing |
| Justifies chosen solution | check / partial / missing |

**Scoring:** Oral fluency 30%, task component 50%, written diagnostic 10%, peer feedback 10%.

**While waiting:** Other students practise troubleshooting staged errors. Instructor prepares 3-4 staged error scenarios on a shared document or repository (e.g., a spreadsheet with a broken formula, a document with accessibility issues, a repository with a bad commit). Students:
1. Identify the error
2. Diagnose what went wrong
3. Fix it (with AI assistance)
4. Write a brief help request as if they couldn't fix it

Students who finish the staged errors: begin the structured peer response on Goal Documents (below).

---

## Break (1:35--1:50)

---

## Segment C: Micro-Defences Continue + Peer Response + Goal Document (1:50--2:45)

### 1:50--2:10 | Micro-Defences Continue
**Format:** Same as above

**~4-5 more students.** Others work on the activities below.

**Logistics note:** With 15-20 students at ~6 min each, most will finish in Week 8. Any remaining students complete their defence in the first 15-20 min of Week 9. Do not rush defences to fit the schedule; quality matters more than completion.

### 1:55--2:15 | Structured Peer Response on Goal Documents
**Format:** Pair work (students not currently in micro-defence)
**Language skills:** Reading (partner's writing), writing (evaluative feedback), speaking (discussion)

*This activity runs in parallel with the remaining micro-defences. Students who have finished their defence join in.*

"You've been writing about your project for seven weeks. Your partner is going to read your Goal Document and tell you whether your plan makes sense."

Pairs read each other's Goal Document (all entries, Weeks 1-7).

**Response task** (displayed on screen): Write answers to two questions about your partner's Goal Document:
1. "Is the project plan clear enough that you could help with it?"
2. "What questions do you have? What's unclear?"

- Writing answers (5 min)
- Sharing with partner and discussing (10 min): "Here's what I understood about your plan. Here's what I'm not sure about."
- Exchange written responses so each student has their peer's feedback

"This is different from Week 4. In Week 4, the question was 'what seems to interest your partner?' Now the question is 'could you help?' That's a higher bar. If the plan isn't clear enough for someone else to act on, it needs more work."

### 2:15--2:35 | Goal Document: Risk Assessment
**Format:** Individual writing, then pair exchange
**Language skills:** Writing (conditional, hypothetical, anticipatory)

"Today was about things going wrong. You practised reading error messages and writing help requests for real problems. Now: think forward. What might go wrong with YOUR project?"

**Prompt** (displayed): "Think about your project: what's the riskiest part? What's most likely to not work? Write a help request for a problem you think might happen."

**Sentence frames** (displayed):
- "The riskiest part of my project is _____ because _____."
- "If _____ goes wrong, I would try _____."
- "I need help with _____. I tried _____, but _____. I expected _____."

Students write entry 8 in their Goal Document (~10-15 min). This entry practises the language of anticipation: conditional and hypothetical structures that are a key B1 development target.

**Pair exchange** (5 min): Partners read each other's help requests and try to answer them. "Can you suggest anything? Does the help request give you enough information to help?"

### 2:35--2:45 | Closing
**Format:** Whole class

- "Today you practised two things: diagnosing problems and explaining them clearly. Both are language skills. Reading an error message is reading comprehension. Writing a help request is professional writing. You'll do both in every course and every job."
- "Next week you start building your project in earnest. You've been thinking about it for eight weeks. You have the skills. Start making it real."
- "I'll read your Goal Documents this week and give you feedback on clarity, feasibility, and how your thinking has developed since Week 4."

---

## After Class

- **Instructor reads all Goal Documents (entries 1-8)** and returns brief comments (1-3 sentences per student). Focus: Is the project plan becoming clear and feasible? Has the student's thinking developed since Week 4? Is the language becoming more precise? Comment on clarity of thinking and language development, not on whether the project is "good enough."
- **Micro-defence scoring:** Return written scores within one week. Note patterns across the class: which checklist criteria are strong, which are weak.
- **Decision Log feedback round 2:** Entries 3-5 should be collected by this week. Return feedback by Week 10, focusing on whether Round 1 feedback was incorporated.
- **Schedule remaining micro-defences** for the start of Week 9 if needed
- **Staged error materials:** Save or note the troubleshooting scenarios used in class for potential reuse or reference

---

## Instructor Prep Checklist

- [ ] Written diagnostic prompt on slide or printed handout
- [ ] Locked-down devices or paper arranged for diagnostic (no AI access during the 10 min)
- [ ] Oral micro-defence task checklist printed (one scoring sheet per student)
- [ ] Peer feedback guidance on slide: one strength + one question
- [ ] 4 error scenarios prepared for Segment A worked examples:
  - [ ] Word document with Copilot reformatting gone wrong
  - [ ] Excel spreadsheet with a #REF! or similar formula error
  - [ ] Git repository with a bad commit (wrong file included)
  - [ ] A real error message (permission denied, file not found, or similar)
- [ ] 3-4 staged error scenarios for student practice during micro-defences (broken formula, accessibility issue, bad commit)
- [ ] Help request template on slide (context / problem / what I tried / what I expected)
- [ ] Good vs. bad help request examples on slide
- [ ] Vocabulary slides: error message, troubleshoot, debug, help request, log
- [ ] Goal Document prompt + sentence frames on slide
- [ ] Peer response instructions on slide (2 questions about partner's Goal Document)
- [ ] Order of micro-defences planned (or sign-up sheet ready)
- [ ] Peer pairings for structured Goal Document response decided (or let students self-pair)

## Language Development Summary

- **Vocabulary:** 5 terms (error message, troubleshoot, debug, help request, log) pre-trained in Segment A, applied in worked examples, troubleshooting practice, and help request writing
- **Speaking:** Oral micro-defence (3-4 min sustained technical explanation); peer feedback delivery; pre-task planning reflection; pair discussion of Goal Documents and risk; pair exchange of help requests
- **Reading:** Error messages (4 scenarios); help request examples (good and bad); partner's Goal Document (7 entries); partner's help request; staged error scenarios
- **Writing:** In-class diagnostic (~50-100 words, unmediated); help requests for staged errors (~3-5 sentences each); peer response notes (2 written answers about partner's plan); Goal Document entry (~50-100 words, conditional/hypothetical -- new language skill this week)
- **Listening:** Worked example think-alouds (4 scenarios); peer's micro-defence; instructor follow-up questions; partner's feedback on Goal Document and help request

## Assessment Alignment

- **Oral Micro-Defence 2 (part of 25% component):**
  - In-class written diagnostic (10% of micro-defence grade): unmediated writing about a technical problem
  - Oral walkthrough (30% fluency + 50% task = 80% of micro-defence grade): sustained explanation of work and learning
  - Peer feedback (10% of micro-defence grade): assessed on the quality of the *peer's* feedback, not the presenter's work
  - **CLOs 2 and 5 assessed** (first formal assessment of both; Week 4 was diagnostic baseline only)
- **Decision Log entries 3-5:** Collected around this week for feedback round 2 (returned by Week 10)
- **Goal Document:** Entry 8 (ungraded; instructor reads after this week and returns 1-3 sentence comments on clarity, feasibility, and development since Week 4)
- **Git Episodes -- Error Recovery episode opportunity:** Students who troubleshoot a Git error during the staged practice have evidence toward this required episode

**DL/GD distinction this week:** The Decision Log (if written this week) records a specific AI interaction and the student's evaluation of it (backward-looking: what happened, what I decided). The Goal Document records anticipated risks and how to handle them (forward-looking: what might happen, what I would try). If a student writes both, the DL evaluates a past event and the GD imagines a future one.
