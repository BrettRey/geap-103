# GEAP 103 Week 3 Lesson Plan: Never Losing Work Again

**Context:** 3 x 55 min (150 min instruction + 15-min break), B1 learners, BYOD, access-neutral version control
**Week 3 of 14** | Phase 1: Discovery

**Learning Objectives (Week 3):**
1. Understand version control as a timeline of snapshots you control (CLO 1 continues)
2. Establish a reliable version-history location for course work
3. Save named versions and recover an earlier version using Git/GitHub or an equivalent version-history tool
4. Practise describing imagined possibilities in the Goal Document

**Goal Thread — The Language of Imagining:**
Students have expressed desires (Week 1) and tested whether their words work (Week 2). This week the Goal Document asks them to describe something that doesn't exist yet: what kind of thing might they want to make? This is speculative language ("it might be...", "I imagine...", "it would look like..."), which is harder than describing what you want. The tool context (Git) connects naturally: students have been making things for two weeks, and now they have a way to keep everything safe. But the English skill is the new one -- describing possibilities, not just desires.

---

## Segment A: Vocabulary + Worked Example (0:00--0:40)

### 0:00--0:05 | Warm-Up
**Format:** Pair share
**Language skills:** Speaking (personal narrative)

"You've been making things for two weeks: a file system, a document with AI, Decision Logs, a Goal Document. Has anyone ever lost something they were working on? Deleted it by accident? Wanted to go back to an earlier version?"

Pairs: "Tell your partner about a time you lost work or couldn't find something." (Partner A speaks first for 1 min, then Partner B for 1 min.)

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

"You may already have something like this in OneDrive, Google Drive, or a desktop app -- version history. Git is another way to save named snapshots, and it works well for sharing with other people."

**5 terms** mapped onto the diagram:
- **Repository:** the whole timeline -- the place where your work and its history are kept
- **Commit:** the act of saving one snapshot ("I'm done with this version, save it")
- **Snapshot:** what the files look like at that moment
- **Restore:** going back to an earlier snapshot
- **Push:** sharing your timeline with someone else (putting it online)

For each term: point to where it lives on the diagram. Repeat the term. Ask a volunteer to use it in a sentence: "When I commit, I am _____."

### 0:20--0:40 | Worked Example: Save, Change, Go Back
**Format:** Instructor demonstration (Git/GitHub plus a non-Git version-history example)
**Language skills:** Listening, reading (system output)

Instructor demonstrates, narrating each step:

1. **Create a repository** on GitHub. "This is one place where work and its history can live."
2. **Add a file** (a simple text document). **Commit** with a message: "Added first draft of my notes."
3. **Change the file** (add a paragraph, delete a sentence). **Commit** again: "Revised introduction, added summary."
4. **Show the two snapshots** side by side. "See? Both versions exist. The old one isn't gone."
5. **Restore** the first version. "I changed my mind. Show me what I had before." The original reappears.

**Aside (conversation hygiene):** "One thing about AI conversations: they have a shelf life. If you've been chatting with AI for 20 minutes and the conversation is long, AI starts losing track of what you said earlier. When a conversation gets confusing or AI starts repeating itself, start a new chat. It's like a clean desk -- AI thinks more clearly without 50 messages of history. You'll notice this as you use AI more. When it happens, just start fresh."

6. **Push** to GitHub. "Now the remote copy is online. Someone else could see it if I share it."

Demonstrate the same save-change-recover cycle once in a non-Git tool (for example, OneDrive or Google Drive version history). Students are assessed on the visible cycle and their explanation, not on access to one service. Do not use a student account or a student's identity documents in the demonstration.

**Key message:** "The commands don't matter. AI handles those. What matters is: WHEN do you save? And WHAT do you write to describe it? The commit message is a piece of writing -- a note to your future self about what you did and why."

---

## Segment B: Planning + Guided Practice (0:40--1:35)

### 0:40--0:45 | Pre-Task Planning
**Format:** Individual reflection

"You've made things over the past two weeks: a file-system map, a Copilot document, a Decision Log, a Goal Document. Today you're going to put all of it in a place where you can never lose it."

"Think: what have you made so far? Which files would you want to find again in 6 months?"

### 0:45--1:05 | Choose a Version-History Path and Save Once
**Format:** Instructor-guided, individual
**Language skills:** Reading (interface text, instructions), writing (commit messages)

Run a two-minute readiness check, then route students immediately:

- **Path A -- GitHub web:** sign in, create `GEAP-103-Portfolio`, upload the Week 1 file-system map, write a descriptive commit message, and commit.
- **Path B -- local Git:** create a local repository, add the Week 1 map, and make a named commit. A remote GitHub repository can be connected later.
- **Path C -- document/cloud version history:** open a course file in a tool with version history, save or name the current version, and record where its history is found.

A regular free GitHub account is enough for Paths A and B; GitHub Education and Copilot are optional and may still be pending. Account registration or Education verification continues outside the timed activity. Never ask a student to display or send identity documents to teaching staff.

Students who finish early: add the Week 2 Decision Log or Goal Document as a second named version. Each snapshot gets its own descriptive note.

### 1:05--1:25 | Partner-Guided Commits
**Format:** Pair work
**Language skills:** Speaking (instructional language -- telling your partner what to do), writing (commit messages)

Pairs take turns: (Partner A goes first, then they switch.)
- **Student A** changes a file (e.g., adds a sentence to the file-system map)
- **Student B** guides the commit: "Now save this version. What's your commit message going to say? Describe what you changed."
- A saves the named version in their chosen tool
- Switch roles

Focus: writing good commit messages. "A commit message describes what you did. 'Updated file' tells you nothing. 'Added Week 2 folder to file map' tells your future self exactly what happened."

### 1:25--1:35 | Restore Practice
**Format:** Pair work
**Language skills:** Speaking (describing actions), reading (system feedback)

"Now: change something in your file. Commit it. Then get the old version back."

Students:
1. Make a change to a file
2. Save the changed version
3. **Recover the previous version as a usable file**; merely opening or viewing the history does not complete the task
4. Keep both the current and recovered versions so the recovery is reversible

Pairs confirm: "Show your partner the restored version. Is it the old one?" (Partner A shows first, then Partner B.)

**Key moment:** "You just went back in time. Your earlier work is still there. You can always get it back."

---

## Break (1:35--1:50)

---

## Segment C: Application + Goal Document + Session Review (1:50--2:45)

### 1:50--2:05 | Continued Practice + Remote Copy Where Available
**Format:** Individual with instructor support
**Language skills:** Reading (system output, error messages)

Students continue in their selected path:
- Add remaining files or save another named version with a descriptive note
- GitHub/local-Git students connect or push a remote copy where available
- Version-history students locate the history again and export or duplicate the recovered version

Instructor circulates, helps with errors. Common errors to watch for: authentication problems, a missing file, a disabled history control, insufficient permissions, or an unnamed version. Help students read the message: "What does this say? What does it want you to do?" If one path remains blocked after two focused attempts, move the student to another path and record the unresolved issue for follow-up.

### 2:05--2:27 | Goal Document Update: Imagining
**Format:** Guided writing, then pair discussion
**Language skills:** Writing (speculative, descriptive), speaking

"You've been writing about what you want for two weeks. Today: try to describe something that doesn't exist yet. This is harder. You have to use words like 'it might be' and 'it would look like' and 'I imagine.' This is the kind of language that lets you plan things before you make them."

**Prompt** (displayed): "Think about the things you've been interested in. If you could make something with a computer, what kind of thing might it be? A document? A spreadsheet? A presentation? Something else? Describe what someone would see if they looked at it."

**Sentence frames** (displayed):
- "I'm curious about making a _____ because _____."
- "It might look like _____, with _____."
- "I'm not sure yet, but I imagine something that _____."

**Writing** (12 min): Students write entry 3 in their Goal Document. This is the first time they practise speculative description -- imagining something concrete from a vague interest.

**Pair share** (7 min): Partners describe what they imagine. (Partner A describes first for 3 min, then Partner B for 3 min.) "Can you picture it? What would someone see? What would it do?" 1 min for partners to identify one overlap or difference.

### 2:27--2:29 | Bridging Activity
**Format:** Individual, silent

"In two minutes, you'll explain commit messages to AI -- specifically, why your commit message was better than what AI would have suggested. Before you open voice mode, do this: look at one of your commit messages from today. Think about what it says and why you wrote it that way. What would a generic message like 'updated file' miss?"

*This bridges the register shift from reflective Goal Document writing to confrontational session review. Students retrieve specific content and switch from reflective to explanatory mode before the voice interaction begins.*

### 2:29--2:41 | Session Review (Speaking Practice)
**Format:** Individual speaking practice. Prefer AI voice; if it is unavailable, use a typed AI exchange read aloud or a live partner/instructor role-play with the same follow-up questions.
**Language skills:** Speaking (explaining a technical decision to a non-expert)

