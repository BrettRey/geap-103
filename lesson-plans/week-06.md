# GEAP 103 Week 6 Lesson Plan: Making Sense of Numbers

**Context:** 3 x 55 min (150 min instruction + 15-min break), B1 learners, BYOD, Office 365 + Copilot
**Week 6 of 14** | Phase 2: Building

**Learning Objectives (Week 6):**
1. Read and interpret an existing spreadsheet: understand what formulas calculate and what charts show (CLO 6)
2. Use Copilot to build a summary and chart from a dataset, then verify one formula manually (CLOs 3, 4)
3. Explain in own words what a formula does and whether a chart accurately represents the data
4. Connect data skills to personal project direction in the Goal Document

**New vocabulary (5):** data, formula, interpret, verify, chart

*All five are AWL words with high transfer across the course. Cell, row, and column are introduced by pointing during the worked example -- they are spatial terms, self-evident once you see them. Average and outlier are taught through the worked example content, not as formal vocabulary items.*

**Goal Thread -- Technical Scoping (continued):**
Students continue developing planning language by connecting the week's challenge to their own project. Whether or not their project involves data, they practise describing what they would need and why. The conditional language from Week 5 ("The user might need...") extends this week to reasoning about data: "If I want to show..., I would need to organize..." This is the same planning-and-justifying complexity level, applied to a new domain.

**This week also marks two milestones:** Decision Log feedback round 1 is returned (entries 1-2), and Git Episodes become formally eligible for documentation. The Git Episodes introduction is in Segment C, where it can breathe; the DL feedback return is at the start, where it can be acted on immediately.

---

## Segment A: Feedback Return + Vocabulary + Worked Example (0:00--0:40)

### 0:00--0:07 | Decision Log Feedback Return
**Format:** Whole class, then individual reading
**Language skills:** Reading (instructor feedback)

Return Decision Log feedback on entries 1-2. Each student receives one strength and one specific improvement target.

"Read your feedback now. You have five minutes. Think about what you'll do differently in your next entry, which you'll write today."

*Do not announce Git Episodes here. That announcement competes with the feedback for attention, and students will retain neither. Git Episodes are introduced in Segment C (2:25), where they have space and an actionable context.*

### 0:07--0:18 | Vocabulary Pre-Training
**Format:** Instructor-led, interactive, then pair confirmation
**Language skills:** Academic vocabulary building

**5 terms:** data, formula, interpret, verify, chart

Display a spreadsheet on the projector with data visible (e.g., a class survey with 20 rows of responses: favourite food, hours of sleep, commute time).

For each term:
1. **Data:** "Information collected about something. These numbers are data. The survey collected data about sleep, food, and commuting. When you work with AI, you'll hear 'data' constantly. Data can be numbers, text, dates -- anything you can organize."
2. **Formula:** "An instruction that tells the spreadsheet to calculate something. This formula adds up all the numbers in this column. The formula does the math; you decide what question to ask." Show `=AVERAGE(B2:B21)` and explain in plain language: "This formula calculates the average -- the middle number."
3. **Interpret:** "To explain what something means. When you read this spreadsheet and say 'most people sleep 7 hours,' you are interpreting the data. When you read an error message and say 'it means the file is missing,' you are interpreting. You've been interpreting AI output since Week 2."
4. **Verify:** "To check whether something is correct. When Copilot writes a formula, you verify it by doing one calculation yourself. We've been talking about verification since the beginning. Today we'll verify numbers."
5. **Chart:** "A picture of data. It shows patterns you can't see in a table. This chart shows that most people sleep 6–8 hours." Point to a bar chart derived from the data.

Introduce **cell**, **row**, and **column** by pointing: "This box is a cell -- one piece of information. This row goes across -- it's one person's answers. This column goes down -- it's one question. You can see what they mean by looking."

**Pair confirmation** (2 min): Display a blank spreadsheet screenshot (no data, just the grid with one formula visible and one chart). Pairs label it together: point to the formula, the chart, a cell. Then: "Tell your partner: what does 'interpret' mean? What does 'verify' mean? Use your own words."

*This confirmation step ensures terms have landed before the worked example. If pairs struggle with "interpret" or "verify," the instructor knows before proceeding.*

