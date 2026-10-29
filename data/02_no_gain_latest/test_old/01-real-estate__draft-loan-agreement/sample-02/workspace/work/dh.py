"""Helper functions for building professional Word documents with python-docx."""
from docx import Document
from docx.shared import Pt, Inches, RGBColor, Emu
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING, WD_TAB_ALIGNMENT
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.section import WD_SECTION
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

FONT = "Times New Roman"
ACCENT = RGBColor(0x1F, 0x33, 0x55)

def _set_font(style_or_run, name=FONT, size=None, bold=None, italic=None):
    f = style_or_run.font
    f.name = name
    if size is not None: f.size = Pt(size)
    if bold is not None: f.bold = bold
    if italic is not None: f.italic = italic
    rpr = style_or_run.element.get_or_add_rPr() if hasattr(style_or_run, "element") else None
    if rpr is not None:
        rf = rpr.find(qn('w:rFonts'))
        if rf is None:
            rf = OxmlElement('w:rFonts'); rpr.append(rf)
        for a in ('w:ascii','w:hAnsi','w:cs','w:eastAsia'):
            rf.set(qn(a), name)

def new_doc(base_size=11, margins=(1.0,1.0,1.0,1.0)):
    doc = Document()
    st = doc.styles['Normal']
    _set_font(st, size=base_size)
    pf = st.paragraph_format
    pf.space_after = Pt(7); pf.space_before = Pt(0)
    pf.line_spacing = 1.08
    pf.alignment = WD_ALIGN_PARAGRAPH.LEFT
    for name, size, bold, before, after in (
        ('Heading 1', 12, True, 16, 8),
        ('Heading 2', 11, True, 12, 6),
        ('Heading 3', 11, True, 10, 4),
    ):
        s = doc.styles[name]
        _set_font(s, size=size, bold=bold, italic=False)
        s.font.color.rgb = RGBColor(0,0,0)
        s.font.all_caps = False
        s.paragraph_format.space_before = Pt(before)
        s.paragraph_format.space_after = Pt(after)
        s.paragraph_format.keep_with_next = True
        s.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
        s.paragraph_format.line_spacing = 1.05
    sec = doc.sections[0]
    sec.page_width, sec.page_height = Inches(8.5), Inches(11)
    sec.top_margin, sec.bottom_margin = Inches(margins[0]), Inches(margins[1])
    sec.left_margin, sec.right_margin = Inches(margins[2]), Inches(margins[3])
    sec.header_distance = Inches(0.5); sec.footer_distance = Inches(0.5)
    return doc

def _field_run(p, instr, size=8.5, bold=False):
    r = p.add_run()
    fld = OxmlElement('w:fldChar'); fld.set(qn('w:fldCharType'), 'begin'); r._r.append(fld)
    r2 = p.add_run()
    it = OxmlElement('w:instrText'); it.set(qn('xml:space'), 'preserve'); it.text = instr; r2._r.append(it)
    r3 = p.add_run()
    fld2 = OxmlElement('w:fldChar'); fld2.set(qn('w:fldCharType'), 'separate'); r3._r.append(fld2)
    r4 = p.add_run("1")
    r5 = p.add_run()
    fld3 = OxmlElement('w:fldChar'); fld3.set(qn('w:fldCharType'), 'end'); r5._r.append(fld3)
    for rr in (r, r2, r3, r4, r5):
        rr.font.size = Pt(size); rr.font.name = FONT; rr.bold = bold
    return p

def header_footer(doc, header_left, header_right="", footer_left=""):
    sec = doc.sections[0]
    sec.different_first_page_header_footer = True
    hp = sec.header.paragraphs[0]
    hp.text = ""
    hp.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = hp.add_run(header_left)
    r.font.size = Pt(8); r.font.name = FONT; r.font.color.rgb = RGBColor(0x44,0x44,0x44)
    _bottom_border(hp)
    fp = sec.footer.paragraphs[0]
    fp.text = ""
    fp.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = fp.add_run((footer_left + "    |    Page ") if footer_left else "Page ")
    r.font.size = Pt(8.5); r.font.name = FONT; r.font.color.rgb = RGBColor(0x44,0x44,0x44)
    _field_run(fp, " PAGE ")
    r = fp.add_run(" of ")
    r.font.size = Pt(8.5); r.font.name = FONT; r.font.color.rgb = RGBColor(0x44,0x44,0x44)
    _field_run(fp, " NUMPAGES ")

