# Day 1 classroom pack

- [Slides](day-01.html): 14 slides with speaker notes. Open in a browser and use the arrow keys. The fonts and screenshot are included in the HTML file.
- [Slide PDF](day-01.pdf): a backup for projection, without speaker notes.
- [One-page reference sheet](day-01-reference.pdf): print one per student, or share the PDF.
- [Practice files](practice-files.zip): unzip before teaching. The text files are invented examples for finding, naming, moving and comparing files.
- [Editable Quarto source](day-01.qmd) and [reference-sheet source](day-01-reference.qmd).

For presenter view with notes, open the hosted slides and press **S**. Locally, run `quarto preview day-01.qmd` from this folder, then press **S**. Share the student slide window with the projector. Slides 4 and 5 each use three clicks to build their diagrams; the PDF shows the completed diagrams.

Before class, open the game and course links on slide 2 and have a file folder ready to demonstrate. If a site is unavailable, the saved game image and this deck provide two things to show. The game image is a screenshot, not a playable replacement. Have the practice files available directly if students cannot open a ZIP file.

The notes follow the [Week 1 lesson plan](../../lesson-plans/week-01.md): 165 minutes including a 15-minute break. They use its folder names and keep the five target computer terms. The reference sheet carries vocabulary and prompts while the projector shows a demonstration. New computer terms have plain explanations; the rest of the student copy is kept short for A2+/low-B1 readers.

## Rebuild

```sh
quarto render day-01.qmd
quarto render day-01-reference.qmd
```

For the slide PDF, open the rendered slides in a browser, add `?print-pdf` to the end of the URL, and print to PDF after the slides have loaded. Use landscape pages and disable browser headers and footers. The supplied PDF has already been exported.

## Credits

Course and teaching text: Brett Reynolds, with LLM assistance, under the course's CC BY 4.0 licence.

The Scoop Sort screenshot belongs to Freja Games. It is reproduced as a credited classroom example and is excluded from the course's CC BY licence. Source: https://freja-games.itch.io/scoop-sort . The maker's description is linked in slide 2's notes.

Folder, document, laptop and cloud icons come from [Microsoft Fluent UI System Icons](https://github.com/microsoft/fluentui-system-icons), under the MIT licence included in `assets/fluent-icons-LICENSE.txt`. Their colours are adapted for the slides.

EB Garamond and Inconsolata use the SIL Open Font License; licence texts are in `assets/`. `house-theme.scss` is a local snapshot of Brett's shared Quarto theme. `day-01.scss` adapts it for projection, using maroon headings and larger text; `fonts.css` loads the bundled fonts.