### 0:18--0:40 | Worked Example: Reading Before Building
**Format:** Instructor demonstration with student interaction
**Language skills:** Listening, reading (spreadsheet data, formulas, charts), critical evaluation

**This sequence is critical: reading first, then building.** Students need to interpret existing spreadsheets before they create their own. Most people encounter spreadsheets others have made, not blank ones.

**Part 1 -- Reading an existing spreadsheet (14 min):**

Instructor displays a finished spreadsheet someone else made: class survey results with 20 rows of data, several formulas, and a chart. The data is simple and relatable (e.g., favourite food, hours of sleep, commute time in minutes).

"Someone made this. Before we build anything, let's read it."

Interactive reading:
- "What does this spreadsheet show? What was the survey about?" (Students answer.)
- Point to a formula: `=AVERAGE(C2:C21)`. "What does this formula do? We learned 'average' a minute ago. It's calculating the average of column C. What's in column C? So what number should we expect?" Students estimate. Compare with the actual result.
- Point to a chart (bar chart of favourite foods). "What does this chart show? Which food is most popular? Does the chart match the data in the table?" Students check by scanning the column.
- Point to a suspicious number: the commute time average says 847 minutes. "Is this number right? That's 14 hours of commuting. Something is wrong." Students look at the data, find the outlier (one person typed 800 instead of 80). "One outlier changes the average. The formula is correct. The data is wrong. The chart looks fine. But the answer is wrong. How would you know if you didn't check?"

"The spreadsheet said the answer was correct. But what was actually there? When you check the number yourself -- on paper, on your phone calculator -- you find out what's actually there. The spreadsheet doesn't care if the answer looks wrong."

"Reading a spreadsheet means checking three things: Is the formula doing what you think? Is the data correct? Does the chart match the data?"

**Part 2 -- Building with Copilot (8 min):**

Instructor creates a new sheet. "Now let's build something. I want a summary of the sleep data."

- "Copilot, calculate the average sleep hours from this column."
- Formula appears. "But I don't just accept this. Let me check." Uses the "explain this" approach: "Copilot, what does this formula do?" Reads the explanation.
- Verifies manually: "The first five values are 7, 6, 8, 7, 9. That's 37 divided by 5 -- about 7.4. The formula says 7.2 for all 20. That's in the right range. I trust it."
- "Now make a chart showing how many people sleep 6, 7, 8 hours." Chart appears.
- Checks: "Does this chart match what I see in the column?" Quick scan confirms.

"The cycle is the same as with documents: tell AI what you want, check what you get, verify. But with numbers, verification means doing at least one calculation yourself."

---

## Segment B: Planning + Guided Practice (0:40--1:35)

### 0:40--0:45 | Pre-Task Planning
**Format:** Individual reflection

Two prompts, both on screen:

1. **DL feedback re-activation** (1 min): "Look at your Decision Log feedback again. Read the improvement target. You're writing a new entry today. What will you do differently?"

2. **Data schema activation** (3 min): "What data do you encounter in your life? A budget? Grades? A work schedule? A phone bill? What questions would you want answered?" Students jot 2-3 notes. These notes feed directly into the Goal Document in Segment C.

### 0:45--0:48 | File-Access Checkpoint + Domain Orientation
**Format:** Whole class

"Open the spreadsheet I've shared. Raise your hand when you see data on your screen."

Wait until all hands are up. Help students who are stuck (wrong browser, not logged in, file opens in desktop app). This prevents 3-5 students from losing the first 5 minutes of the reading task to file-access friction.

Once everyone has the file open: "This is a student's monthly budget. The rows are months. The columns are categories: rent, food, transport, phone, other. The formulas calculate totals and averages. The chart shows spending over time. Now let's read it."

*Note: two variants of this dataset are distributed (Variant A and Variant B). Same structure, same column types, but different numbers and different planted errors. Partners get different variants. This creates a genuine information gap when they compare answers.*

### 0:48--1:08 | Reading Comprehension: Jigsaw Spreadsheets
**Format:** Individual, then pair jigsaw
**Language skills:** Reading (spreadsheet data, formulas), writing (short answers), speaking (explaining findings)

