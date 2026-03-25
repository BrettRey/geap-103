# GEAP 103 Design Notes - Antigravity & AI-Assisted Computing

**Date:** November 18, 2025
**Contributors:** Brett Reynolds, Claude Code
**Status:** Exploratory thinking - not a finalized design

---

## Context

GEAP 103 "Basic Computer Skills" is a 3-hour/week general education course for EAP Level 1 (B1). Originally conceived as adaptation of GCMP 101 (academic upgrading computer skills), but EAP students have **language proficiency issues, not general academic issues**.

Need to reconceive entirely for EAP population strengths and needs.

---

## Claude Code Tips (Links to Review)

These links include practical tips for using Claude Code that could inform GEAP 103 demos or instructor prep:

- https://x.com/petergyang/status/2002402550570758283
- https://x.com/RileyRalmuto/status/2001525273175474466

---

## Curriculum Resources (Added 2026-01-20)

### The Missing Semester of Your CS Education
**URL:** https://missing.csail.mit.edu/
**Source:** MIT IAP course

Fills the gap between CS theory and practical tool proficiency – exactly the "invisible skills" students use constantly but rarely learn formally.

**2026 Topics:**
- Shell and command-line fundamentals
- Development environment setup
- Debugging and profiling
- Version control (Git)
- Packaging and deployment
- **AI-enhanced/agentic coding workflows** (integrated throughout, not standalone)
- Professional practices and code quality

**Relevance to GEAP 103:**
- Could adapt structure: "Missing Semester" → "Missing Digital Literacy"
- Their approach: practical skills for *doing things on computers*, not abstract CS
- 2026 curriculum integrates AI assistants throughout – validates our Antigravity-centered approach
- Materials translated into 13 languages (useful for B1 students?)
- Video lectures available – potential scaffolding resource

**Tension:** MIT assumes programming context. GEAP 103 assumes *no* programming – AI handles that. But the *workflow habits* (version control thinking, debugging mindset, iterative refinement) transfer.

---

### The Plain Person's Guide to Plain Text Social Science
**URL:** https://plain-text.co/
**Author:** Kieran Healy

Argues academics should abandon the "Office model" (Word-centric) for the "Engineering model" (plain text + version control).

**Core stack he recommends:**
- Text editors (not Word)
- R/RStudio/Stata for analysis
- RMarkdown + Knitr for reproducibility
- Pandoc for format conversion
- Git for version control

**Key argument:** The "Office model" creates coordination problems between data, analysis, citations, and prose. The "Engineering model" offers transparency, reproducibility, and maintainability.

**Relevance to GEAP 103:**
- Philosophy aligns with Mollick's insight: "everything on a computer is ultimately code"
- Plain text = universal, AI-readable, version-controllable
- Students who learn plain-text workflows can work with AI agents more effectively (structured files > opaque .docx)
- Could inform how we frame file management: "files your AI can understand" vs "files trapped in apps"
- Healy notes the paradox: friendly interfaces dominate, but powerful tools need file-system knowledge. GEAP 103 could bridge this.

**For instructor prep:** Healy's guide useful background for understanding why plain-text workflows matter – even if students don't need the full technical stack.

---

### GitHub Copilot SDK (Added 2026-01-22)
**URL:** https://github.com/github/copilot-sdk
**Status:** Technical Preview (January 2026)

Multi-platform toolkit (Python, TypeScript, Go, .NET) for embedding Copilot's agentic capabilities into applications. Exposes the same agent runtime behind Copilot CLI.

**Key features:**
- Agent orchestration with production-tested runtime
- Built-in tools: file system, Git workflows, web requests
- Custom agents, skills, and tools extensible
- All Copilot CLI models available

**Relevance to GEAP 103:**
- Alternative to Antigravity for AI tool selection decision
- Could enable custom scaffolded workflows for students
- Git integration built-in (aligns with CLOs 2, 8)
- If Humber has GitHub Education access, licensing may be simpler than Antigravity

**Open question:** Does this change the "which AI tool?" decision? Copilot SDK could allow building course-specific tooling while students use familiar GitHub ecosystem.

---

