# Simulated Expert Reviews: GEAP 103 Topic Sequence (Draft v1)

**Date:** 2026-02-12
**Document reviewed:** 14_Week_Topic_Sequence_v1_2026-02-12.md
**Note:** These are simulated reviews representing the kinds of concerns and recommendations consistent with each scholar's published expertise. They do not represent the actual views of any named individual.

---

## Review 1: Task-Based Language Teaching -- Rod Ellis (Curtin University)

**Perspective:** TBLT, task sequencing, task complexity, conditions for language acquisition.

### Strengths

The most convincing feature of this sequence is the fluency development strategy grounded in Nation's four strands, particularly the decision to recycle a small set of task types across changing content. The Decision Log (8 entries), Micro-Defence (3 iterations), and the AI interaction cycle (articulate, review, decide) all instantiate the principle that fluency emerges from repeated performance of the same task type under time pressure or with new material, not from performing a different task each week. This is well aligned with research on task repetition and its effects on complexity, accuracy, and fluency in L2 production. The sequence gets the ratio approximately right: a limited number of task types, a larger number of content domains.

The grading of autonomy across the three phases (Discovery, Building, Creation) is defensible. Early weeks constrain the task parameters tightly (one tool, one output, one Decision Log entry modelled in class), and later weeks open up choice in both topic and tool combination. This mirrors the movement from teacher-supported to learner-driven performance that task-based syllabi require if they are to develop genuine communicative competence rather than procedural compliance.

The inclusion of troubleshooting and help-request writing (Week 7) is a genuine strength from an acquisitional standpoint. Error messages and help requests create what I would call communicative necessity: the student must process meaning accurately to resolve a real problem. These are not display tasks. They demand negotiation of meaning with the system, with peers, and potentially with the instructor.

### Concerns

**1. The CLO 5/6 timing problem is real and needs resolution.** CLO 5 concerns troubleshooting and CLO 6 concerns professional communication, yet both are listed as assessed in the Week 4 Check-in, three weeks before troubleshooting is explicitly taught. If the Week 4 assessment is diagnostic (i.e., establishing a baseline), this must be made explicit in the assessment specification. If it is evaluative, the sequence has a serious alignment problem: you cannot legitimately assess outcomes that have not yet been taught. Either move these CLOs out of the Week 4 assessment, or redefine that assessment as purely diagnostic for CLOs 5 and 6 while remaining evaluative for CLO 3 only.

**2. The AI interaction cycle needs scrutiny as a "task" in TBLT terms.** A task, minimally defined, requires a communicative outcome, a gap (information, reasoning, or opinion), and primary attention to meaning. The cycle as described (articulate goal, review output, accept/modify/reject) risks functioning as a procedure rather than a task if the outcome is predetermined and the gap is trivial. When a student asks Copilot to "make this paragraph shorter" and then accepts or rejects the result, the meaning negotiation is thin. The cycle becomes a genuine task only when the goal is underspecified, the AI output is ambiguous or partially wrong, and the student must reason about the gap between intention and result. The sequence should build in deliberate mismatch between student intention and AI output, particularly in early weeks, so that the review and decision stages require real cognitive and linguistic work. Without this, the cycle is an instructional routine, not a task.

**3. Week 3 introduces version control concepts that may impose excessive cognitive load at B1.** The vocabulary burden (commit, repository, snapshot, timeline, branch, merge) is high, and the conceptual model is abstract. For A2+ to low-B1 learners, introducing Git in Week 3, before they have consolidated file management and AI interaction routines, risks overloading working memory in ways that suppress language processing. The Cognition Hypothesis predicts that increasing task complexity along resource-directing dimensions (e.g., reasoning demands) can push learners toward more complex language, but only if resource-dispersing dimensions (e.g., number of elements, planning time) are held stable. Week 3 increases both simultaneously.

**4. Meaning negotiation opportunities are unevenly distributed.** Weeks 1 through 4 are largely individual. Peer interaction appears in Week 4 (peer feedback) and then more substantially in Weeks 10 and 11 (PRs, collaborative projects). For B1 learners, interaction is not a luxury; it is the primary mechanism through which modified input and pushed output occur. The sequence would benefit from structured pair work in every week, not only in the collaboration phase.

### Recommendations

1. Redesignate the Week 4 assessment of CLOs 5 and 6 as diagnostic, or defer their assessment to Week 8.
2. Design AI interaction tasks with deliberate intention-output mismatch so that the review stage requires genuine meaning negotiation, not just accept/reject.
3. Move Git introduction to Week 5 or 6. Use Weeks 3 and 4 to deepen file management and consolidate the AI interaction cycle through repetition with varied content.
4. Add structured pair tasks in Weeks 1 through 4: paired file audits, partner Decision Log exchanges, collaborative error identification in AI output. Interaction should not wait until Week 10.
5. Specify planning time explicitly for each task. B1 learners benefit substantially from pre-task planning, and the sequence does not mention it.

---

## Review 2: Computing for Non-Programmers -- Greg Wilson (Teaching Tech Together)

**Perspective:** Evidence-based computing instruction for novices; practical realism about what learners can accomplish.

