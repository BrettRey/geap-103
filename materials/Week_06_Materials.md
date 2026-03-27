# GEAP 103 Week 6: Instructor Materials Package

**Title:** Making Sense of Numbers
**Phase:** Building (Week 6 of 14)
**Contact time:** 3 x 55 min (165 min total: 150 min instruction + 15 min break)
**Date prepared:** 2026-03-27

This file contains everything you need to prepare slides and run the class for Week 6. The lesson plan (`lesson-plans/week-06.md`) has the pedagogical rationale. This file has the concrete content. In case of conflict between this materials package and the lesson plan for Week 6, this materials package governs (it reflects March 2026 design revisions). For anything not covered here, the lesson plan governs.

**Week 6 design note:** This is the second Building phase week. Students shift from making things accessible (Week 5) to reading and building with data. The core principle: reading before building. Most people encounter spreadsheets someone else made, not blank ones. The first skill is understanding what's already there. The second skill is verification -- checking whether a formula is doing what you think and whether the data is correct. AI writes formulas; the student decides what to ask for and checks whether the answer is right.

**Two milestones this week:** Decision Log feedback round 1 is returned (entries 1-2), and Git Episodes become formally eligible for documentation. DL feedback is returned at the start of class; Git Episodes are introduced in Segment C, where they have space and a concrete documentation example.

**New vocabulary (5 AWL terms):** data, formula, interpret, verify, chart

**AI tools:** Same tool-agnostic approach. Students use Copilot (or any AI) to generate formulas and charts. The skill being practised is verification: checking whether the formula does what you think, whether the data is correct, and whether the chart matches the data.

---

## Before Class

### Materials to Prepare

| Material | Description | How to share |
|----------|-------------|-------------|
| **Survey results spreadsheet** | Worked example: 20 rows of class survey data (favourite food, hours of sleep, commute time). 2-3 formulas. 1 bar chart. **One deliberate data error:** one person typed 800 instead of 80 for commute time, producing an average of 847 minutes. | Display on projector only |
| **Practice dataset Variant A** | Student monthly budget. Rows = months, columns = categories (rent, food, transport, phone, other). 15-20 rows. 2-3 formulas. 1 chart. **Planted error:** an outlier in the rent column (e.g., $12,000 instead of $1,200). | Share via OneDrive or Blackboard |
| **Practice dataset Variant B** | Same structure and domain as Variant A, but different numbers. **Planted error:** a formula referencing the wrong column range (e.g., =AVERAGE of the "other" column instead of "food"). | Share via OneDrive or Blackboard |
| **Blank spreadsheet screenshot** | Empty grid with one formula visible and one chart. For the vocabulary pair confirmation task. | Display on slide |
| **Git Episode documentation example** | Screenshot of a git log showing a restore, plus a 3-sentence write-up. | Display on slide in Segment C |

**Dataset distribution:** Assign Variant A to half the class and Variant B to the other half. Partners should get different variants. This creates a genuine information gap when they compare findings.

**Tip:** The practice dataset works best if it uses a domain students recognise. A student's monthly budget is relatable; a corporate sales pipeline is not. Both variants should use the same domain so the pair comparison is meaningful.

### Decision Log Feedback

Decision Log feedback (entries 1-2) must be returned this week. Each entry gets one strength and one specific improvement target. Print or share digitally before class.

---

## Segment A: Feedback Return + Vocabulary + Worked Example (0:00-0:40)

### DL Feedback Return (0:00-0:07)

Distribute Decision Log feedback as students arrive.

> "I've returned your first two Decision Log entries with feedback. Read them now -- you have five minutes. Each entry has one thing you did well and one thing to improve. Think about what you'll do differently, because you're writing a new entry today."

Students read silently. Do not add other announcements here -- let the feedback have the students' full attention.

---

### Vocabulary (0:07-0:18)

**Vocabulary reference slide** (display and leave up):

