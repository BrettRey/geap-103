# GEAP 103 Week 3: Instructor Materials Package

**Title:** Never Losing Work Again
**Phase:** Discovery (Week 3 of 14)
**Contact time:** 3 × 55 min (165 min total: 150 min instruction + 15 min break)
**Date prepared:** 2026-03-27

This file contains everything you need to prepare slides and run the class for Week 3. The lesson plan (`lesson-plans/week-03.md`) has the pedagogical rationale. This file has the concrete content. In case of conflict, the lesson plan governs.

**Week 3 design note:** Students have been making things for two weeks. They have files scattered across their geap-103 folder. Today they learn to protect them: version control as a timeline of snapshots they control. Git/GitHub is the preferred portfolio path, but local Git and document/cloud version history are supported evidence paths. The skill is naming versions clearly, changing a file, and recovering an earlier version as a usable file.

**AI tools:** Same tool-agnostic approach as Week 2. AI assistance is optional. Students may use GitHub web, local Git, or the version-history interface already available in their document/cloud tool.

**GitHub registration is not a timed-class gate.** A regular free GitHub account is sufficient; GitHub Education and Copilot are optional and may still be pending. Education verification requires each student to provide their own current documentation; after approval, allow 72 hours for Copilot Student activation. Instructors must not collect, inspect, or transmit students' identity documents. Students whose accounts or tools are blocked start immediately on the local-Git or document/cloud version-history path.

---

## Segment A: Hook + First Commits (0:00–1:00)

### Warm-Up (0:00–0:10)

> You've been making things for two weeks: a file system, AI conversations, Decision Logs, a Goal Document. Has anyone ever lost something they were working on? Deleted it by accident? Wanted to go back to an earlier version?

Pairs: "Tell your partner about a time you lost work or couldn't find something." Frame: "I was working on _____ and then _____." Partner A speaks first (1 min), then Partner B (1 min).

1–2 volunteers share with the class.

Then:

> Today we fix that. You're going to learn how to save snapshots of your work so you can always go back. It's called version control.

---

### Version-History Readiness Check (start of Step 1)

Ask students to open the version-history route they can use today:

> "Choose one: GitHub in a browser, Git on this computer, or version history in your document/cloud tool. Raise your hand when you can see the file or folder you will use."

After three minutes, route anyone still blocked to the prepared local file and a version-history tool available on their device. A student may continue ordinary GitHub registration outside the activity, but should not wait for registration or Education verification before beginning.

---

### Step 1: Create a Repository (0:10–0:25)

Display Slide 1:

> A **repository** is a place where your work and its history are kept. Think of it as a folder with a memory — it remembers every version of every file.
>
> Create one now for your course work.

**Local Git path:**

> In your terminal, navigate to your geap-103 folder and type:

Display:

```
git init
```

**GitHub web path:**

> Go to github.com. Click "New repository." Name it `geap-103-portfolio`. Then upload one file from your geap-103 folder.

**Document/cloud version-history path:**

> Open a course file in OneDrive, Google Drive, or another approved tool with version history. Find **Version history**, then save or name the current version. Record which tool and file you used.

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

Circulate. **Budget 10 minutes here.** Students who finish early start Step 2.

**If a route fails:** Keep the instructor demonstration visible, but do not treat watching or copying it as student evidence. Move affected students to the prepared document/version-history path. Partner screen-sharing may support navigation, but each student must later produce their own saved and recovered versions.

---

### Step 2: First Commit (0:25–0:40)

Display Slide 2:

> Add a file to your repository. AI will propose a **commit message** — a short description of what you're saving. Read it. Does it accurately describe what this file is?
>
> If not, change it. The commit message is a note to your future self. "Updated file" tells you nothing. "Added goal document from weeks 1–2" tells you exactly what happened.

**Local Git path:**

```
git add "Goal Document.docx"
git commit -m "Added goal document from Weeks 1-2"
```

