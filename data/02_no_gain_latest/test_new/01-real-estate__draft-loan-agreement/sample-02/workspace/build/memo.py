# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, "/workspace/build")
from docxhelp import *
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

RED = RGBColor(0x8B,0x1A,0x1A)

doc = new_doc(1.0)
header_footer(doc,
    "PRIVILEGED AND CONFIDENTIAL — ATTORNEY WORK PRODUCT",
    "Memorandum to Pinnacle Savings Bank, N.A. — CRE-2025-0342")

para(doc, "ASHFORD, CROMDALE CONSULTING & LAINE LLP", size=12, bold=True, align="center", space_after=0)
para(doc, "411 South Tryon Street, Suite 2800 · Charlotte, North Carolina 28202", size=9, align="center", space_after=2)
para(doc, "Counsel to Pinnacle Savings Bank, N.A.", size=9, italic=True, align="center", space_after=18)

p = doc.add_paragraph()
p.paragraph_format.space_after = Pt(14)
r = p.add_run("PRIVILEGED AND CONFIDENTIAL — ATTORNEY WORK PRODUCT — ATTORNEY-CLIENT COMMUNICATION")
r.bold = True; r.font.size = Pt(7.5); r.font.name = FONT; r.font.color.rgb = RED
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
pPr = p._p.get_or_add_pPr()
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
pbdr = OxmlElement("w:pBdr")
for side in ("top","bottom"):
    el = OxmlElement(f"w:{side}")
    el.set(qn("w:val"),"single"); el.set(qn("w:sz"),"8"); el.set(qn("w:space"),"4"); el.set(qn("w:color"),"8B1A1A")
    pbdr.append(el)
pPr.append(pbdr)

para(doc, "MEMORANDUM", size=16, bold=True, align="center", space_after=16)

HD = [
 ("TO:", "David Forsythe, Senior Vice President, Commercial Real Estate Lending;\nSenior Loan Committee, Pinnacle Savings Bank, N.A."),
 ("FROM:", "Katharine “Kate” Drummond, Partner; Marcus Webb, Associate\nAshford, Cromdale Consulting & Laine LLP"),
 ("DATE:", "February 3, 2025"),
 ("RE:", "The Piedmont at Brightleaf — Construction-to-Mini-Permanent Loan (Loan No. CRE-2025-0342)\n"
         "Transmittal of draft Loan Agreement and report of material issues and inconsistencies in the source documents"),
 ("ENCLOSURES:", "(1) Construction-to-Mini-Permanent Loan Agreement (draft dated February 3, 2025)\n"
                 "(2) This memorandum"),
]
t = doc.add_table(rows=0, cols=2)
t.autofit = False
t.style = "Normal Table"
for k, v in HD:
    cells = t.add_row().cells
    cells[0].width = Inches(1.25); cells[1].width = Inches(5.25)
    p0 = cells[0].paragraphs[0]; p0.paragraph_format.space_after = Pt(4)
    r0 = p0.add_run(k); r0.bold = True; r0.font.size = Pt(9.5); r0.font.name = FONT
    p1 = cells[1].paragraphs[0]; p1.paragraph_format.space_after = Pt(4)
    r1 = p1.add_run(v); r1.font.size = Pt(9.5); r1.font.name = FONT
set_col_widths(t, [1.3, 5.2])

# bottom rule under the memo block
para(doc, "", space_after=2)
p = doc.add_paragraph()
p.paragraph_format.space_after = Pt(12)
pPr = p._p.get_or_add_pPr()
pbdr = OxmlElement("w:pBdr")
el = OxmlElement("w:bottom")
el.set(qn("w:val"),"single"); el.set(qn("w:sz"),"12"); el.set(qn("w:space"),"1"); el.set(qn("w:color"),"000000")
pbdr.append(el); pPr.append(pbdr)

# ------------------------------------------------------------------ 1
heading1(doc, "1.  Purpose, Scope and Documents Reviewed", before=6, after=8, size=12)
rich(doc, [("This memorandum transmits our draft of the Construction-to-Mini-Permanent Loan Agreement (the “Draft Agreement”) for the "
            "above-referenced facility and reports the material issues and inconsistencies we identified across the source documents "
            "furnished to us. It is written for the Bank’s internal credit and legal functions, is subject to the attorney-client "
            "privilege and is not to be delivered to Borrower, the Guarantors, the Mezzanine Lender or any third party.")],
     first_indent=0.5)
rich(doc, [("We reviewed each of the seven source documents listed below in full, treating the economic terms of the Term Sheet as "
            "controlling except to the extent Sections 22 and 23 make it binding. We recomputed every ratio, total, date interval and draw amount in the record rather than adopting the "
            "stated figures; the results appear in Section 8. Where a source document conflicts with another, we have identified the "
            "conflict, indicated which document we consider controlling and stated why, and recommended a resolution. We have not resolved "
            "any conflict by assumption: each open item appears in the Draft Agreement in bracketed form, is listed on Exhibit H to the "
            "Draft Agreement and is cross-referenced in this memorandum.")],
     first_indent=0.5)

heading2(doc, "1.1  Source Inventory", before=12, after=8, size=10.5)
SRC = [
["Ref.", "Document", "Date / Identifier", "Role in the file", "Reliability assessment"],
["S-1", "Executed Term Sheet (non-binding except §§ 22–23)", "January 10, 2025; Loan No. CRE-2025-0342", "Governing commercial terms", "Executed by Borrower and Lender; controls the economic terms. Contains internal drafting defects (Section 3.10 below)."],
["S-2", "Senior Loan Committee Credit Memorandum", "January 22, 2025", "Internal credit approval and conditions of approval", "Approved recommendation; contains arithmetic and characterization errors (Sections 3.2, 3.4, 6.1)."],
["S-3", "Appraisal — Executive Summary (self-contained report, 187 pp.)", "Ridgeline Appraisal Services Inc.; Linda M. Haverford, MAI; November 15, 2024; File RAS-2024-1147", "Valuation and stabilized NOI", "USPAP/FIRREA compliant on its face. Operating expenses omit the Declaration assessment; states facts that conflict with S-4 (Section 4.4)."],
["S-4", "Preliminary Title Commitment", "Aldersgate Title & Escrow Inc.; No. NC-2024-88712; effective December 5, 2024; expires June 5, 2025", "Title, vesting, legal descriptions, exceptions", "Primary record evidence for vesting and encumbrances. Legal descriptions do not close (Section 4.2); no environmental land use restriction disclosed (Section 3.5)."],
["S-5", "Phase I Environmental Site Assessment — excerpted sections", "Sentinel Environmental Consulting LLC; Dr. James Whitfield, P.E.; October 28, 2024; Project No. SEC-2024-1147", "Environmental condition and NFA conditions", "Most reliable environmental source; ASTM E1527-21. Expressly declines to verify unit locations relative to the Affected Area."],
["S-6", "Borrower Organizational Chart, Operating Agreement excerpts and certification", "Prepared by Calloway & Strauss PLLC; January 2025; Operating Agreement amended through December 1, 2024", "Ownership, governance, capital contributions", "Borrower-prepared and certified; internally inconsistent with S-4 and S-2 on the Land (Section 3.1) and states a $0 contribution by the 28% member."],
["S-7", "Construction Budget and Draw Schedule (workbook, three tabs)", "Harborview Capital Partners LLC; January 8, 2025", "Budget, draw schedule, interest reserve model", "The only document with line-item cost detail. Draw 9 does not foot; model assumes a SOFR rate 85 bps below the current rate (Sections 3.4, 3.6)."],
["S-8", "Draft Loan Agreement", "February 3, 2025", "Deliverable", "Prepared by Lender’s counsel from S-1 and S-2 with the resolutions described in Sections 3–6."],
]
table(doc, SRC, widths=[0.4, 1.55, 1.5, 1.15, 1.9], size=7.5)

# ------------------------------------------------------------------ 2
heading1(doc, "2.  Executive Summary and Top-Risk Register", before=14, after=8, size=12)
rich(doc, [("The transaction is approvable, but it cannot close in its present documentary condition. Six issues are, in our view, "
            "closing-critical: the Land and the equity story cannot be reconciled across five documents; the loan as sized breaches both the "
            "loan-to-cost covenant and the as-completed loan-to-value covenant, and the condition of approval the Committee adopted does not "
            "cure the first; the $3.4 million prior deed of trust that must be released has no place in the budget or the sources and uses; the "
            "Deed Notice required by the environmental regulator 66 days ago is not evidenced, and the regulator’s land-use restriction is in "
            "direct tension with the residential program; and the interest availability under the mezzanine loan may already be spent.")],
     first_indent=0.5)
rich(doc, [("The Draft Agreement addresses each of these issues with a defined-term mechanism rather than a recital, so that the "
            "resolution is self-executing on the Closing Date. Only one issue requires a commercial decision before the next draft: whether the "
            "Commitment Amount is reduced to $45,360,000 (our recommendation, which cures both the loan-to-cost and the loan-to-value breach) "
            "or Total Project Costs are increased by at least $2,675,000 and funded with additional verified equity.")],
     first_indent=0.5)

RISK = [
["#", "Rating", "Issue", "Consequence if unresolved", "Draft Agreement reference", "Memo §"],
["1", "Critical", "The Land’s acquisition and funding are described five different ways, and the Borrower’s own budget says the Land was paid for with $8,200,000 of mezzanine proceeds", "The “$0 cash equity / land as equity” analysis on which approval rests is unsupported; the mezzanine loan may have only $1,000,000 of undrawn availability; sources and uses do not balance to cash", "§§ 1.1, 3.7(d), 3.16, 5.2; Sch. 1.1, 5.2; Ex. C", "3.1"],
["2", "Critical", "83.77% loan-to-cost against an 80.00% covenant; 65.25% as-completed loan-to-value against a 65.00% covenant; the $2,140,000 escrow condition does not change loan-to-cost", "Covenant breach at closing; no conforming draw schedule or fee calculation", "§§ 2.2, 8.1, 8.2; Ex. C", "3.2"],
["3", "Critical", "Payoff of the $3,400,000 Triangle Commercial Bank deed of trust is neither a use nor a source in the $56,700,000 budget", "Shortfall of at least $3.4 million at closing; no first-priority lien without it", "§ 3.8; Ex. C", "3.3"],
["4", "Critical", "Deed Notice due November 29, 2024 is not evidenced; the NFA Letter restricts the Affected Area to non-residential use while 14 units are said to sit above it", "NFA non-compliance and residential certificate-of-occupancy risk; loss of the 14 units drives DSCR to 1.21x and as-stabilized LTV to 67.56%", "§§ 3.4(c), 3.4(f), 10.2, 10.3; Ex. F", "3.5"],
["5", "High", "Interest reserve characterized as both adequate (+$221,325) and inadequate (−$365,830 / −$565,000) in the same record; no reserve for mini-perm interest during lease-up", "Payment default during construction or lease-up; carry guaranty is the only backstop", "§§ 2.7, 8.3, 8.8; Ex. E", "3.4"],
["6", "High", "Draw schedule disburses 100% of the GMP in Draws 2–8 and then “releases” retainage never withheld; 10% retainage is $3,475,000, not $3,275,000; Draw 9 components footing error of $1,000,000", "Draw 9 cannot be funded as written; over-advance of $1,000,000 against the Commitment", "§§ 4.1, 4.4; Ex. D", "3.6"],
["7", "High", "Both loans take a first-priority pledge of 100% of the membership interests; Intercreditor Agreement unexecuted", "Contested priority in a default; mezzanine loan effectively unsecured; heightened consolidation and lender-liability exposure", "§§ 3.5, 12.2, 12.3", "5.1"],
["8", "High", "The 28% member (an affiliate of the Mezzanine Lender) holds an effective veto over any financing over $1,000,000, any bankruptcy filing and any amendment of the operating agreement; no independent manager, separateness covenants or non-consolidation opinion", "The SPE protections cannot be implemented without the affiliate’s consent, and the affiliate can block the take-out refinancing", "§§ 3.6, 7.4, 11.2, 11.3", "5.2, 5.3"],
["9", "High", "DSCR is tested “at commencement of the Mini-Perm Period,” nine months before projected stabilization; extension condition requires 70% LTV against a 65% covenant", "Covenant failure at inception of the mini-perm by design; internally inconsistent extension test", "§§ 8.3, 2.13(c)(viii)", "3.8, 3.9"],
["10", "Medium", "Parcel 1 and Parcel 2 do not close: a 305.41-foot line is described against a 297.63-foot line; parcel areas and orientation conflict among title, ESA and appraisal", "Title cannot insure a unified site without a survey-based cure; the environmental overlay may be located on the wrong parcel corner", "§§ 3.2, 5.3; Ex. A", "4.2, 4.3"],
["11", "Medium", "Appraisal says the Historic District Association approved the design; title says no approval was furnished. Association assessment of $34,500 per annum is absent from operating expenses", "Stop-work or injunction risk under the CC&Rs; NOI overstated by $34,500 (DSCR 1.30x; value $75.66 million)", "§§ 3.12(d), 6.5, 8.11", "4.4"],
["12", "Medium", "Guaranty described both as $11,875,000 in the aggregate and $11,875,000 per guarantor; Mr. Osei’s exposure is 103.3% of net worth; the Term Sheet’s guarantor-net-worth Event of Default cross-references a Borrower covenant", "Ambiguity in the Bank’s recourse; unenforceable or inoperative default provision", "§§ 13.3, 14.1(n)–(o)", "6.1, 6.3"],
]
table(doc, RISK, widths=[0.3, 0.6, 2.05, 1.75, 1.1, 0.45], size=7)
para(doc, "Rating key: Critical — must be resolved before closing; High — should be resolved before closing and must be documented if "
          "deferred; Medium — resolve in the next draft or confirm on the diligence list.", size=8, italic=True, space_after=10)