| Term | Meaning |
|------|---------|
| **data** | Information collected about something -- numbers, text, dates, anything you can organize |
| **formula** | An instruction that tells the spreadsheet to calculate something -- the formula does the math, you decide what question to ask |
| **interpret** | To explain what something means -- when you read a chart and say "most people sleep 7 hours," you are interpreting |
| **verify** | To check whether something is correct -- when AI writes a formula, you verify it by doing one calculation yourself |
| **chart** | A picture of data -- it shows patterns you can't see in a table |

**Teach these in context, not in isolation.** Display the survey results spreadsheet and use it for every term:

1. **Data:** Point to the spreadsheet.

   > "Information collected about something. These numbers are data. The survey collected data about sleep, food, and commuting. When you work with AI, you'll hear 'data' constantly. Data can be numbers, text, dates -- anything you can organize."

2. **Formula:** Point to `=AVERAGE(B2:B21)`.

   > "An instruction that tells the spreadsheet to calculate something. This formula adds up all the numbers in this column and divides by how many there are. That gives you the average -- the middle number. The formula does the math; you decide what question to ask."

3. **Interpret:** Point to the chart.

   > "To explain what something means. When you look at this chart and say 'most people sleep 7 hours,' you are interpreting the data. When you read an error message and say 'it means the file is missing,' you are interpreting. You've been interpreting AI output since Week 2."

4. **Verify:** Point to the formula result.

   > "To check whether something is correct. The formula says the average is 7.2 hours. I can verify that by adding up a few numbers myself. When Copilot writes a formula, you verify it. We've been talking about verification since Week 2. Today we verify numbers."

5. **Chart:** Point to the bar chart.

   > "A picture of data. It shows patterns you can't see in a table. This chart shows that most people sleep 6-8 hours. But a chart can look convincing and be misleading. You have to check."

Introduce **cell**, **row**, and **column** by pointing:

> "This box is a cell -- one piece of information. This row goes across -- it's one person's answers. This column goes down -- it's one question. You can see what they mean by looking."

**Pair confirmation** (2 min): Display the blank spreadsheet screenshot. Pairs label it together: point to the formula, the chart, a cell. Then:

> "Tell your partner: what does 'interpret' mean? What does 'verify' mean? Use your own words, not the slide."

Quick check: 1-2 volunteers define "interpret" and "verify" aloud. If students struggle, re-explain before proceeding.

---

### Worked Example: Reading Before Building (0:18-0:40)

Display the survey results spreadsheet on the projector.

**Part 1 -- Reading an existing spreadsheet** (14 min):

> "Someone made this spreadsheet. Before we build anything, let's read it."

Interactive reading -- ask students, don't lecture:

| What to display | What to ask |
|----------------|------------|
| The whole spreadsheet | "What does this spreadsheet show? What was the survey about?" (Students answer.) |
| Point to `=AVERAGE(C2:C21)` | "What does this formula do? We just learned 'formula' and 'average.' It's calculating the average of column C. What's in column C? So what number should we expect?" Students estimate. Compare with the actual result. |
| Point to the bar chart | "What does this chart show? Which food is most popular? Does the chart match the data in the table?" Students check by scanning the column. |
| Point to the commute time average: 847 minutes | "Is this number right? That's 14 hours of commuting. Is that reasonable?" |

Wait for students to react to 847 minutes. Then:

> "Let's find the problem. Look at the commute column. Does anything look wrong?"

Students scan and find the outlier: 800 instead of 80.

> "One wrong number changes the average. The formula is correct. The data is wrong. The chart looks fine. But the answer is wrong. How would you know if you didn't check? This is why we verify."

Summarize:

> "Reading a spreadsheet means checking three things: Is the formula doing what you think? Is the data correct? Does the chart match the data?"

**Part 2 -- Building with Copilot** (8 min):

Create a new sheet on the projector.

> "Now let's build something. I want a summary of the sleep data."

| Action | Think-aloud |
|--------|-------------|
| "Copilot, calculate the average sleep hours from this column." | Formula appears. "But I don't just accept this. Let me check." |
| "Copilot, what does this formula do?" | Read the explanation aloud. "OK, that matches what I asked for." |
| Manual check | "The first five values are 7, 6, 8, 7, 9. That's 37 divided by 5 -- about 7.4. The formula says 7.2 for all 20. That's in the right range. I trust it." |
| "Now make a chart showing how many people sleep 6, 7, 8 hours." | Chart appears. "Does this chart match what I see in the column?" Quick scan confirms. |

