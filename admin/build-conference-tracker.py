"""Build the GEAP 103 assessment tracker template (no student data), framework v7, Option 1.

Option 1 (adopted 2026-10-04, reviews/grading-validity-2026-10-04.md): the agreed weights
40/25/15/20 stay; levels 3 and 4 count when shown twice, at least once without AI (one showing
without AI is enough for levels 1 and 2); every outcome must
reach a confirmed level 2 to pass; the Decision Log and final package can't score above the
band of the student's confirmed levels for the outcomes they show.

Run from the repository root:
    python3 admin/build-conference-tracker.py
Then recalculate with LibreOffice before opening in a previewer.
The filled copy holds names and grades: keep it in private/ (gitignored), never in admin/ or materials/.
"""
import math
from datetime import date
from pathlib import Path

from openpyxl import Workbook
from openpyxl.comments import Comment
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation

OUT = Path(__file__).resolve().parent / "conference-tracker-template.xlsx"
ROSTER_ROWS = 35          # Roster!A2:A36
LOG_ROWS = 600            # Log entry rows; the course outcomes, header, and example row sit above them
CAL_ROWS = 40

F = "Arial"
BOLD = Font(name=F, bold=True)
BODY = Font(name=F)
TITLE = Font(name=F, bold=True, size=14, color="800020")
EXAMPLE = Font(name=F, italic=True, color="7F7F7F")
INPUT = PatternFill("solid", fgColor="FFF7CC")      # light yellow: cells to fill in
HEAD = PatternFill("solid", fgColor="F4EFF0")
WRAP = Alignment(wrap_text=True, vertical="top")

CLOS = [(1, "Files and versions"), (2, "Troubleshoot"), (3, "Guide AI"), (4, "Evaluate AI"),
        (5, "Communicate"), (6, "Produce products"), (7, "Collaborate")]
CONF_CLOS = [1, 2, 5, 6, 7]                      # outcomes in the conference record
SOURCES = ["Conference", "Writing", "Decision Log", "Package", "Portfolio"]
UNMEDIATED = ["Conference", "Writing"]
LEVELS = [
    (0, "Hasn't shown it yet.", 0, 49),
    (1, "Tries, but there's little to show.", 40, 49),
    (2, "Does part of it, or gets there only with prompting.", 60, 69),
    (3, "Does it on their own, but the explanation has gaps.", 77, 84),
    (4, "Does it on their own and explains what they did and why.", 92, 100),
]
WEIGHTS = [("Conference record", 40), ("Decision Log", 25), ("In-class writing", 15), ("Final package", 20)]

wb = Workbook()

# ---------------------------------------------------------------- How to use
how = wb.active
how.title = "How to use"
rows = [
    ("GEAP 103 assessment tracker (framework v7)", TITLE),
    ("Template with no student data. Save your filled copy in your own Humber OneDrive, "
     "not in a shared or public folder. It will hold names and grades.", BODY),
    ("", BODY),
    ("Cells to fill in are light yellow.", BOLD),
    ("1. Roster: type each student's name once.", BODY),
    ("2. Log: one row per piece of evidence. Pick the student and the source (Conference, Writing, Decision Log, "
     "Package, Portfolio), then up to three outcomes with a level for each. In conferences, type Y under R, T, or P when "
     "the student shows a required check, and under Final for the final conference.", BODY),
    ("3. Summary: fills itself. It shows each student's confirmed level for all seven outcomes, the required checks, "
     "whether the pass gate is met, the conference-record percentage, and the caps on the Decision Log and package.", BODY),
    ("4. Grades: enter the Decision Log mark, the three in-class writing marks, and the final package mark. "
     "Enter 0 for a writing task a student missed and didn't make up; leave it blank if it hasn't run yet. "
     "The sheet applies the caps, the weights, and the pass gate.", BODY),
    ("5. Calibration: when two teachers watch the same conference, each enters a level; the sheet shows whether they match.", BODY),
    ("The course learning outcomes are listed at the top of the Log. The grey row under the Log headings is an example. "
     "It isn't counted, because 'Example student' isn't on the roster.", BODY),
    ("", BODY),
    ("Confirmed level: a level counts when the student has shown it twice, at least once without AI (a conference or "
     "in-class writing). AI-assisted evidence (log, package, portfolio) can be the second occasion but can't lift an "
     "outcome above what the student shows without AI. One showing without AI is enough for levels 1 and 2; a 3 or 4 shown "
     "only once counts one level lower.", BODY),
    ("Pass gate: every one of the seven outcomes must reach a confirmed level 2. If not, the course grade is the "
     "weighted total or 49, whichever is lower.", BODY),
    ("Caps: the final package can't score above the band of the confirmed level for outcome 6; the Decision Log can't "
     "score above the band of the lower of outcomes 3 and 4.", BODY),
    ("Required checks:  R = got back an earlier version  ·  T = solved a technical problem or described it clearly "
     "enough to get help  ·  P = changed a classmate's work, got a comment, replied.", BODY),
    ("", BODY),
    ("Settings", BOLD),
]
for i, (text, font) in enumerate(rows, start=1):
    c = how.cell(row=i, column=1, value=text)
    c.font, c.alignment = font, WRAP