# ------------------------------------------------------------------ 3
heading1(doc, "3.  Capital Structure, Sizing and Debt Service", before=14, after=8, size=12)

heading2(doc, "3.1  The Land and Borrower’s Equity — Five Irreconcilable Accounts (Critical)", before=10, after=6)
rich(doc, [("The single most consequential problem in the file is that the record cannot tell us who acquired the Land, when, for how much, "
            "or with whose money. Five documents give five answers:")], first_indent=0.5)
LAND = [
["Source", "Account given"],
["Title Commitment, Sch. A ¶ 5 and Ex. A", "Title vested in Borrower by Special Warranty Deed recorded June 12, 2023 (Book 7598, Pages 443 and 445) from Foster Street Properties LLC — an unrelated third party. No contribution from any member appears in the chain of title."],
["Organizational Chart § 1.3; Operating Agreement § 5.1(a)", "The Land “was contributed to Harborview Capital Partners LLC by Elena Vasquez-Torres at a cost basis of $8,200,000,” originally acquired by her “from personal resources” and contributed “upon formation of the project entity” (March 14, 2019)."],
["Credit Memorandum § 2.2", "The Land was acquired by Ms. Vasquez-Torres “on behalf of the Borrower through capital calls from all three members, including Brightleaf Investors Group LLC.”"],
["Phase I ESA §§ 1.2, 2.2", "“Harborview Capital Partners LLC acquired the Subject Property in 2022 for the purpose of redevelopment.”"],
["Appraisal § 6.1", "The $8,200,000 is “the price paid by Harborview Capital Partners LLC in early 2024.”"],
["Budget workbook, Detailed Budget line 1.01", "Land Acquisition “funded by Mezzanine Loan $8,200,000”; note: “Previously closed; funded by mezzanine loan proceeds and member capital calls.”"],
]
table(doc, LAND, widths=[1.95, 4.55], size=8)
rich(doc, [("These accounts cannot all be true. The recorded deed controls the fact of conveyance: the Land was acquired by purchase from a "
            "third party in June 2023, not by contribution at formation in 2019, and the transferor was not a member. That in turn means that "
            "(a) the Operating Agreement’s capital-contribution provision does not describe what actually happened and may itself require "
            "amendment and member consent to be accurate; (b) the credit memorandum’s reliance on “capital calls from all three members” is "
            "unsupported and is contradicted by the Borrower’s own certified chart, which states that Brightleaf Investors Group LLC and "
            "Mr. Osei contributed $0; and (c) the Land was not “free and clear of liens” — the $3,400,000 Triangle Commercial Bank deed of trust "
            "recorded in 2018 against the transferor remains unreleased of record, so Borrower took title subject to it.")],
     first_indent=0.5)
rich(doc, [("The budget line is the most serious of the six. If $8,200,000 of the $9,200,000 mezzanine commitment was advanced to fund the "
            "Land, then at closing only $1,000,000 of mezzanine availability remains, the sources and uses table in the Term Sheet (§ 5.1) and "
            "the credit memorandum (§ 5.1) overstate available mezzanine proceeds by $8,200,000, and — because the mezzanine carries payment-in-kind "
            "interest at 12.50% — the outstanding mezzanine balance is already larger than its stated principal amount. On a simple-interest basis, "
            "an $8,200,000 advance in or about June 2023 would have accreted to approximately $9,908,000 by February 2025, before any further "
            "advance. The Bank would then be closing a senior loan in which the subordinate lender has no remaining capacity, which is precisely "
            "the opposite of the “mezzanine fills the gap” premise of the approval.")],
     first_indent=0.5)
rich(doc, [("We have drafted the Agreement to require verified facts rather than to repeat any of the five accounts. Section 3.7(d) requires the "
            "recorded deeds, the settlement statement, the source of funds, the capital accounts and a Managing Member certificate; Section 3.16 "
            "requires the Mezzanine Documents, a disbursement history and a balance certificate; Section 5.2 states the acquisition facts the "
            "recorded deed establishes and leaves the funding to the certificate; and Exhibit C is presented in two panels because the budget may "
            "have to be restated.")],
     first_indent=0.5)
rich(doc, [("Recommended resolution.", {"bold": True}),
            ("  (i) Obtain the deeds, the June 2023 settlement statement, Borrower’s capital accounts and all amendments to the Operating "
             "Agreement; (ii) obtain the mezzanine disbursement history and a current balance certificate, including capitalized interest; "
             "(iii) restate the sources and uses on the verified facts; (iv) if mezzanine availability is exhausted, require either an additional "
             "equity contribution or a reduction in Total Project Costs sufficient to close the gap, and amend the definition of Permitted "
             "Mezzanine Loan accordingly; and (v) obtain amendments to the Operating Agreement that accurately recite the capital contributions, "
             "with member consents at the 75% threshold. Do not close on the current representation set.")],
     first_indent=0.5, space_after=8)

heading2(doc, "3.2  Loan-to-Cost and Loan-to-Value — and Why the Equity Escrow Condition Does Not Work (Critical)", before=10, after=6)
rich(doc, [("The arithmetic is simple and unforgiving. Total Project Costs are $56,700,000 and the Commitment Amount is $47,500,000, so the "
            "loan-to-cost ratio is 83.77% against the 80.00% covenant in Term Sheet § 6.1. The as-completed loan-to-value ratio is 65.25% "
            "($47,500,000 ÷ $72,800,000) against the 65.00% covenant in Term Sheet §§ 4 and 6.2. The credit memorandum cites only the loan-to-cost "
            "breach and shows the loan-to-value tests as “Pass” by comparing them to the Bank’s 70% policy limit rather than to the 65% covenant "
            "the Bank actually negotiated. The as-completed loan-to-value covenant is breached at closing and the file does not disclose it.")],
     first_indent=0.5)
rich(doc, [("The condition of approval adopted at Condition 10.1.2 — deposit $2,140,000 in cash into a Bank-controlled escrow “to bring the "
            "effective LTC into compliance” — does not achieve its stated purpose. The loan-to-cost ratio is loan divided by total project cost. "
            "Adding $2,140,000 of equity into an unchanged $56,700,000 budget while the Commitment Amount remains $47,500,000 leaves the ratio at "
            "exactly 83.77%. The escrow only works if the commitment is reduced by the same amount so that the equity funds costs the loan would "
            "otherwise have funded. The credit memorandum actually lists “(b) reduce the loan amount to $45,360,000” as an alternative to the "
            "escrow (Section 5.1), but the two are not alternatives: (b) is the mechanism by which (a) works.")],
     first_indent=0.5)
LTC = [
["Path", "Sources", "Loan-to-Cost", "As-Completed LTV", "Comment"],
["As proposed: $47,500,000 loan, $2,140,000 escrow, unchanged budget", "$47.5M + $9.2M + $2.14M = $58.84M against $56.70M of uses", "83.77% — breach", "65.25% — breach", "Escrow creates an unmatched source; ratio unchanged"],
["**Recommended:** reduce commitment to $45,360,000 and fund $2,140,000 of verified equity", "**$45.36M + $9.2M + $2.14M = $56.70M**", "**80.00% — compliant**", "**62.31% — compliant**", "Cures both breaches with one adjustment"],
["Alternative: retain $47,500,000 and increase Total Project Costs", "$47.5M + $9.2M + $2.675M = $59.375M against $59.375M of uses", "80.00% — compliant", "65.25% — breach", "Requires $2,675,000 of new, funded uses and equity; does not cure the LTV breach"],
]
table(doc, LTC, widths=[1.85, 1.65, 0.95, 0.9, 1.15], size=7.5)
rich(doc, [("The reduction to $45,360,000 also improves the as-stabilized loan-to-value ratio to 59.53% and reduces the Bank’s exposure by "
            "$2,140,000 at no cost to the borrower group other than the equity it was already required to deposit. Conforming adjustments follow "
            "automatically in the Draft Agreement because the Origination Fee is defined as 1.00% of the Commitment Amount ($453,600) and the "
            "Partial Repayment Guaranty as 25% of the Commitment Amount ($11,340,000); the title policy amount and the draw schedule are conformed "
            "by Sections 3.2 and 4.1 and Exhibit D.")],
     first_indent=0.5)
note(doc, "Action requested: confirm that the Committee elects the reduction path. This is the only open item in the Draft Agreement that "
          "changes the size of the facility.")

heading2(doc, "3.3  The Unfunded Payoff of the Existing Mortgage (Critical)", before=10, after=6)
rich(doc, [("Title Commitment Schedule B, Part I, Requirement 4 and Part II, item 10 disclose a deed of trust recorded in Book 6215, Page 892, "
            "dated September 14, 2018, from Foster Street Properties LLC (Borrower’s predecessor in title) to Triangle Commercial Bank, securing "
            "an original indebtedness of $3,400,000, against which no release has been recorded. The Title Officer notes that Borrower’s counsel "
            "advised by letter dated November 22, 2024 that the debt “has been partially repaid” and will be satisfied at closing “from the "
            "Borrower’s own funds or from closing proceeds.”")],
     first_indent=0.5)
rich(doc, [("No line item in the $56,700,000 uses of funds provides for that payoff, and no source of funds is identified for it. The Term "
            "Sheet (§ 5.2) does not mention it; the credit memorandum (§ 9.7) treats it as a closing condition without costing it. Because the "
            "Senior Deed of Trust cannot be insured as a first-priority lien until the prior deed of trust is released, the payoff is a "
            "mandatory cash use at closing, in an amount that is presently unknown because no payoff letter has been obtained.")],
     first_indent=0.5)
rich(doc, [("Note also that funding the payoff with additional senior proceeds does not improve the loan-to-cost ratio: if the payoff is added "
            "to uses and funded by an equal increase in the loan, the ratio is unchanged at approximately 83.8%. A conforming closing therefore "
            "requires both a new use line and a new equity source. Section 3.8 of the Draft Agreement conditions closing on a payoff letter dated "
            "within thirty days, deposits with the title company, a recorded cancellation under N.C.G.S. § 45-37, and a conformed sources and uses "
            "statement.")],
     first_indent=0.5)
note(doc, "Action requested: direct Borrower to obtain the payoff letter now. Until the payoff amount is known, neither the closing statement "
          "nor the conformed budget can be completed, and the loan-to-cost test cannot be finalized.")

heading2(doc, "3.4  Interest Reserve: Three Conclusions From the Same Facts (High)", before=10, after=6)
rich(doc, [("The record reaches three different conclusions about whether $4,850,000 is sufficient, and the difference is not analytical "
            "judgment but an assumption error:")], first_indent=0.5)
