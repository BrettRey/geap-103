# GEAP 103 Week 7 Lesson Plan: Working Together Without Breaking Things

**Context:** 3 x 55 min (150 min instruction + 15-min break), B1 learners, BYOD, Office 365 + Copilot
**Week 7 of 14** | Phase 2: Building

**Learning Objectives (Week 7):**
1. Understand pull requests and Issues as communication genres with distinct rhetorical purposes (CLO 7 begins)
2. Write a PR description and Issue that someone else can act on (CLO 5)
3. Make changes in an individual copy, hand them to a partner with a descriptive change note, and respond to review (CLO 1)
4. Practise collaboration scoping in the Goal Document: describing what is hard and what help you need

**New vocabulary (5 AWL terms):** collaborate, contribute, specific, context, respond

*Pull request, issue, and fork are introduced contextually during the worked example -- genre/tool names shown in the GitHub interface. Comment and review are everyday English words.*

**Pre-class readiness:** Post the shared practice file in two forms: a public GitHub repository and a downloadable document. Ask students to try their preferred route before class, but do not make a successful fork a condition of participation. At the start of Segment B, students select the GitHub PR path or the tracked-change/comment path.

**Goal Thread -- Collaboration Scoping:**
For six weeks students have been describing what THEY want. This week shifts the audience: can you describe what SOMEONE ELSE would need to do? Writing a good Issue or PR description is a professional writing genre. It requires precision because you cannot assume shared context. The person reading your Issue has never been inside your head. If the task description is vague, the help you get will be wrong. This is the same skill as prompting AI (Week 2), but now the audience is a human collaborator.

**Week 8 reminder:** Next week is Micro-Defence 2 (triads, 5 criteria). Segment C includes preparation time.

---

## Segment A: Vocabulary + Worked Example (0:00--0:40)

### 0:00--0:10 | Vocabulary Pre-Training
**Format:** Instructor-led, then task-based pair activity
**Language skills:** Academic vocabulary building, writing (evaluative revision)

**5 AWL terms:** collaborate, contribute, specific, context, respond

Brief definitions (3 min):

1. **Collaborate:** "To work together on something. Today you start working with a partner."
2. **Contribute:** "To add something to a shared project. When you fix a heading and send the change, you are contributing."
3. **Specific:** "Detailed enough that someone can act on it. 'Fix the document' is not specific. 'Change the heading in section 2 to Heading 2 style' is specific."
4. **Context:** "The background information someone needs to understand your message. The reader doesn't know what you know."
5. **Respond:** "To reply to what someone wrote. A good response is specific, not just 'OK.'"

**Pair task** (5 min): Display a bad PR description on screen:

> **Title:** Updated file
> **Description:** Fixed some stuff. Looks better now.

Pairs rewrite it to make it specific and provide context. They must use at least 2 of the 5 vocabulary terms. Share 1-2 examples with the class.

*This replaces a define-and-recite exercise with a task that does double duty: vocabulary confirmation + pre-task for the PR writing in Segment B.*

### 0:10--0:30 | Worked Example: Copy, Change, Handoff, Comment
**Format:** Instructor demonstration with think-aloud
**Language skills:** Listening, reading (GitHub interface text), critical evaluation

Instructor demonstrates the full cycle using the prepared shared repository. Show the GitHub terminology first, then briefly show the equivalent handoff in a document with Track Changes/Suggesting and comments.

**Step 1 -- Fork:**
"I want to contribute to this project, but I don't want to break it. So I fork it: I get my own copy." *Show "Fork" button in GitHub interface.*

**Step 2 -- Make a change:**
Fix a heading and add a sentence. Think aloud: "I'm going to fix the heading structure because it's not accessible. I'll also add a sentence explaining the target audience."

**Step 3 -- Write a pull request (PR) description:**
"Now I tell the project owner what I changed. This message is called a pull request." *Show the PR interface.*

Display the **PR writing template** (this stays on screen through Segment B):

