# -*- coding: utf-8 -*-
import sys; sys.path.insert(0,'/workspace/work')
import dh
dh.FONT = "Times New Roman"
doc = dh.new_doc()
dh.header_footer(doc,
    "Cover Memorandum  —  Loan No. CRE-2025-0342  —  Privileged & Confidential",
    "", "Privileged & Confidential — Attorney Work Product")
import memo_p1, memo_p2, memo_p3, memo_p4
for m in (memo_p1, memo_p2, memo_p3, memo_p4):
    [f for f in dir(m) if f.startswith("build_p")] and getattr(m, [f for f in dir(m) if f.startswith("build_p")][0])(doc)
out = "/workspace/output/cover-memorandum.docx"
doc.save(out)
print("saved", out)