### Interactive File System Course (Gemini)
**URL:** https://gemini.google.com/share/6b4d9868b92c
**Format:** Interactive Gemini conversation/course

Interactive course teaching file systems and folder structures.

**Relevance to GEAP 103:**
- File system literacy is foundational for everything else (Missing Semester, plain-text workflows, AI agents)
- Many students arrive with "app-centric" mental models (files live *in* apps, not *on* disk)
- AI agents need file paths – students who don't understand folders can't direct agents effectively
- Could be early-semester scaffolding: "Where do files live?" before "How do I work with AI?"

**Pedagogical note:** Interactive format (conversation-based learning) aligns with GEAP 103's AI-collaboration model. Students learn *by doing*, not by lecture.

---

## Key Insight from Ethan Mollick on Antigravity

**Mollick's Quote (Nov 18, 2025):**

> "For programmers, Antigravity should be familiar territory... If you aren’t a programmer, you may dismiss Antigravity and similar tools. I think that is a mistake because the ability to code isn’t just about programming, it’s about being able to do anything that happens on a computer... A fundamental perspective powering AI development is that everything you do on a computer is, ultimately, code, and if AI can work with code it can do anything someone with a computer can: build you dashboards, work with websites, create PowerPoint, read your files, and so on. This makes agents that can code general purpose tools."

> "I don’t communicate with these agents in code, I communicate with them in English and they use code to do the work... It felt much more like managing a teammate than prompting an AI through a chat interface."

**Critical realization:**
- **The "Basic" Skill is Management:** The core competency is not "coding" but "managing a teammate" (the Agent).
- **English is the Control Layer:** Students communicate intent in English; the Agent translates intent into code.
- **The "Inbox" Metaphor:** Work is asynchronous. You send agents off, they ping you for permission/help. This mirrors professional workflows.
- **Judgment > Syntax:** Errors are "judgment calls or human-like misunderstandings," not syntax errors. The student's role is to provide the judgment the AI lacks.

---

## What Students Actually Do

### **Student's Role:**
1. **Articulate goals clearly** (in English)
   - "I need a dashboard showing themes from these interview transcripts"
   - "Create an interactive website for our group presentation"
   - "Help me organize my research notes into categories"

2. **Evaluate AI output** (critical thinking)
   - Does this work?
   - Is this what I actually wanted?
   - What's wrong or missing?

3. **Refine through iteration** (communication)
   - "Make this graph show X instead"
   - "Change the layout so..."
   - "Add a section that..."

4. **Make decisions when AI checks in** (judgment)
   - AI asks for approval or clarification
   - Student guides direction
   - Student has control

5. **Verify and validate** (quality control)
   - Test that it works
   - Check for errors or misunderstandings
   - Ensure it meets the goal

### **AI's Role:**
- Plans the approach
- Writes code to execute
- Asks for permission when needed
- Presents results for review
- Iterates based on feedback

---

## Why This Matters for Language Learning

### **Language Skills Intensively Developed:**

**Speaking/Writing:**
- Clear description of goals
- Precise feedback on AI output
- Explanation of what you want changed
- Justification of decisions

**Listening/Reading:**
- Understanding AI's explanations of what it did
- Reading technical documentation AI references
- Comprehending error messages or issues
- Following AI's plan before approving

**Pragmatics:**
- How to give effective feedback
- How to ask for what you need
- How to manage a collaborative process
- Professional communication norms

**Metacognition:**
- Evaluating quality of work
- Knowing when something is "good enough"
- Deciding when to iterate vs. move on
- Understanding your own goals better

---

## Relationship to Paul Nation's Four Strands

**Initial concern:** Where's the language fluency development?

**Realization:** The course could develop fluency through:

1. **Meaning-Focused Input:**
   - Reading AI explanations
   - Reading documentation AI suggests
   - Understanding technical concepts AI introduces
   - High volume of comprehension (AI produces a lot of output to evaluate)

2. **Meaning-Focused Output:**
   - Describing goals repeatedly
   - Giving feedback iteratively
   - Explaining what was built
   - Writing documentation

