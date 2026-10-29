# -*- coding: utf-8 -*-
import sys; sys.path.insert(0,'/workspace/work')
from dh import *
from docx.enum.text import WD_ALIGN_PARAGRAPH as AL

def build_p4(doc):
    art(doc, "V.  VERIFIED COMPUTATIONS AND RECONCILIATIONS")
    para(doc, "Every figure used in this memorandum and in the draft Loan Agreement was recomputed from the source components. "
              "Where a source document states a total, we checked the total against its components rather than accepting it. The "
              "results are set out below; differences from the Record are noted.", size=10)

    sub_h(doc, "V.1  Sources and uses \u2014 does the capital stack balance?")
    rows = [
        ["Senior construction loan", "47,500,000", "47,500,000", "\u2014", "Ties"],
        ["Mezzanine loan", "9,200,000", "9,200,000", "\u2014", "Ties"],
        ["Borrower cash equity", "0", "0", "\u2014", "Consistent with zero equity"],
        ["Land contribution (in-kind)", "not shown as a source", "0", "\u2014", "Cannot be a source: see Issue 1"],
        ["TOTAL SOURCES", "56,700,000", "56,700,000", "\u2014", "Balances only if mezzanine funded the land"],
        ["", "", "", "", ""],
        ["Land acquisition", "8,200,000", "8,200,000", "\u2014", "Funded, per Detailed Budget, by mezzanine"],
        ["Hard construction (GMP)", "34,750,000", "34,750,000", "\u2014", "Ties to GMP"],
        ["Soft costs", "4,150,000", "4,150,000", "\u2014", "Line items sum to $4,150,000"],
        ["Interest reserve", "4,850,000", "4,850,000", "\u2014", "Adequacy: Issue 12"],
        ["Origination fee (1.00%)", "475,000", "475,000", "\u2014", "Ties"],
        ["Developer fee (5.00%)", "2,835,000", "2,835,000", "\u2014", "Circular definition; 5.26% of other costs"],
        ["Contingency", "1,440,000", "1,440,000", "\u2014", "Hard $1,140,000 (3.28%) + soft $300,000 (7.23%)"],
        ["TOTAL USES", "56,700,000", "56,700,000", "\u2014", "Ties"],
        ["", "", "", "", ""],
        ["Omitted uses (not budgeted)", "\u2014", "up to 4,080,000", "\u2014", "Payoff up to $3,400,000 + site costs ~$680,000"],
        ["CORRECTED USES", "\u2014", "60,780,000", "\u2014", "Requires equity of $4,080,000 (Issue 3)"],
    ]
    table(doc, ["Item", "Record", "Recomputed", "Difference", "Comment"], rows,
          widths=[1.95, 1.1, 1.05, 0.85, 1.5], size=8.5, align_right_cols=(1,2,3))

    sub_h(doc, "V.2  Credit metrics")
    rows = [
        ["Loan-to-cost", "$47,500,000 \u00f7 $56,700,000", "83.77%", "Maximum 80%", "Excess $2,140,000", "Fails"],
        ["Loan-to-cost (corrected)", "$47,500,000 \u00f7 $60,780,000", "78.15%", "Maximum 80%", "Complies only on corrected budget", "Pass (corrected)"],
        ["LTV as-completed", "$47,500,000 \u00f7 $72,800,000", "65.25%", "Maximum 65%", "Excess $180,000", "Fails"],
        ["LTV as-stabilized", "$47,500,000 \u00f7 $76,200,000", "62.34%", "Maximum 65%", "\u2014", "Pass"],
        ["Cap rate (implied)", "$4,876,800 \u00f7 $76,200,000", "6.40%", "\u2014", "Appraiser's selected rate", "Ties"],
        ["DSCR (senior, I/O, 7.85%)", "$4,876,800 \u00f7 $3,728,750", "1.31x", "Minimum 1.25x", "\u2014", "Pass"],
        ["DSCR (+200 bps, 9.85%)", "$4,876,800 \u00f7 $4,678,750", "1.04x", "Minimum 1.25x", "\u2014", "Fails"],
        ["Combined DSCR (senior + mezz 12.50%)", "$4,876,800 \u00f7 $4,878,750", "1.00x", "Not tested", "Excludes PIK accrual", "Not tested"],
        ["Combined LTV (senior + mezz + PIK at 8/2028)", "$60,725,000 \u00f7 $76,200,000", "79.7%", "Not tested", "\u2014", "Not tested"],
        ["Combined leverage at closing", "($47,500,000 + $9,200,000) \u00f7 $56,700,000", "100.0%", "\u2014", "Zero equity cushion", "Disclosed"],
        ["HVCRE contributed capital (as asserted)", "$10,340,000 \u00f7 $72,800,000", "14.20%", "15% threshold", "$580,000 short", "HVCRE applies"],
        ["HVCRE contributed capital (if land was debt-funded)", "$2,140,000 \u00f7 $72,800,000", "2.94%", "15% threshold", "\u2014", "HVCRE clearly applies"],
    ]
    table(doc, ["Metric", "Computation", "Result", "Standard", "Comment", "Status"], rows,
          widths=[1.5, 1.7, 0.62, 0.8, 1.35, 0.53], size=8, align_right_cols=(2,))

    sub_h(doc, "V.3  Interest reserve \u2014 independent month-by-month recomputation")
    para(doc, "Assumptions: draw timing per the Draw Schedule (Draw 1 in month 1, then months 4, 9, 14, 18, 21, 25 and 30); "
              "interest on the daily outstanding balance at SOFR + 3.25%; 30-month Construction Period. Accrual per month = "
              "outstanding balance \u00d7 all-in rate \u00f7 12 (a 30/360 convention; the Loan accrues on an actual/360 basis, "
              "which would increase every figure below by approximately 1.4%). The model reproduces Borrower's own total at a 3.50% SOFR "
              "($4,628,672 against $4,628,675), which validates the method.", size=9.5)
    rows = [
        ["3.50%", "6.75%", "4,628,672", "221,328", "Borrower's assumption; conclusion \u201cAPPEARS ADEQUATE\u201d"],
        ["4.00%", "7.25%", "4,971,536", "(121,536)", "Shortfall begins"],
        ["4.35%", "7.60%", "5,211,542", "(361,542)", "Credit Memorandum's market assumption; CM states $(565,000) using an average-balance method"],
        ["4.75%", "8.00%", "5,485,833", "(635,833)", "Borrower's sensitivity table shows $(640,165)"],
        ["5.25%", "8.50%", "5,828,698", "(978,698)", "Borrower's sensitivity table shows $(982,060)"],
        ["5.35%", "8.60%", "5,897,271", "(1,047,271)", "(+100 bps scenario in Credit Memorandum \u00a7 6.2)"],
        ["Breakeven", "7.07%", "4,850,000", "0", "Reserve is adequate only if SOFR averages 3.82% or less"],
    ]
    table(doc, ["SOFR", "All-in rate", "Projected interest", "Surplus / (shortfall)", "Comment"], rows,
          widths=[0.75, 0.8, 1.15, 1.2, 2.6], size=8.5, align_right_cols=(0,1,2,3))

    sub_h(doc, "V.4  Draw schedule \u2014 what the Term Sheet does versus what it says")
    rows = [
        ["1", "9,475,000", "9,475,000", "Soft costs 4,150,000 + interest reserve 4,850,000 + origination 475,000", "Consistent"],
        ["2\u20138 (gross hard cost)", "34,750,000", "34,750,000", "Equals 100% of the GMP", "No retainage withheld"],
        ["10% retainage", "0", "3,475,000", "Section 9.1 requires a 10% holdback", "Not implemented"],
        ["Draw 9 as labelled", "3,275,000", "3,475,000", "Labelled \u201cRetainage Release\u201d", "Understated by $200,000"],
        ["Draw 9 decomposed", "3,275,000", "1,440,000 + 1,835,000", "Contingency $1,440,000 + Loan-funded Developer Fee $1,835,000", "Mislabelled"],
        ["Borrower's component columns", "47,500,000 (stated)", "48,500,000 (recomputed)", "Includes the $1,000,000 of Developer Fee attributed to the mezzanine", "$1,000,000 imbalance"],
        ["Conformed schedule (draft Sch. 1)", "\u2014", "47,500,000", "Hard 31,275,000 net + 3,475,000 retainage + soft 4,150,000 + reserve 4,850,000 + fee 475,000 + contingency 1,440,000 + Developer Fee 1,835,000", "Foots exactly"],
    ]
    table(doc, ["Draw", "Term Sheet", "Recomputed", "Composition", "Finding"], rows,
          widths=[1.15, 0.85, 0.95, 2.35, 1.2], size=8, align_right_cols=(1,2))

    sub_h(doc, "V.5  Income, value and environmental sensitivities")
    rows = [
        ["Residential income at $2,245/month", "212 \u00d7 $2,245 \u00d7 12 = $5,711,280", "$5,712,000 stated", "$720 rounding difference; immaterial"],
        ["Gross potential income", "$5,711,280 + $552,000 + $198,000 = $6,461,280", "$6,462,000 stated", "Follows from the rounding above"],
        ["Vacancy and credit loss at 5.0%", "$6,462,000 \u00d7 5.0% = $323,100", "$323,100", "Ties; note submarket vacancy of 5.8% per Appraisal \u00a7 4"],
        ["Effective gross income", "$6,462,000 \u2212 $323,100 = $6,138,900", "$6,138,900", "Ties"],
        ["Operating expenses", "Line items sum to $1,262,100", "$1,262,100", "Ties; expense ratio 20.56%"],
        ["Net operating income", "$6,138,900 \u2212 $1,262,100 = $4,876,800", "$4,876,800", "Ties"],
        ["CC&R assessment omitted", "$0.12 \u00d7 287,500 sq. ft. = $34,500", "not in Appraisal \u00a7 7", "NOI \u2192 $4,842,300; DSCR \u2192 1.30x"],
        ["Loss of 14 units (Credit Memorandum)", "14 \u00d7 $2,245 \u00d7 12 = $377,160", "CM: $377,160", "NOI \u2192 $4,499,640; DSCR \u2192 1.21x"],
        ["Loss of 23 units (proportional overlay)", "23 \u00d7 $2,245 \u00d7 12 = $619,620", "not in Record", "NOI \u2192 $4,257,180; DSCR \u2192 1.14x"],
        ["Real estate taxes", "$49,065 \u00f7 $7,250,000 = 0.677% effective", "$412,000 budgeted", "Implies assessed value of ~$60.9M; confirm with Durham County"],
        ["Price per unit / per sq. ft.", "$72,800,000 \u00f7 212 = $343,396; \u00f7 287,500 = $253.22", "Appraisal: same", "Ties"],
        ["Unit and area cross-check", "180,650 res. sq. ft. + 18,400 retail = 199,050; GBA 287,500; residual 88,450 sq. ft. for 276 spaces (\u2248320 sq. ft./space)", "Appraisal \u00a7 3", "Consistent"],
    ]
    table(doc, ["Check", "Computation", "Record figure", "Finding"], rows,
          widths=[1.6, 2.1, 1.05, 1.75], size=8)

    sub_h(doc, "V.6  Acreage, frontage and date intervals")
    rows = [
        ["Parcel 1 (PIN 0821-04-72-3341)", "305.41 ft. \u00d7 298.62 ft. = 91,202 sq. ft.", "2.094 acres", "2.09 acres (Title)",
         "Phase I states 1.89 acres \u2014 does not tie"],
        ["Parcel 2 (PIN 0821-04-72-4102)", "297.63 ft. \u00d7 201.88 ft. = 60,086 sq. ft.", "1.379 acres", "1.38 acres (Title)",
         "Phase I states 1.58 acres \u2014 does not tie"],
        ["Combined site", "151,288 sq. ft.", "3.473 acres", "3.47 acres (all documents)", "Ties"],
        ["Foster Street frontage", "298.62 ft. + 201.88 ft. = 500.50 ft.", "\u2014", "420 ft. (Appraisal)", "Appraisal understated by ~80 ft."],
        ["Affected Area", "100 ft. \u00d7 165 ft. = 16,500 sq. ft. = 0.379 acres", "0.38 acres", "0.38 acres (NFA)", "Ties; = 10.9% of the site"],
        ["Construction Period", "February 28, 2025 + 30 months", "August 28, 2027", "August 28, 2027", "Ties"],
        ["Mini-Perm Period", "August 28, 2027 + 12 months", "August 28, 2028", "August 28, 2028", "Ties"],
        ["Extension", "August 28, 2028 + 6 months", "February 28, 2029", "February 28, 2029", "Ties"],
        ["Substantial completion vs. maturity", "August 31, 2027 against August 28, 2027", "3 days after", "Both stated", "Project completion post-dates the Construction Maturity Date"],
        ["Stabilization", "August 31, 2027 + 9 months", "May 2028", "May 2028", "Ties"],
        ["Exclusivity period", "January 10, 2025 + 60 days", "March 11, 2025", "March 11, 2025", "Ties"],
        ["NFA deed notice deadline", "September 30, 2024 + 60 days", "November 29, 2024", "November 29, 2024", "Ties"],
        ["Phase I AAI shelf life", "October 28, 2024 + 180 days", "April 26, 2025", "April 26, 2025", "Closes the window before a delayed closing"],
        ["Title Commitment expiration", "December 5, 2024 + 6 months", "June 5, 2025", "June 5, 2025", "Ties"],
        ["Land acquisition date", "\u2014", "\u2014", "Phase I: 2022; Title deed: June 12, 2023; Appraisal and Credit Memorandum: \u201cearly 2024\u201d",
         "Three different dates \u2014 see Issue 1"],
    ]
    table(doc, ["Item", "Computation", "Result", "Record figure", "Finding"], rows,
          widths=[1.35, 1.75, 0.95, 1.25, 1.2], size=8)

    # ---------------- SECTION VI ----------------
    art(doc, "VI.  SOURCE DOCUMENT INVENTORY AND SOURCE-TO-ISSUE LOG")
    para(doc, "The following table records each document in the Record, the propositions we relied on and where they appear, "
              "and the reliability assessment that supports its use.", size=10)
    rows = [
        ["Executed Term Sheet", "Jan. 10, 2025", "Lender / Borrower",
         "Loan amount, rate, fees, term and maturity dates, valuation ratios, budget, guaranties, collateral, draw mechanics, "
         "interest reserve, conditions precedent, covenants, permitted exceptions, insurance", "1\u20135, 12\u201320",
         "Binding only as to \u00a7\u00a7 22\u201323. Contains internal inconsistencies at \u00a7\u00a7 3.1/9.2, 15 and 18, and "
         "omits NFA conditions 2\u20134."],
        ["Credit Memorandum", "Jan. 22, 2025", "D. Forsythe / Senior Loan Committee",
         "LTC analysis and equity-escrow condition, mezzanine terms (including PIK), risk factors, extension conditions, "
         "environmental and title risk analysis, HVCRE", "1\u20135, 8, 11\u201318",
         "Approval document. Applies a 70% LTV policy maximum inconsistent with the Term Sheet; asserts 14 units above the "
         "Affected Area without support; states combined equity of $0 but also treats the land as contributed capital."],
        ["Appraisal executive summary", "Nov. 15, 2024", "Ridgeline Appraisal (L. Haverford, MAI)",
         "As-is $8,900,000; as-completed $72,800,000; as-stabilized $76,200,000; NOI $4,876,800; cap rate 6.40%; rent comparables; "
         "lease-up assumptions; CC&R and ARC statements; environmental assumptions", "3, 4, 6\u201311, 13",
         "FIRREA-compliant summary of a 187-page report we have not seen. Contains the 320 cubic yard and 1950s UST statements that "
         "conflict with the Phase I, a 420-foot frontage figure that conflicts with the survey, and an ARC approval statement the "
         "Title Officer contradicts."],
        ["Preliminary Title Commitment NC-2024-88712", "Eff. Dec. 5, 2024", "Aldersgate Title & Escrow (P. Langley)",
         "Vesting deed, legal descriptions and acreages, zoning, requirements (payoff, survey, taxes), all exceptions, "
         "CC&R terms and ARC requirements, mechanics' lien relation-back note, environmental exclusion", "2, 7\u201310, 17, 20, 21",
         "Primary source for title and for the legal descriptions. Environmental matters expressly excluded (Note 5), so it cannot "
         "confirm or deny recording of the NFA deed notice."],
        ["Phase I ESA (excerpted)", "Oct. 28, 2024", "Sentinel Environmental (J. Whitfield, P.E.)",
         "One REC; contamination concentrations against residential and non-residential standards; soil gas results; remediation "
         "scope and cost; the four NFA conditions and their deadlines; consultant's refusal to opine on the unit overlay; AAI shelf life",
         "6, 7, 8, 10, 11", "ASTM E1527-21 compliant as of its date. Parcel acreages and orientation conflict with the survey; "
         "the consulting contract caps liability at the $12,500 fee."],
        ["Borrower organizational materials and OA excerpts", "Jan. 2025", "Calloway & Strauss (J. Ngo)",
         "Ownership percentages, capital contributions, land contribution recital, 75% major-decision threshold, pledge consent "
         "requirement, absence of SPE provisions and independent manager, affiliate relationship, $14,200,000 net worth", "1, 14, 15, 17",
         "Certification is undated. Conflicts with the Credit Memorandum on member capital contributions and with the title record on "
         "how the land was acquired."],
        ["Construction budget and draw schedule", "Jan. 8, 2025", "Harborview Capital Partners (E. Vasquez-Torres)",
         "Line-item budget, funding sources by line, retainage calculation, draw timing, interest reserve model and sensitivity, "
         "land funded by mezzanine loan (line 1.01)", "1\u20136, 12",
         "Borrower-prepared and unaudited. Contains a $1,000,000 component imbalance and an interest reserve conclusion that its own "
         "sensitivity table contradicts."],
    ]
    table(doc, ["Document", "Date", "Author", "Propositions relied on", "Issues", "Reliability assessment"], rows,
          widths=[1.1, 0.7, 0.9, 1.9, 0.6, 1.3], size=7.5)

    # ---------------- SECTION VII ----------------
    art(doc, "VII.  EXTRACTED FACTS, ASSUMPTIONS, CHARACTERIZATIONS AND OPEN QUESTIONS")
    para(doc, "In accordance with our practice, the following are kept separate so that the Bank can see which statements rest on "
              "documentary evidence, which rest on an assumption, which are legal conclusions, and which remain open.", size=10)
    sub_h(doc, "A.  Facts established by the Record (documented)")
    for t in [
        "Borrower is a North Carolina limited liability company (NC SOS File No. 1923847) formed March 14, 2019, with its principal "
        "office at 400 West Main Street, Suite 310, Durham (Term Sheet \u00a7 1.2; Organizational Materials \u00a7 1.1).",
        "Membership interests are held 62% by Elena Vasquez-Torres (Managing Member), 28% by Brightleaf Investors Group LLC (NC SOS "
        "No. 2045612) and 10% by Reginald K. Osei (Term Sheet \u00a7 1.2; Organizational Materials \u00a7 1.2).",
        "Fee title to both parcels vested in Borrower by Special Warranty Deed recorded in Book 7598, Pages 443 and 445, dated June "
        "12, 2023, from Foster Street Properties LLC (Title Commitment, Schedule A \u00a7 5 and \u00a7 6).",
        "The combined site is approximately 3.47 acres (151,288 square feet per the metes and bounds), zoned MU-D (Title Commitment, "
        "Schedule A \u00a7\u00a7 6\u20137; Appraisal \u00a7 2).",
        "A deed of trust for the benefit of Triangle Commercial Bank dated September 14, 2018, recorded in Book 6215, Page 892, "
        "securing an original principal amount of $3,400,000, remains unreleased of record (Title Commitment, Schedule B\u2013II "
        "\u00b6 10).",
        "The Property is subject to a recorded Duke Energy easement (Book 4387, Page 621), a City of Durham stormwater easement (Book "
        "7421, Page 212) and the Brightleaf Historic District Association CC&Rs (Book 6984, Page 1155, as amended in Book 7102, Page "
        "388) (Title Commitment, Schedule B\u2013II \u00b6\u00b6 8\u201311).",
        "The Phase II investigation detected TPH-DRO at up to 847 mg/kg against a 100 mg/kg residential goal and benzene at 0.42 mg/kg "
        "against 0.065 mg/kg, with soil gas benzene at 185 \u00b5g/m\u00b3 against a 31 \u00b5g/m\u00b3 screening level (Phase I ESA "
        "\u00a7 5).",
        "NCDEQ issued a conditional No Further Action letter on September 30, 2024 imposing four conditions (Phase I ESA \u00a7 7).",
        "The 2024 ad valorem taxes were $29,847.12 on Parcel 0821-04-72-3341 and $19,218.44 on Parcel 0821-04-72-4102, both paid "
        "(Title Commitment, Schedule B\u2013II \u00b6 7).",
        "The general contractor's GMP is $34,750,000 and the Appraiser was furnished an executed copy of the contract (Appraisal "
        "\u00a7 3).",
    ]:
        bullet(doc, t, size=9.5)

    sub_h(doc, "B.  Assumptions made in this memorandum and in the draft (not established by the Record)")
    for t in [
        "That the title commitment's metes and bounds are accurate for the parcels as currently configured; we have not seen a survey.",
        "That the descriptions of work completed in August and September 2024 (demolition and remediation) were paid in full, and therefore "
        "that no mechanics' lien has attached; no invoices or waivers are in the Record.",
        "That the Phase I ESA has been supplemented by a Phase II report that we have not seen, and that the NFA Letter is in the form "
        "summarized in the Phase I ESA.",
        "That the mezzanine loan has not yet been funded in full, that its accrued PIK balance is as computed on simple interest at 12.50%, "
        "and that no mezzanine interest has been paid in cash.",
        "That the appraisal summary accurately reflects the 187-page report, including the lease-up and capitalization assumptions.",
        "That the Guarantors' liquid asset figures are as summarized in the Credit Memorandum from personal financial statements we have "
        "not seen.",
    ]:
        bullet(doc, t, size=9.5)

    sub_h(doc, "C.  Legal characterizations (conclusions of law, subject to confirmation)")
    for t in [
        "That a deed of trust in North Carolina is enforced by the trustee's power of sale in a special proceeding under Article 2A of "
        "Chapter 45, with deficiency determinations subject to N.C.G.S. \u00a7 45-21.36 (Issue 21).",
        "That a mechanics' lien claim relates back to the first furnishing of labor or materials under N.C.G.S. \u00a7 44A-10 and may "
        "therefore prime a later-recorded deed of trust (Issue 10).",
        "That the NFA non-residential use restriction, as written, reaches residential occupancy of space above the affected area until "
        "NCDEQ modifies the determination (Issue 11) \u2014 the conservative reading, and one we recommend resolving by written "
        "interpretation rather than by assumption.",
        "That a pledge of a membership interest requires the Managing Member's written consent under \u00a7 9.1 of the Operating "
        "Agreement, and that the borrowing requires 75% member approval under \u00a7 3.2 (Issue 15).",
        "That the requirement of an unlimited, surviving environmental indemnity is enforceable against the Guarantors in North Carolina "
        "and is not a penalty; a short opinion should confirm this before closing.",
    ]:
        bullet(doc, t, size=9.5)

    sub_h(doc, "D.  Open questions requiring a party's response")
    for t in [
        "What was the actual source of the $8,200,000 used to acquire the land in June 2023, and did any portion come from Brightleaf "
        "Mezzanine Capital LLC or Thomas R. Chen?",
        "What is the current outstanding balance of the Triangle Commercial Bank deed of trust, and is a payoff letter obtainable?",
        "Was the NFA deed notice recorded, and if so on what date and in what form? If not, has NCDEQ consented to late filing?",
        "Has NCDEQ been asked, in writing, whether residential occupancy above the affected area is permitted, and if so what was the "
        "response?",
        "How many units, and which unit types, sit above the 0.38-acre affected area?",
        "Has the Architectural Review Committee approved the final plans, or has the 60-day deemed approval period run?",
        "Has the soil management plan been submitted to and approved by NCDEQ?",
        "Does the GMP scope include the demolition and remediation already completed, and if so has a credit been given?",
        "Has any mezzanine interest been paid in cash, and what is the current accrued balance?",
        "What is Borrower's actual net worth on a GAAP basis as of the most recent month-end?",
    ]:
        numbered(doc, "\u2022", t, indent=0.35, hang=0.2, size=9.5)

    # ---------------- SECTION VIII ----------------
    art(doc, "VIII.  OUTSTANDING DILIGENCE \u2014 REQUEST LIST")
    para(doc, "The following items are required to close under Article III of the draft and are not in the Record. We recommend "
              "circulating this list immediately, with a return date of February 14, 2025 to permit review before a February 28, "
              "2025 closing; the items marked (*) are gating and, if not received, the closing should move rather than fund against "
              "an incomplete file.", size=9.5)
    rows = [
        ["*", "Recorded NFA deed notice, or NCDEQ consent to late recording plus confirmation that the NFA remains in effect", "8, 11",
         "Borrower / environmental counsel", "Feb. 7"],
        ["*", "Triangle Commercial Bank payoff letter (within 30 days) and recordable certificate of satisfaction", "2",
         "Borrower / Title Company", "Feb. 7"],
        ["*", "Certified sources and uses showing the source of the 2023 land purchase and of each member contribution", "1, 3",
         "Borrower", "Feb. 7"],
        ["*", "Architect's unit-by-unit overlay of the Affected Area on floors 1\u20136; NCDEQ written interpretation on residential "
              "occupancy above the area", "7, 11", "Borrower / Architect", "Feb. 14"],
        ["", "ALTA/NSPS survey with the Table A items in section 3.4, including the Affected Area by metes and bounds", "7",
         "Borrower", "Feb. 14"],
        ["", "Final unconditional lien waivers and paid invoices from the demolition, remediation, abatement and geotechnical "
              "consultants", "10", "Borrower", "Feb. 14"],
        ["", "Executed GMP contract with full exhibits, schedule of values and confirmation of scope exclusions; architect's agreement "
              "and consents to assignment", "5", "Borrower", "Feb. 14"],
        ["", "NCDEQ-approved soil management plan; vapor mitigation system design and engineer's certification", "11", "Borrower",
         "Feb. 14"],
        ["", "Architectural Review Committee approval or evidence of submission and lapse of the 60-day period; Association estoppel", "9",
         "Borrower", "Feb. 14"],
        ["", "Amended and restated Operating Agreement (SPE covenants and independent manager) with member consents at 75%; Managing "
              "Member consent to each pledge", "15", "Borrower", "Feb. 14"],
        ["", "Draft and executed intercreditor agreement; mezzanine loan documents and current PIK balance", "17",
         "Bank / Mezzanine Lender", "Feb. 14"],
        ["", "Borrower financial statements (audited or reviewed) and a GAAP net worth computation; Guarantor personal financial "
              "statements dated within 30 days and account verifications; two years of tax returns", "14", "Borrower / Guarantors",
         "Feb. 21"],
        ["", "Zoning compliance letter, building and grading permits, erosion control approval", "\u2014", "Borrower", "Feb. 21"],
        ["", "Insurance certificates and endorsements (construction and, for the mini-perm, property and rent loss); current flood "
              "determination", "18", "Borrower", "Feb. 21"],
        ["", "Non-consolidation opinion, enforceability and perfection opinions, title pro forma with endorsements", "\u2014",
         "Borrower's counsel / Title Company", "Feb. 21"],
        ["", "Contractor financial statements and bonding capacity evidence; Phase II report; full appraisal report", "22",
         "Borrower / Bank", "Feb. 21"],
    ]
    table(doc, ["*", "Diligence item", "Issue", "Responsible", "Return by"], rows,
          widths=[0.25, 3.35, 0.55, 1.55, 0.75], size=8.5)

    # ---------------- SECTION IX ----------------
    art(doc, "IX.  CONSOLIDATED CLOSING CONDITIONS CHECKLIST")
    para(doc, "The draft Loan Agreement organizes the conditions precedent in Article III. The table maps each condition to the "
              "issue it addresses and records the current status on the Record.", size=9.5)
    rows = [
        ["Loan Documents executed and delivered", "3.1", "\u2014", "Outstanding (draft circulated)"],
        ["Appraisal, Phase I, Phase II, geotechnical, updated Phase I if closing after 4/26/2025", "3.2", "6", "Partially satisfied; Phase II and full appraisal not in Record"],
        ["Title policy (pro forma, endorsements, no mechanics' or prior deed of trust exceptions)", "3.3", "2, 10, 20", "Outstanding"],
        ["ALTA survey with Table A items and Affected Area depiction", "3.4", "7", "Outstanding"],
        ["NFA conditions (deed notice, soil plan, vapor design, overlay plan, reliance letter, PLL if required)", "3.5", "6, 8, 11",
         "Outstanding \u2014 gating"],
        ["Historic district ARC approval or deemed approval; Association estoppel", "3.6", "9", "Unverified; Appraisal and Title conflict"],
        ["Equity contribution deposited and source verified; corrected sources and uses", "3.7", "1, 3", "Outstanding \u2014 amount to be conformed"],
        ["Intercreditor agreement executed", "3.8", "17", "Outstanding; not yet drafted on the Record"],
        ["SPE amendments, independent manager, member and Managing Member consents, non-consolidation opinion", "3.9", "15", "Outstanding"],
        ["Organizational documents, good standing, incumbency, identification", "3.10", "\u2014", "Partially in Record"],
        ["Construction contract, architect's agreement, plans, permits, schedule, bonding, scope exclusions", "3.11", "5", "Outstanding"],
        ["Permits, zoning compliance letter, erosion control, impact fee payments", "3.12", "\u2014", "Outstanding"],
        ["Construction and mini-perm insurance", "3.13", "18", "Outstanding"],
        ["Payoff and release of the Triangle Commercial Bank deed of trust", "3.14", "2", "Outstanding \u2014 gating"],
        ["Lien waivers and no-prior-work affidavits", "3.15", "10", "Outstanding"],
        ["Financial statements, guarantor verification, tax returns", "3.16", "14", "Outstanding"],
        ["Legal opinions (enforceability, perfection, non-consolidation)", "3.17", "\u2014", "Outstanding"],
        ["Fees, expenses, excise tax, title premiums", "3.18", "21", "To be quantified at closing"],
        ["No material adverse change; Committee re-approval of any change from the January 22 approval", "3.19", "\u2014",
         "Any change to the loan amount, equity or interest reserve requires re-approval"],
        ["Environmental consultant reliance letter and confirmations", "3.20", "6, 11", "Partially in Record (Phase I Appendix G)"],
    ]
    table(doc, ["Condition", "\u00a7", "Issue", "Status"], rows, widths=[3.05, 0.5, 0.65, 2.25], size=8.5)

    # ---------------- SECTION X ----------------
    art(doc, "X.  DRAFTING CONVENTIONS, RELIANCE AND QUALIFICATIONS")
    for t in [
        "The draft Loan Agreement is a first draft prepared by Bank counsel for discussion. It follows the Term Sheet and the Credit "
        "Memorandum, except where those documents conflict or are incomplete, in which case it adopts the position recommended in this "
        "memorandum. Every such departure is identified in a bracketed Drafting Note keyed to the issue numbers above.",
        "Bracketed items (for example \u201c$[4,080,000]\u201d and \u201c$[60,780,000]\u201d) are amounts we have computed but which "
        "cannot be fixed until the payoff and the land-funding questions are answered. They are not placeholders in the ordinary sense; "
        "they are the arithmetic consequence of the corrected budget and should be conformed, not deleted, at closing.",
        "Schedules 1 and 2 differ from the corresponding schedules in the Term Sheet and in Borrower's delivered schedule because those "
        "schedules do not foot. The differences are reconciled in Section V.4 and should be explained to Borrower when the draft is "
        "circulated.",
        "The draft assumes that the Bank will continue to treat the Mezzanine Loan as debt and not as equity, consistent with the Credit "
        "Memorandum. If the parties later restructure the mezzanine as preferred equity, the loan-to-cost, loan-to-value, HVCRE and "
        "single-purpose entity analyses all change and the draft must be revised.",
        "We have not reviewed the full appraisal report, the Phase II report, the NFA Letter, the survey, the GMP contract, the complete "
        "Operating Agreement, any financial statement, the mezzanine documents or a draft intercreditor agreement. Our conclusions on "
        "those documents are necessarily limited, and several are expressly conditional on seeing them (Issues 6, 7, 11, 14, 17 and 22).",
        "Nothing in this memorandum is a credit recommendation. The credit decision, the sizing of the equity contribution, and any "
        "waiver of the loan-to-cost or loan-to-value requirements are matters for the Senior Loan Committee, which should record its "
        "determination in writing given the discrepancies identified above.",
    ]:
        bullet(doc, t, size=9.5)
    rule(doc)
    para(doc, "Please contact either of us to discuss. We can turn the corrected sources and uses and the conformed draw schedule into "
              "a one-page reconciliation for Committee action, and we recommend a call with Borrower's counsel before the draft is "
              "circulated so that the three threshold questions (source of the land funds, the payoff amount, and NCDEQ's position on "
              "residential occupancy above the affected area) are answered in parallel rather than sequentially.", size=10,
         space_before=8)
    para(doc, "Ashford, Cromdale Consulting & Laine LLP", bold=True, size=10, space_before=12)
    para(doc, "Katharine Drummond, Partner  |  Marcus Webb, Associate", size=10)
    para(doc, "January 31, 2025", size=10)
