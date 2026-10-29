from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.style import WD_STYLE_TYPE
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

doc = Document('ref_base.docx')
sec = doc.sections[0]
sec.page_width, sec.page_height = Inches(8.5), Inches(11)
for m in ('top_margin','bottom_margin','left_margin','right_margin'):
    setattr(sec, m, Inches(1))

def setfont(style, font='Times New Roman', size=None, bold=None, italic=None, caps=None):
    style.font.name = font
    rpr = style.element.get_or_add_rPr()
    rf = rpr.find(qn('w:rFonts'))
    if rf is None:
        rf = OxmlElement('w:rFonts'); rpr.insert(0, rf)
    for a in ('w:ascii','w:hAnsi','w:cs','w:eastAsia'):
        rf.set(qn(a), font)
    for a in ('w:asciiTheme','w:hAnsiTheme','w:cstheme','w:eastAsiaTheme'):
        if rf.get(qn(a)) is not None: del rf.attrib[qn(a)]
    if size: style.font.size = Pt(size)
    if bold is not None: style.font.bold = bold
    if italic is not None: style.font.italic = italic
    if caps is not None: style.font.all_caps = caps

# body
for nm, after, before, ls, align, indent in [
    ('Normal', 6, 0, 1.08, WD_ALIGN_PARAGRAPH.JUSTIFY, None),
    ('Body Text', 6, 0, 1.08, WD_ALIGN_PARAGRAPH.JUSTIFY, None),
    ('First Paragraph', 6, 0, 1.08, WD_ALIGN_PARAGRAPH.JUSTIFY, None),
    ('Compact', 2, 0, 1.0, WD_ALIGN_PARAGRAPH.LEFT, None),
    ('Block Text', 6, 6, 1.08, WD_ALIGN_PARAGRAPH.JUSTIFY, 0.5),
]:
    st = doc.styles[nm]
    setfont(st, size=11 if nm != 'Compact' else 9)
    pf = st.paragraph_format
    pf.space_after = Pt(after); pf.space_before = Pt(before); pf.line_spacing = ls
    pf.alignment = align
    if indent: pf.left_indent = Inches(indent)

h1 = doc.styles['Heading 1']
setfont(h1, size=12, bold=True, caps=False)
h1.font.color.rgb = RGBColor(0,0,0)
h1.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
h1.paragraph_format.space_before = Pt(16); h1.paragraph_format.space_after = Pt(10)
h1.paragraph_format.keep_with_next = True

h2 = doc.styles['Heading 2']
setfont(h2, size=11.5, bold=True)
h2.font.color.rgb = RGBColor(0,0,0)
h2.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
h2.paragraph_format.space_before = Pt(14); h2.paragraph_format.space_after = Pt(10)
h2.paragraph_format.keep_with_next = True

def mkstyle(name, size=11, bold=False, italic=False, align=None, before=0, after=6,
            indent=None, keep_next=False, line=1.0):
    st = doc.styles.add_style(name, WD_STYLE_TYPE.PARAGRAPH)
    st.base_style = doc.styles['Normal']
    setfont(st, size=size, bold=bold, italic=italic)
    pf = st.paragraph_format
    if align is not None: pf.alignment = align
    pf.space_before = Pt(before); pf.space_after = Pt(after)
    if indent is not None: pf.left_indent = Inches(indent)
    pf.line_spacing = line
    pf.keep_with_next = keep_next
    return st

C = WD_ALIGN_PARAGRAPH.CENTER; L = WD_ALIGN_PARAGRAPH.LEFT
mkstyle('CoverTitle', 20, True, False, C, 110, 10, keep_next=True)
mkstyle('CoverSub', 12, False, True, C, 16, 8)
mkstyle('CoverParty', 12, True, False, C, 6, 6)
mkstyle('CoverDetail', 10, False, False, C, 10, 2)
mkstyle('CoverLegend', 8.5, False, True, C, 34, 4)
mkstyle('TOCTitle', 14, True, False, C, 0, 14, keep_next=True)
mkstyle('TOCEntry', 10, True, False, L, 10, 2, keep_next=True)
mkstyle('TOCEntry2', 9, False, False, L, 0, 6, indent=0.28)
mkstyle('RecitalHeading', 12, True, False, C, 6, 12, keep_next=True)

doc.save('reference.docx')
print('ok')