3. **Language-Focused Learning:**
   - Technical vocabulary (in context)
   - Formulaic sequences for requests
   - Precision in language (ambiguity = AI misunderstands)

4. **Fluency Development:**
   - Could happen if students do **repeated, similar tasks**
   - "Build me a visualization" → 10 different visualizations across semester
   - Same language patterns, increasing automaticity
   - **BUT:** If every task is completely novel, no fluency builds

**Open question:** How to balance variety (engaging) vs. repetition (fluency)?

---

## Potential Synergies with Existing EAP Courses

### **EAPI 106 (Integrated Language Skills) - 84 hours**

**What EAPI does:**
- Research capstone project (25% of grade)
- Written summaries, note-taking
- Oral presentations
- Academic reading and listening

**Possible synergies:**
- Students use Antigravity to **manage their research data**
  - "Organize these interview transcripts by theme"
  - "Create visualizations from this survey data"
  - "Build a dashboard showing my findings"

- Students use AI to **prepare presentations**
  - "Create an interactive presentation from these notes"
  - "Generate visual aids for these statistics"

- The technical vocabulary learned in GEAP 103 **enriches academic English**
  - Git/version control metaphors apply to research versioning
  - Data analysis terminology transfers to research methods

**Coordination needed:**
- EAPI instructors need to understand what GEAP 103 enables
- Could EAPI research projects explicitly incorporate AI tools?
- Avoid duplication of instruction on AI use

---

### **EAPA 107 (Communication & Academic Strategies) - 42 hours**

**What EAPA does:**
- Discussions (50% of grade)
- Collaborative tasks
- Online exchanges (synchronous/asynchronous)
- Multimedia resource creation (30% of grade)

**Possible synergies:**
- **GitHub as asynchronous exchange platform**
  - EAPA already assesses "participate in synchronous and asynchronous online exchanges"
  - GitHub issues/pull requests = professional async communication
  - Students learn this in GEAP 103, apply in EAPA

- **Collaborative multimedia projects**
  - EAPA multimedia resource (30%) could use Git for collaboration
  - Version control becomes necessary, not abstract
  - Students manage real collaboration challenges

- **Managing AI as teammate**
  - EAPA teaches "collaborative strategies on shared tasks"
  - Working with Antigravity = managing a collaborator
  - Same skills: checking understanding, giving feedback, coordinating