r = len(rows) + 1
how.cell(row=r, column=1, value="Allow one outcome at level 1 if every other outcome is at 3 or higher?").font = BODY
tol = how.cell(row=r, column=3, value="No")
tol.font, tol.fill = BODY, INPUT
tol.comment = Comment("Not decided. 'No' is the strict pass floor. 'Yes' lets a student pass with one outcome at "
                      "level 1 when all six others are at 3 or 4.", "GEAP 103")
TOL = f"'How to use'!$C${r}"
how.merge_cells(start_row=r, start_column=1, end_row=r, end_column=2)
dv_tol = DataValidation(type="list", formula1='"No,Yes"', allow_blank=False)
how.add_data_validation(dv_tol)
dv_tol.add(f"C{r}")

r += 2
how.cell(row=r, column=1, value="Weights (agreed)").font = BOLD
WEIGHT_CELLS = {}
for name, w in WEIGHTS:
    r += 1
    how.cell(row=r, column=1, value=name).font = BODY
    how.merge_cells(start_row=r, start_column=1, end_row=r, end_column=2)
    c = how.cell(row=r, column=3, value=w / 100)
    c.font, c.number_format = BODY, "0%"
    WEIGHT_CELLS[name] = f"'How to use'!$C${r}"

r += 2
lv_head = r
for j, h in enumerate(["Level", "Meaning", "Percent (PROPOSED)", "Band top (cap)"], start=1):
    c = how.cell(row=lv_head, column=j, value=h)
    c.font, c.fill = BOLD, HEAD
for k, (lvl, meaning, pct, top) in enumerate(LEVELS, start=1):
    rr = lv_head + k
    how.cell(row=rr, column=1, value=lvl).font = BODY
    how.cell(row=rr, column=1).alignment = Alignment(horizontal="left")
    how.cell(row=rr, column=2, value=meaning).font = BODY
    pc = how.cell(row=rr, column=3, value=pct)
    pc.font, pc.fill = BODY, INPUT
    how.cell(row=rr, column=4, value=top).font = BODY
LV_FIRST, LV_LAST = lv_head + 1, lv_head + len(LEVELS)
CONV = f"'How to use'!$C${LV_FIRST}:$C${LV_LAST}"
BANDTOP = f"'How to use'!$D${LV_FIRST}:$D${LV_LAST}"
how.cell(row=lv_head, column=3).comment = Comment(
    "Proposed, not agreed. Each level sits inside the framework v6 band of the same meaning: "
    "Excellent 85-100, Proficient 70-84, Developing 50-69, Insufficient 0-49. Change these cells "
    "and every conference-record percentage updates.", "GEAP 103")