Students answer 3 questions about their variant (written answers, 1-2 sentences each):
1. "What does this spreadsheet track? Who would use it?"
2. "Look at the formula in cell [X]. What does it calculate? Is the answer reasonable?"
3. "Look at the chart. What does it show? Does it match the data in the table?"

**Pair jigsaw** (8 min): Partners have different variants. Each explains what they found:
- "What errors or problems did you find in your spreadsheet?"
- "What does your formula calculate? Does mine do the same thing?"
- "Did anything in your data look wrong? How did you know?"

Each partner has information the other does not have. The listener must evaluate a claim they cannot independently verify -- this is genuine communicative work.

### 1:08--1:25 | Building: Summary + Chart with Copilot
**Format:** Individual with instructor circulation
**Language skills:** Writing (prompts for AI), reading (AI output, formulas), critical evaluation

Using their variant dataset, students build:
1. A new summary calculation using Copilot ("What's the total? What's the average? What's the highest?")
2. A chart that shows something meaningful from the data

Then verify:
- "Copilot, what does this formula do?" Read the explanation.
- Check one calculation manually (calculator, mental math, or count by hand)
- Look at the chart: "Does this match the data? Is anything misleading?"

**Stretch option for fast finishers:** "Ask Copilot: 'What patterns do you notice in this data?' See if it finds something you didn't notice. Do you agree with what it says?"

**Copilot fallback:** If Copilot is unavailable on a student's device, they type the formula manually (e.g., `=AVERAGE(B2:B13)`). The skill being assessed is verification, not formula generation.

Instructor circulates:
- "What did you ask Copilot to calculate? What formula did it write?"
- "Can you explain in your own words what this formula does?"
- "Did you check the answer? How?"
- "What does your chart show? Does it match the numbers?"

### 1:25--1:30 | Naming the Error
**Format:** Whole class, then individual

"Before you write your Decision Log entry, let's name what went wrong. Errors come in types."

Display:

| Error type | Example from today |
|-----------|-------------------|
| **Calculation error** | Formula divides by 30 instead of 28 |
| **Vague description** | Chart title says "Data" instead of "Monthly Spending by Category" |
| **Wrong format** | AI made a pie chart when a bar chart would be clearer |
| **Missing information** | No axis labels, no units on the numbers |

"Look at your spreadsheet work. What kind of error did AI make? Name it. When you write your Decision Log entry, include the error type."

This is the first time students classify AI failures by type, not just by outcome. Over the semester, they build a mental model of how AI breaks.

### 1:30--1:35 | Decision Log Entry
**Format:** Individual writing
**Language skills:** Writing (structured documentation, evaluative)

Students write a Decision Log entry about their spreadsheet work. Template on screen.

Focus: What did I ask Copilot to do? What did it produce? How did I check it? Was the result correct? What type of error did AI make?

"This is your first Decision Log entry since getting feedback. You re-read your improvement target at the start of Segment B. Address it in this entry. I'll be looking for it."

---

## Break (1:35--1:50)

---

## Segment C: Goal Document + Session Review + Git Episodes (1:50--2:45)

### 1:50--2:10 | Goal Document + Data Exploration
**Format:** Individual writing, then pair discussion
**Language skills:** Writing (conditional, planning), speaking (describing data ideas, asking questions)

"Think about your project. Some of you are thinking about data -- budgets, schedules, tracking something. Some of you aren't. Both are fine. The question is: what decision in your project could be informed by numbers, even if you haven't collected them yet?"

**Prompt** (displayed): "What decision in your project (or your life) could be informed by numbers? What would you need to organize and show? If nothing, what surprised you about working with data today?"

**Sentence frames** (displayed):
- "My project involves data about _____. I would want to show _____."
- "A spreadsheet would help me _____ because _____."
- "I didn't expect _____ about working with data today."

**Writing** (10 min): Students write entry 6 in their Goal Document. The language demand continues the Phase 2 pattern: conditional reasoning ("If my project involves..."), justification ("because"), and connecting today's challenge to their evolving project direction.

