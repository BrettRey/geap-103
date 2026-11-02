# Class plan: Monday, October 5, 2026 (Week 4)
<!-- SUMMARY: Teacher plan for the Monday section's Week 4 meeting: milling, terminology review, guide update and syncing, assessment announcement, in-class writing 1, a demonstration on versions and Git basics (commit, clean and dirty trees, push, pull, clone, fork), and conferences (Sigrid observing) · status: ready; all student materials published 2026-10-04; milling 30 minutes · updated: 2026-10-04 -->

Timing assumes a 160-minute meeting with a 15-minute break, with milling taking the first 30 minutes. If the Monday meeting is shorter, shorten work time first.

## Before class

- **Everything students need is published:** the guide (folder and zip), the announcement, both section schedules, and these milling questions.
- **Nothing to print.** Display the milling questions and the announcement. Students write the in-class task by hand on their own paper. Conferences go straight into the spreadsheet: `private/GEAP103B-Mon-tracker-2026-fall.xlsx` in the course folder, already filled with the Monday class list. The Wednesday section's tracker is `private/GEAP103A-Wed-tracker-2026-fall.xlsx`. Both stay in Humber OneDrive and out of the public repository.
- **Demo setup is done.** `~/GEAP103/demo` (the GEAP103 folder in your home folder) has the club notes, a checked `club-message.md`, and a `work-log.md`, as if you had finished Task 3. It's outside iCloud's synced Desktop and Documents, which is where Git repositories belong. In Copilot, add it as a project (**Local folder or repository**) before class. The same `~/GEAP103` folder also holds `student-guide` (the current guide) and `practice` (with the Task 3 files). Add `~/GEAP103/practice` in Copilot too, in place of the old `Documents/GEAP103/practice` project.

## Timeline

| Time | Block |
|---|---|
| 0:00–0:30 | Milling, ending with the terminology review |
| 0:30–0:50 | One course folder, and the agent updates the guide |
| 0:50–1:00 | How you'll be assessed |
| 1:00–1:10 | In-class writing 1 |
| 1:10–1:25 | Break |
| 1:25–2:00 | Demonstration: versions, from copies to Git |
| 2:00–2:35 | Work time and conferences |
| 2:35–2:40 | Close |

## 1. Milling and terminology review (30 minutes)

Use `materials/milling-2026-10-05.md`. Give students different starting numbers. Question 2 is the conference question, so it doubles as rehearsal.

- **0:00–0:02.** Students read the questions and choose where to start.
- **0:02–0:22.** Mingle. Give a signal every three minutes or so to change partners, which gives each student about six conversations. Ask them to use at least four different questions. Listen to questions 3, 4, and 5. They lead into the terminology review and the guide update.
- **0:22–0:30.** Back together. Take two or three ideas from questions 1, 2, and 7, then move to the terminology review below.

**Terminology review (the last few minutes).** Display six descriptions. Pairs say which term fits, then you confirm.

| Description | Term |
|---|---|
| "I open it on my laptop, choose a project, and start a session." | Copilot, the harness |
| "Opus 5.5" | A model |
| "It read the club notes and saved `club-message.md` in my folder." | An agent |
| "I use it in my web browser. It only sees what I paste or upload." | A chat interface |
| "My portfolio repository is stored here, online." | GitHub |
| "One conversation with the agent, which I can reopen later." | A session |

Then two quick questions to the class: "Can a chat interface change a file on your computer? Can an agent?" Add the brand point: Microsoft uses the name Copilot for many products, and GitHub Copilot is one of them. In this course, Copilot means the GitHub Copilot app.

Optional two-minute contrast: ask a chat interface and the agent in Copilot the same thing, "Read `club-message.md` and tell me the meeting time." The chat interface can't open the file; the agent can.

## 2. One course folder, and the agent updates the guide (20 minutes)

**Why.** From today, everything for the course lives in one folder called `GEAP103`, in the home folder: the guide, the practice work, and later the repositories. It's outside OneDrive and any synced Desktop or Documents, because syncing can damage Git's records. The guide also changed: it uses the words from the review, and it shows a date under "GEAP 103". Getting the new guide is a job for the agent. It needs a download from the internet, a new folder, and a check that nothing is overwritten. A chat interface couldn't do it.

**Step 1: the agent makes the folder and gets the guide.** Students copy this into Copilot, in their current practice-folder session:

> Make a folder called `GEAP103` in my home folder, if it doesn't exist. Download the GEAP 103 student guide from https://github.com/BrettRey/geap-103/raw/main/materials/self-paced-student-guide-2026-09-22/student-guide.zip and extract it into `GEAP103/student-guide`. If `GEAP103/student-guide` already exists, rename it `student-guide-old` first. Don't delete or change any other files. Then tell me the full path of `GEAP103` and the date under "GEAP 103" in the new `index.html`.

