import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from memo_helpers import *
import memo_a, memo_b, memo_c, memo_d, memo_e, memo_f, memo_g

doc = memo_doc()
s = doc.sections[0]
s.top_margin = Inches(0.85); s.bottom_margin = Inches(0.8)
header_footer(doc, "Hargrove & Linden LLP  •  Privileged & Confidential  •  Attorney Work Product",
              footer_left="Drafting Issues Memorandum — Ground Lease, 10–30 Pier Street — June 20, 2025")
set_core(doc,
    title="Drafting Issues Memorandum — Ground Lease, 10–30 Pier Street, Port Calloway, CT",
    subject="Source-grounded review of Term Sheet, Bayside loan term sheet, Title Commitment, Phase II ESA, survey and Board Resolution",
    author="Hargrove & Linden LLP (Tenant's Counsel)",
    comments="PRIVILEGED AND CONFIDENTIAL — ATTORNEY WORK PRODUCT. June 20, 2025.")

for mod in (memo_a, memo_b, memo_c, memo_d, memo_e, memo_f, memo_g):
    mod.blocks(doc)

out = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "output", "drafting-issues-memo.docx")
doc.save(out)
print("saved", out)