> "The cycle is the same as with documents: tell AI what you want, check what you get, verify. But with numbers, verification means doing at least one calculation yourself."

---

## Segment B: Planning + Guided Practice (0:40-1:35)

### Pre-Task Planning (0:40-0:45)

Two prompts, both on slide:

> 1. **DL feedback re-activation (1 min):** Look at your Decision Log feedback again. Read the improvement target. You're writing a new entry today. What will you do differently?
>
> 2. **Data schema activation (3 min):** What data do you encounter in your life? A budget? Grades? A work schedule? A phone bill? What questions would you want answered? Jot 2-3 notes.

---

### File-Access Checkpoint + Domain Orientation (0:45-0:48)

> "Open the spreadsheet I've shared. Raise your hand when you see data on your screen."

Wait until all hands are up. Help students who are stuck (wrong browser, not logged in, file opens in desktop app instead of web, Excel Online loads slowly on old laptops). Do not start the reading task until everyone has the file open.

Once everyone is ready:

> "This is a student's monthly budget. The rows are months. The columns are categories: rent, food, transport, phone, other. There are formulas that calculate totals and averages, and a chart that shows spending over time. Your partner has a different version of this budget -- same structure, different numbers, different problems. Now let's read it."

---

### Reading Comprehension: Jigsaw Spreadsheets (0:48-1:08)

**Individual answers** (12 min): Display:

> Answer these 3 questions about your spreadsheet. Write 1-2 sentences each.
>
> 1. What does this spreadsheet track? Who would use it?
> 2. Look at the formula in cell [X]. What does it calculate? Is the answer reasonable?
> 3. Look at the chart. What does it show? Does it match the data in the table?

**Pair jigsaw** (8 min): Display:

> Your partner has a different version of this budget. Take turns:
>
> 1. What errors or problems did you find in your spreadsheet?
> 2. What does your formula calculate? Does your partner's do the same thing?
> 3. Did anything in your data look wrong? How did you know?
>
> Listen carefully -- your partner found different problems than you did.

**What to say while circulating:**

| What you see | What to say |
|-------------|------------|
| Student answered Q2 wrong (misidentified the formula) | "Read the formula aloud. What does each part mean? What column is it looking at?" |
| Student found the planted error | "Good. How did you know it was wrong? What made you suspicious?" |
| Student didn't find the planted error | "Look at [column]. Are all the numbers reasonable? Does anything look too high or too low?" |
| Pair discussion is superficial ("mine was fine") | "What formula did yours have? What does it calculate? Was the answer reasonable? Your partner's had a different problem." |
| Strong pair finishing early | "Can you explain to your partner what 'verify' means using your spreadsheet as an example?" |

---

### Building: Summary + Chart with Copilot (1:08-1:25)

Display:

> Using your spreadsheet, build two things with Copilot:
>
> 1. A new summary calculation ("What's the total? What's the average? What's the highest?")
> 2. A chart that shows something meaningful from the data
>
> Then verify:
> - "Copilot, what does this formula do?" Read the explanation.
> - Check one calculation manually (calculator, mental math, or count by hand)
> - Look at the chart: does it match the data?
>
> **If Copilot is unavailable:** Type the formula manually (e.g., `=AVERAGE(B2:B13)`, `=SUM(B2:B13)`). The skill is verification, not formula generation.

**Stretch option** (display for fast finishers):

> Done? Ask Copilot: "What patterns do you notice in this data?" See if it finds something you didn't notice. Do you agree with what it says?

**What to say while circulating:**

| What you see | What to say |
|-------------|------------|
| Student asking Copilot for a formula | "Good. When it appears, can you explain what it does in your own words?" |
| Student accepted formula without checking | "How do you know it's right? Do one calculation yourself." |
| Student's chart doesn't match data | "Look at the chart, then look at the column. Do the numbers match? What's different?" |
| Student using the stretch option | "What did Copilot say? Do you agree? How would you check?" |
| Student can't get Copilot to work | "Type the formula manually: `=AVERAGE(B2:B13)`. The skill today is checking the answer, not making AI write it." |