**Coordination needed:**
- Could EAPA multimedia projects be built using tools from GEAP 103?
- How to credit the technical vs. communication aspects?
- Avoid making GEAP 103 a prerequisite (they're co-requisites)

---

### **EAPC 106 (Computer-Assisted Language Learning) - 14 hours**

**What EAPC does:**
- Rosetta Stone drills (language practice)
- Graded readers (extensive reading)
- Grammar/vocabulary/pronunciation practice
- Satisfactory/Unsatisfactory grading

**Relationship to GEAP 103:**
- GEAP 103 essentially **replaces** the function of EAPC
- EAPC = 14 hours of software-driven practice (2000s technology)
- GEAP 103 = 42 hours of AI-assisted creation (2025 technology)

**Key difference:**
- EAPC: passive consumption of language drills
- GEAP 103: active creation with AI collaboration

**Consider:** Could EAPC be eliminated and hours absorbed into GEAP 103?
- Or: Keep EAPC for pure language practice, GEAP 103 for applied creation
- Need to check: What do program hour requirements allow?

---

## What Could Students Actually Build?

**Mollick's example:** "Create an attractive list of predictions I made, search web to verify, build a site"

**For EAP students, possibilities:**

### **Connected to EAPI Research:**
- Data visualization dashboards from research findings
- Interactive timelines of historical events
- Comparison tools (e.g., comparing different theories)
- Study tools (flashcards, quiz generators from their notes)
- Literature review organizers

### **Connected to EAPA Communication:**
- Group presentation websites (each person contributes section)
- Collaborative resource collections on topics
- Discussion summary tools
- Multimedia portfolios

### **Standalone Academic Tools:**
- Vocabulary learning apps from their AWL lists
- Grammar practice generators
- Reading comprehension tools
- Citation formatters and organizers

### **Transfer to Degree Programs:**
- Data analysis tools (for social sciences, business, etc.)
- Study aids for any subject
- Presentation tools
- Research management systems

**Common thread:** Students identify **problems they have** or **things they need**, then work with AI to build solutions.

---

## The Narrative Arc Question (Ira Glass)

**Glass's principles:**
- Story needs progression: beginning → middle → end
- "The Gap" between taste and ability
- Volume of work closes the gap
- Emotional journey matters

**Potential arc for GEAP 103:**

### **Act 1: Discovery (Weeks 1-4)**
- **Hook:** "You can build things you thought required programming"
- First small wins with Antigravity
- Discovering that English = your programming language
- **Emotional beat:** "Wait, I can actually do this?"

### **Act 2: Building (Weeks 5-10)**
- **Rising action:** Projects get more complex
- Learning through problems (debugging, misunderstandings)
- Iteration: first version is never perfect
- **Emotional beat:** Frustration → persistence → breakthrough

### **Act 3: Creation (Weeks 11-14)**
- **Climax:** Build something meaningful and complete
- Present/share what was created
- Reflect on the journey
- **Emotional beat:** "I made something that works. I'm capable."

**Question:** What gives coherence if every student builds something different?

**Possible answer:**
- Common **process** (even if products differ)
- Shared **language** (how we talk about working with AI)
- Progressive **complexity** (everyone goes from simple → complex)
- Collective **reflection** (what did we learn about ourselves?)

---

## Open Questions & Tensions

### **1. Coherence vs. Flexibility**

**Tension:**
- If AI can build almost anything, students could go in infinite directions
- How to maintain course coherence?

**Possible approaches:**
- **Structured progression:** Week 1 = simple visualization, Week 5 = multi-page site, Week 10 = collaborative project
- **Scaffolded freedom:** Choice within constraints ("Build a data visualization tool, choose your data")
- **Shared reflective practice:** Different artifacts, same metacognitive process

---

### **2. Assessment Philosophy**

**What do we assess?**

**NOT:** Quality of code (AI wrote it)
**NOT:** Technical sophistication (AI determined that)

**MAYBE:**
- Clarity of goal articulation
- Effectiveness of iteration/refinement
- Quality of final artifact (does it work? does it meet stated goal?)
- Depth of reflection on process
- Understanding of what was built and why

**Grading model:**
- Satisfactory/Unsatisfactory (like EAPC)?
- Portfolio of completed projects?
- Process documentation (how did you work with AI)?
- Presentation of final work?

---

### **3. Language Learning vs. Digital Literacy**

**Tension:**
- Is this a language course that uses technology?
- Or a technology course for language learners?

**Resolution:**
- It's **both**, inseparably
- The technology is the medium
- The language is the interface
- The learning happens at the intersection

**Analogy:**
- EAPI uses research to develop language skills
- GEAP 103 uses AI collaboration to develop language skills
- The vehicle differs, the destination is similar

---

### **4. Dependence on AI**

**Concern:** Are students learning to rely on AI instead of learning fundamentals?

**Counterpoint:**
- Driving doesn't require understanding internal combustion engines
- Writing doesn't require understanding printing presses
- Modern work IS working with AI - this is the fundamental skill

**But:**
- Students should understand **what AI is doing** (not just "magic")
- Students should develop **judgment** (when AI is right/wrong)
- Students should maintain **agency** (I'm managing the AI, not vice versa)

**How to ensure:**
- AI explains its approach (students read and approve plans)
- Deliberate debugging moments (AI makes mistakes, students catch them)
- Reflection on decisions (why did you ask for this? why did you accept/reject that?)

---

### **5. Relationship to Future Degree Programs**

**Value proposition:**
- "This course teaches you skills for any degree program"
- Business students: data analysis
- Social science students: research tools
- Humanities students: digital projects
- STEM students: prototyping and visualization

**But:**
- Degree programs may have their own tech requirements
- Skills need to transfer, not duplicate
- Focus on **general capability** (working with AI) not specific tools

---

## What We Don't Know Yet

### **Pedagogical unknowns:**
1. What's the learning curve for Antigravity with B1 students?
2. How much explicit instruction in AI prompting vs. learning by doing?
3. What happens when students' goals exceed their ability to articulate them?
4. How to scaffold from simple to complex without losing student ownership?

### **Practical unknowns:**
1. Antigravity licensing/access for 25-30 students?
2. Computer lab requirements (can students use own devices)?
3. What if AI tools change dramatically mid-semester?
4. How to support students with widely varying prior tech experience?

### **Coordination unknowns:**
1. Will EAPI/EAPA instructors embrace these tools or resist?
2. Can we coordinate without creating hard dependencies?
3. What if a student fails GEAP 103 but passes EAPI/EAPA?
4. How to communicate value to students (and faculty)?

---

## Frameworks to Consider (From Design Discussion)

### **Ethan Mollick - AI in Education**
- Lower floors (accessible to beginners) AND raise ceilings (experts can go further)
- Learn by making real things
- AI as thought partner, not just tool
- Experimentation over perfection

### **Paul Nation - Four Strands**
- Need balance: input, output, language-focused, fluency
- Current EAP Level 6: heavy output (50%), light fluency (7%)
- GEAP 103 could help, but only if designed intentionally for language learning
- Fluency requires **familiar material at increasing speed** (not constantly novel)

### **Ira Glass - Narrative & The Gap**
- Everyone starting out has taste but their work doesn't match yet
- The gap closes through volume of work
- Story needs emotional progression
- People remember how something made them feel

---

## CLO Evidence Streams (Added 2026-01-22)

Brainstorm of potential evidence sources for each CLO. Not every stream needs formal assessment; the question is what evidence demonstrates attainment.

---

**CLO 1: Articulate task goals for AI assistants**
*Articulate a clear task goal and constraints when using an AI assistant to complete common computing tasks, revising prompts and instructions based on systematic review of outputs.*

- Prompt history / conversation exports
- Revision patterns (how prompts evolved across a session)
- Before/after comparison (initial prompt vs final working version)
- Screencasts showing real-time prompt refinement

---

**CLO 2: Use AI-assisted Git/GitHub workflows**
*Use AI-assisted Git/GitHub workflows to track, restore, and share versions of course and project files, interpreting system feedback and error messages to verify outcomes and troubleshoot routine problems.*

- Restore episodes (reverts, checkouts, resets in git log)
- Branch usage (creation, merging, deletion)
- Error recovery sequences (AI conversation + subsequent commits)
- Sharing patterns (push/pull, collaborator management, forks)
- Checkpoint rhythm (meaningful commit timing)
- Response to Git error messages (in AI conversation logs)

---

**CLO 3: Organise digital files**
*Organise, store, and retrieve digital files using appropriate workflows (foldering, naming conventions, file formats, cloud storage, and version history). Where introduced, apply basic command-line and/or version control practices to track changes.*

- Repository/folder structure snapshots
- Naming convention consistency
- File format choices (appropriate to purpose)
- Structure evolution over semester
- Retrieval demonstrations (can they find things?)

---

**CLO 4: Evaluate AI-generated outputs**
*Evaluate AI-generated outputs using course-provided models and checklists (accuracy, completeness, relevance, bias, accessibility, and academic integrity), and document decisions about correction, verification, or rejection.*

- Accept/reject decisions on AI outputs (visible in conversation logs)
- Annotations or markup showing evaluation
- Decision logs (why they chose X over Y)
- Revision history (what changed from AI suggestion to final)
- Checklist completion records

---

**CLO 5: Interpret technical instructions and troubleshoot**
*Interpret technical instructions, interface guidance, and error messages to troubleshoot routine problems, selecting and justifying appropriate solutions.*

- Issue threads (problem → diagnosis → solution arc)
- Error message handling (what they did when something broke)
- Help-seeking patterns (when/how they asked, what they tried first)
- Solution justification (in issues, reflections, or conversation)

---

**CLO 6: Communicate technical information**
*Communicate technical information clearly in short academic/professional genres (e.g., help request, troubleshooting log, bug report, collaboration note), using essential terminology accurately.*

- GitHub Issues authored
- PR descriptions
- Collaboration notes / handoff documentation
- Help requests (to instructor, peers, or forums)
- README or documentation contributions

---

**CLO 7: Create digital artifacts**
*Create and revise academic/professional digital artifacts (documents, slides, spreadsheets, and simple visualisations/automations) to college standards, including basic accessibility features (e.g., headings, alt text, captions, and accessible colour choices).*

- The artifacts themselves
- Accessibility features present (headings, alt text, captions, colour)
- Iteration history (version progression)
- Alignment with stated purpose/goal

---

**CLO 8: Collaborate with humans and AI**
*Collaborate with humans and AI on digital projects using shared workflows and AI-assisted Git/GitHub version control, contributing changes, tracking updates, and resolving routine conflicts by interpreting system output and negotiating revisions with teammates.*

- PR review activity (given and received)
- Contribution graphs / authorship patterns
- Conflict resolution episodes (merge conflicts, negotiation in comments)
- Response to feedback (what changed after review)
- AI conversation logs showing human-AI collaboration patterns

---

## Language Evidence When Written Output Is LLM-Mediated (Added 2026-01-22)

Much student writing in this course will be filtered through the LLM. Written artifacts show process and product, but not necessarily language ability. For CLOs 5 and 6 (language/communication), unmediated evidence is needed.

**Dynamic speaking assessment**

Teachers can listen in on conversations and grade dynamically using a fluency rubric (see EAPA 107 Speaking Fluency Rubric for model: CEFR-style "I can" statements mapped to percentages).

**Unmediated speaking**
- Live verbal explanation of work (in class, office hours)
- Think-alouds during screen share (narrate while working)
- Peer teaching moments
- Presentations of projects
- Oral troubleshooting with instructor ("what's going wrong here?")

**Recorded but unscripted**
- Video walkthroughs of artifacts
- Voice memo reflections
- Screencasts with narration

**Verification of understanding**
- Follow-up questions about written artifacts (can they explain what "they" wrote?)
- Oral defense of decisions ("why did you do X?")
- If LLM wrote it and student can't explain it, that's signal

**Timed/unassisted writing**
- In-class quick writes
- Exit tickets
- Handwritten notes (low-tech fallback)

**Principle:** Anything where the student produces language in real time, without LLM mediation, becomes the language signal.

---

## Language Assessment Framing (Added 2026-01-22)

Tension: We want to evaluate written language, and the most authentic written language is what students type into the LLM (prompts, instructions, follow-ups). But we don't want them obsessing over prompt form - the course philosophy focuses on effect/outcome. Evaluating prompt effectiveness slides toward CLO 1 (articulate goals), not CLO 6 (communicate technical info).

Resolution: The CLOs themselves dissolve the tension. CLOs 5 and 6 are can-do statements, not grammar assessments:

- **CLO 5:** Can you interpret and act successfully on technical information?
- **CLO 6:** Can you communicate clearly enough to achieve the purpose, using appropriate terminology?

Effect IS the measure. If communication worked, CLO 6 is demonstrated.

**Five complementary lenses (all operate simultaneously):**

1. **Accept the overlap** - Language and content CLOs blur in this course. Prompt writing is both CLO 1 (goal articulation) and CLO 6 (technical communication). Don't force separation.

2. **Threshold, not graded** - Was the language clear enough to work? Yes/no. If prompt achieves effect, language was adequate. No fine-grained language grading on prompts.

3. **Different genres, different focus** - Prompts = effect-focused (CLO 1); GitHub Issues, PRs, documentation = clarity-focused (CLO 6, even if LLM-assisted, student approves/revises).

4. **Meta-awareness as signal** - Can students notice when their language caused AI miscommunication? That's language awareness without form obsession. "The AI did X because I said Y when I meant Z."

5. **Offload to speaking** - Written language in this course is inherently mediated. Accept that and let EAPI/EAPA carry more of the written language assessment load. Get unmediated language evidence through speaking.

---

## Teacher Access to Evidence (Added 2026-01-22)

Practical problem: 25-30 students, each with Git history, AI conversation logs, artifacts, speaking moments, file structures. How does the teacher access this without drowning?

**Options considered:**

1. **Portfolio (student-curated)** - Students select best evidence for each CLO. Teacher reviews curated selection, not everything. Reduces teacher burden, builds metacognition. Risk: students may not know what "best" means.

2. **Automated dashboards** - GitHub contribution graphs, commit stats, PR history already aggregated. Some AI tools export conversation history. Objective, low effort, but misses nuance.

3. **Milestone check-ins** - Scheduled points (Weeks 4, 8, 12) where teacher reviews current state. Combine with live conversation (double-dips as speaking assessment). Distributed workload, catches problems early.

4. **Spot-checking / sampling** - Teacher samples across students rather than reviewing everything. Manageable but incomplete picture.

5. **Student self-assessment with verification** - Students claim CLO attainment with evidence links. Teacher verifies. Students do identification work.

6. **Single integrative project** - One artifact demonstrates multiple CLOs. Coherent, assessable, but may not capture everything.

These layer - portfolio + milestone check-ins + automated dashboards could combine.

---

## Portfolio as Metacognitive Structure (Added 2026-01-22)

The portfolio approach forces students to a meta layer. The curation work IS the learning:

- Review own work
- Judge what counts as evidence
- Select what demonstrates competence
- Articulate why

This is metacognition built into the assessment structure, not bolted on as a final reflection.

Mirrors CLO 4 (evaluate outputs, document decisions) - but applied to their own work instead of AI output. Same skill, different object.

Also professional practice - developers curate GitHub profiles, portfolios, "show your work" culture. The meta layer is the job.

**Portfolio isn't just teacher convenience - it's pedagogically essential.**

**Open question:** How to scaffold portfolio curation so B1 students can do it well?

---

## External Review Feedback (ChatGPT Pro, 2026-01-22)

Framework reviewed with full context (CLOs, evidence streams, design considerations, class size 15-24, Office 365 + Copilot environment). Key feedback incorporated below.

### Environment Advantages

- OneDrive/SharePoint version history and built-in Accessibility Checker are "authentic workplace affordances" - use them rather than adding tools
- Reduces equity issues (everyone has same baseline tool access)
- Copilot chat histories aren't reliably export-friendly - curated excerpts in structured logs work better than raw conversation exports

### Structural Upgrades Recommended

**A) Process Logs → AI Decision Logs**

Replace "prompt history / exports" with structured log entries:
- Task goal + constraints (1-2 sentences)
- AI used (Copilot/other) + where (Word/Excel/Chat/etc.)
- Prompt snippet(s): max 3 turns (copy/paste or screenshot)
- Output summary: what the AI proposed (1-2 sentences)
- Decision: accept / modify / reject
- Verification: how they checked (ran it, cross-checked UI help, tested on sample data, used Accessibility Checker, etc.)
- What changed after AI (1-2 bullets)

Evidence cap: Max 8 log entries over Weeks 2-13 (roughly one every 1-2 weeks), student-selected as "best evidence". Each entry max ~150-200 words of student-authored text (excluding pasted AI excerpt).

**B) Oral Micro-Defences (Weeks 4, 8, 12)**

