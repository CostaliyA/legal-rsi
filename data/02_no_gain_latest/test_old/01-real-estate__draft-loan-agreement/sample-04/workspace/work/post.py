import sys, re
from docx import Document
from docx.shared import Pt, Inches, RGBColor, Emu
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

TOTAL_TWIPS = 9360  # 6.5 inches usable width

def set_cell_border(cell, sz=4, color="8C9AAB"):
    tcPr = cell._tc.get_or_add_tcPr()
    borders = tcPr.find(qn('w:tcBorders'))
    if borders is None:
        borders = OxmlElement('w:tcBorders'); tcPr.insert(0, borders)
    for edge in ('top','left','bottom','right'):
        el = borders.find(qn('w:'+edge))
        if el is None:
            el = OxmlElement('w:'+edge); borders.append(el)
        el.set(qn('w:val'),'single'); el.set(qn('w:sz'),str(sz))
        el.set(qn('w:space'),'0'); el.set(qn('w:color'),color)

def shade(cell, fill="DCE4EE"):
    tcPr = cell._tc.get_or_add_tcPr()
    sh = OxmlElement('w:shd'); sh.set(qn('w:val'),'clear'); sh.set(qn('w:color'),'auto'); sh.set(qn('w:fill'),fill)
    tcPr.append(sh)

def repeat_header(row):
    trPr = row._tr.get_or_add_trPr()
    el = OxmlElement('w:tblHeader'); el.set(qn('w:val'),'true'); trPr.append(el)

def cant_split(row):
    trPr = row._tr.get_or_add_trPr()
    el = OxmlElement('w:cantSplit'); el.set(qn('w:val'),'true'); trPr.append(el)

def col_metrics(table):
    ncols = len(table.columns)
    longest_tok = [6]*ncols
    max_len = [6]*ncols
    for c in range(ncols):
        for row in table.rows:
            cells = row.cells
            if c < len(cells):
                t = cells[c].text.strip()
                max_len[c] = max(max_len[c], len(t))
                for tok in t.split():
                    longest_tok[c] = max(longest_tok[c], len(tok))
    return longest_tok, max_len

def apply_widths(table):
    ncols = len(table.columns)
    lt, ml = col_metrics(table)
    # unbreakable minimum width per column (twips), two tiers
    def build(per_char, pad):
        return [lt[c]*per_char + pad for c in range(ncols)]
    for per_char, pad in ((105, 210), (95, 185), (88, 170), (80, 155)):
        mins = build(per_char, pad)
        if sum(mins) <= TOTAL_TWIPS:
            break
    total_min = sum(mins)
    if total_min >= TOTAL_TWIPS:
        scale = TOTAL_TWIPS/total_min
        widths = [int(m*scale) for m in mins]
    else:
        remaining = TOTAL_TWIPS - total_min
        extra_desire = [max(0, (ml[c]-lt[c])) for c in range(ncols)]
        tot_extra = sum(extra_desire)
        if tot_extra == 0:
            base = sum(mins)
            widths = [mins[c] + int(remaining*(mins[c]/base)) for c in range(ncols)]
        else:
            widths = [mins[c] + int(remaining*extra_desire[c]/tot_extra) for c in range(ncols)]
        diff = TOTAL_TWIPS - sum(widths)
        widths[widths.index(max(widths))] += diff
    tbl = table._tbl
    tblPr = tbl.tblPr
    for el in tblPr.findall(qn('w:tblW')):
        tblPr.remove(el)
    tw = OxmlElement('w:tblW'); tw.set(qn('w:w'), str(TOTAL_TWIPS)); tw.set(qn('w:type'),'dxa'); tblPr.append(tw)
    lay = OxmlElement('w:tblLayout'); lay.set(qn('w:type'),'fixed'); tblPr.append(lay)
    grid = tbl.find(qn('w:tblGrid'))
    if grid is not None:
        for gc in list(grid):
            grid.remove(gc)
        for width in widths:
            gc = OxmlElement('w:gridCol'); gc.set(qn('w:w'), str(width)); grid.append(gc)
    for row in table.rows:
        for j, cell in enumerate(row.cells):
            tcPr = cell._tc.get_or_add_tcPr()
            for el in tcPr.findall(qn('w:tcW')):
                tcPr.remove(el)
            tcw = OxmlElement('w:tcW'); tcw.set(qn('w:w'), str(widths[j])); tcw.set(qn('w:type'),'dxa')
            tcPr.insert(0, tcw)

def fmt_tables(doc):
    for t in doc.tables:
        t.alignment = WD_TABLE_ALIGNMENT.CENTER
        t.autofit = False
        apply_widths(t)
        tblPr = t._tbl.tblPr
        mar = OxmlElement('w:tblCellMar')
        for side,val in (('top',40),('bottom',40),('left',80),('right',80)):
            e = OxmlElement('w:'+side); e.set(qn('w:w'),str(val)); e.set(qn('w:type'),'dxa'); mar.append(e)
        tblPr.append(mar)
        for i,row in enumerate(t.rows):
            cant_split(row)
            if i==0: repeat_header(row)
            for j,cell in enumerate(row.cells):
                set_cell_border(cell)
                if i==0: shade(cell)
                for p in cell.paragraphs:
                    p.paragraph_format.space_after = Pt(1)
                    p.paragraph_format.space_before = Pt(1)
                    p.paragraph_format.line_spacing = 1.0
                    if i==0:
                        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                    for r in p.runs:
                        r.font.size = Pt(8)
                        r.font.name='Times New Roman'
                        if i==0: r.font.bold = True
        # keep table with preceding heading
        # add small spacer after table
        p = OxmlElement('w:p')
        t._tbl.addnext(p)

def add_running_header(doc, right_text):
    for sec in doc.sections:
        hdr = sec.header
        hdr.is_linked_to_previous = False
        p = hdr.paragraphs[0]
        p.text = ""
        p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        r = p.add_run(right_text)
        r.font.size = Pt(7.5); r.font.name='Times New Roman'; r.font.color.rgb = RGBColor(0x66,0x66,0x66)
        pPr = p._p.get_or_add_pPr()
        pbdr = OxmlElement('w:pBdr'); b = OxmlElement('w:bottom')
        b.set(qn('w:val'),'single'); b.set(qn('w:sz'),'4'); b.set(qn('w:space'),'2'); b.set(qn('w:color'),'AAAAAA')
        pbdr.append(b); pPr.append(pbdr)

src, dst, header_text = sys.argv[1], sys.argv[2], sys.argv[3]
doc = Document(src)
fmt_tables(doc)
add_running_header(doc, header_text)
doc.save(dst)
print("ok", dst, "tables:", len(doc.tables))