IRM = [
["Source", "SOFR assumption", "Average balance assumption", "Total interest", "Surplus / (shortfall)"],
["Budget workbook, “Interest Reserve Analysis” tab", "3.50% (all-in 6.75%)", "Derived from the draw schedule (≈$27,429,000)", "$4,628,675", "$221,325 — “APPEARS ADEQUATE”"],
["Budget workbook, sensitivity table", "4.35% (all-in 7.60%)", "Same", "$5,215,830", "($365,830)"],
["Credit Memorandum § 6.2", "4.35% (all-in 7.60%)", "Assumed $28,500,000", "$5,415,000", "($565,000)"],
]
table(doc, IRM, widths=[1.9, 1.05, 1.6, 0.9, 1.05], size=8)
rich(doc, [("The Borrower’s model therefore reports the reserve as adequate only because it assumes a SOFR rate of 3.50%, which is "
            "approximately 85 basis points below the 4.35% rate the credit memorandum itself uses as current. On the Borrower’s own sensitivity "
            "table, the reserve is short at every rate at or above 4.00%. The credit memorandum’s $565,000 figure and the model’s $365,830 figure "
            "differ solely because of the average-balance assumption; both conclude the reserve is short. The approval language in Section 6.2 "
            "(“approves the interest reserve of $4,850,000 as adequate based on current rate assumptions”) is inconsistent with the analysis "
            "immediately preceding it.")],
     first_indent=0.5)
rich(doc, [("Two further gaps compound the problem. First, the model stops at month 30 and therefore excludes interest on the $44.2 million "
            "to $47.5 million outstanding during the mini-perm period, yet the property is not projected to reach stabilization until "
            "approximately May 2028 — nine months into the mini-perm period. Borrower’s only source for roughly $2.8 million of interest over that "
            "stretch is its own funds, and the credit memorandum records that Borrower is contributing $0 of cash equity. The Carry Guaranty is the "
            "sole backstop. Second, the draw dates on the draw schedule tab (Draw 8 in August 2027, Draw 9 in October 2027) are month 31 and month "
            "33 of a 30-month construction period, so the interest model and the draw schedule do not describe the same loan.")],
     first_indent=0.5)
rich(doc, [("Recommended resolution.", {"bold": True}),
            ("  Section 2.7(c) of the Draft Agreement fixes the adequacy floor at the greater of the then-current rate and 4.35% SOFR; "
             "Section 2.7(e) adds a $500,000 borrower-funded Interest Reserve Contingency Escrow available first for interest shortfalls; "
             "Section 8.3(b) provides a lease-up accommodation for the Debt Service Coverage Ratio; and Section 2.13(c)(vi) requires an interest "
             "rate cap as a condition of extension. We recommend also requiring a twelve-month mini-perm interest reserve or a cap struck at or "
             "below 6.35% for the period from the Construction Maturity Date through stabilization.")],
     first_indent=0.5, space_after=8)

heading2(doc, "3.5  Environmental: The Deed Notice and the Use Restriction (Critical)", before=14, after=6)
rich(doc, [("The Phase I ESA describes a conditional No Further Action determination with four conditions, two of which are unmet on the face "
            "of the record:")], first_indent=0.5)
COND = [
["NFA condition", "Requirement and deadline", "Status in the record", "Consequence"],
["Condition 1 — Vapor Mitigation System", "Passive sub-slab depressurization, convertible to active, beneath any enclosed structure over the 0.38-acre Affected Area; as-built drawings and performance verification to NCDEQ within 90 days of foundation completion.", "Design referenced as “incorporated into the construction plans” (Phase I ESA § 8; appraisal § 8) and included in the GMP (budget line 2.08). No engineer’s design, NCDEQ approval or verification protocol is in the file.", "Construction-stage default; inability to obtain certificate of occupancy for space over the Affected Area."],
["Condition 2 — Non-residential land use restriction", "Future use of the Affected Area restricted to non-residential purposes; residential or other sensitive use requires additional investigation and a modification of the NFA determination.", "Credit Memorandum § 9.5 states that 14 residential units are positioned above the Affected Area. The Phase I ESA (§ 8.5) expressly declines to verify that, and the appraisal (§ 8) expresses no opinion on permissibility.", "Up to 14 units may be unoccupiable: NOI falls to $4,499,640, DSCR to 1.21x, as-stabilized value to ≈$70,306,875 and as-stabilized LTV to 67.56% — a breach of the 65% covenant."],
["Condition 3 — Soil Management Plan", "NCDEQ-approved plan required before any excavation, grading or subsurface disturbance in the Affected Area.", "Not in the file. The GMP includes site work and foundations in the Affected Area.", "Work cannot lawfully begin in the Affected Area; a stop-work order would also breach the construction schedule and trigger Section 14.1(f)."],
["Condition 4 — Deed Notice", "Notice of residual contamination and the land use restriction recorded in the Durham County Registry by November 29, 2024 (60 days after the NFA Letter).", "The Phase I ESA (October 28, 2024) states the notice had not been recorded. The title commitment effective December 5, 2024 does not list any recorded environmental land use restriction among its Schedule B-II exceptions, and disclaims environmental matters at Note 5.", "Either the notice was never recorded — apparent non-compliance with the NFA Letter — or it was recorded and omitted from the title commitment, in which case the title commitment is incomplete and the exception must be added."],
]
table(doc, COND, widths=[1.25, 2.0, 1.95, 1.3], size=7.5)
rich(doc, [("The Term Sheet does not help. Section 2 describes remediation as “completed … in accordance with the applicable directives of "
            "NCDEQ,” and Section 17 describes the NFA letter as authorizing “commercial use of the affected area … conditioned on the installation "
            "and maintenance of a soil vapor mitigation system in the parking garage structure.” Neither characterization discloses the "
            "non-residential land use restriction, the Soil Management Plan requirement or the Deed Notice. The vapor system scope in the Term "
            "Sheet (“in the parking garage structure”) is also narrower than the NFA requirement (“beneath any enclosed structure,” which includes "
            "ground-floor retail and any residential space above).")],
     first_indent=0.5)
rich(doc, [("Recommended resolution.", {"bold": True}),
            ("  (i) Produce the recorded Deed Notice immediately; if it was not timely recorded, obtain and produce NCDEQ’s written acknowledgment "
             "that late recordation does not affect the NFA status, and conform the closing date calculation accordingly. (ii) Obtain the architect’s "
             "overlay of the building plans against Figure 3 of the Phase I ESA; the credit memorandum’s assertion about the 14 units is presently "
             "unverified. (iii) If the overlay confirms the conflict, select one of the three resolutions in Section 3.4(f) of the Draft Agreement — "
             "an NFA modification, written NCDEQ confirmation that residential occupancy above the grade-level affected area is permissible with "
             "engineering controls, or redesign — and re-underwrite if the redesign option is chosen. (iv) Require NCDEQ approval of the Soil "
             "Management Plan before any Advance for subsurface work in the Affected Area. (v) Obtain a pollution legal liability quotation, as "
             "the Phase I ESA recommends (Recommendation 6).")],
     first_indent=0.5, space_after=8)

heading2(doc, "3.6  The Draw Schedule Does Not Foot (High)", before=14, after=6)
rich(doc, [("Three arithmetic defects run through the draw schedule as it appears in Term Sheet § 9.2, credit memorandum § 7.1 and the "
            "Borrower’s workbook:")], first_indent=0.5)
DRW = [
["Defect", "Detail", "Correction in Exhibit D"],
["Retainage never withheld", "Draws 2 through 8 total exactly $34,750,000 — 100% of the guaranteed maximum price — so no amount is retained. Draw 9 then “releases” $3,275,000 of retainage. A 10% holdback on $34,750,000 is $3,475,000, not $3,275,000 (which is 9.42%).", "Draws 2 through 8 net of 10% retainage total $31,275,000; Draw 9 releases $3,475,000."],
["Developer fee funded twice", "The budget allocates the $2,835,000 developer fee as $1,835,000 senior and $1,000,000 mezzanine (Detailed Budget line 5.01), but the draw schedule allocates the entire $2,835,000 to senior draws. In the workbook, the components of Draw 9 sum to $4,275,000 against a stated draw of $3,275,000 — a $1,000,000 footing error, equal to the mezzanine share.", "Only $1,835,000 of developer fee is drawn from the senior loan; Draw 9 foots at $3,475,000."],
["Draws after maturity", "Draw 8 (substantial completion) is dated August 2027, which is month 31 of a 30-month construction period ending August 28, 2027; Draw 9 (retainage release) is dated October 2027 — two months after maturity and within the mini-perm period.", "Section 4.4 permits the retainage release after the Construction Maturity Date only on stated conditions and with Lender’s documented consent."],
]
table(doc, DRW, widths=[1.4, 3.6, 1.5], size=8)
rich(doc, [("Exhibit D to the Draft Agreement is a conformed schedule that foots to $47,500,000 and includes a reconciliation table showing each "
            "difference from the Term Sheet schedule. The Committee should also note the practical consequence: because the retainage release is the "
            "last $3.475 million of the facility and falls due after maturity, a Borrower that is otherwise performing will need Lender’s consent to "
            "a post-maturity advance, or a short extension, in order to be paid in full. That should be resolved in the closing documents rather than "
            "at the maturity date.")],
     first_indent=0.5, space_after=8)

heading2(doc, "3.7  Unfunded Costs Outside the Approved Budget (High)", before=14, after=6)
rich(doc, [("The $56,700,000 budget is internally additive — we verified that the seven line items sum exactly — but it is not complete. The "
            "following costs are either incurred, contractual or inevitable, and none is funded:")], first_indent=0.5)
UNF = [
["Item", "Estimated amount", "Basis", "Treatment"],
["Payoff of the Existing Mortgage", "$3,400,000 original principal; balance unknown", "Title Commitment Sch. B-I ¶ 4 and Sch. B-II ¶ 10", "Add as a use; add matching equity source (Section 3.3)"],
["Mezzanine interest at 12.50% (payment-in-kind)", "≈$2,875,000 over 30 months on $9,200,000; ≈$1,708,000 already accrued if funded in June 2023", "Term Sheet § 1.4; Credit Memorandum § 4.4; Budget line 1.01", "Quantify from the Mezzanine Documents; confirm it is payable from refinancing proceeds and not from the Bank’s collateral"],
["Unused line fee at 0.25%", "≈$125,000 over the construction period", "Term Sheet § 3.4; average undrawn balance ≈$20.1 million", "Add to the budget or fund from equity"],
["Exit fee", "Up to $237,500 (0.50% during construction); $118,750 (0.25% in the first six mini-perm months)", "Term Sheet § 3.4", "Add to the budget or fund from equity"],
["Extension fee", "$118,750 if the Extension Option is exercised", "Credit Memorandum § 11(e)", "Fund at the time of exercise"],
["Association assessments under the Declaration", "$34,500 per annum ($0.12 × 287,500 gross building area)", "Title Commitment Sch. B-II ¶ 11(b)", "Add to operating expenses; see Section 4.4"],
["Public art requirement", "Unknown", "Title Commitment Sch. B-II ¶ 12", "Confirm with the City; add to the budget if applicable"],
["Lease-up costs", "≈$680,000 per the appraisal; $250,000 budgeted", "Appraisal § 6.2; Budget line 3.10", "Fund the difference from equity or from the contingency"],
["Environmental remediation already incurred", "$485,000 (plus demolition)", "Phase I ESA § 6.3", "Confirm it was funded by the member, not reimbursed from loan proceeds"],
]
table(doc, UNF, widths=[1.55, 1.65, 1.75, 1.55], size=7.5)
rich(doc, [("None of these is unusual in amount; the problem is that the underwriting treats a budget with a 3.28% hard-cost contingency "
            "($1,140,000 against $34,750,000) and a $300,000 soft-cost contingency as complete, when at least $3.4 million of mandatory closing "
            "uses sit outside it. We recommend that the credit memorandum be revised to state Total Project Costs on a fully funded basis and that "
            "the additional sources be identified before the file returns to Committee.")],
     first_indent=0.5)
note(doc, "The credit memorandum describes the contingency as “$1,440,000 … approximately 4.1% of hard construction costs.” That figure "
          "divides total contingency by hard costs; the hard-cost contingency is separately stated in the Borrower’s budget at $1,140,000, or "
          "3.28% of hard costs, which is at the low end of the Bank’s 3%–5% guidance given a guaranteed maximum price that includes all site work.")

heading2(doc, "3.8  Financial Covenant Design (High)", before=14, after=6)
rich(doc, [("Three design problems in the Term Sheet’s financial covenants would produce a default that no borrower could avoid:")],
     first_indent=0.5)
