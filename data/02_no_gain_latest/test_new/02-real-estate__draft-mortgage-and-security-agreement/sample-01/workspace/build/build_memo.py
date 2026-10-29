import subprocess, sys, json, re, os
from pathlib import Path
from docx import Document
from docx.shared import Pt, Inches, RGBColor, Emu
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_TAB_ALIGNMENT, WD_TAB_LEADER, WD_BREAK
from docx.enum.section import WD_SECTION
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

PARTS = ["memo_00.md","memo_01.md","memo_02.md","memo_03.md","memo_04.md"]
TOC_ITEMS = [
    ("1.","1. PURPOSE, SCOPE AND SUMMARY OF CONCLUSIONS"),
    ("2.","2. SOURCE INVENTORY AND METHODOLOGY"),
    ("3.","3. EXECUTIVE SUMMARY — TOP-RISK REGISTER"),
    ("4.","4. CREDIT CAPACITY, VALUATION AND LOAN SIZING"),
    ("5.","5. TITLE, SURVEY AND COLLATERAL ISSUES"),
    ("6.","6. ENTITY AUTHORITY AND SINGLE-PURPOSE ENTITY ISSUES"),
    ("7.","7. LOAN TERMS REQUIRING PRECISION"),
    ("8.","8. RENOVATION AND CONSTRUCTION ISSUES"),
    ("9.","9. FIGURE RECONCILIATION SUMMARY"),
    ("10.","10. DRAFTING DECISIONS AND PROVISIONS ADDED BEYOND THE TERM SHEET"),
    ("11.","11. OPEN ITEMS, MISSING DOCUMENTS AND INFORMATION REQUESTS"),
    ("12.","12. BLANKS AND BRACKETED ITEMS IN THE DRAFT"),
    ("13.","13. RECOMMENDED NEXT STEPS"),
    ("14.","14. LIMITATIONS"),
    ("APPENDIX","APPENDIX A — RESPONSE TO THE MARKUP NOTES OF MARCH 18, 2025"),
]

def build_md(toc_pages):
    out = []
    for p in PARTS:
        out.append(Path(p).read_text())
    md = "\n".join(out)
    if toc_pages is None:
        lines = "\n\n".join(["x" for _ in TOC_ITEMS])
    else:
        lines = "\n\n".join(f"{label}\x09{pg}" for key,label in TOC_ITEMS for pg in [toc_pages.get(key,"")])
    md = md.replace("TOC_PLACEHOLDER", lines)
    Path("mcombined.md").write_text(md)
    return md

def set_font(run, name="Times New Roman", size=None, bold=None, italic=None, caps=False):
    run.font.name = name
    rpr = run._element.get_or_add_rPr()
    rf = rpr.find(qn('w:rFonts'))
    if rf is None:
        rf = OxmlElement('w:rFonts'); rpr.append(rf)
    for a in ('w:ascii','w:hAnsi','w:cs','w:eastAsia'):
        rf.set(qn(a), name)
    if size is not None: run.font.size = Pt(size)
    if bold is not None: run.font.bold = bold
    if italic is not None: run.font.italic = italic
    if caps: run.font.all_caps = True

def add_field(paragraph, instr):
    r = paragraph.add_run()
    fld = OxmlElement('w:fldChar'); fld.set(qn('w:fldCharType'),'begin')
    r._element.append(fld)
    r2 = paragraph.add_run()
    it = OxmlElement('w:instrText'); it.set(qn('xml:space'),'preserve'); it.text = instr
    r2._element.append(it)
    r3 = paragraph.add_run()
    fld2 = OxmlElement('w:fldChar'); fld2.set(qn('w:fldCharType'),'separate')
    r3._element.append(fld2)
    r4 = paragraph.add_run("1")
    r5 = paragraph.add_run()
    fld3 = OxmlElement('w:fldChar'); fld3.set(qn('w:fldCharType'),'end')
    r5._element.append(fld3)
    for rr in (r,r2,r3,r4,r5):
        set_font(rr, size=8.5)

def para(doc, text="", size=11, bold=False, italic=False, align=None, space_before=0, space_after=0, keep=False, caps=False):
    p = doc.add_paragraph()
    if align is not None: p.alignment = align
    pf = p.paragraph_format
    pf.space_before = Pt(space_before); pf.space_after = Pt(space_after)
    pf.line_spacing = 1.0
    if keep: pf.keep_with_next = True
    if text:
        r = p.add_run(text); set_font(r, size=size, bold=bold, italic=italic, caps=caps)
    return p