"Open your AI tool and start a new chat. Say or paste this prompt."

**Role-setting prompt** (on slide): "Speaking practice. I'm a B1 English student practising explaining my work. Ask me follow-up questions. If my explanation is vague, tell me what's unclear and ask me to be more specific. Don't do the explaining for me."

**This week's scenario** (on slide): "Explain what a commit message is and why yours was better than AI's suggestion."

AI role: Confused classmate who doesn't understand Git.

Students talk to AI for 10-12 minutes, explaining what a commit message is, why it matters, and why a specific, descriptive message is better than a generic one. The AI plays confused: "What do you mean, a snapshot? Why can't I just call it 'my file'? Why does the message matter?"

Instructor circulates and listens. No intervention unless a student is stuck or silent. This is production practice, not instruction.

**If using AI voice:** Voice mode starts a new chat. The prompt is said aloud or pasted at the start. The learning target is the student's explanation and follow-up answers, not access to voice mode.

### 2:41--2:42 | Self-Check
**Format:** Individual, written

"Write one sentence: what did AI ask you to clarify?"

*This is a 1-min diagnostic -- if you can't write that sentence, the session didn't work.*

### 2:42--2:45 | Closing
**Format:** Whole class

- "Today you learned two things: how to protect your work so you never lose it, and how to describe something that doesn't exist yet. Both are skills you'll use all semester."
- "You also saw what's actually there in your work history -- not what you remember doing, but what Git recorded. Version control doesn't lie. That's its power."
- Quick vocabulary check: "What's a commit?" "What's a repository?" "What does restore mean?" (volunteers answer)
- "Next week is a check-in. You'll show what you've done, explain your work to someone, and reflect on what you've learned so far."
- **Specific prep for Week 4:** "Your file-system artifact is due next week. Make sure your GEAP 103 folder is organized with clear names. Bring evidence of at least two named versions and one actual recovery from the version-history path you used."

---

## Instructor Prep Checklist

- [ ] Post the three supported paths (GitHub web, local Git, and document/cloud version history); do not predict how many students will need each path
- [ ] Visual model slide or whiteboard plan: timeline with snapshots and vocabulary labels
- [ ] Vocabulary slides: repository, commit, snapshot, restore, push
- [ ] Instructor-owned GitHub/local-Git example and a non-Git version-history example tested; a public demo verifies only the shared interface, not each student's registration or eligibility
- [ ] Worked example file prepared (something simple to commit and modify)
- [ ] Plan for common errors: authentication failure, wrong directory, missing history, permissions, and unclear snapshot names; prepare downloadable practice files
- [ ] Students' Week 1 and Week 2 files identified (for uploading to repository)
- [ ] Goal Document prompt + sentence frames on slide
- [ ] Session review slide: role-setting prompt + Week 3 scenario ("Explain what a commit message is and why yours was better than AI's suggestion")

## Language Development Summary

- **Vocabulary:** 5 terms (repository, commit, snapshot, restore, push) pre-trained visually in Segment A, then applied with tools in B and C
- **Speaking:** Pair share about lost work; partner-guided commits (instructional register); pair sharing of imagined possibilities; **session review** (12 min AI voice interaction: explaining a technical decision to a confused non-expert -- the first scenario requiring explanation of a concept, not just narration of an experience)
- **Reading:** GitHub interface text; commit messages; system feedback and error messages
- **Writing:** Commit messages (short, descriptive); Goal Document update (~50-100 words; speculative description -- a new language skill this week)
- **Listening:** Visual pre-training narration; worked example walkthrough; partner's guidance during commits; AI follow-up questions during session review

## Assessment Alignment

- No graded assessment this week
- CLO 1 continues (manage files + versions -- Git/GitHub as version control)
- CLO 1 continues (manage files + versions -- repository as a way to organize and protect work)
- Version-history location established; GitHub remains the preferred portfolio path, with equivalent evidence accepted when access is blocked
- Goal Document updated (ungraded; instructor reads at Week 4)
- Students should have at least 1 Decision Log entry (from Week 2); they curate 8 entries from the ten-week window, Weeks 2-11. Instructor collects entries 1-2 by ~Week 4
- **Session review** (formative, not graded): Week 3 scenario practises explaining a technical concept to a non-expert -- builds toward Micro-Defence 1 (Week 4, 3 criteria: clear description, terminology, explaining a decision)
