# GEAP 103 Status
<!-- SUMMARY: GEAP 103 now runs as a self-paced task progression; the conference-portfolio assessment was agreed with Tim and Sigrid on 2026-10-04, but the published framework and schedules still show v6 · status: active · updated: 2026-10-04 -->

### 2026-03-25 Session Notes
- Week 4 materials written, review-boarded (6 reviewers, all R&R), revised. Triad defence format adopted. Scoring sheet trimmed to 3 criteria for diagnostic baseline.
- Week 5 materials written (not yet review-boarded).
- Assessment Framework v6 written (staggered timeline, oral reflection, evolving criteria, observation tracking, session review scenarios). Review-boarded (1 Accept, 5 R&R on practical issues). All fixes implemented.
- Session review speaking practice designed and implemented in Weeks 1–5. Role-setting prompt added to copilot-instructions.md.
- Faculty preparation module created (faculty-preparation.html + .md).
- GitHub repo created (BrettRey/geap-103), reorganised, pushed. Pages enabled.
- Advisory board saved with 6 reviewers.

### 2026-03-27/28 Session Notes (afternoon through evening)
- WCAG 2.0 AA contrast fixes on faculty-preparation.html and copilot-cli-setup-guide.html.
- Week 6 lesson plan + materials: full rewrite, review-boarded (4 Accept, 2 R&R), revised, shipped.
- Week 7 lesson plan + materials: full rewrite, review-boarded (6 R&R), revised, shipped.
- Week 4 lesson plan rewritten to match AF v6 (triads, 3 criteria). Materials package patched.
- Weeks 1-3 and 5: session reviews added, structured turn-taking, cross-cutting fixes (GitHub prerequisite, Git maintenance Wk5, sentence frames optional Wk5+).
- Whole-sequence review (Weeks 1-7): 5 R&R, 1 Accept. Cross-cutting fixes adopted/adapted/set aside.
- Week 8 lesson plan + materials: full rewrite (triads, 7→5 criteria per AF v6, AWL vocab), review-boarded (4 Accept, 2 R&R), revised, shipped.
- Week 9 lesson plan + materials: rewrite, review-boarded (4 Accept, 2 R&R), revised, second-pass review (5 Accept, 1 R&R), final fix shipped.
- Week 10 lesson plan + materials: rewrite (session review before written reflection, DL feedback moved to Wk11), review-boarded (3 Accept, 3 R&R), revised, shipped.
- Week 11 lesson plan + materials: complete rewrite (old plan omitted Micro-Defence 3 entirely), review-boarded (6 R&R), revised (criteria modelled, scoring anchors, DL feedback digital distribution, ungrouped student contingency), shipped.
- Weeks 12-14 lesson plans + materials: written, review-boarded (Wk12: 5A/1R&R, Wk13: 3A/3R&R, Wk14: 2A/4R&R), all fixes applied, shipped.
- 5 assessment rubrics created (DL, micro-defences, artifact packages, Git episodes, oral reflection). Review-boarded (6 R&R), all fixes applied, shipped.
- Sample project ideas (21 curated from Mollick/Cummins/Willison) shipped.

**All 14 weeks complete. Assessment rubrics complete. Project ideas complete.**

### 2026-03-30 Session Notes (evening)
- AI literacy integration across all 14 lesson plans. North star "What's actually there?" introduced in Week 1 and recurring through Week 14. Progressive AI literacy skills woven into existing activities (one per week, weeks 1-9). CLOs unchanged.
- Cowen/Roberts EconTalk analysis: validated course direction, identified model literacy gap (now addressed via Week 2 model comparison activity), pushed back on prompting-will-become-trivial claim for B1 learners.
- Worked example ("Elif's Pixel Art Agent Dashboard") written: follows one student through all 14 weeks. Four HTML artifacts (v1-v4) built during session with real AI prompts. v4 is a Python server + HTML dashboard that launches real CLI agents. Narrative documents the authentic iteration process.
- Sample project idea #23 (Pixel Art Agent Dashboard) added.
- Decision Log template: "AI used" → "Tool used" with expanded guidance.
- Micro-defence criterion 6 scoring anchor expanded to include tool choice.
- Week 14 transfer table expanded with 4 AI literacy skills.
- Timing audited on all modified weeks — no overflows. Week 2 persona demo moved from worked example to Segment B to fit. Week 9 pre-task planning extended by 2 min (building time 43 min instead of 45).

**Next:** Remaining worked examples at different rubric levels (due Apr 4). Instructor guide + polish (due Apr 18). v4 dashboard needs browser testing (server threading fix applied but not confirmed in browser).

### 2026-06-30 Session Notes

- Added a reusable `premortem` agent skill at `skills/premortem/SKILL.md`.
- Integrated the premortem idea into the course as a lightweight Week 8 risk-assessment move: students imagine their project has failed, work backward to the most likely reason, and write a help request for the anticipated problem.
- Updated README, instructor orientation, Week 8 lesson/instructor materials, topic sequence, student schedule, and faculty preparation prompt.

### 2026-09-04 Session Notes

