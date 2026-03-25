# GEAP 103 Assessment Framework - Review Package

**Purpose:** Seeking feedback on assessment framework design for a new course.
**Date:** 2026-01-22

---

## Course Context

**Course:** GEAP 103 Basic Computer Skills
**Program:** English for Academic Purposes (EAP), Foundation Semester
**Hours:** 3 hours/week, 14 weeks (42 contact hours)
**Language level:** Entry A2+/low-B1, Exit B1 (IELTS 4.5 / TOEFL PBT 487 / TOEFL iBT 56)
**Grading:** Percentage grades, 50% pass (Humber College standard)

**Core philosophy:** Students use AI assistants (e.g., GitHub Copilot, Claude) to accomplish computing tasks. The AI handles syntax and code; students handle intent, judgment, and evaluation. "English is the control layer" (Mollick). The course develops skills for managing AI collaboration, not programming.

**Semester arc:** Discovery (Weeks 1-4) → Building (Weeks 5-10) → Creation (Weeks 11-14)

---

## Finalized Course Learning Outcomes (8 CLOs, 3 domains)

### Core Content (Digital and AI Competence)

**CLO 1: Articulate task goals for AI assistants**
Articulate a clear task goal and constraints when using an AI assistant to complete common computing tasks, revising prompts and instructions based on systematic review of outputs.

**CLO 2: Use AI-assisted Git/GitHub workflows**
Use AI-assisted Git/GitHub workflows to track, restore, and share versions of course and project files, interpreting system feedback and error messages to verify outcomes and troubleshoot routine problems.

**CLO 3: Organise digital files**
Organise, store, and retrieve digital files using appropriate workflows (foldering, naming conventions, file formats, cloud storage, and version history). Where introduced, apply basic command-line and/or version control practices to track changes.

**CLO 4: Evaluate AI-generated outputs**
Evaluate AI-generated outputs using course-provided models and checklists (accuracy, completeness, relevance, bias, accessibility, and academic integrity), and document decisions about correction, verification, or rejection.

### Language and Communication

**CLO 5: Interpret technical instructions and troubleshoot**
Interpret technical instructions, interface guidance, and error messages to troubleshoot routine problems, selecting and justifying appropriate solutions.

**CLO 6: Communicate technical information**
Communicate technical information clearly in short academic/professional genres (e.g., help request, troubleshooting log, bug report, collaboration note), using essential terminology accurately.

### Applied and Integrated

**CLO 7: Create digital artifacts**
Create and revise academic/professional digital artifacts (documents, slides, spreadsheets, and simple visualisations/automations) to college standards, including basic accessibility features (e.g., headings, alt text, captions, and accessible colour choices).

**CLO 8: Collaborate with humans and AI**
Collaborate with humans and AI on digital projects using shared workflows and AI-assisted Git/GitHub version control, contributing changes, tracking updates, and resolving routine conflicts by interpreting system output and negotiating revisions with teammates.

---

## Evidence Streams by CLO

We identified potential evidence sources for each CLO. Not every stream needs formal assessment; the question is what evidence demonstrates attainment.

**CLO 1 (Articulate task goals):**
- Prompt history / conversation exports
- Revision patterns (how prompts evolved)
- Before/after comparison (initial vs final working prompt)
- Screencasts showing real-time prompt refinement

**CLO 2 (Git/GitHub workflows):**
- Restore episodes (reverts, checkouts, resets in git log)
- Branch usage (creation, merging, deletion)
- Error recovery sequences (AI conversation + subsequent commits)
- Sharing patterns (push/pull, collaborator management, forks)
- Checkpoint rhythm (meaningful commit timing)
- Response to Git error messages (in AI conversation logs)

**CLO 3 (Organise files):**
- Repository/folder structure snapshots
- Naming convention consistency
- File format choices (appropriate to purpose)
- Structure evolution over semester
- Retrieval demonstrations (can they find things?)

**CLO 4 (Evaluate AI outputs):**
- Accept/reject decisions on AI outputs (visible in conversation logs)
- Annotations or markup showing evaluation
- Decision logs (why they chose X over Y)
- Revision history (what changed from AI suggestion to final)
- Checklist completion records

**CLO 5 (Interpret technical text, troubleshoot):**
- Issue threads (problem → diagnosis → solution arc)
- Error message handling (what they did when something broke)
- Help-seeking patterns (when/how they asked, what they tried first)
- Solution justification (in issues, reflections, or conversation)

**CLO 6 (Communicate technical info):**
- GitHub Issues authored
- PR descriptions
- Collaboration notes / handoff documentation
- Help requests (to instructor, peers, or forums)
- README or documentation contributions