---

### Decision Log Entry (1:25-1:35)

Display:

> Write a Decision Log entry about your spreadsheet work today.
>
> | Field | Your answer |
> |-------|-------------|
> | **Task goal + constraints** | What were you trying to do with the spreadsheet? |
> | **AI used** | Which tool? (Copilot in Excel, ChatGPT, etc.) |
> | **Prompt snippet(s)** | What did you ask? (1-3 turns) |
> | **Output summary** | What did AI produce? |
> | **Decision** | Accept / Modify / Reject |
> | **Verification** | How did you check it? |
> | **What changed** | What did you do after checking? |
> | **Self-assessment** | Rate this entry: Excellent / Proficient / Developing / Insufficient. Why? |
>
> **Remember:** You re-read your DL feedback at the start of Segment B. Address your improvement target in this entry.

---

## Break (1:35-1:50)

---

## Segment C: Goal Document + Session Review + Git Episodes (1:50-2:45)

### Goal Document + Data Exploration (1:50-2:10)

> "Think about your project. Some of you are thinking about data -- budgets, schedules, tracking something. Some of you aren't. Both are fine."

**Prompt** (display):

> What decision in your project (or your life) could be informed by numbers? What would you need to organize and show? If nothing, what surprised you about working with data today?

**Sentence frames** (display):

> - "My project involves data about _____. I would want to show _____."
> - "A spreadsheet would help me _____ because _____."
> - "I didn't expect _____ about working with data today."

**Writing** (10 min): Students write entry 6 in their Goal Document.

**Pair discussion** (10 min): Partners read each other's entries. Display:

> - Does your partner's project involve data? What kind?
> - What data do you encounter in your life? If you could organize it in a spreadsheet, what questions would you ask?
> - What question would a spreadsheet answer for your partner?
> - Did today change your thinking about your own project?

---

### Bridging Activity (2:10-2:12)

> "In two minutes, you'll explain your spreadsheet work to AI. Before you open voice mode, do this: look at your spreadsheet from Segment B. Pick one change you made -- one formula, one chart, one fix. Rehearse in your head: what did you change, and why?"

Two minutes of silence. Students look at their work and prepare.

---

### Session Review -- Speaking Practice (2:12-2:25)

Display:

> **Open your AI tool. Start a new chat.**
>
> **First, say this (or paste it):**
> "Speaking practice. I'm a B1 English student practising explaining my work. Ask me follow-up questions. If my explanation is vague, tell me what's unclear and ask me to be more specific. Don't do the explaining for me."
>
> **Then, your task:** You made a change to a shared spreadsheet. Explain what you changed and why to someone who needs to review your work. AI is playing your teammate -- and your teammate can reject your change if you don't explain it well enough.
>
> Start with: "I made a change to the budget spreadsheet. I _____."

**Voice mode encouraged.** Remind students: voice mode starts a new chat. Paste the role-setting prompt first, then switch to speaking.

Students talk to AI for 10-12 minutes. Instructor circulates and listens. No intervention unless a student is stuck or silent.

**What to listen for:**

| What you hear | What it means |
|--------------|---------------|
| Student explains what they changed with specific details | Good production -- the justification skill is developing |
| Student says "I changed the thing" and AI pushes back | The system is working -- AI is demanding specificity |
| Student is silent | Approach quietly: "Start with one thing you did. What formula did you build?" |
| Student and AI are having a genuine back-and-forth | Let it run. This is the goal. |

---

### Git Episodes Introduction (2:25-2:35)

> "Starting this week, you can formally document your Git Episodes. You need three by Week 12."

Display the three required episodes:

> | Episode | What it is | What you need |
> |---------|-----------|---------------|
> | **Restore** | Recover an earlier version of a file | The story (what happened) + evidence (screenshot of git log) |
> | **Error Recovery** | Something broke, you diagnosed it, you fixed it | The story + the error message + what you did |
> | **Collaboration** | A pull request with a description and one comment exchange | The PR link or screenshot |