Three short individual check-ins per student across term:
- Student submits 2 written artifacts before each check-in
- 3-4 minute oral walkthrough of ONE artifact + 1-2 follow-up questions
- Scoring: Fluency (40%) using CEFR-style rubric + Task-based checklist (60%)

Task-based checklist components:
- Clear problem statement + context
- Correct use of 5-10 essential terms (course-defined)
- Shows what they tried (not just "it doesn't work")
- Interprets an instruction/error message accurately (or notices uncertainty)
- Justifies the chosen solution (even briefly)

Time math: 3 rounds × ~5 min/student × 24 students ≈ 6 hours across semester. Realistic during lab time.

**C) Git: Episodes Not Quantities**

Commit cadence and contribution graphs are weak evidence with beginners and easy to game. Assess required episodes instead:

1. **Restore**: demonstrate recovering an earlier version (documented)
2. **Error recovery**: one "something broke → diagnosis → fix" sequence with error text captured
3. **Collaboration**: one PR (or equivalent) with description + one comment exchange
4. **Conflict resolution**: real or staged merge conflict with brief explanation

Checklist-based assessment, with short oral confirmation for suspiciously "perfect" artifacts.

**D) Verification Notes on Artifacts**

Require a short "verification note" (3-5 bullets) attached to each artifact:
- What Copilot did
- What they changed
- What they checked

