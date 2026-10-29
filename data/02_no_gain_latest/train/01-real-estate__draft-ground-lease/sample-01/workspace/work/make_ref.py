from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn

doc = Document()
sec = doc.sections[0]
sec.page_width = Inches(8.5); sec.page_height = Inches(11)
sec.left_margin = Inches(1.0); sec.right_margin = Inches(1.0)
sec.top_margin = Inches(0.9); sec.bottom_margin = Inches(0.9)

base = doc.styles['Normal']
base.font.name = 'Times New Roman'; base.font.size = Pt(11)
base.element.rPr.rFonts.set(qn('w:eastAsia'), 'Times New Roman')
pf = base.paragraph_format
pf.space_after = Pt(7); pf.space_before = Pt(0); pf.line_spacing = 1.06
pf.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY

def style(name, size=11, bold=False, italic=False, align=WD_ALIGN_PARAGRAPH.JUSTIFY,
          before=0, after=7, base_on='Normal', keep=False, color=None):
    try:
        s = doc.styles[name]
    except KeyError:
        from docx.enum.style import WD_STYLE_TYPE
        s = doc.styles.add_style(name, WD_STYLE_TYPE.PARAGRAPH)
    try:
        s.base_style = doc.styles[base_on]
    except Exception:
        pass
    s.font.name='Times New Roman'; s.font.size=Pt(size); s.font.bold=bold; s.font.italic=italic
    if color: s.font.color.rgb=color
    r = s.element.get_or_add_rPr(); rf = r.get_or_add_rFonts()
    rf.set(qn('w:ascii'),'Times New Roman'); rf.set(qn('w:hAnsi'),'Times New Roman')
    s.paragraph_format.alignment = align
    s.paragraph_format.space_before = Pt(before); s.paragraph_format.space_after = Pt(after)
    s.paragraph_format.keep_with_next = keep
    return s

style('Heading 1', 15, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, before=0, after=12, keep=True)
style('Heading 2', 11.5, bold=True, align=WD_ALIGN_PARAGRAPH.LEFT, before=15, after=7, keep=True)
style('Heading 3', 11, bold=True, align=WD_ALIGN_PARAGRAPH.LEFT, before=11, after=4, keep=True)
style('Heading 4', 11, bold=True, italic=True, align=WD_ALIGN_PARAGRAPH.LEFT, before=9, after=4, keep=True)
style('Title', 18, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, before=0, after=10)
style('Body Text', 11, after=7)
style('First Paragraph', 11, after=7)
style('Compact', 11, after=2, align=WD_ALIGN_PARAGRAPH.LEFT)
style('Table Caption', 9.5, italic=True, align=WD_ALIGN_PARAGRAPH.LEFT, before=6, after=3, keep=True)
doc.save('work/reference.docx')
print("ref ok")
