import subprocess, sys, json, re, os
from pathlib import Path
from docx import Document
from docx.shared import Pt, Inches, RGBColor, Emu
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_TAB_ALIGNMENT, WD_TAB_LEADER, WD_BREAK
from docx.enum.section import WD_SECTION
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

PARTS = ["mtg_00.md","mtg_01.md","mtg_02.md","mtg_03.md","mtg_04.md","mtg_05.md"]
TOC_ITEMS = [
    ("RECITALS","RECITALS"),
    ("ARTICLE 1","ARTICLE 1 — DEFINITIONS AND RULES OF CONSTRUCTION"),
    ("ARTICLE 2","ARTICLE 2 — THE LOAN, THE NOTE AND PAYMENT TERMS"),
    ("ARTICLE 3","ARTICLE 3 — GRANT OF MORTGAGE; SECURITY INTEREST; COLLATERAL"),
    ("ARTICLE 4","ARTICLE 4 — ABSOLUTE ASSIGNMENT OF LEASES AND RENTS"),
    ("ARTICLE 5","ARTICLE 5 — REPRESENTATIONS AND WARRANTIES"),
    ("ARTICLE 6","ARTICLE 6 — AFFIRMATIVE COVENANTS"),
    ("ARTICLE 7","ARTICLE 7 — NEGATIVE COVENANTS; SINGLE-PURPOSE ENTITY"),
    ("ARTICLE 8","ARTICLE 8 — RENOVATION AND CONSTRUCTION"),
    ("ARTICLE 9","ARTICLE 9 — INSURANCE"),
    ("ARTICLE 10","ARTICLE 10 — RESERVES AND ESCROWS"),
    ("ARTICLE 11","ARTICLE 11 — ENVIRONMENTAL MATTERS AND THE LAND USE RESTRICTION"),
    ("ARTICLE 12","ARTICLE 12 — FINANCIAL COVENANTS AND REPORTING"),
    ("ARTICLE 13","ARTICLE 13 — PREPAYMENT"),
    ("ARTICLE 14","ARTICLE 14 — EVENTS OF DEFAULT AND REMEDIES"),
    ("ARTICLE 15","ARTICLE 15 — CASUALTY AND CONDEMNATION"),
    ("ARTICLE 16","ARTICLE 16 — GUARANTOR; NON-RECOURSE; LIMITATION OF LIABILITY"),
    ("ARTICLE 17","ARTICLE 17 — MISCELLANEOUS"),
    ("SIGNATURE","SIGNATURE PAGE"),
    ("NOTARY","NOTARY ACKNOWLEDGMENT"),
    ("# EXHIBIT A","EXHIBIT A — LEGAL DESCRIPTION OF THE PROPERTY"),
    ("# EXHIBIT B","EXHIBIT B — RENT ROLL AND LEASE SUMMARY AS OF THE CLOSING DATE"),
    ("# EXHIBIT C","EXHIBIT C — PERMITTED EXCEPTIONS"),
    ("# EXHIBIT D","EXHIBIT D — RENOVATION BUDGET SUMMARY"),
    ("# EXHIBIT E","EXHIBIT E — FORM OF DRAW REQUEST AND ARCHITECT'S CERTIFICATE"),
    ("# EXHIBIT F","EXHIBIT F — FORM OF ANNUAL LAND USE RESTRICTION COMPLIANCE CERTIFICATE"),
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
    Path("combined.md").write_text(md)
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
    subprocess.run(["pandoc","-f","markdown-tex_math_dollars","-t","docx","combined.md","-o","body.docx"], check=True)
    doc = Document("body.docx")

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
        if p.text.strip() == "TABLE OF CONTENTS":
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

    # ---- cover page: build paragraphs and move to front
    tmp = []
    def cp(text="", size=11, bold=False, italic=False, after=0):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        pf = p.paragraph_format
        pf.space_before = Pt(0); pf.space_after = Pt(after); pf.line_spacing = 1.0
        if text:
            r = p.add_run(text); set_font(r, size=size, bold=bold, italic=italic)
        tmp.append(p)

    cp("", after=0)
    cp("", after=0)
    cp("MORTGAGE AND SECURITY AGREEMENT", size=22, bold=True, after=6)
    cp("(With Absolute Assignment of Leases and Rents)", size=12, italic=True, after=30)
    cp("by and from", size=11, italic=True, after=10)
    cp("PALMETTO GATEWAY PARTNERS LLC", size=13, bold=True, after=2)
    cp("a South Carolina limited liability company", size=11, after=10)
    cp("as Borrower and Mortgagor", size=11, italic=True, after=16)
    cp("to", size=11, italic=True, after=16)
    cp("CALVERLEY HERITAGE BANK", size=13, bold=True, after=2)
    cp("a Georgia state-chartered commercial bank", size=11, after=10)
    cp("as Lender and Mortgagee", size=11, italic=True, after=30)
    cp("Dated as of April 15, 2025", size=12, bold=True, after=30)
    cp("Property: 520–534 King Street, Charleston, South Carolina 29403", size=10.5, after=2)
    cp("Tax Map Nos. 460-12-04-007, 460-12-04-008 and 460-12-04-009,", size=10.5, after=2)
    cp("together with the vacated Anson Lane strip, Charleston County, South Carolina", size=10.5, after=14)
    cp("Principal Amount Secured: $14,750,000.00", size=12, bold=True, after=2)
    cp("(including future advances of the Renovation Holdback)", size=10.5, italic=True, after=26)
    cp("RECORDING INFORMATION", size=10.5, bold=True, after=2)
    cp("To be recorded in the Office of the Register of Mesne Conveyances for Charleston County, South Carolina.", size=10, after=10)
    cp("AFTER RECORDING, RETURN TO: Fielding, Ashworth & Cole LLP, Charleston, South Carolina, Attn: Catherine Ashworth, Partner", size=10, after=10)
    cp("PREPARED BY: Fielding, Ashworth & Cole LLP, counsel for Lender", size=10, after=26)
    cp("DRAFT — MARCH 27, 2025 — PRIVILEGED AND CONFIDENTIAL — SUBJECT TO REVIEW AND COMMENT", size=9.5, bold=True, after=0)

    # page break paragraph at end of cover
    pb = doc.add_paragraph()
    pb.add_run().add_break(WD_BREAK.PAGE)
    tmp.append(pb)

    first = body[0]
    for el in tmp:
        first.addprevious(el._p)

    # ---- header / footer
    sec = doc.sections[0]
    hdr = sec.header
    hp = hdr.paragraphs[0]
    hp.text = ""
    hp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    hr = hp.add_run("Mortgage and Security Agreement — CHB / Palmetto Gateway Partners LLC — DRAFT 03/27/2025")
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
    out = "pass1.docx"
    if len(sys.argv) > 1:
        tp = json.loads(Path(sys.argv[1]).read_text())
        out = sys.argv[2] if len(sys.argv)>2 else "pass2.docx"
    build(tp, out)
