import docx
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

d = docx.Document('build/memo_raw.docx')

def bottom_border(p):
    pPr = p._p.get_or_add_pPr()
    pbdr = OxmlElement('w:pBdr')
    for edge, sz in (('top','6'),('bottom','6')):
        e = OxmlElement('w:'+edge)
        e.set(qn('w:val'),'single'); e.set(qn('w:sz'),sz); e.set(qn('w:space'),'4'); e.set(qn('w:color'),'888888')
        pbdr.append(e)
    pPr.append(pbdr)

first_h1 = True
first_h2 = True
for p in d.paragraphs:
    t = p.text.strip()
    st = p.style.name
    if st == 'Heading 1' and first_h1:
        first_h1 = False
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(2)
        for r in p.runs:
            r.font.size = Pt(14); r.font.bold = True
            rPr = r._element.get_or_add_rPr()
            sp = OxmlElement('w:spacing'); sp.set(qn('w:val'), '30'); rPr.append(sp)
        continue
    if t.startswith('411 South Tryon'):
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_after = Pt(14)
        for r in p.runs: r.font.size = Pt(9)
        continue
    if t.startswith('PRIVILEGED AND CONFIDENTIAL'):
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_before = Pt(4)
        p.paragraph_format.space_after = Pt(16)
        for r in p.runs: r.font.size = Pt(7.5); r.font.bold = True
        bottom_border(p)
        continue
    if t.startswith('Item M-') and len(t) < 160:
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        p.paragraph_format.space_before = Pt(12)
        p.paragraph_format.space_after = Pt(3)
        p.paragraph_format.keep_with_next = True
        for r in p.runs: r.font.size = Pt(11); r.font.bold = True
        continue
    if st == 'Heading 2':
        if first_h2:
            first_h2 = False
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p.paragraph_format.space_before = Pt(6)
            p.paragraph_format.space_after = Pt(14)
            for r in p.runs: r.font.size = Pt(12.5)
            continue
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        p.paragraph_format.space_before = Pt(16)
        p.paragraph_format.space_after = Pt(6)
        for r in p.runs: r.font.size = Pt(11.5)
        continue
    if st == 'Heading 3':
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        p.paragraph_format.space_before = Pt(12)
        p.paragraph_format.space_after = Pt(4)
        for r in p.runs: r.font.size = Pt(10.5); r.font.italic = False
        continue
    if t.startswith(('TO:','FROM:','DATE:','RE:','ENCLOSURE:')):
        p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
        p.paragraph_format.space_after = Pt(8)
        continue

# suppress running header on page 1
sec = d.sections[0]
sec.different_first_page_header_footer = True
from docx.oxml import OxmlElement as OE
from docx.oxml.ns import qn as Q
fp = sec.first_page_footer.paragraphs[0]
fp.text = ''
fp.alignment = WD_ALIGN_PARAGRAPH.CENTER
def _fld(par, code):
    run = par.add_run()
    a = OE('w:fldChar'); a.set(Q('w:fldCharType'),'begin')
    b = OE('w:instrText'); b.set(Q('xml:space'),'preserve'); b.text = code
    c = OE('w:fldChar'); c.set(Q('w:fldCharType'),'end')
    run._r.append(a); run._r.append(b); run._r.append(c)
    return run
r = fp.add_run("Page "); r.font.size = Pt(7.5)
f = _fld(fp, ' PAGE '); f.font.size = Pt(7.5)
r = fp.add_run(" of "); r.font.size = Pt(7.5)
f = _fld(fp, ' NUMPAGES '); f.font.size = Pt(7.5)

# table refinements
five = [t for t in d.tables if len(t.columns) == 5]
widths_sets = [[0.55,1.45,1.45,1.95,1.10],[1.15,1.55,1.55,1.10,1.15]]
for i,tb in enumerate(five):
    w = widths_sets[i] if i < len(widths_sets) else [1.3]*5
    for j,c in enumerate(tb.columns):
        c.width = Inches(w[j])
    for row in tb.rows:
        for j,cell in enumerate(row.cells):
            cell.width = Inches(w[j])
for tb in d.tables:
    for row in tb.rows:
        trPr = row._tr.get_or_add_trPr()
        el = OxmlElement('w:cantSplit'); el.set(qn('w:val'),'true'); trPr.append(el)

d.save('build/memo_raw.docx')
print('memo post ok')