def _bottom_border(p):
    pPr = p._p.get_or_add_pPr()
    pbdr = OxmlElement('w:pBdr')
    b = OxmlElement('w:bottom')
    b.set(qn('w:val'),'single'); b.set(qn('w:sz'),'4'); b.set(qn('w:space'),'1'); b.set(qn('w:color'),'999999')
    pbdr.append(b); pPr.append(pbdr)

def title_block(doc, lines):
    for i,(text,size,bold,space,align,color,italic) in enumerate(lines):
        p = doc.add_paragraph()
        p.alignment = align
        p.paragraph_format.space_before = Pt(space[0]); p.paragraph_format.space_after = Pt(space[1])
        p.paragraph_format.keep_with_next = True
        r = p.add_run(text)
        r.font.size = Pt(size); r.bold = bold; r.font.name = FONT; r.italic = italic
        if color: r.font.color.rgb = color

def para(doc, text="", bold=False, italic=False, size=None, align=None, space_before=None,
         space_after=None, indent=0.0, first_line=None, keep=False, color=None, style=None):
    p = doc.add_paragraph(style=style) if style else doc.add_paragraph()
    if text:
        add_runs(p, text, bold=bold, italic=italic, size=size, color=color)
    if align is not None: p.alignment = align
    if indent: p.paragraph_format.left_indent = Inches(indent)
    if first_line is not None: p.paragraph_format.first_line_indent = Inches(first_line)
    if space_before is not None: p.paragraph_format.space_before = Pt(space_before)
    if space_after is not None: p.paragraph_format.space_after = Pt(space_after)
    if keep: p.paragraph_format.keep_with_next = True
    return p

def add_runs(p, text, bold=False, italic=False, size=None, color=None):
    """Supports **bold** and _italic_ inline markers."""
    import re
    tokens = re.split(r'(\*\*.+?\*\*)', text)
    for t in tokens:
        if not t: continue
        b, i, s = bold, italic, text.replace(t,'')
        if t.startswith('**') and t.endswith('**'):
            t = t[2:-2]; b = True
        r = p.add_run(t)
        r.bold = b; r.italic = i; r.font.name = FONT
        if size: r.font.size = Pt(size)
        if color: r.font.color.rgb = color
    return p

def art(doc, text):
    p = doc.add_paragraph(style='Heading 1')
    p.paragraph_format.space_before = Pt(18)
    r = p.add_run(text); r.bold = True; r.font.size = Pt(12); r.font.name = FONT
    return p

def sec_h(doc, text):
    p = doc.add_paragraph(style='Heading 2')
    r = p.add_run(text); r.bold = True; r.font.size = Pt(11); r.font.name = FONT
    return p

def sub_h(doc, text):
    p = doc.add_paragraph(style='Heading 3')
    r = p.add_run(text); r.italic = True; r.bold = True; r.font.size = Pt(11); r.font.name = FONT
    return p

def numbered(doc, num, text, indent=0.35, hang=0.35, size=None, bold_lead=None):
    p = doc.add_paragraph()
    p.paragraph_format.left_indent = Inches(indent)
    p.paragraph_format.first_line_indent = Inches(-hang)
    p.paragraph_format.space_after = Pt(7)
    r = p.add_run(num + "\t"); r.font.name = FONT; r.bold = False
    if size: r.font.size = Pt(size)
    p.paragraph_format.tab_stops.add_tab_stop(Inches(indent))
    if bold_lead:
        rr = p.add_run(bold_lead); rr.bold = True; rr.font.name = FONT
        if size: rr.font.size = Pt(size)
    add_runs(p, text, size=size)
    return p

def bullet(doc, text, level=0, size=None):
    p = doc.add_paragraph()
    p.paragraph_format.left_indent = Inches(0.4 + 0.28*level)
    p.paragraph_format.first_line_indent = Inches(-0.2)
    p.paragraph_format.space_after = Pt(5)
    r = p.add_run("\u2022\t" if level == 0 else "\u2013\t"); r.font.name = FONT
    add_runs(p, text, size=size)
    return p

