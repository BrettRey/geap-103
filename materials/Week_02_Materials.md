# GEAP 103 Week 2: Instructor Materials Package

**Title:** Getting AI to Do What I Mean
**Phase:** Discovery (Week 2 of 14)
**Contact time:** 3 × 55 min (150 min instruction + 15 min break)
**Date prepared:** 2026-03-23 (revised same day)

This file contains everything you need to prepare slides and run the class for Week 2. It is keyed to the lesson plan (`lesson-plans/week-02.md`). The lesson plan has the pedagogical rationale, timing, and activity design. This file has the concrete content: what goes on slides, what to say, what to display. Use the lesson plan for the "why," this file for the "what." In case of conflict, the lesson plan governs.

**Week 2 design note:** AI's output improves in direct proportion to how much the student can say about themselves, their purpose, and their perspective. The student experiences this firsthand, with their own wish from Week 1, not by watching the instructor demonstrate it. The instructor's role is to circulate, notice what students are doing, name the vocabulary as it arises, and push students to say more. Both the Decision Log and the Goal Document are assigned this week. They serve different purposes: the DL looks backward at a specific interaction; the GD looks forward at evolving interests.

**AI tools:** This course is tool-agnostic. Students use whatever AI they can access. The assessment is on what they can articulate, evaluate, and produce – not which tool they use. Recommended options:

