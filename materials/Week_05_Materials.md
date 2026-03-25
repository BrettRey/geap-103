# GEAP 103 Week 5: Instructor Materials Package

**Title:** Making Something Others Can Read and Use
**Phase:** Building (Week 5 of 14)
**Contact time:** 3 × 55 min (165 min total: 150 min instruction + 15 min break)
**Date prepared:** 2026-03-25

This file contains everything you need to prepare slides and run the class for Week 5. The lesson plan (`lesson-plans/week-05.md`) has the pedagogical rationale. This file has the concrete content. In case of conflict between this materials package and the lesson plan for Week 5, this materials package governs (it reflects March 2026 design revisions). For anything not covered here, the lesson plan governs.

**Week 5 design note:** This is the first Building phase week. Students shift from discovering tools to using them for a purpose. The purpose this week: making something that works for someone else, not just you. The difference between a document that looks nice and one that actually works (headings vs. bold text, alt text vs. no alt text) is invisible until you check. The Accessibility Checker makes the invisible visible. The language shift is from "I want..." to "The user might need..." — from first-person desire to third-person consideration. This is harder English than anything in Phase 1.

**Format change from lesson plan:** The lesson plan reserves the first 15 minutes for leftover Week 4 micro-defences. The triad format in Week 4 eliminates overflow, so this time is reallocated to vocabulary and the worked example, giving both activities more room.

**New vocabulary (5):** heading (style), alt text, screen reader, Accessibility Checker, contrast

**AI tools:** Same tool-agnostic approach. Students use AI to fix accessibility issues (e.g., "Apply heading styles to all section titles"). The skill being practised is evaluating what AI did — did the heading styles make sense? Did the alt text actually describe the image?

---

## Before Class

### Materials to Prepare

| Material | Description | How to share |
|----------|-------------|-------------|
| **Document A ("Looks nice")** | One-page document (e.g., campus fundraiser poster). Bold text for section titles, no heading styles. One image with no alt text. Low-contrast grey text. Looks clean and professional. | Display on projector only |
| **Document B ("Actually works")** | Same content as Document A. Heading styles applied. Alt text on image. High-contrast text. Looks nearly identical on screen. | Display on projector only |
| **Practice document** | One-page document with 4 accessibility problems: (1) bold text instead of heading styles on 3–4 section titles, (2) one image with no alt text, (3) one instance of low-contrast text, (4) table with no header row specified. | Share via OneDrive or Blackboard — students each get a copy |

**Tip:** The practice document works best if it's about something students care about. A campus event poster, a study-abroad information sheet, or a course welcome page are all good. Avoid anything that feels like a test document.

### Decision Log Feedback

Decision Log feedback (entries 1–2) should be returned this week. If you haven't finished marking them, return them by Week 6 at the latest. Each entry gets one strength and one specific improvement target.

---

## Segment A: Vocabulary + Worked Example (0:00–0:45)

### DL Feedback + Settling In (0:00–0:05)

Return Decision Log feedback (entries 1–2) as students arrive. If distributing digitally, post on Blackboard before class.

> "I've returned your first two Decision Log entries with feedback. Read mine before next class — your next entry should show you've thought about what I said."

Students can read feedback now or later. Don't spend class time on it — the activities ahead need the full session.

---

### Vocabulary (0:05–0:20)

**Vocabulary reference slide** (display and leave up — same approach as previous weeks):

| Term | Meaning |
|------|---------|
| **heading (style)** | A label that tells the computer "this is a section title" — not just big bold text, but a structure the computer can find |
| **alt text** | A description of an image for people who can't see it — if you don't write it, a blind person doesn't know the image exists |
| **screen reader** | Software that reads a document out loud for people who can't see the screen — it can only read what has structure |
| **Accessibility Checker** | A tool that finds problems a screen reader would have — it tells you what's broken |
| **contrast** | The difference between text colour and background colour — low contrast means some people can't read it |

**Teach these in context, not in isolation.** For each term, show a concrete example:

1. **Heading (style):** Open Word. Type a section title. Bold it, make it bigger. Then apply Heading 1 style. "These look the same on screen. But only one has structure. Watch."

   Display the Navigation Pane. The heading-styled title appears; the bold title doesn't.

   > "A heading isn't just big bold text. It's a label that tells the computer 'this is a section title.' The computer can find it. Bold text that looks like a heading is invisible to the computer."

