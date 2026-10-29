import docx, sys
from docx.shared import Inches, Pt
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
from docx.enum.table import WD_ALIGN_VERTICAL

def fix(path, specs):
    d = docx.Document(path)
    for i, t in enumerate(d.tables):
        w = specs[i]
        tbl = t._tbl
        grid = tbl.find(qn('w:tblGrid'))
        for gc, width in zip(grid.findall(qn('w:gridCol')), w):
            gc.set(qn('w:w'), str(int(width*1440)))
        tblPr = tbl.tblPr
        lay = tblPr.find(qn('w:tblLayout'))
        if lay is None:
            lay = OxmlElement('w:tblLayout'); tblPr.append(lay)
        lay.set(qn('w:type'),'fixed')
        tw = tblPr.find(qn('w:tblW'))
        if tw is not None:
            tw.set(qn('w:w'), str(int(sum(w)*1440))); tw.set(qn('w:type'),'dxa')
        for row in t.rows:
            for cell, width in zip(row.cells, w):
                cell.width = Inches(width)
                cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
    d.save(path)
    print("tables fixed in", path)

if __name__ == "__main__":
    # mortgage: table0 budget, table1 rent roll
    fix("output/mortgage-and-security-agreement.docx", [[0.7,2.2,1.2,1.2,1.2],[0.85,0.55,1.55,0.8,0.7,0.75,0.7,0.65]])