### Strengths

The design principles are sound, and more importantly, they're stated up front, which means they can actually be evaluated. The "one new tool per week" constraint and the assessment-week consolidation pattern (Weeks 4, 8, 12) show that someone has thought about pacing rather than just listing everything students should eventually know. That puts this ahead of most computing curricula I've seen.

The framing of "English is the control layer" is genuinely smart. It gives the course a reason to exist inside an EAP program that goes beyond "students need computer skills too." The Decision Log as a recurring artefact is also good: it forces metacognition about AI output without requiring technical depth, and it generates writing practice, which is the actual program goal. The cycle of articulate goal, review output, accept/modify/reject is a learnable, repeatable procedure. That matters.

The check-in weeks with no new tools are the right instinct. Three of them in fourteen weeks is about the minimum viable amount of consolidation.

### Concerns

**Git in Week 3 is the most obvious problem.** By the end of Week 2, students have had one week of "where are my files" and one week of "here is an AI assistant in Word." They are still building a mental model of files and folders. Git requires a second, more abstract mental model layered on top of the first: that a repository is a special folder, that a commit is a snapshot, that there's a timeline of snapshots. Research on novice programmers (and these students aren't even novice programmers, they're novice computer users at B1 English) consistently shows that version control is one of the hardest conceptual hurdles. You're asking students who last week learned what a file extension is to understand commits. That is too much, too soon.

**The cognitive load arithmetic doesn't work for this population.** In any given "new tool" week, students are simultaneously doing three things: learning the tool's interface, learning the English vocabulary to talk about it, and learning to evaluate AI-generated output in that tool. Each of those is a significant task on its own. Doing all three in a three-hour block (or even two 1.5-hour sessions) means something gets shortchanged every week. For students whose English is at A2+ to low-B1, the vocabulary load alone is substantial. Week 7 explicitly lists "10-15 essential technical terms," but every other new-tool week implicitly introduces at least that many. That needs to be acknowledged in the design, not just in one week.

**The Building phase tries to speedrun Office.** Word in Week 5, Excel in Week 6, PowerPoint in Week 9. Each of these applications has its own interface logic, its own Copilot interaction patterns, and its own genre conventions. Two weeks is not enough for Excel. One week is not enough for PowerPoint if you're also teaching visual communication and accessibility. The accessibility content in Week 5 is important, but bolting it onto "drafting, restructuring, formatting" in the same week means either accessibility gets ten minutes or formatting gets ten minutes.

**Collaboration is introduced too late and too fast.** PRs and Issues appear in Week 10, and by Week 11 students are expected to be doing sustained collaborative work with PR descriptions, code review, and bug reports. That's one week of introduction followed by immediate application at scale. Collaborative Git workflows are genuinely difficult. People who write software for a living get confused by merge conflicts. Giving B1 English learners one week of runway before expecting them to write PR descriptions and conduct peer review through GitHub is optimistic to the point of being unrealistic.

### Recommendations

1. **Move Git to Week 5 or 6.** Let students spend Weeks 1 through 4 getting solid on files, folders, naming, OneDrive, and Copilot in Word. Introduce Git only after they have a stable mental model of "what a file is and where it lives." Use the early weeks to build the artefacts that Git will later track.
2. **Introduce collaboration concepts in Week 8 or 9, not Week 10.** If the final project is collaborative, students need at least three weeks of practice with the collaboration tools before they depend on them. That means PRs and Issues should appear by mid-semester at the latest.
3. **Cut one Office application or give it a second week.** Excel in particular needs two weeks. If you only have one week for PowerPoint, drop the visual communication theory and just teach "make slides that aren't terrible." Be honest about what three hours can do.
4. **Make the vocabulary load explicit in every week's plan.** If you're going to introduce 10-15 terms in Week 7, do the same accounting for every other week. When you see the total, you'll know where to cut.
5. **Budget time within each three-hour block.** Write out a realistic minute-by-minute plan for Week 6 (Excel + Copilot + formula comprehension + Git episode). If it doesn't fit, it doesn't fit, and it's better to know that now than in Week 6.

---

## Review 3: Cognitive Load and Multimedia Learning -- Richard Mayer (UC Santa Barbara)

**Perspective:** Cognitive theory of multimedia learning; worked examples; segmenting; pre-training; split attention.

### Strengths

The sequence reflects several principles that cognitive science supports. The explicit constraint of one new tool per week is a sound application of the segmenting principle: it prevents the kind of element interactivity overload that arises when learners must simultaneously process multiple novel systems. The recurring task types (Decision Logs, verification notes, micro-defences) function as what the worked example literature would call "fading" structures. Once students have completed a Decision Log as a whole class in Week 2, subsequent entries require progressively more independent execution of the same schema. This is well aligned with the worked example effect, where initial guidance is withdrawn as learners develop automation of the relevant procedures.

The consolidation weeks are positioned at structurally appropriate intervals. Week 4 follows three consecutive weeks of new tool introduction, and Week 7's focus on error messages and troubleshooting is effectively a metacognitive consolidation point rather than a new-tool week, even though it appears in the "Building" phase. The design principle that "technical content serves language development" is a coherence-promoting commitment: it establishes a criterion for excluding material that does not serve the dual objective.

