# GEAP 103 Week 3 Lesson Plan: Never Losing Work Again

**Context:** 3 x 55 min (150 min instruction + 15-min break), B1 learners, BYOD, Office 365 + Copilot
**Week 3 of 14** | Phase 1: Discovery

**Learning Objectives (Week 3):**
1. Understand version control as a timeline of snapshots you control (CLO 1 continues)
2. Create a portfolio repository and add course work to it
3. Make commits and restore earlier versions using AI-assisted Git
4. Practise describing imagined possibilities in the Goal Document

**Goal Thread — The Language of Imagining:**
Students have expressed desires (Week 1) and tested whether their words work (Week 2). This week the Goal Document asks them to describe something that doesn't exist yet: what kind of thing might they want to make? This is speculative language ("it might be...", "I imagine...", "it would look like..."), which is harder than describing what you want. The tool context (Git) connects naturally: students have been making things for two weeks, and now they have a way to keep everything safe. But the English skill is the new one -- describing possibilities, not just desires.

---

## Segment A: Vocabulary + Worked Example (0:00--0:40)

### 0:00--0:05 | Warm-Up
**Format:** Pair share
**Language skills:** Speaking (personal narrative)

"You've been making things for two weeks: a file system, a document with AI, Decision Logs, a Goal Document. Has anyone ever lost something they were working on? Deleted it by accident? Wanted to go back to an earlier version?"

Pairs: "Tell your partner about a time you lost work or couldn't find something." (2 min each)

1-2 volunteers share with the class.

### 0:05--0:20 | Visual Pre-Training: The Timeline
**Format:** Instructor-led, visual model (no tools yet)
**Language skills:** Listening, vocabulary building, visual literacy

Draw on board or display a slide: a timeline with labelled snapshots.

```
[Snapshot 1]          [Snapshot 2]          [Snapshot 3]
"My essay,        --> "My essay,        --> "My essay,
 first draft"          added conclusion"      fixed intro"
                                               |
                                    <-- "I can go back here"
```

"You already have something like this in OneDrive -- version history. Git is the same idea, but YOU control when to save a snapshot, and it works for sharing with other people."

**5 terms** mapped onto the diagram:
- **Repository:** the whole timeline -- the place where your work and its history are kept
- **Commit:** the act of saving one snapshot ("I'm done with this version, save it")
- **Snapshot:** what the files look like at that moment
- **Restore:** going back to an earlier snapshot
- **Push:** sharing your timeline with someone else (putting it online)

For each term: point to where it lives on the diagram. Repeat the term. Ask a volunteer to use it in a sentence: "When I commit, I am _____."

### 0:20--0:40 | Worked Example: Save, Change, Go Back
**Format:** Instructor demonstration (all through Copilot/AI)
**Language skills:** Listening, reading (system output)

Instructor demonstrates, narrating each step:

1. **Create a repository** on GitHub. "This is where my work lives. It's empty right now."
2. **Add a file** (a simple text document). **Commit** with a message: "Added first draft of my notes."
3. **Change the file** (add a paragraph, delete a sentence). **Commit** again: "Revised introduction, added summary."
4. **Show the two snapshots** side by side. "See? Both versions exist. The old one isn't gone."
5. **Restore** the first version. "I changed my mind. Show me what I had before." The original reappears.
6. **Push** to GitHub. "Now it's online. Safe. Someone else could see it too."

All commands through Copilot or an AI chat interface -- not typed into a terminal.

**Key message:** "The commands don't matter. AI handles those. What matters is: WHEN do you save? And WHAT do you write to describe it? The commit message is a piece of writing -- a note to your future self about what you did and why."

---

## Segment B: Planning + Guided Practice (0:40--1:35)

### 0:40--0:45 | Pre-Task Planning
**Format:** Individual reflection

"You've made things over the past two weeks: a file-system map, a Copilot document, a Decision Log, a Goal Document. Today you're going to put all of it in a place where you can never lose it."

"Think: what have you made so far? Which files would you want to find again in 6 months?"

### 0:45--1:05 | Create Portfolio Repository
**Format:** Instructor-guided, individual
**Language skills:** Reading (interface text, instructions), writing (commit messages)

Step by step, instructor on projector, students on their own devices:
1. Sign in to GitHub (accounts created in advance if possible; otherwise, create now)
2. Create a new repository: name it `GEAP-103-Portfolio`
3. Add one file: Week 1 file-system map (upload or copy-paste)
4. Write a commit message: "Added Week 1 file system map"
5. Commit

Instructor circulates, troubleshoots sign-in issues, helps with upload.

Students who finish early: add the Week 2 Decision Log or Goal Document as a second commit. Each commit gets its own message.

### 1:05--1:25 | Partner-Guided Commits
**Format:** Pair work
**Language skills:** Speaking (instructional language -- telling your partner what to do), writing (commit messages)

