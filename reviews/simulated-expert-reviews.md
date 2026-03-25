# Simulated Expert Reviews: GEAP 103 Assessment Framework (Draft v2)

**Date:** 2026-02-12
**Document reviewed:** Assessment_Framework_Draft_v2_2026-01-22.md
**Note:** These are simulated reviews representing the kinds of concerns and recommendations consistent with each scholar's published expertise. They do not represent the actual views of any named individual.

---

## Review 1: Language Assessment -- Constant Leung (King's College London)

**Perspective:** Classroom-based language assessment; critical analysis of CEFR application in institutional contexts.

### What is strong

The framework's central design decision, distinguishing between AI-mediated and unmediated student performance, is genuinely thoughtful and addresses a problem most EAP assessment frameworks have not yet confronted. The explicit statement that "written artifacts are expected to be LLM-assisted" while "oral micro-defences provide unmediated language evidence" shows an honest engagement with the realities of the current instructional environment rather than the usual pretence that students produce written work without technological mediation. This transparency is commendable and, frankly, rare.

The AI Decision Logs are a credible attempt to assess something difficult: the capacity to evaluate and act on AI output. The mandatory failure episode is a particularly smart inclusion. It rewards critical evaluation rather than compliant acceptance, and it generates evidence of autonomous decision-making that is hard to fake. If students can articulate *why* an AI output was wrong and *what* they did about it, that tells us something real about their developing competence.

The portfolio architecture, with multiple low-stakes collection points feeding a final reflective synthesis, is well suited to a 14-week course. The weight distribution is sensible: no single assessment carries catastrophic stakes, and the spread across weeks gives both students and instructors time to identify problems.

### What concerns me

**The oral micro-defences carry too much of the language assessment burden.** This is the only component that generates unmediated spoken language evidence, and it accounts for just 25% of the course grade, of which only 40% (i.e., 10% of the total course grade) is scored on a fluency rubric. If the course claims a B1.2 exit target, the evidential base for that claim rests on three brief oral performances totalling perhaps 10-12 minutes of student speech across 14 weeks. That is a thin foundation for a CEFR-referenced proficiency judgment.

**The fluency rubric bands raise questions.** Labelling a band "B1+" and assigning it 75-84% conflates two different measurement logics. CEFR levels describe qualitative profiles of communicative competence; percentage scores describe performance on a task relative to a marking scheme. Mapping one onto the other in this way risks giving the impression that reaching 75% on a course task *means* the student has reached B1+, which it does not and cannot. The CEFR descriptors were not designed for this kind of mechanical translation, and doing so may produce claims about proficiency that the assessment instrument cannot actually support. This is especially problematic at an institutional level: if these scores feed into progression decisions, they need to be defensible.

**The relationship between "task" and "language" in the written components is underspecified.** The Digital Artifacts and Git Episodes are assessed on checklists that appear to be primarily functional (did the student do the thing?). But these are, nominally, tasks in a language course. If a student completes a Git conflict resolution entirely through AI-assisted English, what has been assessed? Technical procedure compliance, certainly. Language competence, not necessarily. The framework needs to be clearer about *where* in these components language development is being evaluated, if it is being evaluated at all.

**Washback is a consideration.** Students will quickly learn that the oral micro-defences are where language "counts" and that written work can be substantially offloaded to AI tools. The likely washback effect is that students invest their language-development effort in preparing oral scripts for the defences and invest their strategic effort in prompt engineering for everything else. Whether that constitutes the kind of language development an EAP course should foster is a question worth asking explicitly.

### Recommendations

1. **Increase the unmediated language evidence.** Consider adding a brief written component that is also unmediated, perhaps an in-class diagnostic or a short timed writing task, so that claims about B1.2 exit competence do not rest entirely on 10 minutes of oral performance.

2. **Decouple CEFR labels from percentage bands.** Report the fluency rubric as a qualitative profile (e.g., "performance consistent with B1 descriptors for sustained monologue") and keep the percentage scoring for institutional grading purposes. Do not imply that one maps directly onto the other.

3. **Make language expectations explicit in the written components.** Even where AI assistance is expected, specify what linguistic evidence you are looking for. For instance, the verification notes could require students to explain *in their own words* what the AI did, creating a small but genuine window into their independent language use.

4. **Address the evidence gap for the exit claim.** If the institution is claiming students exit at B1.2, articulate what combination of evidence across the portfolio supports that claim. A single reflective essay and three short oral performances may not be sufficient unless the framework explicitly theorises how the other components contribute indirect evidence of language development.

---

## Review 2: Computing Education -- Mark Guzdial (University of Michigan)

**Perspective:** Computing education research; teaching computing to non-CS-majors; evidence-based pedagogy.

### What is strong

The file system literacy decision is the best call in the whole framework. There is a surprisingly robust body of evidence that students, including CS majors, struggle with hierarchical file systems, and the problem is getting worse as mobile-first users enter postsecondary. Putting it at Week 4 as a foundational, assessed artifact is smart. It is also genuinely transferable in a way that many of the other components may not be.

