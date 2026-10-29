import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from helpers import *
import content_a, content_b, content_c, content_d, content_e, content_f, content_g

doc = new_doc()
header_footer(doc,
    "Ground Lease Agreement  •  City of Port Calloway Redevelopment Authority / Meridian Gateway Holdings LLC",
    footer_left="DRAFT 6/20/2025 — Privileged & Confidential — Attorney Work Product — Not for Execution")
set_core(doc,
    title="Ground Lease Agreement — 10–30 Pier Street, Port Calloway, CT",
    subject="Long-Term Ground Lease (99 years) — Tenant draft",
    author="Hargrove & Linden LLP (Tenant's Counsel)",
    comments="DRAFT of June 20, 2025. Privileged and confidential; attorney work product. Prepared on behalf of Meridian Gateway Holdings LLC as Tenant.")

for mod in (content_a, content_b, content_c, content_d, content_e, content_f, content_g):
    mod.blocks(doc)

out = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "output", "ground-lease-agreement.docx")
doc.save(out)
print("saved", out)
