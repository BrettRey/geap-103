# GEAP 103 Assessment Framework (Draft v2)

**Course:** GEAP 103 Basic Computer Skills
**Version:** Draft v2, 2026-01-22
**Status:** Revised after external review

---

## Grading

- Percentage grades (Humber standard)
- Pass threshold: 50%
- Language level: Exit target B1.2 (IELTS 4.5 / TOEFL PBT 487 / TOEFL iBT 56)
- Entry level: A2+ to low-B1
- Class size: 15-24 students
- Environment: Office 365 + Copilot

---

## Assessment Overview

| Assessment | Weight | Timing | Primary CLOs |
|------------|--------|--------|--------------|
| AI Decision Logs | 25% | Ongoing (8 entries, Weeks 2-13) | 1, 4 |
| Oral Micro-Defences + Written Artifacts | 25% | Weeks 4, 8, 12 | 5, 6 |
| Digital Artifacts + Verification Notes | 25% | Weeks 4, 10, 14 | 3, 7 |
| Git Episodes | 15% | Weeks 6-14 | 2, 8 |
| Evidence-Indexed Reflection | 10% | Week 14 | All |

**Total: 100%**

---

## Assessment Details

### 1. AI Decision Logs (25%)

**What:** Structured documentation of AI-assisted work, curated by student.

**Format:** Template-based log entries (max 8 across semester, student-selected as best evidence):

| Field | Content |
|-------|---------|
| Task goal + constraints | 1-2 sentences |
| AI used | Copilot / Claude / other + where (Word/Excel/Chat/etc.) |
| Prompt snippet(s) | Max 3 turns (copy/paste or screenshot) |
| Output summary | What the AI proposed (1-2 sentences) |
| Decision | Accept / Modify / Reject |
| Verification | How they checked (ran it, used Accessibility Checker, tested on sample, etc.) |
| What changed | 1-2 bullets |

**Evidence cap:** ~150-200 words student-authored text per entry (excluding pasted AI excerpt).

**Mandatory failure episode:** At least 1 of the 8 entries must document a case where AI output was wrong/misleading, student detected the problem, and rejected or substantially revised it with explanation.

**CLO Alignment:**
- CLO 1: Task goal articulation, prompt revision
- CLO 4: Evaluation of AI outputs, decision documentation

**Grading Criteria:**

| Level | Description | % Range |
|-------|-------------|---------|
| Excellent | Clear goals, systematic evaluation, substantive decisions with rationale, includes meaningful failure episode | 85-100 |
| Proficient | Goals stated, evaluation present, decisions documented, failure episode present | 70-84 |
| Developing | Goals vague, evaluation superficial, minimal decision rationale | 50-69 |
| Insufficient | Missing elements, no failure episode, unclear process | 0-49 |

---

### 2. Oral Micro-Defences + Written Artifacts (25%)

**What:** Three check-ins across semester combining written technical communication with oral demonstration of understanding.

**Schedule:** Weeks 4, 8, 12

**Process:**
1. Student submits 2 written artifacts before each check-in (e.g., help request + troubleshooting log, or GitHub issue + collaboration note)
2. 3-4 minute oral walkthrough of ONE artifact
3. Instructor asks 1-2 follow-up questions

**Written artifact types (CLO 6):**
- Help request
- Troubleshooting log
- Bug report
- GitHub Issue
- PR description
- Collaboration note / handoff documentation

**Scoring (per check-in):**

**Fluency component (40%)** - using CEFR-style rubric:

| Band | Description | % |
|------|-------------|---|
| B1+ | Relative ease, able to keep going, pauses for planning evident but doesn't lose thread | 75-84 |
| B1 | Can keep going in a way people understand, pauses regularly to think | 65-74 |
| A2+/low B1 | Can say longer things but slow, sometimes has to give up | 50-64 |
| Below threshold | Very short contributions, mostly words/phrases | 0-49 |

**Task component (60%)** - checklist:

| Criterion | Evidence |
|-----------|----------|
| Clear problem statement + context | ✓ / partial / ✗ |
| Correct use of essential terminology (5-10 course-defined terms) | ✓ / partial / ✗ |
| Shows what was tried (not just "it doesn't work") | ✓ / partial / ✗ |
| Interprets instruction/error message accurately (or notices uncertainty) | ✓ / partial / ✗ |
| Justifies chosen solution | ✓ / partial / ✗ |

**CLO Alignment:**
- CLO 5: Interpret technical instructions, troubleshoot, justify solutions
- CLO 6: Communicate technical information clearly in professional genres

**Time requirement:** ~5 min/student × 24 students × 3 rounds ≈ 6 hours across semester (during lab time while others work independently).

---

### 3. Digital Artifacts + Verification Notes (25%)

**What:** Three digital artifacts of increasing complexity, each with verification note.

**Artifacts:**

| Artifact | Week | Weight | Requirements |
|----------|------|--------|--------------|
| Organised file system | 4 | 7% | Logical folder structure, consistent naming, version awareness |
| Mid-semester project | 10 | 8% | Document/slides/spreadsheet/visualization, accessibility basics, Accessibility Checker screenshot |
| Final project | 14 | 10% | More complex artifact, iteration visible, meets college standards |

**Verification note (required for each artifact):** 3-5 bullets:
- What Copilot/AI did
- What the student changed
- What the student checked (including Accessibility Checker where applicable)

**Office 365 affordances to leverage:**
- OneDrive/SharePoint version history
- Built-in Accessibility Checker (require screenshot)
- Native file formats (.docx, .pptx, .xlsx) with PDF exports for versioning

**CLO Alignment:**
- CLO 3: Organise, store, retrieve digital files
- CLO 4: Evaluate AI outputs (via verification notes)
- CLO 7: Create and revise digital artifacts to college standards

