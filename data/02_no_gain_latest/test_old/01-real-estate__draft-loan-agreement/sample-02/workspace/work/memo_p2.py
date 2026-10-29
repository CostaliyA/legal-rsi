# -*- coding: utf-8 -*-
import sys; sys.path.insert(0,'/workspace/work')
from dh import *
from docx.enum.text import WD_ALIGN_PARAGRAPH as AL

def issue(doc, num, title, severity, record, analysis, consequence, recommendation, addressed):
    p = doc.add_paragraph(style='Heading 2')
    r = p.add_run("Issue %s \u2014 %s" % (num, title)); r.bold=True; r.font.size=Pt(11); r.font.name=FONT
    r2 = p.add_run("   [Severity: %s]" % severity); r2.bold=True; r2.italic=True; r2.font.size=Pt(9); r2.font.name=FONT
    r2.font.color.rgb = RGBColor(0x8B,0x1A,0x1A)
    for label, body in (("Record.", record), ("Analysis.", analysis), ("Consequence.", consequence),
                        ("Recommendation.", recommendation), ("Where addressed.", addressed)):
        p = doc.add_paragraph()
        p.paragraph_format.left_indent = Inches(0.18)
        p.paragraph_format.space_after = Pt(5)
        rr = p.add_run(label + " "); rr.bold = True; rr.italic = True; rr.font.size = Pt(10); rr.font.name = FONT
        add_runs(p, body, size=10)

