"""Draw red rings and arrows on the GitHub screen captures for get-it-back-projector.html.

    python3 materials/get-it-back-captures/annotate.py

Reads the untouched captures in raw/ and writes the marked copies beside this script.
Captured 2026-11-20 from the throwaway private repository BrettRey/get-it-back-test
(GitHub dark theme; the forced light theme lost the red and green in the change view).
Coordinates are pixels in the raw image. To move a mark, edit MARKS and run again.
  ring:  (left, top, right, bottom)
  arrow: (tail_x, tail_y, head_x, head_y)
Same drawing code as pull-requests-captures/annotate.py.
"""
from pathlib import Path
import math
from PIL import Image, ImageDraw

HERE = Path(__file__).resolve().parent
RED = (232, 38, 56, 255)   # a little brighter than the light-theme deck, for the dark captures
SS = 4
WIDTH = 5

# output name: (raw source, marks)
MARKS = {
    "file-main-pencil.png": ("file-main.png", {"rings": [(846, 172, 884, 206)], "arrows": []}),
    "file-main-history.png": ("file-main.png", {"rings": [(860, 110, 944, 146)], "arrows": []}),
    "commit-break.png": ("commit-break.png", {"rings": [(18, 186, 942, 214)], "arrows": []}),
    "history-break.png": ("history.png", {"rings": [(68, 219, 1238, 281)], "arrows": []}),
    "history-view-code.png": ("history.png", {"rings": [(76, 288, 224, 318), (1150, 294, 1190, 332)], "arrows": [(1060, 400, 1146, 336)]}),
    "history-story.png": ("history.png", {"rings": [(68, 152, 1238, 346)], "arrows": []}),
    "file-at-commit-copy.png": ("file-at-commit.png", {"rings": [(1086, 173, 1119, 206), (16, 104, 266, 138)], "arrows": [(1102, 300, 1102, 212)]}),
    "branch-menu.png": ("branch-menu.png", {"rings": [(16, 104, 266, 138), (58, 286, 357, 320)], "arrows": []}),
}


def arrow(d, x0, y0, x1, y1):
    w = WIDTH * SS
    ang = math.atan2(y1 - y0, x1 - x0)
    head = 22 * SS
    bx, by = x1 * SS - head * math.cos(ang), y1 * SS - head * math.sin(ang)
    d.line([(x0 * SS, y0 * SS), (bx, by)], fill=RED, width=w)
    half = 11 * SS
    d.polygon([(x1 * SS, y1 * SS),
               (bx + half * math.sin(ang), by - half * math.cos(ang)),
               (bx - half * math.sin(ang), by + half * math.cos(ang))], fill=RED)


for name, (src, marks) in MARKS.items():
    im = Image.open(HERE / "raw" / src).convert("RGBA")
    over = Image.new("RGBA", (im.width * SS, im.height * SS), (0, 0, 0, 0))
    d = ImageDraw.Draw(over)
    for l, t, r, b in marks["rings"]:
        rad = min((b - t) / 2, 16) * SS
        d.rounded_rectangle([l * SS, t * SS, r * SS, b * SS], radius=rad, outline=RED, width=WIDTH * SS)
    for a in marks["arrows"]:
        arrow(d, *a)
    over = over.resize(im.size, Image.LANCZOS)
    Image.alpha_composite(im, over).convert("RGB").save(HERE / name)
    print(name, im.size, len(marks["rings"]), "rings", len(marks["arrows"]), "arrows")