The AI Decision Logs with a mandatory failure episode show real pedagogical thinking. Requiring students to document a case where AI was wrong, and where *they* caught it, is the most important single assessment in this course. That is where the actual learning lives: the moment a student has to evaluate output against their own understanding. I would consider weighting this component higher.

The course arc (Discovery, Building, Creation) with a practice buffer before assessment is a reasonable progression model. Three weeks of Git practice before any graded Git work is a defensible choice.

### What concerns me

**Git is the elephant in the room.** I want to be direct: the Git expectations here are almost certainly too high for this population in this timeframe. Not because B1 learners lack intelligence, but because Git's conceptual model is genuinely difficult. Research on CS2 students (people who have already passed an introductory programming course) shows persistent confusion about staging, branching, and merge states. You are asking intermediate English language learners, who are simultaneously building the vocabulary to *talk about* these operations, to demonstrate conflict resolution within 14 weeks. The "real or instructor-staged merge conflict" option suggests you already suspect authentic conflicts may not arise organically, which is itself a signal that the task may be artificial for this context.

My specific worry: students will learn a ritual sequence of commands (or, given your AI-teammate model, a ritual sequence of prompts) without building a mental model of what a version history actually *is*. If you cannot articulate what mental model of version control you expect students to hold by Week 14, that is a design problem, not an assessment problem.

**The "not assessed: code quality" stance needs more scrutiny.** I understand the logic: if AI writes the code, assessing code quality is assessing the AI, not the student. But this creates a coherence problem. If students are using AI-assisted Git workflows, they are interacting with artifacts that have *structure*, whether that is code, markdown, or document formatting. The framework says the basic skill is "management," but management of what? If students do not develop even a rudimentary model of what is inside the artifacts they are versioning, what does "error recovery" actually mean to them? They are restoring a black box to a previous black-box state. That may be a useful workplace skill, but it is not computing literacy in any meaningful sense. I would push you to define what *just enough* structural understanding looks like, even if you are not assessing code quality per se.

**Transferability is the deeper question.** The "English is the control layer" framing is clever, and it is partly true. But the research question I would want answered is: after 14 weeks of this course, can students transfer any of these skills to a new tool, a new AI system, or a context where Copilot is not available? If the answer is "only if the new context also has AI assistance," then you have taught tool proficiency, not computing competence. That is not necessarily wrong for a course called "Basic Computer Skills," but you should be honest with yourselves about the claim you are making.

### Recommendations

1. **Reduce Git to two episodes, not four.** Restore and Collaboration are defensible. Error recovery and conflict resolution are graduate-level version control concepts dressed up as "basic skills." Replace the dropped episodes with something that reinforces file system and document management literacy, where you have a much stronger chance of building durable understanding.

2. **Add a "no-AI" checkpoint.** Even a single low-stakes task where students must complete a file management or troubleshooting operation without AI assistance. This is your only way to distinguish "student understands the concept" from "student can prompt effectively." Both are useful; only assessment can tell you which one you have actually taught.

3. **Define the mental models explicitly.** For each CLO, write one sentence describing what conceptual understanding looks like independent of any tool. If you cannot write that sentence, the CLO may be tool training rather than education. Tool training is fine, but label it honestly.

4. **Raise the weight on AI Decision Logs to 30%, drop Git Episodes to 10%.** Your assessment weights should reflect where the most important learning happens. The decision logs are where students practice judgment. Weight them accordingly.

5. **Pilot the Git Episodes with a small group before committing to this design.** If you find that instructors have to stage most of the scenarios, that is evidence that the task does not fit the context. Respond to that evidence rather than engineering around it.

---

## Review 3: Assessment Design -- David Boud (Deakin University)

**Perspective:** Sustainable assessment; evaluative judgment; self- and peer assessment; feedback design.

### What is strong

This framework has several features that any assessment scholar would welcome. First, the weight distribution across process, language, product, collaboration, and metacognition signals a genuine commitment to assessing the *practice* of learning rather than terminal products alone. That 25% sits with the AI Decision Logs, an ongoing, low-stakes, distributed task, is a sound structural choice: it creates repeated occasions for students to articulate judgments about quality, which is the raw material from which evaluative capacity develops.

The oral micro-defences are also well conceived. Asking students to walk through an artifact and justify decisions in speech, not just submit polished text, introduces a kind of dialogic accountability that written-only assessment misses. The task checklist (clear problem statement, correct terminology, shows what was tried, interprets errors, justifies solution) is doing real intellectual work: it makes the criteria for good technical communication visible to the student *before* the performance, which is a precondition for self-regulation.

The verification notes attached to digital artifacts are a small but important design move. They require students to distinguish between what the AI produced and what they themselves checked or changed, a habit of mind that matters far beyond this course.

### What concerns me