def build_p2(doc):
    art(doc, "IV.  MATERIAL ISSUES AND INCONSISTENCIES")
    para(doc, "Each item below identifies the conflicting or incomplete record, our analysis (with independent computation "
              "where figures are involved), the consequence of leaving the point open, our recommendation, and where the "
              "draft Loan Agreement deals with it. Recommendations are cumulative; several issues must be resolved together "
              "(notably 1, 2 and 3).", size=10)

    sub_h(doc, "A.  Capital structure and funding")
    issue(doc, "1", "The land acquisition is described in three irreconcilable ways, and the capital structure contains no verified equity", "H",
      "Term Sheet \u00a7 5.1 (\u201cBorrower Equity (land previously acquired)\u201d shown at $0; \u201cTotal Sources "
      "$56,700,000\u201d) and \u00a7 5.2 (land \u201cacquired by the Borrower prior to the closing \u2026 funded from prior "
      "capital contributions by the Borrower's members\u201d). Credit Memorandum \u00a7 2.2 (land \u201cacquired by Ms. "
      "Vasquez-Torres on behalf of the Borrower through capital calls from all three members, including Brightleaf Investors "
      "Group LLC, at a total acquisition cost of $8,200,000\u201d) and \u00a7 5.1 (\u201cBorrower Cash Equity $0\u201d). "
      "Organizational Materials \u00a7 1.3 and Operating Agreement \u00a7 5.1(a) (land \u201cacquired by Ms. Vasquez-Torres "
      "\u2026 from her personal resources and subsequently contributed to the Borrower\u201d at an $8,200,000 cost basis for a "
      "62% interest; Brightleaf Investors Group LLC contribution \u201c$0 cash to date\u201d; Mr. Osei \u201c$0\u201d). "
      "Borrower Draw Schedule, Detailed Budget line 1.01 (land acquisition \u201cFunded by Mezzanine Loan $8,200,000\u201d; "
      "note: \u201cPreviously closed; funded by mezzanine loan proceeds and member capital calls\u201d). Appraisal \u00a7 3 "
      "(\u201cThe developer's equity contribution, inclusive of the value of the land, is projected to comprise the balance of "
      "the capital stack\u201d). Title Commitment, Schedule A \u00a7 5 (fee title vested in Borrower by Special Warranty Deed "
      "from Foster Street Properties LLC recorded in Book 7598, Page 443, dated June 12, 2023 \u2014 i.e., Borrower bought the "
      "land from a third party; there is no deed from Ms. Vasquez-Torres).",
      "The arithmetic identifies which version can be true. Uses total $56,700,000, including land acquisition of $8,200,000. "
      "Sources total $56,700,000, consisting of the Loan ($47,500,000) and the Mezzanine Loan ($9,200,000), with cash equity "
      "at $0. If the land were a genuine in-kind equity contribution, standard presentation would show it as an $8,200,000 "
      "source as well as an $8,200,000 use; the documents instead show a zero equity source, which means the $8,200,000 use "
      "must have been paid from one of the two debt sources. Only the Detailed Budget says so expressly: the mezzanine column "
      "totals $9,200,000, of which $8,200,000 is land and $1,000,000 is Developer Fee, and the senior column totals exactly "
      "$47,500,000. We tested the components: senior loan = hard costs $34,750,000 + soft costs $4,150,000 + interest reserve "
      "$4,850,000 + origination fee $475,000 + contingency $1,440,000 + senior-funded Developer Fee $1,835,000 = $47,500,000. "
      "That reconciles to the dollar and confirms that the mezzanine loan, not member capital, funded the land. Three further "
      "facts corroborate: (i) the land was conveyed to Borrower by a third-party seller in June 2023, not contributed by a "
      "member; (ii) the Operating Agreement recites that Brightleaf Investors Group LLC received its 28% interest for $0 in "
      "consideration of \u201cits commitment to arrange third-party mezzanine financing\u201d \u2014 an interest issued for "
      "financing services by an entity under the common control of the mezzanine lender's principal; and (iii) the Appraisal "
      "describes a \u201cbalance of the capital stack\u201d that does not exist because the sources and uses are equal.",
      "If the mezzanine loan funded the land, then (a) the Borrower contributed no capital of its own; (b) the Credit "
      "Memorandum's loan-to-cost and HVCRE analyses are built on a contributed-capital figure ($10,340,000 including $8,200,000 "
      "of land) that is not contributed capital at all \u2014 on this reading contributed capital is only the proposed $2,140,000 "
      "equity escrow, or 2.9% of the as-completed value, far below the 15% HVCRE threshold, so HVCRE classification is "
      "certain rather than marginal; (c) the \u201ccircular funding\u201d concern identified in Credit Memorandum \u00a7 5.1 is "
      "confirmed rather than hypothetical, because the same investor group supplied both the land financing and the equity "
      "member; and (d) any certificate that the land was funded by member equity (section 6.13 of the draft) would be false.",
      "Obtain the 2023 closing statement and bank records for the land purchase, and a schedule tracing each member capital "
      "account. Restate the sources and uses to show the land as a funded use with an identified source. If the mezzanine "
      "funded the land, treat the capital stack as 100% debt plus the new equity contribution, price and document the credit on "
      "that basis, and conform the Operating Agreement recital in \u00a7 5.1(a) (by amendment or by a corrective confirmation) "
      "before any opinion is given. Require the certifications in section 3.7 and section 6.13 of the draft to be given only "
      "after that verification.",
      "Sections 4.6(b) and 6.13 (no representation that the land is the Equity Contribution); section 3.7 (source verification); "
      "Schedule 2 Part B and the reconciliation note.")

    issue(doc, "2", "A $3,400,000 prior deed of trust must be released at closing, but the payoff is not a use of funds and no source is identified", "H",
      "Title Commitment, Schedule B\u2013Part II \u00b6 10 and Schedule B\u2013Part I \u00b6 4 (deed of trust from Foster Street "
      "Properties LLC to the Trustee for Triangle Commercial Bank dated September 14, 2018, recorded in Book 6215, Page 892, "
      "securing an original principal amount of $3,400,000; \u201cno cancellation, release, satisfaction, or subordination "
      "\u2026 has been recorded\u201d; Borrower's counsel advised by letter dated November 22, 2024 that the debt has been "
      "\u201cpartially repaid\u201d and the balance \u201cwill be satisfied in full at or prior to closing from the Borrower's own "
      "funds or from closing proceeds\u201d; the Title Company has not verified the balance and requires a payoff letter dated "
      "within 30 days of closing). Credit Memorandum \u00a7 9.7 (payoff \u201cfrom the proceeds of the senior construction loan or "
      "from borrower funds\u201d). Term Sheet \u00a7 5.2 and Borrower Draw Schedule, Uses of Funds (no payoff line). Appraisal "
      "extraordinary assumption 4 (assumes the deed of trust is satisfied at or concurrently with closing).",
      "The payoff is a cash use at closing of up to $3,400,000 (the actual balance is undisclosed). Total uses as budgeted are "
      "$56,700,000 against sources of $56,700,000; adding the payoff produces uses of up to $60,100,000 with no corresponding "
      "source, a shortfall of up to $3,400,000. The Credit Memorandum's suggestion that the payoff may come from \u201cthe "
      "proceeds of the senior construction loan\u201d cannot be right without reducing another use, because the entire $47,500,000 "
      "of senior proceeds is already allocated to hard costs, soft costs, the interest reserve, the origination fee, the "
      "contingency and part of the Developer Fee (see Issue 3). Note also the implication for Issue 1: if the $8,200,000 land "
      "price was partly financed by this $3,400,000 mortgage and the balance has since been paid down, the cash equity actually "
      "invested in the land is at most $4,800,000 and possibly less.",
      "Closing cannot deliver the first-priority lien the Term Sheet and the Title Commitment require, and the commitment "
      "condition in section 3.14 of the draft cannot be satisfied, unless the payoff is both quantified and funded. If it is "
      "funded from the senior loan, other costs are short by the same amount and the project is under-budget before the first "
      "draw.",
      "Obtain the payoff letter and per diem now, not at closing. Insert the payoff as a use in the corrected sources and uses "
      "and identify its source; on our computation the required equity rises accordingly (Issue 3). Require simultaneous "
      "recording of a certificate of satisfaction under N.C.G.S. \u00a7 45-37, no title exception for the prior deed of trust, "
      "and a settlement statement that shows the disbursement.",
      "Section 3.14 (payoff condition); section 9.1(c)(ii) (payoff included in Total Project Costs); Schedule 2, Part B.")

    issue(doc, "3", "Loan-to-cost exceeds the 80% maximum, and the required equity is computed against a budget that omits required uses", "H",
      "Term Sheet \u00a7 6.1 (maximum loan-to-cost 80%; \u201cTotal Project Costs are estimated at $56,700,000\u201d) and \u00a7 5.2 "
      "(uses of $56,700,000). Credit Memorandum \u00a7 5.3 and \u00a7 10.1(2) (loan-to-cost 83.77%; maximum loan at 80% = "
      "$45,360,000; shortfall $2,140,000; condition that Borrower deposit $2,140,000 in cash). Borrower Draw Schedule, Summary "
      "tab (same figures; note \u201cEXCEEDS 80% MAX PER TERM SHEET\u201d).",
      "The loan-to-cost arithmetic is correct on the budget as presented: $47,500,000 \u00f7 $56,700,000 = 83.77%, and 80% of "
      "$56,700,000 is $45,360,000, so the excess is $2,140,000. The difficulty is the denominator. The $56,700,000 budget excludes "
      "(i) the up to $3,400,000 payoff (Issue 2) and (ii) approximately $680,000 of demolition and remediation costs that, "
      "according to the Appraisal \u00a7 6.1, were incurred and paid before closing (\u201cThe demolition and remediation "
      "activities, which cost approximately $680,000\u201d; the Phase I ESA \u00a7 6.3 puts remediation alone at approximately "
      "$485,000). Adding the payoff only gives $60,100,000 and a loan-to-cost of 79.03%; adding both gives approximately "
      "$60,780,000 and a loan-to-cost of 78.15%, which complies with the 80% covenant without any reduction in the loan amount. "
      "But on that corrected budget the equity requirement is $60,780,000 \u2212 $47,500,000 \u2212 $9,200,000 = $4,080,000, "
      "not $2,140,000. In other words, the Committee's condition is $1,940,000 too low once the omitted uses are added, and if "
      "the omitted uses are not added then the payoff is unfunded. The two positions cannot both be right; something must be "
      "specified, and the arithmetic cannot be satisfied by a $2,140,000 escrow against a $56,700,000 budget that must fund a "
      "$3,400,000 payoff.",
      "As drafted, the loan-to-cost covenant would be breached at closing on the uncorrected budget, and the closing certificate "
      "would either be false or unattainable. If the parties instead rely on the corrected budget, the equity escrow is "
      "under-funded by approximately $1,940,000 and the payoff competes with construction costs for the same dollars.",
      "Rebuild the sources and uses from verified components and present it to the Committee for ratification: uses "
      "approximately $60,780,000; sources Loan $47,500,000 plus Mezzanine $9,200,000 plus verified equity of approximately "
      "$4,080,000. Alternatively reduce the loan to $45,360,000 (which resolves Issue 3 on the uncorrected budget but worsens "
      "the funding gap), or increase the mezzanine (which requires Committee, intercreditor and HVCRE reassessment). Confirm that "
      "the equity comes from Ms. Vasquez-Torres or another source unaffiliated with the mezzanine lender, and document the "
      "source.",
      "Section 9.1 (loan-to-cost, with Total Project Costs defined to include the payoff and pre-closing site costs); section "
      "3.7 (Equity Contribution of $[4,080,000]); Schedule 2, Parts A and B.")

    issue(doc, "4", "The as-completed loan-to-value ratio at closing is 65.25% against a 65% maximum stated in the Term Sheet", "M-H",
      "Term Sheet \u00a7 4 (\u201cLTV (As-Completed): $47,500,000 \u00f7 $72,800,000 = 65.25%\u201d and \u201cThe Lender's maximum "
      "loan-to-value ratio shall not exceed 65% on an as-completed basis\u201d) and \u00a7 6.2 (as-completed and as-stabilized "
      "maximums of 65%). Credit Memorandum \u00a7 6.1 (policy maximum stated as \u201cMax 70%\u201d; LTV of 65.25% reported as "
      "\u201cPass\u201d) and \u00a7 11(h) (70% LTV requirement for the extension).",
      "The Term Sheet cannot be satisfied as written: the loan is 65.25% of the as-completed value against a 65% cap. To comply, "
      "65% of $72,800,000 = $47,320,000, a reduction of $180,000; equivalently, the as-completed value would need to be "
      "$73,077,000 to support $47,500,000 at 65%. The Credit Memorandum avoids the problem by applying a 70% policy maximum that "
      "does not appear in the Term Sheet, so the credit file contains two different maximums for the same test. The "
      "as-stabilized ratio (62.34%) complies either way.",
      "A covenant that is breached on the day of closing is worse than no covenant: it converts every subsequent draw into a "
      "waiver request and gives Borrower an argument that the approved credit contemplated a 65.25% position. It also creates a "
      "discrepancy between the Term Sheet and the credit approval that a reviewer, auditor or purchaser of the loan will "
      "identify.",
      "Elect one of three cures and document it: (a) reduce the loan amount to $47,320,000; (b) obtain an updated appraisal "
      "supporting at least $73,077,000; or (c) record a specific Committee-approved exception to 65.25% and set the covenant "
      "accordingly. We recommend (c) with a compensating reduction of $180,000 at the first draw if the appraisal is not "
      "updated, because a $180,000 sizing change distorts the budget more than it improves the credit.",
      "Section 9.2(d) (states the 65.25% position, the $180,000 equivalent, and the permitted cures); Schedule 6, Part A.")

    issue(doc, "5", "The draw schedule does not withhold the retainage it promises, mislabels the final draw, and Borrower's schedule does not balance", "H",
      "Term Sheet \u00a7 9.1 (\u201ca 10% retainage holdback shall apply to all hard construction cost disbursements \u2026 released "
      "only upon satisfaction of the conditions \u2026 for Draw 9\u201d) and \u00a7 9.2 (Draws 2\u20138 of $5,212,500, $6,950,000, "
      "$6,950,000, $5,212,500, $3,475,000, $3,475,000 and $3,475,000; Draw 9 \u201cRetainage Release\u201d of $3,275,000). Credit "
      "Memorandum \u00a7 7.1 (same table; \u00a7 7.2 states that \u201cthe retainage amount of $3,275,000 represents approximately "
      "9.4% of the hard construction cost GMP\u201d). Borrower Draw Schedule, Detailed Budget lines 2.01\u20132.09 and Draw "
      "Schedule tab.",
      "Three separate defects. First, the Term Sheet's Draws 2 through 8 total $34,750,000, which is exactly 100% of the GMP, so "
      "no retainage is withheld during construction notwithstanding \u00a7 9.1; a final draw of 10% of the GMP would then "
      "over-disburse the hard cost line by $3,475,000. Second, 10% of $34,750,000 is $3,475,000, not $3,275,000, and $3,275,000 is "
      "precisely the sum of the Contingency ($1,440,000) and the Loan-funded Developer Fee ($1,835,000), which means the line "
      "labelled \u201cRetainage Release\u201d is in fact the contingency and developer fee and the retainage is never held at all. "
      "Third, Borrower's own schedule does not foot: its component columns total $9,475,000 (soft costs, interest reserve and "
      "origination fee) + $34,750,000 (net hard costs) + $1,440,000 (contingency) + $2,835,000 (the full Developer Fee) = "
      "$48,500,000, which is $1,000,000 more than the $47,500,000 stated total \u2014 the $1,000,000 of Developer Fee that the "
      "Detailed Budget attributes to the mezzanine loan \u2014 and its Draw 9 line shows components of $4,275,000 ($3,475,000 hard "
      "+ $200,000 Developer Fee + $600,000 contingency) against a \u201cTotal Draw Amount\u201d of $3,275,000. Its \u201cgross hard "
      "cost\u201d column also totals $38,225,000 against a $34,750,000 GMP because Draw 9 re-states the released retainage as "
      "gross cost. Related budget integrity points: (a) line item 2.01 describes $3,180,000 of site work as including "
      "\u201cDemolition, grading, utilities, paving\u201d although the warehouse demolition was completed in August 2024 and "
      "remediation in September 2024 (Phase I ESA \u00a7\u00a7 2.2, 6; Appraisal \u00a7 2), so completed work may be funded twice; "
      "(b) the Contingency is 100% loan-funded, so there is no borrower-funded contingency; and (c) Draw 1 funds $4,150,000 of "
      "soft costs including Lender's counsel ($310,000), the appraisal ($35,000), the Phase I ($12,500) and title premiums "
      "($245,000), several of which will already have been incurred and paid before closing, and the $75,000 expense deposit is "
      "not shown as a source at all.",
      "Without a functioning holdback the Bank has no completion leverage at the point of maximum risk, and the mislabeling means "
      "the Bank may believe it holds $3,475,000 of retainage when it holds nothing. The $1,000,000 imbalance in Borrower's model "
      "will be replicated in draw requests and will surface as an over-advance.",
      "Adopt Schedule 1 to the draft, which restores the 10% holdback ($3,475,000 released as Draw 9), separates the Contingency "
      "and Developer Fee into their own columns, and foots exactly to $47,500,000 across nine draws. Require Borrower to correct "
      "and re-certify its schedule before the first draw request. Require written confirmation that the GMP scope excludes the "
      "completed demolition and remediation (or that a credit has been given), line-item identification of the vapor mitigation "
      "system cost within the schedule of values, and paid invoices for pre-closing soft costs before those items are funded.",
      "Section 4.1 and Schedule 1 (conformed draw schedule); section 3.11(g) (GMP scope confirmation); section 4.5 (change orders "
      "and contingency sub-limits); section 4.2(h) and section 6.12 (budget certification).")

    sub_h(doc, "B.  Environmental and property description")
    issue(doc, "6", "Environmental facts conflict across the Record, and one remediation cost line is missing from the budget", "M",
      "Remediation volume: Phase I ESA \u00a7 6.1 (\u201capproximately 1,200 cubic yards of soil were excavated\u201d) against "
      "Appraisal \u00a7 8 (\u201capproximately 320 cubic yards\u201d) and Credit Memorandum \u00a7 8.2 (\u201capproximately 340 cubic "
      "yards\u201d). Underground storage tank: Phase I ESA \u00a7\u00a7 1, 2.2 and 3.3 (2,000-gallon diesel tank serving a backup "
      "generator, installed approximately 1972, removed approximately 1998, with \u201cno formal UST closure records\u201d \u2014 a "
      "data gap) against Appraisal \u00a7 8 (installed in the 1950s for heating oil, \u201cnot in active use since approximately "
      "1988\u201d). Cost: Phase I ESA \u00a7 6.3 (remediation cost approximately $485,000, funded by Borrower) against Borrower Draw "
      "Schedule line 3.05 (\u201cEnvironmental & Geotechnical \u2026 Phase I, Phase II, remediation monitoring, geotech\u201d "
      "$185,000). Insurance: Phase I ESA \u00a7 10, Recommendation 6 (pollution legal liability coverage) \u2014 no such coverage "
      "appears anywhere in the Record.",
      "The Phase I's 1,200 cubic yards is the version most consistent with the described excavation (roughly 100 feet by 165 feet "
      "to a depth of about 12 feet in the most impacted zone), and the Appraisal's 320 cubic yards and the Credit Memorandum's 340 "
      "cubic yards are inconsistent with each other as well as with the Phase I. The UST descriptions cannot both be accurate: a "
      "tank installed in 1972 and removed in 1998 is not a 1950s heating-oil tank taken out of service in 1988. Neither "
      "discrepancy changes the regulatory outcome, but both affect the reliability of the environmental conclusions in the "
      "Appraisal (which in turn supports the as-completed and as-stabilized values) and the accuracy of any certificate Borrower "
      "gives at closing. The $485,000 remediation cost is a pre-closing cost that is not in the budget at all (Issue 3), while the "
      "$185,000 budget line appears to double-count investigation and monitoring work that has already been performed.",
      "The Bank's credit file will contain inconsistent environmental facts that cannot be reconciled at closing, and the "
      "remediation cost gap is a direct contributor to the funding gap in Issue 3. Absent pollution legal liability coverage, the "
      "environmental indemnity is the Bank's only remedy for the residual condition, and the Guarantors' ability to fund a "
      "remediation claim is limited (see Issue 14).",
      "Ask Sentinel to reconcile the excavated volume and to document its UST records search (including the absence of closure "
      "records) so that the discrepancy is explained on the record. Correct the remediation volume in the Appraisal summary or note "
      "the correction. Move the remediation cost into the corrected budget (Issue 3) and re-scope line 3.05. Require a pollution "
      "legal liability policy as a condition of closing or, at a minimum, obtain a written cost estimate and a Committee decision "
      "to proceed without it.",
      "Section 3.5(g) and section 12.8 (environmental insurance); section 12.1 (acknowledgement of the specific contamination "
      "levels and the limits of the NFA Letter); Schedule 4.")

    issue(doc, "7", "Parcel acreages, orientation and frontage are described inconsistently across the Title Commitment, the Phase I ESA and the Appraisal", "M",
      "Phase I ESA \u00a7 1 and \u00a7 2.1 (Parcel 0821-04-72-3341 of \u201capproximately 1.89 acres\u201d, described as the "
      "\u201cwestern parcel\u201d, and Parcel 0821-04-72-4102 of \u201capproximately 1.58 acres\u201d, described as the "
      "\u201ceastern parcel\u201d; \u201cThe site fronts Foster Street to the north\u201d). Title Commitment, Schedule A \u00b6 6 "
      "(Parcel 1 / PIN 0821-04-72-3341 \u201ccontaining approximately 2.09 acres\u201d with a metes and bounds description; Parcel 2 "
      "/ PIN 0821-04-72-4102 \u201ccontaining approximately 1.38 acres\u201d, beginning at the \u201csouthwestern corner of Parcel "
      "1\u201d and running south, i.e., Parcel 2 lies south of Parcel 1; Foster Street is the \u201ceastern right-of-way "
      "margin\u201d of the western boundary). Appraisal \u00a7 2 (\u201capproximately 420 feet of frontage along Foster Street on the "
      "western boundary\u201d; \u201csecondary vehicular access \u2026 from a 20-foot public alley along the eastern boundary\u201d). "
      "Phase I ESA, Figure 3 description (Parcel 0821-04-72-3341 \u201cshown on the left (western) portion of the map\u201d; Foster "
      "Street \u201cdepicted along the northern boundary\u201d).",
      "We checked the metes and bounds against the stated acreages: Parcel 1 is 305.41 feet by 298.62 feet = 91,202 square feet = "
      "2.094 acres; Parcel 2 is 297.63 feet by 201.88 feet = 60,086 square feet = 1.379 acres; the combined area is 151,288 square "
      "feet = 3.473 acres, which matches the 3.47 acres stated in every document. The Title Commitment's acreages therefore tie to "
      "the legal descriptions, and the Phase I ESA's 1.89/1.58 split does not (although it sums to the same total). Frontage along "
      "Foster Street per the metes and bounds is 298.62 + 201.88 = 500.50 feet, not the 420 feet stated in the Appraisal. And the "
      "parcels are configured north and south, not west and east, with Foster Street along the western boundary rather than the "
      "northern boundary. No document in the Record describes a 20-foot public alley.",
      "The location of the 0.38-acre Affected Area turns on this geometry. The NFA Letter describes it as the northeast corner of "
      "Parcel 0821-04-72-4102; if that parcel is the southern parcel (as the metes and bounds indicate), its northeast corner is an "
      "interior point of the assembled site, not a corner abutting Foster Street \u2014 which is how the Phase I ESA's Figure 3 "
      "describes it. Until the affected area is fixed by survey, the Bank cannot test the Credit Memorandum's assertion that "
      "exactly 14 units sit above it (Issue 11), cannot confirm that the vapor mitigation system is being built in the right place, "
      "and cannot describe the restricted area accurately in a lease, a C/O application or a title exception.",
      "Require an ALTA/NSPS survey with the Table A items specified in section 3.4 of the draft, including a metes-and-bounds "
      "depiction of the Affected Area taken from the recorded deed notice, and an architect-certified overlay of the affected area "
      "on each floor plan. Correct the Phase I ESA's acreage and orientation description by errata so the environmental record and "
      "the title record agree. Confirm access (including the alleged alley) as an ALTA access endorsement item.",
      "Section 3.4 (survey scope); section 3.5(e) (overlay plan); Exhibit A (legal description and note); Schedule 3.")

    issue(doc, "8", "The NFA deed notice appears not to have been recorded, and the Title Commitment does not show it", "H",
      "NFA Letter condition 4, as summarized in Phase I ESA \u00a7 7 (\u201cThe property owner is required to record a notice in the "
      "Durham County Registry of Deeds \u2026 within 60 days of the date of the NFA Letter \u2014 that is, by November 29, "
      "2024\u201d) and Phase I ESA \u00a7\u00a7 8.1, 10 (Recommendation 3) (\u201cAs of the date of this Phase I ESA (October 28, "
      "2024), the consultant was not provided evidence that the required deed notice has been recorded\u201d). Title Commitment, "
      "Schedule B\u2013Part II (thirteen exceptions; none is a deed notice or declaration of land use restriction) and Note 5 "
      "(environmental matters expressly outside the scope of the commitment and any policy). Appraisal \u00a7 2 (\u201cThis land use "
      "restriction is memorialized in a Declaration of Land Use Restrictions recorded at the Durham County Register of "
      "Deeds\u201d) and \u00a7 8. Credit Memorandum \u00a7 9.5 (addresses only the use restriction, not the deed notice).",
      "The Record cannot be reconciled: either the notice was recorded (as the Appraisal states) or it was not (as the Phase I ESA "
      "states, and as the Title Commitment's silence suggests, since the commitment was effective December 5, 2024, six days after "
      "the deadline). If it was recorded, the Title Commitment should show it in Schedule B\u2013Part II and any policy will except "
      "to it \u2014 which Borrower and the Bank need to know before closing. If it was not recorded, Borrower is in breach of a "
      "condition of the NFA determination, which is itself a representation the Bank proposes to require (section 6.11 of the "
      "draft), and the NFA status \u2014 the linchpin of the environmental diligence \u2014 is at risk of being reopened.",
      "A closing certificate that the NFA conditions have been satisfied would either be false or unavailable, and the Bank could "
      "take title to a property subject to an unrecorded restriction it did not underwrite. Because the Title Commitment note "
      "excludes environmental matters entirely, the Bank cannot rely on the title policy for protection.",
      "Obtain a certified copy of the recorded notice or, if none exists, a written statement from Borrower and its environmental "
      "counsel together with (a) immediate recordation with NCDEQ's written consent to the late filing and (b) NCDEQ confirmation "
      "that the NFA determination remains in effect. Require a title date-down confirming the recording and confirm the form of "
      "exception with the Title Company. Do not close before this is resolved.",
      "Section 3.5(b) (recorded deed notice as a condition precedent); section 12.5; Schedule 3 \u00b6 7 (permitted exception "
      "form); section 6.11 (representation).")

    issue(doc, "9", "Historic district architectural approval is unverified, and the CC&R assessment is not in the operating budget", "M",
      "Appraisal \u00a7 2 (\u201cthe architectural design has been reviewed and approved by the Brightleaf Historic District "
      "Association in accordance with the CC&Rs\u201d). Title Commitment, Schedule B\u2013Part II \u00b6 11 and its Title Officer "
      "note (\u201cThe Company has not received evidence that the current project plans \u2026 have been submitted to or approved by "
      "the Brightleaf Historic District Association Architectural Review Committee\u201d; submissions due at least 90 days before "
      "construction commences; 60-day deemed approval; the Association may seek injunctive relief to halt unapproved "
      "construction). Credit Memorandum \u00a7 9.8 and \u00a7 10.1(14) (records approval as a condition of closing). Declaration of "
      "Covenants, Conditions and Restrictions, Book 6984, Page 1155, as amended by First Amendment recorded in Book 7102, Page 388 "
      "(assessment of $0.12 per square foot of gross building area per annum).",
      "Two documents directly contradict each other on approval, and the Title Officer's version is the more reliable because it "
      "speaks to the absence of evidence rather than to an assumption. The timing is also tight: with a closing targeted for "
      "February 28, 2025 and construction to start immediately thereafter, a 90-day submission requirement may not have been met, "
      "in which case the Borrower's remedy is a 60-day deemed approval \u2014 which postpones the draw schedule and therefore the "
      "interest reserve and the construction maturity date, because the Construction Period runs from closing, not from the "
      "permit. Separately, we tested the assessment: $0.12 \u00d7 287,500 square feet of gross building area = $34,500 per annum, "
      "which does not appear in the Appraisal's operating expense schedule (\u00a7 7: total operating expenses of $1,262,100, of "
      "which \u201cOther Operating Expenses\u201d are $30,038). Including it reduces stabilized NOI to $4,842,300 and the "
      "interest-only DSCR from 1.31x to 1.30x \u2014 small, but it is a real recurring charge and it compounds with the other "
      "adjustments in Issue 11.",
      "Construction could be enjoined mid-project by the Association, which would be a construction delay default under section "
      "13.6 and would strand sunk costs; and the NOI on which the loan was sized is overstated by a known, quantifiable amount.",
      "Obtain either the Architectural Review Committee's written approval or evidence that a complete submission was made at least "
      "90 days before the intended construction start and that the 60-day period has run; in either case, obtain an estoppel from "
      "the Association as to assessments and violations. Require the NOI used for covenant testing to include the assessment, and "
      "note the correction for the Appraisal and the credit file.",
      "Section 3.6 (approval or deemed approval, plus Association estoppel); section 7.7 (compliance with the Declaration); "
      "section 11.2 (assessment as a carrying cost under the Carry Guaranty); Schedule 5.")

    issue(doc, "10", "Site work performed in 2024 creates mechanics' lien relation-back exposure ahead of the Deed of Trust", "M",
      "Title Commitment, Note 4 (\u201cunder North Carolina law (N.C.G.S. \u00a7 44A-10), a claim of lien on real property \u2026 "
      "relates back to and is effective from the time of first furnishing of labor or materials\u201d; recommends owner and "
      "contractor affidavits that no labor or materials were furnished before recording, and lien waivers if work has "
      "commenced). Phase I ESA \u00a7\u00a7 2.2, 6 (demolition completed August 2024; remediation contractor excavated and disposed "
      "of soil in September 2024; total remediation cost approximately $485,000). Appraisal \u00a7 2 (demolition pursuant to City of "
      "Durham permits, August 2024). Borrower Draw Schedule line 3.05 (only $185,000 budgeted for environmental work).",
      "Substantial work was performed at the Property in 2024 by a demolition contractor, a remediation contractor, a "
      "pre-demolition hazardous-materials abatement consultant (Southern Environmental Services Inc., per Phase I ESA \u00a7 4) and "
      "a geotechnical consultant. If any of them is unpaid, or later asserts a claim, the lien relates back to first furnishing "
      "\u2014 that is, to a date before the Deed of Trust is recorded \u2014 and would prime the Bank. The remediation cost of "
      "approximately $485,000 is not in the budget, so the Bank has no direct evidence that it has been paid.",
      "The Bank could take a first-priority deed of trust that is in fact subordinate to a later-filed mechanics' lien, and the "
      "title policy would not necessarily protect it.",
      "Obtain final unconditional lien waivers and paid invoices from the demolition contractor, the remediation contractor, the "
      "abatement consultant and the geotechnical consultant before recording; obtain owner and general contractor affidavits as to "
      "the date of first furnishing; and require the Title Company to insure over mechanics' liens with the usual pending "
      "disbursement or no-prior-work endorsement. If any work under the GMP has begun before closing, restructure the closing to "
      "record first.",
      "Section 3.15 (lien waivers and no prior work); section 4.2(c) (partial waivers with each draw); section 4.4(d) "
      "(120-day period before retainage release); Schedule 3.")

    issue(doc, "11", "The NFA non-residential use restriction has not been reconciled to the residential program, and the \u201c14 units\u201d figure is unsupported", "H",
      "NFA Letter condition 2, quoted in Phase I ESA \u00a7 7 (\u201cthis No Further Action determination is contingent upon the "
      "restriction of future use of the affected area to non-residential (commercial or industrial) purposes \u2026 a modification "
      "to this NFA determination would need to be obtained from NCDEQ prior to such change in use\u201d) and condition 1 (vapor "
      "mitigation beneath \u201cany enclosed structure constructed over the affected area\u201d); condition 3 (NCDEQ-approved soil "
      "management plan before any subsurface disturbance). Phase I ESA \u00a7 8.5 (\u201cThe consultant did not independently verify "
      "whether any residential units would be positioned directly above the affected 0.38-acre area \u2026 this determination "
      "requires a detailed overlay\u201d). Credit Memorandum \u00a7 8.2 and \u00a7 9.5 (\u201cthe current project plans position 14 "
      "residential units in the building above this area\u201d; lost revenue of $377,160; recalculated DSCR of 1.21x). Appraisal "
      "\u00a7 8 (\u201cThe appraiser has not adjusted the valuation conclusions to account for any potential impact of the NFA use "
      "restriction\u201d). Term Sheet \u00a7 17 (describes only the vapor mitigation system and omits the use restriction, the soil "
      "management plan and the deed notice).",
      "The Credit Memorandum's 14-unit figure is not supported by any document in the Record, and the number 14 coincides with the "
      "number of three-bedroom units, which suggests the two may have been conflated. A 0.38-acre affected area is 10.9% of the "
      "3.47-acre site; a proportional overlay of 212 units implies roughly 23 units, and the actual exposure depends on the "
      "footprint (which the Phase I ESA says \u201cextends across substantial portions of both parcels\u201d). We ran the economics "
      "both ways: at 14 units, lost rent is 14 \u00d7 $2,245 \u00d7 12 = $377,160, NOI falls to $4,499,640 and DSCR to 1.21x; at 23 "
      "units, lost rent is $619,620, NOI falls to $4,257,180 and DSCR to 1.14x. Both are below the 1.25x covenant in section 9.3 of "
      "the draft, and at 23 units the loan would also fail a 65% as-stabilized LTV if value were reduced proportionally. Separately, "
      "the soil management plan must be approved by NCDEQ before any subsurface disturbance in the affected area \u2014 that is, "
      "before Draw 2 (foundation) if the foundation falls in or under the area \u2014 and no evidence of its submission appears in "
      "the Record. The vapor system must be designed by a North Carolina licensed professional engineer, and as-built drawings and a "
      "performance verification must go to NCDEQ within 90 days of foundation completion; the budget carries the system only as an "
      "unquantified note within the $3,590,000 parking line (line 2.08).",
      "If NCDEQ treats residential occupancy above the affected area as a change in land use requiring modification (the conservative "
      "reading, and the one the NFA Letter's text supports), Borrower will be unable to obtain certificates of occupancy for the "
      "affected units without a modification that the Phase I ESA says would \u201clikely require additional environmental "
      "investigation, risk assessment, and potentially additional remediation.\u201d That would reduce revenue, NOI and value "
      "simultaneously, and the appraised values would be overstated because the Appraisal expressly assumed compliance without "
      "adjustment. Conversely, if NCDEQ confirms in writing that residential use on upper floors above an engineered vapor system is "
      "permitted, the issue closes cheaply. The record does not allow the Bank to know which it is.",
      "Do three things before closing. (1) Obtain a written interpretation from NCDEQ, in response to a written request supported by "
      "the vapor system design and the architect's overlay, that residential occupancy on floors above the affected area either is or "
      "is not permitted under the existing NFA determination. (2) Have the architect certify, unit by unit, how many units and which "
      "unit types lie above the affected area, and replace the unsupported \u201c14 units\u201d figure with that certification. (3) If "
      "residential occupancy is not permitted, redesign (convert the affected stack to amenity, office or common area, or relocate "
      "units) and re-underwrite; if it is permitted, document the basis. In either case, make NCDEQ approval of the soil management "
      "plan a condition to each draw for work in the affected area, require a plan-and-specification line item for the vapor system, "
      "and conform section 17 of the Term Sheet so that all four NFA conditions are contractual.",
      "Sections 3.5(a)\u2013(f) (conditions precedent); sections 12.2\u201312.7 (use restriction, vapor system, soil management plan, "
      "deed notice, draw conditions); sections 8.12 and 11.4 (use restriction as a negative covenant and a recourse trigger); "
      "Schedule 4.")
