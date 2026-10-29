import sys, json, copy
import docx
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
from docx.text.paragraph import Paragraph

FONT = "Times New Roman"

def set_run_font(run, size=None, bold=None, italic=None, color=None, caps=None):
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
    tblPr = table._tbl.tblPr
    borders = OxmlElement('w:tblBorders')
    for edge in ('top','left','bottom','right','insideH','insideV'):
        e = OxmlElement('w:'+edge)
        e.set(qn('w:val'),'single'); e.set(qn('w:sz'),'4'); e.set(qn('w:space'),'0'); e.set(qn('w:color'),'999999')
        borders.append(e)
    tblPr.append(borders)

def set_cell_margins(table, twips=45):
    tblPr = table._tbl.tblPr
    mar = OxmlElement('w:tblCellMar')
    for side in ('top','left','bottom','right'):
        e = OxmlElement('w:'+side)
        e.set(qn('w:w'), str(twips if side in ('left','right') else 15))
        e.set(qn('w:type'),'dxa')
        mar.append(e)
    tblPr.append(mar)

def set_table_width(table, total_in):
    tblPr = table._tbl.tblPr
    for el in tblPr.findall(qn('w:tblW')):
        tblPr.remove(el)
    w = OxmlElement('w:tblW'); w.set(qn('w:type'),'dxa'); w.set(qn('w:w'), str(int(total_in*1440)))
    tblPr.append(w)
    lay = OxmlElement('w:tblLayout'); lay.set(qn('w:type'),'fixed'); tblPr.append(lay)
    ncols = len(table.columns)
    widths = [total_in/ncols]*ncols
    # widen first column for label/description tables
    if ncols in (2,3):
        widths[0] = total_in*0.32; widths[-1] = total_in - widths[0] - (total_in*0.34 if ncols==3 else 0)
    if ncols >= 8:
        w0 = 0.42; w1 = 1.55
        rest = (total_in - w0 - w1)/(ncols-2)
        widths = [w0, w1] + [rest]*(ncols-2)
    for i, col in enumerate(table.columns):
        col.width = Inches(round(widths[i],3))
    for row in table.rows:
        for i, cell in enumerate(row.cells):
            if i < len(widths):
                cell.width = Inches(round(widths[i],3))

def insert_break_para_before(par):
    newp = OxmlElement('w:p')
    par._p.addprevious(newp)
    p = Paragraph(newp, par._parent)
    p.paragraph_format.space_before = Pt(0); p.paragraph_format.space_after = Pt(0)
    return p

def add_sectpr_to_para(p, sectPr_template, landscape=False):
    pPr = p._p.get_or_add_pPr()
    sp = copy.deepcopy(sectPr_template)
    if landscape:
        pgSz = sp.find(qn('w:pgSz'))
        pgSz.set(qn('w:w'), '15840'); pgSz.set(qn('w:h'), '12240')
        pgSz.set(qn('w:orient'), 'landscape')
        mar = sp.find(qn('w:pgMar'))
        mar.set(qn('w:top'),'864'); mar.set(qn('w:bottom'),'864')
        mar.set(qn('w:left'),'1080'); mar.set(qn('w:right'),'1080')
        mar.set(qn('w:header'),'432'); mar.set(qn('w:footer'),'432')
    pPr.append(sp)
    p.paragraph_format.space_after = Pt(0)
    for r in p.runs: r.font.size = Pt(1)