**The absence of self-assessment and peer assessment is the most significant gap in this framework.** The document notes this absence matter-of-factly, but it should be treated as an urgent design problem, not a feature to be added later. Every assessment task here asks students to produce evidence and submit it for instructor judgment. At no point are students formally asked to *judge their own work against criteria before submitting it*, or to *apply criteria to a peer's work and articulate why*. This means the framework documents performance without systematically building the capacity to evaluate performance, which is precisely the capacity students will need when no instructor is present.

For B1 language learners, this matters doubly. These students are developing not only technical skills but the English-language resources to talk about quality, error, and improvement. Self- and peer assessment tasks, scaffolded with the rubrics already present in the framework, would give students structured practice in using evaluative language, a form of language development the course claims to prioritise.

**The feedback architecture is underspecified.** The framework describes *what* students submit and *when*, but says almost nothing about what happens after submission. Who gives feedback on the AI Decision Logs? How quickly? In what form? Do students act on that feedback before the next entry, or do they simply accumulate entries? If a student's Week 3 log entry is graded "Developing," what mechanism ensures the Week 5 entry improves? Without explicit feedback loops, the ongoing structure risks becoming a collection exercise rather than a learning progression.

**The mandatory failure episode is a good instinct with a design risk.** Requiring students to document a case where AI was wrong and the student detected the error is pedagogically sound in principle: it normalises failure and rewards critical evaluation. But mandating it as a graded requirement creates a perverse incentive. Students may perform failure rather than genuinely engage with it. If the episode is not encountered organically, students may fabricate a scenario or select a trivially obvious error. The framework needs to consider how to authenticate the episode and, more importantly, how to make failure documentation a *valued habit* rather than a compliance task.

**The Evidence-Indexed Reflection reads more like a mapping exercise than genuine reflection.** Asking students to link artifacts to CLOs and write "I can now..." sentences is useful for portfolio organisation, but it is not, in any deep sense, reflective practice. It asks students to *claim* competence and *point to* evidence, but it does not ask them to evaluate the *quality* of that evidence, identify what they would do differently, or articulate what they still find difficult. At 400-600 words across 8 CLOs, the word budget essentially guarantees surface-level treatment.

### Recommendations

1. **Add structured self-assessment to the AI Decision Logs.** Before submitting each entry, students should rate their own entry against the rubric and write one sentence justifying the rating. This adds perhaps 30 words per entry and converts a documentation task into a judgment task.

2. **Introduce peer assessment into the oral micro-defences.** After each 3-4 minute walkthrough, a peer could provide structured feedback using the same task checklist. This is a natural fit: the checklist is already clear, the oral format makes the work visible, and the peer gains practice in applying criteria.

3. **Specify the feedback cycle for ongoing assessments.** For the Decision Logs in particular, state explicitly: feedback on entry *n* is returned before entry *n+2* is due, and students are expected to identify one specific change based on that feedback.

4. **Reframe the mandatory failure episode as a recurring invitation.** Rather than requiring exactly one, encourage failure documentation in any entry and reward it when it appears. This reduces performativity and increases the chance of authentic engagement.

5. **Redesign the Evidence-Indexed Reflection to include evaluative judgment.** For each CLO, ask not only "What can I do?" and "Where is the evidence?" but also "How strong is this evidence?" and "What would I still need to work on?" This shifts the task from portfolio indexing toward genuine self-evaluation, which is the stated purpose of a capstone reflection.

---

## Cross-Review Summary

### Convergence
All three reviewers identify the **AI Decision Logs** (especially the failure episode) as the framework's strongest component. All three find something significant missing: Leung wants more language evidence, Guzdial wants fewer Git expectations, and Boud wants students judging their own work.

### Key tensions
- Guzdial recommends reducing Git to 2 episodes; the CLOs commit to Git/GitHub in CLOs 2 and 8.
- Leung and Guzdial both want some form of "no-AI" or "unmediated" assessment; the course philosophy emphasises AI as teammate.
- Boud's self-/peer-assessment recommendations add instructor coordination overhead in a 15-24 student class.

### Priority actions (synthesis)
1. Decouple CEFR labels from percentage bands (Leung) -- low effort, high defensibility gain
2. Add self-assessment to Decision Logs (Boud) -- low effort, high pedagogical gain
3. Specify feedback cycles (Boud) -- medium effort, essential for learning progression
4. Reduce Git episodes from 4 to 2-3 (Guzdial) -- medium effort, realism gain
5. Reweight: increase Decision Logs, decrease Git (Guzdial) -- low effort
6. Add peer feedback to micro-defences (Boud) -- medium effort, dual language/assessment gain
7. Make language expectations explicit in written components (Leung) -- low effort
8. Expand reflection to include evaluative judgment (Boud) -- low effort, quality gain
9. Add unmediated diagnostic component (Leung + Guzdial) -- medium effort, addresses evidence gap
10. Articulate B1.2 exit evidence basis (Leung) -- medium effort, institutional necessity