Show the modelled documentation example on the projector:

> **Episode: Restore**
> **Date:** Week 5
> **What happened:** I was fixing accessibility in my document. I accidentally deleted the table of contents. I used `git restore` to get the previous version back.
> **Evidence:** [screenshot of git log showing the restore command and the two commits]

> "This is what a documented episode looks like. You need the story -- what happened -- and the evidence -- a screenshot or a log. Some of you already did a restore in Week 5. If so, you can write it up like this."

> "You have from now until Week 12. These will happen naturally as you work. When something goes wrong or you collaborate with someone, document it."

---

### Closing (2:35-2:45)

> "Today you practised reading numbers before making them. That matters. Most spreadsheets you'll encounter in your life were made by someone else. The first skill is understanding what's already there."
>
> "The second skill is checking. A formula can be correct and still give a wrong answer if the data is wrong. One wrong number -- an outlier -- changed the average from 45 minutes to 847 minutes. Verification isn't optional."
>
> "You got your Decision Log feedback today. Your entry from today should show that you read it. I'll be looking for that."
>
> "Next week: working together. You've been building things individually. What happens when two people need to work on the same thing?"

Remind:

> "Your portfolio repository should have your recent work committed. If you haven't pushed lately, do it before next class."

---

## After Class

### Instructor Tasks

| Task | Deadline | Notes |
|------|----------|-------|
| Review DL entries written this week | Before Week 8 feedback | Are students incorporating round 1 feedback? Note patterns. |
| Note data interpretation skills | Ongoing | Which students could read the spreadsheet accurately? (CLO 6 tracking) |
| Track Git episode activity | Ongoing | Students may begin documenting episodes. Note any who mentioned restores. |
| Review session review patterns | Before Week 7 | Were students able to justify changes? Note students who were silent -- consider pairing them before voice next week. |

---

## Catch-Up Instructions for Latecomers

### If You Missed Week 6

In Week 6, we learned to read and build spreadsheets, and how to verify that formulas and charts are correct.

**1. Learn these 5 terms:**

| Term | Meaning |
|------|---------|
| **data** | Information collected about something -- numbers, text, dates |
| **formula** | An instruction that tells the spreadsheet to calculate something |
| **interpret** | To explain what something means (e.g., "the chart shows most people sleep 7 hours") |
| **verify** | To check whether something is correct (e.g., do one calculation yourself) |
| **chart** | A picture of data that shows patterns |

**2. Practise reading a spreadsheet.** Open any spreadsheet you can find (a budget template, a grade tracker, anything with numbers). Answer these questions:
- What does this spreadsheet track? Who would use it?
- Find a formula. What does it calculate? Is the answer reasonable?
- If there's a chart, does it match the data in the table?

**3. Build something with AI.** Open Excel. Ask Copilot (or any AI): "Calculate the average of [column]." Then:
- Ask AI to explain the formula
- Check one calculation manually
- Build a chart and check whether it matches the data

**4. Write a Decision Log entry** about what you built and how you verified it.

**5. Update your Goal Document.** Write entry 6: What decision in your project could be informed by numbers? What would you need to organize and show?

**6. Read your Decision Log feedback** (entries 1-2) if you haven't already. Your next entry should address the improvement target.

**7. Git Episodes are now eligible.** You need 3 by Week 12: Restore, Error Recovery, Collaboration. See the example in the lesson for what documentation looks like.

---

## Instructor Prep Checklist