The CLI will propose a commit message. The student reads it and either accepts, modifies, or rejects it — the same cycle from Week 2.

**Web path:**

> On your repository page, click "Add file" → "Upload files." Choose a file from your geap-103 folder. GitHub suggests a commit message. Read it. If it doesn't describe your file accurately, change it. Click "Commit changes."

**Document/cloud version-history path:**

> Name the current version so a future reader can identify it, for example, "Goal document before Week 3 revision." If the tool does not support names, record the timestamp and add the description to your evidence note.

**What to say while circulating:**

| What you see | What to say | What you're naming |
|-------------|------------|-------------------|
| Student created a repo | "Good. That's your *repository*. Now let's put something in it." | repository |
| Student added a file and AI proposed a message | "Read the message. Does it describe what you actually added? If not, change it." | commit message as evaluation (CLO 4) |
| Student accepted "updated file" or a vague message without reading | "Your future self reads this in 3 months. Will they know what this file is? What would be more specific?" | The commit message is a review exercise, not a writing exercise. |
| Student revised the AI's message to be more specific | "Good. You just evaluated AI's description and made it better. That's the same skill from Week 2." | revise, evaluate |
| Student committed successfully | "You just saved a *snapshot*. Even if you change the file later, this version still exists." | snapshot, commit |
| Student got an error | "Read the error message aloud. What is it asking you to do?" | troubleshoot (CLO 2 preview) |
| Student's tool won't cooperate | "After two focused attempts, move to another path. Your partner may help you navigate, but you still need your own saved versions." | — |

**At ~0:35, brief pause:**

> "Who has at least one commit? Thumbs up." [Most hands.] "You've saved a snapshot. Even if you delete everything in that file tomorrow, this version still exists. That's version control."

---

### Step 3: Change and Commit Again (0:40–0:55)

Display Slide 3:

> Change something in your file. Add a sentence, delete a paragraph, fix a spelling mistake — anything.
> Then commit again. Read the message AI proposes. Is it accurate?
>
> Now you have two snapshots. Two moments in time. You can go back to either one.

**Local Git path:**

```
git add "Goal Document.docx"
git commit -m "Added Week 3 project description"
```

AI proposes a message. Student reads, evaluates, accepts or revises.

**Web path:**

> Open the file on GitHub, click the pencil icon to edit, make a change. Read the suggested commit message. Change it if it doesn't describe what you actually did. Click "Commit changes."

**Document/cloud version-history path:** Save or name the changed version, using a description such as "Added Week 3 project description."

Students who finish early: add a second file (Decision Log, file system map) as a new commit. Each time, read AI's proposed message and decide: keep, revise, or replace?

**Pair activity (0:50–0:55):** "Partner A goes first: show your partner your two commit messages. Did AI describe your changes accurately? Did you have to change anything? What did you change and why? (2 min.) Then Partner B. (2 min.)"

---

### Folder Creation Moment (0:55–1:00)

For students who only created 5 folders in Week 1:

> "Remember in Week 1 you only created a few folders? Now ask AI to create the rest."

**CLI path:** Start an interactive session with `copilot`. At its prompt, enter:

```
Create folders week-02 through week-14 in my geap-103 directory.
```

Read the proposed action and approve only the course-folder change you understand.

**Web/other path:** Students create folders manually, or ask their AI tool "Create a list of folder names from week-02 to week-14 that I can copy." Then create them.

This is a 3-minute activity that delivers the Week 1 promise: "Next week you can ask AI to do this for you."

---

## Break (1:00–1:15)

---

## Segment B: Restore + Partner Commits (1:15–2:00)

### Step 4: Recover an Earlier Version (1:15–1:30)

Display Slide 4:

> Now the important part. Recover your old version — the one before you changed it — as a usable file. Keep the current version too.
>
> Frame: "Show me what my file looked like before I changed it."

**CLI path:**