2. **Alt text:** Show an image in a document. Right-click → View Alt Text. The pane is empty.

   > "A description of an image for people who can't see it. If you don't write alt text, a blind person doesn't know the image is there."

3. **Screen reader:** Play a 10-second clip of a screen reader navigating a document with headings (it jumps between sections) vs. without (it reads everything linearly). If you don't have a clip, describe it:

   > "Software that reads a document out loud. It can only read what has structure. If your headings are just bold text, the screen reader skips them — it doesn't know they're headings."

4. **Accessibility Checker:** Open it in Word (Review → Check Accessibility). Show the panel.

   > "A tool that finds problems a screen reader would have. It tells you what's broken. Think of it like a spell checker, but for accessibility."

5. **Contrast:** Display two versions of the same text: dark text on white background (high contrast) vs. light grey text on white background (low contrast).

   > "The difference between text colour and background colour. Low contrast means some people can't read it — especially on a phone screen in bright light."

Quick check after all five:

> "If I make text bigger and bold but don't apply a heading style, can a screen reader find it?" (No.)

---

### Worked Example: Two Documents, Same Content (0:20–0:45)

This is the core teaching moment. Instructor demonstrates on the projector. Students watch and respond.

**Display Document A and Document B side by side.** They look nearly identical.

> "These two documents look almost the same. But watch what happens."

**Step 1 — Run Accessibility Checker on Document A** (5 min):

Errors appear: missing headings, missing alt text, contrast issue, table header missing.

> "This document is broken for anyone using a screen reader. It looks good, but it doesn't work."

Read aloud each error the Checker found. Ask students: "What does this error mean? Can someone say it in their own words?"

**Step 2 — Run Accessibility Checker on Document B** (2 min):

No errors (or minimal).

> "This one works because it has structure, not just formatting. Same content, same appearance — but one is accessible and one isn't."

**Step 3 — Fix Document A using AI** (10 min):

Fix the issues one at a time, using AI where possible. Think aloud about each fix:

| Problem | AI prompt | Think-aloud |
|---------|-----------|-------------|
| Bold text instead of headings | "Apply heading styles to all section titles" | "Did it get the right ones? Let me check the Navigation Pane. Yes — three headings now appear." |
| Missing alt text | "Write alt text for this image" | "I need to check what it wrote. Does it actually describe what the image shows? [Read it aloud.] It says 'a group of people.' That's vague. What's actually happening in the image? Let me revise: 'Students setting up tables for the campus food drive, March 2026.'" |
| Low-contrast text | "Change this grey text to black" | "Simple fix. But the question is: why was it grey in the first place? Probably because it 'looked nice.' Looking nice isn't enough." |
| Table header row | "Set the first row of this table as a header row" | "This tells screen readers which row has the column labels. Without it, the reader just reads cells in order — the user can't tell what each number means." |

**The alt text moment is the most important.** This is where students see CLO 4 (evaluate AI text) in action: AI proposes something, the student checks it against reality, and revises if it's wrong. Spend time here. Ask students: "Is 'a group of people' good enough? What's missing? What would a blind person need to know?"

**Step 4 — Re-run Accessibility Checker** (2 min):

Errors resolved.

> "The question this week isn't 'can you make a nice document?' You've been doing that since Week 2. The question is: can someone else actually use what you made? Someone you've never met, using tools you've never seen?"

**Step 5 — Brief pair exchange** (3 min):

> "Turn to your partner. What was the biggest difference between Document A and Document B? What surprised you?"

1–2 volunteers share with the class.

---

## Segment B: Guided Practice + Verification Note (0:45–1:35)

### Pre-Task Planning (0:45–0:50)

> "Think about who would read a document you make. Not you — someone else. A classmate. A family member. An instructor. A stranger. What might make it hard for them?"

Students jot 2–3 notes: Who is the reader? What problems might they have? (e.g., uses a screen reader, has poor eyesight, reads on a phone, speaks a different first language)

This is the language shift: from "I want..." to "the user might need..." Students may struggle. That's the point — this language is new.

---

### Guided Practice: Fix the Document (0:50–1:15)

Students open the practice document (shared via OneDrive or Blackboard). Work individually with instructor circulating.

