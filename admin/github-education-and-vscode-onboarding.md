# Teacher onboarding and support plan: GitHub Education, Copilot, and VS Code

This guide is for instructors preparing GEAP 103 students for the GitHub and VS Code parts of the course.

The main operational fact is that these are **separate access paths**, not one mandatory chain:

```text
GitHub account
      ├── GitHub Free repositories → GitHub web path
      └── GitHub Education application
             ├── individual current-student documentation
             ├── Education approval
             └── 72-hour wait → Copilot Student activation

VS Code + Git installation → local Git path

OneDrive or another version-history tool → equivalent evidence path

Public course repository or starter ZIP → available without Education approval
```

GitHub Education requires each student to use their own current documentation. The instructor cannot reproduce, complete, or adjudicate this individualized process on a clean account. Begin it early, allow 72 hours after approval for Copilot Student activation, and keep every course activity usable without Education or Copilot.

## What the course should promise

Promise students:

- a clear checklist;
- a place to report the exact step where they are stuck;
- a non-punitive fallback if account verification or installation is delayed; and
- assessment based on articulation, evaluation, documentation, and communication rather than on a particular model or account tier.

Do not promise:

- that Education approval and the Copilot email will arrive at the same time;
- that an application will be decided immediately;
- that every student will see the same Copilot models;
- that Education approval automatically activates Copilot; or
- that an instructor can fix an account decision from inside the classroom.

GitHub currently distinguishes **Copilot Student** for verified students from free Copilot Pro access for verified teachers. The model list and agent features may differ between these plans. Students should not be instructed to purchase a plan while an included benefit is still being applied.

## Recommended timeline

### Two weeks before the first Git-dependent class, or as soon as the roster is available

- Send students the [student setup guide](../onboarding/student-setup.md).
- Tell students to begin GitHub Education verification immediately.
- Explain what counts as proof of current student status.
- Explain that documents remain inside GitHub's application and are never sent to the instructor.
- Give a concrete date by which students should show you a pending, approved, or blocked status.
- Decide what the class fallback will be: campus computers, browser-based work, OneDrive version history, paired work, or instructor demonstration.

### One week before

- Check your own GitHub Education and Copilot status.
- Verify that the course repository, Pages site, starter ZIP, and links work in a private browser window.
- Test the public and signed-out path: course links, starter ZIP, and public repository. Test instructor-owned tools only with your own authorized account. Do not attempt to reproduce a student's Education-verification result.
- Confirm whether students need to create personal repositories, use a teacher-provided repository, or use GitHub Classroom. Do not make students guess which repository is theirs.
- Prepare a class troubleshooting sheet using the table below.

### Three days before

- Ask for a simple status check, not screenshots of private documents: `not started`, `pending`, `approved—waiting for email`, `Copilot active`, or `blocked`.
- Group common problems before class.
- Remind students that a current student card, schedule, transcript, or enrolment letter may be useful proof. The application may prefer a camera photo and may accept only one image; students can combine current enrolment and identity evidence in that image if GitHub's form permits it.
- For students already approved, record the approval date; the 72-hour Copilot wait starts from that date, not from the application date.
- Remind students never to post passwords, two-factor codes, or identity documents in class channels.

### First class

- Explain the separate paths on the projector. Do not demonstrate a student's individualized document submission or ask a student to project it.
- Have students open their own account and status page, not share accounts.
- Use a two-minute smoke test on each student's available path: open the course folder, use an available AI or static-output task, and confirm the student's declared version-history path.
- Pair students by task, not by account status: one student can explain what they see while the other follows the steps.
- Move blocked students to the fallback activity without making them wait for the whole class.

## Teacher preflight checklist

### Accounts and permissions

- [ ] My GitHub account is verified as a teacher, if I am using the teacher benefit.
- [ ] I know whether my account shows Copilot Pro or another Copilot plan.
- [ ] I can sign into GitHub in a private browser window.
- [ ] I know which GitHub account owns the course repository.
- [ ] I have checked that no organization policy blocks Copilot or Git operations.

### Course repository

- [ ] The public repository link works.
- [ ] The README links to the student guide.
- [ ] The starter ZIP downloads and opens.
- [ ] The starter kit contains the expected folder structure and Copilot instructions.
- [ ] Students have a clear path to their own working copy.
- [ ] The repository does not contain private student data, unpublished assessment information, or teacher-only notes.

### Classroom support

- [ ] The class has a fallback that does not depend on GitHub approval.
- [ ] I have a simple roster/status sheet.
- [ ] I know how students will ask for help.
- [ ] I have a short smoke test ready.
- [ ] I have allowed time for account and installation problems rather than treating them as student failure.
- [ ] I have a GitHub-web, local-Git, and version-history evidence path, and each produces individual evidence.

## Suggested status sheet

Keep only the minimum information needed. A useful status sheet has:

| Student | GitHub sign-in | Education status | Approval date | Copilot status | Git/VS Code | Declared evidence path | Smoke test | Next action |
|---|---|---|---|---|---|---|---|---|
|  | Works / blocked | Not started / Pending / Approved / Not approved |  | Waiting for 72h / Active | Ready / blocked | GitHub / local Git / version history | Pass / needs support |  |