> **What I changed:** [describe each change]
> **Why I changed it:** [give the reason]
> **What I did NOT change:** [say what's the same]

Instructor fills in the template live:
> What I changed: Changed the heading from bold text to Heading 2 style. Added one sentence to the introduction.
> Why: The heading wasn't accessible. The introduction didn't explain who the document is for.
> What I did NOT change: Everything else is the same.

**Step 4 -- Comment and response:**
Show a pre-made comment exchange. The "reviewer" writes: "The heading change looks good. Can you also add alt text to the image in section 2?" Instructor responds: "Good catch. I'll add that in a second commit."

"A comment is a conversation about someone's contribution. An issue is different -- it says 'here's a problem or an idea, someone should work on it.'" *Show the Issues tab.* A task note in the provided document uses the same genre when GitHub is unavailable.

### 0:30--0:32 | Comprehension Gate
**Format:** Pairs
**Language skills:** Speaking (retelling a sequence)

"Before we practise, make sure you can retell the four steps. Turn to your partner. Take turns: first you make your own copy, then you _____, then you _____, then your partner _____."

Instructor listens to 2-3 pairs. If students cannot retell the sequence, clarify before proceeding.

### 0:32--0:40 | Good vs. Bad Examples
**Format:** Whole class, interactive
**Language skills:** Reading (evaluative), speaking

Display 3 pairs of good and bad examples:

1. **Issue titles:** "Problem" vs. "Budget spreadsheet formula in row 12 returns #REF! error"
2. **PR descriptions:** "Updated file" vs. "Added alt text to all three images in the event page. Used descriptive alt text, not just filenames."
3. **Comments:** "Nice" vs. "Your description is clear, but I don't understand what 'fix the layout' means. Can you describe what the layout should look like?"

Quick pair check after each: "Which is more specific? What context is missing?" Volunteers share.

"The pattern is always the same: be specific enough that someone who isn't you can act on it."

---

## Segment B: Planning + Guided Practice (0:40--1:35)

### 0:40--0:43 | Pre-Task Planning
**Format:** Individual reflection

"Think about a time you worked on something with another person. What went wrong?" Students jot 1-2 notes: overlapping work, unclear responsibilities, someone doing the wrong thing because they misunderstood.

"Today's system: write down clearly what you're going to do, do it, explain what you did."

### 0:43--0:45 | Path and Partner Confirmation
**Format:** Whole class

"Open the GitHub fork or your own downloaded copy. Raise your hand when you can edit your copy without changing the instructor's original."

**Routing:** Students with a working fork use the GitHub PR path. Everyone else uses the tracked-change/comment path in their own copy. Do not add students to an instructor-owned branch as an improvised fallback; that creates permissions and overwrite risks. If a partner is absent, form one triad or pair the student with the instructor's prepared sample response.

### 0:45--1:13 | Paired Change-Handoff Exercise
**Format:** Pair work
**Language skills:** Writing (PR descriptions, comments), reading (partner's changes), speaking (negotiation)

**PR writing template** remains on screen throughout. **Sentence frames** also displayed:

> - "I changed _____ because _____."
> - "The result should look like _____."
> - "I did not change _____ because _____."

Process:
1. **Divide the work verbally** (2 min): "I'll fix the headings. You add the missing information in section 3."
2. **Each partner makes their changes independently** in their own fork/copy (~12 min)
3. **Each partner writes a PR description or change note** using the same template (~6 min)
4. **Each partner reviews the other's PR or tracked changes** and leaves one specific comment (~8 min)

For the document path, students keep Track Changes/Suggesting on, add the What/Why/What-not note to their individual copy or Blackboard handoff, exchange the copy/link, and reply to the reviewer's comment. Neither student edits the instructor original, and a single shared artifact does not count as both students' evidence.

**Checkpoint at 1:00 (15 min in):** "If you haven't started writing your PR description yet, stop making changes. Write the description for what you've done so far. The writing is more important than finishing all the changes."

**Stretch option for fast finishers:** "Ask AI to write a PR description for the same change you made. Compare it with yours. Which is more specific? Which provides better context? Would a collaborator prefer yours or AI's?"

**Persona review technique** (3 min, after the main PR review): "Before you submit your review, try this: paste your partner's PR description into AI with a persona. Type: 'You are my teammate. You cannot see my screen. Read this PR description. Based only on what it says, tell me: what was changed? Why? What is NOT clear?' Compare AI's reading with your own. Did AI understand the same things you did? If AI was confused, your collaborator will be too."

Instructor circulates:
- "What does your PR description say? Would I know what you changed without looking at the file?"
- "Your comment says 'looks good.' Can you be more specific?"
- "You both fixed the same heading. What went wrong in your planning?"

**Version-control -- Collaboration episode:** Each student saves evidence of their own change handoff, their partner's specific response, and their reply. A GitHub PR is one route; tracked changes/version history plus a comment exchange is equivalent. Watching a partner's screen is support, not individual evidence.

### 1:13--1:16 | Debrief
**Format:** Whole class

"I noticed something while circulating. Many of you wrote comments like 'looks good' or 'nice work.' What would be more specific?" Take 1-2 examples. Reinforce: specific comments say what was done well or what should change, not just a judgment.

"Now we're switching genres. You've been writing about YOUR changes. Next: you'll write about someone ELSE'S project."

### 1:16--1:35 | Writing Issues for Each Other's Projects
**Format:** Pair work
**Language skills:** Writing (task scoping), speaking (explaining project), reading (partner's Issue)

**Oral briefing frames** displayed:

> - "My project is about _____."
> - "Right now I have finished _____."
> - "The part I need help with is _____."

**Issue template** displayed:

> **Title:** [Clear, specific title -- not "help" or "task"]
> **Context:** This project is _____. It currently has _____.
> **Task:** Change / Add / Fix _____.
> **The result should:** [describe what it looks like when done]
> **You will need to know:** [any information the helper needs]

Process:
1. Partner A explains their project using the oral frames (2 min)
2. Partner B asks clarifying questions (2 min): "What part are you stuck on? What would help most?"
3. Partner B writes an Issue on Partner A's repository or completes the supplied task-note template (~6 min)
4. Switch roles (~10 min total for reverse)

Partners read the Issues written for their projects and respond: "I could / could not do this task because _____."

**Bridging reflection** (last 2 min): "What information did you wish your partner had given you when explaining their project? Remember that feeling. You'll need to provide that same information when you write about your own project after the break."

---

## Break (1:35--1:50)

---

## Segment C: Goal Document + Session Review + Week 8 Prep (1:50--2:45)

### 1:50--2:10 | Goal Document: Collaboration Scoping
**Format:** Individual writing, then pair share
**Language skills:** Writing (conditional, reflective, descriptive)

**Explicit genre framing:**

"You just wrote instructions for someone else -- an Issue that says what to do. Now write about yourself: what is the hardest part of your project, and why? What would a collaborator need to know to help you? The Issue is a task. The Goal Document is a reflection."

**Prompt** (displayed): "What is the hardest part of your project right now? Why is it hard? If a collaborator read your Goal Document, would they understand enough to help?"

**Sentence frames** (displayed):
- "The hardest part of my project is _____ because _____."
- "A collaborator would need to know _____ to help me."
- "I learned today that writing for someone else requires _____."
- "The most important thing about collaboration is _____."

**Writing** (10 min): Students write entry 7 in their Goal Document. This is distinct from the Issue: the Issue specifies a task; the Goal Document reflects on what is difficult and what collaboration requires.

**Pair share** (10 min): Partners read each other's entries. "Does this help you understand the project? What context is still missing?"

### 2:10--2:12 | Bridging Activity
**Format:** Individual, silent

"In two minutes, you'll describe a problem to AI -- a problem in someone else's work, as if they can't see your screen. Think of a problem you noticed today: something in the shared document, in your partner's PR, or in an Issue. Rehearse: what's the problem, and how would you describe it?"

### 2:12--2:25 | Session Review (Speaking Practice)
**Format:** Individual speaking practice. Prefer AI voice; if it is unavailable, use a typed AI exchange read aloud or a live partner/instructor role-play with the same follow-up questions.
**Language skills:** Speaking (describing a problem precisely, responding to follow-up questions)

**Role-setting prompt** (on slide): "Speaking practice. I'm a B1 English student practising explaining my work. Ask me follow-up questions. If my explanation is vague, tell me what's unclear and ask me to be more specific. Don't do the explaining for me."

**This week's scenario** (on slide): "A collaborator's proposed change has a problem. Describe the problem clearly enough for them to fix it without your help. They can't see your screen."

AI role: Collaborator who can't see your screen.

Students talk to AI for 10-12 minutes. The AI pushes back on vague descriptions: "Where exactly is the problem? What should it look like instead?"

Instructor circulates and listens. No intervention unless a student is stuck or silent.

**If using AI voice:** Voice mode starts a new chat. The prompt is said aloud or pasted at the start. The learning target is the student's explanation and follow-up answers, not access to voice mode.

### 2:25--2:35 | Week 8 Micro-Defence Preparation
**Format:** Individual review, then pair practice
**Language skills:** Speaking (previewing oral explanation)

"Next week is Micro-Defence 2. You'll explain one piece of work to your triad partners and answer questions. The criteria have expanded from Week 4."

Display the 5 criteria:

> | Criterion | What the instructor is looking for |
> |-----------|-----------------------------------|
> | Clear description of what was done + context | You explain what you did and why |
> | Correct use of essential terminology | You use course vocabulary accurately |
> | Explains a decision or choice (why, not just what) | You justify something |
> | Shows what was tried (not just "it doesn't work") | **NEW:** You describe your process |
> | Interprets instruction/error message accurately | **NEW:** You can read and explain an error |

"Review your portfolio now. Pick one piece of work you'll present next week. It could be a Decision Log entry, a PR, an Issue, an accessibility fix, a spreadsheet -- anything you can explain."

**Pair preview** (4 min): "Tell your partner in 1 minute: what will you present, and what decision did you make? Partner: ask one question."

### 2:35--2:45 | Closing
**Format:** Whole class

- "Today's core skill: writing clearly enough that someone who isn't you can do what needs to be done. A PR description, an Issue, a help request, a task assignment -- the question is always: does the reader have enough context to act?"
- "Your collaborator doesn't know what you know. That gap -- between your head and theirs -- is what PRs and Issues exist to bridge. The question is always: what's actually there in your description? Not what you meant to say. What you actually wrote."
- "You practised five words: collaborate, contribute, specific, context, respond. These describe good teamwork in any setting."
- "Save evidence of your own change handoff, your partner's specific comment, and your reply. A PR and a tracked-change handoff both count as the Collaboration episode."
- "Next week: Micro-Defence 2. Review your portfolio tonight. You'll present one piece of work in triads and answer questions. The two new criteria are 'show what you tried' and 'interpret an error.' Pick something where you can demonstrate those."

---

## After Class

- **Review change handoffs and task notes** students wrote. Note students whose descriptions are vague or whose comments lack specificity. These students may need support in Week 8.
- **Collaboration episode evidence:** Note which students have their own complete handoff + comment + reply evidence, regardless of route.
- **Session review patterns:** Were students able to describe problems remotely? Note students who struggled -- this skill feeds directly into Micro-Defence 2 (Week 8).
- **Week 8 prep:** Prepare triad groupings and scoring sheets (5 criteria). Students with "partial" or "deferred" observation from Week 4 get first visits.

---

## Instructor Prep Checklist

- [ ] **Shared practice artifact** prepared in two forms: public GitHub repository and downloadable document with deliberate gaps and errors. Share both in Blackboard.
- [ ] **Readiness prompt assigned:** students try their preferred path before class; successful forking is not a participation gate.
- [ ] **Both evidence routes tested:** GitHub fork/PR and individual document copy with tracked changes/version history and comments. Do not use instructor-repository write access as a fallback.
- [ ] Pre-made comment exchange for worked example (second account or screenshot)
- [ ] Good vs. bad example slides (3 pairs: Issue titles, PR descriptions, comments)
- [ ] PR writing template on slide (What I changed / Why / What I did NOT change)
- [ ] Issue template on slide (Title / Context / Task / Result / What you need to know)
- [ ] Oral briefing frames on slide (My project is... / I have finished... / I need help with...)
- [ ] Vocabulary slides: collaborate, contribute, specific, context, respond + bad PR for pair rewriting
- [ ] Goal Document prompt + sentence frames on slide
- [ ] Session review slide: role-setting prompt + Week 7 scenario
- [ ] Week 8 micro-defence criteria slide (5 criteria, 2 new ones highlighted)
- [ ] Plan for pairing (different project types pair well)
- [ ] Prepare an absent-partner route: one triad plus an instructor-prepared sample response; every student still creates individual evidence

## Language Development Summary

- **Vocabulary:** 5 AWL terms (collaborate, contribute, specific, context, respond) pre-trained with a task-based pair activity (rewriting a bad PR description). Pull request, issue, and fork introduced contextually during the worked example. The AWL terms transfer beyond GitHub: "provide context" and "be specific" apply to help requests, bug reports, and AI prompts.
- **Speaking:** Pre-task planning reflection; negotiating task division; explaining own project using oral briefing frames; pair feedback on Issues; pair Goal Document share; pair micro-defence preview; **session review** (12 min AI voice: describing a PR problem to a remote collaborator -- the first scenario requiring description of something the listener cannot see)
- **Reading:** GitHub interface text; PR descriptions (good and bad examples); partner's PR description and comments; partner's Issue; partner's Goal Document entry; Week 8 micro-defence criteria
- **Writing:** PR description (~3-4 sentences using template); PR comment (~1-2 sentences, specific feedback); Issue for partner's project (~3-5 sentences using template); Goal Document entry 7 (~75-100 words; collaboration reflection)
- **Listening:** Vocabulary pre-training; worked example think-aloud; partner's project explanation; partner's feedback on Issue clarity; AI follow-up questions during session review

## Assessment Alignment

- **CLO 7 begins** (collaborate using shared practices): paired PR exercise provides first practice; Issues are the first peer-directed writing
- **CLO 5 continues** (communicate about technical work/decisions): PR descriptions, Issues, and comments are professional genres
- **CLO 1 continues** (manage files + versions): creating an individual copy/version, changing it, and handing it off for review
- **Version-control -- Collaboration episode:** Students who completed their own change handoff + specific comment + reply have evidence. This may be a PR exchange or tracked-change/version-history handoff. Students who did not finish can complete an equivalent exchange asynchronously before Week 12.
- **Decision Log:** Optional this week (students curate 8 entries from the ten-week window, Weeks 2-11)
- **Session review** (formative, not graded): Week 7 scenario practises remote problem description -- builds toward Micro-Defence 2 (Week 8, 5 criteria: "shows what was tried" and "interprets instruction/error accurately")
- **Goal Document:** Entry 7 (ungraded; instructor reads after Week 8)
- **Week 8 Micro-Defence 2 preparation:** Students review portfolio, select work to present, preview with partner