CVD = [
["Covenant", "Term Sheet drafting", "Problem", "Draft Agreement"],
["Debt Service Coverage Ratio", "“Tested at the commencement of the Mini-Perm Period and annually thereafter based on actual trailing twelve-month net operating income” (§ 6.3)", "The mini-perm begins August 28, 2027. Trailing twelve-month NOI at that date is effectively nil, and the appraiser projects stabilization only in approximately May 2028 (Appraisal § 6.3). The first test fails by construction and would immediately require a principal curtailment or a cash collateral deposit.", "§ 8.3(b): 1.15x on annualized in-place income until twelve months after Substantial Completion; 1.25x thereafter."],
["Loan-to-Value", "65% as-completed and as-stabilized (§ 6.2) but the extension condition in the credit memorandum requires ≤70% (§ 11(h))", "Inconsistent thresholds: an extension could be granted while the Loan is in breach of § 8.2.", "§ 2.13(c)(viii) conformed to 65.00%."],
["Guarantor net worth", "Event of Default if “any Guarantor’s net worth falls below the minimum threshold set forth in Section 6.4” (§ 15)", "Section 6.4 is the Borrower net worth covenant. There is no guarantor net worth covenant in the Term Sheet, so the default provision has no referent and is inoperative.", "§ 14.1(n)–(o): revocation of a Guaranty and failure to meet the § 8.5 liquidity covenant, with a cure period."],
]
table(doc, CVD, widths=[1.2, 1.9, 2.2, 1.2], size=7.5)
rich(doc, [("The exposure created by the loan-to-value covenant deserves emphasis. Because the as-stabilized value depends on 212 units, a "
            "loss of the 14 units over the Affected Area reduces the as-stabilized value to approximately $70,306,875 and drives the as-stabilized "
            "loan-to-value ratio to 67.56%, in breach of the 65% covenant even at the conformed commitment of $45,360,000 (which would be 64.52% on "
            "the reduced value). The environmental issue in Section 3.5 and the loan-to-value covenant are therefore the same credit issue viewed "
            "from two directions, and the lender should not accept a covenant cure mechanism that permits the Bank to be paid down rather than "
            "requiring the use restriction to be resolved.")],
     first_indent=0.5, space_after=8)

heading2(doc, "3.9  Extension Option and Lease-Up Timing (Medium)", before=14, after=6)
rich(doc, [("The appraisal projects substantial completion on August 31, 2027, stabilization (95% occupancy) in approximately May 2028, and an "
            "absorption rate of 22 to 25 units per month (Appraisal §§ 4, 6.3). The construction maturity date is August 28, 2027 — three days "
            "before the projected substantial completion date — and the mini-perm matures August 28, 2028. The extension notice must be given "
            "sixty days before that, by June 28, 2028, at which point the property would be roughly one month past the appraiser’s own stabilization "
            "estimate. The 75% occupancy condition may be achievable in that window, but not by a wide margin, and a two-month absorption slip "
            "would defeat the extension.")],
     first_indent=0.5)
rich(doc, [("Relatedly, the Completion Guaranty in Term Sheet § 7.1 requires completion “on or before the Construction Maturity Date of "
            "August 28, 2027,” while the Project schedule and the appraisal both provide for substantial completion on August 31, 2027. The "
            "Guarantors would be in breach of the completion covenant three days before the contractor is contractually required to finish. "
            "Section 13.1 of the Draft Agreement sets the Completion Date at October 31, 2027 (sixty days after the Construction Maturity Date, "
            "consistent with the schedule) while preserving the separate obligation under Section 6.2 to achieve Substantial Completion by "
            "August 31, 2027. The Committee may prefer the opposite allocation; the point is that the two dates must be reconciled.")],
     first_indent=0.5)
note(doc, "Action requested: confirm the Completion Date allocation (October 31, 2027 versus August 28, 2027) and whether the extension "
          "occupancy threshold should be reduced from 75% to 65% with a corresponding increase in the principal curtailment requirement.")

# ------------------------------------------------------------------ 4
heading1(doc, "4.  Collateral, Title and Survey", before=16, after=8, size=12)

heading2(doc, "4.1  The Permitted Exceptions Provision Cannot Be Performed as Written (Medium)", before=10, after=6)
rich(doc, [("Term Sheet § 18 lists four Permitted Exceptions and then requires that “all other exceptions shown on Schedule B-II … including "
            "but not limited to any prior deeds of trust, shall be removed, released, or otherwise satisfied.” Schedule B-II contains items that "
            "cannot be removed: item 12 is the City of Durham Unified Development Ordinance and MU-D zoning district, which is a matter of law; and "
            "item 13 is facts ascertainable by inspection, which can only be modified by an affidavit of possession and a survey. The result is a "
            "closing condition that is literally impossible to satisfy, which invites a waiver at the closing table and leaves the insured "
            "exceptions undetermined.")],
     first_indent=0.5)
rich(doc, [("Exhibit B to the Draft Agreement restates the schedule as the eight matters Title Company can actually insure (the seven "
            "remaining exceptions plus the Deed Notice, if recorded) and specifies the treatment of each: standard exceptions 1, 2, 3, 5 and 6 to "
            "be deleted on the basis of the survey, the owner’s affidavit and standard endorsements; the mechanics’ lien exception to be modified "
            "to exclude pre-recording work; items 12 and 13 permitted as modified; and the Triangle Commercial Bank deed of trust expressly not "
            "permitted.")],
     first_indent=0.5)

heading2(doc, "4.2  The Two Parcels Do Not Close — A 7.78-Foot Discrepancy (Medium)", before=10, after=6)
rich(doc, [("Reproducing the metes and bounds from Schedule A of the title commitment and running the courses produces a closed rectangle for "
            "each parcel in isolation, but the two descriptions cannot both be right:")], first_indent=0.5)
BDY = [
["Parcel 1", "S 02°14′33″ W 298.62′ along Foster Street; S 87°45′27″ E 305.41′; N 02°14′33″ E 298.62′; N 87°45′27″ W 305.41′ to the point of beginning. Computes to 91,202 square feet = 2.094 acres (stated: 2.09 acres)."],
["Parcel 2", "Begins at the southwestern corner of Parcel 1; S 02°14′33″ W 201.88′ along Foster Street; S 87°45′27″ E 297.63′; N 02°14′33″ E 201.88′ to the “southeastern corner of Parcel 1”; thence along the southern boundary of Parcel 1, N 87°45′27″ W 297.63′ to the point of beginning. Computes to 60,086 square feet = 1.379 acres (stated: 1.38 acres)."],
["Conflict", "Parcel 1’s southern boundary is 305.41 feet. Parcel 2’s return course along that same boundary is 297.63 feet. The difference is 7.78 feet, so the descriptions leave either a 7.78-foot gap or a 7.78-foot overlap along the common line, and the “southeastern corner of Parcel 1” is not where Parcel 2 says it is."],
["Why it matters", "The Deed of Trust encumbers both parcels as a single integrated site; the appraisal values 3.47 acres as one site; the environmental delineation and the stormwater and utility easements are located by reference to parcel boundaries. A survey exception that cannot be deleted, or a boundary dispute with an adjoining owner, impairs both the lien and the development program."],
]
table(doc, BDY, widths=[1.0, 5.5], size=8)
rich(doc, [("Section 3.2(c)–(e) of the Draft Agreement requires a single-sheet ALTA/NSPS survey of both parcels certified to Lender, Borrower "
            "and Title Company, a boundary line agreement, quitclaim deed or corrected legal description sufficient to permit deletion of the "
            "survey exception and insurance of the Property as a single contiguous site, and a conformed Exhibit A. We also recommend that the "
            "Bank require the survey to carry Table A items 1, 2, 3, 4, 6(b), 7(a), 7(b)(1), 8, 9, 10, 11, 13, 14, 15 and 16.")],
     first_indent=0.5)

heading2(doc, "4.3  Parcel Area, Orientation and Frontage Conflicts (Medium)", before=10, after=6)
rich(doc, [("Three of the source documents describe the site geometry differently, and the difference is not academic because the "
            "environmental restriction is located by reference to the “northeast corner of Parcel 0821-04-72-4102”:")], first_indent=0.5)
ORI = [
["Attribute", "Title commitment", "Phase I ESA", "Appraisal", "Comment"],
["Parcel 1 area", "2.09 acres", "1.89 acres", "3.47 acres combined", "Areas differ by 0.20 acre each way; the survey will resolve"],
["Parcel 2 area", "1.38 acres", "1.58 acres", "3.47 acres combined", "Same"],
["Relative position", "Parcel 2 lies south of Parcel 1 (it begins at Parcel 1’s southwestern corner)", "Parcel 1 is the “western parcel”; Parcel 2 is the “eastern parcel”", "Not stated", "Direct conflict; affects where the Affected Area sits relative to the building footprint"],
["Street frontage", "Foster Street bounds both parcels on the west (298.62′ + 201.88′ = 500.50′)", "Foster Street is “to the north” (Fig. 3: “along the northern boundary”)", "420 feet of frontage along Foster Street on the western boundary; 20-foot public alley on the eastern boundary", "Frontage varies by 80 feet; the “public alley” does not appear in the title commitment"],
["Topography", "Not stated", "Slope of approximately 2% from northwest to southeast; elevations 395–401 feet", "Grade change of approximately four feet from north to south", "Minor"],
]
table(doc, ORI, widths=[0.95, 1.6, 1.6, 1.4, 0.95], size=7.5)
rich(doc, [("We recommend that the survey also be used to confirm (a) that no Improvement encroaches on the 20-foot Duke Energy easement or "
            "the 0.22-acre stormwater easement, (b) that the stormwater detention function required by the recorded easement survives the "
            "proposed site plan, and (c) that the parking structure’s 276 spaces comply with any maximum parking limitation in the MU-D district. "
            "Schedule B-II item 12 expressly refers to “parking minimums and maximums,” while the Term Sheet, appraisal and credit memorandum all "
            "conclude only that minimum parking requirements are satisfied. If the MU-D district imposes a maximum, the “permitted as of right” "
            "conclusion in Term Sheet § 2 is inaccurate as to parking.")],
     first_indent=0.5)

heading2(doc, "4.4  Declaration of Covenants: Approval Status and Unbudgeted Assessments (Medium)", before=10, after=6)
rich(doc, [("The appraisal states that “the architectural design has been reviewed and approved by the Brightleaf Historic District "
            "Association in accordance with the CC&Rs” (Appraisal § 2, item (c)). The title officer states the opposite: “The Company has not "
            "received evidence that the current project plans … have been submitted to or approved by the Brightleaf Historic District Association "
            "Architectural Review Committee” (Title Commitment, Schedule B-II ¶ 11, Note). The Declaration requires submission at least ninety days "
            "before construction and permits a building permit only after written approval or the lapse of a sixty-day deemed-approval period, and "
            "it gives the Association a right to seek injunctive relief to halt unapproved construction. The credit memorandum correctly treats "
            "approval as an open item (Condition 10.1.14) but does not note that the appraisal says it is already obtained.")],
     first_indent=0.5)
rich(doc, [("Separately, Schedule B-II ¶ 11(b) discloses assessments of $0.12 per square foot of gross building area per annum. Applied to "
            "287,500 square feet, that is $34,500 per year, and it is not among the operating expenses in the appraiser’s stabilized analysis "
            "(Appraisal § 7). Deducting it reduces stabilized NOI to $4,842,300, the Debt Service Coverage Ratio to 1.30x and the as-stabilized "
            "value at a 6.40% capitalization rate to $75,660,938 — the covenant still passes, but the omission should be corrected before the "
            "operating expense ratio of 20.6% is relied upon.")],
     first_indent=0.5)

heading2(doc, "4.5  Mechanic’s Lien Relation-Back and Pre-Closing Work (High)", before=10, after=6)
rich(doc, [("Title Commitment Note 4 correctly recites that under N.C.G.S. § 44A-10 a claim of lien for labor or materials relates back to "
            "the time of first furnishing at the site. Demolition was completed in August 2024 and environmental remediation in September 2024; "
            "the site has been rough-graded; and budget line 2.01 allocates $3,180,000 of guaranteed maximum price value to “Site Work — "
            "Demolition, grading, utilities, paving.” Work has therefore been performed at the site before the Deed of Trust will be recorded, and "
            "the Bank’s lien will be subordinate to any related claim of lien unless the exposure is closed out.")],
     first_indent=0.5)