def insert_before(doc, new_elements, ref_element):
    for el in new_elements:
        ref_element.addprevious(el)

def build(toc_pages, out_path):
    build_md(toc_pages)
    subprocess.run(["pandoc","-f","markdown-tex_math_dollars","-t","docx","mcombined.md","-o","mbody.docx"], check=True)
    doc = Document("mbody.docx")

    # page setup
    for s in doc.sections:
        s.page_width = Inches(8.5); s.page_height = Inches(11)
        s.left_margin = Inches(1.0); s.right_margin = Inches(1.0)
        s.top_margin = Inches(1.0); s.bottom_margin = Inches(1.0)
        s.different_first_page_header_footer = True

    # base styles
    st = doc.styles['Normal']
    st.font.name = 'Times New Roman'; st.font.size = Pt(11)
    st.paragraph_format.space_after = Pt(6)
    st.paragraph_format.line_spacing = 1.05
    st.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    rpr = st.element.get_or_add_rPr()
    rf = OxmlElement('w:rFonts')
    for a in ('w:ascii','w:hAnsi','w:cs','w:eastAsia'): rf.set(qn(a),'Times New Roman')
    rpr.append(rf)

    for name, size, before, after in (('Heading 1',12,20,10),('Title',20,0,12)):
        try:
            h = doc.styles[name]
        except KeyError:
            continue
        h.font.name='Times New Roman'; h.font.size=Pt(size); h.font.bold=True
        h.font.color.rgb = RGBColor(0,0,0)
        h.paragraph_format.space_before=Pt(before); h.paragraph_format.space_after=Pt(after)
        h.paragraph_format.keep_with_next=True
        h.paragraph_format.alignment=WD_ALIGN_PARAGRAPH.LEFT
        h.paragraph_format.line_spacing=1.0

    # body tweaks: heading paragraphs, subparagraph indents, TOC
    body = doc.element.body
    for p in doc.paragraphs:
        style = p.style.name if p.style is not None else ""
        if style == 'Heading 1':
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT
            for r in p.runs: set_font(r, size=12, bold=True)
            # all caps headings
            txt = p.text.strip().upper()
            if p.text.strip() != txt and p.runs:
                p.runs[0].text = txt
                for r in p.runs[1:]: r.text = ""
            # page break before Exhibits and Signature
        txt = p.text.strip()
        if txt.startswith("(") and len(txt) > 2 and txt[2:3] == ")" and style=="Body Text":
            p.paragraph_format.left_indent = Inches(0.35)
            p.paragraph_format.first_line_indent = Inches(-0.0)
        # left-align signature, notary and form-field lines
        LEFT_PREFIXES = ("By:", "Name:", "Title:", "Date:", "Architect:", "SC License", "I, the undersigned",
                         "WITNESS my hand", "STATE OF SOUTH CAROLINA", "COUNTY OF CHARLESTON", "(SEAL)",
                         "My Commission", "Neil Ashford Graydon, individually", "PALMETTO GATEWAY PARTNERS LLC",
                         "CALVERLEY HERITAGE BANK", "GRAYDON DEVELOPMENT GROUP LLC")
        if txt.startswith(LEFT_PREFIXES) or (txt.startswith("____")):
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT

    # tables: grid + small font + computed widths
    for tbl in doc.tables:
        try:
            tbl.style = doc.styles['Table Grid']
        except Exception:
            pass
        for row in tbl.rows:
            for cell in row.cells:
                for p in cell.paragraphs:
                    p.paragraph_format.space_after = Pt(2)
                    p.paragraph_format.space_before = Pt(2)
                    p.paragraph_format.line_spacing = 1.0
                    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
                    for r in p.runs: set_font(r, size=8.5)
        # tighten cell margins
        tblPr = tbl._tbl.tblPr
        mar = OxmlElement('w:tblCellMar')
        for side in ('left','right'):
            el = OxmlElement('w:'+side); el.set(qn('w:w'),'58'); el.set(qn('w:type'),'dxa'); mar.append(el)
        tblPr.append(mar)
        if tbl.rows:
            for cell in tbl.rows[0].cells:
                for p in cell.paragraphs:
                    for r in p.runs: r.font.bold = True
            trPr = tbl.rows[0]._tr.get_or_add_trPr()
            th = OxmlElement('w:tblHeader'); th.set(qn('w:val'), 'true'); trPr.append(th)
        # widths
        try:
            ncols = len(tbl.columns)
            tbl.autofit = False
            weights = []
            for ci in range(ncols):
                mx = 1
                for row in tbl.rows:
                    cells = row.cells
                    if ci < len(cells):
                        for word in cells[ci].text.split():
                            mx = max(mx, len(word))
                weights.append(max(3, min(mx, 20) + 2))
            tot = sum(weights)
            avail = 6.5
            widths = [max(0.5, avail * w / tot) for w in weights]
            scale = avail / sum(widths)
            widths = [Inches(w * scale) for w in widths]
            for row in tbl.rows:
                for ci, cell in enumerate(row.cells):
                    if ci < len(widths):
                        cell.width = widths[ci]
            # enforce grid widths and fixed layout so rendering honours the widths
            grid = tbl._tbl.find(qn('w:tblGrid'))
            if grid is not None:
                for gc, w in zip(grid.findall(qn('w:gridCol')), widths):
                    gc.set(qn('w:w'), str(int(w.twips)))
            tblPr2 = tbl._tbl.tblPr
            for el in tblPr2.findall(qn('w:tblLayout')):
                tblPr2.remove(el)
            lay = OxmlElement('w:tblLayout'); lay.set(qn('w:type'), 'fixed'); tblPr2.append(lay)
            for el in tblPr2.findall(qn('w:tblW')):
                tblPr2.remove(el)
            tw = OxmlElement('w:tblW'); tw.set(qn('w:w'), str(int(sum(w.twips for w in widths)))); tw.set(qn('w:type'), 'dxa'); tblPr2.append(tw)
        except Exception as e:
            print("width warn", e)

    # TOC styling: paragraphs following the 'TABLE OF CONTENTS' heading up to the page break
    paras = doc.paragraphs
    ti = None
    for i, p in enumerate(paras):
        if p.text.strip() == "CONTENTS":
            ti = i
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            for r in p.runs: set_font(r, size=13, bold=True)
            break
    if ti is not None:
        anchor = None
        for p in paras[ti+1:]:
            if p._p.findall('.//' + qn('w:br')):
                anchor = p._p
                break
            anchor = None
        if anchor is None:
            anchor = paras[ti]._p
            # page-break paragraph not found; append at end of that paragraph's parent
        # remove existing placeholder paragraphs
        for p in paras[ti+1:]:
            if p._p is anchor:
                break
            p._p.getparent().remove(p._p)
        # build entries
        for key, label in TOC_ITEMS:
            np = doc.add_paragraph()
            pf = np.paragraph_format
            pf.left_indent = Inches(0.0)
            pf.space_before = Pt(0)
            pf.space_after = Pt(5)
            pf.line_spacing = 1.0
            pf.right_indent = Inches(0.0)
            pf.tab_stops.add_tab_stop(Inches(6.5), WD_TAB_ALIGNMENT.RIGHT, WD_TAB_LEADER.DOTS)
            np.alignment = WD_ALIGN_PARAGRAPH.LEFT
            r1 = np.add_run(label); set_font(r1, size=10)
            rt = np.add_run(); set_font(rt, size=10)
            rt._element.append(OxmlElement('w:tab'))
            pg = "" if toc_pages is None else str(toc_pages.get(key, ""))
            r2 = np.add_run(pg); set_font(r2, size=10)
            anchor.addprevious(np._p)

    # ---- header / footer
    sec = doc.sections[0]
    hdr = sec.header
    hp = hdr.paragraphs[0]
    hp.text = ""
    hp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    hr = hp.add_run("PRIVILEGED AND CONFIDENTIAL — ATTORNEY WORK PRODUCT — Fielding, Ashworth & Cole LLP")
    set_font(hr, size=8, italic=True)

    ftr = sec.footer
    fp = ftr.paragraphs[0]
    fp.text = ""
    fp.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = fp.add_run("Page "); set_font(r, size=8.5)
    add_field(fp, " PAGE ")
    r = fp.add_run(" of "); set_font(r, size=8.5)
    add_field(fp, " NUMPAGES ")

    # ensure first page different (blank)
    sec.different_first_page_header_footer = True
    if sec.first_page_footer is not None:
        for p in sec.first_page_footer.paragraphs: p.text = ""
    doc.save(out_path)
    print("saved", out_path)

if __name__ == "__main__":
    tp = None
    out = "m1.docx"
    if len(sys.argv) > 1:
        tp = json.loads(Path(sys.argv[1]).read_text())
        out = sys.argv[2] if len(sys.argv)>2 else "pass2.docx"
    build(tp, out)
