"""Draw red rings and arrows on the GitHub screen captures for pull-requests-projector.html.

    python3 materials/pull-requests-captures/annotate.py

Reads the untouched captures in raw/ and writes the marked copies beside this script.
Coordinates are pixels in the raw image. To move a mark, edit MARKS and run again.
  ring:  (left, top, right, bottom)
  arrow: (tail_x, tail_y, head_x, head_y)
"""
from pathlib import Path
import math
from PIL import Image, ImageDraw

HERE = Path(__file__).resolve().parent
RED = (214, 20, 38, 255)
SS = 4          # draw at 4x, then shrink, so the edges are smooth
WIDTH = 5       # line width in image pixels

MARKS = {
    "branch-menu.png": {"rings": [(11, 81, 129, 125), (24, 266, 328, 334)], "arrows": [(450, 308, 336, 308)]},
    "pr1-open.png": {"rings": [(11, 59, 103, 101), (361, 61, 555, 97)], "arrows": []},
    "pr1-merged.png": {"rings": [(11, 58, 119, 100)], "arrows": []},
    "fork-button.png": {"rings": [(995, 19, 1099, 63)], "arrows": [(1047, 132, 1047, 70)]},
    "fork-page.png": {"rings": [(9, 39, 307, 67)], "arrows": [(430, 53, 314, 53)]},
    "pr-form.png": {"rings": [(57, 81, 377, 123), (498, 81, 807, 123)], "arrows": []},
    "pr2-open.png": {"rings": [(448, 111, 609, 153)], "arrows": [(730, 132, 616, 132)]},
    "diff.png": {"rings": [(8, 141, 912, 199)], "arrows": []},
    "review-box.png": {"rings": [(84, 417, 464, 563), (536, 582, 711, 628)], "arrows": [(845, 605, 718, 605)]},
    "thread-merge.png": {"rings": [(71, 577, 264, 625)], "arrows": [(4, 601, 65, 601)]},
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


for name, marks in MARKS.items():
    im = Image.open(HERE / "raw" / name).convert("RGBA")
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