rich(doc, [("Section 3.2(e) and Section 4.12 of the Draft Agreement require an owner’s affidavit and a contractor’s affidavit as to all work "
            "performed and materials furnished before closing, conditional lien waivers for that work, and, from each subsequent draw, statutory "
            "partial waivers from the general contractor and every subcontractor and materialman. We also recommend that the Bank require a "
            "performance and payment bond notwithstanding the 10% retainage, which the Term Sheet does not require (Section 3.9(c) of the Draft "
            "Agreement treats the bond as required unless expressly waived).")],
     first_indent=0.5)

heading2(doc, "4.6  Flood Determination Conflict (Low)", before=10, after=6)
rich(doc, [("The appraisal cites FEMA panel 3710406400J effective May 2, 2019; the Phase I ESA cites panel 3720098700J effective March 2, "
            "2009. Both conclude Zone X (minimal hazard), so the conclusion is consistent even though the source data are not. The Bank is "
            "required to obtain a Standard Flood Hazard Determination for the life of the loan in any event; Section 3.10 of the Draft Agreement "
            "requires it, and Section 9.1(f) requires flood insurance only if the determination places any part of the Property in a Special "
            "Flood Hazard Area.")],
     first_indent=0.5)

# ------------------------------------------------------------------ 5
heading1(doc, "5.  Structure, Affiliate and Single-Purpose Entity Issues", before=16, after=8, size=12)

heading2(doc, "5.1  Competing Pledges of 100% of the Membership Interests (High)", before=10, after=6)
rich(doc, [("Term Sheet § 8 gives the Bank a “first priority” pledge of 100% of the membership interests, and Term Sheet § 1.4 and the "
            "Organizational Chart both state that the mezzanine loan is secured by “a pledge of 100% of the membership interests.” Only one lender "
            "can hold a first-priority security interest in the same collateral. The credit memorandum (§ 4.2) identifies the conflict and recommends "
            "that the Bank take first priority and the mezzanine lender second, with the priority resolved in the Intercreditor Agreement. That "
            "Intercreditor Agreement has been “negotiated but is not yet executed” (Organizational Chart § 1.2; Credit Memorandum § 4.4).")],
     first_indent=0.5)
rich(doc, [("We have drafted to the approved credit decision, but we recommend that the Committee reconsider the allocation before the "
            "intercreditor negotiation concludes, for four reasons:")], first_indent=0.5)
PLG = [
("(a)", "The pledge of 100% of the equity is the mezzanine lender’s only collateral. Subordinating it to the Bank’s pledge leaves a $9.2 million loan secured by an interest that is worthless on a senior foreclosure — a structure that invites a recharacterization argument, an equitable subordination claim or a lender-liability claim against the Bank if the mezzanine lender later fails."),
("(b)", "A first-priority pledge in favor of the Bank means that on foreclosure the Bank acquires the Borrower itself, together with the Borrower’s environmental liabilities, rather than the real property. Given the residual contamination and the conditional NFA, that is an unattractive acquisition."),
("(c)", "The pledge is not needed for the Bank’s credit support. The Bank already holds a first deed of trust, an assignment of rents, a security interest in all personal property and intangibles, collateral assignments of the construction and architectural contracts, a completion guaranty, a carry guaranty, a 25% payment guaranty and an unlimited environmental indemnity, at a 62.31% as-completed loan-to-value ratio. The credit memorandum makes the same point when it describes the real-property collateral as sufficient (Section 9.4, Alternative)."),
("(d)", "A first-priority pledge by the mortgage lender of the equity of a borrower whose member is an affiliate of the mezzanine lender is precisely the fact pattern that heightens substantive consolidation risk, which Section 9.3 of the credit memorandum identifies as a principal concern."),
]
for lbl, txt in PLG:
    sub(doc, lbl, txt, level=1, size=10)
rich(doc, [("We recommend a first-priority pledge in favor of the mezzanine lender with the Bank holding a springing, second-priority pledge, "
            "step-in rights upon an Event of Default, and a ninety-day standstill on the mezzanine lender’s remedies, all as set out in Section 12.3 "
            "of the Draft Agreement. If the Committee retains the approved allocation, Section 12.2 and the Intercreditor Agreement should say so "
            "expressly, and the Bank should require a mezzanine lender consent to the Bank’s ownership of the equity on foreclosure and a release of "
            "the mezzanine lender’s claims against the equity in that event.")],
     first_indent=0.5)

heading2(doc, "5.2  The 28% Member Is the Mezzanine Lender’s Affiliate — and Holds a Veto (High)", before=10, after=6)
rich(doc, [("Three features of the capital structure, taken together, are more significant than the credit memorandum’s “affiliate relationship” "
            "heading suggests:")], first_indent=0.5)
rich(doc, [("First, Brightleaf Investors Group LLC contributed $0 and received 28% “in consideration of its commitment to arrange third-party "
            "mezzanine financing for the Project” (Operating Agreement § 5.1(b); Organizational Chart § 1.3). The financing was arranged with "
            "Brightleaf Mezzanine Capital LLC, an entity under the common control of Thomas R. Chen. On the face of the operating agreement, "
            "therefore, the mezzanine lender holds an indirect 28% equity interest in its own borrower, acquired for no cash. That is not simply an "
            "affiliate relationship; it is an equity-for-debt-arrangement exchange that a bankruptcy court or a subsequent purchaser could treat as "
            "evidence that the mezzanine loan is equity. The credit memorandum’s statement that the Land was funded “through capital calls from all "
            "three members, including Brightleaf Investors Group LLC” (Section 2.2) is directly contradicted by the operating agreement excerpt and "
            "by the Borrower’s certified chart.")],
     first_indent=0.5)
rich(doc, [("Second, the operating agreement requires the approval of members holding at least 75% of the membership interests for any "
            "financing or refinancing over $1,000,000, any sale or encumbrance of substantially all assets, any amendment of the operating "
            "agreement, and any voluntary bankruptcy filing (Operating Agreement § 3.2). Ms. Vasquez-Torres holds 62% and Mr. Osei 10%; together "
            "they hold 72% and cannot reach 75%. Brightleaf Investors Group LLC therefore holds an effective veto over (i) the permanent take-out "
            "refinancing that is the Bank’s exit, (ii) the Bankruptcy Code filing that the independent manager provision is designed to control, and "
            "(iii) the amendments to the operating agreement that the Bank is requiring as a condition of closing. The same 75% threshold governs "
            "the member consents required to authorize this loan (Section 3.2(b)), so the Bank’s closing condition cannot be satisfied without the "
            "affiliate’s signature.")],
     first_indent=0.5)
rich(doc, [("Third, Section 5.3 of the operating agreement permits capital calls with a two-for-one dilution penalty for non-funding members. "
            "An involuntary dilution of that kind would be a transfer of a membership interest without the Bank’s consent, in breach of the negative "
            "covenant against transfers; the Draft Agreement addresses it directly at Section 7.10. The negative covenant in Term Sheet § 14 and the "
            "operating agreement mechanism cannot both operate as written.")],
     first_indent=0.5)
rich(doc, [("We also note a diligence gap: the credit memorandum certifies that Know Your Customer and Customer Due Diligence were completed "
            "on Brightleaf Investors Group LLC and Thomas R. Chen (Section 12), while the Organizational Chart states that the identities of the "
            "other members of Brightleaf Investors Group are “available upon request under separate confidentiality agreement” (Section 1.2). The "
            "Bank should obtain the beneficial ownership certification for the entity member before closing, as Section 5.16 of the Draft Agreement "
            "represents.")],
     first_indent=0.5)
rich(doc, [("Recommended resolution.", {"bold": True}),
            ("  Require (i) an amended and restated operating agreement that (A) contains the separateness and independent manager provisions, "
             "(B) removes the 75% consent requirement for any refinancing, sale or other action approved by Lender under the Loan Documents, and "
             "(C) eliminates or subjects to Lender consent the dilution mechanism in Section 5.3; (ii) member consents executed by all three members, "
             "including Brightleaf Investors Group LLC, authorizing the loan, the pledges and the amendments; (iii) the non-consolidation opinion "
             "from Borrower’s counsel; and (iv) beneficial ownership certifications for the entity member. Sections 3.6, 7.4, 7.10, 11.2, 11.3 and "
             "11.5 of the Draft Agreement implement these requirements.")],
     first_indent=0.5, space_after=8)

heading2(doc, "5.3  Single-Purpose Entity Status Is Currently Unsupported (High)", before=10, after=6)
rich(doc, [("The Borrower’s certified chart states plainly that the operating agreement “does not currently include provisions for an "
            "independent director or independent manager, nor does it contain separateness covenants customarily associated with single-purpose "
            "entity structures,” and that there are “no separateness covenants requiring the Company to maintain its own books, records, and bank "
            "accounts separate from those of its members or their affiliates, no prohibition on commingling of funds with affiliates, and no "
            "requirement that the Company obtain a non-consolidation opinion.” The Term Sheet nevertheless requires the Borrower to represent that it "
            "is a single-purpose entity (Section 12) and to maintain that status (Sections 13, 20), and the credit memorandum’s recommendation rests "
            "in part on SPE covenants. The representation would be inaccurate on the date it is made. Sections 3.6 and 11.1 through 11.5 of the "
            "Draft Agreement convert the requirement into a pre-closing deliverable rather than a present representation.")],
     first_indent=0.5)

# ------------------------------------------------------------------ 6
heading1(doc, "6.  Guaranties and Guarantor Capacity", before=16, after=8, size=12)

heading2(doc, "6.1  The Partial Repayment Guaranty Is Ambiguously Sized (Medium)", before=10, after=6)
rich(doc, [("Term Sheet § 7.3 provides for a guaranty “in the amount of 25% of the Loan Amount (25% × $47,500,000 = $11,875,000)” that is "
            "“joint and several, meaning that each Guarantor shall be individually liable for the full guaranteed amount.” The credit memorandum "
            "then measures “each guarantor’s partial repayment guaranty of $11,875,000” against each guarantor’s individual net worth (Section "
            "2.3.3), which reads as $23,750,000 of aggregate exposure. The two characterizations produce very different recourse. Section 13.3 of the "
            "Draft Agreement fixes a single aggregate Guaranteed Amount of $11,875,000 ($11,340,000 at the conformed commitment) collectible once, "
            "while preserving each Guarantor’s joint and several liability up to that amount. The Committee should confirm this is what was "
            "approved.")],
     first_indent=0.5)

heading2(doc, "6.2  Guarantor Capacity (Medium)", before=10, after=6)
rich(doc, [("Applying the stated net worth figures, the $11,875,000 guaranty represents approximately 39.8% of Ms. Vasquez-Torres’s net worth "
            "and approximately 103.3% of Mr. Osei’s. The credit memorandum acknowledges the point (Section 2.3.3) and observes that both "
            "guarantors’ net worth is concentrated in illiquid real estate (approximately 65% and 59%, respectively). A payment guaranty that "
            "exceeds a guarantor’s net worth is not meaningful recourse. We recommend either (a) a separate, lower cap for Mr. Osei, (b) additional "
            "collateral or a letter of credit from Mr. Osei, or (c) a requirement that he maintain a specified minimum net worth during the term. "
            "Note that no guarantor net worth covenant exists in the Term Sheet (see Section 3.8 above).")],
     first_indent=0.5)

heading2(doc, "6.3  Documentary Inconsistencies in the Guaranty Package (Low)", before=10, after=6)
rich(doc, [("Term Sheet § 7.4 requires the Environmental Indemnity from the Guarantors only, while the credit memorandum requires it from "
            "“both the Borrower and the Guarantors” (Section 8.2) and Condition 10.1.11 refers only to the completion, carry and partial repayment "
            "guaranties. Section 13.4 of the Draft Agreement requires the Environmental Indemnity from Borrower and each Guarantor, which is the "
            "stronger and correct formulation. Term Sheet § 19 does not require the architect’s professional liability insurance that credit "
            "memorandum § 8.1 requires at $2,000,000; Section 9.1(e) of the Draft Agreement requires it, together with $1,000,000 for the engineer "
            "designing the vapor mitigation system.")],
     first_indent=0.5)

# ------------------------------------------------------------------ 7
heading1(doc, "7.  Regulatory, Diligence Currency and Insurance", before=16, after=8, size=12)

