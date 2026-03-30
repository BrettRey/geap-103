# Worked Example: Elif's Pixel Art Agent Dashboard

**What this document is:** The story of one student's project across the whole semester. This is not a script. The AI prompts are real. The results are real. The mistakes are real. Each version of the app (v1, v2, v3) is in the `worked-example/` folder. You can open them in your browser and see exactly what Elif got.

**Who is Elif:** A B1 EAP student from Istanbul in her Foundation Semester at Humber. She studied business administration in Turkey. She came to Canada five months ago. She uses her phone for everything and had never thought about file paths before this course.

---

## Weeks 1-2: Wishes and First Attempts

### Week 1: What Elif wants

In her first Goal Document entry, Elif writes:

> I wish my computer could help me study better. I always forget what I need to do for my courses. I want to learn how to make something useful, not just write essays. I wish I could make an app but I think that is too hard. I want to learn how to organize my files because I lose everything.

She sets up her GEAP 103 folder in OneDrive. She sketches a file-system map and discovers that most of her files are in Downloads with names like `Document (3).docx`. She renames one file and moves it to a folder. It feels small but it is the first time she has thought about where her files live.

### Week 2: Testing her words

Elif picks "help me study better" from her wish list and types this into Copilot:

> Help me study better

She gets a generic list of study tips. This is not what she wanted. She wanted a tool, not advice. In the class Decision Log exercise, she writes:

| Field | What Elif writes |
|-------|-----------------|
| Task goal | "I wanted a tool that helps me study, not a list of tips" |
| AI used | Copilot in Word |
| Prompt | "Help me study better" |
| Output summary | "It gave me 10 tips like 'take breaks' and 'use flashcards.' This is not a tool." |
| Decision | Reject |
| What changed | "I need to say WHAT KIND of help. A schedule? A quiz? A reminder? I was not specific." |

Her revised prompt:

> Make me a weekly study schedule for 4 courses. I have GEAP 103 on Monday and Wednesday, EAPI on Tuesday and Thursday, EAPA on Tuesday and Thursday, and math on Friday. Show me when to study for each one.

This gets a real schedule. It is not perfect (the times are wrong, it does not know how much homework she has), but it is a tool she can use and improve. She learns: "help me study" is a wish. "Make me a weekly schedule for 4 courses with these days" is an instruction.

In the model comparison activity, Elif and her partner type the same prompt into different tools. Elif uses Copilot; her partner uses ChatGPT. Copilot gives a table. ChatGPT gives a schedule with time blocks and colours. Same prompt, different results. Elif writes in her Decision Log: "Tool used: Copilot in Word. My partner used ChatGPT. ChatGPT made it look like a real calendar. Copilot made a simple table. I liked the table better because it was easier to change."

**Goal Document entry 2:**

> I think AI could help me make a study tool because it can organize information faster than me. My most interesting idea right now is a schedule that changes when I have a test. I changed my mind about AI because I thought it would understand what I mean, but I have to be very specific.

---

## Week 3: Never Losing Work Again

Elif creates her `GEAP-103-Portfolio` repository on GitHub. She uploads her file-system map and her Decision Log. She writes commit messages:

- `Added Week 1 file system map`
- `Added Week 2 decision log about study schedule`

She practises restoring an earlier version. She changes her file-system map (adds a new folder), commits it, then restores the old version. Both exist. She has never experienced version control before. She tells her partner: "It is like an undo button that works forever."

The instructor mentions that AI conversations have a shelf life: when they get too long, AI loses track. Elif does not think much about this now. Later, in Week 7, she will have a long conversation with Claude about her project and notice the responses getting repetitive. She will remember this lesson and start a fresh chat. It will work immediately.

**Goal Document entry 3:**

> I'm curious about making a study app because I have too many things to remember. It might look like a calendar with my courses and homework. I'm not sure yet, but I imagine something that tells me what to do each day. Maybe it can change when my schedule changes.

---

## Week 4: Where Am I Now?

Elif submits her file-system artifact package: her organized GEAP 103 folder with clear naming, and 2-3 sentences of process documentation:

> "I organized my files by week and by type. I named them with the date so I can find old versions. I would change the folder names to be shorter because some paths are very long."