**Pair discussion** (10 min): Partners read each other's Goal Document entries. Discussion prompts merge the data exploration that was previously a separate segment:
- "Does your partner's project involve data? What kind?"
- "What data do you encounter in your life? If you could organize it in a spreadsheet, what questions would you ask?"
- "What question would a spreadsheet answer for your partner?"
- "Did today change your thinking about your own project?"

### 2:10--2:12 | Bridging Activity
**Format:** Individual, silent

"In two minutes, you'll explain your spreadsheet work to AI. Before you open voice mode, do this: look at your spreadsheet from Segment B. Pick one change you made -- one formula, one chart, one fix. Rehearse in your head: what did you change, and why?"

*This bridges the register shift from reflective Goal Document writing to confrontational session review. Students retrieve specific content and switch from reflective to explanatory mode before the voice interaction begins.*

### 2:12--2:25 | Session Review (Speaking Practice)
**Format:** Individual, AI voice mode
**Language skills:** Speaking (justifying a change, responding to follow-up questions)

"Open your AI tool and start a new chat. Say or paste this prompt."

**Role-setting prompt** (on slide): "Speaking practice. I'm a B1 English student practising explaining my work. Ask me follow-up questions. If my explanation is vague, tell me what's unclear and ask me to be more specific. Don't do the explaining for me."

**This week's scenario** (on slide): "You made a change to a shared spreadsheet. Explain what you changed and why to someone who needs to review your work."

AI role: Teammate reviewing your work.

Students talk to AI for 10-12 minutes, explaining what they did with the spreadsheet -- what they found in the reading comprehension task, what formula they built, what they verified. The AI pushes back when the explanation is vague.

"The AI is playing your teammate. Your teammate can reject your change if you don't explain it well enough. Be specific."

Instructor circulates and listens. No intervention unless a student is stuck or silent. This is production practice, not instruction.

**Note:** Voice mode starts a new chat. Students cannot paste work into the conversation and then switch to voice. The prompt is said aloud or pasted at the start, then the conversation is entirely spoken.

### 2:25--2:35 | Git Episodes Introduction
**Format:** Whole class, instructor-led
**Language skills:** Reading (documentation example), listening

"Starting this week, you can formally document your Git Episodes. You need three by Week 12: a Restore, an Error Recovery, and a Collaboration."

Show one concrete example of a documented Restore episode on the projector:

> **Episode: Restore**
> **Date:** Week 5
> **What happened:** I was fixing accessibility in my document. I accidentally deleted the table of contents. I used `git restore` to get the previous version back.
> **Evidence:** [screenshot of git log showing the restore command and the two commits]

"This is what a documented episode looks like. You need the story (what happened) and the evidence (a screenshot or a log). Some of you already did a restore in Week 5. If so, you can write it up like this."

Display the three required episodes:
- **Restore:** Recover an earlier version of a file
- **Error Recovery:** Something broke, you diagnosed it, you fixed it
- **Collaboration:** A pull request with a description and one comment exchange

"You have from now until Week 12. These will happen naturally as you work. When something goes wrong or you collaborate, document it."

### 2:35--2:45 | Closing
**Format:** Whole class

- "Today you practised reading numbers before making them. That matters. Most spreadsheets you'll encounter in your life were made by someone else. The first skill is understanding what's already there."
- "The second skill is checking. A formula can be correct and still give a wrong answer if the data is wrong. An outlier -- one wrong number -- changed the average from 45 minutes to 847 minutes. Verification isn't optional."
- "You got your Decision Log feedback today. Your entry from today should show that you read it. I'll be looking for that."
- "Next week: working together. You've been building things individually. What happens when two people need to work on the same thing?"
- Remind: "Your portfolio repository should have your recent work committed. If you haven't pushed lately, do it before next class."

---

## After Class

- **Review Decision Log entries** written this week: Are students incorporating feedback from round 1? Note patterns for round 2 feedback.
- **Note which students demonstrated data interpretation skills** during the reading comprehension task (useful for tracking CLO 6 development).
- **Track Git episode activity:** Students may begin documenting episodes from this week forward (due Week 12). Note any students who mentioned restores during Segment C.
- **Listen for session review patterns:** Were students able to justify their spreadsheet changes? Did the AI push them to be specific? Note any students who were silent or struggled -- consider pairing them with a partner next week before going to voice.

