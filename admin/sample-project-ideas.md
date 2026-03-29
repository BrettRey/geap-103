# GEAP 103: Sample Project Ideas

**Purpose:** Inspiration for instructors and students. Presented informally in Week 4 and referenced throughout. Students are not limited to this list.

**The ceiling is high.** The language level is B1. The artifact ambition should be genuinely surprising. "Make a budget spreadsheet" is trivial for AI. "Build an app that tracks my spending, flags unusual purchases, and texts me a weekly summary" requires real articulation. Every project on this list would have required hiring a developer six months ago. Now it requires being able to say what you want clearly enough.

**Design principles:**
- The student brings knowledge AI doesn't have (their life, culture, community, domain expertise)
- AI handles all technical execution (code, formatting, data processing, design)
- The articulation gap is where the learning happens: vague descriptions produce generic junk; precise descriptions produce genuinely useful things
- Every project produces a working artifact with a URL that the student would show their family

---

## Working Apps and Interactive Tools

### 1. Neighbourhood Safety + Transit Score App
A web app where you enter any Toronto address and it shows: walk score, nearest TTC stop with real-time arrivals, distance to the nearest grocery store, and a safety rating based on Toronto Police open data. The student defines what "safe" means to them (weighting criteria differently than the default) and writes the explanatory text. **Articulation challenge:** Defining weighted scoring criteria in plain English; specifying what data sources to use and how to combine them; writing user-facing explanations of what the scores mean.

### 2. Apartment Hunter with Automated Alerts
A tool that scrapes Kijiji or Facebook Marketplace rental listings, filters them by the student's criteria (price, transit time to Humber, number of bedrooms, allows cooking), scores each listing against weighted preferences, and emails a daily digest of the best new matches. **Articulation challenge:** Specifying filter criteria precisely enough that the tool doesn't miss good listings or surface bad ones; defining what "best" means across multiple dimensions; writing the scoring logic in plain English.

### 3. Personal Finance App with Spending Predictions
Not a spreadsheet. A web app where you photograph receipts (OCR), it categorizes spending automatically, tracks against a monthly budget, and predicts whether you'll run out of money before the end of the month based on your spending pattern so far. Alerts when a category is trending over budget. **Articulation challenge:** Defining spending categories that match your actual life (not generic ones); specifying the prediction logic ("If I'm spending $15/day on food and there are 12 days left, but I have $120 in my food budget..."); writing alert messages that are actually helpful.

### 4. Custom Study Scheduler with Spaced Repetition
A web app that takes your course schedule, assignment due dates, and exam dates, then generates a personalized study plan using spaced repetition. It tells you what to study today, tracks what you've reviewed, and reschedules topics you're struggling with. Syncs with your phone calendar. **Articulation challenge:** Describing your courses, their difficulty levels, and your study preferences; specifying what "struggling" means (how the app knows to reschedule); defining the balance between courses.

### 5. Multilingual Phrasebook App with Audio
A mobile-friendly web app that teaches someone your first language, with phrases organized by situation (restaurant, transit, emergency, small talk), audio recordings of you pronouncing each phrase, cultural usage notes, and a quiz mode. Not a translation tool — a teaching tool, designed by someone who knows both the language and the cultural context. **Articulation challenge:** Explaining pronunciation and grammar in English; writing usage notes that capture pragmatic nuance ("You only say this to people older than you"); specifying quiz logic and feedback messages.

