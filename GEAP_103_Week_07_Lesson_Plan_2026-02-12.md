# GEAP 103 Week 7 Lesson Plan: Working Together Without Breaking Things

**Context:** 3 x 55 min (150 min instruction + 15-min break), B1 learners, BYOD, Office 365 + Copilot
**Week 7 of 14** | Phase 2: Building

**Learning Objectives (Week 7):**
1. Understand pull requests and Issues as communication genres with distinct rhetorical purposes (CLO 7 begins)
2. Write a PR description and Issue that someone else can act on (CLO 5)
3. Fork a shared repository, make changes, and submit a PR with a descriptive comment (CLO 1)
4. Practise collaboration scoping in the Goal Document: describing tasks for someone who doesn't share your context

**New vocabulary (5):** pull request (PR), issue, fork, comment, review

**Goal Thread -- Collaboration Scoping:**
For six weeks students have been describing what THEY want. This week shifts the audience: can you describe what SOMEONE ELSE would need to do? Writing a good Issue or PR description is a professional writing genre. It requires precision because you cannot assume shared context. The person reading your Issue has never been inside your head. If the task description is vague, the help you get will be wrong. This is the same skill as prompting AI (Week 2), but now the audience is a human collaborator. The language demands are higher: conditional ("If you want to do this, you would need to..."), imperative ("Change the heading to..."), and descriptive ("The result should look like...").

---

## Segment A: Vocabulary + Worked Example (0:00--0:40)

### 0:00--0:10 | Vocabulary Pre-Training: Communication Genres
**Format:** Instructor-led, interactive
**Language skills:** Academic vocabulary building, listening

**5 terms** introduced as communication genres, not tool features:

| Term | What it communicates |
|------|---------------------|
| **Pull request (PR)** | "Here's what I changed and why. Please look at it." |
| **Issue** | "Here's a problem or an idea. Someone should work on it." |
| **Fork** | "I want my own copy of your work so I can try something without breaking yours." |
| **Comment** | "I have a question or suggestion about what you did." |
| **Review** | "I looked at your work. Here's what I think." |

For each term: show it on screen in the GitHub interface. Point to where it appears. Ask a volunteer to explain it in their own words.

"These are not just buttons on a website. Each one is a way of communicating with someone you're working with. A PR is a short piece of writing. An Issue is a short piece of writing. A comment is a conversation. Today is about writing these well enough that someone else can understand and act on them."

### 0:10--0:30 | Worked Example: Fork, Change, PR, Comment
**Format:** Instructor demonstration with think-aloud
**Language skills:** Listening, reading (GitHub interface text), critical evaluation

Instructor demonstrates the full cycle using a prepared shared repository (e.g., a simple document with a few known problems):

**Step 1 -- Fork:**
"I want to help with this project, but I don't want to break it. So I fork it: I get my own copy."

**Step 2 -- Make a change:**
Change something visible (fix a heading, add a sentence, correct a spelling error). Think aloud: "I'm going to fix the heading structure because it's not accessible. I'll also add a sentence explaining who this document is for."

**Step 3 -- Write a PR description:**
Display two versions:

**Bad PR description:**
> "Fixed some stuff."

**Good PR description:**
> "Changed the heading from bold text to Heading 2 style so screen readers can navigate the document. Added one sentence to the introduction explaining the target audience. No other changes."

"Which one tells you what happened? Which one would you trust? The good PR description answers three questions: what did I change, why did I change it, and what did I NOT change."

**Step 4 -- Comment exchange:**
Instructor switches to a second account (or shows a pre-made example). The "reviewer" leaves a comment: "The heading change looks good. Can you also add alt text to the image in section 2?" Instructor responds: "Good catch. I'll add that in a second commit."

"This is a conversation. The comment is specific: it says exactly what needs to happen and where. 'Looks good' is not a useful comment. 'Can you also add alt text to the image in section 2?' is useful because the other person can act on it."

### 0:30--0:40 | Good vs. Bad Examples
**Format:** Whole class, interactive
**Language skills:** Reading (evaluative), speaking

Display 3-4 pairs of good and bad examples (on slides or screen). For each pair, students identify which is better and why:

1. **Issue titles:** "Problem" vs. "Budget spreadsheet formula in row 12 returns #REF! error"
2. **PR descriptions:** "Updated file" vs. "Added alt text to all three images in the event page. Used descriptive alt text, not just filenames."
3. **Comments:** "Nice" vs. "Your description is clear, but I don't understand what 'fix the layout' means. Can you describe what the layout should look like?"

Quick pair check after each: "Which is better? Why?" Volunteers share.

"The pattern is always the same: be specific enough that someone who isn't you can act on it. This is the same skill you practised in Week 2 with AI prompts. The audience is different (a person, not AI), but the principle is identical: say what you mean."

---

## Segment B: Planning + Guided Practice (0:40--1:35)

### 0:40--0:45 | Pre-Task Planning
**Format:** Individual reflection

"Think about a time you worked on something with another person. A group project, a shared document, cooking together, building something. What went wrong? How did you divide the work?"

Students jot 2-3 notes. Not a story, just the problem: overlapping work, lost files, unclear responsibilities, someone doing the wrong thing because they misunderstood.

"Today you'll practise a system for working together without those problems. The system isn't the tool. The system is: write down clearly what you're going to do, do it, and explain what you did."

### 0:45--1:15 | Paired PR Exercise
**Format:** Pair work
**Language skills:** Writing (PR descriptions, comments), reading (partner's changes), speaking (negotiation)

Instructor has prepared a shared repository with a simple document (e.g., a student club FAQ page or a campus event page, with deliberate gaps and errors: missing headings, placeholder text, no alt text on images, an incorrect date).

Each pair:
1. **Both partners fork the repository** (using Copilot/AI to handle the Git commands)
2. **Divide the work verbally:** "I'll fix the headings. You add the missing information in section 3." (2 min discussion)
3. **Each partner makes their changes independently** (~10 min)
4. **Each partner writes a PR description** explaining what they changed and why
5. **Each partner reviews the other's PR:** leave one specific comment (a question, a suggestion, or a confirmation)

Instructor circulates. Key coaching points:
- "What does your PR description say? Would I know what you changed without looking at the file?"
- "Your comment says 'looks good.' Can you be more specific? What exactly looks good?"
- "You both fixed the same heading. What went wrong in your planning? How would you prevent that?"

### 1:15--1:35 | Writing Issues for Each Other's Projects
**Format:** Pair work
**Language skills:** Writing (task scoping, imperative and descriptive register), reading (partner's project context)

"Now something harder. You're going to write a GitHub Issue about your PARTNER'S project. This means you need to understand enough about what they're doing to describe a useful task."

Process:
1. Partner A explains their project briefly (2 min): what they're building, where they are, what's left to do
2. Partner B asks clarifying questions (2 min): "What part are you stuck on? What would help most?"
3. Partner B writes an Issue on Partner A's repository: a concrete task that Partner B could (hypothetically) pick up and complete
4. Switch roles

"The Issue should be specific enough that a stranger could read it and know what to do. If it says 'help with the project,' that's useless. If it says 'Add alt text to the three images in the student guide. Each image shows a building on campus; the alt text should say which building and where it is,' that's something someone can act on."

Partners read the Issues written for their projects and respond: "Could someone actually do this? Is anything unclear?"

---

## Break (1:35--1:50)

---

## Segment C: Application + Goal Document (1:50--2:45)

### 1:50--2:15 | Application: Writing an Issue for Your Own Project
**Format:** Individual with pair check
**Language skills:** Writing (task scoping), reading (reviewing own work from collaborator's perspective)

"Now write an Issue about YOUR OWN project. Think about the hardest part, or the part you're least sure about. Describe it as a task that someone else could pick up."

Students write a GitHub Issue on their own portfolio repository. The Issue describes one task related to their project that a collaborator could help with.

Requirements for the Issue:
- A clear title (not "help" or "task")
- Context: what the project is and where this task fits
- The specific task: what needs to be done
- What the result should look like
- Any information the helper would need

Instructor circulates: "Read your Issue as if you've never seen this project before. Does it make sense? Could you do this task based only on what's written here?"

Pairs read each other's Issues and give one piece of feedback: "I could / could not do this task because _____."

### 2:15--2:35 | Goal Document: Collaboration Scoping
**Format:** Individual writing
**Language skills:** Writing (conditional, descriptive, imperative)

"For six weeks you've been writing about what YOU want. Today: write about what SOMEONE ELSE would need to do to help you. This is harder because you can't assume they know what you know."

**Prompt** (displayed): "Think about your project. What part is hardest? What part could someone else help with? Write a GitHub Issue describing one task on your project that a partner could pick up."

**Sentence frames** (displayed):
- "I need help with _____. The task is to _____."
- "To do this task, you would need to know _____."
- "The result should look like _____."

Students write entry 7 in their Goal Document (~10-15 min). This overlaps with the Issue they just wrote, but the Goal Document version is more reflective: it's about what's hard and why, not just the task specification.

**Pair share** (5 min): Partners read each other's entry. "Is the task clear enough that you could help? What questions do you have?"

### 2:35--2:45 | Closing
**Format:** Whole class

- "Today's new skill is something you'll use in every job you ever have: writing clearly enough that someone who isn't you can do what needs to be done. A PR description, an Issue, a help request, a task assignment -- these are all the same genre. The question is always: does this make sense to someone who doesn't share my context?"
- "Next week: things go wrong. Formulas break, commits fail, AI misunderstands you. You'll learn to read error messages and write the most useful thing you can write in a professional setting: a good help request."
- "Next week is also Micro-Defence 2. Review your portfolio and your recent work. You'll explain one piece of work and answer questions about it."

---

## After Class

- **Review Issues and PRs** students wrote during class. Note students whose Issue descriptions are vague or whose PR descriptions lack specificity. These students may need extra support in Week 8 when writing help requests.
- **Collaboration episode evidence:** Students who completed the paired PR exercise have evidence toward the Git Episodes collaboration requirement. Note which students have usable PR + comment exchanges.
- **Decision Log reminder:** Students who choose to write a DL entry this week would document an AI interaction during the PR or Issue-writing process.

---

## Instructor Prep Checklist

- [ ] Shared repository prepared with a simple document containing deliberate gaps and errors (missing headings, placeholder text, no alt text, incorrect date)
- [ ] Second GitHub account or pre-made comment exchange for the worked example
- [ ] Good vs. bad example slides prepared (3-4 pairs: Issue titles, PR descriptions, comments)
- [ ] Vocabulary slides: pull request (PR), issue, fork, comment, review -- framed as communication genres
- [ ] Forking process tested with Copilot/AI on student-accessible devices
- [ ] Goal Document prompt + sentence frames on slide
- [ ] Confirm all students have GitHub accounts and can access their portfolio repositories
- [ ] Plan for pairing (students with different project types pair well; similar project types also work)
- [ ] Reminder slide for Week 8 micro-defence preparation

## Language Development Summary

- **Vocabulary:** 5 terms (pull request, issue, fork, comment, review) pre-trained as communication genres in Segment A, applied in paired practice and individual writing in B and C
- **Speaking:** Pre-task planning reflection (pair); explaining own project to partner; negotiating task division; discussing Issue clarity; pair feedback on Goal Document entries
- **Reading:** GitHub interface text; PR descriptions (good and bad examples); partner's PR description and comments; partner's Issue; partner's Goal Document entry
- **Writing:** PR description (~2-4 sentences; descriptive + justificatory); comments on partner's PR (~1-2 sentences; specific feedback); Issue for partner's project (~3-5 sentences; task scoping); Issue for own project (~3-5 sentences); Goal Document entry (~50-100 words; collaboration scoping with conditional and descriptive language)
- **Listening:** Vocabulary pre-training; worked example think-aloud; partner's project explanation; partner's feedback on Issue clarity

## Assessment Alignment

- **CLO 7 begins** (collaborate using shared practices): paired PR exercise provides first practice
- **CLO 5** (communicate about technical work/decisions): PR descriptions, Issues, and comments are professional genres
- **CLO 1** (manage files + versions): forking, committing, and submitting PRs
- **Git Episodes -- Collaboration episode:** Students who completed a PR with description + comment exchange have evidence toward this required episode. Instructor notes which students have usable evidence.
- **Decision Log:** Optional this week (students choose 8 of 12 eligible weeks). If written, the DL would document an AI interaction during the collaborative work.
- **Goal Document:** Entry 7 (ungraded; instructor reads after Week 8)
