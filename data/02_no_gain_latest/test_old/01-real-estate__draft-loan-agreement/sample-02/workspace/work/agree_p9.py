# -*- coding: utf-8 -*-
import sys; sys.path.insert(0,'/workspace/work')
from dh import *
from docx.enum.text import WD_ALIGN_PARAGRAPH as AL

def _sig(doc, label, name_lines):
    para(doc, label, bold=True, size=10.5, space_before=14, space_after=2)
    para(doc, "By: _________________________________", size=10.5, space_after=2)
    for l in name_lines:
        para(doc, l, size=10.5, space_after=2)

def build_part9(doc):
    # ---------------- SIGNATURES ----------------
    page_break(doc)
    art(doc, "SIGNATURE PAGES")
    para(doc, "IN WITNESS WHEREOF, the parties have executed this Construction-to-Mini-Permanent Loan Agreement as of the "
              "date first written above.")
    para(doc, "LENDER:", bold=True, size=11, space_before=16, space_after=4)
    para(doc, "PINNACLE SAVINGS BANK, N.A.,", bold=True, size=10.5, space_after=2)
    para(doc, "a nationally chartered savings bank", size=10.5, space_after=18)
    para(doc, "By: _________________________________", size=10.5, space_after=2)
    para(doc, "Name: _______________________________", size=10.5, space_after=2)
    para(doc, "Title: ________________________________", size=10.5, space_after=2)
    para(doc, "Date: _________________________________", size=10.5, space_after=24)

    para(doc, "BORROWER:", bold=True, size=11, space_before=8, space_after=4)
    para(doc, "HARBORVIEW CAPITAL PARTNERS LLC,", bold=True, size=10.5, space_after=2)
    para(doc, "a North Carolina limited liability company", size=10.5, space_after=18)
    para(doc, "By: _________________________________", size=10.5, space_after=2)
    para(doc, "Name: Elena Vasquez-Torres", size=10.5, space_after=2)
    para(doc, "Title: Managing Member", size=10.5, space_after=2)
    para(doc, "Date: _________________________________", size=10.5, space_after=24)

    para(doc, "GUARANTORS:", bold=True, size=11, space_before=8, space_after=8)
    para(doc, "_____________________________________", size=10.5, space_after=2)
    para(doc, "ELENA VASQUEZ-TORRES, individually", size=10.5, space_after=2)
    para(doc, "Date: _________________________________", size=10.5, space_after=22)
    para(doc, "_____________________________________", size=10.5, space_after=2)
    para(doc, "REGINALD K. OSEI, individually", size=10.5, space_after=2)
    para(doc, "Date: _________________________________", size=10.5, space_after=18)
    para(doc, "[Signature page to Construction-to-Mini-Permanent Loan Agreement — Loan No. CRE-2025-0342 — Harborview Capital "
              "Partners LLC / The Piedmont at Brightleaf]", italic=True, size=9, align=AL.CENTER, space_before=18)
    page_break(doc)

    # ---------------- SCHEDULE 1 (landscape) ----------------
    new_section(doc, landscape=True, margins=(0.65, 0.65, 0.75, 0.75))
    art(doc, "SCHEDULE 1 — DRAW SCHEDULE AND CONSTRUCTION MILESTONES")
    para(doc, "Capitalized terms used in this Schedule have the meanings given in the Agreement. Advances shall be made only in "
              "accordance with this Schedule 1 and Article IV. The percentages in the “% Complete” column are "
              "measured against the GMP of $34,750,000 on a cumulative basis, inclusive of Retainage.", size=10)
    rows = [
        ["1", "Closing — soft costs, Interest Reserve, Origination Fee", "0%", "Feb. 2025", "—", "—", "4,150,000", "—", "475,000", "9,475,000", "9,475,000"],
        ["2", "Foundation complete", "15%", "June 2025", "5,212,500", "(521,250)", "—", "—", "—", "4,691,250", "14,166,250"],
        ["3", "Structural frame — Level 3", "35%", "Nov. 2025", "6,950,000", "(695,000)", "—", "—", "—", "6,255,000", "20,421,250"],
        ["4", "Structural frame — topped out", "55%", "Apr. 2026", "6,950,000", "(695,000)", "—", "440,000", "458,750", "7,153,750", "27,575,000"],
        ["5", "Building envelope complete", "70%", "Aug. 2026", "5,212,500", "(521,250)", "—", "—", "—", "4,691,250", "32,266,250"],
        ["6", "MEP rough-in complete", "80%", "Nov. 2026", "3,475,000", "(347,500)", "—", "400,000", "458,750", "3,986,250", "36,252,500"],
        ["7", "Interior finish — 50% of units", "90%", "Mar. 2027", "3,475,000", "(347,500)", "—", "—", "—", "3,127,500", "39,380,000"],
        ["8", "Substantial Completion / TCO", "100%", "Aug. 2027", "3,475,000", "(347,500)", "—", "600,000", "458,750", "4,186,250", "43,566,250"],
        ["9", "Retainage release and final Developer Fee", "Post-CO", "Oct. 2027", "—", "3,475,000", "—", "—", "458,750", "3,933,750", "47,500,000"],
        ["", "TOTAL", "", "", "34,750,000", "0", "4,150,000", "1,440,000", "1,835,000", "47,500,000", ""],
    ]
    table(doc, ["No.", "Milestone", "% Comp.", "Date", "Gross Hard Cost", "Retainage",
                "Soft Costs", "Contin-gency", "Dev. Fee", "Total Advance", "Cumulat-ive"],
          rows, widths=[0.45, 1.75, 0.68, 0.82, 0.85, 0.8, 0.8, 0.75, 0.8, 0.85, 0.88], size=8.5,
          align_right_cols=(2,4,5,6,7,8,9,10), bold_last_row=True)
    para(doc, "Notes to Schedule 1:", bold=True, size=9.5, space_before=4, space_after=3)
    notes = [
        "Draw 1 is the Initial Advance and consists of soft costs of $4,150,000, the Interest Reserve of $4,850,000 and the "
        "Origination Fee of $475,000.",
        "Retainage of ten percent (10%) is withheld from each hard cost Advance, aggregating $3,475,000 (10% of the $34,750,000 "
        "GMP), and is released as Draw 9 upon satisfaction of Section 4.4.",
        "The Contingency ($1,440,000) is disbursed only upon Lender's approval of an approved change order or cost under "
        "Section 4.5, in the amounts shown and subject to the sub-limits of $1,140,000 (hard costs) and $300,000 (soft costs).",
        "The Developer Fee column reflects only the $1,835,000 portion funded from the Loan. The remaining $1,000,000 of the "
        "$2,835,000 Developer Fee is to be funded from sources other than the Loan, and no portion of the Developer Fee may be "
        "disbursed while a Default or Event of Default exists or before Substantial Completion (Section 8.7).",
        "The aggregate of all Advances shall not exceed $47,500,000. Amounts not drawn may not be reborrowed.",
        "Estimated dates are for reference only. Failure to achieve a milestone within sixty (60) days of the estimated date "
        "constitutes an Event of Default under Section 13.6.",
    ]
    for n in notes:
        bullet(doc, n, size=9)
    para(doc, "Reconciliation: $9,475,000 + $4,691,250 + $6,255,000 + $7,153,750 + $4,691,250 + $3,986,250 + $3,127,500 + "
              "$4,186,250 + $3,933,750 = $47,500,000.", size=9, italic=True, space_before=4)
    para(doc, "[Drafting Note: Section 9.2 of the Term Sheet and Section 7.1 of the Credit Memorandum present a nine-draw table "
              "totaling $47,500,000 in which Draws 2 through 8 aggregate $34,750,000 (100% of the GMP) without withholding "
              "Retainage, and in which Draw 9 of $3,275,000 is described as a retainage release although 10% of the GMP is "
              "$3,475,000. The $3,275,000 figure equals exactly the Contingency ($1,440,000) plus the Loan-funded Developer Fee "
              "($1,835,000). The draw schedule delivered by Borrower on January 8, 2025 shows $3,475,000 for Draw 9 but its "
              "component columns total $48,500,000 against a stated total of $47,500,000, a $1,000,000 imbalance attributable to "
              "the $1,000,000 of Developer Fee said to be funded by the Mezzanine Loan. Schedule 1 conforms the schedule to the "
              "10% retainage requirement of Section 9.1 of the Term Sheet and separately identifies the Contingency and Developer "
              "Fee. See Cover Memorandum Issue No. 5.]", size=9)
    # ---------------- SCHEDULE 2 ----------------
    new_section(doc, landscape=False, margins=(1.0, 1.0, 1.0, 1.0))
    art(doc, "SCHEDULE 2 — PROJECT BUDGET AND SOURCES AND USES OF FUNDS")
    sec_h(doc, "Part A — Uses of Funds (Approved Project Budget)")
    uses = [
        ["Land acquisition (previously closed)", "8,200,000", "—", "14.46%"],
        ["Hard construction costs (GMP — Graystone Construction Group Inc.)", "34,750,000", "—", "61.29%"],
        ["Soft costs (architecture, engineering, permits, legal, accounting, inspection, insurance, marketing)", "4,150,000", "—", "7.32%"],
        ["Interest Reserve", "4,850,000", "—", "8.55%"],
        ["Origination Fee (1.00% of Loan Amount)", "475,000", "—", "0.84%"],
        ["Developer Fee (5.00% of Total Project Costs)", "1,835,000", "1,000,000", "5.00%"],
        ["Contingency (hard $1,140,000; soft $300,000)", "1,440,000", "—", "2.54%"],
        ["TOTAL", "47,500,000", "9,200,000", "100.00%"],
    ]
    table(doc, ["Use of Funds", "Loan", "Mezzanine", "% of Total"], uses,
          widths=[3.3, 1.1, 1.0, 1.0], size=9, align_right_cols=(1,2,3), bold_last_row=True)
    para(doc, "Total Uses: $56,700,000.", size=9.5, italic=True)

    sec_h(doc, "Part B — Sources of Funds (to be conformed at Closing)")
    src = [
        ["Senior Construction Loan — Lender", "47,500,000", "78.15%", "Fixed commitment"],
        ["Mezzanine Loan — Brightleaf Mezzanine Capital LLC", "9,200,000", "15.14%", "12.50% fixed; PIK during Construction Period"],
        ["Equity Contribution (Equity Escrow Account)", "[4,080,000]", "[6.71%]", "Verified third-party source required by Section 3.7"],
        ["TOTAL", "[60,780,000]", "100.00%", ""],
    ]
    table(doc, ["Source of Funds", "Amount", "% of Total", "Notes"], src,
          widths=[2.35, 1.0, 0.75, 2.3], size=9, align_right_cols=(1,2), bold_last_row=True)
    para(doc, "Reconciliation to the corrected budget:", bold=True, size=9.5, space_before=4, space_after=3)
    recon = [
        "Total Project Costs per the budget certified by Borrower and reviewed by the appraiser: $56,700,000.",
        "Add: payoff of the deed of trust recorded in Book 6215, Page 892, Durham County Registry (Triangle Commercial Bank; "
        "original principal $3,400,000; outstanding balance to be confirmed by payoff letter): up to $[3,400,000].",
        "Add: demolition and environmental remediation costs incurred before Closing (approximately $680,000 per the appraisal; "
        "remediation alone approximately $485,000 per the Phase I ESA), which are not line items of the $56,700,000 budget: "
        "$[680,000].",
        "Corrected Total Project Costs: $[60,780,000]. Less the Loan ($47,500,000) and the Mezzanine Loan ($9,200,000) = "
        "required Equity Contribution of $[4,080,000].",
        "Loan-to-Cost Ratio on the corrected budget: $47,500,000 \u00f7 $[60,780,000] = 78.15% (within the 80% maximum of "
        "Section 9.1). On the uncorrected budget the ratio is 83.77%, which exceeds the maximum by $2,140,000.",
        "If the payoff and pre-Closing costs are not added to Total Project Costs, the Equity Contribution of $2,140,000 "
        "required by the Credit Memorandum merely restores the 80% ratio on a budget that omits a required closing use; the "
        "payoff would then be unfunded.",
    ]
    for r in recon:
        bullet(doc, r, size=9)
    para(doc, "[Drafting Note: Schedule 2 Part B and the reconciliation above are presented in brackets because the record does "
              "not disclose (a) the outstanding balance of the Triangle Commercial Bank loan, (b) whether the $680,000 of "
              "pre-Closing site costs have been paid and by whom, or (c) the actual source of the $8,200,000 land cost. Line item "
              "1.01 of Borrower's project budget states that the land was \u201cFunded by Mezzanine Loan\u201d; Sections 5.1 and "
              "5.2 of the Term Sheet and Section 2.2 of the Credit Memorandum state that it was contributed as equity by the "
              "members; and Section 1.3 of the organizational materials states that it was contributed by Ms. Vasquez-Torres "
              "personally. Only the first description balances the sources and uses as presented. See Cover Memorandum Issues "
              "Nos. 1, 2 and 3.]", size=9)
    page_break(doc)

    # ---------------- SCHEDULE 3 ----------------
    art(doc, "SCHEDULE 3 — PERMITTED EXCEPTIONS")
    para(doc, "The Title Policy may contain only the following exceptions, together with such other exceptions as Lender may "
              "approve in writing:", size=10)
    perm = [
        ["1", "Standard printed exceptions (rights of parties in possession; facts disclosed by survey; easements or claims of "
              "easements not of record) — to be removed to the extent permitted by the Title Company upon delivery of the ALTA "
              "survey and an owner's affidavit of possession.", "Delete/modify as stated"],
        ["2", "Ad valorem real property taxes for the fiscal year 2025 and subsequent years, not yet due and payable. "
              "(2024 taxes: Parcel 0821-04-72-3341 — $29,847.12; Parcel 0821-04-72-4102 — $19,218.44; both paid.)", "Permitted"],
        ["3", "Easement in favor of Duke Energy Carolinas, LLC, 20 feet in width along the western boundary of Parcel "
              "0821-04-72-3341, recorded in Book 4387, Page 621, Durham County Registry (March 22, 1997).", "Permitted, subject "
              "to Lender's review of the instrument and the survey"],
        ["4", "Stormwater management easement in favor of the City of Durham affecting approximately 0.22 acres in the southern "
              "portion of Parcel 0821-04-72-3341, recorded in Book 7421, Page 212, Durham County Registry (April 8, 2022); "
              "depicted on plat recorded in Plat Book 232, Page 91.", "Permitted, subject to confirmation that no building "
              "footprint, parking or stormwater credit is impaired"],
        ["5", "Declaration of Covenants, Conditions and Restrictions recorded by Brightleaf Historic District Association, Inc. "
              "in Book 6984, Page 1155, Durham County Registry (November 3, 2014), as amended by First Amendment recorded in "
              "Book 7102, Page 388 (June 19, 2017), including the architectural review, assessment ($0.12 per square foot of "
              "gross building area per annum) and use restriction provisions.", "Permitted, subject to Section 3.6"],
        ["6", "Terms, conditions, easements and restrictions imposed by the City of Durham Unified Development Ordinance and the "
              "MU-D zoning district.", "Permitted"],
        ["7", "Deed notice and declaration of land use restriction to be recorded pursuant to Condition 4 of the NCDEQ No Further "
              "Action Letter dated September 30, 2024, with respect to the Affected Area (approximately 0.38 acres).", "Permitted "
              "only in the form approved by Lender and only upon recordation as required by Section 12.5"],
    ]
    table(doc, ["No.", "Exception", "Status"], perm, widths=[0.4, 4.05, 2.0], size=9)
    para(doc, "The following matters shown in Schedule B-II of Commitment No. NC-2024-88712 must be removed, released or "
              "satisfied of record at or before Closing and shall not be Permitted Exceptions:", bold=True, size=9.5, space_before=4)
    bullet(doc, "Deed of trust from Foster Street Properties LLC to the Trustee for the benefit of Triangle Commercial Bank, "
                "dated September 14, 2018, recorded in Book 6215, Page 892, Durham County Registry, securing an original "
                "principal amount of $3,400,000 (see Section 3.14).", size=9)
    bullet(doc, "Any mechanics' or materialmen's lien, lis pendens, judgment, state or federal tax lien, or other monetary "
                "encumbrance of record.", size=9)
    bullet(doc, "Any encroachment, boundary line dispute, or matter of survey that Lender's survey review does not approve.", size=9)
    para(doc, "[Drafting Note: Section 18 of the Term Sheet identifies only four Permitted Exceptions (standard printed "
              "exceptions, the Duke Energy easement, the City stormwater easement and the CC&Rs). It does not mention the tax "
              "exception, the UDO/zoning exception, the possession exception or the First Amendment to the CC&Rs recorded in "
              "Book 7102, Page 388. Schedule 3 conforms the list to the Title Commitment. See Cover Memorandum Issue No. 20.]",
         size=9)
    page_break(doc)

    # ---------------- SCHEDULE 4 ----------------
    art(doc, "SCHEDULE 4 — NCDEQ NO FURTHER ACTION CONDITIONS AND ENVIRONMENTAL COMPLIANCE REQUIREMENTS")
    para(doc, "The following requirements derive from the No Further Action determination letter issued by NCDEQ (Inactive "
              "Hazardous Sites Branch) dated September 30, 2024 for Site ID IHSB-24-1203 and Incident No. NONUST-24-0847, as "
              "summarized in the Phase I ESA. Each requirement is a continuing covenant of Borrower under Article XII and "
              "Section 7.8.", size=10)
    nfa = [
        ["1", "Soil vapor mitigation system beneath any enclosed structure constructed over the Affected Area: passive sub-slab "
              "depressurization with capability of conversion to active depressurization; designed by a North Carolina licensed "
              "professional engineer; as-built drawings and performance verification report submitted to NCDEQ within 90 days "
              "after completion of the building foundation in the Affected Area.", "Design at Closing; installation with the "
              "parking structure / podium; NCDEQ submittal within 90 days of foundation completion; maintenance throughout the "
              "Loan term and thereafter while the NFA Letter remains in effect."],
        ["2", "Land use restriction: the Affected Area (approximately 0.38 acres in the northeast corner of Parcel "
              "0821-04-72-4102) is restricted to non-residential use. Any change to residential or other sensitive use requires "
              "additional investigation and a modification of the NFA determination.", "No residential occupancy in the Affected "
              "Area; overlay plan and Architect certification at Closing; Lender consent and NCDEQ modification required before "
              "any change (Section 12.2)."],
        ["3", "Soil management plan: NCDEQ-approved plan governing all excavation, grading and subsurface disturbance in the "
              "Affected Area, including screening, stockpiling, dust control, worker health and safety and disposal.", "NCDEQ "
              "approval before any subsurface disturbance (Section 3.5(c) and Section 12.4); compliance certification with each "
              "affected Draw Request."],
        ["4", "Deed notice: recorded notice in the Durham County Registry of Deeds within 60 days after September 30, 2024 "
              "(i.e., by November 29, 2024), describing the Affected Area, the residual contamination and the land use "
              "restriction.", "Recordation before Closing with evidence of recording and a title date-down (Section 12.5); "
              "Permitted Exception in the Title Policy."],
        ["5", "Regulatory status: the NFA determination is conditional and does not constitute clean closure; residual soil "
              "contamination remains above residential Preliminary Soil Remediation Goals (TPH-DRO up to 847 mg/kg against a "
              "100 mg/kg residential goal; benzene up to 0.42 mg/kg against 0.065 mg/kg); soil gas benzene up to 185 "
              "\u00b5g/m\u00b3 against a 31 \u00b5g/m\u00b3 screening level.", "No action that could cause reopening; reporting "
              "to Lender under Section 12.6; environmental indemnity and, if required, PLL insurance."],
    ]
    table(doc, ["No.", "Requirement", "Loan Document Timing and Covenant"], nfa, widths=[0.4, 3.6, 2.45], size=8.5)
    page_break(doc)

    # ---------------- SCHEDULE 5 ----------------
    art(doc, "SCHEDULE 5 — REQUIRED INSURANCE")
    ins = [
        ["Builder's Risk (all-risk, replacement cost, including materials in transit and stored off-site)", "Not less than "
         "$34,750,000 (the GMP)", "Lender as mortgagee and loss payee", "Construction Period through final completion"],
        ["Commercial General Liability (premises, products/completed operations, contractual, personal and advertising injury)",
         "$5,000,000 per occurrence / $10,000,000 aggregate", "Lender as additional insured", "Throughout the Loan term"],
        ["Umbrella / Excess Liability", "$10,000,000 per occurrence and aggregate", "Lender as additional insured", "Throughout "
         "the Loan term"],
        ["Workers' Compensation and Employer's Liability", "Statutory (N.C.G.S. Chapter 97); employer's liability "
         "$1,000,000", "Lender as waiver of subrogation", "Throughout the Loan term"],
        ["Property insurance (special form, replacement cost, agreed amount)", "Full insurable replacement value of the "
         "completed Project", "Lender as mortgagee and loss payee", "From Substantial Completion through the Mini-Perm Period"],
        ["Business income / rent loss", "Not less than 12 months of gross rental income and continuing expenses, including debt "
         "service", "Lender as loss payee", "From Substantial Completion through the Mini-Perm Period"],
        ["Flood insurance", "As required by the National Flood Insurance Act if any portion of the Project is in a Special "
         "Flood Hazard Area", "Lender as mortgagee and loss payee", "Throughout the Loan term if applicable"],
        ["Equipment breakdown / boiler and machinery", "Replacement cost of covered equipment", "Lender as loss payee", "From "
         "Substantial Completion through the Mini-Perm Period"],
        ["Professional liability — Architect (Meridian Design Collective PC)", "$2,000,000 per claim", "Certificate to Lender",
         "Throughout construction and for the applicable statute of repose period"],
        ["Pollution legal liability (if required by Lender under Section 12.8)", "Amount to be determined by Lender",
         "Lender as additional insured and loss payee", "Loan term plus such period as Lender requires"],
    ]
    table(doc, ["Coverage", "Limit / Requirement", "Lender's Interest", "Period"], ins,
          widths=[2.4, 1.7, 1.4, 0.95], size=8.5)
    para(doc, "All policies shall be with insurers rated A- or better by A.M. Best, shall provide not less than thirty (30) days' "
              "prior written notice of cancellation, non-renewal or material reduction in coverage (ten (10) days for "
              "non-payment of premium), shall waive subrogation against Lender, and shall be primary as to Lender's interests.",
         size=9.5)
    page_break(doc)

    # ---------------- SCHEDULE 6 ----------------
    art(doc, "SCHEDULE 6 — FINANCIAL COVENANTS AND COMPLIANCE CERTIFICATE")
    sec_h(doc, "Part A — Covenant Summary")
    cov = [
        ["Loan-to-Cost Ratio", "Not greater than 80%", "Each Draw Request and at Closing", "Section 9.1", "83.77% at Closing on "
         "the uncorrected budget; 78.15% on the corrected budget"],
        ["Loan-to-Value (as-completed)", "Not greater than 65%", "At Closing; on reappraisal", "Section 9.2",
         "65.25% at Closing ($47.5M \u00f7 $72.8M)"],
        ["Loan-to-Value (as-stabilized)", "Not greater than 65%", "On reappraisal; at extension", "Section 9.2", "62.34% at "
         "Closing ($47.5M \u00f7 $76.2M)"],
        ["Debt Service Coverage Ratio", "Not less than 1.25x", "Commencement of Mini-Perm Period and quarterly thereafter",
         "Section 9.3", "1.31x at 7.85% interest-only; 1.04x at +200 bps"],
        ["Borrower Net Worth", "Not less than $12,000,000", "At Closing and annually", "Section 9.4", "$14,200,000 represented"],
        ["Guarantor combined Liquidity", "Not less than $5,000,000", "Quarterly", "Section 9.5", "$9,300,000 represented"],
        ["Interest Reserve adequacy", "Sufficient to pay interest through the Construction Maturity Date", "Each Draw Request "
         "and quarterly", "Section 5.4", "$4,850,000; adequate only if SOFR averages 3.82% or less"],
        ["Combined leverage (information only)", "Not a covenant", "—", "—", "100% of Total Project Costs at Closing "
         "($47.5M + $9.2M \u00f7 $56.7M)"],
    ]
    table(doc, ["Covenant", "Required Level", "Testing", "Section", "Position at Closing"], cov,
          widths=[1.25, 1.3, 1.45, 0.7, 1.75], size=8.5)

    sec_h(doc, "Section 6.19 of the Agreement — Members and Membership Interests")
    mem = [["Elena Vasquez-Torres", "Individual", "62%", "Managing Member; Guarantor; pledgor"],
           ["Brightleaf Investors Group LLC (NC SOS No. 2045612)", "North Carolina LLC", "28%", "Member; Affiliate of Mezzanine "
            "Lender; pledgor"],
           ["Reginald K. Osei", "Individual", "10%", "Member; Guarantor; pledgor"],
           ["TOTAL", "", "100%", ""]]
    table(doc, ["Member", "Type", "Interest", "Role"], mem, widths=[2.4, 1.35, 0.7, 2.0], size=9, align_right_cols=(2,),
          bold_last_row=True)
    page_break(doc)

    # ---------------- SCHEDULE 7 ----------------
    art(doc, "SCHEDULE 7 — NOTICE ADDRESSES")
    sec_h(doc, "Lender")
    para(doc, "Pinnacle Savings Bank, N.A.\nCommercial Real Estate Lending Division\n215 South Tryon Street, 18th Floor\n"
              "Charlotte, North Carolina 28202\nAttention: David Forsythe, Senior Vice President\n"
              "Email: dforsythe@pinnaclebank.example", size=10)
    para(doc, "With a copy to (which shall not constitute notice):", italic=True, size=10, space_before=6)
    para(doc, "Ashford, Cromdale Consulting & Laine LLP\n411 South Tryon Street, Suite 2800\nCharlotte, North Carolina 28202\n"
              "Attention: Katharine Drummond; Marcus Webb", size=10)
    sec_h(doc, "Borrower")
    para(doc, "Harborview Capital Partners LLC\n400 West Main Street, Suite 310\nDurham, North Carolina 27701\n"
              "Attention: Elena Vasquez-Torres, Managing Member", size=10)
    para(doc, "With a copy to (which shall not constitute notice):", italic=True, size=10, space_before=6)
    para(doc, "Calloway & Strauss PLLC\n324 Blackwell Street, Suite 200\nDurham, North Carolina 27701\n"
              "Attention: Jonathan F. Ngo", size=10)
    sec_h(doc, "Guarantors")
    para(doc, "Elena Vasquez-Torres\n[Address to be confirmed — Durham, North Carolina]\n"
              "Reginald K. Osei\n[Address to be confirmed — Chapel Hill, North Carolina]", size=10)
    sec_h(doc, "Title Company")
    para(doc, "Aldersgate Title & Escrow Inc.\n307 West Chapel Hill Street, Suite 400\nDurham, North Carolina 27701\n"
              "Attention: Patricia Langley, Escrow Officer", size=10)
    page_break(doc)

    # ---------------- EXHIBITS ----------------
    art(doc, "EXHIBIT A — LEGAL DESCRIPTION")
    para(doc, "The Land is described as follows, as confirmed by the ALTA/NSPS survey to be delivered under Section 3.4:")
    para(doc, "Parcel 1 (Durham County PIN 0821-04-72-3341 — 601 Foster Street): being all of that certain lot, tract or parcel "
              "situated in the City of Durham, Durham County, North Carolina, BEGINNING at an existing iron pipe in the eastern "
              "right-of-way margin of Foster Street (60-foot public right-of-way), South 02\u00b014'33\u201d West, 312.47 feet "
              "from the intersection of the eastern right-of-way margin of Foster Street with the southern right-of-way margin of "
              "West Corporation Street; thence South 02\u00b014'33\u201d West 298.62 feet; thence South 87\u00b045'27\u201d East "
              "305.41 feet; thence North 02\u00b014'33\u201d East 298.62 feet; thence North 87\u00b045'27\u201d West 305.41 feet "
              "to the point of BEGINNING, containing approximately 2.09 acres, as shown on the plat recorded in Plat Book 218, "
              "Page 47, Durham County Registry, and being the same property conveyed to Harborview Capital Partners LLC by "
              "Special Warranty Deed recorded in Book 7598, Page 443.", size=10)
    para(doc, "Parcel 2 (Durham County PIN 0821-04-72-4102 — 615 Foster Street): BEGINNING at an existing iron pipe in the "
              "eastern right-of-way margin of Foster Street, being the southwestern corner of Parcel 1; thence South "
              "02\u00b014'33\u201d West 201.88 feet; thence South 87\u00b045'27\u201d East 297.63 feet; thence North "
              "02\u00b014'33\u201d East 201.88 feet; thence along the southern boundary of Parcel 1, North 87\u00b045'27\u201d West "
              "297.63 feet to the point of BEGINNING, containing approximately 1.38 acres, as shown on the plat recorded in Plat "
              "Book 218, Page 48, Durham County Registry, and being the same property conveyed to Harborview Capital Partners LLC "
              "by Special Warranty Deed recorded in Book 7598, Page 445.", size=10)
    para(doc, "Total combined land area: approximately 3.47 acres (151,288 square feet per the metes and bounds).", size=10,
         italic=True)
    para(doc, "[Drafting Note: The descriptions above are transcribed from Schedule A of Commitment No. NC-2024-88712 and are "
              "subject to confirmation by the ALTA survey. The acreages reconcile to the metes and bounds (2.094 and 1.379 "
              "acres; 3.473 acres combined), which indicates that the parcel acreages stated in the Phase I ESA (1.89 and 1.58 "
              "acres) are incorrect. The Phase I ESA also describes Parcel 0821-04-72-3341 as the western parcel and Parcel "
              "0821-04-72-4102 as the eastern parcel with frontage on Foster Street to the north, which is inconsistent with the "
              "legal descriptions (north and south parcels, Foster Street along the western boundary) and with the appraisal "
              "(approximately 420 feet of frontage along Foster Street on the western boundary, against 500.50 feet per the "
              "metes and bounds). The location of the 0.38-acre Affected Area must be fixed by survey before the non-residential "
              "use restriction can be reconciled to the building plans. See Cover Memorandum Issue No. 7.]", size=9)
    page_break(doc)

    art(doc, "EXHIBIT B — FORM OF DRAW REQUEST AND BORROWER'S CERTIFICATE")
    para(doc, "Draw Request No. ____  Dated: ____________  Requested Advance Date: ____________  Amount Requested: $__________")
    para(doc, "To: Pinnacle Savings Bank, N.A., Commercial Real Estate Lending Division, 215 South Tryon Street, 18th Floor, "
              "Charlotte, North Carolina 28202.", size=10)
    para(doc, "The undersigned, on behalf of Harborview Capital Partners LLC, certifies to Pinnacle Savings Bank, N.A. as follows:",
         size=10, space_before=8)
    for i, x in enumerate([
        "The milestone described as Draw No. ____ in Schedule 1 has been achieved as of ____________, and the work has been "
        "performed in accordance with the Approved Plans and Specifications.",
        "The aggregate amount requested does not exceed the applicable line item of the Approved Project Budget, and the "
        "undisbursed Loan proceeds, the Contingency and Borrower's equity are sufficient to complete the Project, as confirmed "
        "by the Construction Inspector and the attached budget reconciliation.",
        "Attached are the AIA G702 and G703 applications certified by the Architect and the general contractor, conditional "
        "partial lien waivers from the general contractor and all subcontractors and suppliers, the Construction Inspector's "
        "report, the title date-down endorsement, evidence of insurance, and the interest reserve adequacy certification "
        "required by Section 5.4.",
        "No Default or Event of Default exists, and each representation and warranty in Article VI is true and correct in all "
        "material respects as of the date hereof.",
        "The work covered by this Draw Request does not include any work in or over the Affected Area, or, if it does, the "
        "requirements of Section 12.7 have been satisfied and attached hereto.",
        "Borrower's equity has been fully disbursed and applied to Project costs, other than with respect to Draw No. 1.",
    ], 1):
        numbered(doc, "(%d)" % i, x, indent=0.4, hang=0.25, size=10)
    para(doc, "HARBORVIEW CAPITAL PARTNERS LLC", bold=True, size=10, space_before=14)
    para(doc, "By: ______________________________     Name: Elena Vasquez-Torres     Title: Managing Member", size=10)
    para(doc, "Certified by: __________________________ (Construction Inspector)     Date: ______________", size=10, space_before=10)
    page_break(doc)

    art(doc, "EXHIBIT C — FORM OF COMPLIANCE CERTIFICATE")
    para(doc, "The undersigned, the Managing Member of Harborview Capital Partners LLC, certifies to Pinnacle Savings Bank, N.A. "
              "that, as of ____________ (the \u201cTest Date\u201d), the following calculations are true and correct and were "
              "derived from the books and records of Borrower:", size=10)
    crows = [["Total Project Costs (Section 9.1(b) and (c))", "$", ""],
             ["Outstanding principal balance of the Loan", "$", ""],
             ["Loan-to-Cost Ratio (maximum 80%)", "", "%"],
             ["As-completed appraised value / Loan-to-Value (maximum 65%)", "$", "%"],
             ["As-stabilized appraised value / Loan-to-Value (maximum 65%)", "$", "%"],
             ["Net operating income (trailing twelve months, annualized)", "$", ""],
             ["Annual debt service at the then-current Interest Rate", "$", ""],
             ["Debt Service Coverage Ratio (minimum 1.25x)", "", "x"],
             ["Borrower's Net Worth (Section 9.4(c)) (minimum $12,000,000)", "$", ""],
             ["Guarantors' combined Liquidity (minimum $5,000,000)", "$", ""],
             ["Interest Reserve balance / projected interest to Construction Maturity", "$", ""]]
    table(doc, ["Covenant", "Amount", "Ratio"], crows, widths=[3.65, 1.4, 1.4], size=9)
    para(doc, "The undersigned further certifies that no Default or Event of Default exists, that no condition exists that with "
              "notice or lapse of time would constitute a Default or Event of Default, that all representations and warranties "
              "remain true and correct in all material respects, and that Borrower is in compliance with the SPE Covenants, the "
              "NFA Letter conditions and the Intercreditor Agreement.", size=10)
    para(doc, "HARBORVIEW CAPITAL PARTNERS LLC", bold=True, size=10, space_before=14)
    para(doc, "By: ______________________________     Name: Elena Vasquez-Torres     Title: Managing Member     "
              "Date: ____________", size=10)