---

## Instructor Prep Checklist

- [ ] Decision Log feedback (entries 1-2) printed or shared digitally -- one strength + one improvement target per student
- [ ] Survey results spreadsheet prepared for worked example (20 rows, relatable data, 2-3 formulas, 1 chart, one deliberate data error for the "Is this number right?" moment)
- [ ] **Two variants** of the practice dataset prepared and shared (same structure/domain, different data and different planted errors; e.g., Variant A has an outlier in the rent column, Variant B has a formula referencing the wrong range). Distribute so partners get different variants.
- [ ] Domain orientation prepared: know the 2-sentence description of the practice dataset ("This is a student's monthly budget. The rows are months...")
- [ ] Copilot in Excel confirmed working on student devices; **fallback plan:** students who cannot access Copilot type formulas manually (=AVERAGE, =SUM). The skill is verification.
- [ ] Vocabulary slides: data, formula, interpret, verify, chart (cell/row/column introduced by pointing during worked example)
- [ ] Blank spreadsheet screenshot for pair vocabulary confirmation task (grid with one formula, one chart -- no data; pairs label and define "interpret" and "verify" in own words)
- [ ] Goal Document prompt + sentence frames on slide
- [ ] Decision Log template accessible to students
- [ ] Verification approach prepared: know one calculation you'll do manually in the worked example
- [ ] Reading comprehension questions prepared for the practice spreadsheet (3 questions, same for both variants)
- [ ] Session review slide: role-setting prompt + Week 6 scenario ("You made a change to a shared spreadsheet...")
- [ ] Git Episodes slide: 3 required episodes (Restore, Error Recovery, Collaboration), due Week 12, with one modelled documentation example
- [ ] Git Episodes documentation example prepared (screenshot of a git log + 3-sentence write-up)

## Language Development Summary

- **Vocabulary:** 5 AWL terms (data, formula, interpret, verify, chart) pre-trained in Segment A with pair confirmation task; cell, row, and column introduced contextually by pointing during worked example. "Interpret" and "verify" are high-transfer terms that connect back to Weeks 2-5 and forward to all AI evaluation work. "Average" and "outlier" are taught through the worked example content (not formal vocabulary items).
- **Speaking:** Pair jigsaw in Segment B (explaining findings from a spreadsheet your partner hasn't seen -- genuine information gap); pair Goal Document + data exploration discussion; **session review** (12 min sustained AI voice interaction: justifying a change to a teammate who can reject it -- the first scenario requiring justification to someone with authority)
- **Reading:** Existing spreadsheet (data, formulas, charts -- reading comprehension applied to a structured data format); AI-generated formulas; Copilot explanations of formulas; partner's Goal Document entry; **Decision Log feedback from instructor** (reading and interpreting evaluative comments); Git Episode documentation example
- **Writing:** Reading comprehension answers (3 short responses); Decision Log entry (~150-200 words, incorporating round 1 feedback); Goal Document entry (~75-100 words, conditional and planning language)
- **Listening:** Vocabulary pre-training; worked example narration (reading then building); partner's jigsaw explanation of their spreadsheet variant; partner's Goal Document + data exploration discussion; AI follow-up questions during session review; Git Episodes introduction

## Assessment Alignment

- **CLO 6 continues** (produce digital products -- spreadsheet interpretation and creation)
- **CLO 3 continues** (guide AI tools -- prompting Copilot to build formulas and charts)
- **CLO 4 continues** (evaluate AI text -- verifying formulas and checking charts against data)
- **Decision Log entry** (part of 30% component): First entry after round 1 feedback; instructor should track whether feedback is being incorporated
- **Decision Log feedback round 1 returned** (entries 1-2): One strength + one improvement target per student
- **Git Episodes formally eligible** starting this week (10% component, due Week 12): Students can begin documenting Restore, Error Recovery, and Collaboration episodes. Documentation format modelled in Segment C.
- **Session review** (formative, not graded): Week 6 scenario practises justifying changes -- builds toward Micro-Defence 2 (Week 8, 5 criteria) where students must show what was tried and interpret errors
- **Goal Document updated** (ungraded; instructor reads at Week 8)