The course document's own identification of the four competing demands (computing concepts, English vocabulary, AI evaluation, and English proficiency) is notable. Designers who can name the sources of cognitive load are better positioned to manage them.

### Concerns

**Worked examples beyond Week 2.** The class-wide Decision Log in Week 2 is a genuine worked example, but I see few other instances where the sequence specifies that students observe a fully solved problem before attempting one themselves. Week 5 asks students to "improve a poorly formatted document," which could function as a completion problem (a partially worked example), but only if students first see a model of what a well-formatted document looks like and how it was produced. Week 10 introduces pull requests and asks students to fork a repository, submit a PR, and comment on a partner's PR. This is a complex, multi-step procedure. Without a demonstrated example of each step, the germane cognitive load of learning the PR workflow will compete with the extraneous load of figuring out the interface. I would want to see explicit worked examples specified for Weeks 5, 6, 9, and 10.

**The split-attention effect is underaddressed.** The "AI interaction cycle every class" means students are routinely attending to at least four information sources: the AI output, their own communicative intention, the tool interface, and the English vocabulary required to evaluate the output. This is a textbook case of split attention. The sequence does not describe any spatial or temporal integration strategies. For instance, are verification notes presented alongside the AI output they evaluate, or on a separate screen? Are vocabulary terms introduced before the AI interaction or during it? Without physical or temporal integration of these sources, students will engage in extensive visual search and mental integration, which the split-attention literature consistently shows degrades learning.

**Three-hour sessions and segmenting.** The sequence describes weekly topics but does not specify how 3-hour blocks are segmented internally. A 3-hour session is long by any standard; for learners processing content in a second language, it is particularly demanding. The segmenting principle would call for explicit breaks between conceptually distinct portions of each session, with learner-paced transitions rather than instructor-paced ones where feasible.

**Pre-training for Git.** Week 3 introduces Git concepts (commit as snapshot, timeline) and immediately proceeds to first repository and commits. This is the point in the sequence where I am most concerned about inadequate pre-training. Version control is conceptually unlike anything in most learners' prior experience. The pre-training principle would suggest that the mental model of "commit as snapshot" and "repository as timeline" should be established before students open a terminal or interface. A dedicated pre-training segment using visual models (animated or static diagrams of a timeline accumulating snapshots) would reduce the cognitive load of the subsequent procedural task.

### Recommendations

1. **Add explicit worked examples** for Weeks 5, 6, 9, and 10. For each new tool-task combination, specify that students first observe a complete, narrated example before attempting the task. Fade guidance across subsequent weeks.
2. **Integrate vocabulary pre-training into the session structure.** Introduce the 3-5 weekly terms before, not during, the tool interaction. This applies the pre-training principle and reduces split attention during the AI interaction cycle.
3. **Specify within-session segmenting.** For each 3-hour block, describe at least two natural break points and indicate which segments are learner-paced. This is especially important for Weeks 3, 6, and 10, which carry the highest element interactivity.
4. **Add a visual pre-training module for Git** (in Week 5/6 per the revised schedule, or as a pre-class activity) that establishes the snapshot/timeline mental model before any procedural instruction begins.
5. **Address split attention in the AI interaction cycle** by physically integrating the AI output and the verification task on a single screen or template, and by providing evaluation criteria in the same visual field as the output being evaluated.

---

## Cross-Review Summary

### Unanimous concerns
- **Git in Week 3 is too early.** All three reviewers agree, from different theoretical bases.
- **More worked examples / modelling needed** throughout, not just in Week 2.
- **Vocabulary/cognitive load is underspecified** and needs explicit accounting in every week.

### Strong agreement (2 of 3)
- **Collaboration introduced too late** (Wilson, Ellis). Pair work should appear from Week 1; collaborative Git tools (PRs/Issues) should appear by Week 8-9.
- **CLO 5/6 assessed in Week 4 before being explicitly taught** (Ellis). Needs to be diagnostic or deferred.
- **Building phase is overcrowded** (Wilson, Mayer). Excel and PowerPoint each need more time.
- **3-hour sessions need internal segmenting** (Mayer, Wilson).

### Key structural recommendation (consensus)
Move Git to Week 5 or 6. Use the freed-up Weeks 3-4 to deepen file management, consolidate AI interaction through varied repetition, and introduce pair work.

### Priority actions
1. **Restructure Weeks 1-6**: Files/OneDrive (1) → Copilot in Word (2) → Deepened file management + pair work (3) → Check-in 1 (4) → Git concepts with visual pre-training (5) → Git practice + first episodes (6)
2. **Move collaboration earlier**: PRs/Issues by Week 8-9
3. **Add worked examples** for every new tool-task combination
4. **Specify vocabulary load and session segmenting** for every week
5. **Designate Week 4 CLO 5/6 assessment as diagnostic**
6. **Design AI interaction tasks with deliberate intention-output mismatch** (Ellis)
7. **Give Excel two weeks** or reduce scope
