from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING
from docx.enum.section import WD_SECTION
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
import copy

doc = Document()

# Page setup
for s in doc.sections:
    s.page_width = Inches(8.5); s.page_height = Inches(11)
    s.left_margin = Inches(1.0); s.right_margin = Inches(1.0)
    s.top_margin = Inches(1.0); s.bottom_margin = Inches(0.9)
    s.header_distance = Inches(0.5); s.footer_distance = Inches(0.5)

styles = doc.styles

def setfont(st, name='Times New Roman', size=11, bold=None, italic=None, color=None, caps=None):
    f = st.font
    f.name = name; f.size = Pt(size)
    if bold is not None: f.bold = bold
    if italic is not None: f.italic = italic
    if caps is not None: f.all_caps = caps
    if color is not None: f.color.rgb = RGBColor(*color)
    rpr = st.element.get_or_add_rPr()
    rf = rpr.find(qn('w:rFonts'))
    if rf is None:
        rf = OxmlElement('w:rFonts'); rpr.append(rf)
    for a in ('w:ascii','w:hAnsi','w:cs','w:eastAsia'):
        rf.set(qn(a), name)

# Normal
setfont(styles['Normal'], size=11)
pf = styles['Normal'].paragraph_format
pf.space_before = Pt(0); pf.space_after = Pt(6)
pf.line_spacing_rule = WD_LINE_SPACING.SINGLE

for nm in ('Body Text','First Paragraph','Compact'):
    try: st = styles[nm]
    except KeyError:
        st = styles.add_style(nm, 1)
    setfont(st, size=11)
    pf = st.paragraph_format
    pf.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    pf.left_indent = Inches(0.5)
    pf.first_line_indent = Inches(0)
    pf.space_before = Pt(0); pf.space_after = Pt(8)
    pf.line_spacing = 1.15

# Heading 1 - Article
st = styles['Heading 1']
setfont(st, size=11.5, bold=True, color=(0,0,0))
pf = st.paragraph_format
pf.alignment = WD_ALIGN_PARAGRAPH.CENTER
pf.space_before = Pt(18); pf.space_after = Pt(10)
pf.keep_with_next = True
pf.left_indent = Inches(0)

# Heading 2 - Section
st = styles['Heading 2']
setfont(st, size=11, bold=True, color=(0,0,0))
pf = st.paragraph_format
pf.alignment = WD_ALIGN_PARAGRAPH.LEFT
pf.space_before = Pt(12); pf.space_after = Pt(6)
pf.keep_with_next = True
pf.left_indent = Inches(0.5)

# Heading 3
st = styles['Heading 3']
setfont(st, size=11, bold=True, italic=True, color=(0,0,0))
pf = st.paragraph_format
pf.space_before = Pt(8); pf.space_after = Pt(4)
pf.keep_with_next = True
pf.left_indent = Inches(0.5)

# Title
st = styles['Title']
setfont(st, size=16, bold=True, color=(0,0,0))
pf = st.paragraph_format
pf.alignment = WD_ALIGN_PARAGRAPH.CENTER
pf.space_before = Pt(0); pf.space_after = Pt(12)

# Subtitle
st = styles['Subtitle']
setfont(st, size=12.5, bold=False, italic=True, color=(0,0,0))
pf = st.paragraph_format
pf.alignment = WD_ALIGN_PARAGRAPH.CENTER
pf.space_before = Pt(0); pf.space_after = Pt(8)

# SubPara: hanging lettered clause
try: st = styles['SubPara']
except KeyError: st = styles.add_style('SubPara', 1)
setfont(st, size=11)
pf = st.paragraph_format
pf.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
pf.left_indent = Inches(1.0); pf.first_line_indent = Inches(-0.35)
pf.space_before = Pt(0); pf.space_after = Pt(6)
pf.line_spacing = 1.15

# SubPara2 deeper
try: st = styles['SubPara2']
except KeyError: st = styles.add_style('SubPara2', 1)
setfont(st, size=11)
pf = st.paragraph_format
pf.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
pf.left_indent = Inches(1.4); pf.first_line_indent = Inches(-0.35)
pf.space_before = Pt(0); pf.space_after = Pt(6)
pf.line_spacing = 1.15

# DraftNote style
try: st = styles['DraftNote']
except KeyError: st = styles.add_style('DraftNote', 1)
setfont(st, size=9.5, italic=True, color=(0x44,0x44,0x44))
pf = st.paragraph_format
pf.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
pf.left_indent = Inches(0.5); pf.right_indent = Inches(0.4)
pf.space_before = Pt(4); pf.space_after = Pt(8)
pf.line_spacing = 1.0
# left border
pPr = st.element.get_or_add_pPr()
pbdr = OxmlElement('w:pBdr')
left = OxmlElement('w:left')
left.set(qn('w:val'),'single'); left.set(qn('w:sz'),'8'); left.set(qn('w:space'),'6'); left.set(qn('w:color'),'888888')
pbdr.append(left); pPr.append(pbdr)

# Table style base
try: st = styles['Table']
except KeyError: st = styles.add_style('Table', 3)
setfont(st, size=9.5)

# Caption / table title
try: st = styles['Caption']
except KeyError: st = styles.add_style('Caption', 1)
setfont(st, size=9.5, bold=True, italic=False, color=(0,0,0))
styles['Caption'].paragraph_format.space_before = Pt(10)
styles['Caption'].paragraph_format.space_after = Pt(4)
styles['Caption'].paragraph_format.keep_with_next = True
styles['Caption'].paragraph_format.left_indent = Inches(0)


# SigBlock style
try: st = styles['SigBlock']
except KeyError: st = styles.add_style('SigBlock', 1)
setfont(st, size=11, italic=False)
pf = st.paragraph_format
pf.alignment = WD_ALIGN_PARAGRAPH.LEFT
pf.left_indent = Inches(0.5); pf.first_line_indent = Inches(0)
pf.space_before = Pt(0); pf.space_after = Pt(0)
pf.line_spacing = 1.15

doc.save('ref.docx')
print("ref saved")