In her first micro-defence, she explains her file system to two partners. The instructor asks: "Why did you name the files this way?" She answers, but she says "because it is better" instead of explaining how the naming helps her find things. She learns that "better" is not a reason. She needs to say better *for what*.

The project-type menu is shown. Elif is interested in "Data Tool" (she likes the expense tracker idea) and "Game" (the escape room sounds fun). She is not thinking about the pixel art dashboard yet. That idea has not arrived.

**Goal Document entry 4:**

> The most interesting thing I've learned is that I have to say exactly what I mean. AI does not guess. I want to try making an expense tracker next because I spend too much money on Uber Eats. My thinking changed because now I know I can make real tools, not just documents.

---

## Week 5: Making Something Others Can Read and Use

Elif learns about accessibility. She runs the Accessibility Checker on her study schedule document from Week 2. It has problems: no heading styles, no alt text on the chart Copilot made, low-contrast text.

She fixes it. Copilot applies heading styles and writes alt text. But the alt text says "An image" which is useless. She rewrites it: "A weekly study schedule showing four courses in a table. Columns are days of the week. Rows are morning, afternoon, and evening."

Her verification note:

> "The Checker found 3 problems: no headings, missing alt text, and low contrast. Copilot fixed the headings and contrast. The alt text Copilot wrote was too short. I wrote a better description of the schedule table. After my changes, the Checker found 0 problems."

She also tries the second-opinion technique from class: she pastes Copilot's original alt text ("An image") into ChatGPT and asks "Is this alt text accurate?" ChatGPT says: "This is not useful alt text. It should describe what the image shows -- the layout, the data, the purpose." This confirms her judgment. Two tools agreeing that something is wrong is more convincing than one.

This is the week the language shifts. The Goal Document prompt asks about "the user." Elif realizes that her study schedule is only for her, but if she built an expense tracker, other people might use it. What would they need?

**Goal Document entry 5:**

> The person using my project might have trouble with small text on a phone because I use my phone for everything and I know the screen is small. I need to check that my tool works on a phone, not just a laptop. One thing I learned today is that a document can look good but be broken for some people.

---

## Week 6: Making Sense of Numbers

Elif reads an existing spreadsheet (a sample budget) and builds summary calculations. She asks Copilot to add a column that calculates how much she spends per day. The formula is wrong the first time: it divides by 30 days even in February. She catches this because she checks the numbers, not because she understands the formula.

Decision Log entry:

| Field | What Elif writes |
|-------|-----------------|
| Task goal | "Add a daily spending average to my budget spreadsheet" |
| AI used | Copilot in Excel |
| Prompt | "Add a column that shows my average daily spending each month" |
| Output summary | "The formula divides by 30 for every month. February has 28 days. The number was wrong." |
| Decision | Modify |
| Verification | "I divided my February total by 28 on my phone calculator. Copilot's number was different. I asked it to use the real number of days in each month." |
| What changed | "The formula now uses a function that counts the days in each month" |

**Goal Document entry 6:**

> I am still interested in the expense tracker, but now I think it is more complicated than I thought. The numbers have to be right and AI makes mistakes with formulas. I need to check everything. I am also starting to use three different AI tools at the same time for different courses and I keep losing track of what each one is doing. That is annoying.

This is the first time she mentions the problem that will become her project.

---

## Week 7: Working Together Without Breaking Things

Elif forks a classmate's repository, makes changes to a shared document, and writes a pull request description. She writes Issues for a partner's project. The language demand is new: writing for a collaborator, not for herself.

She writes an Issue for her partner's recipe project:

> "When I click 'Scale Recipe' and type 7, the salt amount says 7 tablespoons. That is too much salt. I think the scaling should know that some ingredients do not multiply the same way."

Her partner writes an Issue for Elif's expense tracker prototype:

> "The categories are in English but you said some users might speak Turkish. Where do I change the language?"

This makes Elif think about users again. But she is also thinking about something else. She now has three AI agents she uses regularly: Claude for her essay research, Copilot for spreadsheets and documents, and ChatGPT for quick questions. She switches between browser tabs constantly. She forgets what each one is doing. She mentioned this in Week 6. Now it is bothering her more.

**Goal Document entry 7:**

