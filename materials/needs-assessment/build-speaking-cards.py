"""Build the reviewed GEAP 103 speaking cards, one per Letter page."""

from collections import Counter
from pathlib import Path
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
FONTS = HERE.parent / "day-01" / "assets"
OUTPUT = HERE / "speaking-cards.pdf"

CARDS = [
    (
        "What do you use your phone or computer for outside class?",
        "Which thing do you do most often?",
        "I use it to…",
    ),
    (
        "How do you like to learn something new?",
        "Can you give an example?",
        "I like to learn by…",
    ),
    (
        "What's something you enjoy doing or know a lot about?",
        "How did you get interested in it?",
        "I enjoy… / I know a lot about…",
    ),
    (
        "What's something you'd like to learn to do this year?",
        "Why would you like to learn that?",
        "I'd like to learn to…",
    ),
    (
        "What's one everyday thing you wish were easier?",
        "Who else might want that to be easier?",
        "I wish it were easier to…",
    ),
    (
        "If you could make something with a computer, what would you like to make?",
        "Who would use it or enjoy it?",
        "I'd like to make… / I'm not sure yet, but I like…",
    ),
]

pdfmetrics.registerFont(TTFont("EBGaramond", FONTS / "EBGaramond-Regular.ttf"))
pdfmetrics.registerFont(TTFont("EBGaramondItalic", FONTS / "EBGaramond-Italic.ttf"))
INK = HexColor("#191919")
MAROON = HexColor("#800020")


def put_paragraph(doc, text, top, size, leading, *, italic=False, color=INK):
    style = ParagraphStyle(
        "card",
        fontName="EBGaramondItalic" if italic else "EBGaramond",
        fontSize=size,
        leading=leading,
        textColor=color,
    )
    paragraph = Paragraph(escape(text), style)
    _, height = paragraph.wrap(504, 700)
    paragraph.drawOn(doc, 54, top - height)
    return top - height


def build():
    doc = canvas.Canvas(str(OUTPUT), pagesize=letter, pageCompression=1)
    doc.setTitle("GEAP 103 speaking cards")
    doc.setAuthor("Brett Reynolds")
    order = list(range(6)) * 4 + [0]
    assert Counter(order) == {0: 5, 1: 4, 2: 4, 3: 4, 4: 4, 5: 4}
    for card_number in order:
        question, follow_up, starter = CARDS[card_number]
        doc.setFillColor(MAROON)
        doc.setFont("EBGaramond", 20)
        doc.drawString(54, 735, "GEAP 103")
        doc.setFillColor(INK)
        doc.setFont("EBGaramond", 16)
        doc.drawRightString(558, 735, f"Question {card_number + 1}")
        question_bottom = put_paragraph(doc, question, 654, 42, 49)
        assert question_bottom >= 430, (question, question_bottom)
        put_paragraph(doc, "Ask more", 388, 18, 22, color=MAROON)
        follow_up_bottom = put_paragraph(doc, follow_up, 353, 27, 33)
        assert follow_up_bottom >= 275
        put_paragraph(doc, "Start", 241, 18, 22, color=MAROON)
        starter_bottom = put_paragraph(doc, starter, 206, 27, 33, italic=True)
        assert starter_bottom >= 120
        put_paragraph(doc, "Ask. Listen. Answer their question.", 86, 17, 21)
        put_paragraph(doc, "Find a new partner. You can pass on a question.", 62, 17, 21)
        doc.showPage()
    doc.save()
    reader = PdfReader(OUTPUT)
    assert len(reader.pages) == 25
    for page, card_number in zip(reader.pages, order):
        text = " ".join(page.extract_text().split())
        for expected in CARDS[card_number]:
            assert " ".join(expected.split()) in text, (card_number, expected)
        assert float(page.mediabox.width) == 612
        assert float(page.mediabox.height) == 792
    print(f"Built {OUTPUT}: 25 Letter pages, six question types; all text verified.")


if __name__ == "__main__":
    build()