Display:

> 1. Run the Accessibility Checker (Review → Check Accessibility)
> 2. Read the error list
> 3. Fix each issue — use AI or do it manually
> 4. For alt text: check what AI wrote. Does it describe the image accurately? If not, revise it.
> 5. Re-run the Accessibility Checker to confirm the issues are resolved

**What to say while circulating:**

| What you see | What to say |
|-------------|------------|
| Student ran the Checker and is reading errors | "Good. Read me the first error. What does it mean?" |
| Student used AI to fix headings | "Did AI apply headings to the right sections? Check the Navigation Pane." |
| Student accepted AI's alt text without reading it | "Read the alt text aloud. Does it describe what the image actually shows? Would a blind person understand what's there?" |
| Student fixed everything quickly | "Good — now swap with your partner (see pair review below). Or: open one of your own files and run the Checker on that." |
| Student is stuck on the Checker | "Where is it? Review tab, then Check Accessibility. If it's not showing, try the web version of Word." |
| Student doesn't understand an error message | "Read it aloud. What is it asking you to fix? If you're not sure, ask AI: 'What does this accessibility error mean?'" |

---

### Verification Note (1:15–1:25)

> "Now write a short note about what just happened. This is called a verification note. It's in your own words — not AI-generated. It describes what AI did, what you changed, and what you checked."

Display:

> Write ~75–100 words covering:
>
> - What accessibility issues the Checker found
> - What AI did to fix them
> - What you checked or changed after AI's fixes
> - Whether the document passed the Checker afterward

**Sentence frames** (display):

> - "The Accessibility Checker found _____ problems: _____."
> - "I asked AI to _____, and it _____."
> - "I checked the alt text and changed it because _____."
> - "After the fixes, the Checker showed _____."

This is practice for the process documentation required in Artifact Packages. The language here is descriptive and technical — students are narrating what happened and what they did about it. The verification note is in the student's own words, not AI-generated.

**Collect verification notes** (or have students save them in their week-05 folder). These are formative evidence of CLO 4 (evaluate AI text) and CLO 5 (communicate about technical work).

---

### Pair Accessibility Review (1:25–1:35)

Partners swap documents (the practice document they fixed, not their own work).

Display:

> 1. Run the Accessibility Checker on your partner's fixed document
> 2. Did your partner catch everything? Are there issues left?
> 3. Read your partner's alt text. Does it describe what the image actually shows?
>
> Tell your partner: "One thing you fixed well was _____. One thing that still needs work is _____."

**What to listen for:**

| What you hear | What it means |
|--------------|---------------|
| "Your alt text says _____ but the image shows _____" | Student is evaluating AI-generated text against reality (CLO 4) |
| "You missed one — the table header" | Student can read and interpret Checker output independently |
| "Everything passed" without checking | Prompt: "Read the alt text aloud. Is it specific enough?" |

---

## Break (1:35–1:50)

---

## Segment C: Application + Goal Document (1:50–2:45)

### Apply to Your Own Work (1:50–2:15)

> "Now apply what you learned to something of your own. Open a document from your geap-103 folder — something you made in Weeks 2–4, or start something new connected to what interests you. Run the Accessibility Checker. Fix what it finds."

Students work on their own documents. This is the first time accessibility principles meet the student's personal project direction. Some students will have a clear project idea; others are still exploring. Both are fine. The task is the same: make whatever you have accessible.

**Git opportunity:** Students have been using Git since Week 3. While circulating, invite students who haven't done a Git restore yet:

> "Have you tried going back to an earlier version of a file? This is a good time to try. Commit what you have now. Then make some changes. If something goes wrong, restore the previous version."

This is one of the three required Git Episodes (Restore). Not a formal activity — an invitation the instructor extends individually. Note which students attempt it.

**What to say while circulating:**

| What you see | What to say |
|-------------|------------|
| Student running Checker on their own document | "Good. What did it find? Any surprises?" |
| Student adding alt text to their own images | "Read it to me. Would someone who can't see the image understand what it shows?" |
| Student has no document to work on | "Start something connected to what you wrote about in your Goal Document. Even a single page with a heading and an image is enough to practise." |
| Student finished quickly | "Commit your changes to Git. Write a commit message that says what you fixed. Then try restoring an earlier version to see the difference." |
| Student attempting a Git restore | "Good — that's one of your three Git Episodes. Save a screenshot or copy the output as evidence." |

