# GEAP 103: 14-Week Topic Sequence (Draft v3)

**Course:** GEAP 103 Basic Computer Skills (Foundation Semester, B1)
**Version:** Draft v3, 2026-02-12
**Status:** Revised from v2; Git restored to Week 3 with AI-assisted interaction
**Arc:** Discovery (Weeks 1-4) → Building (Weeks 5-10) → Creation (Weeks 11-14)
**Contact time:** 3 hours/week (42 hours total)
**Environment:** Office 365 + Copilot, BYOD

---

## v2 → v3 Changes

The v2 review process moved Git from Week 3 to Week 5 based on three reviewers' concerns about cognitive load. That was an overcorrection. Their concerns assumed traditional Git instruction where students memorise terminal commands and parse cryptic error messages. In this course, Git interaction is AI-mediated:

- "Copilot, save this version"
- "Copilot, show me what changed"
- "Copilot, send my changes to the shared project"

The conceptual model (snapshots on a timeline, a shared project you contribute to) is simple. The command-line complexity that historically made Git hard is exactly what the AI handles. Deferring Git to Week 5 also created an incoherent collaboration story: if students are doing pair work from Week 1 (Ellis's valid recommendation), they need a shared workspace. Without Git, "collaboration" is emailing files.

| Change from v2 | Rationale |
|----------------|-----------|
| Git restored to Week 3 (from Week 5) | AI-assisted Git is conceptually simple; collaboration needs infrastructure from early on |
| v2 Week 3 consolidation removed | Unnecessary with Git filling the slot; file format concepts folded into Weeks 1 and 3 |
| PRs/Issues moved to Week 7 (from Week 9) | With Git from Week 3, students have 4 weeks of practice before learning the social layer; gives 7 weeks of collaboration runway before final project |
| Presentations moved to Week 9 (from Week 10) | Frees Week 10 for mid-semester project work and submission |

**Retained from v2** (all the genuine improvements):
- Worked examples for every new tool-task combination
- Vocabulary pre-training (5 terms/session, before tool interaction)
- Session segmenting (3 blocks per 3-hour class)
- Pair work every week from Week 1
- Deliberate intention-output mismatch in AI tasks
- Week 4 CLO 5/6 assessment designated as diagnostic
- Troubleshooting instruction in Week 8

---

## Design Principles

1. **One new tool or concept per week.**
2. **Recurring task types build fluency.** Decision Logs (8x), verification notes (3x), micro-defences (3x), and the AI interaction cycle recur across different content.
3. **Assessment weeks consolidate; they do not introduce.** Weeks 4, 8, 12.
4. **Technical content serves language development.** Material that does not serve the dual objective is excluded.
5. **Scaffolded freedom.** Early weeks tightly structured; later weeks give increasing choice.
6. **Worked examples before independent performance.** Every new tool-task combination begins with instructor demonstration. Guidance fades across subsequent weeks.
7. **Vocabulary pre-training.** New terms introduced at the start of each session, before tool interaction.
8. **Pair work throughout.** Structured pair tasks every week. Interaction is a condition for language acquisition.
9. **Deliberate mismatch.** AI tasks are designed so output sometimes fails to match intent, requiring genuine meaning negotiation.
10. **Git is infrastructure, not a topic.** Students learn Git as the way work gets saved and shared, not as a standalone technology unit. AI handles the commands; students handle the concepts.

---

## Session Structure (Standard 3-Hour Block)

| Segment | Duration | Purpose |
|---------|----------|---------|
| **A: Vocabulary + Worked Example** | ~40 min | Pre-train 3-5 new terms. Instructor demonstrates the week's tool-task combination. Students observe, ask questions. |
| **B: Guided Practice** | ~70 min | Students attempt the task with instructor support. Pair work integrated. Decision Log or verification note written. |
| *Break* | ~10 min | |
| **C: Independent/Pair Application + Wrap-up** | ~60 min | Students apply the skill to their own content or a partner's. Brief whole-class debrief (5-10 min). |

Assessment weeks (4, 8, 12) replace this structure with diagnostic + micro-defences + peer feedback.

---

## Phase 1: Discovery (Weeks 1-4)

### Week 1: Where Do Files Live?

**Focus:** File-system mental model; from app-centric to file-centric thinking

**New vocabulary (5):** folder, subfolder, file path, file extension, cloud sync

**Segment A -- Worked example:** Instructor shows their own file system (OneDrive). Walks through: folder, file, path, sync. Shows file types: .docx vs .pdf vs .txt -- why it matters.

**Segment B -- Guided practice:** Students open their own OneDrive. Map their current file system on paper (diagnostic). In pairs, compare maps: "Where are your photos? Where are your school files?"

**Segment C -- Application:** Create a course folder structure (template provided). Name 3 files with proper conventions. Partners review each other's folders: "Can you find [file]?"

**CLOs:** 3 (begin)
**Pair work:** File-system audit; partner folder review

---

### Week 2: First AI Interactions + Decision Logging

**Focus:** First use of Copilot in Word; the Decision Log

**New vocabulary (5):** prompt, generate, revise, accept/reject, verification

**Segment A -- Worked example:** Instructor uses Copilot to draft a class directory entry. Deliberately shows a case where AI output doesn't match the goal. Completes a Decision Log entry on the projector, thinking aloud.

**Segment B -- Guided practice:** Students draft their own directory entry with Copilot. Complete first Decision Log entry together (class-wide worked example). In pairs, compare: "What did yours say? What did you change?"

**Segment C -- Application:** Second AI task with a deliberate mismatch (e.g., "Summarise this paragraph" where the AI is likely to miss a key point). Independent Decision Log entry. Partners exchange and discuss.

**CLOs:** 1 (begin), 4 (begin)
**Assessment:** Decision Log entries begin
**Pair work:** Comparing AI outputs; exchanging Decision Logs

---

### Week 3: Saving and Sharing Work with Git

**Focus:** Git as the way work gets saved and shared. AI handles the commands.

**New vocabulary (5):** repository, commit, version history, restore, push

**Segment A -- Visual pre-training + worked example:** Before touching any tool, instructor presents a visual model: a timeline of snapshots. "You already have version history in OneDrive. Git is the same idea, but it works everywhere, and you control when snapshots happen." Then, worked example: instructor creates a repository, adds a file, commits (using Copilot: "Save this version with the message 'first draft'"), changes the file, commits again, restores the first version. Students observe.

**Segment B -- Guided practice:** Students create a repository for their course portfolio. Add their Week 1 file map and Week 2 document. Make first commits with Copilot assistance. In pairs, one student changes a file, partner talks them through committing.

**Segment C -- Application:** Restore practice: change a file, commit, restore previous version (using Copilot: "Show me the previous version" / "Go back to my last save"). Write Decision Log entry. Pairs compare: "What happened when you restored?"

**CLOs:** 2 (begin), 3
**Pair work:** Partner-guided commits; paired restore practice
**Note:** The vocabulary is conceptual (snapshot, version, restore), not command-line (rebase, cherry-pick, HEAD~3). Students interact with Git through natural language via Copilot.

---

### Week 4: Check-in 1

**Focus:** First assessment checkpoint. No new tools.

**Segment A:** Review of Weeks 1-3. Students prepare file-system artefact.

**Segment B:** In-class written diagnostic (10 min, unmediated): "Describe how you organised your files for this course and why." Oral Micro-Defence 1 runs while others work on portfolio.

**Segment C:** Peer feedback on walkthroughs. Students commit their file-system artefact to their portfolio repository.

**Assessment:**
- File System artefact due (7%)
- Oral Micro-Defence 1 (incl. diagnostic + peer feedback)

**CLOs assessed:**
- CLO 3: evaluative
- CLOs 5, 6: **diagnostic only** (baseline; not graded for these CLOs)

---

## Phase 2: Building (Weeks 5-10)

### Week 5: Documents with AI + Accessibility

**Focus:** Creating and revising documents with Copilot; accessibility fundamentals

**New vocabulary (5):** heading (style), alt text, screen reader, Accessibility Checker, contrast

**Segment A -- Worked example:** Instructor shows two versions of the same document: one with no headings/alt text, one properly structured. Runs Accessibility Checker on both. Demonstrates fixing one issue with Copilot.

**Segment B -- Guided practice:** Students take a poorly formatted document (provided). Use Copilot to restructure. Run Accessibility Checker. Write verification note in own words.

**Segment C -- Application:** Apply accessibility to own course document. Partners review each other's documents with Accessibility Checker. Commit updated document to portfolio.

**CLOs:** 7 (begin), 4
**Assessment:** Decision Log feedback round 1 returned; Git episodes begin (Restore opportunity from Week 3 practice)
**Pair work:** Peer accessibility review

---

### Week 6: Spreadsheets with AI

**Focus:** Working with structured data in Excel + Copilot

**New vocabulary (5):** cell, row, column, formula, chart

**Segment A -- Worked example:** Instructor demonstrates Excel + Copilot with a dataset (e.g., class survey). Shows: entering data, asking Copilot to create a formula, creating a chart. Demonstrates the "can you explain this?" check: "Copilot, what does this formula do?" Verifies one calculation manually.

**Segment B -- Guided practice:** Students work with a provided dataset. Use Copilot to create summary table and chart. Verify one formula manually. Write Decision Log entry.

**Segment C -- Application:** Pairs work with a different dataset. One creates a chart; partner evaluates: "Does this show what you wanted? Is anything misleading?" Commit to portfolio.

**CLOs:** 7, 1, 4
**Pair work:** Partner evaluation of charts

---

### Week 7: Collaboration Through Git: PRs and Issues

**Focus:** The social layer of Git: pull requests and issues as professional communication

**New vocabulary (5):** pull request (PR), issue, fork, comment, review

**Segment A -- Worked example:** Instructor demonstrates the full PR workflow: fork a repository, make a change, write a PR description ("Here is what I changed and why"), receive a comment, respond. Then demonstrates writing a GitHub Issue. Shows models of good and bad PR descriptions.

**Segment B -- Guided practice:** In pairs, students fork a shared practice repository, make a change, submit a PR with description, and comment on their partner's PR. Instructor circulates.

**Segment C -- Application:** Write a GitHub Issue for a real or hypothetical problem. Partners respond to each other's issues. Decision Log entry about collaboration. This is the Collaboration episode opportunity for Git Episodes.

**CLOs:** 8 (begin), 6, 2
**Pair work:** Paired PR exercise; issue response
**Note:** Students have had 4 weeks of Git practice (Weeks 3-6) before learning PRs/Issues. This gives 7 weeks of collaboration runway before the final project.

---

### Week 8: Check-in 2 + Troubleshooting

**Focus:** Second assessment checkpoint + explicit troubleshooting instruction

**New vocabulary (5):** error message, troubleshoot, debug, help request, log

**Segment A (40 min) -- Troubleshooting worked example:** Instructor presents 3 real error messages (from Office 365, Git, or Copilot). Parses each: "What happened? Where? What should I try?" Demonstrates writing a help request (context → problem → what I tried → what I expect).

**Segment B (70 min) -- Micro-defences:** In-class written diagnostic (10 min). Oral Micro-Defence 2 runs while others practise troubleshooting with provided error messages and write a help request.

**Segment C (50 min) -- Troubleshooting practice:** In pairs, troubleshoot a staged problem (e.g., "This formula gives the wrong answer" or "This commit failed"). Write help request if stuck. Decision Log entry.

**Assessment:**
- Oral Micro-Defence 2 (incl. diagnostic + peer feedback)

**CLOs assessed:** 5, 6 (first evaluative assessment, after explicit instruction)

---

### Week 9: Presentations with AI

**Focus:** Slides with Copilot; accessible, functional presentations

**New vocabulary (5):** slide, layout, speaker notes, caption, colour contrast

**Segment A -- Worked example:** Instructor creates a 3-slide presentation using Copilot. Runs Accessibility Checker. Shows: alt text, contrast, meaningful slide titles. Focus is practical (accessible, clear slides), not theoretical (visual communication principles).

**Segment B -- Guided practice:** Students create a 3-5 slide presentation on a topic of choice. Run Accessibility Checker. Write verification note.

**Segment C -- Application:** Partners review each other's slides for accessibility. Commit to portfolio. Begin thinking about mid-semester project: what will you build?

**CLOs:** 7, 1, 4
**Pair work:** Peer accessibility review of slides

---

### Week 10: Mid-Semester Project Work + Submission

**Focus:** Finalising and submitting mid-semester artefact

**No new vocabulary.** Consolidation week.

**Segment A -- Project clinic:** Instructor available for troubleshooting and questions. Students finalise artefact (document, spreadsheet, or presentation, student's choice).

**Segment B -- Submission:** Write verification note. Commit to portfolio. Submit mid-semester artefact.

**Segment C -- Preview of Creation phase:** Instructor introduces the collaborative project (Weeks 11-14). Form pairs/groups. Begin scoping: what will you build together?

**Assessment:** Mid-Semester Artefact due (8%); Decision Log feedback round 2 returned
**CLOs:** 7, 3, 4

---

## Phase 3: Creation (Weeks 11-14)

### Week 11: Collaborative Project Launch

**Focus:** Sustained collaborative project in pairs or small groups

**No new vocabulary.** All terms consolidated.

**Segment A -- Project setup:** Groups define scope, divide work, create shared repository. Instructor models a project kick-off: "Here is my goal, here is how I divide work, here is my first issue."

**Segment B -- Project work:** Groups build. Each student submits at least one PR with description and comments on a partner's work. Error recovery episode opportunity for Git Episodes.

**Segment C -- Status update:** Each group gives a 2-minute update (informal, not graded): "What we're building, what's done, what's next."

**CLOs:** 8, 6, 2

---

### Week 12: Check-in 3 + Project Continuation

**Focus:** Final assessment checkpoint and project work

**Segment A (40 min) -- Portfolio curation preview:** Instructor demonstrates mapping evidence to CLOs. Worked example of an Evidence-Indexed Reflection entry. Students identify strongest evidence for 2-3 CLOs.

**Segment B (70 min) -- Micro-defences + project work:** In-class written diagnostic (10 min). Oral Micro-Defence 3 while others continue projects.

**Segment C (50 min) -- Project work.**

**Assessment:** Oral Micro-Defence 3 (incl. diagnostic + peer feedback)
**CLOs assessed:** 5, 6

---

### Week 13: Project Refinement + Portfolio Curation

**Focus:** Iterating on projects; curating portfolio evidence

**Segment A -- Self-assessment calibration:** Instructor returns Decision Log self-assessment patterns. Discussion: "What does 'Proficient' look like?" Worked example of full Evidence-Indexed Reflection (including evaluative judgment: "How strong is this evidence?").

**Segment B -- Portfolio curation workshop:** Students map evidence to CLOs and draft reflection. Partners exchange reflections: "Is this evidence convincing?"

**Segment C -- Project refinement.** Decision Logs due (8 entries, 30%).

**CLOs:** All
**Assessment:** Decision Logs due

---

### Week 14: Final Submissions + Course Wrap-up

**Segment A -- Final submissions:** Final artefact (with verification note), Git Episodes, Evidence-Indexed Reflection.

**Segment B -- Sharing:** 2-3 minute informal presentations: show something you built, say something you learned. Not graded.

**Segment C -- Wrap-up:** "What can you do now that you couldn't in Week 1?" Transfer to degree programs. Course evaluation.

**Assessment:**
- Final Artefact due (10%)
- Git Episodes due (10%)
- Evidence-Indexed Reflection due (10%)

---

## Tool Introduction Schedule

| Week | New Tool/Feature | Builds On |
|------|-----------------|-----------|
| 1 | OneDrive, file system | -- |
| 2 | Copilot in Word, Decision Log template | File system |
| 3 | Git/GitHub (AI-assisted) | File system + Copilot |
| 4 | *Assessment* | |
| 5 | Accessibility Checker, Word styles | Copilot in Word |
| 6 | Copilot in Excel | Copilot in Word |
| 7 | GitHub PRs + Issues | Git (4 weeks of practice) |
| 8 | *Assessment + troubleshooting* | |
| 9 | Copilot in PowerPoint | Copilot in Word/Excel |
| 10 | *Project work* | |
| 11-14 | *No new tools* | |

New tools in Weeks 1-3, 5-7, 9. Consolidation in Weeks 4, 8, 10-14.

---

## Vocabulary Schedule

| Week | New Terms (~5/week) | Cumulative |
|------|-------------------|------------|
| 1 | folder, subfolder, file path, file extension, cloud sync | 5 |
| 2 | prompt, generate, revise, accept/reject, verification | 10 |
| 3 | repository, commit, version history, restore, push | 15 |
| 4 | *Review* | 15 |
| 5 | heading (style), alt text, screen reader, Accessibility Checker, contrast | 20 |
| 6 | cell, row, column, formula, chart | 25 |
| 7 | pull request, issue, fork, comment, review | 30 |
| 8 | error message, troubleshoot, debug, help request, log | 35 |
| 9 | slide, layout, speaker notes, caption, colour contrast | 40 |
| 10-14 | *Consolidation* | 40 |

**Total: ~40 terms across 9 teaching weeks.** Pre-trained at start of each session before tool interaction.

---

## CLO Activation Timeline

| CLO | Introduced | Practised | First Assessed |
|-----|-----------|-----------|----------------|
| 1. Articulate task goals | Week 2 | Weeks 2-13 | Decision Logs (ongoing) |
| 2. Git/GitHub workflows | Week 3 | Weeks 3-14 | Git Episodes (Weeks 5-14) |
| 3. Organise digital files | Week 1 | Weeks 1-5 | File System artefact (Week 4) |
| 4. Evaluate AI outputs | Week 2 | Weeks 2-13 | Decision Logs (ongoing) |
| 5. Interpret/troubleshoot | Week 8 | Weeks 8-14 | Micro-Defence 2 (Week 8) |
| 6. Communicate technical info | Week 7 | Weeks 7-14 | Micro-Defence 2 (Week 8) |
| 7. Create digital artefacts | Week 5 | Weeks 5-14 | Mid-semester artefact (Week 10) |
| 8. Collaborate | Week 7 | Weeks 7-14 | Git Episodes + final artefact |

Week 4 Micro-Defence: CLOs 5/6 assessed diagnostically (baseline only).

---

## Pair Work Schedule

| Week | Pair Activity |
|------|--------------|
| 1 | Compare file-system maps; review partner's folder structure |
| 2 | Compare AI outputs; exchange Decision Log entries |
| 3 | Partner-guided Git commits; paired restore practice |
| 4 | Peer feedback on micro-defence walkthroughs |
| 5 | Peer accessibility review of documents |
| 6 | Partner evaluation of charts |
| 7 | Paired PR exercise; respond to partner's Issue |
| 8 | Paired troubleshooting of staged errors; peer feedback on micro-defences |
| 9 | Peer accessibility review of slides |
| 10 | Project scoping in pairs/groups |
| 11 | Collaborative project work |
| 12 | Peer feedback on micro-defences; project work |
| 13 | Peer review of reflection drafts |
| 14 | Informal sharing |

---

## Fluency Development Strategy

| Strand | Where | Recurrence |
|--------|-------|------------|
| **Meaning-focused input** | AI output, error messages, technical instructions | Every week |
| **Meaning-focused output** | Decision Logs, verification notes, help requests, PR descriptions | Every week |
| **Language-focused learning** | Vocabulary pre-training; genre templates | Every week |
| **Fluency development** | Same task types, different content: Decision Logs (8x), micro-defences (3x), verification notes (3x), AI cycle (12 weeks) | Built into structure |

The AI interaction cycle uses deliberate intention-output mismatch in early weeks (2-5) so the review stage requires genuine meaning negotiation. Mismatch decreases as students develop precision, but AI output remains imperfect enough to sustain the negotiation demand.
