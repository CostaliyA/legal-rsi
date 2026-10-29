import re
from docx import Document
from docx.shared import Pt, Inches, RGBColor, Emu
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING, WD_BREAK
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.section import WD_SECTION
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

FONT = "Times New Roman"

def new_doc(margin_l=1.0, margin_r=1.0):
    doc = Document()
    st = doc.styles["Normal"]
    st.font.name = FONT
    st.font.size = Pt(10.5)
    st.element.rPr.rFonts.set(qn("w:eastAsia"), FONT)
    pf = st.paragraph_format
    pf.space_before = Pt(0); pf.space_after = Pt(6)
    pf.line_spacing_rule = WD_LINE_SPACING.SINGLE
    s = doc.sections[0]
    s.page_width = Inches(8.5); s.page_height = Inches(11)
    s.left_margin = Inches(margin_l); s.right_margin = Inches(margin_r)
    s.top_margin = Inches(1.0); s.bottom_margin = Inches(0.9)
    return doc

def _runs(par, text, bold=False, italic=False, size=None, caps=False, color=None, underline=False):
    """Render text, honouring **bold** and _italic_ inline markers."""
    tokens = re.split(r"(\*\*.+?\*\*|__.+?__|(?<!\*)\*[^*\n]{1,140}\*(?!\*))", text)
    for t in tokens:
        if not t: continue
        b, i = bold, italic
        if t.startswith("**") and t.endswith("**") and len(t) > 4:
            t = t[2:-2]; b = True
        elif t.startswith("__") and t.endswith("__") and len(t) > 4:
            t = t[2:-2]; i = True
        elif t.startswith("*") and t.endswith("*") and len(t) > 2:
            t = t[1:-1]; i = True
        r = par.add_run(t)
        r.bold = b; r.italic = i
        r.font.name = FONT
        if size: r.font.size = Pt(size)
        if caps: r.font.all_caps = True
        if underline: r.underline = True
        if color: r.font.color.rgb = color
    return par

def cover_line(doc, text, size=10, bold=False, space_after=6, center=True, italic=False, caps=False, color=None):
    p = doc.add_paragraph()
    if center: p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_after = Pt(space_after)
    _runs(p, text, bold=bold, italic=italic, size=size, caps=caps, color=color)
    return p

def art(doc, text):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    pf = p.paragraph_format
    pf.space_before = Pt(16); pf.space_after = Pt(10); pf.keep_with_next = True
    label = text.upper()
    if ". " in label:
        num, title = label.split(". ", 1)
        label = num + " \u2014 " + title
    r = p.add_run(label); r.bold = True; r.font.name = FONT; r.font.size = Pt(11)
    return p

def sec(doc, num, heading, body=None):
    p = doc.add_paragraph()
    pf = p.paragraph_format
    pf.left_indent = Inches(0.5); pf.first_line_indent = Inches(-0.5)
    pf.space_before = Pt(8); pf.space_after = Pt(6); pf.keep_with_next = bool(body is None)
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    _runs(p, num + ".\t", bold=True)
    tab_stops = p.paragraph_format.tab_stops
    tab_stops.add_tab_stop(Inches(0.5))
    if heading:
        _runs(p, heading + ". ", bold=True)
    if body:
        _runs(p, body)
    return p

def sub(doc, label, body, level=1):
    ind = {1: 1.0, 2: 1.5, 3: 2.0}[level]
    p = doc.add_paragraph()
    pf = p.paragraph_format
    pf.left_indent = Inches(ind); pf.first_line_indent = Inches(-0.5)
    pf.space_before = Pt(0); pf.space_after = Pt(5)
    pf.tab_stops.add_tab_stop(Inches(ind))
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    _runs(p, label + "\t")
    _runs(p, body)
    return p

def para(doc, text, indent=0.0, first=0.0, space_after=6, align="justify", size=None, bold=False, italic=False):
    p = doc.add_paragraph()
    pf = p.paragraph_format
    pf.left_indent = Inches(indent); pf.first_line_indent = Inches(first)
    pf.space_after = Pt(space_after)
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY if align == "justify" else WD_ALIGN_PARAGRAPH.CENTER
    _runs(p, text, bold=bold, italic=italic, size=size)
    return p

def defn(doc, term, text):
    return para(doc, '**"%s"** %s' % (term, text), first=0.5, space_after=5)

def note(doc, text):
    p = doc.add_paragraph()
    pf = p.paragraph_format
    pf.left_indent = Inches(0.5); pf.right_indent = Inches(0.5)
    pf.space_before = Pt(4); pf.space_after = Pt(8)
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    _runs(p, text, italic=True, size=9)
    return p

