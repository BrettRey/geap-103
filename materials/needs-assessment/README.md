# GEAP 103 needs assessment and speaking cards

## Printing the cards

Print **one copy of all 25 pages** of [speaking-cards.pdf](speaking-cards.pdf), single-sided on Letter paper. Give one page to each student. There are six different questions: five copies of Question 1 and four copies of each other question.

Allow about 20 minutes. Students read their card, think of an answer, and ask several classmates the same question. Both partners ask and answer. With 25 students, one group can have three people. Students can stay seated while partners visit, change cards, or pass on a question.

Finish with “What did you have in common?”, “What was different?”, and “Did you hear an idea you'd like to explore?” Don't collect names or record conversations. A match isn't required.

## Online needs assessment

The 11-question form is hosted in Humber Microsoft Forms. [The form questions and settings](needs-assessment-form.md) are stored here for reuse. **Responses are closed pending Humber's applicable collection notice.**

Student response link, for Blackboard after collection is opened:

[Open the needs assessment](https://forms.cloud.microsoft/r/QCX2ZhE2Gt).

Settings checked: Humber-only sign-in, recorded names, one response per person, all questions optional, no shuffling, and a maximum of three learning priorities. The student preview discloses name and email collection. No co-authors or results-sharing links were added.

Add the applicable collection notice to the introduction before turning on **Settings → Accept responses**. Keep identifying responses and exports in Humber systems, out of the public repository and external LLMs. If sign-in fails, offer a private conversation instead of opening the form to public named responses.

The printable source is [build-speaking-cards.py](build-speaking-cards.py). To rebuild from the repository root:

```sh
uv run --with reportlab --with pypdf python materials/needs-assessment/build-speaking-cards.py
```