heading2(doc, "7.1  HVCRE Classification Turns on an Accounting Judgment (Low, but confirm)", before=10, after=6)
rich(doc, [("The credit memorandum concludes that the loan will be a high volatility commercial real estate exposure because contributed "
            "capital of $10,340,000 ($8,200,000 of Land at cost plus the $2,140,000 equity deposit) is 14.2% of the $72,800,000 as-completed "
            "appraised value, below the 15% threshold ($10,920,000). The conclusion depends on the value assigned to contributed real property. If "
            "the Land is counted at its $8,900,000 appraised value rather than its $8,200,000 cost, contributed capital is $11,040,000, or 15.16%, "
            "and the exposure may not be high volatility commercial real estate. The difference is a 150% risk weight and has a real capital "
            "consequence. We recommend that the Bank’s regulatory reporting group confirm the convention applied, and that the conclusion be "
            "re-run after the Land facts in Section 3.1 are verified.")],
     first_indent=0.5)

heading2(doc, "7.2  Diligence Currency (Medium — calendar risk)", before=10, after=6)
rich(doc, [("Three expiration dates bear on the closing calendar:")], first_indent=0.5)
CUR = [
["Item", "Date", "Expires / milestone", "Requirement if closing slips"],
["Phase I ESA — AAI shelf life (40 C.F.R. § 312.20(c))", "October 28, 2024", "April 26, 2025 (180 days)", "Update the assessment and obtain a new reliance letter (Draft Agreement § 3.4(g))"],
["Title commitment NC-2024-88712", "Effective December 5, 2024", "June 5, 2025 (six months)", "Written extension or re-issuance plus a date-down endorsement (§ 3.17)"],
["Appraisal (FIRREA 12-month rule)", "November 15, 2024", "November 15, 2025", "No action required for a February 28, 2025 closing; reappraisal at the Borrower’s expense if the Bank requires"],
["Environmental remediation report / NFA Letter", "September 2024 / September 30, 2024", "Deed Notice due November 29, 2024", "Immediate cure (Section 3.5)"],
]
table(doc, CUR, widths=[1.7, 1.2, 1.3, 2.3], size=8)
rich(doc, [("Because the ground-up construction period runs thirty months from closing, any delay in closing shortens the time available to "
            "reach substantial completion before the August 28, 2027 construction maturity date, which is already three days earlier than the "
            "projected substantial completion date. If closing moves beyond early March 2025, the Bank should consider making the Construction "
            "Maturity Date a fixed date rather than thirty months from closing, or requiring the general contractor to confirm that the guaranteed "
            "maximum price and the schedule survive the delay.")],
     first_indent=0.5)

heading2(doc, "7.3  Insurance Limits (Medium)", before=10, after=6)
rich(doc, [("Term Sheet § 19 requires builder’s risk insurance “in an amount not less than the total hard construction costs ($34,750,000).” "
            "Builder’s risk is ordinarily written for the completed replacement cost of the improvements, not for the contractor’s price, and the "
            "as-completed appraised value is $72,800,000 ($253 per square foot of gross building area). A $34,750,000 limit would leave the "
            "Bank’s loss payee interest substantially underinsured in a total loss, particularly because soft costs, the developer fee and the "
            "interest reserve are all funded through the loan. Section 9.1(a) of the Draft Agreement requires full replacement cost with an "
            "agreed-value endorsement and soft cost and delayed-opening coverage.")],
     first_indent=0.5)

# ------------------------------------------------------------------ 8
heading1(doc, "8.  Reconciliation Schedule — Every Figure Recomputed", before=16, after=8, size=12)
rich(doc, [("The following table records our independent recomputation of each figure in the record. “Verified” means the figure was "
            "reproduced from its stated inputs. “Verified — not reported” means the figure is correct but does not appear in the record and "
            "bears on compliance. “Does not reconcile” means the stated figure cannot be reproduced.")], first_indent=0.5)
REC = [
["#", "Item", "Stated", "Our computation", "Result"],
["1", "Loan-to-cost ratio", "83.77%", "$47,500,000 ÷ $56,700,000 = 83.7743%", "Verified — exceeds the 80.00% covenant"],
["2", "Maximum loan at 80% loan-to-cost", "$45,360,000", "$56,700,000 × 0.80 = $45,360,000", "Verified — excess of $2,140,000"],
["3", "As-completed loan-to-value ratio", "65.25%", "$47,500,000 ÷ $72,800,000 = 65.2473%", "Verified — exceeds the 65.00% covenant"],
["4", "Maximum loan at 65% as-completed loan-to-value", "not stated", "$72,800,000 × 0.65 = $47,320,000", "Verified — not reported; excess of $180,000"],
["5", "As-stabilized loan-to-value ratio", "62.34%", "$47,500,000 ÷ $76,200,000 = 62.3360%", "Verified"],
["6", "Total Project Costs", "$56,700,000", "$8,200,000 + $34,750,000 + $4,150,000 + $4,850,000 + $475,000 + $2,835,000 + $1,440,000 = $56,700,000", "Verified — but incomplete (Section 3.7)"],
["7", "Sources of funds", "$56,700,000", "$47,500,000 + $9,200,000 + $0 = $56,700,000", "Verified arithmetically; land appears as a use with no corresponding source (Section 3.1)"],
["8", "Gross potential income", "$6,462,000", "$5,712,000 + $552,000 + $198,000 = $6,462,000", "Verified"],
["9", "Residential rental income", "$5,712,000 (stated as 212 × $2,245 × 12)", "212 × $2,245 × 12 = $5,711,280", "Does not reconcile as stated; the figure is a normalized amount derived from face rents of $5,932,200 less $220,200 of concessions (Appraisal § 7)"],
["10", "Vacancy and credit loss; EGI; NOI", "$323,100; $6,138,900; $4,876,800", "5.0% × $6,462,000 = $323,100; $6,462,000 − $323,100 = $6,138,900; less $1,262,100 = $4,876,800", "Verified — the nine operating expense line items sum exactly to $1,262,100"],
["11", "Operating expense ratio", "20.6%", "$1,262,100 ÷ $6,138,900 = 20.56%", "Verified"],
["12", "Capitalization rate; as-stabilized value", "6.40%; $76,200,000", "$4,876,800 ÷ $76,200,000 = 6.4000%; $4,876,800 ÷ 0.0640 = $76,200,000", "Verified"],
["13", "As-completed value", "$72,800,000", "$76,200,000 − ($3,130,000 + $270,000) = $72,800,000", "Verified (lease-up deduction $2,450,000 rent + $680,000 costs + $270,000 risk)"],
["14", "Debt service coverage ratio", "1.31x", "$47,500,000 × 7.85% = $3,728,750; $4,876,800 ÷ $3,728,750 = 1.3079x", "Verified"],
["15", "Stress-tested debt service coverage ratio (+200 bps)", "1.04x", "$47,500,000 × 9.85% = $4,678,750; $4,876,800 ÷ $4,678,750 = 1.0423x", "Verified — fails the 1.25x minimum"],
["16", "Debt service coverage ratio after Association assessments", "not stated", "$4,876,800 − $34,500 = $4,842,300; ÷ $3,728,750 = 1.2986x", "Verified — not reported; passes, but NOI and value are overstated"],
["17", "Value and leverage if the 14 units are lost", "not stated", "$4,876,800 − $377,160 = $4,499,640; DSCR 1.2067x; value at 6.40% = $70,306,875; as-stabilized LTV = 67.56%", "Verified — not reported; breaches both the DSCR and LTV covenants"],
["18", "Draw schedule total", "$47,500,000", "$9,475,000 + $5,212,500 + $6,950,000 + $6,950,000 + $5,212,500 + $3,475,000 + $3,475,000 + $3,475,000 + $3,275,000 = $47,500,000", "Verified as stated — but the components total $51,775,000 (Section 3.6)"],
["19", "Retainage at 10% of guaranteed maximum price", "$3,275,000 (Draw 9)", "$34,750,000 × 0.10 = $3,475,000", "Does not reconcile — $200,000 understated (9.42% rather than 10.00%)"],
["20", "Draws 2–8 against the guaranteed maximum price", "$34,750,000", "$34,750,000 = 100% of the GMP", "Verified — confirms that no retainage is withheld in Draws 2–8"],
["21", "Interest reserve — total interest at 3.50% SOFR", "$4,628,675 (surplus $221,325)", "Reproduced from the draw-schedule model; implied average balance $27,429,185", "Verified on its own assumption — the assumption is 85 bps below the current rate"],
["22", "Interest reserve — total interest at 4.35% SOFR", "$5,215,830 (shortfall $365,830); $5,415,000 (shortfall $565,000) per the Credit Memorandum", "$27,429,185 × 7.60% × 2.5 = $5,215,830; $28,500,000 × 7.60% × 2.5 = $5,415,000", "Both verified; the $199,170 difference is entirely the average-balance assumption"],
["23", "Contingency percentages", "“$1,440,000 = approximately 4.1% of hard construction costs”", "Hard cost contingency $1,140,000 ÷ $34,750,000 = 3.28%; soft cost $300,000 ÷ $4,150,000 = 7.23%; total ÷ hard = 4.14%", "Does not reconcile as characterized — the hard-cost contingency is 3.28%"],
["24", "Developer fee", "$2,835,000 (5.00% of Total Project Costs)", "$56,700,000 × 0.05 = $2,835,000", "Verified (5% is applied to a base that itself includes the fee and the Land)"],
["25", "Partial repayment guaranty", "$11,875,000", "$47,500,000 × 0.25 = $11,875,000; 103.26% of Mr. Osei’s net worth; 39.85% of Ms. Vasquez-Torres’s", "Verified — aggregate versus per-guarantor remains ambiguous (Section 6.1)"],
["26", "Guarantor liquidity coverage", "1.86x", "$9,300,000 ÷ $5,000,000 = 1.86x", "Verified"],
["27", "Land value", "$8,900,000", "3.47 acres × $2,565,000 = $8,900,550; $8,900,000 ÷ $151,153 = $58.88 per square foot", "Verified (rounded)"],
["28", "Parcel areas from the metes and bounds", "2.09 and 1.38 acres", "298.62′ × 305.41′ = 91,202 sf = 2.094 acres; 201.88′ × 297.63′ = 60,086 sf = 1.379 acres", "Verified in isolation — the shared boundary does not close by 7.78 feet (Section 4.2)"],
["29", "Foster Street frontage", "420 feet (Appraisal § 2)", "298.62′ + 201.88′ = 500.50 feet (Title Commitment, Sch. A ¶ 6)", "Does not reconcile — 80.5-foot difference"],
["30", "HVCRE contributed capital", "14.2% ($10,340,000 ÷ $72,800,000)", "At cost: 14.20%. At appraised land value ($8,900,000 + $2,140,000 = $11,040,000): 15.16%. Threshold: $10,920,000 (15.00%)", "Verified on the stated convention; the conclusion changes on the alternative convention (Section 7.1)"],
["31", "Mezzanine payment-in-kind accrual", "not quantified", "$9,200,000 × 12.50% × 2.5 years = $2,875,000 over 30 months; if $8,200,000 was advanced in June 2023, accrued interest to February 2025 is approximately $1,708,000", "Verified — not reported and not budgeted"],
["32", "Unused line fee over the construction period", "not quantified", "0.25% × ($47,500,000 − $27,429,185) × 2.5 = approximately $125,464", "Verified — not budgeted"],
["33", "Parking ratio", "1.30 spaces per unit", "276 ÷ 212 = 1.3019", "Verified"],
["34", "Remediation volume", "340 cubic yards (Credit Memorandum § 8.2); 320 cubic yards (Appraisal § 8); 1,200 cubic yards (Phase I ESA § 6.1)", "The Phase I ESA is the primary source", "Does not reconcile — a 3.5x to 3.75x discrepancy in the reported excavation volume"],
["35", "Remediation cost", "$485,000 (Phase I ESA § 6.3)", "Not referenced in the Credit Memorandum or the Appraisal; not in the Approved Budget", "Not reported elsewhere — confirm the funding source"],
]
table(doc, REC, widths=[0.3, 1.45, 1.35, 2.15, 1.25], size=7)

# ------------------------------------------------------------------ 9
heading1(doc, "9.  Missing Documents and Diligence Requests", before=14, after=8, size=12)
rich(doc, [("The following documents are referenced in the record but were not furnished. Several are conditions of the Bank’s own approval "
            "and cannot be satisfied without them.")], first_indent=0.5)
