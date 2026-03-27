# GEAP 103 Week 7: Instructor Materials Package

**Title:** Working Together Without Breaking Things
**Phase:** Building (Week 7 of 14)
**Contact time:** 3 x 55 min (165 min total: 150 min instruction + 15 min break)
**Date prepared:** 2026-03-27

This file contains everything you need to prepare slides and run the class for Week 7. The lesson plan (`lesson-plans/week-07.md`) has the pedagogical rationale. This file has the concrete content.

**Week 7 design note:** This is the first collaboration week. Students shift from working alone to working with a partner. The core skill: writing clearly enough that someone who doesn't share your context can act on what you write. Pull requests, Issues, and comments are treated as communication genres, not GitHub features. The quality criterion is always: "Could someone who isn't you act on this?"

**Pre-class requirement:** Students must fork the shared practice repository before class. Assign this in Week 6 closing or via Blackboard. This prevents forking friction from consuming the paired PR exercise.

**New vocabulary (5 AWL terms):** collaborate, contribute, specific, context, respond

**AI tools:** AI handles Git commands. The human handles the writing. Stretch activity: students compare their PR description with an AI-generated one.

---

## Before Class

### Materials to Prepare

| Material | Description | How to share |
|----------|-------------|-------------|
| **Shared practice repository** | A simple document (student club FAQ or campus event page) with deliberate problems: 3-4 missing headings (bold text, no heading styles), placeholder text in section 3, one image with no alt text, one incorrect date. | Public GitHub repo or GitHub Classroom template. Share URL via Blackboard with forking instructions. |
| **Pre-made comment exchange** | Screenshot or second-account demo showing a reviewer commenting on a PR ("The heading change looks good. Can you also add alt text to the image in section 2?") and the author responding ("Good catch. I'll add that."). | Display on projector |
| **Bad PR description for vocabulary task** | "Title: Updated file. Description: Fixed some stuff. Looks better now." | Display on slide |
| **Good vs. bad examples** | 3 pairs (see Segment A below) | Display on slides |
| **Week 8 micro-defence criteria** | Table of 5 criteria with 2 new ones highlighted | Display on slide |

**Repository setup notes:**
- Use a GitHub template repository or a public repo that students can fork.
- If using GitHub Classroom, create an assignment with individual forks.
- Test that 20 simultaneous forks don't hit rate limits.
- **Fallback:** If forking fails for any student, they can work in the GitHub web editor using a branch on the instructor's repo. Set branch permissions to allow this.

### Pre-Fork Verification

Before class, check how many students have forked:
- Go to your repository → Insights → Forks
- Or check GitHub Classroom dashboard
- Students who haven't forked will need 2-3 minutes at the start of Segment B

---

## Segment A: Vocabulary + Worked Example (0:00-0:40)

### Vocabulary (0:00-0:10)

**Vocabulary reference slide** (display and leave up):

| Term | Meaning |
|------|---------|
| **collaborate** | To work together on something |
| **contribute** | To add something to a shared project |
| **specific** | Detailed enough that someone can act on it |
| **context** | The background information someone needs to understand your message |
| **respond** | To reply to what someone wrote -- a good response says what you'll do |

Brief definitions (3 min): One sentence per term, connecting to today's work.

**Pair rewriting task** (5 min): Display the bad PR description:

> **Title:** Updated file
> **Description:** Fixed some stuff. Looks better now.

> "With your partner, rewrite this PR description. Make it specific. Provide context. Use at least 2 of the 5 vocabulary terms."

Pairs write for 3 minutes. Instructor collects 1-2 examples:

> "What did you write? How is it better? What context did you add?"

---

### Worked Example: Fork, Change, PR, Comment (0:10-0:30)

Demonstrate on the projector using the shared practice repository.

**Step 1 -- Fork** (2 min):

> "I want to contribute to this project, but I don't want to break it. So I fork it -- I get my own copy."

Show the Fork button. Click it. Show the forked copy.

> "A fork is like a photocopy of someone else's folder. I can change my copy without affecting theirs."

**Step 2 -- Make a change** (3 min):

Fix a heading (bold → Heading 2) and add a sentence. Think aloud:

> "I'm going to fix the heading structure because it's not accessible. I'll also add a sentence explaining who this document is for."

**Step 3 -- Write a PR description** (5 min):

> "Now I tell the project owner what I changed. This message is called a pull request."

Display the **PR writing template** (leave on screen through Segment B):

> | Field | Your answer |
> |-------|-------------|
> | **What I changed** | [describe each change] |
> | **Why I changed it** | [give the reason] |
> | **What I did NOT change** | [say what's the same] |

Fill it in live:

> What I changed: Changed the heading from bold text to Heading 2 style. Added one sentence to the introduction.
> Why: The heading wasn't accessible. The introduction didn't explain who the document is for.
> What I did NOT change: Everything else is the same.

> "Three questions: what, why, what not. That's specific. That's context."

**Step 4 -- Comment exchange** (5 min):

Show the pre-made example. Reviewer writes: "The heading change looks good. Can you also add alt text to the image in section 2?" Author responds: "Good catch. I'll add that in a second commit."

> "A comment is a conversation about someone's contribution. An issue is different -- it says 'here's a problem or an idea, someone should work on it.'"

Show the Issues tab briefly.

> "Comments are about existing contributions. Issues are requests for new contributions. Both need to be specific."

**Step 5 -- Show the Issue interface** (2 min):

Open a sample Issue. Show Title + Description fields.

> "An Issue has a title and a description. The title says what the problem is. The description gives context: where is the problem, what should it look like, what does the helper need to know."

---

### Comprehension Gate (0:30-0:32)

> "Before we practise, make sure you know the four steps. Turn to your partner. Take turns saying them: first you fork, then you _____, then you _____, then your partner _____."

Listen to 2-3 pairs. Clarify if needed.

---

### Good vs. Bad Examples (0:32-0:40)

Display each pair. Pairs discuss (30 seconds), then share.

**Pair 1 -- Issue titles:**
> Bad: "Problem"
> Good: "Budget spreadsheet formula in row 12 returns #REF! error"

> "Which one gives you context? Which one is specific?"

**Pair 2 -- PR descriptions:**
> Bad: "Updated file"
> Good: "Added alt text to all three images in the event page. Used descriptive alt text, not just filenames."

**Pair 3 -- Comments:**
> Bad: "Nice"
> Good: "Your description is clear, but I don't understand what 'fix the layout' means. Can you describe what the layout should look like?"

> "The pattern is always the same: be specific enough that someone who isn't you can act on it."

---

## Segment B: Planning + Guided Practice (0:40-1:35)

### Pre-Task Planning (0:40-0:43)

> "Think about a time you worked on something with another person. What went wrong? Overlapping work? Unclear responsibilities? Someone misunderstanding? Jot 1-2 notes."

> "Today's system: write down clearly what you're going to do, do it, explain what you did."

---

### Fork Confirmation (0:43-0:45)

> "Everyone should have forked the practice repository. Open GitHub and find your fork. Raise your hand when you see it."

Help students who haven't forked (2 min). **Fallback:** students who can't fork work in the GitHub web editor on a branch.

---

### Paired PR Exercise (0:45-1:13)

**PR template and sentence frames stay on screen:**

> **PR Template:**
> - What I changed: _____
> - Why I changed it: _____
> - What I did NOT change: _____
>
> **Sentence frames:**
> - "I changed _____ because _____."
> - "The result should look like _____."
> - "I did not change _____ because _____."

Display the steps:

> 1. Divide the work with your partner (2 min): "I'll fix _____. You fix _____."
> 2. Make your changes (12 min)
> 3. Write your PR description using the template (6 min)
> 4. Read your partner's PR. Leave one specific comment (8 min)

**Checkpoint at 1:00** (display or announce):

> "If you haven't started writing your PR description yet, stop making changes. Write the description for what you've done so far. The writing is more important than finishing."

**Stretch option** (display for fast finishers):

> Done? Ask AI to write a PR description for the same change. Compare: which is more specific? Which provides better context? Would a collaborator prefer yours or AI's?

**What to say while circulating:**

| What you see | What to say |
|-------------|------------|
| Student writing PR description | "Read it to me. Would I know what you changed without looking at the file?" |
| Student's comment says "looks good" | "Can you be more specific? What exactly looks good?" |
| Both partners fixed the same thing | "What went wrong in your planning? How would you prevent that?" |
| Student stuck on Git | "What are you trying to do? Ask AI to help. If that doesn't work, use the web editor." |
| Strong pair finished with comment exchange | "Save a screenshot -- that's your Collaboration episode for Git Episodes." |

**Git Episodes reminder:**

> "If you finished a PR with a comment exchange, save a screenshot. This counts as your Collaboration episode."

---

### Debrief (1:13-1:16)

> "I noticed something. Many of you wrote comments like 'looks good' or 'nice work.' What would be more specific?"

Take 1-2 examples from the class.

> "A specific comment says what was done well OR what should change. Not just a judgment."
>
> "Now we're switching genres. You've been writing about YOUR changes. Next: you'll write about someone ELSE'S project."

---

### Writing Issues for Each Other's Projects (1:16-1:35)

**Oral briefing frames** (display):

> - "My project is about _____."
> - "Right now I have finished _____."
> - "The part I need help with is _____."

**Issue template** (display):

> | Field | Your answer |
> |-------|-------------|
> | **Title** | [clear, specific -- not "help" or "task"] |
> | **Context** | This project is _____. It currently has _____. |
> | **Task** | Change / Add / Fix _____. |
> | **The result should** | [describe what it looks like when done] |
> | **You will need to know** | [information the helper needs] |

Display the steps:

> 1. Partner A explains their project using the frames above (2 min)
> 2. Partner B asks questions: "What part are you stuck on? What would help?" (2 min)
> 3. Partner B writes an Issue on Partner A's repo using the template (6 min)
> 4. Switch roles (10 min for reverse)
>
> When done: read the Issue your partner wrote for you. "I could / could not do this task because _____."

**Last 2 minutes -- bridging reflection:**

> "What information did you wish your partner had given you? Remember that feeling. After the break, you'll write about your own project, and you'll need to provide that same kind of information."

**What to say while circulating:**

| What you see | What to say |
|-------------|------------|
| Partner B writing a vague Issue | "Read it as if you've never seen this project. Could you do the task?" |
| Partner A's explanation was too brief | "Ask: 'What part are you stuck on? What have you tried?'" |
| Issue title is "Help" | "Can you make the title more specific? What exactly is the task?" |
| Strong Issue | "Good. Now read it as a stranger would. Is anything missing?" |

---

## Break (1:35-1:50)

---

## Segment C: Goal Document + Session Review + Week 8 Prep (1:50-2:45)

### Goal Document: Collaboration Scoping (1:50-2:10)

**Genre framing** (display):

> "You just wrote instructions for someone else -- an Issue that says what to do. Now write about yourself: what is the hardest part of your project, and why? What would a collaborator need to know to help you?
>
> The Issue is a task. The Goal Document is a reflection."

**Prompt** (display):

> What is the hardest part of your project right now? Why is it hard? If a collaborator read your Goal Document, would they understand enough to help?

**Sentence frames** (display):

> - "The hardest part of my project is _____ because _____."
> - "A collaborator would need to know _____ to help me."
> - "I learned today that writing for someone else requires _____."
> - "The most important thing about collaboration is _____."

**Writing** (10 min): Entry 7 in the Goal Document.

**Pair share** (10 min): Partners read each other's entries.

> "Does this help you understand the project? What context is still missing?"

---

### Bridging Activity (2:10-2:12)

> "In two minutes, you'll describe a problem to AI. Think of a problem you noticed today: something in the shared document, in your partner's PR, or in an Issue. Rehearse in your head: what's the problem, and how would you describe it to someone who can't see your screen?"

---

### Session Review -- Speaking Practice (2:12-2:25)

Display:

> **Open your AI tool. Start a new chat.**
>
> **First, say this (or paste it):**
> "Speaking practice. I'm a B1 English student practising explaining my work. Ask me follow-up questions. If my explanation is vague, tell me what's unclear and ask me to be more specific. Don't do the explaining for me."
>
> **Then, your task:** A collaborator's pull request has a problem. Describe the problem clearly enough for them to fix it without your help. They can't see your screen.
>
> Start with: "I was reviewing a pull request and I found a problem. The problem is _____."

Students talk to AI for 10-12 minutes. Instructor circulates and listens.

**What to listen for:**

| What you hear | What it means |
|--------------|---------------|
| Student provides specific description with location | Strong -- the "can't see your screen" constraint is working |
| Student says "the thing is broken" and AI pushes back | The system is working -- AI demands specificity |
| Student is silent | "Start with one thing: what did you review today? What was wrong with it?" |

---

### Week 8 Micro-Defence Preparation (2:25-2:35)

> "Next week is Micro-Defence 2. You'll explain one piece of work to your triad partners and answer questions."

Display the 5 criteria:

> | Criterion | What the instructor looks for |
> |-----------|------------------------------|
> | Clear description of what was done + context | You explain what and why |
> | Correct use of essential terminology | You use course vocabulary accurately |
> | Explains a decision or choice (why, not just what) | You justify something |
> | **Shows what was tried** (not just "it doesn't work") | **NEW: You describe your process** |
> | **Interprets instruction/error message accurately** | **NEW: You read and explain an error** |

> "Review your portfolio now. Pick one piece of work you'll present. It could be a Decision Log entry, a PR, an Issue, an accessibility fix, a spreadsheet -- anything you can explain."

**Pair preview** (4 min):

> "Tell your partner in 1 minute: what will you present? What decision did you make? Partner: ask one question."

---

### Closing (2:35-2:45)

> "Today's core skill: writing clearly enough that someone who isn't you can do what needs to be done. A PR description, an Issue, a help request -- the question is always: does the reader have enough context to act?"
>
> "You practised five words: collaborate, contribute, specific, context, respond. These describe good teamwork in any setting."
>
> "If you completed a PR with a comment exchange today, save a screenshot. That's your Collaboration episode for Git Episodes."
>
> "Next week: Micro-Defence 2. Review your portfolio tonight. Pick one piece of work. The two new criteria are 'show what you tried' and 'interpret an error.' Pick something where you can demonstrate those."

---

## After Class

### Instructor Tasks

| Task | Deadline | Notes |
|------|----------|-------|
| Review student PRs and Issues | Before Week 8 | Note vague descriptions -- these students need support in Week 8 |
| Track collaboration episode evidence | Ongoing | Which students have PR + comment exchange? |
| Review session review patterns | Before Week 8 | Could students describe problems remotely? Note struggles. |
| Prepare Week 8 micro-defence | Before Week 8 | Triad groupings, scoring sheets (5 criteria), observation rotation (students with "partial/deferred" from Week 4 get first visits) |

---

## Catch-Up Instructions for Latecomers

### If You Missed Week 7

In Week 7, we learned to work together using pull requests and Issues on GitHub.

**1. Learn these 5 terms:**

| Term | Meaning |
|------|---------|
| **collaborate** | To work together on something |
| **contribute** | To add something to a shared project |
| **specific** | Detailed enough that someone can act on it |
| **context** | Background information someone needs to understand your message |
| **respond** | To reply -- a good response says what you'll do, not just "OK" |

**2. Understand these GitHub genres:**

| Genre | Purpose |
|-------|---------|
| **Pull request (PR)** | "Here's what I changed and why. Please look at it." |
| **Issue** | "Here's a problem or idea. Someone should work on it." |
| **Fork** | "I want my own copy of your work so I can try something." |

**3. Write a PR description.** Find the shared practice repository (link on Blackboard). Fork it, make one change (fix a heading, add alt text, correct a date), and write a PR description using this template:
- What I changed: _____
- Why I changed it: _____
- What I did NOT change: _____

**4. Write an Issue on your own repository.** Describe one task that someone else could help with:
- Title: [specific]
- Context: My project is _____
- Task: Change / Add / Fix _____
- The result should: _____

**5. Update your Goal Document.** Write entry 7: What is the hardest part of your project? Why? What would a collaborator need to know?

**6. Prepare for Week 8 Micro-Defence.** Review your portfolio. Pick one piece of work you can explain. You'll present to 2 partners and answer questions. New criteria: show what you tried, interpret an error.

---

## Instructor Prep Checklist

- [ ] Shared practice repository created and URL shared (Blackboard or Week 6 closing)
- [ ] Pre-fork homework assigned and verified (check Insights → Forks before class)
- [ ] Fallback plan: branch permissions set so students can work in web editor if forking fails
- [ ] Pre-made comment exchange (second account or screenshot) for worked example
- [ ] Good vs. bad example slides (3 pairs)
- [ ] Bad PR description for vocabulary rewriting task
- [ ] PR writing template on slide (What / Why / What not)
- [ ] Issue template on slide (Title / Context / Task / Result / Need to know)
- [ ] Oral briefing frames on slide (My project is / I have finished / I need help with)
- [ ] Sentence frames for PR writing on slide
- [ ] Vocabulary slides: collaborate, contribute, specific, context, respond
- [ ] Goal Document prompt + sentence frames on slide
- [ ] Session review slide: role-setting prompt + Week 7 scenario
- [ ] Week 8 micro-defence criteria slide (5 criteria, 2 new highlighted)
- [ ] Triad groupings drafted for Week 8
- [ ] Scoring sheets printed for Week 8 (can wait until next week)

---

## Assessment Alignment

| Assessment component | What happens this week | Weight | CLOs |
|---------------------|----------------------|--------|------|
| **Git Episodes -- Collaboration** | PR + comment exchange = evidence for Collaboration episode | Part of 10% component | 1, 7 |
| **Session review** | Week 7: remote problem description (formative) | Feeds Micro-Defence 2 | 5 |
| **Goal Document** | Entry 7: collaboration scoping (ungraded) | Instructor reads after Week 8 | -- |
| **Decision Log** | Optional this week (students choose 8 of 12) | Part of 30% component | 3, 4 |

**CLO 7 begins** (collaborate using shared practices). **CLO 5 continues** (communicate about technical work). **CLO 1 continues** (manage files + versions).

---

## Language Development Summary

| Skill | Activity |
|-------|----------|
| **Vocabulary** | 5 AWL terms (collaborate, contribute, specific, context, respond) via bad-PR rewriting task; pull request, issue, fork introduced contextually during worked example |
| **Speaking** | Negotiating task division; explaining project using oral frames; pair feedback on Issues; pair Goal Document share; pair micro-defence preview; session review (12 min AI voice: remote problem description) |
| **Reading** | GitHub interface; good/bad PR and Issue examples; partner's PR + comments; partner's Issue; partner's Goal Document; Week 8 criteria |
| **Writing** | PR description (template); PR comment; Issue for partner (template); Goal Document entry 7 (reflection on collaboration) |
| **Listening** | Vocabulary task; worked example; partner's project explanation; partner's feedback; AI follow-ups |

---

## Timing Summary

| Segment | Time | Minutes | Notes |
|---------|------|---------|-------|
| Vocabulary | 0:00-0:10 | 10 | 5 AWL terms + bad-PR rewriting task |
| Worked example | 0:10-0:30 | 20 | Fork → change → PR → comment cycle |
| Comprehension gate | 0:30-0:32 | 2 | Pairs narrate back the 4 steps |
| Good vs. bad examples | 0:32-0:40 | 8 | 3 pairs, pair check + share |
| Pre-task planning | 0:40-0:43 | 3 | Collaboration reflection |
| Fork confirmation | 0:43-0:45 | 2 | Verify pre-fork; fallback for stragglers |
| Paired PR exercise | 0:45-1:13 | 28 | Divide → change → write PR → review PR |
| Debrief | 1:13-1:16 | 3 | Surface "looks good" pattern |
| Issue writing (partner) | 1:16-1:35 | 19 | Oral briefing → questions → write Issue → switch |
| **Break** | **1:35-1:50** | **15** | |
| Goal Document | 1:50-2:10 | 20 | Writing (10 min) + pair share (10 min) |
| Bridging activity | 2:10-2:12 | 2 | Rehearse problem description |
| Session review | 2:12-2:25 | 13 | AI voice: remote problem description |
| Week 8 prep | 2:25-2:35 | 10 | Review criteria, pick work, pair preview |
| Closing | 2:35-2:45 | 10 | Summary, Git Episodes reminder, Week 8 reminder |
| **Total** | | **150 min instruction** | |