how.cell(row=lv_head, column=4).comment = Comment(
    "Top of the v6 band for each level. A capped part can't score above this.", "GEAP 103")

how.column_dimensions["A"].width = 16
how.column_dimensions["B"].width = 52
how.column_dimensions["C"].width = 23
how.column_dimensions["D"].width = 16
for rr in range(1, len(rows) + 1):
    how.merge_cells(start_row=rr, start_column=1, end_row=rr, end_column=4)
    n = len(str(how.cell(row=rr, column=1).value or ""))
    how.row_dimensions[rr].height = 15 * max(1, math.ceil(n / 85)) + 3
how.row_dimensions[1].height = 22
how.page_setup.orientation = "portrait"
how.sheet_properties.pageSetUpPr.fitToPage = True
how.page_setup.fitToWidth, how.page_setup.fitToHeight = 1, 0

# -------------------------------------------------------------------- Roster
roster = wb.create_sheet("Roster")
roster["A1"], roster["A1"].font, roster["A1"].fill = "Student", BOLD, HEAD
for rr in range(2, 2 + ROSTER_ROWS):
    roster.cell(row=rr, column=1).fill = INPUT
roster.column_dimensions["A"].width = 32
roster.freeze_panes = "A2"
ROSTER_RANGE = f"Roster!$A$2:$A${1 + ROSTER_ROWS}"

# ----------------------------------------------------------------------- Log
log = wb.create_sheet("Log")
# Course learning outcomes at the top (titles from CLOs.md), then the log table.
CLO_TITLES = [
    (1, "Manage digital files and project versions"),
    (2, "Troubleshoot routine technical problems"),
    (3, "Formulate clear requests to guide AI tools"),
    (4, "Evaluate AI-generated text"),
    (5, "Communicate about technical work and decisions"),
    (6, "Produce digital products"),
    (7, "Collaborate with peers on digital projects"),
]
log.cell(row=1, column=1, value="Course learning outcomes").font = BOLD
for k, (n, title) in enumerate(CLO_TITLES, start=2):
    a = log.cell(row=k, column=1, value=n)
    a.font, a.alignment = BOLD, Alignment(horizontal="left")
    log.cell(row=k, column=2, value=title).font = BODY
    log.merge_cells(start_row=k, start_column=2, end_row=k, end_column=9)
HEAD_ROW = len(CLO_TITLES) + 3          # one blank row after the outcomes
EX_ROW, FIRST = HEAD_ROW + 1, HEAD_ROW + 2
LOG_COLS = ["Date", "Student", "Source", "Outcome A", "Level A", "Outcome B", "Level B", "Outcome C", "Level C",
            "R", "T", "P", "Final", "Observer", "What they showed", "Next question"]
widths = [12, 24, 13, 10, 8, 10, 8, 10, 8, 8, 8, 8, 7, 10, 46, 34]
for j, (h, w) in enumerate(zip(LOG_COLS, widths), start=1):
    c = log.cell(row=HEAD_ROW, column=j, value=h)
    c.font, c.fill = BOLD, HEAD
    log.column_dimensions[c.column_letter].width = w
example = [date(2026, 10, 5), "Example student", "Conference", 1, 3, 5, 2, 4, 2, "Y", None, None, None, "BR",
           "Restored Monday's version of club-message.md; unsure how to confirm it was the right one; "
           "said what they asked the agent but not why they kept its version",
           "Ask how they'd check which version is newer"]
for j, v in enumerate(example, start=1):
    log.cell(row=EX_ROW, column=j, value=v).font = EXAMPLE
log[f"A{EX_ROW}"].number_format = "yyyy-mm-dd"
LAST = FIRST + LOG_ROWS - 1
for rr in range(FIRST, LAST + 1):
    for j in range(1, len(LOG_COLS) + 1):
        log.cell(row=rr, column=j).fill = INPUT
    log.cell(row=rr, column=1).number_format = "yyyy-mm-dd"