MISS = [
["#", "Document", "Referenced in", "Why required", "Priority"],
["1", "Executed signature pages of the Term Sheet; confirmation that the $75,000 expense deposit was received", "Term Sheet §§ 22, 23", "The copy in the file shows blank signature blocks; the deposit is a condition of acceptance", "Immediate"],
["2", "Recorded Special Warranty Deeds (Book 7598, Pages 443 and 445); June 2023 settlement statement", "Title Commitment Sch. A ¶ 5", "Resolves the Land acquisition and funding inconsistency (Section 3.1)", "Immediate"],
["3", "Mezzanine Loan agreement, pledge documents, disbursement history and current balance certificate", "Organizational Chart § 1.2; Credit Memorandum § 4.4", "Determines remaining availability and outstanding balance (Section 3.1)", "Immediate"],
["4", "Payoff letter from Triangle Commercial Bank; cancellation of deed of trust", "Title Commitment Sch. B-I ¶ 4; Sch. B-II ¶ 10", "Quantifies and clears the unbudgeted $3.4 million payoff (Section 3.3)", "Immediate"],
["5", "Recorded Deed Notice (or NCDEQ acknowledgment of late recording)", "Phase I ESA §§ 7, 10; NFA Letter Condition 4", "NFA compliance; title exception (Section 3.5)", "Immediate"],
["6", "Full NCDEQ NFA Letter with attachments and the Affected Area delineation", "Phase I ESA § 7; Term Sheet § 17", "Only summarized in the record; the recorded land use restriction must be reviewed", "Immediate"],
["7", "Phase II Environmental Site Assessment (Project No. SEC-2024-1089) and Sentinel reliance letters", "Phase I ESA §§ 5, 11", "Bank’s reliance and CERCLA protected-party status", "Before closing"],
["8", "Architect’s overlay of the building plans on the Phase I ESA Figure 3", "Phase I ESA § 8.5, Rec. 1", "Determines whether 14 units sit above the Affected Area (Section 3.5)", "Immediate"],
["9", "Fully executed GMP Contract with all exhibits and change orders; contractor financial statements and bonding capacity", "Term Sheet § 2; Appraisal § 3; Budget line 2.02–2.09", "Conditions precedent to closing; cost certainty", "Before closing"],
["10", "Architect’s Contract and professional liability certificate", "Term Sheet § 8; Credit Memorandum § 8.1", "Collateral assignment; insurance", "Before closing"],
["11", "ALTA/NSPS survey of both parcels", "Term Sheet § 18; Title Commitment Sch. B-I ¶ 5", "Resolves the boundary and area conflicts (Sections 4.2, 4.3)", "Before closing"],
["12", "Full Operating Agreement and all amendments, including the December 1, 2024 amendment; member resolutions", "Organizational Chart §§ 2.1–2.5", "Only excerpts were furnished; the 75% consent threshold must be satisfied", "Before closing"],
["13", "Beneficial ownership certification for Brightleaf Investors Group LLC", "Credit Memorandum § 12; Organizational Chart § 1.2", "KYC/CDD; the chart says identities are available only on request", "Before closing"],
["14", "Borrower financial statements supporting net worth of $14,200,000", "Term Sheet § 6.4; Credit Memorandum § 2.1", "The covenant may be breached at closing (Section 6.2)", "Before closing"],
["15", "Guarantor personal financial statements dated December 15 and 18, 2024, with asset support", "Credit Memorandum § 2.3", "Verification of the liquidity covenant and guaranty capacity", "Before closing"],
["16", "Zoning compliance letter (including maximum parking) and building permits", "Term Sheet § 11; Title Commitment Sch. B-II ¶ 12", "Confirms “permitted as of right” and the parking conclusion", "Before closing"],
["17", "Architectural Review Committee approval or deemed-approval evidence", "Title Commitment Sch. B-II ¶ 11, Note", "The appraisal asserts approval that has not been produced (Section 4.4)", "Before closing"],
["18", "Intercreditor Agreement (executed)", "Term Sheet §§ 1.4, 11; Credit Memorandum § 10.1.3", "Resolves the competing pledges (Section 5.1)", "Before closing"],
]
table(doc, MISS, widths=[0.3, 1.75, 1.5, 2.1, 0.85], size=7)

# ------------------------------------------------------------------ 10
heading1(doc, "10.  Recommended Revisions to the Conditions of Approval", before=16, after=8, size=12)
rich(doc, [("We recommend that the credit memorandum’s conditions of approval (Section 10) be reissued as follows before the file returns "
            "to Committee. The revisions are limited to conditions that are either arithmetically ineffective or incomplete.")],
     first_indent=0.5)
DELTA = [
["Credit Memorandum condition", "Issue", "Recommended revision"],
["10.1.2 — Equity Escrow Deposit of $2,140,000 “to bring the effective LTC into compliance”", "Depositing equity against an unchanged $56,700,000 budget while the Commitment Amount remains $47,500,000 does not change the loan-to-cost ratio", "Restate as two linked conditions: (a) reduction of the Commitment Amount to $45,360,000 on the Closing Date; and (b) deposit of $2,140,000 of verified, independently sourced equity, disbursed ahead of loan advances. Add the as-completed loan-to-value breach (65.25% against 65.00%), which is not reported"],
["10.1.5 — Satisfactory Title", "The condition does not address the boundary defect, the exceptions that cannot be removed, or the recorded Deed Notice", "Add: ALTA/NSPS survey and boundary resolution; conformed Permitted Exceptions per Exhibit B; Deed Notice as a permitted exception if recorded; title policy in the conformed amount"],
["10.1.7 — Environmental", "Requires the NFA letter and vapor system design but not the Deed Notice, the Soil Management Plan or resolution of the use restriction", "Add: (i) evidence of the recorded Deed Notice; (ii) NCDEQ-approved Soil Management Plan before any subsurface work; (iii) NFA modification, NCDEQ written confirmation, or redesign, per Draft Agreement § 3.4(f); (iv) pollution legal liability quotation"],
["10.1.4 — SPE Covenants and Non-Consolidation Opinion", "Does not address the 75% member approval threshold, which the affiliate of the mezzanine lender controls, or the dilution mechanism in Operating Agreement § 5.3", "Add: member consents executed by all three members; deletion or lender-control of the 75% consent requirement for refinancing, sale and bankruptcy; deletion of the dilution penalty for the term of the Loan"],
["10.1.3 — Intercreditor Agreement", "Requires lender first priority and mezzanine second priority; the reverse allocation is recommended in Section 5.1 above", "Conform to the Committee’s decision on priority; add a requirement that the mezzanine lender release its claims against the Pledged Interests upon a senior foreclosure if lender first priority is retained"],
["10.1.6 — Appraisal Confirmation", "Confirms only the value conclusions; does not address the omitted Association assessment, the unverified real estate tax estimate ($412,000 against $49,066 of current land taxes) or the unit overlay", "Add: confirmation that operating expenses include the Declaration assessment; support for the real estate tax estimate; confirmation that no unit is located over the Affected Area, or re-underwriting if one is"],
["10.1.14 — Brightleaf Historic District Association", "Contradicted by the appraisal’s statement that approval has been obtained", "Retain, and require a written statement from the Association rather than relying on the appraisal’s recital"],
["10.2.7 — Interest Reserve Adequacy Test", "No floor on the SOFR assumption; no reserve for the mini-perm lease-up period", "Fix the adequacy floor at the greater of the then-current rate and 4.35% SOFR; add the $500,000 Interest Reserve Contingency Escrow; require a twelve-month mini-perm interest reserve or an interest rate cap"],
["10.2.8 — Equity First", "Refers to “the equity escrow deposit, if required,” which leaves the requirement conditional", "Make the LTC Equity Deposit unconditional and require disbursement before any Advance other than Draw 1"],
["11 — Extension Option conditions", "The loan-to-value condition is stated at 70% against a 65% covenant; occupancy of 75% may be unattainable on the appraiser’s absorption schedule", "Conform the loan-to-value condition to 65.00%; consider 65% occupancy with a corresponding curtailment; require an interest rate cap with a strike at or below 6.35%"],
["Not in the Credit Memorandum", "No condition addresses the payoff of the Existing Mortgage or the mezzanine balance", "Add: payoff letter and recorded cancellation; mezzanine balance certificate and disbursement history; restated sources and uses"],
["Not in the Credit Memorandum", "No condition requires a payment and performance bond or full replacement-cost builder’s risk", "Add: 100% performance and payment bond unless expressly waived by an authorized officer; builder’s risk at full replacement cost with agreed-value endorsement"],
["Not in the Credit Memorandum", "Guaranty cap ambiguity and Mr. Osei’s capacity are noted but not conditioned", "Add: confirmation of the aggregate Guaranteed Amount; a separate cap, additional collateral or a net worth covenant for Mr. Osei"],
]
table(doc, DELTA, widths=[1.5, 2.3, 2.7], size=7.5)

# ------------------------------------------------------------------ 11
heading1(doc, "11.  Matters Requiring Instruction Before the Next Draft", before=14, after=8, size=12)
rich(doc, [("The Draft Agreement resolves what can be resolved on the documents and leaves the following seven matters in bracketed form. "
            "Each is identified in the text and on Exhibit H.")], first_indent=0.5)
INS = [
("1.", "Size of the facility.", "Reduce the Commitment Amount to $45,360,000 and require $2,140,000 of verified equity (recommended, cures both breaches), or retain $47,500,000 and fund at least $2,675,000 of additional project costs with additional equity. Draft Agreement §§ 2.2, 8.1, 8.2; Exhibit C."),
("2.", "Interest reserve protections.", "Approve the $500,000 Interest Reserve Contingency Escrow and the 4.35% adequacy floor, and decide whether a twelve-month mini-perm interest reserve or a rate cap is required. Draft Agreement §§ 2.7(e), 8.8; Exhibit E."),
("3.", "Completion Date.", "Confirm October 31, 2027 for the Completion Guaranty (sixty days after the Construction Maturity Date, consistent with the projected August 31, 2027 substantial completion) rather than August 28, 2027. Draft Agreement § 13.1."),
("4.", "Pledge priority.", "Confirm whether the Bank takes first or second priority in the membership interests, and whether a mezzanine lender release upon senior foreclosure is required. Draft Agreement § 12.2."),
("5.", "Guaranty sizing and capacity.", "Confirm the $11,875,000 aggregate cap ($11,340,000 at the conformed commitment) and whether Mr. Osei’s exposure requires a separate cap, additional collateral or a net worth covenant. Draft Agreement §§ 13.3, 8.5."),
("6.", "Environmental use restriction.", "Select the resolution path in Draft Agreement § 3.4(f) once the architect’s overlay and NCDEQ’s position are known."),
("7.", "Extension conditions.", "Confirm the 65% loan-to-value condition (against the Credit Memorandum’s 70%), the 75% occupancy threshold and the requirement for an interest rate cap. Draft Agreement § 2.13(c)."),
]
for n, head, body in INS:
    p = doc.add_paragraph()
    pf = p.paragraph_format
    pf.left_indent = Inches(0.85); pf.first_line_indent = Inches(-0.35)
    pf.space_after = Pt(5); pf.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    pf.tab_stops.add_tab_stop(Inches(0.85))
    r = p.add_run(f"{n}\t"); r.bold = True; r.font.size = Pt(10.5); r.font.name = FONT
    r2 = p.add_run(head + "  "); r2.bold = True; r2.font.size = Pt(10.5); r2.font.name = FONT
    r3 = p.add_run(body); r3.font.size = Pt(10.5); r3.font.name = FONT

