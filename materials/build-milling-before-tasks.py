"""Build the reviewed one-page GEAP 103 milling handout from its Markdown."""
from pathlib import Path
import re
from xml.sax.saxutils import escape

from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph
from pypdf import PdfReader

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
SOURCE = HERE / "milling-before-tasks-2026-09-23.md"
OUTPUT = ROOT / "output/pdf/milling-before-tasks-2026-09-23.pdf"
FONTS = HERE / "day-01/assets"
INK = HexColor("#191919")
ACCENT = HexColor("#800020")
RULE = HexColor("#cbbfc2")

pdfmetrics.registerFont(TTFont("EG", FONTS / "EBGaramond-Regular.ttf"))
pdfmetrics.registerFont(TTFont("EGItalic", FONTS / "EBGaramond-Italic.ttf"))


def paragraph(text, width, size=13, leading=15.5, *, color=INK, italic=False):
    style = ParagraphStyle(
        "handout", fontName="EGItalic" if italic else "EG", fontSize=size,
        leading=leading, textColor=color,
    )
    item = Paragraph(escape(text), style)
    _, height = item.wrap(width, 720)
    return item, height


def put(doc, text, x, top, width, **kwargs):
    item, height = paragraph(text, width, **kwargs)
    item.drawOn(doc, x, top - height)
    return top - height


def build():
    raw = SOURCE.read_text()
    student = raw.split("\n---\n", 1)[0]
    assert not re.search(r"\{(?:>>|\+\+|--|~~)", student), "Resolve review markup first"
    section = student.split("## Questions\n\n")[1].split("## Useful phrases")[0]
    cards = re.findall(
        r"### (\d+)\. ([^\n]+)\n\n(.*?)\n\n\*\*Ask more:\*\* (.*?)(?=\n\n###|\Z)",
        section.strip(), re.S,
    )
    assert [number for number, *_ in cards] == [str(n) for n in range(1, 9)]
    instructions = student.split("## Talk to your classmates\n\n")[1].split("## Questions")[0].strip()
    steps, access = instructions.split("\n\n", 1)
    phrases = student.split("## Useful phrases\n\n")[1].split("## Back together")[0]
    phrases = [line[2:].strip().strip('"') for line in phrases.strip().splitlines()]
    closing = student.split("## Back together\n\n")[1].strip()

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    doc = canvas.Canvas(str(OUTPUT), pagesize=letter, pageCompression=1)
    doc.setTitle("Ready to work with AI? - GEAP 103 speaking warm-up")
    doc.setAuthor("Brett Reynolds")
    doc.setSubject("Eight B1 milling questions before the self-paced tasks")
    left, width = 40, 532
    top = put(doc, "Ready to work with AI?", left, 759, width, size=27, leading=29, color=ACCENT)
    top = put(doc, "GEAP 103  |  September 23, 2026  |  Speaking warm-up", left, top - 5, width, size=11.5, leading=14)
    top -= 11
    for line in steps.splitlines():
        top = put(doc, line, left, top, width, size=12, leading=14.3)
    top = put(doc, access, left, top - 7, width, size=11.4, leading=13.1)
    top -= 13

    gap, pad = 14, 10
    card_width = (width - gap) / 2
    inner = card_width - 2 * pad
    for index in range(0, 8, 2):
        pair = cards[index:index + 2]
        heights = []
        for number, title, question, follow in pair:
            qh = paragraph(question, inner)[1]
            fh = paragraph("Ask more: " + follow.strip(), inner, size=11.8, leading=14.1)[1]
            heights.append(pad + 15 + 6 + qh + 6 + fh + pad)
        row_height = max(heights)
        for column, (number, title, question, follow) in enumerate(pair):
            x = left + column * (card_width + gap)
            doc.setStrokeColor(RULE)
            doc.setLineWidth(.6)
            doc.roundRect(x, top - row_height, card_width, row_height, 4, stroke=1, fill=0)
            y = put(doc, f"{number}. {title}", x + pad, top - pad, inner, size=12, leading=15, color=ACCENT)
            y = put(doc, question, x + pad, y - 6, inner)
            y = put(doc, "Ask more: " + follow.strip(), x + pad, y - 6, inner, size=11.8, leading=14.1)
            assert y >= top - row_height + pad - .01
        top -= row_height + 9

    top = put(doc, "Useful phrases", left, top - 2, width, size=11.8, leading=14, color=ACCENT)
    top -= 3
    for group in (phrases[:3], phrases[3:]):
        phrase_line = "   |   ".join(f'"{phrase}"' for phrase in group)
        top = put(doc, phrase_line, left, top, width, size=11.7, leading=14, italic=True)
    top = put(doc, "Back together: " + closing, left, top - 8, width, size=12, leading=14.3)
    assert top >= 32, f"Content extends below safe margin: {top:.1f}"
    doc.showPage()
    doc.save()

    reader = PdfReader(OUTPUT)
    assert len(reader.pages) == 1
    text = " ".join(reader.pages[0].extract_text().split())
    for number, title, question, follow in cards:
        for expected in (f"{number}. {title}", question, follow.strip()):
            assert " ".join(expected.split()) in text, expected
    for phrase in phrases:
        assert phrase in text, phrase
    assert "Teacher notes" not in text
    assert "passwords, sign-in codes" in text
    assert tuple(float(v) for v in reader.pages[0].mediabox) == (0, 0, 612, 792)
    print(f"Built {OUTPUT}")
    print(f"Verified: one Letter page; eight questions and follow-ups; all phrases; bottom margin {top:.1f} pt.")


if __name__ == "__main__":
    build()