### 6. Recipe Scaling + Substitution Engine
Not a recipe website. An app where you paste any recipe URL, it extracts the ingredients and steps, scales to any number of servings (handling non-linear scaling: you can't just double the baking powder), suggests substitutions for unavailable ingredients based on what's in your pantry (which you maintain as a list), and generates a shopping list organized by aisle at your specific grocery store. **Articulation challenge:** Specifying substitution rules that account for texture, flavour, and dietary restrictions; describing your pantry and your grocery store's layout; defining what "equivalent" means for different ingredient types.

---

## Games and Interactive Experiences

### 7. Escape Room Game Set in Your Home City
A browser-based escape room with 5+ puzzles, set in a real location from your home country or culture. Players solve puzzles using cultural knowledge, language clues, and logic. Timer, hint system, scoring, and a leaderboard. The setting and puzzles teach the player something about your culture. **Articulation challenge:** Designing puzzle logic with multiple states and conditions; writing atmospheric descriptions; specifying hint progressions that help without giving away the answer; describing win/lose conditions and branching paths.

### 8. "Survive Your First Winter" Simulation Game
An interactive simulation where the player is a newcomer to Canada in October. They have a budget and must make decisions: buy a winter coat or save money? Take the bus or walk? Each decision affects health, money, and comfort scores over 5 months. Based on real prices and real weather data. Educational and funny. **Articulation challenge:** Designing a decision tree with consequences that cascade; specifying how variables interact ("If health drops below 30 and it's January, trigger a hospital visit that costs $X"); writing dialogue and flavour text that is both informative and entertaining.

### 9. Interactive Fiction: A Day in Two Countries
A branching narrative where the reader makes choices that play out a single day simultaneously in two places: the student's home country and Toronto. Same character, parallel timelines, diverging based on choices. Explores what's different and what's the same. Playable in a browser with illustrated scenes. **Articulation challenge:** Writing branching dialogue that sounds natural in both cultural contexts; specifying how choices in one timeline affect the other; describing scenes vividly enough for AI to generate consistent illustrations.

### 10. Multiplayer Quiz Tournament Platform
Not just a quiz. A platform where you create quiz tournaments that multiple people can join via a code (like Kahoot, but yours). You write the questions on any topic, set difficulty tiers, configure tournament brackets, and see live leaderboards. Share the code with friends and family in different countries and play together. **Articulation challenge:** Designing tournament logic (brackets, elimination, tiebreakers); writing questions at calibrated difficulty levels; specifying real-time synchronization requirements; describing the user experience for both the host and the players.

---

## Data Systems and Automations

### 11. Immigration Document Tracker and Deadline Alert System
A web app that tracks all your immigration documents (study permit, work permit, PGWP eligibility, PR application stages), their expiry dates, renewal windows, and required supporting documents. Sends email alerts 90/60/30 days before deadlines. Includes a checklist for each document type based on IRCC requirements. **Articulation challenge:** Specifying the relationship between document types (work permit depends on study permit status); defining alert timing and escalation; writing checklist items that are accurate and actionable; describing conditional logic ("If study permit expires before PGWP application is processed...").

### 12. Course Grade Simulator with "What If" Scenarios
A tool where you enter your course structure (assignments, weights, due dates), your grades so far, and then ask "what if" questions: "What grade do I need on the final to get a B+?" "What happens if I skip Assignment 4?" "If I get 75% on everything remaining, what's my final grade?" Visual dashboard showing scenarios side by side. **Articulation challenge:** Specifying grade calculation rules (weighted averages, dropped lowest scores, participation components); describing scenarios precisely; writing the interpretive text that explains what each scenario means.

### 13. Job Application Tracker with Follow-Up Automation
A system that tracks every job you apply to: company, position, date applied, contact person, status (applied/interviewed/rejected/offered), and next action. Generates follow-up email drafts at configurable intervals (1 week after application, 2 days after interview). Dashboard shows your pipeline. **Articulation challenge:** Defining status transitions and follow-up rules; writing email templates for different situations (follow-up after no response vs. thank-you after interview vs. negotiation after offer); specifying what the dashboard should prioritize.

### 14. Neighbourhood Price Comparison Scraper
A tool that monitors prices for specific items you buy regularly (milk, rice, phone plans, transit passes) across multiple stores and services near you. Updates weekly. Shows you where to buy each item cheapest, with a map. Calculates how much you'd save per month by switching. **Articulation challenge:** Defining which items to track and at which stores; specifying how to handle different sizes and brands ("Compare the per-100g price, not the package price"); writing the summary logic that turns raw data into actionable advice.

---

## Creative and Cultural Projects

### 15. Animated Explainer: A Concept from Your Culture That Doesn't Exist in English
A 2-3 minute animated explainer video (AI-generated visuals + your voiceover) that teaches English speakers a concept from your culture that has no direct English translation. Examples: the Korean concept of 눈치 (nunchi), the Arabic concept of كيف (keif), the Japanese concept of 木漏れ日 (komorebi). The animation shows the concept in action through scenarios. **Articulation challenge:** Explaining an untranslatable concept through examples and scenarios rather than definitions; scripting visual scenes precisely enough for AI animation; speaking clearly for voiceover at a controlled pace.

### 16. Interactive Cultural Calendar with Event Planner
Not a static calendar. A web app that maps your community's cultural events, holidays, and festivals onto the academic year, with: countdown timers, preparation checklists ("for Nowruz you need: ..."), links to local vendors, estimated costs, and a "plan this event" mode that generates shopping lists and task timelines. **Articulation challenge:** Explaining cultural practices to an unfamiliar audience without oversimplifying; specifying the planning logic for each event; writing preparation checklists that are accurate and complete.

### 17. Oral History Archive with Search and Themes
Record 3-5 interviews with elders in your community (in any language). AI transcribes, translates, and indexes them. Build a searchable web archive where visitors can browse by theme (immigration, work, family, food, war, education), listen to audio clips, read translations, and see connections between stories. **Articulation challenge:** Designing the thematic taxonomy; writing interview questions that elicit rich narratives; specifying how the search and theme-linking should work; writing the framing text that contextualizes the archive for visitors.

### 18. "Port" a Classic Game to the Browser
Take a game you grew up playing (a card game, a board game, a schoolyard game that's specific to your culture) and build a playable browser version. AI writes the code; you specify the rules, the UI, and the experience. Include a "How to Play" section that teaches the cultural context. **Articulation challenge:** Translating implicit game rules into explicit, unambiguous specifications; describing spatial layouts and turn sequences; handling edge cases and special rules; writing cultural context that makes a foreign game interesting to a Canadian player.

---

## Professional and Community Impact

### 19. Small Business Operations Dashboard
For a real family business or side hustle: a dashboard that tracks customers/clients, appointments, income, expenses, inventory (if applicable), and generates invoices. Not a website about the business — an actual operational tool the business uses. **Articulation challenge:** Mapping the real workflow of the business into system requirements; specifying invoice formats, tax calculations, and reporting periods; defining what the business owner needs to see first when they open the dashboard.

### 20. Community Needs Survey Platform + Report Generator
Build a survey tool (not Google Forms — a custom one with your questions, your logic, your design), distribute it to your community, and have the system automatically generate a report with charts, findings, and recommendations as responses come in. Real-time dashboard. **Articulation challenge:** Writing survey questions that avoid bias; specifying skip logic and branching; defining how to aggregate and visualize responses; writing the auto-generated report template that turns data into narrative.

### 21. Newcomer Onboarding System for Your Workplace
A training tool for new employees at a workplace you know (restaurant, warehouse, retail, care facility). Interactive modules: "Here's how the cash register works" (with clickable simulation), "Here's what to do if a customer complains" (with branching scenarios), "Here's the safety equipment and when to use it" (with visual guide). Built from your real experience. **Articulation challenge:** Turning tacit workplace knowledge into explicit, teachable steps; writing branching scenarios with realistic dialogue; specifying simulation logic; describing safety procedures with precision.

---

## Assessment Note

These ideas are presented as inspiration, not requirements. Assessment is on the communicative package (articulation + evaluation + documentation + sharing), not on technical sophistication. But the AF v6 explicitly says: "A student who attempts something that genuinely challenged their ability to articulate what they wanted is demonstrating more than a student who describes a trivial goal perfectly. The language is B1; the ambition can be high."

A student who tries to build #11 (immigration document tracker) and only gets the deadline alerts working — with excellent process documentation about why the conditional logic was hard to specify — scores higher than a student who builds a generic portfolio website with no documentation.