> I work with 3 AI tools now. Claude helps me research for my essays. Copilot helps me with documents and spreadsheets. ChatGPT is fast for quick questions. The problem is I forget what I asked each one to do. I switch tabs and I lose track. I wish I had one screen that shows me all my agents and what they are doing. Like a control room.

The project idea is forming. Not from the sample list. From her own experience.

---

## Week 8: When Things Go Wrong

Elif's second micro-defence. She explains her expense tracker prototype. She has to show what she tried, describe errors, and interpret what went wrong. New criteria this week: "shows what was tried" and "interprets errors."

She tells the triad about the February formula bug. The instructor asks: "How did you know the formula was wrong?" Elif says: "I checked the number on my phone. The answer was different." This is verification. She is doing it naturally now.

In her Goal Document, the prompt asks about risk: what could go wrong with your project?

**Goal Document entry 8:**

> My biggest risk is that I am changing my project idea. I was going to build an expense tracker, but now I want to build something else. I want to make a dashboard that shows my AI agents as pixel art characters in an office. Each character shows what the agent is doing. I saw a video about something like this and I thought: I need this. The risk is I might not be able to describe it well enough. It is complicated. But it is the thing I actually want to use every day.

She has committed to the pixel art dashboard. The idea came from her real workflow problem (Week 6-7), not from the sample list. She saw the pixel-agents video and recognised her own need.

---

## Week 9: Building My Thing (Part 1)

This is where the building happens. Elif has one class session (about 45 minutes of building time) plus her own time outside class.

In class, the instructor taught three techniques for building: scaffolding (start small, check, add), restatement (ask AI what it thinks you want before it builds), and tool selection (pick the right AI for each task). Elif heard all three. She did not apply them in Round 1.

### Task list (Goal Document entry 9)

> Today I will focus on getting the basic office to work. The requirement is: I open the file in my browser and I see a pixel art office with 3 characters at desks. Each character is one of my agents. There are buttons to start and stop them. My draft should include the office, the characters, and the buttons by the end of today. If I finish this, I will work on animations.

### Round 1: The chess timer

Elif opens her AI tool and types:

> I want to build the pixel art agent dashboard from my project ideas list. It should show a small office with pixel art characters. Each character is one of my AI agents. When an agent is working, the character types at a desk. When it is done, it waves. I want it to look nice and work in the browser. Maybe 3 agents. The office should look like a real office with desks and computers.

She gets [v1.html](v1.html). A pixel art office with three characters, buttons to start each agent, and status dots. It works. It looks nice. She is excited for about two minutes.

Then she clicks the buttons and realizes: this is a chess timer. She clicks "Start" and the character types. She clicks "Done" and it waves. But it does not know what any agent is actually doing. It does not track real tasks. It does not remember anything. If she closes the browser and opens it again, everything is gone.

**Process documentation:**

| AI prompt | AI output | My decision | Why |
|-----------|-----------|-------------|-----|
| "Build a pixel art office with 3 agents, buttons to start/stop, animations" | A complete HTML file with office, characters, and buttons | Keep but not finished | It looks good but it is just a toy. I click buttons and characters move. It does not track real work. |

**What she learned:** Her prompt described what the app should LOOK like but not what it should DO. "When an agent is working, the character types" describes an animation, not a function. She told AI how it should look. She did not tell AI what it should be useful for.

### Peer check-in

Her partner looks at v1 and reads Elif's Goal Document (Week 8 entry about the "control room" idea). Partner says:

> "Your Goal Document says you want to see what your agents are doing. But this app does not know what they are doing. You press a button. That is you telling the app, not the app telling you."

This is exactly right. The dashboard should show Elif's real workflow, not play animations when she presses buttons.

---

### Between Rounds: What changed in Elif's thinking

Elif's Week 5 lesson about "the user" comes back. She IS the user. What does she need? Not animations. She needs to know: which agent is working on what? How long has it been? What finished today? She writes in her process notes:

> "The problem with v1 is it does not do anything real. I need to think about what I actually need when I am working. I switch between 3 agents. I forget what each one is doing. I need to see all of them in one place and know what task each one has."

### Round 2: The screensaver

She tries again:

> This is not what I meant. I don't want to click buttons to start the agents. The agents should work on their own. When I open the page, I want to see my office and the agents are already doing things.
>
> I have 3 agents: Research Agent, Code Agent, and Review Agent. They work like this:
> - Research Agent gets a task, works for a while, then finishes. Then it waits a little and gets another task.
> - Code Agent waits for Research Agent to finish, then it starts coding. It takes longer than research.
> - Review Agent waits for Code Agent to finish, then it checks the code. This is the fastest one.
> - After Review Agent finishes, sometimes it sends the work back to Code Agent because there is a problem. Maybe 30% of the time.
> - When an agent is waiting, it should look bored -- maybe drinking coffee or looking at phone.
>
> I don't want any buttons. Just the office running by itself. Maybe a small log on the side that shows what is happening, like "Research Agent started Task 3" or "Review Agent sent code back to Code Agent."

She gets [v2.html](v2.html). This is impressive. The agents work autonomously. They have a pipeline: research, then code, then review. Sometimes work gets sent back. The agents drink coffee and scroll their phones when waiting. There is an activity log. It runs by itself.

But after watching it for five minutes, she realizes: this is a screensaver. The agents are not doing HER tasks. The tasks are fake. "Task #3" is not a real thing. If she closes the browser and opens it again, the simulation just restarts. It has no connection to her actual work.

**Process documentation:**

| AI prompt | AI output | My decision | Why |
|-----------|-----------|-------------|-----|
| "Agents should work on their own, no buttons, pipeline with research/code/review, 30% revision rate, idle animations, activity log" | Autonomous simulation with pipeline, coffee/phone animations, activity log | Reject | It looks amazing but it is not real. The tasks are fake. It does not know what I am actually working on. It is a screensaver. |

**What she learned:** Her prompt described behaviour rules for a simulation, not requirements for a tool. She told AI exactly HOW the agents should move and interact, but she still did not tell AI what the tool should DO for her. The rules were interesting and the simulation was fun to watch, but "fun to watch" is not the same as "useful."

---

## Week 10: Building My Thing (Part 2)

Elif has one more class session before the mid-semester artifact package is due. She knows what went wrong twice. She writes a new task list:

### Task list (Goal Document entry 10)

> v1 was a toy because I told AI what it should look like, not what it should do. v2 was a screensaver because I told AI how agents should behave, not what I need from the tool. This time I will describe what the tool does for ME.
>
> Today I will focus on making a dashboard that tracks my REAL work. Requirements:
> 1. I can add my own agents by name
> 2. I can give each agent a real task (typing what it is doing)
> 3. I can see how long each task takes
> 4. Everything saves so I do not lose it
> 5. There is a log of what happened today

### Round 3: The real tool

Before typing her v3 prompt, Elif uses the restatement technique from Week 2. She pastes her task list into AI and asks: "Tell me what you think I'm asking for." AI's response helps her see that she needs to emphasise that this is a REAL tool for HER workflow, not another simulation. She also notices that her v3 prompt is structured differently from v1 and v2: eight numbered requirements, each one specific. She is scaffolding without realising it -- building the description one requirement at a time instead of asking for everything in one sentence.

> OK I think I understand what was wrong. The first two versions were not real tools. They were toys. I need something I will actually use every day when I work with my agents.
>
> Here is what I want now:
>
> 1. When I open the dashboard, I see my pixel art office. It is empty at first.
> 2. I can add an agent by typing its name (like "Research Agent" or "Essay Helper"). A new pixel art character appears at a desk.
> 3. I can click on a character and type what it is working on right now (like "finding sources for my essay" or "checking my grammar"). The character starts typing and the task shows on its monitor screen.
> 4. When the task is done, I click "Done" and the character waves. The task moves to a "Completed" list.
> 5. I can see how long each task took.
> 6. Everything saves in the browser so when I close and open again, my agents and tasks are still there.
> 7. There is a log on the side that shows everything that happened today, like "10:32 AM - Research Agent started: finding sources for essay"
> 8. I can remove an agent if I don't use it anymore.
>
> The important thing is: this is MY workflow. The agents are MY agents. The tasks are MY real tasks. It is not a simulation. It is a real tool for managing my work.