Keeps CLO 4 integrated rather than siloed.

**E) Final Reflection as Evidence Index**

At B1, long reflective writing risks becoming LLM product. Make reflection an "index + commentary":
- For each CLO: 1 claim sentence + links to 1-2 artifacts + 2-3 lines of justification
- "What I learned / what I can now do / what I check now that I didn't before"

Stays aligned with portfolio-as-metacognition rationale, keeps workload controlled.

### Two Tightening Moves

**1. Mandatory failure/rejection episode**

Require exactly one portfolio entry where:
- The AI output was wrong/misleading/inappropriate
- The student detected the problem
- The student rejected or substantially revised it, and explains why

Directly operationalizes CLO 4, prevents "AI success theatre."

**2. CLO 5 vs CLO 6 assessor guidance**

For marking reliability, internal distinction (not necessarily student-facing):
- **CLO 5** evidence centres on interpretation and choice under uncertainty (reading the system, diagnosing, selecting a fix, justifying)
- **CLO 6** evidence centres on packaging information for another person (genre moves: context, reproduction steps, expected/actual, polite tone, concise terminology)

A single artifact can support both; rubric tells assessor what to look for so they don't collapse them into "they explained something."

### Fluency Rubric Alignment with B1.2 Target

For B1.2-benchmarked course, operationally relevant anchors:
- **50% band**: "short contributions... pauses/false starts... very evident" (A2+/low B1)
- **75% band**: "relative ease... able to keep going... pauses for planning/repair evident" (B1)
- **80%+ bands**: B2-ish and above; will be rare at this level

