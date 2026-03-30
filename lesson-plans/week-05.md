# GEAP 103 Week 5 Lesson Plan: Making Something Others Can Read and Use

**Context:** 3 x 55 min (150 min instruction + 15-min break), B1 learners, BYOD, Office 365 + Copilot
**Week 5 of 14** | Phase 2: Building

**Learning Objectives (Week 5):**
1. Distinguish between visual formatting and structural formatting in a document (CLO 6 begins)
2. Identify and fix accessibility issues using the Accessibility Checker and Copilot
3. Write a verification note describing what AI did, what the student changed, and what was checked (CLO 4)
4. Shift from first-person desire language ("I want...") to third-person consideration language ("The user might need...")

**New vocabulary (5):** heading (style), alt text, screen reader, Accessibility Checker, contrast

**Goal Thread -- Technical Scoping:**
This is the first week where students move from describing what they want to describing what *someone else* needs. The Goal Document shifts from "I want..." to "The user might need..." This is a significant language shift: from first-person desire to third-person consideration. It marks the beginning of "planning and justifying" language (Phase 2 complexity level). Students practise conditional language, reasoning about constraints, and considering an audience they cannot see.

---

## Segment A: Vocabulary + Worked Example (0:00--0:40)

### 0:00--0:15 | Remaining Week 4 Micro-Defences
**Format:** Individual presentations (instructor + 1 peer), while others review DL feedback
**Language skills:** Speaking (sustained technical explanation), listening (peer), evaluative language (peer feedback)

Any students who did not complete their oral micro-defence in Week 4 go now. Use the same format: 3-4 min walkthrough, 1-2 instructor questions, 1 min peer feedback. Aim for 2-3 students maximum (~15 min).

**While waiting:** Other students review the Decision Log feedback that was returned this week (entries 1-2). Instructor has marked one strength and one specific improvement target per student. Students read the feedback and think about what they will change in future entries.

*If no remaining micro-defences, use this time for DL feedback review + vocabulary pre-training (expand the vocabulary segment below to 15 min).*

### 0:15--0:25 | Vocabulary Pre-Training
**Format:** Instructor-led, interactive
**Language skills:** Academic vocabulary building

**5 terms:** heading (style), alt text, screen reader, Accessibility Checker, contrast

For each term:
1. **Heading (style):** "A heading isn't just big bold text. It's a label that tells the computer 'this is a section title.' A screen reader can find it. Bold text that looks like a heading is invisible to the computer." Show Heading 1 vs. manually bolded text in Word -- they look the same, but one has structure.
2. **Alt text:** "A description of an image for people who can't see it. If you don't write alt text, a blind person doesn't know the image is there." Show an image with and without alt text in the accessibility tree.
3. **Screen reader:** "Software that reads a document out loud for people who can't see the screen. It can only read what has structure. If your headings are just bold text, the screen reader skips them."
4. **Accessibility Checker:** "A tool that finds problems a screen reader would have. It tells you what's broken." Show the Accessibility Checker panel in Word.
5. **Contrast:** "The difference between text colour and background colour. Low contrast means some people can't read it." Show a high-contrast and low-contrast example side by side.

Quick check: "If I make text bigger and bold but don't apply a heading style, can a screen reader find it?" (No.)

### 0:25--0:40 | Worked Example: Two Documents, Same Content
**Format:** Instructor demonstration with think-aloud
**Language skills:** Listening, critical evaluation, reading (system feedback)

Instructor displays two versions of the same one-page document (e.g., an event poster for a campus fundraiser) side by side:

**Document A -- "Looks nice":**
- Section titles are bold, larger font -- no heading styles applied
- An image with no alt text
- Low-contrast grey text on white background
- Looks clean and professional on screen

**Document B -- "Actually works":**
- Heading styles applied (Heading 1, Heading 2)
- Alt text on the image
- High-contrast text
- Looks nearly identical on screen

"These two documents look almost the same. But watch what happens."

**Step 1:** Run Accessibility Checker on Document A. Errors appear: missing headings, missing alt text, contrast issue. "This document is broken for anyone using a screen reader. It looks good but it doesn't work."

**Step 2:** Run Accessibility Checker on Document B. No errors (or minimal). "This one works because it has structure, not just formatting."

**Step 3:** Fix Document A using Copilot. "Copilot, apply heading styles to section titles." "Copilot, write alt text for this image." Think aloud: "I need to check what Copilot wrote for the alt text. Does it actually describe what the image shows?" Read the alt text, evaluate it, revise if needed.