def shade(cell, hexcolor="D9D9D9"):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear"); shd.set(qn("w:color"), "auto"); shd.set(qn("w:fill"), hexcolor)
    tcPr.append(shd)

def table(doc, rows, widths, header=True, size=9, align_right=None, caption=None, bold_rows=()):
    if caption:
        p = doc.add_paragraph(); p.paragraph_format.space_before = Pt(6); p.paragraph_format.space_after = Pt(3)
        p.paragraph_format.keep_with_next = True
        runs(p, caption, bold=True, size=9)
    t = doc.add_table(rows=len(rows), cols=len(rows[0]))
    t.style = "Table Grid"; t.alignment = WD_TABLE_ALIGNMENT.CENTER
    t.autofit = False
    tblPr = t._tbl.tblPr
    # fixed layout
    layout = OxmlElement("w:tblLayout"); layout.set(qn("w:type"), "fixed"); tblPr.append(layout)
    tblW = OxmlElement("w:tblW"); tblW.set(qn("w:type"), "dxa")
    tblW.set(qn("w:w"), str(int(sum(widths) * 1440))); tblPr.append(tblW)
    mar = OxmlElement("w:tblCellMar")
    for side in ("top", "left", "bottom", "right"):
        e = OxmlElement("w:" + side)
        e.set(qn("w:w"), "60" if side in ("left", "right") else "20")
        e.set(qn("w:type"), "dxa"); mar.append(e)
    tblPr.append(mar)
    # grid
    for i, w in enumerate(widths):
        t.columns[i].width = Inches(w)
    align_right = align_right or []
    for ri, row in enumerate(rows):
        for ci, val in enumerate(row):
            cell = t.cell(ri, ci)
            cell.width = Inches(widths[ci])
            cell.text = ""
            p = cell.paragraphs[0]
            p.paragraph_format.space_before = Pt(1); p.paragraph_format.space_after = Pt(1)
            p.paragraph_format.line_spacing_rule = WD_LINE_SPACING.SINGLE
            if ci in align_right and ri > 0:
                p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
            runs(p, str(val), bold=(header and ri == 0) or (ri in bold_rows), size=size)
            if header and ri == 0:
                shade(cell, "D9D9D9")
    # repeat header row on page breaks
    if header:
        trPr = t.rows[0]._tr.get_or_add_trPr()
        th = OxmlElement("w:tblHeader"); th.set(qn("w:val"), "true"); trPr.append(th)
    sp = doc.add_paragraph(); sp.paragraph_format.space_after = Pt(2)
    sp.paragraph_format.space_before = Pt(0)
    for r in sp.runs: pass
    return t

def pagebreak(doc):
    p = doc.add_paragraph()
    p.add_run().add_break(WD_BREAK.PAGE)

def field(par, instr):
    r = par.add_run()
    f1 = OxmlElement("w:fldChar"); f1.set(qn("w:fldCharType"), "begin")
    it = OxmlElement("w:instrText"); it.set(qn("xml:space"), "preserve"); it.text = instr
    f2 = OxmlElement("w:fldChar"); f2.set(qn("w:fldCharType"), "separate")
    t = OxmlElement("w:t"); t.text = "1"
    f3 = OxmlElement("w:fldChar"); f3.set(qn("w:fldCharType"), "end")
    r._r.append(f1); r._r.append(it); r._r.append(f2); r._r.append(t); r._r.append(f3)

def header_footer(doc, left_text, right_text="", footer_left=""):
    s = doc.sections[0]
    hp = s.header.paragraphs[0]
    hp.text = ""
    hp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    _runs(hp, left_text, size=8, italic=True)
    # bottom border on header paragraph
    pPr = hp._p.get_or_add_pPr()
    pbdr = OxmlElement("w:pBdr"); bottom = OxmlElement("w:bottom")
    bottom.set(qn("w:val"), "single"); bottom.set(qn("w:sz"), "4"); bottom.set(qn("w:space"), "1"); bottom.set(qn("w:color"), "808080")
    pbdr.append(bottom); pPr.append(pbdr)
    fp = s.footer.paragraphs[0]
    fp.text = ""
    fp.alignment = WD_ALIGN_PARAGRAPH.CENTER
    if footer_left:
        _runs(fp, footer_left + "    |    ", size=8, italic=True)
    _runs(fp, "Page ", size=8)
    field(fp, "PAGE")
    _runs(fp, " of ", size=8)
    field(fp, "NUMPAGES")

def set_core(doc, title, subject, author, comments):
    cp = doc.core_properties
    cp.title = title; cp.subject = subject; cp.author = author
    cp.comments = comments; cp.category = "Ground Lease"

runs = _runs
