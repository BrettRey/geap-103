# GEAP 103 Week 3: Instructor Materials Package

**Title:** Never Losing Work Again
**Phase:** Discovery (Week 3 of 14)
**Contact time:** 3 × 55 min (165 min total: 150 min instruction + 15 min break)
**Date prepared:** 2026-03-24

This file contains everything you need to prepare slides and run the class for Week 3. The lesson plan (`Week_03_Lesson_Plan_2026-02-12.md`) has the pedagogical rationale. This file has the concrete content. In case of conflict, the lesson plan governs.

**Week 3 design note:** Students have been making things for two weeks. They have files scattered across their geap-103 folder. Today they learn to protect them: version control as a timeline of snapshots they control. The tool is Git/GitHub. The skill is writing commit messages — short descriptions of what you did and why. With the CLI, Git is a conversation: "save this version," "show me the previous version," "put this online." Without the CLI, Git is the GitHub web interface, which is clunkier but achieves the same thing. Both paths are supported.

**AI tools:** Same tool-agnostic approach as Week 2. Students use whatever they set up last week. CLI users get Git for free (it's built in). Browser-based AI users use the GitHub web interface for Git operations.

---

## Segment A: Hook + First Commits (0:00–1:00)

### Warm-Up (0:00–0:10)

> You've been making things for two weeks: a file system, AI conversations, Decision Logs, a Goal Document. Has anyone ever lost something they were working on? Deleted it by accident? Wanted to go back to an earlier version?

Pairs: "Tell your partner about a time you lost work or couldn't find something." Frame: "I was working on _____ and then _____." (2 min each)

1–2 volunteers share with the class.

Then:

> Today we fix that. You're going to learn how to save snapshots of your work so you can always go back. It's called version control.

---

### Step 1: Create a Repository (0:10–0:25)

Display Slide 1:

> A **repository** is a place where your work and its history are kept. Think of it as a folder with a memory — it remembers every version of every file.
>
> Create one now for your course work.

**CLI path:**

> In your terminal, navigate to your geap-103 folder and type:

Display:

```
copilot "Create a Git repository here and connect it to a new GitHub repository called geap-103-portfolio"
```

**Web path:**

> Go to github.com. Click "New repository." Name it `geap-103-portfolio`. Then upload one file from your geap-103 folder.

**Vocabulary reference slide** (display and leave up — same approach as Weeks 1–2):

| Term | Meaning |
|------|---------|
| **repository** | A folder with a memory — it keeps your work and every version of it |
| **commit** | Saving a snapshot — telling the repository "remember this version" |
| **snapshot** | What your files look like at one moment in time |
| **restore** | Going back to an earlier snapshot |
| **push** | Putting your repository online so it's safe and shareable |

**Single-projector rooms:** Tell students to photograph this slide now.

Do NOT pre-teach all five terms. Students will encounter them over the next hour. Name each one as it comes up: "What you just did — saving a version — that's called a *commit*."

Circulate. **Budget 10 minutes here.** Most students should have GitHub accounts from Week 1. Those who don't: help them sign up now. Students who finish early start Step 2.

**Whole-class fallback:** If more than a third of students can't get a repo created by 0:25, switch to a live walkthrough on the projector: create one repo together as a class, then students replicate what they saw. This is slower but ensures everyone has a working repo before Step 2.

---

### Step 2: First Commit (0:25–0:40)

Display Slide 2:

> Add a file to your repository. AI will propose a **commit message** — a short description of what you're saving. Read it. Does it accurately describe what this file is?
>
> If not, change it. The commit message is a note to your future self. "Updated file" tells you nothing. "Added goal document from weeks 1–2" tells you exactly what happened.

**CLI path:**

```
copilot "Add my goal document to the repository and commit"
```

The CLI will propose a commit message. The student reads it and either accepts, modifies, or rejects it — the same cycle from Week 2.

**Web path:**

> On your repository page, click "Add file" → "Upload files." Choose a file from your geap-103 folder. GitHub suggests a commit message. Read it. If it doesn't describe your file accurately, change it. Click "Commit changes."

**What to say while circulating:**

| What you see | What to say | What you're naming |
|-------------|------------|-------------------|
| Student created a repo | "Good. That's your *repository*. Now let's put something in it." | repository |
| Student added a file and AI proposed a message | "Read the message. Does it describe what you actually added? If not, change it." | commit message as evaluation (CLO 4) |
| Student accepted "updated file" or a vague message without reading | "Your future self reads this in 3 months. Will they know what this file is? What would be more specific?" | The commit message is a review exercise, not a writing exercise. |
| Student revised the AI's message to be more specific | "Good. You just evaluated AI's description and made it better. That's the same skill from Week 2." | revise, evaluate |
| Student committed successfully | "You just saved a *snapshot*. Even if you change the file later, this version still exists." | snapshot, commit |
| Student got an error | "Read the error message aloud. What is it asking you to do?" | troubleshoot (CLO 2 preview) |
| Student's tool won't cooperate | "Try the web interface: github.com. Or sit with a partner and share their screen for now." | — |

**At ~0:35, brief pause:**

> "Who has at least one commit? Thumbs up." [Most hands.] "You've saved a snapshot. Even if you delete everything in that file tomorrow, this version still exists. That's version control."

---

### Step 3: Change and Commit Again (0:40–0:55)

Display Slide 3:

> Change something in your file. Add a sentence, delete a paragraph, fix a spelling mistake — anything.
> Then commit again. Read the message AI proposes. Is it accurate?
>
> Now you have two snapshots. Two moments in time. You can go back to either one.

**CLI path:**

```
copilot "I changed my goal document. Commit."
```

AI proposes a message. Student reads, evaluates, accepts or revises.

**Web path:**

> Open the file on GitHub, click the pencil icon to edit, make a change. Read the suggested commit message. Change it if it doesn't describe what you actually did. Click "Commit changes."

Students who finish early: add a second file (Decision Log, file system map) as a new commit. Each time, read AI's proposed message and decide: keep, revise, or replace?

**Pair activity (0:50–0:55):** "Show your partner your two commit messages. Did AI describe your changes accurately? Did you have to change anything? What did you change and why?"

---

### Folder Creation Moment (0:55–1:00)

For students who only created 5 folders in Week 1:

> "Remember in Week 1 you only created a few folders? Now ask AI to create the rest."

**CLI path:**

```
copilot "Create folders week-02 through week-14 in my geap-103 directory"
```

**Web/other path:** Students create folders manually, or ask their AI tool "Create a list of folder names from week-02 to week-14 that I can copy." Then create them.

This is a 3-minute activity that delivers the Week 1 promise: "Next week you can ask AI to do this for you."

---

## Break (1:00–1:15)

---

## Segment B: Restore + Partner Commits (1:15–2:00)

### Step 4: View Your History (1:15–1:30)

Display Slide 4:

> Now the important part. Look at your old version — the one before you changed it. It's still there.
>
> Frame: "Show me what my file looked like before I changed it."

**CLI path:**

```
copilot "Show me what my goal document looked like in my first commit"
```

**Web path:**

> On your repository page, click on the file, then click "History." Click on your first commit. You'll see the old version.

**Important: this is viewing, not overwriting.** Students are looking at an old snapshot. Their current file is untouched. Actual file restoration (overwriting the current version with an old one) happens later in the course when students need it — and that's when you name it.

> You just looked back in time. Your earlier work is still there. Even after you changed it, the old version was saved.

Circulate. This is the moment that makes version control real. Watch for students who get it — their face changes when the old version appears.

| What you see | What to say | What you're naming |
|-------------|------------|-------------------|
| Student saw the old version | "That's your history. Every *snapshot* you saved is still there." | snapshot |
| Student confused about which version they're looking at | "How many commits do you have? Each one is a *snapshot*. You're looking at an earlier one. Your current file hasn't changed." | snapshot |
| Student accidentally overwrote their current version (CLI did a restore instead of a view) | "That's fine — your most recent commit is still saved. Ask AI: 'Show me my most recent version.'" | This is a teaching moment, not a disaster. |
| Student got an error | "Read it aloud. What does it say?" | troubleshoot |

**This is Git Episode 1 (Restore) for the Git Episodes assessment.** Students who view an earlier version can document this as evidence. Mention it: "If you just looked at an earlier version of your file, you've started one of the three Git Episodes you need this semester. Save a screenshot or copy the output."

---

### Partner-Guided Commits (1:30–1:55)

This is a speaking activity disguised as a Git activity. Pairs evaluate AI-generated commit messages together.

Display:

> **Partner A:** Make a change to one of your files. Commit. Don't change AI's message yet.
> **Partner B:** Read the commit message AI proposed. Then ask:

**Sentence frames for the evaluating partner** (display on slide):

- "What did you actually change?"
- "Does AI's message describe that accurately?"
- "What's missing from the message?"
- "How would you make it more specific?"

> If the message is wrong or vague, Partner A revises it and commits again.
> Then switch roles.

The instructor's role: listen for the evaluation language, not the Git. Are students noticing when AI's description doesn't match what they actually did? Are they articulating what's wrong?

| What you hear | What to say |
|--------------|------------|
| Partner B says "it's fine" without reading carefully | "Read it aloud. Now Partner A, tell them what you actually changed. Do they match?" |
| Student notices AI got the description wrong | "Good catch. What's the difference between what AI said and what you did? That's *evaluation* — the same skill from Week 2." |
| Student revises the message to be more specific | "Read the new version to your partner. Better? That's the revision cycle: AI proposes, you evaluate, you improve." |
| Pair is stuck on the tool | "What are you trying to do? Say it in English first, then tell AI." |
| One partner is on CLI, the other on web | "That's fine. The questions are the same: 'What did AI say? What did you actually do? Do they match?'" |
| Pair finished quickly | "Try this: one partner makes a change on purpose and doesn't say what it was. Commit. The other partner reads ONLY the commit message and guesses what changed. Then check. Did the message give enough information?" |

---

### Push to GitHub (1:55–2:00)

Display Slide 5:

> **Push** means putting your repository online — safe, backed up, shareable.

**CLI path:**

```
copilot "Push my repository to GitHub"
```

**Web path:** If students have been working on github.com directly, their work is already online. For GitHub Desktop users: click "Push origin."

> "Go to github.com and find your repository. You should see your commits listed with your messages. That's your work history. It's safe."

---

## Segment C: Goal Document + Session Review (2:00–2:45)

### Goal Document Update (2:00–2:20)

> You've been writing about what you want for two weeks. Today: try to describe something that doesn't exist yet. This is harder. You have to use words like "it might be" and "it would look like" and "I imagine."

**Prompt** (display on slide):

> Think about the things you've been interested in. If you could make something with a computer, what kind of thing might it be? Describe what someone would see if they looked at it.

**Sentence frames** (display on slide):

- "I'm curious about making a _____ because _____."
- "It might look like _____, with _____."
- "I'm not sure yet, but I imagine something that _____."

**Model entry** (display briefly, then remove):

> "I'm curious about making a website for my family's restaurant because they don't have one. It might look like a page with the menu, some photos of the food, and a map showing where the restaurant is. I'm not sure yet, but I imagine something simple that my parents could update themselves."

**Writing** (12 min): Students write entry 3 in their Goal Document. First time practising speculative description. Aim for 4–5 sentences.

**Pair share** (8 min): "Can your partner picture what you described? What would someone see? What would it do?"

---

### Debrief + Next Week Preview (2:20–2:25)

> Today you learned to protect your work — snapshots you control, that you can always go back to. You also practised describing something that doesn't exist yet. Both skills matter all semester.

Quick check: "What's a commit?" "What's a repository?" "What does restore mean?" (volunteers)

> Next week is a check-in. You'll show what you've done, explain your work to someone, and reflect on what you've learned so far. Your file-system artifact is due: your geap-103 folder in OneDrive should be organized, and your portfolio repository should have at least 2–3 commits.

---

### AI Session Review (2:25–2:45)

**Student review (2:25–2:38)**

Display:

> Open a new document in your week-03 folder (or continue in the CLI). Name it `week03-review-yourname.docx`.
>
> **Voice mode encouraged.**
>
> **First, say or paste this:** "Speaking practice. I'm a B1 English student practising explaining my work. Ask me follow-up questions. If my explanation is vague, tell me what's unclear and ask me to be more specific. Don't do the explaining for me."
>
> **Then, your task:** Explain to AI what a commit message is and why the one you wrote today was better than what AI originally suggested. AI will play a classmate who doesn't understand Git — answer its questions.
>
> Start with: "Today I learned about version control. A commit message is _____. AI suggested _____ for my commit message, but I changed it to _____ because _____."
>
> When AI asks follow-up questions (like "Why does it matter?" or "What would happen if you didn't change it?"), try to answer. You're practising explaining technical decisions — the same skill you'll use next week when you explain your work to two partners.

Students have a short exchange with AI (8–10 min). Spoken or typed – voice is better. Save the conversation.

**What this practises:** Explaining a technical decision to someone who doesn't share your context. This is a direct rehearsal for the Week 4 triad defence, where students explain one piece of work to two partners. Students who practise here will be noticeably more comfortable next week.

**Pair share** (5 min): "What question did AI ask that was hardest to answer? How did you handle it?"

**Instructor reflection on projector (2:38–2:45)** — cut this if time is short.

Ask AI:

> "My B1 students just learned Git through AI-assisted commands. Some used the CLI, some used the web interface. They practised commits, restores, and writing commit messages. Next week they present their work for the first time. What should I watch for?"

Read together. Brief reaction.

---

## Catch-Up Instructions for Latecomers

### If You Missed Week 3

In Week 3, we learned version control — how to save snapshots of your work so you can always go back.

**1. Create a GitHub account** if you don't have one: github.com/signup. Use your Humber email. Apply for the [Student Developer Pack](https://education.github.com/pack) (free).

**2. Create a repository called `geap-103-portfolio`.**

- If you have the CLI: `copilot "Create a Git repository here and connect it to a new GitHub repository called geap-103-portfolio"`
- If not: go to github.com, click "New repository," name it `geap-103-portfolio`

**3. Add at least one file and commit it.** Upload your Goal Document or a Decision Log. Write a commit message describing what it is (e.g., "Added goal document from weeks 1-3").

**4. Try restoring.** Make a change to the file, commit again, then go back to the earlier version. This is the key skill from Week 3.

**5. Read and recognise these 5 words.**

| Term | Meaning |
|------|---------|
| **repository** | A folder with a memory — it keeps your work and every version of it |
| **commit** | Saving a snapshot — telling the repository "remember this version" |
| **snapshot** | What your files look like at one moment in time |
| **restore** | Going back to an earlier snapshot |
| **push** | Putting your repository online so it's safe and shareable |

**6. Update your Goal Document.** Write entry 3: describe something you might want to make with a computer. Use "I imagine..." or "It might look like..."

---

## Instructor Prep Checklist

- [ ] AI tool accessible on projector (CLI recommended for demo — Git commands are natural language)
- [ ] GitHub account: confirm you can sign in and create a repository on the projector
- [ ] Vocabulary reference slide ready (5 terms in table — displayed as silent reference, not pre-taught). Print copies or plan for students to photograph if single-projector room.
- [ ] Five progression slides ready (Create repo → First commit → Change and commit → Restore → Push). Reveal progressively during practice.
- [ ] Verify: do most students have GitHub accounts? (Created in Week 1 or via catch-up instructions.) Plan for 2–3 stragglers who don't.
- [ ] Know common Git errors: authentication failures, "not a git repository," empty commit message. For each: what does the error say, and what should the student do?
- [ ] Goal Document prompt + sentence frames on a slide
- [ ] Reminder slide: Week 4 file-system artifact is due (organized folder + 2–3 commits)

---

## Assessment Alignment

- No graded assessment this week (Week 4 file-system artifact due next week)
- CLO 1 continues (manage files + versions — Git as version control)
- CLO 2 previewed (troubleshoot — reading error messages during Git practice)
- CLO 3 continues (guide AI tools — using AI to execute Git commands)
- CLO 5 continues (communicate — commit messages are short technical writing)
- **Git Episode opportunity:** students who restore an earlier version can document this as their Restore episode (1 of 3 required)
- Goal Document updated (ungraded; instructor reads at Week 4)

---

## Language Development Summary

| Skill | Activity |
|-------|----------|
| **Vocabulary** | 5 terms (repository, commit, snapshot, restore, push) displayed as reference, named by instructor during practice |
| **Speaking** | Warm-up lost-work stories; partner evaluation of AI commit messages ("What did you actually change? Does AI's message match?"); pair Goal Document share; pair session review share |
| **Reading** | AI-proposed commit messages (evaluating accuracy); GitHub interface text; error messages; AI-generated session review |
| **Writing** | Revising AI commit messages (short evaluative editing); Goal Document entry (~50–100 words; speculative description); session review document |
| **Listening** | Partner's guidance during commits; partner's imagined project; AI session review response |

---

## Timing Summary

| Segment | Time | Minutes | Notes |
|---------|------|---------|-------|
| Warm-up | 0:00–0:10 | 10 | Lost work stories, framing |
| Step 1: Create repo | 0:10–0:25 | 15 | Account creation absorbed here; CLI and web paths |
| Step 2: First commit | 0:25–0:40 | 15 | Add file, write commit message, circulate |
| Step 3: Change + commit | 0:40–0:55 | 15 | Second commit, pair check of messages |
| Folder creation moment | 0:55–1:00 | 5 | AI creates remaining week folders |
| **Break** | **1:00–1:15** | **15** | |
| Step 4: Restore | 1:15–1:30 | 15 | Git Episode opportunity |
| Partner-guided commits | 1:30–1:55 | 25 | Speaking activity: directing partner through commits |
| Push to GitHub | 1:55–2:00 | 5 | Put it online |
| Goal Document | 2:00–2:20 | 20 | Speculative description |
| Debrief + preview | 2:20–2:25 | 5 | Vocab check, Week 4 prep reminder |
| Session review (student) | 2:25–2:38 | 13 | AI exchange + pair share |
| Session review (instructor) | 2:38–2:45 | 7 | Cut if time is short |
| **Total** | | **150 min instruction** | |