Use fluency rubric only for "delivery/flow" slice of oral evidence. Pair with task-based checklist for "technical explanation quality" tied to CLO 5/6.

---

## Next Steps (When Ready to Move from Thinking to Designing)

**Not now. But eventually:**

1. Define the **semester narrative arc**
   - What's the opening hook?
   - What's the progression?
   - What's the culminating experience?

2. Identify **scaffolded project types**
   - Week-by-week progression
   - Increasing complexity
   - Maintaining student agency

3. Develop **assessment framework**
   - What demonstrates learning?
   - How to assess process vs. product?
   - Rubrics that make sense for AI-assisted work

4. Create **synergy touchpoints** with EAPI/EAPA
   - Specific coordination opportunities
   - Shared vocabulary/concepts
   - Complementary assessments

5. Design **instructor materials**
   - How to facilitate (not lecture)
   - Troubleshooting guide
   - Example projects
   - Reflection prompts

6. Pilot and iterate
   - Small scale first
   - Gather student feedback
   - Adjust based on what actually happens

---

## Closing Thoughts

**The big idea:**
GEAP 103 could be the course where EAP students discover they can **accomplish anything on a computer** by working with AI agents using **English as their interface**.

Not "learning to code."
Not "learning Git commands."

But: **Learning to articulate goals, evaluate results, refine iteratively, and manage AI collaboration to build real things.**

This is:
- Language-intensive (all communication is in English)
- Transferable (applies to any field)
- Confidence-building (especially for international students)
- Future-focused (this is how modern work happens)

**The challenge:**
- Maintaining course coherence with student-directed projects
- Balancing structure with flexibility
- Ensuring language learning remains central (not just "cool tech stuff")
- Coordinating with existing courses without creating dependencies

**The opportunity:**
- Create something genuinely new
- Position EAP students as **capable digital creators**, not just language learners
- Build skills that transfer immediately to degree programs
- Model what language learning + AI collaboration looks like

---

**Document Status:** Exploratory notes, not design
**Next:** Continue thinking. Read more Mollick. Consider Nation's frameworks. Talk to colleagues.
**Created:** November 18, 2025
**By:** Brett Reynolds with Claude Code