log.freeze_panes = f"D{HEAD_ROW + 1}"

def add_list(ws, formula, ref, prompt, warn=True):
    dv = DataValidation(type="list", formula1=formula, allow_blank=True,
                        errorStyle="warning" if warn else "stop", showErrorMessage=True)
    dv.error, dv.errorTitle = prompt, "Check this entry"
    ws.add_data_validation(dv)
    for part in ref.split():
        dv.add(part)


add_list(log, f"={ROSTER_RANGE}", f"B{FIRST}:B{LAST}", "Pick a name from the Roster sheet.")
add_list(log, '"' + ",".join(SOURCES) + '"', f"C{FIRST}:C{LAST}", "Pick a source from the list.")
add_list(log, '"1,2,3,4,5,6,7"', f"D{FIRST}:D{LAST} F{FIRST}:F{LAST} H{FIRST}:H{LAST}", "Outcomes run from 1 to 7.")
add_list(log, '"0,1,2,3,4"', f"E{FIRST}:E{LAST} G{FIRST}:G{LAST} I{FIRST}:I{LAST}", "Levels run from 0 to 4.")
add_list(log, '"Y"', f"J{FIRST}:M{LAST}", "Type Y, or leave it blank.")

L = lambda col: f"Log!${col}${FIRST}:${col}${LAST}"
STU, SRC, OA, LA, OB, LB, OC, LC = L("B"), L("C"), L("D"), L("E"), L("F"), L("G"), L("H"), L("I")
SLOTS = ((OA, LA), (OB, LB), (OC, LC))

# ------------------------------------------------- Confirm (helper, hidden)
conf = wb.create_sheet("Confirm")
conf["A1"], conf["A1"].font = "Student", BOLD
CONF_COL = {}
for k, (n, _) in enumerate(CLOS):
    base = 2 + 6 * k
    for j, h in enumerate([f"U{n}", f"n1_{n}", f"n2_{n}", f"n3_{n}", f"n4_{n}", f"CLO{n}"]):
        conf.cell(row=1, column=base + j, value=h).font = BOLD
    CONF_COL[n] = base
for i in range(ROSTER_ROWS):
    rr = 2 + i
    conf.cell(row=rr, column=1, value=f'=IF(Roster!A{rr}="","",Roster!A{rr})')
    for n, base in CONF_COL.items():
        u, c1, c2, c3, c4, cc = (get_column_letter(base + j) for j in range(6))
        maxifs = ",".join(
            f"_xlfn.MAXIFS({lv},{STU},$A{rr},{oc},{n},{SRC},\"{s}\")"
            for (oc, lv) in SLOTS for s in UNMEDIATED)
        conf[f"{u}{rr}"] = f'=IF($A{rr}="","",MAX({maxifs}))'
        for lvl, col in zip((1, 2, 3, 4), (c1, c2, c3, c4)):
            cnt = "+".join(f'COUNTIFS({STU},$A{rr},{oc},{n},{lv},">={lvl}")' for oc, lv in SLOTS)
            conf[f"{col}{rr}"] = f'=IF($A{rr}="","",{cnt})'
        rule = (f"IF(AND({u}{rr}>=4,{c4}{rr}>=2),4,IF(AND({u}{rr}>=3,{c3}{rr}>=2),3,"
                f"IF(AND({u}{rr}>=2,{c2}{rr}>=2),2,IF(AND({u}{rr}>=1,{c1}{rr}>=2),1,0))))")
        single = f"IF({u}{rr}<=2,{u}{rr},{u}{rr}-1)"   # one showing counts in full up to level 2
        conf[f"{cc}{rr}"] = f'=IF($A{rr}="","",MAX({single},{rule}))'
conf.sheet_state = "hidden"

# ------------------------------------------------------------------- Summary
summ = wb.create_sheet("Summary")
heads = (["Student", "Conferences"] + [f"{n} {name}" for n, name in CLOS]
         + ["R", "T", "P", "Final done", "Pass gate", "Conference record %", "Package cap", "Decision Log cap"])
