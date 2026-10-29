# -*- coding: utf-8 -*-
import sys; sys.path.insert(0,'/workspace/work')
import dh
from dh import *
import agree_p1, agree_p2, agree_p3, agree_p4, agree_p5, agree_p6, agree_p7, agree_p8, agree_p9

doc = dh.new_doc()
dh.header_footer(doc,
    "Loan Agreement  —  Pinnacle Savings Bank, N.A. / Harborview Capital Partners LLC  —  CRE-2025-0342",
    "", "DRAFT — January 31, 2025 — Privileged & Confidential — Attorney Work Product")
for m in (agree_p1, agree_p2, agree_p3, agree_p4, agree_p5, agree_p6, agree_p7, agree_p8, agree_p9):
    m.build_part1(doc) if m is agree_p1 else None
for m in (agree_p2, agree_p3, agree_p4, agree_p5, agree_p6, agree_p7, agree_p8, agree_p9):
    func = [f for f in dir(m) if f.startswith("build_part")][0]
    getattr(m, func)(doc)
out = "/workspace/output/loan-agreement-draft.docx"
doc.save(out)
print("saved", out)