| Tool | How to access | Notes |
|------|--------------|-------|
| **GitHub Copilot CLI** (recommended) | Free GitHub account + [Student Developer Pack](https://education.github.com/pack). [Install](https://docs.github.com/en/copilot/how-tos/set-up/install-copilot-cli): standalone executable, shell script, Homebrew (Mac), WinGet (Windows), or npm. No package manager required. | Works in the project folder, sees your files, saves conversations, free for students. The strongest "English is the control layer" experience. |
| **Copilot Chat** | copilot.microsoft.com, sign in with Humber account | Free, no install, works in any browser |
| **ChatGPT** | chatgpt.com | Free tier available, no institutional dependency |
| **Claude** | claude.ai | Free tier available |
| **Other** | Whatever the student already uses or prefers | Fine. The DL "AI used" field captures which tool. |

If you want to demonstrate the CLI in class (recommended), install it before the session using any method above and authenticate with your GitHub account. First launch prompts browser-based login – no terminal auth commands needed. The CLI works in the terminal, inside the student's project folder, and the conversation is captured automatically.

---

## Segment A: Launch (0:00–0:10)

### Warm-Up (0:00–0:05)

Display or say:

> Last week you wrote about what you want. Today you try to make it happen. The question is: can you say what you mean clearly enough for AI to help?

Quick show of hands: "Who has used ChatGPT, Copilot, or another AI tool before?"

Follow-up: "Did it do what you wanted, or something different?"

2–3 students share briefly. Listen for stories where AI did something unexpected. These set up the theme.

---

### Step 1 + Go (0:05–0:10)

Display only Slide 1. Students start immediately.

**Slide 1: Start**

> Open your Goal Document from last week. Pick one wish.
> Ask AI to help with it. See what happens.
>
> Frame: "I want to _____."

**Path B** (display alongside): "If you're not sure what you want, ask AI: 'I'm interested in _____. What could I make with a computer that would help me?' Then try one of the suggestions."

> Open your AI tool now. You have 10 minutes on this first step.

**Vocabulary reference slide** (put up on a second screen, or tell students to photograph it – same approach as Week 1). Do not explain it. Students will encounter these concepts as they work. Name them during circulation.

| Term | Meaning |
|------|---------|
| **prompt** | What you type or say to tell AI what you want |
| **generate** | When AI creates something based on your prompt |
| **revise** | To change what you said to make it better or clearer |
| **accept / modify / reject** | To keep what AI created (accept), change part of it (modify), or throw it away and try again (reject) |
| **verification** | Checking whether AI's output is correct and matches what you wanted |

**First-time AI access:** Some students will need 5–10 minutes to set up or log in. This is their Week 2 troubleshooting moment. Help them get in while others are already working on Step 1. Don't hold the class for stragglers – the students who are working are learning.

---

## Segment B: Guided Practice (0:10–1:35)

### Students Work Through the Progression (0:10–1:10)

Students work through four steps with their own wish. CLI users work in their geap-103 project folder. Browser users work in whichever tool they've chosen. Reveal each subsequent step when the room is ready – roughly every 15 minutes, but read the room. A useful check: if most students are reading output rather than typing, they're ready for the next step.

**What to do while circulating:**

| What you notice | What to say | What you're naming |
|----------------|------------|-------------------|
| Student typed a wish and got output | "Can you read it? Are there words you don't know?" | If they can't read it: "You need to tell AI about yourself. Try Step 2." |
| Student added audience info and output improved | "What changed? You told AI something about yourself and the answer got better. That's *revising* your prompt." | revise |
| Student is stuck on what to type | "Look at your wish. What exactly do you want? Who is it for? Why do you want it?" | prompt (as goal articulation) |
| Student got something good on the first try | "Good. Now try Step 3 – tell AI what you specifically need this for. Does it get more focused?" | The point isn't failure. It's that more information produces more useful output. |
| Student used Path B and got interesting suggestions | "Which one surprised you? Try that one. What do you need to tell AI about yourself to make it work for you?" | generate, then revise |
| Student is at Step 4 (expert perspective) | "What expert did you pick? Why that person? How is this output different from your version?" | perspective, verification (comparing two outputs) |
| Student's output is clearly wrong or confusing | "Is this right? How would you check? What does the output say, and does that match what you know?" | verification |
| Student's wish is very ambitious (e.g., "translate my grandmother's letters and read them in her voice") | "That's a great wish. It might be bigger than one session. Pick one piece of it and try that today. Which part matters most to you?" | The wish isn't wrong. Help the student find an entry point. |
| Student's wish is trivially satisfiable (AI answers in one turn) | "Good, that worked. Now make it harder. What else would you need? Who else might use this?" | Push toward Steps 3–4. |
| Student can't read AI's output at all (wall of text, hard vocabulary) | "Tell AI: 'Explain this in simple English. I am learning English at B1 level.' That one sentence is the most useful thing you can learn today." | revise (and this IS Step 2) |
| Student's tool won't load / gives errors / device too slow | "Try a different tool: copilot.microsoft.com, chatgpt.com, or claude.ai. If nothing works in 3 minutes, sit with a partner and share their screen. You'll set up your own tool after class." | troubleshoot |

**At ~0:25 (most students have output from Step 1), reveal Slide 2:**

**Slide 2: Add who you are**

> Now tell AI something about yourself. How does the output change?
>
> Frame: "I am _____. I need _____."

Brief pause: "Hands up if AI gave you something you couldn't easily read the first time." [Hands.] "Tell AI about yourself. Watch what changes."

**At ~0:40 (most students have tried Step 2), reveal Slide 3:**

**Slide 3: Add what you need this for**

> Now tell AI what you specifically need this for. How does it change?
>
> Frame: "I want this because _____. Focus on _____."

1–2 students share what changed. Name the pattern: "You told AI who you are and what you need, and the answer got more useful. That's the skill."

**At ~0:55 (most students have tried Step 3), reveal Slide 4:**

**Slide 4: Add an expert perspective**

> Now ask: what would an expert say about this? Pick someone who knows about your topic – a doctor, a teacher, a researcher, a coach. How does the output change?
>
> Frame: "What would a _____ say about this?"

---

### Pair Debrief (1:10–1:20)

New pairs (not the same partner as Week 1 if possible).

Display:

- "Scroll back to your first output. Now show your partner your first output and your most recent output. What changed?"
- "What did the expert say that surprised you?"
- "What did you learn that you didn't know before you started?"

---

### Class Discussion (1:20–1:35)

2–3 volunteers share. The instructor's job is to draw out the pattern:

> Every time you told AI more – about yourself, about what you need, about whose perspective to take – you got a more useful answer. The skill isn't "writing a good prompt." The skill is knowing what you need and being able to say it in English.

Introduce the Decision Log briefly. Display the template fields:

| Field | What to write |
|-------|--------------|
| **Task goal** | What were you trying to do? Why? |
| **AI used** | Which tool? |
| **Prompt snippets** | Copy up to 3 of your prompts |
| **Output summary** | What did AI produce? |
| **Decision** | Accept / Modify / Reject |
| **Verification** | How did you check? |
| **What changed** | What did you change? Why? |
| **Self-assessment** | Rate this entry + 1 sentence why |

> "After the break, you'll write one of these about what you just did. It captures what you meant, what you said, and what happened."

---

**Before break** (display): "Copy your prompts and AI's responses into a document in your week-02 folder before you close anything. You'll need them after the break."

**If a student loses their history after break:** "Open AI again and re-do Steps 1 and 3 quickly with the same wish. Write your DL about the re-do. It still counts – the point is what you said and what changed, not which attempt it was."

## Break (1:35–1:50)

---

## Segment C: Decision Log + Goal Document (1:50–2:45)

### Individual Decision Log Entry (1:50–2:10)

Display the template on screen.

> Write your own Decision Log entry about today's AI interaction. Save it as `dl01-yourname.docx` in your geap-103/decision-logs/ folder.

**Sentence frames** (display on slide – these scaffold the first few entries until students internalize the genre):

- **Task goal:** "I wanted to _____ because _____."
- **Output summary:** "The first output was _____, but after I told AI about _____, it became _____."
- **Verification:** "I checked by _____." / "I compared _____ with _____."
- **What changed:** "I added _____ to my prompt because _____."
- **Self-assessment:** "I rate this entry _____ (Excellent / Proficient / Developing / Insufficient) because _____."

**Sample DL entry** (display briefly as a model, then remove so students write their own):

> **Task goal:** I wanted to find a good route to bike to my new part-time job because I don't know the area well.
> **AI used:** ChatGPT (phone app)
> **Prompt snippets:** 1. "How do I bike from Lakeshore campus to Dundas and Ossington?" 2. "I am new to Toronto. I need a safe route with bike lanes." 3. "I start work at 7 AM. Which route has the least traffic in the morning?"
> **Output summary:** The first answer listed three routes but used street names I didn't know. The second was clearer and mentioned bike lanes. The third told me which route is quietest before 8 AM.
> **Decision:** Modify
> **Verification:** I checked one of the streets on Google Maps to see if it really has a bike lane.
> **What changed:** I added information about myself (new to Toronto, need bike lanes, early morning). Each time, the answer was more useful for my situation.
> **Self-assessment:** I rate this entry Proficient because I showed how the output changed, but I only checked one fact.

Circulate. Look for: does the entry capture how the output improved as the student said more? Not just "AI made something and I changed it" but "I told AI X about myself and the output shifted in Y way."

**If time is short, protect the DL entry.** The DL is the higher-stakes task (30% of the course grade, and the first entry sets the genre for the semester). The GD can be compressed. The session review can be shortened. The DL cannot.

Target length: ~150–200 words of student-authored text (excluding pasted AI excerpts). **For this first entry, 4–5 fields completed well is better than 8 fields completed mechanically.** Students will get faster as the genre becomes familiar.

---

### Goal Document Update (2:10–2:20)

**Prompt** (display on slide):

> What do you think now about your wishes? Write 2–3 sentences about what changed today.

**Sentence frames** (display on slide):

- "My most interesting idea right now is _____ because _____."
- "I changed my mind about _____ because _____."
- "The expert said _____, which I didn't know before."

**Writing** (10 min): Students update their Goal Document. This is entry 2. Shorter than Week 1's entry – the DL carried the heavy writing this week.

---

### Debrief (2:20–2:25)

2–3 volunteers share.

> Today you discovered that AI gets better when you tell it more about yourself. Who you are. What you need. Why you need it. Whose perspective matters. That's not a technology skill. That's an English skill. The more you can say, the more you can do.

---

### AI Session Review (2:25–2:45)

The session review is a conversation with AI – spoken or typed – that the student saves. It serves three purposes: (a) reflecting on today's learning in English, (b) getting personalised advice for next week, and (c) building a persistent record that makes AI more useful over time because it knows more about the student.

**Student review (2:25–2:38)**

Display:

> Open a new document in your week-02 folder. Name it `week02-review-yourname.docx`.
>
> **Voice mode encouraged.** Use any AI tool (voice on your phone, Copilot, ChatGPT, Claude).
>
> **First, paste this as text (then switch to voice):** "Speaking practice. I'm a B1 English student practising explaining my work. Ask me follow-up questions. If my explanation is vague, tell me what's unclear and ask me to be more specific. Don't do the explaining for me."
>
> **Then, your task:** Describe to AI what happened when you tried your prompt today. Be specific about what went well and what didn't. AI will coach you on being more specific.
>
> Start with: "Today I asked AI to help me with _____. It gave me _____. I expected _____, but what I got was _____."
>
> When AI asks you to be more specific, try. If you can say exactly what was different from what you wanted, you're practising the skill that makes AI more useful.

Students have a short exchange with AI (8–10 min). Spoken or typed – voice is better if available. If spoken on phone, student saves a screenshot or types a brief summary into the document. The document lives in the course folder and builds a record the student (and AI) can refer back to.

**What this practises:** The language of evaluation – describing what you expected vs. what you got, and being specific about the gap. This is the same skill assessed in Decision Logs (CLO 4) and in the Week 4 triad defence.

**Pair share** (5 min): "What was hard to describe? Did AI help you say it more clearly?"

**Instructor reflection on projector (2:38–2:45)** — this is the first thing to cut if time is short. The student review and pair share are more important.

Ask AI on the projector with the class watching:

> "My B1 English learners just spent an hour asking AI to help with personal goals. They practised adding information about themselves – who they are, what they need, what an expert would say. Some students found it easy and some struggled. What should I watch for next week when we introduce version control?"

Read the response together. Brief discussion: "Does this match your experience today?"

> Next week: you've started making things with AI. What happens when you lose your work? We'll make sure that never happens.

Reminders (display):
- Bring your device
- Your Decision Log entry should be in your geap-103/decision-logs/ folder
- Your Goal Document should have two entries now
- Your session review should be in your week-02 folder

---

## DL/GD Distinction (Instructor Reference)

Both a Decision Log entry and a Goal Document update are assigned this week. They practise different language skills:

| | Decision Log | Goal Document |
|---|---|---|
| **Direction** | Backward-looking | Forward-looking |
| **Focus** | A specific AI interaction | Evolving interests and ideas |
| **Language skill** | Describing what happened; how output improved as student said more | Expressing interests; explaining changes of mind; describing new discoveries |
| **Cognitive operation** | Evaluative | Exploratory |

---

## Instructor Prep Checklist

- [ ] AI tool accessible on projector (GitHub Copilot CLI recommended for demo; any tool works for students)
- [ ] Four progression slides ready (Start → Add who you are → Add what you need → Add expert perspective), each with sentence frame. Only Slide 1 is shown at launch; reveal 2–4 during practice.
- [ ] Vocabulary reference slide ready (6 terms in table format – displayed as silent reference, not pre-taught). Print copies or plan for students to photograph it if single-projector room.
- [ ] Decision Log template accessible to students (shared on LMS or OneDrive)
- [ ] Decision Log sentence frames on a slide
- [ ] Goal Document prompt + sentence frames on a slide
- [ ] Confirm students have Goal Documents from Week 1 accessible (email reminder before class)
- [ ] AI tool available for session review (same tool students used during practice)

---

## Assessment Alignment

- **Decision Log entries begin** (30% component, ongoing; 8 entries across Weeks 2–13)
- CLO 3 begins (formulate clear requests to guide AI tools) – the 4-step progression
- CLO 4 begins (evaluate AI-generated text) – comparing outputs across steps
- CLO 5 begins (communicate about technical work) – the DL entry is the first instance of this genre
- Goal Document updated (ungraded; instructor reads at Week 4)
- Instructor collects DL entries 1–2 by ~Week 4; feedback returned by Week 6

---

## Language Development Summary

| Skill | Activity |
|-------|----------|
| **Vocabulary** | 5 entries covering 7 terms (prompt, generate, revise, accept, modify, reject, verification) displayed as reference, named by instructor as students encounter the concepts during practice |
| **Speaking** | Warm-up sharing; brief whole-class check-ins during practice; pair debrief (comparing outputs, discussing expert perspective); class discussion; pair Goal Document discussion |
| **Reading** | AI-generated output across 4 progressively refined prompts (authentic digital text); Decision Log template fields |
| **Writing** | Decision Log entry (~150–200 words; documenting how output improved); Goal Document update (2–3 sentences); session review document |
| **Speaking** (session review) | Conversational AI exchange (spoken or typed) describing learning and asking for advice; pair share of AI's suggestions |
| **Listening** | Pair partner's discoveries; classmates' sharing; instructor naming vocabulary during circulation; AI-generated session feedback read aloud |

---

## Timing Summary

| Segment | Time | Minutes | Notes |
|---------|------|---------|-------|
| Warm-up | 0:00–0:05 | 5 | Show of hands, 2–3 share |
| Step 1 + Go | 0:05–0:10 | 5 | Show Slide 1 only, students start immediately |
| Student practice (Steps 1–4) | 0:10–1:10 | 60 | Steps revealed progressively; 3 brief pauses; AI access setup absorbed into Step 1 time |
| Pair debrief | 1:10–1:20 | 10 | Compare Step 1 vs Step 3 outputs |
| Class discussion + DL intro | 1:20–1:35 | 15 | Pattern, template fields, save-before-break |
| **Break** | **1:35–1:50** | **15** | |
| DL entry | 1:50–2:10 | 20 | First entry; 4–5 fields OK |
| GD update | 2:10–2:20 | 10 | 2–3 sentences |
| Debrief | 2:20–2:25 | 5 | Key line + volunteers |
| Session review (student) | 2:25–2:38 | 13 | AI exchange, pair share |
| Session review (instructor) | 2:38–2:45 | 7 | One prompt, read, react |
| **Total** | | **150 min instruction** | |

---

## Catch-Up Instructions for Latecomers

Share this with any student who missed Week 2 (e.g., post on LMS or email).

---

### If You Missed Week 2

In Week 2, we used AI for the first time. Here is what you need to do before Week 3.

**1. Try the 4-step progression with one of your wishes from your Goal Document.**

Open AI (Copilot in Word, copilot.microsoft.com, or ChatGPT). Work through these steps:

- Ask AI to help with your wish
- Tell AI something about yourself ("I am learning English. I need simple vocabulary.")
- Tell AI what you specifically need this for ("I want this because _____. Focus on _____.")
- Ask what an expert would say about your topic ("What would a _____ say about this?")

Save your prompts and AI's responses in a document in your geap-103/week-02/ folder.

**2. Write your first Decision Log entry.**

Create a file called `dl01-yourname.docx` in your geap-103/decision-logs/ folder. Fill in these fields about your AI interaction:

- **Task goal:** What were you trying to do? Why?
- **AI used:** Which tool?
- **Prompt snippets:** Copy up to 3 of your prompts
- **Output summary:** What did AI produce?
- **Decision:** Accept / Modify / Reject
- **Verification:** How did you check?
- **What changed:** What did you change? Why?
- **Self-assessment:** Rate this entry (Excellent / Proficient / Developing / Insufficient) + 1 sentence why

**3. Update your Goal Document.**

Add 2–3 sentences: what do you think now about your wishes? Did anything change when you tried AI?

**4. Read and recognise these 6 words.**

| Term | Meaning |
|------|---------|
| **prompt** | What you type or say to tell AI what you want |
| **generate** | When AI creates something based on your prompt |
| **revise** | To change what you said to make it better or clearer |
| **accept** | To keep what AI created |
| **modify** | To change part of what AI created |
| **reject** | To throw away what AI created and try again |
| **verification** | Checking whether AI's output is correct and matches what you wanted |