Before approving each permission request, students read it aloud to a partner. What will the agent run? Which address will it download from, and where will it save? The address should start with `https://github.com/BrettRey/geap-103`, and the folder should be in the home folder. Writing outside the practice folder may need a permission. That's expected, and worth reading carefully.

**Step 2: move the practice folder by hand.** Close the session. In Finder or File Explorer, move the `practice` folder into `GEAP103`. If it's inside an old guide folder, move it out into `GEAP103`. The home folder opens with Shift-Command-H on a Mac. On Windows, it's This PC, then C:, then Users, then the student's name.

**Step 3: reconnect Copilot.** In Copilot, remove the old practice project and add `GEAP103/practice` (**Local folder or repository**). Start a session and ask: "List the files in this folder." Check that `club-message.md` and `work-log.md` are there.

**Step 4: check the guide yourself.** Open `GEAP103/student-guide/index.html`, check the date "Updated October 4, 2026", and bookmark it. Task 1, step 2 in the guide describes the same folder for anyone who missed today.

Partners take turns typing. Early finishers write the step 1 request in their own words and compare.

**If it goes wrong.** If the agent can't make the folder, download, or extract, students describe the message to you, which is Task 2's troubleshooting practice. Then they make `GEAP103` by hand and download the zip in a browser from the course page.

**Pairs discuss (five minutes):** "How will you know when the guide changes, and how will you get the new version?" Put options on the board:

1. When the teacher says the guide has changed, ask the agent to download it again into `GEAP103/student-guide`, renaming the old one first, and to tell you what changed.
2. Bookmark an online version that is always current.
3. Ask the agent to keep a copy of the course repository and get updates. This is called *pulling*, and Task 9 practises it.

Frames: "The easiest way is … because …", "If I'm offline, …", "I'd know it's new because the date …", "I'd ask the agent to …"

**Teacher note.** All three options work now that the guide folder is published. Option 1 adds a natural extra job for the agent: "tell me what changed". For option 2, the always-current link is https://brettrey.github.io/geap-103/materials/self-paced-student-guide-2026-09-22/. For option 3, the copy is a Git repository, so it must go in a folder that doesn't sync. A student can ask: "Clone https://github.com/BrettRey/geap-103 into a folder called `GEAP103/course-repo` in my home folder, not in Documents, Desktop, or OneDrive. Don't change anything in it. Tell me the full path." On Windows, the home folder is `C:\Users\<name>`. Later: "Pull the latest changes in `course-repo` and tell me what changed in the student guide." That's a preview of Tasks 7 and 9, so offer it to students who finish early.

## 3. How you'll be assessed (10 minutes)

Use `materials/assessment-announcement-2026-10.md`. Cover what's cancelled, the four parts and weights, the three things to show in conferences, the levels, and the pass rule. Check understanding with two questions: "What do you need to pass?" (every outcome at level 2) and "How many times do you need to show level 3?" (twice, at least once without AI). Say that conferences start today.

## 4. In-class writing 1 (10 minutes)

By hand, no AI, no notes, no partner, ten minutes on a visible timer. Display the prompt from the Week 4 materials:

> Describe something you tried to do with AI this semester. What happened? What would you do differently?
>
> Write about 50–100 words.

Collect the papers. Later, enter each mark in the Grades sheet and log a Writing row in the Log sheet for any outcomes it shows. It usually shows outcomes 3, 4 and 5, and sometimes 2.

## 5. Demonstration: versions, from copies to Git (35 minutes)

Task 4 says students can use "version history or Git" instead of a copy, so this block explains both. The agent will run Git for them, but they need to know what each action does before they approve it. Getting an earlier version back is also one of the three things every student must show in a conference.

**Ideas (about 8 minutes).** Build this on the board as you go:

```
your files now          your saved versions            GitHub (online)
(working tree)  --commit-->  (history)    --push-->    (remote)
                                         <--pull--
```

- A *version* is a saved state of a file at one moment. Undo only works while the file is open. A saved version lasts.
- **Three ways back.** A copy you make yourself, which is Task 4's first step. *Version history*: OneDrive keeps earlier versions of a file automatically, and you can restore one. *Git*: you choose when to record versions of a whole project folder.
- **Repository:** a project folder plus its recorded history.
- **Working tree:** the files as they are now, the ones you open and edit. Git calls a folder of files a *tree*.
- **Commit:** a version of the project you choose to record, with a short message about what changed. It works like a save point in a game: you can always go back to it.
- **Clean and dirty trees.** A tree is *clean* when nothing has changed since the last commit. It's *dirty* when you've changed files and haven't committed yet. Dirty isn't bad; it just means the changes aren't recorded. Before you ask an agent for a big change, check whether your tree is dirty.
- **Push and pull.** *Push* sends your commits to GitHub, so another computer or another person can get them. *Pull* gets commits from GitHub into your copy. This is how the guide reaches your computer.
- **Clone and fork.** A *clone* is your own copy of a repository on your computer. A *fork* is your own copy of someone else's repository on GitHub. You can change your fork without changing theirs; to suggest a change back, you open a pull request, which is Task 11.

