from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.style import WD_STYLE_TYPE
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

doc = Document()
sec = doc.sections[0]
sec.page_width, sec.page_height = Inches(8.5), Inches(11)
for m in ('top_margin','bottom_margin','left_margin','right_margin'):
    setattr(sec, m, Inches(1))

def mkstyle(name, size=11, bold=False, italic=False, align=None, before=0, after=6,
            indent=None, allcaps=False, spacing=None, keep_next=False, font='Times New Roman',
            base='Normal'):
    st = doc.styles.add_style(name, WD_STYLE_TYPE.PARAGRAPH)
    st.base_style = doc.styles[base]
    st.font.name = font
    st.font.size = Pt(size)
    st.font.bold = bold
    st.font.italic = italic
    st.font.all_caps = allcaps
    rpr = st.element.get_or_add_rPr()
    rf = rpr.find(qn('w:rFonts'))
    if rf is None:
        rf = OxmlElement('w:rFonts'); rpr.append(rf)
    for a in ('w:ascii','w:hAnsi','w:cs','w:eastAsia'):
        rf.set(qn(a), font)
    pf = st.paragraph_format
    if align is not None: pf.alignment = align
    pf.space_before = Pt(before); pf.space_after = Pt(after)
    if indent is not None: pf.left_indent = Inches(indent)
    pf.line_spacing = spacing if spacing else 1.0
    pf.keep_with_next = keep_next
    return st

# Normal
n = doc.styles['Normal']
n.font.name = 'Times New Roman'; n.font.size = Pt(11)
rpr = n.element.get_or_add_rPr()
rf = rpr.find(qn('w:rFonts'))
if rf is None:
    rf = OxmlElement('w:rFonts'); rpr.append(rf)
for a in ('w:ascii','w:hAnsi','w:cs','w:eastAsia'):
    rf.set(qn(a), 'Times New Roman')
n.paragraph_format.space_after = Pt(6)
n.paragraph_format.line_spacing = 1.08
n.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY

C = WD_ALIGN_PARAGRAPH.CENTER
L = WD_ALIGN_PARAGRAPH.LEFT

mkstyle('CoverTitle', 22, True, False, C, 150, 10, keep_next=True)
mkstyle('CoverSub', 12, False, True, C, 14, 8)
mkstyle('CoverParty', 12.5, True, False, C, 6, 6)
mkstyle('CoverDetail', 10, False, False, C, 10, 2)
mkstyle('CoverLegend', 8.5, False, True, C, 60, 4)
mkstyle('TOCTitle', 14, True, False, C, 0, 14, keep_next=True)
mkstyle('TOCEntry', 10, True, False, L, 10, 2, keep_next=True)
mkstyle('TOCEntry2', 9, False, False, L, 0, 6, indent=0.28)
mkstyle('RecitalHeading', 12, True, False, C, 6, 12, keep_next=True)
mkstyle('PageBreak', 2, False, False, L, 0, 0)

h1 = doc.styles['Heading 1']
h1.font.name = 'Times New Roman'; h1.font.size = Pt(12); h1.font.bold = True
h1.font.color.rgb = RGBColor(0,0,0)
h1.paragraph_format.alignment = C
h1.paragraph_format.space_before = Pt(16); h1.paragraph_format.space_after = Pt(10)
h1.paragraph_format.keep_with_next = True
h2 = doc.styles['Heading 2']
h2.font.name = 'Times New Roman'; h2.font.size = Pt(11.5); h2.font.bold = True
h2.font.color.rgb = RGBColor(0,0,0)
h2.paragraph_format.alignment = C
h2.paragraph_format.space_before = Pt(14); h2.paragraph_format.space_after = Pt(10)
h2.paragraph_format.keep_with_next = True

doc.save('reference.docx')
print('reference.docx written')