for j, h in enumerate(heads, start=1):
    c = summ.cell(row=1, column=j, value=h)
    c.font, c.fill, c.alignment = BOLD, HEAD, Alignment(wrap_text=True, vertical="bottom")
summ.row_dimensions[1].height = 32
COL = {h: get_column_letter(j) for j, h in enumerate(heads, start=1)}
clo_col = {n: get_column_letter(3 + k) for k, (n, _) in enumerate(CLOS)}
for i in range(ROSTER_ROWS):
    rr = 2 + i
    summ[f"A{rr}"] = f'=IF(Roster!A{rr}="","",Roster!A{rr})'
    summ[f"B{rr}"] = f'=IF($A{rr}="","",COUNTIFS({STU},$A{rr},{SRC},"Conference"))'
    for n in clo_col:
        summ[f"{clo_col[n]}{rr}"] = f"=Confirm!{get_column_letter(CONF_COL[n] + 5)}{rr}"
    for k, col_letter in enumerate(["J", "K", "L", "M"]):
        tgt = get_column_letter(10 + k)
        summ[f"{tgt}{rr}"] = (f'=IF($A{rr}="","",IF(COUNTIFS({STU},$A{rr},{L(col_letter)},"Y")>0,"Yes","No"))')
    rng = f"C{rr}:I{rr}"
    summ[f"{COL['Pass gate']}{rr}"] = (
        f'=IF($A{rr}="","",IF(COUNTIF({rng},">=2")=7,"Met",'
        f'IF(AND({TOL}="Yes",COUNTIF({rng},">=3")=6,MIN({rng})=1),"Met (tolerance)","Not yet")))')
    avg = "+".join(f"INDEX({CONV},{clo_col[n]}{rr}+1)" for n in CONF_CLOS)
    summ[f"{COL['Conference record %']}{rr}"] = f'=IF($A{rr}="","",({avg})/{len(CONF_CLOS)})'
    summ[f"{COL['Package cap']}{rr}"] = f'=IF($A{rr}="","",INDEX({BANDTOP},{clo_col[6]}{rr}+1))'
    summ[f"{COL['Decision Log cap']}{rr}"] = (
        f'=IF($A{rr}="","",INDEX({BANDTOP},MIN({clo_col[3]}{rr},{clo_col[4]}{rr})+1))')
    summ[f"{COL['Conference record %']}{rr}"].number_format = "0"
    for j in range(1, len(heads) + 1):
        summ.cell(row=rr, column=j).font = BODY
summ.column_dimensions["A"].width = 24
for j in range(2, len(heads) + 1):
    summ.column_dimensions[get_column_letter(j)].width = 11
summ.freeze_panes = "B2"

# -------------------------------------------------------------------- Grades
gr = wb.create_sheet("Grades")
gheads = ["Student", "Conference record %", "Decision Log mark", "Decision Log counted",
          "Writing 1", "Writing 2", "Writing 3", "Writing counted",
          "Final package mark", "Final package counted", "Weighted total", "Pass gate", "Course grade"]
for j, h in enumerate(gheads, start=1):
    c = gr.cell(row=1, column=j, value=h)
    c.font, c.fill, c.alignment = BOLD, HEAD, Alignment(wrap_text=True, vertical="bottom")