**Demonstration part A: a copy (about 3 minutes).** This is Task 4's first step, quickly.

1. In the file manager, copy `club-message.md` and name the copy `club-message-before.md`. Say: "Now I have a way back, but only for this one file, and only because I remembered."

**Demonstration part B: Git with the agent (about 12 minutes).** Use `~/GEAP103/demo`, which has the club notes, `club-message.md`, and `work-log.md`. Before step 1, say why it's there: "A Git repository goes in a folder that doesn't sync. OneDrive, or iCloud's Desktop and Documents, can damage Git's records. GitHub is the backup once you push." Type each request in Copilot, and read every permission request aloud before approving it.

1. > Make this folder a Git repository. Then commit all the current files with the message "Start: checked club message".

   Say: "That's my first save point."
2. > Show me the Git status in plain English.

   It should report a clean working tree.
3. > Make `club-message.md` shorter. Keep every event detail and the final question.

   Then:

   > Show me the Git status and exactly what changed.

   Now the tree is dirty, and the agent shows the changed lines. Ask the class: "Is anything recorded yet?"
4. > Commit `club-message.md` with the message "Shorter message". Then show me the history.

   There are two commits, and the tree is clean again.
5. > Bring back `club-message.md` as it was in the first commit. Don't delete any history.

   The tree is dirty again, because bringing something back is also a change. Open the file and check it against the notes: "reply by Thursday at noon" is back.

   > Commit it with the message "Bring back the full message". Then show me the history.

   There are three commits now. Nothing was lost, including the shorter version.

**Demonstration part C: GitHub (about 5 minutes).** Open the course repository's history at https://github.com/BrettRey/geap-103/commits/main.

- Point to "Publish the student guide and update its terminology". Say: "I made this commit on my computer, then pushed it. When you ask the agent to pull, or to download the new guide, this is where it comes from."
- Point to the **Fork** button without clicking it. "A fork would be your own copy of my repository on GitHub."

**Model the conference explanation:**

> I committed the message before the change. The agent made it shorter, but it dropped the reply deadline. I brought back the version from my first commit. I know it's the right one because "reply by Thursday at noon" is back, and the history shows all three versions.

**Check in pairs (about 4 minutes).**

1. "Your tree is dirty. What does that mean? Is that a problem?"
2. "What's the difference between a push and a pull?"
3. "Why would you fork a repository instead of changing it?"
4. "In part A, what would you lose if you skipped the copy?"

**Board rule:** Git repositories go in a folder that doesn't sync, such as `~/GEAP103` or `C:\Users\<name>\GEAP103`.

**Board frames:** "I committed … before …", "The tree was dirty because …", "The agent changed …", "I brought back …", "I know it's the right version because …", "Push sends …; pull gets …"

**If Copilot fails live,** do part A by hand, explain part B with the board diagram, and show part C on GitHub, which doesn't need Copilot.

The guide's Task 4 now has a short "What are version history and Git?" box, and the Useful words list has Git, version history, clean working tree, clone, and fork. Students can reread those after the demonstration.

## 6. Work time and conferences (35 minutes)

Most students continue with Task 4, using a copy, version history, or Git. At five minutes each, about 25 minutes of conferencing fits five students, and the rest of the time goes to helping.

- Start with students who have finished Task 3. Ask them to show `club-message.md` and how they checked it.
- Ask the AI-use question in every conference: "What did you ask the AI? What did you keep, change, or reject, and why?"
- Ask each student first whether they mind Sigrid listening. Sigrid notes her own level for each conference, on paper or her own device, without seeing yours. After class, put both sets of levels on the Calibration sheet to see where you agree.
- Log each conference in the Monday tracker as you go, on the Log sheet: pick the student, choose Conference, enter up to three outcomes with levels, and type Y under R, T, or P for any required check shown. The "What they showed" and "Next question" notes can be a few words.

## 7. Close (5 minutes)

Each student writes one sentence: "Today I can show …, and my next task is …" Remind them there's no class next Monday (Thanksgiving), and the next class is October 19. If they have Decision Log entries, they can submit the permanent link in Blackboard for feedback.