**Step 4:** Re-run Accessibility Checker. Errors resolved.

"The question this week isn't 'can you make a nice document?' It's: what's actually there? A document that looks good is not one that works. What does a screen reader actually find? What does the Accessibility Checker actually report? That's what's actually there -- not what your eyes see. You've been making nice documents since Week 2. The question is: can someone else actually use what you made? Someone you've never met, using tools you've never seen?"

---

## Segment B: Planning + Guided Practice (0:40--1:35)

### 0:40--0:45 | Pre-Task Planning
**Format:** Individual reflection

"Think about who would read a document you make. Not you -- someone else. A classmate. A family member. An instructor. A stranger. What might make it hard for them?"

Students jot 2-3 notes: Who is the reader? What problems might they have? (e.g., uses a screen reader, has poor eyesight, reads on a phone, speaks a different first language)

### 0:45--1:10 | Guided Practice: Making a Document Accessible
**Format:** Individual with instructor circulation, then pair review
**Language skills:** Reading (system feedback from Accessibility Checker), writing (verification note)

Instructor distributes a poorly formatted document (shared via OneDrive or LMS). The document is one page, looks presentable, but has these problems:
- Bold text instead of heading styles (3-4 section titles)
- One image with no alt text
- One instance of low-contrast text
- Table with no header row specified

Students work through the fix:
1. Run Accessibility Checker. Read the error list.
2. Fix each issue. Students can use Copilot ("Apply heading styles to all section titles") or do it manually. For alt text, students should check what Copilot writes -- does it actually describe the image?
3. Re-run Accessibility Checker to confirm issues are resolved.

Instructor circulates:
- "What errors did the Checker find? Can you read me the first one?"
- "What did Copilot do? Did you check it? Is the alt text accurate?"
- "What's the difference between how the document looks and how it works?"

