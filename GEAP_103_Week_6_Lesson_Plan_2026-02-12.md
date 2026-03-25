# GEAP 103 Week 6 Lesson Plan: Making Sense of Numbers

**Context:** 3 x 55 min (150 min instruction + 15-min break), B1 learners, BYOD, Office 365 + Copilot
**Week 6 of 14** | Phase 2: Building

**Learning Objectives (Week 6):**
1. Read and interpret an existing spreadsheet: understand what formulas calculate and what charts show (CLO 6)
2. Use Copilot to build a summary and chart from a dataset, then verify one formula manually (CLO 3, 4)
3. Explain in own words what a formula does and whether a chart accurately represents the data
4. Connect data skills to personal project direction in the Goal Document

**New vocabulary (5):** cell, row, column, formula, chart

**Goal Thread -- Technical Scoping (continued):**
Students continue developing planning language by connecting the week's challenge to their own project. Whether or not their project involves data, they practise describing what they would need and why. The conditional language from Week 5 ("The user might need...") extends this week to reasoning about data: "If I want to show..., I would need to organize..." This is the same planning-and-justifying complexity level, applied to a new domain.

---

## Segment A: Vocabulary + Worked Example (0:00--0:40)

### 0:00--0:10 | Vocabulary Pre-Training
**Format:** Instructor-led, interactive
**Language skills:** Academic vocabulary building

**5 terms:** cell, row, column, formula, chart

Display a spreadsheet on the projector with data visible (e.g., a class survey with 20 rows of responses: favourite food, hours of sleep, commute time).

For each term:
1. **Cell:** "One box. It holds one piece of information. This cell says 'pizza.' This cell says '7 hours.'" Point to specific cells.
2. **Row:** "A horizontal line of cells. Each row is one person's answers." Highlight a row.
3. **Column:** "A vertical line of cells. Each column is one question." Highlight a column.
4. **Formula:** "An instruction that tells the spreadsheet to calculate something. This formula adds up all the numbers in this column. The formula does the math; you decide what question to ask." Show `=AVERAGE(B2:B21)` and explain in plain language.
5. **Chart:** "A picture of numbers. It shows patterns you can't see in a table. This chart shows that most people sleep 6-8 hours." Point to a bar chart derived from the data.

Quick check: "How many rows of data are there? Which column has the sleep hours? What does this formula calculate?" Volunteers answer.

### 0:10--0:35 | Worked Example: Reading Before Building
**Format:** Instructor demonstration with student interaction
**Language skills:** Listening, reading (spreadsheet data, formulas, charts), critical evaluation

**This sequence is critical: reading first, then building.** Students need to interpret existing spreadsheets before they create their own. Most people encounter spreadsheets others have made, not blank ones.

**Part 1 -- Reading an existing spreadsheet (15 min):**

Instructor displays a finished spreadsheet someone else made: class survey results with 20 rows of data, several formulas, and a chart. The data is simple and relatable (e.g., favourite food, hours of sleep, commute time in minutes).

"Someone made this. Before we build anything, let's read it."

Interactive reading:
- "What does this spreadsheet show? What was the survey about?" (Students answer.)
- Point to a formula: `=AVERAGE(C2:C21)`. "What does this formula do? It's calculating the average of column C. What's in column C? So what number should we expect?" Students estimate. Compare with the actual result.
- Point to a chart (bar chart of favourite foods). "What does this chart show? Which food is most popular? Does the chart match the data in the table?" Students check by scanning the column.
- Point to a suspicious number: the commute time average says 847 minutes. "Is this number right?" Students look at the data, find an outlier (one person typed 800 instead of 80). "One wrong number changes the average. The formula is correct. The data is wrong. The chart looks fine. But the answer is wrong. How would you know if you didn't check?"

"Reading a spreadsheet means checking three things: Is the formula doing what you think? Is the data correct? Does the chart match the data?"

**Part 2 -- Building with Copilot (10 min):**

Instructor creates a new sheet. "Now let's build something. I want a summary of the sleep data."

- "Copilot, calculate the average sleep hours from this column."
- Formula appears. "But I don't just accept this. Let me check." Uses the "explain this" approach: "Copilot, what does this formula do?" Reads the explanation.
- Verifies manually: "The first five values are 7, 6, 8, 7, 9. That's 37 divided by 5 -- about 7.4. The formula says 7.2 for all 20. That's in the right range. I trust it."
- "Now make a chart showing how many people sleep 6, 7, 8 hours." Chart appears.
- Checks: "Does this chart match what I see in the column?" Quick scan confirms.