gr.row_dimensions[1].height = 32
S = lambda h, rr: f"Summary!{COL[h]}{rr}"
for i in range(ROSTER_ROWS):
    rr = 2 + i
    gr[f"A{rr}"] = f'=IF(Roster!A{rr}="","",Roster!A{rr})'
    gr[f"B{rr}"] = f'=IF($A{rr}="","",{S("Conference record %", rr)})'
    gr[f"D{rr}"] = f'=IF(OR($A{rr}="",C{rr}=""),"",MIN(C{rr},{S("Decision Log cap", rr)}))'
    gr[f"H{rr}"] = (f'=IF(OR($A{rr}="",COUNT(E{rr}:G{rr})=0),"",IF(COUNT(E{rr}:G{rr})=1,MAX(E{rr}:G{rr}),'
                   f'(LARGE(E{rr}:G{rr},1)+LARGE(E{rr}:G{rr},2))/2))')
    gr[f"J{rr}"] = f'=IF(OR($A{rr}="",I{rr}=""),"",MIN(I{rr},{S("Package cap", rr)}))'
    w = WEIGHT_CELLS
    gr[f"K{rr}"] = (f'=IF(OR($A{rr}="",COUNT(B{rr},D{rr},H{rr},J{rr})<4),"",'
                   f'{w["Conference record"]}*B{rr}+{w["Decision Log"]}*D{rr}+{w["In-class writing"]}*H{rr}'
                   f'+{w["Final package"]}*J{rr})')
    gr[f"L{rr}"] = f'=IF($A{rr}="","",{S("Pass gate", rr)})'
    gr[f"M{rr}"] = (f'=IF(OR($A{rr}="",K{rr}=""),"",IF(LEFT(L{rr},3)="Met",ROUND(K{rr},0),'
                   f'MIN(ROUND(K{rr},0),49)))')
    for col in "CEFGI":
        gr[f"{col}{rr}"].fill = INPUT
    for col in "BDHJK":
        gr[f"{col}{rr}"].number_format = "0"
    for j in range(1, len(gheads) + 1):
        gr.cell(row=rr, column=j).font = BODY
gr.column_dimensions["A"].width = 24
for j in range(2, len(gheads) + 1):
    gr.column_dimensions[get_column_letter(j)].width = 12
gr.freeze_panes = "B2"

# --------------------------------------------------------------- Calibration
cal = wb.create_sheet("Calibration")
cheads = ["Date", "Student initials", "Outcome", "Observer 1", "Observer 1 level",
          "Observer 2", "Observer 2 level", "Match?"]
for j, h in enumerate(cheads, start=1):
    c = cal.cell(row=1, column=j, value=h)
    c.font, c.fill = BOLD, HEAD
    cal.column_dimensions[c.column_letter].width = 16
for rr in range(2, 2 + CAL_ROWS):
    for j in range(1, 8):
        cal.cell(row=rr, column=j).fill = INPUT
    cal.cell(row=rr, column=1).number_format = "yyyy-mm-dd"
    cal.cell(row=rr, column=8,
             value=f'=IF(OR(E{rr}="",G{rr}=""),"",IF(E{rr}=G{rr},"Same","Differs by "&ABS(E{rr}-G{rr})))').font = BODY
sr = 3 + CAL_ROWS
cal.cell(row=sr, column=1, value="Conferences rated by both").font = BOLD
cal.cell(row=sr, column=5, value=f'=COUNTIFS(E2:E{1+CAL_ROWS},"<>",G2:G{1+CAL_ROWS},"<>")').font = BODY
cal.cell(row=sr + 1, column=1, value="Same level").font = BOLD
cal.cell(row=sr + 1, column=5, value=f'=COUNTIF(H2:H{1+CAL_ROWS},"Same")').font = BODY
cal.cell(row=sr + 2, column=1, value="Within one level").font = BOLD
cal.cell(row=sr + 2, column=5,
         value=f'=COUNTIF(H2:H{1+CAL_ROWS},"Same")+COUNTIF(H2:H{1+CAL_ROWS},"Differs by 1")').font = BODY
add_list(cal, '"1,2,3,4,5,6,7"', f"C2:C{1+CAL_ROWS}", "Outcomes run from 1 to 7.")
add_list(cal, '"0,1,2,3,4"', f"E2:E{1+CAL_ROWS} G2:G{1+CAL_ROWS}", "Levels run from 0 to 4.")
cal.freeze_panes = "A2"

wb.save(OUT)
print("wrote", OUT.name)