def main(cfg):
    path = cfg['path']
    doc = docx.Document(path)
    for s in doc.sections:
        s.page_width = Inches(8.5); s.page_height = Inches(11)
        s.left_margin = Inches(1.0); s.right_margin = Inches(1.0)
        s.top_margin = Inches(1.0); s.bottom_margin = Inches(1.0)

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

    for name, size, align, before, after in (('Heading 1', 13, WD_ALIGN_PARAGRAPH.CENTER, 12, 6),
                                             ('Heading 2', 11.5, WD_ALIGN_PARAGRAPH.CENTER, 14, 6),
                                             ('Heading 3', 11, WD_ALIGN_PARAGRAPH.LEFT, 10, 4)):
        try: st = doc.styles[name]
        except KeyError: continue
        st.font.name = FONT; st.font.size = Pt(size); st.font.bold = True
        st.font.color.rgb = RGBColor(0,0,0); st.font.italic = False
        st.paragraph_format.alignment = align
        st.paragraph_format.space_before = Pt(before); st.paragraph_format.space_after = Pt(after)
        st.paragraph_format.keep_with_next = True; st.paragraph_format.line_spacing = 1.0

    # ---------- COVER ----------
    toc_marker = cfg.get('toc_marker', 'TABLE OF CONTENTS')
    paras = doc.paragraphs
    toc_idx = next((i for i,p in enumerate(paras) if p.text.strip().upper().startswith(toc_marker)), None)
    if toc_idx:
        cover = paras[:toc_idx]
        for i,p in enumerate(cover):
            t = p.text.strip()
            if not t: continue
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p.paragraph_format.first_line_indent = Inches(0)
            p.paragraph_format.space_after = Pt(6)
            if i == 0:
                for r in p.runs: set_run_font(r, size=19, bold=True)
                p.paragraph_format.space_before = Pt(70); p.paragraph_format.space_after = Pt(8)
            elif t.startswith('('):
                for r in p.runs: set_run_font(r, size=11.5, italic=True)
            elif t == 'THE PIEDMONT AT BRIGHTLEAF':
                for r in p.runs: set_run_font(r, size=15, bold=True)
                p.paragraph_format.space_before = Pt(24)
            elif t in ('BETWEEN','AND'):
                for r in p.runs: set_run_font(r, size=10.5, bold=True)
                p.paragraph_format.space_before = Pt(18)
            elif t.startswith('DRAFT'):
                for r in p.runs: set_run_font(r, size=11, bold=True)
                p.paragraph_format.space_before = Pt(30)
            elif t.startswith('Prepared by') or t.startswith('This draft'):
                for r in p.runs: set_run_font(r, size=8.5, italic=True)
                p.paragraph_format.left_indent = Inches(0.55); p.paragraph_format.right_indent = Inches(0.55)
                p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
            else:
                for r in p.runs: set_run_font(r, size=11)
        cover[-1].add_run().add_break(WD_BREAK.PAGE)

    for p in doc.paragraphs:
        if p.text.strip().upper().startswith(toc_marker):
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p.paragraph_format.space_before = Pt(0); p.paragraph_format.space_after = Pt(10)
            for r in p.runs: set_run_font(r, size=12, bold=True)
            break

    # ---------- LANDSCAPE RANGES ----------
    lr = cfg.get('landscape', [])
    body_sectPr = doc.element.body.find(qn('w:sectPr'))
    for r in lr:
        start = next((p for p in doc.paragraphs if p.text.strip().upper().startswith(r['start'].upper())), None)
        end = next((p for p in doc.paragraphs if p.text.strip().upper().startswith(r['end'].upper())), None)
        if not start or not end:
            print("landscape markers not found", r); continue
        pre = insert_break_para_before(start)
        add_sectpr_to_para(pre, body_sectPr, landscape=False)
        post = insert_break_para_before(end)
        add_sectpr_to_para(post, body_sectPr, landscape=True)

    # ---------- BODY ----------
    for p in doc.paragraphs:
        if p.style.name.startswith('Heading'): continue
        if not p.text.strip(): continue
        p.paragraph_format.first_line_indent = Inches(0)
        t = p.text.strip()
        if not (t.startswith(('By:','Name:','Title:','Date:','_____','Executed this')) or t.split(chr(10))[0].strip().endswith('individually') or t in ('LENDER:','BORROWER:','GUARANTORS:')):
            p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        else:
            p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT

    # ---------- TABLES ----------
    for t in doc.tables:
        ncols = len(t.columns)
        total = cfg.get('wide_total', 9.35) if ncols >= 8 else 6.5
        t.alignment = WD_TABLE_ALIGNMENT.CENTER
        set_borders(t); set_cell_margins(t, 40 if ncols>=8 else 80); set_table_width(t, total)
        for ri,row in enumerate(t.rows):
            if ri == 0: repeat_header(row)
            for cell in row.cells:
                if ri == 0: shade(cell, 'E6E6E6')
                for p in cell.paragraphs:
                    pfx = p.paragraph_format
                    pfx.space_before = Pt(1); pfx.space_after = Pt(1); pfx.line_spacing = 1.0
                    pfx.first_line_indent = Inches(0)
                    pfx.alignment = WD_ALIGN_PARAGRAPH.LEFT
                    fsz = cfg.get('table_font', 8) if ncols < 8 else cfg.get('wide_font', 7)
                    for r in p.runs:
                        set_run_font(r, size=fsz, bold=(True if ri==0 else None))

    # ---------- page breaks before exhibits ----------
    for p in doc.paragraphs:
        if p.style.name.startswith('Heading'):
            up = p.text.strip().upper()
            if up.startswith(cfg.get('exhibit_prefix','EXHIBIT')) or 'SIGNATURE PAGES' in up:
                p.paragraph_format.page_break_before = True

    # ---------- page break after TOC ----------
    seen_toc = False
    for p in doc.paragraphs:
        if p.text.strip().upper().startswith(toc_marker):
            seen_toc = True; continue
        if seen_toc and p.style.name.startswith('Heading'):
            p.paragraph_format.page_break_before = True
            break

    # ---------- header/footer ----------
    sec = doc.sections[0]
    hp = sec.header.paragraphs[0]; hp.text=''
    hp.alignment = WD_ALIGN_PARAGRAPH.CENTER
    set_run_font(hp.add_run(cfg['header']), size=7.5, italic=True, color=RGBColor(0x55,0x55,0x55))
    fp = sec.footer.paragraphs[0]; fp.text=''
    fp.alignment = WD_ALIGN_PARAGRAPH.CENTER
    set_run_font(fp.add_run(cfg['footer'] + "   |   Page "), size=7.5, color=RGBColor(0x55,0x55,0x55))
    set_run_font(field(fp,' PAGE '), size=7.5, color=RGBColor(0x55,0x55,0x55))
    set_run_font(fp.add_run(" of "), size=7.5, color=RGBColor(0x55,0x55,0x55))
    set_run_font(field(fp,' NUMPAGES '), size=7.5, color=RGBColor(0x55,0x55,0x55))

    doc.save(path)
    print("ok", path)

if __name__ == '__main__':
    main(json.loads(sys.argv[1]))