### 1:10--1:22 | Verification Note
**Format:** Individual writing
**Language skills:** Writing (descriptive, technical; in student's own words)

"Now write a short note about what just happened. This is called a verification note. It's in your own words -- not AI-generated. It describes what AI did, what you changed, and what you checked."

Students write a verification note (~75-100 words) covering:
- What accessibility issues the Checker found
- What AI did to fix them
- What the student checked or changed after AI's fixes
- Whether the document passed the Checker afterward

This is practice for the process documentation required in Artifact Packages.

### 1:22--1:35 | Pair Accessibility Review
**Format:** Pair work (structured A/B turns)
**Language skills:** Speaking (explaining problems and fixes), reading (partner's document)

Partners swap documents. Each student runs Accessibility Checker on the partner's fixed document.

**Partner A goes first** (5 min): Run the Checker on Partner B's document. Report findings aloud: "I found ___. This means ___." Partner B listens and takes notes but does not respond yet.

**Partner B responds** (5 min): Address what Partner A found, then run the Checker on Partner A's document and report findings the same way.

For both turns:
- "Did your partner catch everything? Are there issues left?"
- "Read your partner's alt text. Does it describe what the image actually shows?"

Brief report to partner: one thing they fixed well, one thing that still needs work.

**Second-opinion check** (3 min): "One more check. Take the alt text that Copilot wrote for your image. Paste it into a different AI tool -- ChatGPT, Claude, or another one you have. Ask: 'Here is alt text for an image. Is this description accurate and complete? What is missing?' Compare what the second AI says with what Copilot wrote."

"This is called a second opinion. You already know to verify AI's work. Now you're learning to verify it using a *different* AI. Two tools looking at the same output will catch different problems."

---

## Break (1:35--1:50)

---

## Segment C: Application + Goal Document + Session Review (1:50--2:45)

### 1:50--2:10 | Application: Accessibility in Your Own Work
**Format:** Individual with instructor support
**Language skills:** Reading (Accessibility Checker output), writing (alt text, headings), critical evaluation

"Now apply what you learned to something of your own. Open a document related to your project goal -- something you made in Weeks 2-4, or start something new connected to what interests you. Run the Accessibility Checker. Fix what it finds."

**Git maintenance (first 5 min):** Before students start fixing their document, they commit what they have now. "Before you change anything, commit your current document. Use a message like 'before accessibility fixes.' After you fix the accessibility issues, commit again with a message describing what you fixed. Then check your Git timeline: can you see both versions?" This reinforces the commit-before-changing habit from Week 3 and bridges the gap between the Week 3 Git introduction and the Week 6 Git Episodes launch.

Students work on their own documents. This is the first time accessibility principles meet the student's personal project direction. Some students will have a clear project idea; others are still exploring. Both are fine. The task is the same: make whatever you have accessible.

**Git Restore episode opportunity:** Students have been using Git since Week 3. During this work time, instructor can prompt students who haven't yet done a restore: "Have you tried going back to an earlier version of a file? This is a good time to try. If you break something while fixing accessibility, you can always restore the previous version." This is one of the three required Git Episodes. Not a formal activity; an invitation the instructor can extend individually.

Instructor circulates:
- "What did the Checker find? Can you explain the error in your own words?"
- "Who is going to use this document? What do they need?"
- "Did you commit before you started fixing? Good. After you finish, commit again so you can see both versions."
- For students ready for Git: "Want to try restoring an earlier version? Commit what you have now, then try going back."

### 2:10--2:25 | Goal Document
**Format:** Individual writing, then pair share (structured A/B turns)
**Language skills:** Writing (third-person consideration, conditional, planning), speaking (describing user needs)

"For four weeks you've been writing about what YOU want. Today you practised thinking about someone else -- a reader, a user, someone who might have trouble with what you make. Your Goal Document entry this week is about that shift."

**Prompt** (displayed): "Think about who will use what you build. What would make it hard for them to use? What accessibility issues should you plan for?"

*Sentence frames (optional -- use if you're stuck). From this week forward, sentence frames are available as support, not the default. Try writing without them first.*
- "The person using my project might have trouble with _____ because _____."
- "I need to check _____ to make sure it's accessible."
- "One thing I learned today that applies to my project is _____."

**Writing** (8 min): Students write entry 5 in their Goal Document. The new language demand is third-person consideration: reasoning about someone else's experience. This is harder than "I want..." because it requires imagining a user the student has never met.

**Pair share** (7 min, structured A/B turns): Partners read each other's Goal Document entries.

**Partner A presents first** (~3 min): Read your entry aloud or summarise it. Partner B listens and asks one question: "Who is the user you're thinking about?" or "What problem are you most worried about?"

**Partner B presents** (~3 min): Same format. Then 1 min for both to note anything their partner mentioned that they hadn't considered.

"Who is your partner thinking about? What problems did they anticipate? Did they think of something you didn't?"

### 2:25--2:27 | Bridging Activity
**Format:** Individual, silent

"In two minutes, you'll describe your accessibility work to AI. Before you open voice mode, do this: think about one accessibility problem you found today. Rehearse in your head: what was the problem, what did the Checker say, and how did you fix it?"

*This bridges the register shift from reflective Goal Document writing to the session review. Students retrieve specific content from today's work and switch from reflective to explanatory mode before the voice interaction begins.*

### 2:27--2:40 | Session Review (Speaking Practice)
**Format:** Individual, AI voice mode
**Language skills:** Speaking (narrating a troubleshooting sequence, responding to follow-up questions)

"Open your AI tool and start a new chat. Say or paste this prompt."

**Role-setting prompt** (on slide): "Speaking practice. I'm a B1 English student practising explaining my work. Ask me follow-up questions. If my explanation is vague, tell me what's unclear and ask me to be more specific. Don't do the explaining for me."

**This week's scenario** (on slide): "Describe an accessibility problem you found, what the Checker said, and how you fixed it."

AI role: Help desk.

Students talk to AI for 10-12 minutes, narrating the troubleshooting sequence from today's work: what accessibility issue they found, what the Accessibility Checker reported, what they did to fix it, and whether the fix worked. The AI pushes back when the explanation is vague.

"The AI is playing a help desk. You're calling in to describe a problem you already solved. They need to understand what you did so they can close the ticket. Be specific."

Instructor circulates and listens. No intervention unless a student is stuck or silent. This is production practice, not instruction.

**Note:** Voice mode starts a new chat. Students cannot paste work into the conversation and then switch to voice. The prompt is said aloud or pasted at the start, then the conversation is entirely spoken.

**Self-check** (final minute): "Before you close the chat, write one sentence in your notes: what did AI ask you to clarify?"

### 2:40--2:45 | Closing
**Format:** Whole class

- "Today's question was: can someone else use what you make? Not just look at it -- actually use it. That's a different standard from 'does it look nice.'"
- "The language shifted too. You went from 'I want' to 'the user might need.' That shift -- thinking about someone you can't see -- is one of the hardest things in communication."
- "You got feedback on your Decision Logs this week. Read it carefully. Your next DL entry should show you've thought about the feedback."
- "Next week: making sense of numbers. We'll read a spreadsheet before we build one."
- Remind: "Check your Git timeline. You should have at least two commits from today -- one before your accessibility fixes and one after."

---

## After Class

- **Decision Log feedback round 1 returned** (entries 1-2): If not yet distributed, return by the start of Week 5. Each entry gets one strength and one specific improvement target.
- **Spot-check verification notes** from Segment B: Are students writing in their own words? Are they describing what they checked, not just what AI did?
- **Note which students attempted a Git restore** during Segment C (for Git Episodes tracking)
- **Note which students completed the Git maintenance commits** (two commits visible in timeline: before and after accessibility fixes)
- **Collect any remaining micro-defence scores** from students who presented at the start of this week
- **Listen for session review patterns:** Were students able to narrate the troubleshooting sequence (problem, Checker output, fix)? Did the AI push them to be specific? Note any students who were silent or struggled -- consider pairing them with a partner next week before going to voice.

---

## Instructor Prep Checklist

- [ ] Two versions of the same document prepared: one "looks nice" (no structure), one "actually works" (heading styles, alt text, contrast). Visually near-identical.
- [ ] Poorly formatted document for student practice prepared and shared (OneDrive or LMS)
- [ ] Accessibility Checker confirmed working on student devices (Word for web and Word desktop both support it)
- [ ] Vocabulary slides: heading (style), alt text, screen reader, Accessibility Checker, contrast
- [ ] Screen reader example or video prepared (optional but powerful: show 10 seconds of a screen reader navigating a document without headings)
- [ ] Goal Document prompt + sentence frames on slide (sentence frames labelled "optional -- use if you're stuck")
- [ ] Verification note instructions on slide (what AI did, what I changed, what I checked)
- [ ] Session review slide: role-setting prompt + Week 5 scenario ("Describe an accessibility problem you found, what the Checker said, and how you fixed it.")
- [ ] Git maintenance instructions ready (commit before fixing, commit after fixing, check timeline)
- [ ] Decision Log feedback (entries 1-2) ready to return to students
- [ ] List of students who still need to complete Week 4 micro-defence (schedule for 0:00--0:15)
- [ ] Second AI tool prepared for second-opinion alt text verification (students paste Copilot's alt text into a different AI)
- [ ] Know which students have not yet done a Git restore (for prompting during Segment C)

## Language Development Summary

- **Vocabulary:** 5 terms (heading (style), alt text, screen reader, Accessibility Checker, contrast) pre-trained in Segment A, applied during practice in Segment B, reinforced in Segment C application
- **Speaking:** Remaining micro-defences (if any); pair accessibility review with structured A/B turns (explaining problems and fixes); pair share of Goal Document entries with structured A/B turns (describing user needs); **session review** (12 min sustained AI voice interaction: narrating a troubleshooting sequence to a help desk -- the first scenario requiring a complete problem-diagnosis-fix narrative)
- **Reading:** Accessibility Checker error messages (authentic system feedback); partner's fixed document; partner's Goal Document entry
- **Writing:** Verification note (~75-100 words, in student's own words: what AI did, what I changed, what I checked); Goal Document entry (~75-100 words: third-person consideration, conditional language -- a new language demand this week); Git commit messages (brief descriptive writing); session review self-check sentence
- **Listening:** Vocabulary pre-training; worked example think-aloud; partner's accessibility review feedback; partner's Goal Document discussion; AI follow-up questions during session review

## Assessment Alignment

- **CLO 6 begins** (produce digital products to college standards, including accessibility features)
- **CLO 4 continues** (evaluate AI text -- via Copilot's accessibility fixes and verification notes)
- **CLO 1 reinforced** (manage files and versions -- Git maintenance commits during application time bridge Weeks 3-6)
- **Decision Log feedback round 1 returned** (entries 1-2): Students should apply feedback to future entries
- **Git Restore episode opportunity** (part of 10% Git Episodes component): Students who recover an earlier version during Segment C can document this as their Restore episode
- **Git maintenance** (formative): Two commits (before and after accessibility fixes) reinforce the commit-as-snapshot mental model and keep Git practice active between the Week 3 introduction and Week 6 formal launch
- **Session review** (formative, not graded): Week 5 scenario practises narrating a troubleshooting sequence -- builds toward Micro-Defence 2 (Week 8, 5 criteria) where students must show what was tried and interpret errors
- **Goal Document updated** (ungraded; instructor reads at Week 8)
- **Verification note** practises process documentation format used in Artifact Packages (25%)