**CLO 7 (Create digital artifacts):**
- The artifacts themselves
- Accessibility features present (headings, alt text, captions, colour)
- Iteration history (version progression)
- Alignment with stated purpose/goal

**CLO 8 (Collaborate):**
- PR review activity (given and received)
- Contribution graphs / authorship patterns
- Conflict resolution episodes (merge conflicts, negotiation in comments)
- Response to feedback (what changed after review)
- AI conversation logs showing human-AI collaboration patterns

---

## Key Design Considerations

### Language Assessment When Written Output Is LLM-Mediated

Much student writing will be filtered through the LLM (prompts, commit messages, PR descriptions). Written artifacts show process and product, but not necessarily language ability.

**Unmediated language evidence:**
- Live speaking (presentations, explanations, troubleshooting conversations)
- Think-alouds during screen share
- Video walkthroughs with narration
- Oral defense of decisions
- Follow-up questions about written artifacts (can they explain what "they" wrote?)

**Resolution via CLOs:** CLOs 5 and 6 are can-do statements, not grammar assessments. Effect is the measure. If communication worked, CLO is demonstrated.

### Five Complementary Lenses for Language Assessment

1. **Accept the overlap** - Language and content CLOs blur. Prompt writing is both CLO 1 (goal articulation) and CLO 6 (technical communication). Don't force separation.

2. **Threshold, not graded** - Was the language clear enough to work? Yes/no. If prompt achieves effect, language was adequate.

3. **Different genres, different focus** - Prompts = effect-focused (CLO 1); GitHub Issues, PRs, documentation = clarity-focused (CLO 6).

4. **Meta-awareness as signal** - Can students notice when their language caused AI miscommunication? "The AI did X because I said Y when I meant Z."

5. **Offload to speaking** - Written language is inherently mediated in this course. Get unmediated language evidence through speaking.

### Teacher Access to Evidence

Practical problem: 25-30 students, each with Git history, AI conversation logs, artifacts, file structures. Options considered:

1. Portfolio (student-curated)
2. Automated dashboards (GitHub stats, etc.)
3. Milestone check-ins (Weeks 4, 8, 12)
4. Spot-checking / sampling
5. Student self-assessment with verification
6. Single integrative project

These can layer.

### Portfolio as Metacognitive Structure

**Key insight:** Portfolio forces students to a meta layer. The curation work IS the learning:
- Review own work
- Judge what counts as evidence
- Select what demonstrates competence
- Articulate why

This mirrors CLO 4 (evaluate outputs, document decisions) but applied to their own work. Also professional practice - developers curate GitHub profiles, portfolios.

**Portfolio isn't just teacher convenience - it's pedagogically essential.**

---

## Draft Assessment Framework (Initial Proposal)

This was an early draft before the brainstorming above. May need significant revision based on portfolio approach.

| Assessment | Weight | Timing | Primary CLOs |
|------------|--------|--------|--------------|
| Process Logs | 25% | Ongoing (Weeks 2-13) | 1, 4 |
| Technical Communication Portfolio | 20% | Weeks 4, 8, 12 | 5, 6 |
| Digital Artifacts | 30% | Weeks 4, 10, 14 | 3, 7 |
| Collaboration & Version Control | 15% | Weeks 6-14 | 2, 8 |
| Final Reflection | 10% | Week 14 | All |

**Note:** This structure may be reconceived around a portfolio model where students curate evidence across all CLOs, with milestone check-ins and speaking assessments layered in.

---

## Open Questions

1. **Portfolio scaffolding:** How to help B1 students curate effectively? What prompts, templates, or checkpoints?

2. **Speaking integration:** When and how does the teacher assess speaking? Embedded in milestone check-ins? Separate slots?

3. **Git evidence vs gaming:** Commit cadence is evidence, but can be gamed. How to distinguish meaningful patterns from busy-work?

4. **AI tool selection:** Antigravity vs GitHub Copilot SDK vs Claude vs other. Affects what evidence is accessible.

5. **Coordination with EAPI/EAPA:** How tight should connections be? Shared projects? Independent but complementary?

6. **Weighting:** If portfolio becomes primary structure, how to weight CLO domains? Equal? Prioritized?

---

## Request for Feedback

Please review this assessment framework design and provide feedback on:

1. **Alignment:** Do the evidence streams adequately capture the CLOs? Any gaps?

2. **Feasibility:** Is this manageable for one instructor with 25-30 B1-level students?

3. **Coherence:** Does the portfolio-as-metacognition framing hold together? Any contradictions?

4. **Language assessment:** Is the approach to assessing language (effect-based, speaking-focused) sound given the LLM-mediated context?

5. **Missing considerations:** What haven't we thought about?

6. **Alternative approaches:** Are there assessment models from similar contexts (e.g., project-based learning, competency-based education, digital literacy courses) that could inform this design?