- Created separate Fall 2026 schedules for the Wednesday 14-meeting section and Monday 12-meeting section, plus a reusable 13-content-meeting map.
- Confirmed that the Monday section loses two Mondays to public holidays (Labour Day and Thanksgiving) and one to Reading Week; it therefore has 12 live meetings. The Wednesday section has 14 live meetings.
- Adopted one compression: curricular Weeks 9 and 10 become a redesigned build/peer-check/verification meeting. Week 14 becomes an accessible asynchronous closeout only in the 12-meeting delivery. Weeks 12 and 13 remain separate.
- Added the canonical delivery ledger with assessment invariants, dated deadlines, make-up windows, access-neutral evidence rules, and a week-by-week contingency matrix.
- Reworked GitHub onboarding around separate paths: GitHub Free, individualized Education verification, Copilot Student activation, local Git, and document/cloud version history. Removed the clean-account test and the assumption that Education or Copilot access gates class participation.
- Hardened the standard lessons for blocked accounts, absent partners, failed links, missing drafts, AI/Copilot outages, local-only folders, network failure during oral reflection, and assessment absences.
- Corrected cross-document conflicts: Decision Log window is Weeks 2-11; feedback round 2 arrives before Week 11; Week 3 requires actual usable recovery; Week 7/11/12 Collaboration evidence has a non-GitHub equivalent; Week 12 now includes its scheduled cross-group Goal Document response; Week 13 has a defined live make-up.
- Updated both faculty-preparation prompt sources to link the repository, name all delivery versions, and rehearse fallback decisions rather than only the GitHub happy path.
- Removed remaining voice-only session-review directions and added typed-and-read or live role-play paths in the lesson-level files.
- Corrected the Monday-section feedback and make-up calendar: DL feedback round 2 returns November 23, and the October 5 Micro-Defence make-up occurs by October 9 rather than after the Thanksgiving closure.
- Updated the optional Copilot CLI guide to use GitHub's current installation and login commands, to distinguish Education approval from Copilot activation, and to stop safely when installation or account access is blocked.
- Premortem and delivery-repair plan saved under `reviews/`; all new/changed Markdown parses with Pandoc and all local links resolve.

**Micro-Defence observation fallback:** When the instructor lacks enough direct evidence from the triad, the student may book a short live follow-up outside class. The result remains Deferred until the observation occurs. This is an individual contingency, not a mandatory appointment system.

**Next:** Publish the section-specific LMS schedule and exact absence make-up blocks; prepare/download the Week 2 static responses, Week 5 manual accessibility checklist, Week 6 alternate datasets, and Week 7 document-path practice artifact before teaching.

### 2026-10-04 Status

- Classes moved to the self-paced task progression from September 23 (`reviews/self-paced-task-progression-2026-09-17.md`; student guide in `materials/self-paced-student-guide-2026-09-22/`). The September 4 notes above are superseded where they assume weekly lessons.
- Assessment: the conference portfolio (Plan 2 in `reviews/assessment-plans-2026-09-29.md`) was proposed on 2026-09-29 and agreed by Tim and Sigrid. See the 2026-10-04 entry in `DECISIONS.md` for its terms.
- Tasks 11A, 14A and 17A (MCP and API use) are drafted in the progression only. They're not yet in the student guide and are untested in the app.
- Sigrid plans to observe Brett's class on October 5, including conferences, and to compare levels with him.
- Built for October 5, not yet pushed: student announcement (`materials/assessment-announcement-2026-10.md`), conference observation sheet (`admin/conference-observation-sheet.md`, `output/pdf/conference-observation-sheet.pdf`), conference tracker template (`admin/conference-tracker-template.xlsx`), and v7 updates to the framework, both section schedules, `student-schedule.md`, the delivery ledger, and README. Filled trackers go in the gitignored `private/` folder.
- Grading Option 1 adopted (confirmed levels, pass gate, caps; weights unchanged). The tracker computes confirmed levels, the gate, caps, and course grades; the announcement, framework v7, observation sheet, and student schedule state the rules. Every conference also asks about AI use, giving evidence for outcomes 3 and 4.
- Course terminology applied (GitHub, Copilot as the harness, model, agent, chat interface, session) to the student guide, its rebuilt `student-guide.zip`, and the progression. The guide now shows "Updated October 4, 2026". Not pushed.
- Tim and Sigrid were sent the grading rules, terms, and materials on 2026-10-04. October 5 class plan: `reviews/class-plan-2026-10-05.md`; milling questions: `materials/milling-2026-10-05.md`.

- The student guide folder and its zip were published on 2026-10-04 (commit 4b7d7f6); Pages serves it at https://brettrey.github.io/geap-103/materials/self-paced-student-guide-2026-09-22/. Task 4's version history and Git explanation and the new glossary entries were pushed the same day (commit e639f52). Later pushes the same day added the work-log pointer in Tasks 4–5, copying a path in Task 1, and the rule that Git repositories stay out of synced folders (Task 7 and the setup page; commit c955e29).

- The announcement, the Monday schedule, and the October 5 milling questions were pushed on 2026-10-04 (commit 1c197d7).

- The rest of the v7 changes students can see (Wednesday schedule, `student-schedule.md`, framework, README, delivery ledger, `.gitignore`) were pushed on 2026-10-04 (commit e16ee1f).
- One `GEAP103` course folder in the home folder is now the rule for students (guide Task 1, step 2; Task 7; setup page; pushed in commit e43273f). Brett's files are copied to `~/GEAP103`; delete `Documents/GEAP103` after re-pointing Copilot.

**Next:** Before Task 7, test where Copilot puts a repository it clones from GitHub. Decide the tolerance for one outcome at level 1 (tracker default: strict). Agree the percentage conversion (proposed values are in the tracker). Confirm October 7 for the Wednesday section's first in-class writing task (none ran on September 30). Test Tasks 11A, 14A and 17A in Copilot before adding them to the student guide.