---

### Goal Document: Who Is This For? (2:15–2:35)

> "For four weeks you've been writing about what YOU want. Today you practised thinking about someone else — a reader, a user, someone who might have trouble with what you make. Your Goal Document entry this week is about that shift."

**Prompt** (display):

> Think about who will use what you build. What would make it hard for them to use? What accessibility issues should you plan for?

**Sentence frames** (display):

> - "The person using my project might have trouble with _____ because _____."
> - "I need to check _____ to make sure it's accessible."
> - "One thing I learned today that applies to my project is _____."
> - "If I want to make _____, I would need to think about _____."

**Writing** (10 min): Students write entry 5 in their Goal Document. The new language demand is **third-person consideration**: reasoning about someone else's experience. This is harder than "I want..." because it requires imagining a user the student has never met. Conditional language ("If I want to..., I would need to...") appears for the first time.

**Pair share** (10 min): Partners read each other's Goal Document entry.

> "Who is your partner thinking about? What problems did they anticipate? Did they think of something you didn't?"

---

### Closing (2:35–2:45)

> "Today's question was: can someone else use what you make? Not just look at it — actually use it. That's a different standard from 'does it look nice.'"
>
> "The language shifted too. You went from 'I want' to 'the user might need.' That shift — thinking about someone you can't see — is one of the hardest things in communication."
>
> "You got feedback on your Decision Logs this week. Read it carefully. Your next DL entry should show you've thought about the feedback."
>
> "Next week: making sense of numbers. We'll read a spreadsheet before we build one."

### AI Session Review (2:40–2:45)

Display:

> Open a new document in your week-05 folder. Name it `week05-review-yourname.docx`.
>
> **Voice mode encouraged.**
>
> **First, say this (or paste it if using text):** "Speaking practice. I'm a B1 English student practising explaining my work. Ask me follow-up questions. If my explanation is vague, tell me what's unclear and ask me to be more specific. Don't do the explaining for me."
>
> **Then, your task:** AI is a help desk. Describe an accessibility problem you found today — what the Checker said, what was wrong, and how you fixed it. AI will tell you if your description is clear enough to act on.
>
> Start with: "I found a problem in a document today. The Accessibility Checker said _____. The issue was _____. I fixed it by _____."

Students have a brief exchange with AI (5 min). Save the conversation. Cut this if time is short.

---

## After Class

### Instructor Tasks

| Task | Deadline | Notes |
|------|----------|-------|
| Return DL feedback (entries 1–2) | This week (Week 5 or 6 at latest) | One strength + one improvement target per entry |
| Spot-check verification notes | Before Week 6 | Are students writing in their own words? Are they describing what they checked, not just what AI did? |
| Note Git restore attempts | Before Week 6 | Track which students attempted a restore during Segment C (for Git Episodes tracking) |
| Follow up on "deferred" triad students from Week 4 | Start of Week 5 or after class | Brief 2-min follow-up for any students the instructor didn't observe during triads |
| Make-up defence for Week 4 absentees | During guided practice (0:50–1:15) or application (1:50–2:15) | Absent student writes diagnostic during settling in (0:00–0:05) or arrives 10 min early. During a work period, form an ad hoc triad with 2 volunteers. Score as normal — you hear the whole thing. |

---

## Catch-Up Instructions for Latecomers

### If You Missed Week 5

In Week 5, we learned about accessibility — making documents that work for everyone, not just people who can see the screen perfectly.

**1. Learn these 5 terms:**

| Term | Meaning |
|------|---------|
| **heading (style)** | A label that tells the computer "this is a section title" — not just big bold text |
| **alt text** | A description of an image for people who can't see it |
| **screen reader** | Software that reads a document out loud for people who can't see the screen |
| **Accessibility Checker** | A tool that finds accessibility problems in your document |
| **contrast** | The difference between text colour and background colour |