```
git show HEAD~1:"Goal Document.docx" > "Goal Document recovered.docx"
```

**Web path:**

> On your repository page, open the file's History, select the earlier commit, then download that version as `Goal Document recovered` or copy its contents into a clearly labelled recovered file.

**Document/cloud version-history path:** Open Version history, select the earlier version, and use **Download**, **Make a copy**, or the tool's safe **Restore** command. If Restore replaces the current version, first duplicate or download the current file so both versions remain available.

> You just recovered earlier work. Open the recovered file and identify one detail that proves it is the earlier version.

Circulate. This is the moment that makes version control real. Watch for students who get it — their face changes when the old version appears.

| What you see | What to say | What you're naming |
|-------------|------------|-------------------|
| Student recovered the old version | "Open it and point to the earlier content. That confirms the recovery worked." | restore/recover |
| Student only opened a history preview | "That proves the version exists. Now download, copy, or safely restore it so you have a usable recovered file." | evidence threshold |
| Student accidentally overwrote their current version (CLI did a restore instead of a view) | "That's fine — your most recent commit is still saved. Ask AI: 'Show me my most recent version.'" | This is a teaching moment, not a disaster. |
| Student got an error | "Read it aloud. What does it say?" | troubleshoot |

**This is the Restore/Recovery episode for the version-control assessment.** Evidence must show the before state, the recovery action, and the usable recovered result. A history screen or instructor demonstration alone is not enough.

---

### Partner-Guided Commits (1:30–1:55)

This is a speaking activity disguised as a Git activity. Pairs evaluate AI-generated commit messages together.

Display:

> **Partner A goes first:** Make a change to one of your files. Commit. Don't change AI's message yet.
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

### Remote Copy or Recovery Check (1:55–2:00)

Display Slide 5:

> **Push** means putting a local Git repository online. If you are using another version-history path, use this time to confirm that both the current and recovered versions open.

**CLI path:** In an interactive `copilot` session, enter:

```
Push my repository to GitHub.
```

Read the proposed command and destination before approving it. If authentication or repository permissions fail, keep the local version evidence and move on.

**Web path:** If students have been working on github.com directly, their work is already online. For GitHub Desktop users: click "Push origin."

> "Confirm the result in your own path: identify the current version, the earlier snapshot, and the recovered file. If you pushed to GitHub, open the remote repository and verify the commits are there."

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

**Pair share** (8 min): "Can your partner picture what you described? What would someone see? What would it do?" Partner A describes first (3 min), then Partner B (3 min).

---

### Debrief + Next Week Preview (2:20–2:25)

> Today you learned to protect your work — snapshots you control, that you can always go back to. You also practised describing something that doesn't exist yet. Both skills matter all semester.

Quick check: "What's a commit?" "What's a repository?" "What does restore mean?" (volunteers)

> Next week is a check-in. You'll show what you've done, explain your work to someone, and reflect on what you've learned so far. Your file-system artifact is due: your geap-103 folder may be local or cloud-based and should be organized. Bring evidence of two named versions and one actual recovery in the path you used.

---

### Bridging Activity (2:25–2:27)

Display:

> In two minutes, you'll explain commit messages to AI – specifically, why your commit message was better than what AI would have suggested. Before you open voice mode, do this: look at one of your commit messages from today. Think about what it says and why you wrote it that way. What would a generic message like "updated file" miss?

Two minutes of silence. Students look at their work and prepare.

*This bridges the register shift from reflective Goal Document writing to confrontational session review. Students retrieve specific content and switch from reflective to explanatory mode before the voice interaction begins.*

---

### Session Review -- Speaking Practice (2:27–2:39)

Display:

> **Open your AI tool. Start a new chat.**
>
> **First, say this (or paste it if using text):**
> "Speaking practice. I'm a B1 English student practising explaining my work. Ask me follow-up questions. If my explanation is vague, tell me what's unclear and ask me to be more specific. Don't do the explaining for me."
>
> **Then, your task:** Explain what a commit message or named-version label is and why a specific description is better than a generic one.
>
> Start with: "Today I learned about version control. A commit message is _____. AI suggested _____ for my commit message, but I changed it to _____ because _____."
>
> When AI asks follow-up questions (like "Why does it matter?" or "What would happen if you didn't change it?"), try to answer. You're practising explaining technical decisions — the same skill you'll use next week when you explain your work to two partners.

AI role: Confused classmate who doesn't understand Git.

**Routes:** Prefer AI voice. If it is unavailable, use a typed AI exchange that the student reads aloud, or a live partner/instructor role-play with the same follow-up questions.

Students talk to AI for 10–12 minutes, explaining what a commit message is, why it matters, and why a specific, descriptive message is better than a generic one. The AI plays confused: "What do you mean, a snapshot? Why can't I just call it 'my file'? Why does the message matter?"

Instructor circulates and listens. No intervention unless a student is stuck or silent.

**What to listen for:**

| What you hear | What it means |
|--------------|---------------|
| Student explains commit messages with specific examples | Good production – the technical explanation skill is developing |
| Student says "it's important" and AI pushes back | The system is working – AI is demanding specificity |
| Student is silent | Approach quietly: "Start with one thing. What did you save today?" |
| Student and AI are having a genuine back-and-forth | Let it run. This is the goal. |

**If using AI voice:** Voice mode starts a new chat. The prompt is said aloud or pasted at the start. The learning target is the student's explanation and follow-up answers, not access to voice mode.

**What this practises:** Explaining a technical decision to someone who doesn't share your context. This is a direct rehearsal for the Week 4 triad defence, where students explain one piece of work to two partners. Students who practise here will be noticeably more comfortable next week.

---

### Self-Check (2:39–2:40)

> Write one sentence: what did AI ask you to clarify?

*This is a 1-min diagnostic – if you can't write that sentence, the session didn't work.*

---

### Pair Share (2:40–2:43)

> "What question did AI ask that was hardest to answer? How did you handle it?"

Partner A shares first (1 min), then Partner B (1 min).

---

### Closing (2:43–2:45)

> "Today you learned two things: how to protect your work so you never lose it, and how to describe something that doesn't exist yet. Both are skills you'll use all semester."

**Specific prep for Week 4:** "Your file-system artifact is due next week. Make sure your local or cloud GEAP 103 folder is organized with clear names. Bring evidence of two named versions and one actual recovery in your chosen path."

---

## Catch-Up Instructions for Latecomers

### If You Missed Week 3

In Week 3, we learned version control — how to save snapshots of your work so you can always go back.

**1. Choose a path you can use now:** GitHub web, local Git, or version history in a document/cloud tool. A regular GitHub account is enough. The Student Developer Pack is optional and requires your own current documentation; after Education approval, allow 72 hours for Copilot Student activation. Do not send documents to your instructor.

**2. Establish a version-history location.** Create a repository called `geap-103-portfolio`, or choose a course file in a tool with version history.

- If you have the CLI: start an interactive `copilot` session, then enter `Create a Git repository here and connect it to a new GitHub repository called geap-103-portfolio.` Read the proposed commands before approving them.
- If not: go to github.com, click "New repository," name it `geap-103-portfolio`

**3. Add at least one file and commit it.** Upload your Goal Document or a Decision Log. Write a commit message describing what it is (e.g., "Added goal document from weeks 1-3").

**4. Recover an earlier version.** Make a change and save a second named version. Then download, copy, or safely restore the earlier version as a usable file. Keep evidence of the before state, action, and result; merely viewing the history is not enough.

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