- [ ] Decision Log feedback (entries 1-2) printed or shared -- one strength + one improvement target per student
- [ ] Survey results spreadsheet for worked example (20 rows, relatable data, 2-3 formulas, 1 chart, one deliberate data error: 800 instead of 80)
- [ ] Practice dataset **Variant A** prepared and shared (student budget, 15-20 rows, planted outlier error)
- [ ] Practice dataset **Variant B** prepared and shared (same structure, different data, planted formula-range error)
- [ ] Distribution plan: which students get Variant A, which get Variant B (partners must get different variants)
- [ ] Domain orientation prepared: "This is a student's monthly budget. The rows are months..."
- [ ] Blank spreadsheet screenshot for pair vocabulary confirmation
- [ ] Copilot in Excel confirmed working on student devices; **fallback:** students type formulas manually
- [ ] Vocabulary reference slide: data, formula, interpret, verify, chart
- [ ] Goal Document prompt + sentence frames on slide
- [ ] Decision Log template accessible to students
- [ ] Session review slide: role-setting prompt + Week 6 scenario
- [ ] Git Episodes slide: 3 required episodes with modelled documentation example
- [ ] Git Episodes documentation example prepared (screenshot + 3-sentence write-up)
- [ ] Reading comprehension questions on slide (3 questions)
- [ ] Know one calculation you'll do manually in the worked example (for verification demo)

---

## Assessment Alignment

| Assessment component | What happens this week | Weight | CLOs |
|---------------------|----------------------|--------|------|
| **Decision Log feedback** | Round 1 returned (entries 1-2); new entry written incorporating feedback | Part of 30% component | 3, 4 |
| **Git Episodes** | Formally eligible starting this week; documentation format modelled | Part of 10% component | 1, 7 |
| **Session review** | Week 6 scenario: justify a change to a teammate (formative, not graded) | Feeds Micro-Defence 2 (Week 8) | 5 |
| **Goal Document** | Entry 6 written (conditional reasoning, data connection to project) | Ungraded | -- |

**CLO 6 continues** (produce digital products -- spreadsheet interpretation and creation). **CLO 3 continues** (guide AI tools -- prompting Copilot for formulas and charts). **CLO 4 continues** (evaluate AI output -- verifying formulas and checking charts against data).

---

## Language Development Summary

| Skill | Activity |
|-------|----------|
| **Vocabulary** | 5 AWL terms (data, formula, interpret, verify, chart) taught in context with projected spreadsheet; cell/row/column by pointing; pair confirmation task (label screenshot, define "interpret" and "verify" in own words) |
| **Speaking** | Pair jigsaw (explain spreadsheet findings your partner can't see); pair Goal Document + data discussion; session review (12 min AI voice: justify a change to a sceptical teammate) |
| **Reading** | Existing spreadsheet (formulas, charts, data errors); AI-generated formulas and explanations; partner's Goal Document entry; Decision Log feedback from instructor; Git Episode documentation example |
| **Writing** | Reading comprehension answers (3 short responses); Decision Log entry (~150-200 words, incorporating round 1 feedback); Goal Document entry 6 (~75-100 words, conditional language) |
| **Listening** | Vocabulary pre-training; worked example narration; partner's jigsaw explanation; partner's data discussion; AI follow-up questions during session review |

---

## Timing Summary

| Segment | Time | Minutes | Notes |
|---------|------|---------|-------|
| DL feedback return | 0:00-0:07 | 7 | Return feedback, silent reading |
| Vocabulary | 0:07-0:18 | 11 | 5 AWL terms + pair confirmation |
| Worked example | 0:18-0:40 | 22 | Reading (14 min) + building (8 min) |
| Pre-task planning | 0:40-0:45 | 5 | DL re-activation + data schema activation |
| File-access checkpoint | 0:45-0:48 | 3 | Everyone opens file; domain orientation |
| Reading comprehension (jigsaw) | 0:48-1:08 | 20 | Individual (12 min) + pair jigsaw (8 min) |
| Building with Copilot | 1:08-1:25 | 17 | Build formula + chart; verify; stretch option |
| Decision Log entry | 1:25-1:35 | 10 | First entry after round 1 feedback |
| **Break** | **1:35-1:50** | **15** | |
| Goal Document + data exploration | 1:50-2:10 | 20 | Writing (10 min) + pair discussion (10 min) |
| Bridging activity | 2:10-2:12 | 2 | Pick one change, rehearse justification |
| Session review | 2:12-2:25 | 13 | AI voice: justify change to teammate |
| Git Episodes introduction | 2:25-2:35 | 10 | 3 episodes, modelled documentation |
| Closing | 2:35-2:45 | 10 | Theme summary, DL reminder, look-ahead |
| **Total** | | **150 min instruction** | |
