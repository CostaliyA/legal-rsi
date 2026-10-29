"""Post-process a pandoc-generated .docx into a firm-quality legal document."""
import sys, re, copy
import docx
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
from docx.enum.section import WD_SECTION
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

FONT = "Times New Roman"

def set_run_font(run, size=None, bold=None, italic=None, caps=None, color=None):
    run.font.name = FONT
    rpr = run._element.get_or_add_rPr()
    rf = rpr.find(qn('w:rFonts'))
    if rf is None:
        rf = OxmlElement('w:rFonts'); rpr.append(rf)
    for a in ('w:ascii','w:hAnsi','w:cs','w:eastAsia'):
        rf.set(qn(a), FONT)
    if size is not None: run.font.size = Pt(size)
    if bold is not None: run.font.bold = bold
    if italic is not None: run.font.italic = italic
    if caps: run.font.all_caps = True
    if color is not None: run.font.color.rgb = color

def restyle_para_fonts(paragraph, size=None):
    for r in paragraph.runs:
        set_run_font(r, size=size)

def field(paragraph, code):
    run = paragraph.add_run()
    f1 = OxmlElement('w:fldChar'); f1.set(qn('w:fldCharType'), 'begin')
    it = OxmlElement('w:instrText'); it.set(qn('xml:space'), 'preserve'); it.text = code
    f2 = OxmlElement('w:fldChar'); f2.set(qn('w:fldCharType'), 'end')
    run._r.append(f1); run._r.append(it); run._r.append(f2)
    return run

def shade(cell, hexcolor):
    tcPr = cell._tc.get_or_add_tcPr()
    sh = OxmlElement('w:shd'); sh.set(qn('w:val'),'clear'); sh.set(qn('w:color'),'auto'); sh.set(qn('w:fill'),hexcolor)
    tcPr.append(sh)

def repeat_header(row):
    trPr = row._tr.get_or_add_trPr()
    el = OxmlElement('w:tblHeader'); el.set(qn('w:val'), 'true'); trPr.append(el)

def set_borders(table):
    tbl = table._tbl
    tblPr = tbl.tblPr
    borders = OxmlElement('w:tblBorders')
    for edge in ('top','left','bottom','right','insideH','insideV'):
        e = OxmlElement('w:'+edge)
        e.set(qn('w:val'),'single'); e.set(qn('w:sz'),'4'); e.set(qn('w:space'),'0'); e.set(qn('w:color'),'808080')
        borders.append(e)
    tblPr.append(borders)