- [ ] Instructor-owned GitHub/local-Git example and non-Git version-history example accessible on the projector
- [ ] Vocabulary reference slide ready (5 terms in table — displayed as silent reference, not pre-taught). Print copies or plan for students to photograph if single-projector room.
- [ ] Five progression slides ready (Create repo → First commit → Change and commit → Restore → Push). Reveal progressively during practice.
- [ ] Three paths posted: GitHub web, local Git, and document/cloud version history. Prepare a downloadable practice file for students whose usual path is blocked.
- [ ] Know common failures: authentication, permissions, missing history, "not a git repository," and unclear version names. After two focused attempts, route the student to another path and log the unresolved issue.
- [ ] Goal Document prompt + sentence frames on a slide
- [ ] Session review slide: role-setting prompt + Week 3 scenario ("Explain what a commit message is and why yours was better than AI's suggestion")
- [ ] Reminder slide: Week 4 file-system artifact is due (organized folder + two named versions + one actual recovery)

---

## Assessment Alignment

- No graded assessment this week (Week 4 file-system artifact due next week)
- CLO 1 continues (manage files + versions — Git as version control)
- CLO 2 previewed (troubleshoot — reading error messages during Git practice)
- CLO 3 continues (guide AI tools — using AI to execute Git commands)
- CLO 5 continues (communicate — commit messages are short technical writing)
- **Version-control episode opportunity:** students who recover an earlier version as a usable file can document the Restore/Recovery episode; a history preview alone is insufficient
- Goal Document updated (ungraded; instructor reads at Week 4)
- **Session review** (formative, not graded): Week 3 scenario practises explaining a technical concept to a non-expert – builds toward Micro-Defence 1 (Week 4, 3 criteria: clear description, terminology, explaining a decision)

---

## Language Development Summary

| Skill | Activity |
|-------|----------|
| **Vocabulary** | 5 terms (repository, commit, snapshot, restore, push) displayed as reference, named by instructor during practice |
| **Speaking** | Warm-up lost-work stories; partner evaluation of AI commit messages ("What did you actually change? Does AI's message match?"); pair Goal Document share; **session review** (12 min AI voice interaction: explaining a technical decision to a confused non-expert – the first scenario requiring explanation of a concept, not just narration of an experience); pair session review share |
| **Reading** | AI-proposed commit messages (evaluating accuracy); GitHub interface text; error messages |
| **Writing** | Revising AI commit messages (short evaluative editing); Goal Document entry (~50–100 words; speculative description); session review self-check sentence |
| **Listening** | Partner's guidance during commits; partner's imagined project; AI follow-up questions during session review |

---

## Timing Summary

| Segment | Time | Minutes | Notes |
|---------|------|---------|-------|
| Warm-up | 0:00–0:10 | 10 | Lost work stories, framing |
| Step 1: Create repo | 0:10–0:25 | 15 | Account verification + creation; CLI and web paths |
| Step 2: First commit | 0:25–0:40 | 15 | Add file, write commit message, circulate |
| Step 3: Change + commit | 0:40–0:55 | 15 | Second commit, pair check of messages |
| Folder creation moment | 0:55–1:00 | 5 | AI creates remaining week folders |
| **Break** | **1:00–1:15** | **15** | |
| Step 4: Restore | 1:15–1:30 | 15 | Git Episode opportunity |
| Partner-guided commits | 1:30–1:55 | 25 | Speaking activity: directing partner through commits |
| Push to GitHub | 1:55–2:00 | 5 | Put it online |
| Goal Document | 2:00–2:20 | 20 | Speculative description |
| Debrief + preview | 2:20–2:25 | 5 | Vocab check, Week 4 prep reminder |
| Bridging activity | 2:25–2:27 | 2 | Pick a commit message, rehearse justification |
| Session review (student) | 2:27–2:39 | 12 | AI voice: explain commit messages to confused classmate |
| Self-check | 2:39–2:40 | 1 | One sentence: what did AI ask you to clarify? |
| Session review (pair share) | 2:40–2:43 | 3 | Hardest question from AI |
| Closing | 2:43–2:45 | 2 | Week 4 prep reminder |
| **Total** | | **150 min instruction** | |
