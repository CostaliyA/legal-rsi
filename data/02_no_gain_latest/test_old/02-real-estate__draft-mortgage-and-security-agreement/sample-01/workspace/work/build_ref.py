import docx
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.style import WD_STYLE_TYPE
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

d = docx.Document('work/ref_base.docx')
FONT = 'Times New Roman'

def set_font(style, size=None, bold=None, italic=None, color=RGBColor(0,0,0), caps=None):
    f = style.font
    f.name = FONT
    rpr = style.element.get_or_add_rPr()
    rfonts = rpr.find(qn('w:rFonts'))
    if rfonts is None:
        rfonts = OxmlElement('w:rFonts'); rpr.append(rfonts)
    for a in ('w:ascii','w:hAnsi','w:cs','w:eastAsia'):
        rfonts.set(qn(a), FONT)
    if size: f.size = Pt(size)
    if bold is not None: f.bold = bold
    if italic is not None: f.italic = italic
    if color is not None: f.color.rgb = color
    if caps is not None:
        c = OxmlElement('w:caps'); c.set(qn('w:val'), '1' if caps else '0'); rpr.append(c)

# Normal
n = d.styles['Normal']; set_font(n, 11)
pf = n.paragraph_format; pf.space_after = Pt(6); pf.space_before = Pt(0); pf.line_spacing = 1.15

for name in ('Body Text','First Paragraph','Compact'):
    st = d.styles[name]; set_font(st, 11)
    st.paragraph_format.space_after = Pt(7)
    st.paragraph_format.line_spacing = 1.05
    st.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    st.paragraph_format.first_line_indent = Inches(0)
d.styles['Compact'].paragraph_format.space_after = Pt(3)

# Title
t = d.styles['Title']; set_font(t, 18, bold=True)
t.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
t.paragraph_format.space_after = Pt(10)
t.paragraph_format.space_before = Pt(0)
# remove title bottom border if any
s = d.styles['Subtitle']; set_font(s, 12, bold=False, italic=False)
s.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
s.paragraph_format.space_after = Pt(10)

# Headings
sizes = {'Heading 1':12.5,'Heading 2':11.5,'Heading 3':11,'Heading 4':11,'Heading 5':11,'Heading 6':11}
for name,sz in sizes.items():
    st = d.styles[name]; set_font(st, sz, bold=True, italic=False)
    st.paragraph_format.space_before = Pt(14 if name=='Heading 1' else 10)
    st.paragraph_format.space_after = Pt(6)
    st.paragraph_format.keep_with_next = True
    st.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
    st.paragraph_format.line_spacing = 1.0

# Table style borders
tbl = d.styles['Table']; set_font(tbl, 9.5)
tblPr = tbl.element.find(qn('w:tblPr'))
if tblPr is None:
    tblPr = OxmlElement('w:tblPr'); tbl.element.append(tblPr)
for old in tblPr.findall(qn('w:tblBorders')): tblPr.remove(old)
borders = OxmlElement('w:tblBorders')
for edge in ('top','left','bottom','right','insideH','insideV'):
    e = OxmlElement(f'w:{edge}'); e.set(qn('w:val'),'single'); e.set(qn('w:sz'),'4'); e.set(qn('w:space'),'0'); e.set(qn('w:color'),'666666')
    borders.append(e)
tblPr.append(borders)
for m in ('w:tblCellMar',):
    pass

# Block quote for recitals
try:
    bq = d.styles['Block Text']; set_font(bq, 11)
except KeyError:
    pass

d.save('work/reference.docx')
print('built reference.docx')
