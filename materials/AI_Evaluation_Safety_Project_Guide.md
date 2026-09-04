# AI Evaluation / Safety Test: Student Project Guide

## The idea

You can make a small test of an AI tool instead of asking AI to make a product for you.

Your question should be narrow:

> How well does **this AI tool** do **this task** for **these users**, under **these conditions**?

A **benchmark** is a set of test cases that you check in the same way. A safety test studies one limited risk, such as invented citations, missed private information, or an accessibility problem. It is not an attempt to make an AI system produce dangerous material.

The AI tool does not need to pass or fail for your project to succeed. You are assessed on the usual course work: stating a clear goal, documenting what happened, checking the output with evidence outside the AI system, explaining your decisions and limits, saving versions, and sharing the result with another person.

## Possible questions

| Focus | Possible project question | What you can use to check |
|---|---|---|
| **Language** | Does the tool translate common college instructions clearly into a language I know? | Original instructions and a proficient speaker |
| **Current local information** | Does the tool answer questions from current Humber webpages correctly? | The official webpages |
| **Citations** | Are the sources it gives real, and do they support its claims? | The original sources |
| **Privacy** | Does the tool remove every identifying detail from invented records? | An answer key made before the test |
| **Accessibility** | Does its image description include the information a user needs? | A checklist and a human reviewer |
| **Consistency** | Does a small change in wording change the answer? | Paired prompts and a clear comparison rule |

You may propose another question. Ask the instructor before testing fairness or demographic differences.

## Build the test

### 1. State the question

Name:

- the tool and model name, if the model name is shown;
- the task;
- the intended user or audience;
- the conditions, including the date and exact instructions; and
- what will count as **meets**, **partly meets**, or **does not meet** the criterion.

### 2. Make the test cases and answer key

Prepare 20–30 cases. Make the correct answer or scoring rule before you run the final test. Use evidence outside the AI system, such as an official source, a calculation, direct observation, or a qualified human reader.

The AI tool being tested cannot mark its own work. A second AI tool may help you notice a problem, but it is not independent proof that the answer is correct.

### 3. Pilot, revise, and lock the method

Try your procedure on 5 pilot cases. Look for unclear prompts, weak answer keys, and scoring rules that are hard to apply. Revise the procedure, then keep the prompt and scoring rule unchanged for the remaining cases. Keep the pilot results separate from the final results.

### 4. Record what happened

Keep the raw output. Use one row per case:

| Case | Prompt or input | Expected answer and source | AI output | Meets / partly / does not meet | Reason |
|---|---|---|---|---|---|
|  |  |  |  |  |  |

Also record the tool, model name if shown, date, exact instructions, and any setting that might change the result. You do not need an API or a special account.

### 5. Report a limited result

Give counts first. A chart may show how many cases met, partly met, or did not meet the criterion. Then show three cases that help the reader understand the result: one success, one partial success, and one failure.

Your conclusion applies only to the task, cases, tool, and conditions you tested. Do not write “this model is accurate” or “this model is safe.” Write what happened in your test and name its limits.

## What to submit

Submit the usual Artifact Package. For this project, the product contains:

1. an evaluation card with the question, task, audience, conditions, model and date, criteria, and sources;
2. the completed test sheet with the raw outputs;
3. one chart; and
4. three explained examples: a success, a partial success, and a failure.

Add the usual Decision Log entries, saved versions, verification notes, and sharing evidence.

Keep these three statements separate:

- **Claim:** what you found in this test.
- **Evidence:** how the cases, answer key, and scoring support the claim.
- **Revision:** what you would change in a stronger next test.

## Safety limits

- Use invented data for privacy and redaction tests. Do not upload names, student numbers, passwords, private documents, workplace records, or recordings without informed permission.
- Do not test malware, weapons, self-harm, sexual exploitation, extremist propaganda, or ways to bypass an AI system's safety rules.
- Do not test medical, legal, or financial advice where a wrong answer could harm someone.
- Stop and tell the instructor if the tool produces disturbing or unexpected harmful content.
- Ask the instructor before a project involving demographic groups, stereotypes, or other sensitive traits.

## Sentence frames

- “I tested whether _____ could _____ for _____.”
- “I expected _____ because _____.”
- “The tool met the criterion in _____ of _____ final cases.”
- “The most important failure was _____.”
- “This result applies only to _____.”
- “A stronger next test would _____.”