# ------------------------------------------------------------------ 12
heading1(doc, "12.  Next Steps", before=14, after=8, size=12)
STEPS = [
["#", "Action", "Responsible party", "Target"],
["1", "Deliver the diligence requests in Section 9; confirm the payoff amount and the mezzanine balance first, as both feed the closing statement", "Borrower’s counsel (Calloway & Strauss PLLC)", "February 7, 2025"],
["2", "Committee instruction on the seven items in Section 11", "Senior Loan Committee / Mr. Forsythe", "February 10, 2025"],
["3", "Confirm the Deed Notice status with NCDEQ and obtain the architect’s overlay", "Borrower; Sentinel Environmental Consulting LLC", "February 12, 2025"],
["4", "Conclude the Intercreditor Agreement consistent with the Committee’s priority decision", "Ashford, Cromdale / mezzanine counsel", "February 17, 2025"],
["5", "ALTA/NSPS survey and boundary resolution; revised legal description", "Borrower; surveyor; Aldersgate Title & Escrow", "February 17, 2025"],
["6", "Second draft of the Loan Agreement and the companion documents (Note, Deed of Trust, Guaranties, Environmental Indemnity, Pledge Agreements) issued with the conformed budget, draw schedule and Exhibit B", "Ashford, Cromdale", "February 19, 2025"],
["7", "Non-consolidation opinion and Borrower’s legal opinions", "Calloway & Strauss PLLC", "February 24, 2025"],
["8", "Closing", "All parties", "February 28, 2025 (target)"],
]
table(doc, STEPS, widths=[0.3, 3.3, 1.9, 1.0], size=8)
rich(doc, [("The February 28, 2025 target is achievable if the Section 9 items are produced in the first ten days of February. If they are "
            "not, the closing should be moved rather than the conditions waived: the Phase I ESA’s AAI shelf life expires April 26, 2025, and every "
            "week of delay shortens the thirty-month construction period that the August 28, 2027 maturity date assumes.")],
     first_indent=0.5, space_after=10)

rich(doc, [("We would be pleased to discuss any of the foregoing. Please direct questions on the environmental and title items to the "
            "undersigned and questions on the credit analysis to Mr. Forsythe’s group.")], first_indent=0.5, space_after=16)

para(doc, "Respectfully submitted,", size=10.5, space_after=18)
para(doc, "ASHFORD, CROMDALE CONSULTING & LAINE LLP", size=10.5, bold=True, space_after=20)
para(doc, "By: ______________________________", size=10.5, space_after=2)
para(doc, "Katharine “Kate” Drummond, Partner", size=10.5, space_after=2)
para(doc, "Marcus Webb, Associate", size=10.5, space_after=2)
para(doc, "Counsel to Pinnacle Savings Bank, N.A.", size=9.5, italic=True, space_after=0)

# ------------------------------------------------------------------ Appendix A
page_break(doc)
heading2(doc, "Appendix A — Source-to-Issue Log", before=0, after=8, size=11)
rich(doc, [("Each material proposition on which the Draft Agreement relies is recorded below with its source. “Conflict” indicates that "
            "another document in the record states a different proposition.")], first_indent=0.5)
LOG = [
["#", "Proposition", "Source and citation", "Conflict / corroboration", "Draft Agreement"],
["A-1", "Lender is Pinnacle Savings Bank, N.A.; relationship manager David Forsythe; counsel Ashford, Cromdale", "Term Sheet § 1.1; Credit Memorandum cover", "Corroborated", "Preamble; § 15.1"],
["A-2", "Borrower is a North Carolina LLC, SOS No. 1923847, formed March 14, 2019", "Term Sheet § 1.2; Organizational Chart § 1.1; Title Commitment Sch. A ¶ 5", "Corroborated", "§ 5.1"],
["A-3", "Membership: 62% Vasquez-Torres, 28% Brightleaf Investors Group LLC, 10% Osei", "Term Sheet § 1.2; Org. Chart § 1.2; Credit Memorandum § 2.2", "Corroborated", "§ 5.2; Sch. 5.2"],
["A-4", "Brightleaf Investors Group LLC contributed $0; its 28% was issued for arranging mezzanine financing", "Org. Chart §§ 1.3, 2.3; Operating Agreement § 5.1(b)", "Conflict: Credit Memorandum § 2.2 says the Land was funded “through capital calls from all three members”", "§§ 5.2, 5.14; Sch. 5.2"],
["A-5", "Land was acquired by deed from Foster Street Properties LLC, recorded June 12, 2023, at $8,200,000", "Title Commitment Sch. A ¶ 5, ¶ 6; Price: Appraisal § 6.1", "Conflict: Org. Chart / Operating Agreement (contribution at formation); Credit Memorandum (capital calls); Phase I ESA § 2.2 (2022); Appraisal § 6.1 (early 2024)", "§§ 3.7(d), 5.2"],
["A-6", "The Land was funded with $8,200,000 of mezzanine proceeds", "Budget workbook, Detailed Budget line 1.01 and note", "Conflict: Term Sheet §§ 5.1, 5.2 and Credit Memorandum § 5.1 show the Land as Borrower equity and mezzanine proceeds as a source of the $56,700,000 budget", "§§ 3.16, 12.4; Sch. 1.1; Ex. C"],
["A-7", "Mezzanine loan: $9,200,000 at 12.50% fixed, coterminous, 100% equity pledge, PIK during construction", "Term Sheet § 1.4; Credit Memorandum § 4.4; Org. Chart § 1.2", "Corroborated as to terms; principal amount and balance unverified", "§ 1.1; § 12.4; Sch. 1.1"],
["A-8", "Both loans take a pledge of 100% of the membership interests", "Term Sheet §§ 1.4, 8; Org. Chart §§ 1.2, 2.5; Credit Memorandum § 4.2", "Corroborated — the duplication is the issue", "§§ 12.2, 12.3"],
["A-9", "Occupancy: 212 units (142/56/14); 18,400 sf retail in 7 bays; 276 spaces; 287,500 sf GBA", "Term Sheet § 2; Credit Memorandum § 3.1; Appraisal § 3; Phase I ESA § 1", "Corroborated", "§ 1.1 (Improvements)"],
["A-10", "As-is $8,900,000; as-completed $72,800,000; as-stabilized $76,200,000 at a 6.40% cap rate", "Appraisal §§ 2, 6, 10; Term Sheet § 4; Credit Memorandum § 3.3", "Corroborated; recomputed at Section 8 rows 12–13", "§ 3.3"],
["A-11", "Stabilized NOI $4,876,800", "Appraisal § 7; Term Sheet § 4; Credit Memorandum § 6.3", "Corroborated; recomputed at Section 8 rows 8–11; omits the Association assessment", "§ 8.11"],
["A-12", "Total Project Costs $56,700,000; senior $47,500,000; mezzanine $9,200,000; equity $0", "Term Sheet §§ 5.1, 5.2; Credit Memorandum § 5.1; Appraisal § 3; Budget, Summary tab", "Corroborated internally; omits the Existing Mortgage payoff and the items in Section 3.7", "§ 1.1; Ex. C"],
["A-13", "Loan-to-cost 83.77%; maximum 80%", "Term Sheet § 6.1; Credit Memorandum § 5.3; Budget, Key Financial Metrics", "Corroborated; recomputed", "§§ 2.2, 8.1"],
["A-14", "Loan-to-value 65.25% / 62.34%; maximum 65%", "Term Sheet §§ 4, 6.2; Appraisal § 10", "Corroborated; the Credit Memorandum § 6.1 compares to a 70% policy maximum instead", "§ 8.2; Sch. 8.11"],
["A-15", "Interest rate: Daily Simple SOFR + 3.25% / + 3.50%; 1.00% floor; default +5.00%", "Term Sheet § 3.3; Credit Memorandum § 4.1; Budget, Summary tab", "Corroborated", "§§ 2.5, 2.6, 2.11; Ex. E"],
["A-16", "Interest reserve $4,850,000, adequate", "Term Sheet § 10; Credit Memorandum §§ 6.2, 9.2; Budget, Interest Reserve Analysis", "Conflict: surplus of $221,325 at 3.50% SOFR; shortfall of $365,830 at 4.35%; shortfall of $565,000 (Credit Memorandum)", "§§ 2.7, 8.8; Ex. E"],
["A-17", "Draw schedule: 9 draws totaling $47,500,000 with 10% retainage and a $3,275,000 Draw 9", "Term Sheet § 9.2; Credit Memorandum § 7.1; Budget, Draw Schedule tab", "Conflict: 10% retainage is $3,475,000; Draw 9 components total $4,275,000 in the workbook", "§§ 4.1, 4.4; Ex. D"],
["A-18", "Title: first-priority lender’s policy of $47,500,000; exceptions as listed; Triangle Commercial Bank deed of trust unreleased", "Title Commitment Sch. A, B-I ¶ 4, B-II ¶¶ 7–13; Term Sheet § 18; Credit Memorandum § 9.7", "Conflict: Term Sheet § 18 omits items 12 and 13 from its Permitted Exceptions but requires all others to be removed", "§§ 3.2, 3.8; Ex. B"],
["A-19", "REC: former 2,000-gallon diesel UST; contamination above residential but below non-residential standards; 0.38-acre Affected Area", "Phase I ESA §§ 1, 5.2, 8.1; Term Sheet § 17; Credit Memorandum § 8.2", "Corroborated as to condition", "§§ 1.1, 5.10, 10.2"],
["A-20", "NFA Letter dated September 30, 2024 with four conditions: vapor system, non-residential use restriction, soil management plan, deed notice by November 29, 2024", "Phase I ESA § 7; Term Sheet § 17 (omits conditions 2, 3 and 4); Credit Memorandum § 8.2 (omits the soil management plan and deed notice)", "Conflict by omission", "§§ 3.4, 10.2–10.6; Ex. F"],
["A-21", "Fourteen residential units are located above the Affected Area", "Credit Memorandum §§ 8.2, 9.5", "Conflict: Phase I ESA § 8.5 expressly declines to verify; Appraisal § 8 expresses no opinion", "§§ 3.4(f), 10.3"],
["A-22", "Remediation involved excavation of 1,200 cubic yards at a cost of $485,000", "Phase I ESA §§ 6.1, 6.3", "Conflict: 340 cubic yards (Credit Memorandum § 8.2); 320 cubic yards (Appraisal § 8)", "§ 5.10"],
["A-23", "CC&Rs include architectural review, an assessment of $0.12/sf of GBA, and an injunction remedy", "Title Commitment Sch. B-II ¶ 11", "Conflict: Appraisal § 2 states the design has been approved; the title officer states approval has not been evidenced", "§§ 3.12(d), 6.5; Ex. B item 4"],
["A-24", "Operating Agreement requires 75% member approval for financing over $1,000,000, bankruptcy and amendments; permits dilution on unfunded capital calls", "Operating Agreement §§ 3.2, 5.3, 9.1", "Corroborated by the Org. Chart’s own analysis", "§§ 3.6, 7.4, 7.10, 11.4"],
["A-25", "No independent manager, separateness covenants or non-consolidation opinion currently exist", "Org. Chart §§ 1.1, 2.2; Credit Memorandum §§ 2.1, 9.3", "Corroborated", "§§ 3.6, 11.1–11.5"],
["A-26", "Guarantors: net worth $29,800,000 and $11,500,000; liquidity $9,300,000; 25% partial repayment guaranty of $11,875,000", "Term Sheet §§ 1.3, 6.5, 7.3; Credit Memorandum § 2.3; Org. Chart § 1.2", "Corroborated; the per-guarantor versus aggregate cap is ambiguous", "§§ 8.5, 13.3"],
["A-27", "Builder’s risk of $34,750,000; general liability $5,000,000/$10,000,000; umbrella $10,000,000", "Term Sheet § 19; Credit Memorandum § 8.1", "Corroborated; the builder’s risk limit is less than half of the as-completed value", "§ 9.1"],
["A-28", "Property is in Zone X; FEMA panel cited as 3710406400J (2019) and 3720098700J (2009)", "Appraisal § 2; Phase I ESA § 2.3", "Conflict as to the panel and effective date; consistent as to the zone", "§ 3.10; § 9.1(f)"],
["A-29", "Zoning is MU-D and the Project is permitted as of right, with no variance or special use permit", "Term Sheet § 2; Credit Memorandum § 3.1; Appraisal § 2", "Corroborated; the parking-maximum question in Sch. B-II ¶ 12 is unresolved", "§§ 5.5, 3.12"],
["A-30", "Construction is 30 months; Construction Maturity August 28, 2027; Mini-Perm August 28, 2028; extension to February 28, 2029", "Term Sheet §§ 3.2, 7.1; Credit Memorandum § 4.1", "Corroborated; the Term Sheet’s own Completion Guaranty date precedes the projected substantial completion date", "§§ 2.13, 6.2, 13.1"],
]
table(doc, LOG, widths=[0.35, 1.6, 1.6, 1.85, 1.1], size=6.8)

out = "/workspace/output/cover-memorandum.docx"
doc.save(out)
print("saved", out)