Pairs take turns:
- **Student A** changes a file (e.g., adds a sentence to the file-system map)
- **Student B** guides the commit: "Now save this version. What's your commit message going to say? Describe what you changed."
- A executes the commit (using Copilot: "Commit this file with the message _____")
- Switch roles

Focus: writing good commit messages. "A commit message describes what you did. 'Updated file' tells you nothing. 'Added Week 2 folder to file map' tells your future self exactly what happened."

### 1:25--1:35 | Restore Practice
**Format:** Pair work
**Language skills:** Speaking (describing actions), reading (system feedback)

"Now: change something in your file. Commit it. Then get the old version back."

Students:
1. Make a change to a file
2. Commit the change
3. Restore the previous version (using Copilot: "Show me the previous version" or "Go back to the last commit")

Pairs confirm: "Show your partner the restored version. Is it the old one?"

**Key moment:** "You just went back in time. Your earlier work is still there. You can always get it back."

---

## Break (1:35--1:50)

---

## Segment C: Application + Goal Document (1:50--2:45)

### 1:50--2:10 | Continued Practice + Push
**Format:** Individual with instructor support
**Language skills:** Reading (system output, error messages)

Students continue adding to their repository:
- Add remaining files (Week 2 documents, Goal Document), commit each with a descriptive message, push to GitHub
- For students who are comfortable: visit their GitHub repository page in a browser and see their commits listed

Instructor circulates, helps with errors. Common errors to watch for: authentication problems, file-not-found, forgetting to write a commit message. Help students read the error message: "What does this say? What does it want you to do?"

### 2:10--2:35 | Goal Document Update: Imagining
**Format:** Guided writing, then pair discussion
**Language skills:** Writing (speculative, descriptive), speaking

"You've been writing about what you want for two weeks. Today: try to describe something that doesn't exist yet. This is harder. You have to use words like 'it might be' and 'it would look like' and 'I imagine.' This is the kind of language that lets you plan things before you make them."

**Prompt** (displayed): "Think about the things you've been interested in. If you could make something with a computer, what kind of thing might it be? A document? A spreadsheet? A presentation? Something else? Describe what someone would see if they looked at it."

**Sentence frames** (displayed):
- "I'm curious about making a _____ because _____."
- "It might look like _____, with _____."
- "I'm not sure yet, but I imagine something that _____."

**Writing** (15 min): Students write entry 3 in their Goal Document. This is the first time they practise speculative description -- imagining something concrete from a vague interest.

**Pair share** (10 min): Partners describe what they imagine. "Can you picture it? What would someone see? What would it do?"

### 2:35--2:45 | Debrief + Next Week Preview
**Format:** Whole class

- "Today you learned two things: how to protect your work so you never lose it, and how to describe something that doesn't exist yet. Both are skills you'll use all semester."
- Quick vocabulary check: "What's a commit?" "What's a repository?" "What does restore mean?" (volunteers answer)
- "Next week is a check-in. You'll show what you've done, explain your work to someone, and reflect on what you've learned so far."
- **Specific prep for Week 4:** "Your file-system artifact is due next week. Make sure your GEAP 103 folder in OneDrive is organized with clear naming and folders. Your portfolio repository should have at least 2-3 commits."

---

## Instructor Prep Checklist

- [ ] GitHub accounts: confirm students can sign in (pre-register if possible; plan extra time for account creation if not)
- [ ] Visual model slide or whiteboard plan: timeline with snapshots and vocabulary labels
- [ ] Vocabulary slides: repository, commit, snapshot, restore, push
- [ ] Copilot/AI interface tested for Git commands (create repo, commit, restore, push)
- [ ] Worked example file prepared (something simple to commit and modify)
- [ ] Plan for common errors: GitHub authentication failures, wrong directory, missing commit message
- [ ] Students' Week 1 and Week 2 files identified (for uploading to repository)
- [ ] Goal Document prompt + sentence frames on slide

## Language Development Summary

- **Vocabulary:** 5 terms (repository, commit, snapshot, restore, push) pre-trained visually in Segment A, then applied with tools in B and C
- **Speaking:** Pair share about lost work; partner-guided commits (instructional register); pair sharing of imagined possibilities
- **Reading:** GitHub interface text; commit messages; system feedback and error messages
- **Writing:** Commit messages (short, descriptive); Goal Document update (~50-100 words; speculative description -- a new language skill this week)
- **Listening:** Visual pre-training narration; worked example walkthrough; partner's guidance during commits

## Assessment Alignment

- No graded assessment this week
- CLO 1 continues (manage files + versions -- Git/GitHub as version control)
- CLO 1 continues (manage files + versions -- repository as a way to organize and protect work)
- Portfolio repository established (used for all future submissions and Git Episodes assessment)
- Goal Document updated (ungraded; instructor reads at Week 4)
- Students should have at least 1 Decision Log entry (from Week 2); additional entries are optional (students choose 8 of 12 eligible weeks). Instructor collects entries 1-2 by ~Week 4