She gets [v3.html](pixel-agent-dashboard.html). This time, the dashboard starts empty. She adds "Claude" and a character appears at a desk. She adds "Copilot" and "ChatGPT." Three characters in the office. She clicks Claude and types "finding sources for psychology essay." Claude's character starts typing. The monitor shows the task. A timer starts. The activity log records: "10:32 AM - Claude started: finding sources for psychology essay."

When she finishes with Claude, she clicks Done. The character waves. The timer stops. The task moves to Completed with the time it took. She closes the browser. She opens it again. Everything is still there.

**Process documentation:**

| AI prompt | AI output | My decision | Why |
|-----------|-----------|-------------|-----|
| "8 specific requirements: empty office, add agents by name, assign real tasks, mark done, time tracking, save in browser, activity log, remove agents" | A complete tool that does exactly what I described | Accept | This is what I needed. It tracks my real work. It saves. It is useful. |

### What changed across three versions

| Version | What Elif described | What she got | Problem |
|---------|-------------------|--------------|---------|
| v1 | What it should LOOK like | A nice animation with buttons | No real function. A chess timer. |
| v2 | How agents should BEHAVE | An impressive simulation | No real data. A screensaver. |
| v3 | What the tool should DO for her | A real productivity tool | Works. Useful. She uses it. |

The difference was not better English. It was better thinking. Elif had to understand what "useful" means before she could describe it. That took two failures and eight weeks of learning to think about what tools do, not just what they look like.

---

## Weeks 11-14: Finishing, Sharing, Reflecting

### Week 11: Micro-Defence 3

Elif presents her dashboard to a triad. The Week 11 criteria add "describes how AI was directed" and "evaluates AI output." She walks through all three versions:

> "Version 1 failed because I described the appearance, not the function. I said 'when an agent is working, the character types' but that is just an animation. Version 2 failed because I described behaviour rules for a simulation, but a simulation is not a tool. Version 3 worked because I described 8 specific things the tool has to do for me. The most important sentence was 'this is my workflow, the agents are my agents, the tasks are my real tasks.'"

The instructor asks: "What would you change about v3?" Elif says: "The characters all look similar. I want them to be more different. And I want to see how many tasks each agent finished this week, not just today."

### Week 12: Git Episodes

Elif's Git Episodes show her version history. She has commits for v1, v2, and v3. Her Restore episode documents going back to v1 after building v2 to compare them. Her Collaboration episode shows the Issue her partner wrote about the dashboard.

### Week 13: The Conversation

In her 4-minute oral reflection with the instructor, Elif discusses two CLOs:

**CLO 3 (Guide AI tools to support a work goal):**

> "I learned that AI does exactly what you say, not what you mean. In Week 2 I said 'help me study better' and got tips. By Week 10 I said '8 specific requirements' and got a real tool. The skill is knowing what to say."

**CLO 4 (Evaluate AI-generated text):**

> "AI makes mistakes I would not expect. In Week 6 the formula was wrong for February. In Week 5 the alt text said 'an image.' I have to check everything, even when it looks right."

### Week 14: Final Presentation

Elif opens her dashboard in the browser. Three pixel art characters are at their desks. She shows the class her real activity log from the past week. 47 tasks completed. She says:

> "This app took me three tries. The first time I described what it should look like. The second time I described how it should behave. The third time I described what it should do for me. That is the difference between a picture, a toy, and a tool."

---

## How Assessment Worked

Elif's grade was based on:

- **Could she describe what she wanted clearly enough?** (Yes, by v3, after two honest failures.)
- **Did she document the process?** (Yes: process tables, Decision Logs, commit messages, Goal Document entries tracking her evolving thinking.)
- **Could she explain her work to someone else?** (Yes: micro-defences, peer check-ins, and the final presentation all showed she could articulate what went right and wrong.)
- **Was the final artifact impressive?** (This was not a grading criterion. But yes, it was.)

The language level was B1. The project ambition had no limit.

---

## The Files

Open these in your browser to see exactly what Elif got at each stage:

- [v1.html](v1.html) -- The chess timer. Buttons and animations, no real function.
- [v2.html](v2.html) -- The screensaver. Impressive simulation, no real data.
- [v3.html](pixel-agent-dashboard.html) -- The real tool. Tracks actual work, saves everything.

Each version took about 10 minutes for AI to build. The time was not spent building. It was spent thinking about what to ask for.