**Grading Criteria:**

| Level | Description | % Range |
|-------|-------------|---------|
| Excellent | Well-organised, functional, accessible, verification note shows thoughtful AI collaboration | 85-100 |
| Proficient | Organised, functional, mostly accessible, verification note present | 70-84 |
| Developing | Some organisation, functional with issues, verification note incomplete | 50-69 |
| Insufficient | Disorganised, non-functional, missing verification note | 0-49 |

---

### 4. Git Episodes (15%)

**What:** Evidence of specific Git/version control competencies through required episodes, not quantity metrics.

**Required episodes (each demonstrated once, Weeks 6-14):**

| Episode | Evidence Required | CLO |
|---------|-------------------|-----|
| **Restore** | Demonstrate recovering an earlier version (screenshot/log of revert/checkout/restore) | 2 |
| **Error recovery** | One "something broke → diagnosis → fix" sequence with error text captured | 2, 5 |
| **Collaboration** | One PR (or equivalent) with description + one comment exchange | 8 |
| **Conflict resolution** | Real or instructor-staged merge conflict with brief explanation of what happened | 2, 8 |

**Assessment:** Checklist-based. Short oral confirmation for any suspiciously "perfect" artifact.

**CLO Alignment:**
- CLO 2: Use AI-assisted Git/GitHub workflows
- CLO 8: Collaborate using shared workflows, resolve conflicts

**Grading:**

| Level | Description | % Range |
|-------|-------------|---------|
| Complete | All 4 episodes documented with clear evidence | 85-100 |
| Mostly complete | 3 episodes documented clearly, 1 weak or missing | 70-84 |
| Partial | 2 episodes documented | 50-69 |
| Insufficient | Fewer than 2 episodes | 0-49 |

---

### 5. Evidence-Indexed Reflection (10%)

**What:** Structured reflection linking claims to evidence, not open-ended prose.

**Format:** For each of the 8 CLOs:
- 1 claim sentence ("I can now...")
- Links to 1-2 portfolio artifacts as evidence
- 2-3 lines of justification ("What I learned / what I can now do / what I check now that I didn't before")

**Total length:** ~400-600 words (roughly 50-75 words per CLO)

**CLO Alignment:** All (metacognitive synthesis)

**Grading Criteria:**

| Level | Description | % Range |
|-------|-------------|---------|
| Excellent | Specific claims, appropriate evidence links, genuine insight about learning | 85-100 |
| Proficient | Claims present, evidence linked, some reflection | 70-84 |
| Developing | General claims, weak evidence links, minimal reflection | 50-69 |
| Insufficient | Missing CLOs, no evidence links, no reflection | 0-49 |

---

## CLO Coverage Matrix

| CLO | Decision Logs | Oral + Written | Artifacts | Git Episodes | Reflection |
|-----|---------------|----------------|-----------|--------------|------------|
| 1. Articulate task goals | **Primary** | | Secondary | | Secondary |
| 2. Git/GitHub workflows | | | | **Primary** | Secondary |
| 3. Organise digital files | | | **Primary** | | Secondary |
| 4. Evaluate AI outputs | **Primary** | | Secondary | | Secondary |
| 5. Interpret/troubleshoot | | **Primary** | | Secondary | Secondary |
| 6. Communicate technical info | | **Primary** | | | Secondary |
| 7. Create digital artifacts | | | **Primary** | | Secondary |
| 8. Collaborate | | | | **Primary** | Secondary |

---

## Semester Timeline

| Week | Phase | Assessment Activity |
|------|-------|---------------------|
| 1 | Discovery | — |
| 2 | Discovery | Decision Log entries begin |
| 3 | Discovery | Git introduced |
| 4 | Discovery | **Oral Micro-Defence 1**, **File System artifact due** |
| 5 | Building | |
| 6 | Building | Git episodes begin |
| 7 | Building | |
| 8 | Building | **Oral Micro-Defence 2** |
| 9 | Building | |
| 10 | Building | **Mid-Semester Artifact due** |
| 11 | Creation | |
| 12 | Creation | **Oral Micro-Defence 3** |
| 13 | Creation | Decision Logs due (8 entries) |
| 14 | Creation | **Final Artifact due**, **Git Episodes due**, **Evidence-Indexed Reflection due** |

---

## Assessor Guidance

### CLO 5 vs CLO 6 Distinction

For marking reliability:

- **CLO 5** (Interpret/troubleshoot): Evidence centres on interpretation and choice under uncertainty. Look for: reading system output, diagnosing problems, selecting a fix, justifying the choice.

- **CLO 6** (Communicate): Evidence centres on packaging information for another person. Look for: genre moves (context, reproduction steps, expected vs actual), polite tone, concise terminology, would-this-work-if-sent-to-someone test.

A single artifact can support both. Don't collapse them into "they explained something."

### Fluency Rubric Usage

Use fluency rubric only for delivery/flow slice of oral evidence. The 75% band is the target for B1.2; 80%+ is above expectation for this level.

### Failure Episode Verification

The mandatory failure/rejection episode should show:
1. What the AI got wrong
2. How the student noticed
3. What they did instead

Generic or vague failure episodes ("the AI made a mistake so I fixed it") are insufficient.

---

## Notes

- Assessment weights: Process (25%) + Language (25%) + Product (25%) + Collaboration (15%) + Metacognition (10%)
- Early assessments (Weeks 2-6) pitched at A2+; later assessments scaffold toward B1.2
- Git introduced Week 3, assessed from Week 6 (3 weeks practice buffer)
- Oral micro-defences provide unmediated language evidence; written artifacts are expected to be LLM-assisted
- Office 365 affordances (version history, Accessibility Checker) treated as authentic workplace tools
