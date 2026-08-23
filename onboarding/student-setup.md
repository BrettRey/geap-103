# GEAP 103: GitHub Education and VS Code setup

## Start here

Please begin this setup **at least one week before the first class**. The GitHub Education application is usually decided within a few minutes. After GitHub approves your Education application, the approval message says to wait **72 hours** for an email about Copilot access.

You do not need to be a programmer. We'll learn the steps together. Your job is to follow the instructions, read what happens, and ask for help when something is unclear.

## Use this checklist as you go

You do not need to understand every item before you begin. Read the guide once, then check items off as you complete them.

- [ ] I have a GitHub account.
- [ ] I have turned on two-factor authentication if GitHub asks me to do so.
- [ ] I have applied for GitHub Education.
- [ ] I have provided proof of current student status if GitHub asked for it.
- [ ] I have received the Education decision.
- [ ] I have waited 72 hours after approval for the Copilot email.
- [ ] I have followed the email's instructions and checked that Copilot Student is active.
- [ ] I have installed Visual Studio Code.
- [ ] I have signed into VS Code with the same GitHub account.
- [ ] I can open the Copilot Chat panel.
- [ ] I have asked Copilot to help me install Git, if Git is not already installed.
- [ ] I can open the course files or the repository link provided by the instructor.

## 1. Make or check your GitHub account