Do not record passwords, two-factor codes, identity-document contents, or screenshots of private account pages.

## The smoke test

The first test should be small enough to complete even when students are anxious:

1. Open VS Code.
2. Sign in through the Accounts menu with the same GitHub account used for Education.
3. Open Chat with **Control + Command + I** on macOS or **Ctrl + Alt + I** on Windows/Linux.
4. Ask: `Explain what a file path is in two short sentences.`
5. Ask the student to say whether the answer matches the request.
6. Open the course folder or the repository assigned by the instructor.

For students without Copilot or VS Code, run the same request in an available AI tool or give them a static response to evaluate, then open the course folder and confirm the version-history path. The smoke test checks participation readiness, not entitlement to one product.

## Troubleshooting decision tree

### A. The Education application is pending or not approved

GitHub's verification process is individually tailored. Ask the student to show only the status wording, not private documents. Confirm:

- they used the intended GitHub account;
- they submitted the application rather than only opening it;
- they have current or clearer proof available if GitHub did not approve the first attempt; and
- they know that the 72-hour wait starts only after Education approval.

If the first attempt did not result in approval, encourage the student to read GitHub's request, add current or clearer proof, and try again. They should not make a second GitHub account. Move them to the fallback activity while the account issue is being resolved.

### B. The application was rejected or GitHub asks for more proof

Send the student to GitHub's own instructions. A current student card, schedule, transcript, or enrolment letter may be accepted. The student should upload proof only through GitHub's application flow.

Do not ask the student to email documents to the instructor. Do not try to adjudicate whether a document will be accepted.

### C. Education is approved but Copilot is still Free

Explain that Education approval and Copilot activation are separate. The approval message says to wait 72 hours after approval for the Copilot email. Send the student to [the student guide](../onboarding/student-setup.md), ask them to check spam/junk and their Education benefits settings, and record the exact status. If a paid checkout page appears, they should not purchase anything.

### D. VS Code shows the wrong GitHub account

Have the student open the Accounts menu, sign out of the wrong account, and sign in with the account used for the Education application. If the problem persists, close and reopen VS Code before escalating.

### E. Git is missing

Have the student ask Copilot for safe, step-by-step instructions for their operating system, and ask Copilot to explain each step before they run it. If they still need a direct download, send them to [git-scm.com/downloads](https://git-scm.com/downloads) or the campus IT support route. The VS Code **Open in VS Code** flow does not necessarily install Git.

### F. The computer cannot install software

Use one of the course's equity paths:

- a campus computer;
- a browser-based repository or Codespaces route, if available and tested;
- paired work with one student driving and one student articulating;
- OneDrive version history for the version-control concept; or
- instructor demonstration and a written verification note.

The learning target is not ownership of a particular laptop. It is the ability to articulate a task, evaluate what happened, document decisions, and recover from problems. A demonstration or partner's account provides practice only; graded Restore, Error recovery, and Collaboration evidence must show the individual student's action on an available path.

## Support script for authentication problems

Ask the student to report:

1. Which step they were trying to complete.
2. What they expected.
3. What happened instead.
4. The exact visible error message.
5. What they have already tried.

Useful request:

> I applied for GitHub Education on Monday using the account `example-name`. The status page still says pending. I have not received a rejection email. I expected the application to be approved already. I have not made a second account or submitted the application again.

Unsafe request:

> Send me your GitHub password, two-factor code, and a picture of your student card.

Never use the unsafe request. GitHub should handle identity documents and authentication directly.

## Repository and classroom choices

For the current course design, keep the student-facing path simple:

- use the public GEAP 103 repository as the source of course materials;
- give each student a clearly named working copy or personal repository when individual Git work begins;
- use the starter ZIP when a clean folder structure is more important than repository administration; and
- introduce pull requests and issues as communication genres in Week 7 while providing the tracked-change/version-history handoff equivalent.

If the course later adopts GitHub Classroom, test the complete teacher and student path before class. GitHub's current documentation notes that the GitHub Classroom extension for VS Code is no longer in active development; do not make that extension a required dependency without testing it first.

## Official references

- [GitHub Education for students](https://docs.github.com/en/education/about-github-education/github-education-for-students)
- [Apply to GitHub Education as a student](https://docs.github.com/en/education/about-github-education/github-education-for-students/apply-to-github-education-as-a-student)
- [Access GitHub Copilot for free as a student](https://docs.github.com/en/copilot/how-tos/copilot-on-github/set-up-copilot/enable-copilot/set-up-for-students)
- [Access Copilot Pro for free as a teacher](https://docs.github.com/en/copilot/how-tos/copilot-on-github/set-up-copilot/enable-copilot/set-up-for-teachers-and-os-maintainers)
- [Plans for GitHub Copilot](https://docs.github.com/en/copilot/get-started/plans)
- [Quickstart for GitHub educators](https://docs.github.com/en/education/quickstart)
- [Using Visual Studio Code with GitHub Classroom](https://docs.github.com/en/education/manage-coursework-with-github-classroom/integrate-github-classroom-with-an-ide/about-using-visual-studio-code-with-github-classroom)