**2. Practise fixing a document.** Open any document you've created. Run the Accessibility Checker (Review → Check Accessibility). Fix what it finds:
- Apply heading styles to section titles (don't just make them bold)
- Add alt text to images (describe what the image shows, specifically)
- Fix any contrast issues
- Re-run the Checker to confirm

**3. Write a verification note** (~75–100 words): What did the Checker find? What did AI fix? What did you check or change? Did it pass afterward?

**4. Update your Goal Document.** Write entry 5: Think about who will use what you build. What would make it hard for them? Use the frames:
- "The person using my project might have trouble with _____ because _____."
- "I need to check _____ to make sure it's accessible."

**5. Read your Decision Log feedback** (entries 1–2). Your next entry should show you've thought about the feedback.

---

## Instructor Prep Checklist

- [ ] Document A ("looks nice") and Document B ("actually works") prepared for projector demo
- [ ] Practice document prepared and shared via OneDrive or Blackboard (one copy per student)
- [ ] Accessibility Checker confirmed working on student devices (Word for web and Word desktop both support it)
- [ ] Vocabulary reference slide ready (5 terms in table)
- [ ] Screen reader clip or description prepared (optional but powerful)
- [ ] Verification note instructions on slide (what AI did, what I changed, what I checked)
- [ ] Goal Document prompt + sentence frames on slide
- [ ] Decision Log feedback (entries 1–2) ready to return
- [ ] List of any "deferred" micro-defence students from Week 4 (for brief follow-up)
- [ ] List of students absent in Week 4 who need make-up defence (diagnostic paper + ad hoc triad during a work period)
- [ ] Scoring sheets printed for any make-up students
- [ ] Know which students have not yet done a Git restore (for prompting during Segment C)

---

## Assessment Alignment

| Assessment component | What happens this week | Weight | CLOs |
|---------------------|----------------------|--------|------|
| **Decision Log feedback** | Entries 1–2 returned with feedback (one strength, one improvement target) | Part of 30% component | 3, 4 |
| **Artifact Packages** | Verification note practises process documentation format | Part of 25% component | 4, 6 |
| **Git Episodes** | Restore episode opportunity during Segment C (individual invitation) | Part of 10% component | 1 |
| **Goal Document** | Entry 5 written (third-person consideration, conditional language) | Ungraded | — |

**CLO 6 begins** this week (produce digital products to college standards, including accessibility). Students encounter accessibility for the first time and practise fixing it with AI assistance.

---

## Language Development Summary

| Skill | Activity |
|-------|----------|
| **Vocabulary** | 5 new terms (heading style, alt text, screen reader, Accessibility Checker, contrast) taught in context with live demos, applied during practice, reinforced in application |
| **Speaking** | Pair exchange after worked example; pair accessibility review ("one thing you fixed well, one thing still needs work"); pair Goal Document share (describing user needs) |
| **Reading** | Accessibility Checker error messages (authentic system feedback); AI-generated alt text (evaluating accuracy); partner's fixed document; partner's Goal Document entry |
| **Writing** | Verification note (~75–100 words, own words: what AI did, what I changed, what I checked); Goal Document entry 5 (~75–100 words: third-person consideration, conditional language) |
| **Listening** | Vocabulary demonstrations; worked example think-aloud; partner's accessibility review feedback; partner's Goal Document discussion |

---

## Timing Summary

| Segment | Time | Minutes | Notes |
|---------|------|---------|-------|
| DL feedback + settling in | 0:00–0:05 | 5 | Return feedback, brief announcement |
| Vocabulary | 0:05–0:20 | 15 | 5 terms, taught in context with live demos |
| Worked example | 0:20–0:45 | 25 | Two documents side by side; fix with AI; think-aloud; pair exchange |
| Pre-task planning | 0:45–0:50 | 5 | Who is the reader? What might be hard for them? |
| Guided practice | 0:50–1:15 | 25 | Fix the practice document; instructor circulates |
| Verification note | 1:15–1:25 | 10 | Write in own words: what happened, what I checked |
| Pair accessibility review | 1:25–1:35 | 10 | Swap documents, run Checker, give feedback |
| **Break** | **1:35–1:50** | **15** | |
| Application to own work | 1:50–2:15 | 25 | Fix own documents; Git restore opportunity |
| Goal Document entry 5 | 2:15–2:35 | 20 | Writing (10 min) + pair share (10 min) |
| Closing + session review | 2:35–2:45 | 10 | Theme summary, DL reminder, AI review (cut if short) |
| **Total** | | **150 min instruction** | |