Go to [github.com](https://github.com/).

If you already have a GitHub account, use it. Do not make a second account just for this course unless your instructor tells you to. If you need an account, choose **Sign up** and follow GitHub's instructions.

Use an email address that you can access. GitHub Education may ask you to connect a school email address, but a school email address is not the only possible proof of student status.

Keep your password and two-factor authentication codes private. Your instructor will never need them.

## 2. Apply for GitHub Education

Open [GitHub Education for students](https://github.com/education/students) and choose the option to apply. You can also open your [GitHub Education benefits settings](https://github.com/settings/education/benefits) and choose **Start an application**.

GitHub will ask you to prove that you are currently a student. GitHub lists examples such as:

- a student card with a current date or enrolment information;
- a current class schedule;
- a transcript; or
- a letter confirming enrolment.

The application may offer a **Take photo** button and may prefer a photo from your device. If the form accepts only one image, you can put your current student card over a blank part of a current printed schedule and take one photo, so the image shows both your identity and current enrolment. Follow the instructions that GitHub shows you.

Upload proof only through GitHub's application page. Do not send it to your instructor, to a classmate, or in a class chat.

If the first attempt does not result in approval, read the request carefully, add current or clearer proof, and try again. Be persistent. Do not make a second GitHub account.

## 3. Check the Education decision

Check [your GitHub Education benefits settings](https://github.com/settings/education/benefits). The application is usually decided within a few minutes, often in less than five minutes.

If GitHub has not approved the application:

- read the message and follow its request;
- try again with current, clearer proof if necessary;
- do not make a second GitHub account; and
- show the instructor the exact status message if you are still blocked.

The 72-hour wait does **not** start when you submit the application. It starts after GitHub approves your Education application.

## 4. After approval: wait for the Copilot email

Education approval does not mean that Copilot is active immediately. Once GitHub approves your Education application, start a 72-hour wait. The approval message says that you will then receive an email about Copilot access.

During this wait:

- do not submit another Education application;
- do not create a second GitHub account; and
- do not enter payment details if GitHub shows a paid Copilot page.

When the email arrives:

1. Follow its instructions.
2. If GitHub sends you to your [Education benefits settings](https://github.com/settings/education/benefits), open **Free GitHub developer resources for students and teachers** and choose **Learn more**.
3. Check that **Copilot Student** is active.

If the email has not arrived after 72 hours, check your spam or junk folder and your GitHub Education benefits settings. Then show the instructor the exact status message. If the problem continues, use GitHub Support. Do not buy anything to solve the problem.

Copilot may show a different set of models or features for different accounts. GEAP 103 grades your explanation, evaluation, documentation, and communication—not which model you used.

## 5. Install Visual Studio Code

Download Visual Studio Code from [code.visualstudio.com](https://code.visualstudio.com/Download). Choose the version for your operating system.

Open VS Code after it installs. If VS Code asks whether you trust a folder, only trust a folder whose files you understand or that came from your instructor or from a repository you chose to download.

## 6. Sign into GitHub in VS Code

In VS Code:

1. Open the **Accounts** menu in the lower-left or upper-right area of the window, depending on your layout.
2. Choose **Sign in with GitHub**.
3. Your browser will open. Approve the sign-in request if it is for VS Code.
4. Return to VS Code.

Use the same GitHub account that was approved for GitHub Education. If VS Code shows a different account, sign out of that account and sign in with the correct one.

## 7. Open Copilot Chat

In VS Code on macOS, press **Control + Command + I**. On Windows or Linux, press **Ctrl + Alt + I**.

You can also:

1. Open the **Chat** menu in the VS Code title bar.
2. Choose **Open Chat**.

Type a small test question, such as:

> Explain what a file path is in two short sentences.

Read the answer. Check whether it answers your question. If it does not, revise your question. This is part of the course.

## 8. Ask Copilot to help you install Git

Git saves versions of your work and lets you share them through GitHub. First ask Copilot whether Git is already installed:

> How can I check whether Git is installed on my computer?

If Git is missing, ask Copilot for instructions for your operating system:

> Git is not installed. Give me safe, step-by-step instructions for installing Git on my computer. Tell me what each step does before I run it.

Read the instructions. Do not run a command that you do not understand. If you need a direct download, use [git-scm.com/downloads](https://git-scm.com/downloads), or use the installation method your operating system recommends.

To check that Git is installed, open Terminal on macOS or Linux, or Git Bash/PowerShell on Windows, and type:

```text
git --version
```

You should see a version number. If you see an error, copy the exact error message for your help request.

## 9. Open the course files

Use the repository or starter files provided by your instructor. Do not edit the instructor's repository unless the instructor tells you to.

If your instructor asks you to download the starter kit from the course repository:

1. Open the course repository in your browser.
2. Choose **Code** → **Download ZIP**.
3. Unzip the downloaded file in a place you can find again, such as a course folder in Documents or OneDrive.
4. In VS Code, choose **File** → **Open Folder** and select the unzipped course folder.

If your instructor gives you a personal repository link, follow that link instead. The important thing is that you know where your files are and can open them again.

## If something goes wrong

| What you see | What to do |
|---|---|
| GitHub has not approved the application | The application is usually decided within minutes. Read the message, add current or clearer proof, and try again. Show the instructor the exact status message if you remain blocked. |
| GitHub asks for proof | Use a current student card, schedule, transcript, or enrolment letter. The application may prefer a camera photo and may accept only one image. Upload it only on GitHub's page. |
| GitHub Education is approved but the Copilot email has not arrived | Start the 72-hour wait from the approval time. Check spam/junk and your Education benefits settings. Do not purchase a plan. |
| VS Code shows the wrong GitHub account | Open Accounts, sign out of the wrong account, and sign in with the account used for Education. |
| Copilot Chat does not open | Check that VS Code is signed into GitHub, then reload VS Code. If it still does not work, copy the exact message. |
| Git is missing | Ask Copilot for instructions, read them, and follow the steps for your operating system. If you still need help, use [git-scm.com/downloads](https://git-scm.com/downloads). |
| You cannot install software on your computer | Tell the instructor early. We will use a campus computer, a browser-based option, or a class demonstration while the problem is solved. |

## How to ask for help

A useful help request includes:

1. What you wanted to do.
2. What you tried.
3. What happened.
4. The exact error message, if there is one.
5. What you expected to happen.

For example:

> I wanted to open Copilot Chat in VS Code. I signed in with my GitHub account and pressed Control + Command + I. The Chat panel opened, but it says that Copilot is not available. I expected to see a place to type a question. My GitHub Education application was approved yesterday.

Never include your password, two-factor authentication code, or a picture of your identity document in a help request.

## Official links

- [GitHub Education for students](https://docs.github.com/en/education/about-github-education/github-education-for-students)
- [Apply to GitHub Education as a student](https://docs.github.com/en/education/about-github-education/github-education-for-students/apply-to-github-education-as-a-student)
- [Access GitHub Copilot for free as a student](https://docs.github.com/en/copilot/how-tos/copilot-on-github/set-up-copilot/enable-copilot/set-up-for-students)
- [Visual Studio Code download](https://code.visualstudio.com/Download)
- [Git downloads](https://git-scm.com/downloads)