"The cycle is the same as with documents: tell AI what you want, check what you get, verify. But with numbers, verification means doing at least one calculation yourself."

### 0:35--0:40 | Connect to the Practice
**Format:** Instructor-led

- "Now it's your turn. You'll get a dataset -- someone else's spreadsheet. First you'll read it. Then you'll build something from it. And you'll check your own work."
- "Think about this: what data do you encounter in your life? A budget? Grades? A work schedule? What questions would you want to ask that data?"

---

## Segment B: Planning + Guided Practice (0:40--1:35)

### 0:40--0:45 | Pre-Task Planning
**Format:** Individual reflection

"What data do you encounter in your life? A budget? Grades? A work schedule? A phone bill? What questions would you want answered?"

Students jot 2-3 notes: What data have I seen recently? What did I want to know from it? (This connects the practice to their lives and, later, to their project direction.)

### 0:45--1:05 | Reading Comprehension: An Existing Spreadsheet
**Format:** Individual, then pair check
**Language skills:** Reading (spreadsheet data, formulas), writing (short answers)

Instructor distributes a dataset via OneDrive or LMS: a spreadsheet with 15-20 rows of realistic data (e.g., a student's monthly budget with categories, amounts, and dates; or a grade tracker with assignments, scores, and weights). The spreadsheet includes 2-3 formulas and one chart already built.

Students answer 3 questions about the existing spreadsheet (written answers, 1-2 sentences each):
1. "What does this spreadsheet track? Who would use it?"
2. "Look at the formula in cell [X]. What does it calculate? Is the answer reasonable?"
3. "Look at the chart. What does it show? Does it match the data in the table?"

Pairs compare answers: "Did you get the same thing? Where do you disagree?"

This is a reading comprehension task. The spreadsheet is the text. The questions check whether students can extract meaning from a structured data format, the same skill they use when reading any unfamiliar document.

### 1:05--1:25 | Building: Summary + Chart with Copilot
**Format:** Individual with instructor circulation
**Language skills:** Writing (prompts for AI), reading (AI output, formulas), critical evaluation

Using the same dataset, students build:
1. A new summary calculation using Copilot ("What's the total? What's the average? What's the highest?")
2. A chart that shows something meaningful from the data

Then verify:
- "Copilot, what does this formula do?" Read the explanation.
- Check one calculation manually (calculator, mental math, or count by hand)
- Look at the chart: "Does this match the data? Is anything misleading?"

Instructor circulates:
- "What did you ask Copilot to calculate? What formula did it write?"
- "Can you explain in your own words what this formula does?"
- "Did you check the answer? How?"
- "What does your chart show? Does it match the numbers?"

### 1:25--1:35 | Decision Log Entry
**Format:** Individual writing
**Language skills:** Writing (structured documentation, evaluative)

Students write a Decision Log entry about their spreadsheet work. Template on screen.

Focus: What did I ask Copilot to do? What did it produce? How did I check it? Was the result correct?

"Remember the feedback you got on your first entries. What did your instructor say to improve? Try to apply that here."

This is the first DL entry students write after receiving round 1 feedback. Instructor should note (when reviewing later) whether students have incorporated the improvement targets from entries 1-2.

---

## Break (1:35--1:50)

---

## Segment C: Application + Goal Document (1:50--2:45)

### 1:50--2:10 | Pair Data Exploration
**Format:** Pair work
**Language skills:** Speaking (explaining data, asking questions), listening, reading (partner's spreadsheet)

"Tell your partner about the data you thought of during planning. What data do you encounter in your life? If you could organize it in a spreadsheet, what questions would you ask?"

Each partner describes their data idea (3 min each). Then pairs work together:
- Choose one partner's data idea (the simpler one, or the one they have more information about)
- Sketch a quick spreadsheet structure on paper or in Excel: What are the columns? What are the rows? What formula would answer the question?
- If time, start entering sample data and build a formula with Copilot

This connects spreadsheet skills to each student's personal interests and project direction. Students who already know their project involves data get to start working with real content. Students whose projects don't involve data still practise the skill with personally relevant information.

### 2:10--2:35 | Goal Document
**Format:** Individual writing, then pair discussion
**Language skills:** Writing (conditional, planning, connecting challenge to project)

"Think about your project. Some of you are thinking about data -- budgets, schedules, tracking something. Some of you aren't. Both are fine. The question is: what would data be useful for in your life or your project?"

**Prompt** (displayed): "Think about your project. If it involves numbers or data, what would you need to organize and show? If it doesn't, what data from your life would be useful to have in a spreadsheet?"

**Sentence frames** (displayed):
- "My project involves data about _____. I would want to show _____."
- "A spreadsheet would help me _____ because _____."
- "I don't need data for my project, but I could use a spreadsheet to _____."

**Writing** (10 min): Students write entry 6 in their Goal Document. The language demand continues the Phase 2 pattern: conditional reasoning ("If my project involves..."), justification ("because"), and connecting today's challenge to their evolving project direction.

**Pair discussion** (15 min): Partners read each other's Goal Document entries. Discussion prompts:
- "Does your partner's project involve data? What kind?"
- "What question would a spreadsheet answer for your partner?"
- "Did today change your thinking about your own project?"

### 2:35--2:45 | Closing
**Format:** Whole class

- "Today you practised reading numbers before making them. That matters. Most spreadsheets you'll encounter in your life were made by someone else. The first skill is understanding what's already there."
- "The second skill is checking. A formula can be correct and still give a wrong answer if the data is wrong. A chart can look convincing and be misleading. Verification isn't optional."
- "Next week: working together. You've been building things individually. What happens when two people need to work on the same thing?"
- Remind: "Your portfolio repository should have your recent work committed. If you haven't pushed lately, do it before next class."

---

## After Class

- **Review Decision Log entries** written this week: Are students incorporating feedback from round 1? Note patterns for round 2.
- **Note which students demonstrated data interpretation skills** during the reading comprehension task (useful for tracking CLO 6 development)
- **Track Git episode eligibility:** Git episodes are now formally eligible for documentation (Weeks 6-14). Students who did a restore in Week 5 can begin writing up their Restore episode. Remind students at the start of Week 7.

---

## Instructor Prep Checklist

- [ ] Survey results spreadsheet prepared for worked example (20 rows, relatable data, 2-3 formulas, 1 chart, one deliberate data error for the "Is this number right?" moment)
- [ ] Practice dataset prepared and shared (different from worked example; 15-20 rows, 2-3 formulas, 1 chart, 3 reading comprehension questions)
- [ ] Copilot in Excel confirmed working on student devices (Copilot in Excel for web may have different capabilities; test in advance)
- [ ] Vocabulary slides: cell, row, column, formula, chart
- [ ] Goal Document prompt + sentence frames on slide
- [ ] Decision Log template accessible to students
- [ ] Verification approach prepared: know one calculation you'll do manually in the worked example
- [ ] Pair data exploration instructions on slide ("Describe your data idea to your partner")
- [ ] Reading comprehension questions prepared for the practice spreadsheet (3 questions, 1-2 sentences each)

## Language Development Summary

- **Vocabulary:** 5 terms (cell, row, column, formula, chart) pre-trained visually in Segment A using a real spreadsheet, applied in reading comprehension (Segment B) and building tasks (Segment B-C)
- **Speaking:** Pair comparison of reading comprehension answers; pair data exploration (describing personal data ideas, asking questions about partner's data); pair Goal Document discussion
- **Reading:** Existing spreadsheet (data, formulas, charts -- this is reading comprehension applied to a structured data format); AI-generated formulas; Copilot explanations of formulas; partner's Goal Document entry
- **Writing:** Reading comprehension answers (3 short responses); Decision Log entry (~150-200 words, incorporating round 1 feedback); Goal Document entry (~75-100 words, conditional and planning language)
- **Listening:** Vocabulary pre-training; worked example narration (reading then building); partner's data idea description; partner's Goal Document discussion

## Assessment Alignment

- **CLO 6 continues** (produce digital products -- spreadsheet interpretation and creation)
- **CLO 3 continues** (guide AI tools -- prompting Copilot to build formulas and charts)
- **CLO 4 continues** (evaluate AI text -- verifying formulas and checking charts against data)
- **Decision Log entry** (part of 30% component): First entry after round 1 feedback; instructor should track whether feedback is being incorporated
- **Git Episodes formally eligible** starting this week (10% component): Students can begin documenting Restore, Error Recovery, and Collaboration episodes
- **Goal Document updated** (ungraded; instructor reads at Week 8)