def main(path, header_left, footer_left, cover_end_marker=None, exhibit_prefix="EXHIBIT", toc_marker="TABLE OF CONTENTS"):
    doc = docx.Document(path)

    # page setup
    for s in doc.sections:
        s.page_width = Inches(8.5); s.page_height = Inches(11)
        s.left_margin = Inches(1.0); s.right_margin = Inches(1.0)
        s.top_margin = Inches(1.0); s.bottom_margin = Inches(1.0)
        s.header_distance = Inches(0.5); s.footer_distance = Inches(0.5)

    # base styles
    normal = doc.styles['Normal']
    normal.font.name = FONT; normal.font.size = Pt(11)
    rpr = normal.element.get_or_add_rPr()
    rf = rpr.find(qn('w:rFonts'))
    if rf is None:
        rf = OxmlElement('w:rFonts'); rpr.append(rf)
    for a in ('w:ascii','w:hAnsi','w:cs','w:eastAsia'):
        rf.set(qn(a), FONT)
    pf = normal.paragraph_format
    pf.space_before = Pt(0); pf.space_after = Pt(6); pf.line_spacing = 1.12
    pf.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY

    for name, size, align, before, after in (('Heading 1', 14, WD_ALIGN_PARAGRAPH.CENTER, 12, 8),
                                             ('Heading 2', 11.5, WD_ALIGN_PARAGRAPH.CENTER, 14, 8),
                                             ('Heading 3', 11, WD_ALIGN_PARAGRAPH.LEFT, 10, 4)):
        try:
            st = doc.styles[name]
        except KeyError:
            continue
        st.font.name = FONT; st.font.size = Pt(size); st.font.bold = True
        st.font.color.rgb = RGBColor(0,0,0)
        st.font.italic = False
        st.paragraph_format.alignment = align
        st.paragraph_format.space_before = Pt(before)
        st.paragraph_format.space_after = Pt(after)
        st.paragraph_format.keep_with_next = True
        st.paragraph_format.line_spacing = 1.0

    paras = doc.paragraphs

    # ---- cover page block (first paragraph through the paragraph before the TOC marker)
    toc_idx = None
    for i, p in enumerate(paras):
        if p.text.strip().upper().startswith(toc_marker):
            toc_idx = i; break

    if toc_idx:
        cover = paras[:toc_idx]
        for i, p in enumerate(cover):
            if not p.text.strip():
                continue
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p.paragraph_format.space_after = Pt(6)
            p.paragraph_format.first_line_indent = Inches(0)
            txt = p.text.strip()
            if i == 0:
                for r in p.runs: set_run_font(r, size=20, bold=True)
                p.paragraph_format.space_before = Pt(96); p.paragraph_format.space_after = Pt(10)
            elif txt.startswith('('):
                for r in p.runs: set_run_font(r, size=12, italic=True)
            elif txt == 'THE PIEDMONT AT BRIGHTLEAF':
                for r in p.runs: set_run_font(r, size=15, bold=True)
                p.paragraph_format.space_before = Pt(26)
            elif txt == 'BETWEEN' or txt == 'AND':
                for r in p.runs: set_run_font(r, size=11, bold=True)
                p.paragraph_format.space_before = Pt(22)
            elif txt.startswith('DRAFT'):
                for r in p.runs: set_run_font(r, size=11, bold=True)
                p.paragraph_format.space_before = Pt(34)
            elif txt.startswith('Prepared by'):
                for r in p.runs: set_run_font(r, size=9, italic=True)
                p.paragraph_format.space_before = Pt(10)
                p.paragraph_format.left_indent = Inches(0.6); p.paragraph_format.right_indent = Inches(0.6)
            else:
                for r in p.runs: set_run_font(r, size=11.5)
        # page break after cover
        last = cover[-1]
        last.add_run().add_break(WD_BREAK.PAGE)

    # ---- TOC heading
    for i, p in enumerate(doc.paragraphs):
        if p.text.strip().upper().startswith(toc_marker):
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p.paragraph_format.space_before = Pt(0); p.paragraph_format.space_after = Pt(12)
            for r in p.runs: set_run_font(r, size=12, bold=True)
            break

    # ---- tables
    for t in doc.tables:
        t.alignment = WD_TABLE_ALIGNMENT.CENTER
        t.autofit = True
        set_borders(t)
        for ri, row in enumerate(t.rows):
            if ri == 0:
                repeat_header(row)
            for cell in row.cells:
                if ri == 0: shade(cell, 'E8E8E8')
                for p in cell.paragraphs:
                    p.paragraph_format.space_after = Pt(1)
                    p.paragraph_format.space_before = Pt(1)
                    p.paragraph_format.line_spacing = 1.0
                    p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
                    for r in p.runs:
                        set_run_font(r, size=8.5, bold=(ri == 0) or None)

    # ---- body paragraph formatting
    for i, p in enumerate(doc.paragraphs):
        if p.style.name.startswith('Heading'):
            continue
        if p.text.strip() == '':
            continue
        p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        p.paragraph_format.first_line_indent = Inches(0)
        # signature lines / short centered blocks left as-is
        if p.text.strip().startswith(('By:', 'Name:', 'Title:', 'Date:', '_____', 'Executed this')):
            p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT

    # ---- page break before each exhibit heading
    for p in doc.paragraphs:
        if p.style.name.startswith('Heading') and p.text.strip().upper().startswith(exhibit_prefix):
            p.paragraph_format.page_break_before = True
    # page break before SIGNATURE PAGES heading
    for p in doc.paragraphs:
        if p.style.name.startswith('Heading') and 'SIGNATURE PAGES' in p.text.upper():
            p.paragraph_format.page_break_before = True

    # ---- header / footer
    sec = doc.sections[0]
    hp = sec.header.paragraphs[0]
    hp.text = ''
    r = hp.add_run(header_left)
    set_run_font(r, size=8, italic=True, color=RGBColor(0x44,0x44,0x44))
    hp.alignment = WD_ALIGN_PARAGRAPH.CENTER

    fp = sec.footer.paragraphs[0]
    fp.text = ''
    fp.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = fp.add_run(footer_left + "   |   Page ")
    set_run_font(r, size=8, color=RGBColor(0x44,0x44,0x44))
    fr = field(fp, ' PAGE '); set_run_font(fr, size=8, color=RGBColor(0x44,0x44,0x44))
    r = fp.add_run(" of "); set_run_font(r, size=8, color=RGBColor(0x44,0x44,0x44))
    fr = field(fp, ' NUMPAGES '); set_run_font(fr, size=8, color=RGBColor(0x44,0x44,0x44))

    doc.save(path)
    print("styled", path)

if __name__ == '__main__':
    import json
    cfg = json.loads(sys.argv[1])
    main(cfg['path'], cfg['header'], cfg['footer'])