def draft_note(doc, label, text):
    p = doc.add_paragraph()
    p.paragraph_format.left_indent = Inches(0.35)
    p.paragraph_format.right_indent = Inches(0.2)
    p.paragraph_format.space_before = Pt(2); p.paragraph_format.space_after = Pt(10)
    r = p.add_run(label + " "); r.bold = True; r.italic = True; r.font.size = Pt(9); r.font.name = FONT
    r.font.color.rgb = RGBColor(0x66,0x33,0x00)
    rr = p.add_run(text); rr.italic = True; rr.font.size = Pt(9); rr.font.name = FONT
    rr.font.color.rgb = RGBColor(0x66,0x33,0x00)
    return p

def shade(cell, hexcolor):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'),'clear'); shd.set(qn('w:color'),'auto'); shd.set(qn('w:fill'),hexcolor)
    tcPr.append(shd)

def set_repeat_header(row):
    trPr = row._tr.get_or_add_trPr()
    el = OxmlElement('w:tblHeader'); el.set(qn('w:val'),'true'); trPr.append(el)

def table(doc, header, rows, widths=None, size=9.5, header_fill="1F3355", align_right_cols=(), bold_last_row=False, first_col_bold=False, zebra=True):
    t = doc.add_table(rows=1, cols=len(header))
    t.style = 'Table Grid'
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    t.autofit = False
    hdr = t.rows[0]
    for i, h in enumerate(header):
        c = hdr.cells[i]
        c.text = ""
        p = c.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_before = Pt(3); p.paragraph_format.space_after = Pt(3)
        r = p.add_run(h); r.bold = True; r.font.size = Pt(size); r.font.name = FONT
        r.font.color.rgb = RGBColor(0xFF,0xFF,0xFF)
        shade(c, header_fill)
    set_repeat_header(hdr)
    for ri, row in enumerate(rows):
        new_row = t.add_row()
        trPr = new_row._tr.get_or_add_trPr()
        cs = OxmlElement('w:cantSplit'); cs.set(qn('w:val'), 'true'); trPr.append(cs)
        cells = new_row.cells
        last = bold_last_row and ri == len(rows)-1
        for ci, val in enumerate(row):
            c = cells[ci]
            c.text = ""
            p = c.paragraphs[0]
            p.paragraph_format.space_before = Pt(2); p.paragraph_format.space_after = Pt(2)
            p.alignment = WD_ALIGN_PARAGRAPH.RIGHT if ci in align_right_cols else WD_ALIGN_PARAGRAPH.LEFT
            add_runs(p, str(val), size=size, bold=last or (first_col_bold and ci==0))
            if last: shade(c, "EDEFF3")
            elif zebra and ri % 2 == 1: shade(c, "F7F8FA")
    if widths:
        tot = sum(widths)
        usable = doc.sections[-1].page_width - doc.sections[-1].left_margin - doc.sections[-1].right_margin
        if tot*914400 > usable:
            raise ValueError("table too wide: %.2f in vs %.2f in usable" % (tot, usable/914400))
        for i, w in enumerate(widths):
            t.columns[i].width = Inches(w)
        for row in t.rows:
            for i, w in enumerate(widths):
                row.cells[i].width = Inches(w)
    doc.add_paragraph().paragraph_format.space_after = Pt(2)
    return t

def page_break(doc):
    from docx.enum.text import WD_BREAK
    p = doc.add_paragraph()
    p.add_run().add_break(WD_BREAK.PAGE)

def rule(doc, space=6):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(space); p.paragraph_format.space_after = Pt(space)
    _bottom_border(p)
    return p

def new_section(doc, landscape=False, margins=(0.8,0.8,1.0,1.0)):
    from docx.enum.section import WD_SECTION, WD_ORIENT
    sec = doc.add_section(WD_SECTION.NEW_PAGE)
    if landscape:
        sec.orientation = WD_ORIENT.LANDSCAPE
        sec.page_width, sec.page_height = Inches(11), Inches(8.5)
        sec.top_margin, sec.bottom_margin = Inches(margins[0]), Inches(margins[1])
        sec.left_margin, sec.right_margin = Inches(margins[2]), Inches(margins[3])
    else:
        sec.orientation = WD_ORIENT.PORTRAIT
        sec.page_width, sec.page_height = Inches(8.5), Inches(11)
        sec.top_margin, sec.bottom_margin = Inches(margins[0]), Inches(margins[1])
        sec.left_margin, sec.right_margin = Inches(margins[2]), Inches(margins[3])
    return sec
