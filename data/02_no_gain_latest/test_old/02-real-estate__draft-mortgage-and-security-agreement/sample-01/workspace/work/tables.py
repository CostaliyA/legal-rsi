from docx.oxml.ns import qn
from docx.oxml import OxmlElement
from docx.shared import Pt, Inches

def set_table_layout(table, widths_in, font_pt=9.0):
    tbl = table._tbl
    tblPr = tbl.tblPr
    # fixed layout
    for el in tblPr.findall(qn('w:tblLayout')): tblPr.remove(el)
    layout = OxmlElement('w:tblLayout'); layout.set(qn('w:type'),'fixed'); tblPr.append(layout)
    # total width 100%
    for el in tblPr.findall(qn('w:tblW')): tblPr.remove(el)
    w = OxmlElement('w:tblW'); w.set(qn('w:w'),'9720'); w.set(qn('w:type'),'dxa'); tblPr.append(w)
    # grid
    grid = tbl.find(qn('w:tblGrid'))
    if grid is not None:
        cols = grid.findall(qn('w:gridCol'))
        for i, gc in enumerate(cols):
            if i < len(widths_in):
                gc.set(qn('w:w'), str(int(widths_in[i]*1440)))
    for row in table.rows:
        for i, cell in enumerate(row.cells):
            if i < len(widths_in):
                cell.width = Inches(widths_in[i])
            for p in cell.paragraphs:
                pf = p.paragraph_format
                pf.space_before = Pt(1.5); pf.space_after = Pt(1.5)
                for r in p.runs:
                    r.font.size = Pt(font_pt)
    # cell margins
    for el in tblPr.findall(qn('w:tblCellMar')): tblPr.remove(el)
    mar = OxmlElement('w:tblCellMar')
    for side, val in (('top',30),('left',70),('bottom',30),('right',70)):
        e = OxmlElement(f'w:{side}'); e.set(qn('w:w'),str(val)); e.set(qn('w:type'),'dxa'); mar.append(e)
    tblPr.append(mar)
