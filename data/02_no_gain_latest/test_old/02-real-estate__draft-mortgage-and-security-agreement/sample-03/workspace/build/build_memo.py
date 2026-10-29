# -*- coding: utf-8 -*-
"""Builds drafting-issues-memorandum.docx"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from docxstyle import *
from docx.shared import Pt, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH

doc = None

def h1(text):
    p = doc.add_paragraph(style="Heading 1")
    pf = p.paragraph_format
    pf.space_before = Pt(16); pf.space_after = Pt(6); pf.first_line_indent = Inches(0)
    pf.keep_with_next = True
    from docxstyle import _set_font
    _set_font(p.add_run(text), size=11.5, bold=True, color="000000")
    return p

def h2(text):
    p = doc.add_paragraph()
    pf = p.paragraph_format
    pf.space_before = Pt(10); pf.space_after = Pt(4); pf.first_line_indent = Inches(0)
    pf.keep_with_next = True
    from docxstyle import _set_font
    _set_font(p.add_run(text), size=10.5, bold=True)
    return p

def issue(num, title, severity, sources, finding, treatment, action):
    p = doc.add_paragraph()
    pf = p.paragraph_format
    pf.space_before = Pt(11); pf.space_after = Pt(3); pf.first_line_indent = Inches(0)
    pf.keep_with_next = True
    from docxstyle import _set_font
    _set_font(p.add_run(f"{num}.  {title}"), size=10.5, bold=True)
    rich(doc, [("Severity:  ", True, False), (severity, False, False),
               ("        Sources:  ", True, False), (sources, False, False)],
         size=9.5, left=0.3, first=-0.3, space_after=3, keep_next=True)
    rich(doc, [("Finding and effect.  ", True, False), (finding, False, False)],
         size=10, left=0.3, first=-0.3, space_after=3)
    if treatment:
        rich(doc, [("Treatment in the draft.  ", True, False), (treatment, False, False)],
             size=10, left=0.3, first=-0.3, space_after=3)
    if action:
        rich(doc, [("Recommended action / open item.  ", True, False), (action, False, False)],
             size=10, left=0.3, first=-0.3, space_after=3)

def front_matter(d):
    para(d, "FIELDING, ASHWORTH & COLE LLP", size=8, align="center", space_after=0)
    para(d, "Attorneys at Law  \u2022  Charleston, South Carolina  |  Savannah, Georgia", size=8.5, align="center", space_after=2)
    hr(d, space_before=2, space_after=10)
    para(d, "PRIVILEGED AND CONFIDENTIAL \u2014 ATTORNEY WORK PRODUCT \u2014 PREPARED AT THE DIRECTION OF COUNSEL",
         size=8.5, bold=True, align="center", space_after=14)
    para(d, "MEMORANDUM", size=15, bold=True, align="center", space_after=2)
    para(d, "Drafting Issues, Source Reconciliation and Open Items", size=11, italic=True, align="center", space_after=14)

    rows = [
        ["TO:", "Marcus Prideaux, Senior Vice President \u2014 Commercial Real Estate Lending, Calverley Heritage Bank"],
        ["FROM:", "Jordan Vickers, Associate; reviewed by Catherine \u201cKit\u201d Ashworth, Partner, Real Estate Practice Group"],
        ["DATE:", "April 2, 2025"],
        ["RE:", "Draft Mortgage and Security Agreement \u2014 CHB CRE Loan No. 2025-CHS-0047 \u2014 "
                "Palmetto Gateway Partners LLC \u2014 520\u2013534 King Street, Charleston, South Carolina 29403"],
        ["LOAN:", "$14,750,000.00, of which $12,500,000.00 Initial Advance and $2,250,000.00 Renovation Holdback"],
        ["ENCLOSURE:", "Mortgage and Security Agreement (with Absolute Assignment of Leases, Rents and Profits; Security "
                       "Agreement; and Fixture Filing), with Exhibits A\u2013F"],
    ]
    table(d, rows, widths=[1.05, 5.45], header=False, size=9.5, bold_first_col=True)
    hr(d, space_before=10, space_after=10)


def s1_purpose(d):
    h1("1.  Purpose, Deliverable and Summary of Conclusions")
    para(d, "This memorandum accompanies and supports the enclosed draft Mortgage and Security Agreement (the \u201cMortgage\u201d) "
            "for the above loan, and records (a) the pre-drafting issue review required before circulation, (b) the independent "
            "recomputation of every figure used in the draft, (c) the drafting treatments adopted and the reconciliations made "
            "between the executed Term Sheet dated April 1, 2025, the Title Commitment (No. PT-2025-04-1178), the appraisal, "
            "the Phase I Environmental Site Assessment, the rent roll and lease abstracts, the renovation budget and draw "
            "schedule, and the borrower\u2019s operating agreement, and (d) the matters on which we require the Bank\u2019s "
            "instruction before the draft can be finalized for closing.")
    para(d, "The Mortgage is substantially complete and internally consistent: it contains thirteen Articles and ninety-eight "
            "Sections, six Exhibits, an executed-form signature page with two subscribing witnesses and a South Carolina "
            "notarial acknowledgment, a guarantor joinder for limited purposes, and an express statement that South Carolina "
            "is a judicial foreclosure jurisdiction and that no power of sale is granted. Two structural points drive the "
            "document: first, the loan is non-recourse and therefore depends entirely on the single-purpose entity and "
            "bankruptcy-remoteness covenants in Articles 7 and 8; second, the Property carries a recorded SCDHEC land use "
            "restriction that cannot be removed, which required bespoke covenants and a dedicated Event of Default.")

    h2("1.1  The four conclusions that require action before closing")
    para(d, "Read with Section 3 below, the review produced four conclusions that go beyond ordinary drafting customisation:")
    items = [
        ("(a)", "The Loan, as priced and structured, cannot satisfy its own financial covenant. On the Bank\u2019s own rent "
                "roll projections, the best-case stabilised DSCR is 0.554x and the realistic DSCR at the first test date is "
                "0.280x, against a required 1.25x. This is a structural credit issue, not a documentation issue, and it will "
                "produce an Event of Default at the first or second test date (Issues 1 and 2)."),
        ("(b)", "The appraised values are not supported by the income approach stated in the appraisal. The NOI figures and "
                "capitalisation rates printed in the appraisal produce values of roughly $5.3 million to $10.1 million, not "
                "$18.2 million and $23.5 million. The as-is LTV of 81.04%, and therefore the Bank\u2019s principal collateral "
                "metric, rests on the sales-comparison approach alone (Issue 3)."),
        ("(c)", "Occupancy is 56.13%, not the 68% recited in the Term Sheet and the appraisal. The Term Sheet is internally "
                "contradictory on this point (it states 68% occupancy and, three lines later, 43.9% vacancy), and the "
                "appraisal\u2019s own figures cannot be reconciled to a 31,000 square foot building (Issue 4). The draft "
                "represents the correct figure."),
        ("(d)", "The borrower\u2019s operating agreement does not support a non-recourse loan. It contains no independent "
                "manager, no separateness covenants, no single-purpose restriction and no lender consent to dissolution or "
                "amendment, and the 75% approval threshold for Major Decisions means the 72% managing member cannot act "
                "alone. An executed amendment signed by all three members is a condition to closing (Issue 6)."),
    ]
    for lbl, txt in items:
        rich(d, [(lbl + "\u2003", False, False), (txt, False, False)], left=0.35, first=-0.35, space_after=5)
    para(d, "Thirty issues are logged at Section 4. The twenty-four most consequential are ranked in the register at Section 3. "
            "Three are rated critical: the DSCR covenant (Issue 1), the appraisal\u2019s income support (Issue 3) and the "
            "entity structure (Issue 6). Eleven are rated high: the absence of any DSCR cure mechanism (Issue 2), the Anson "
            "Lane quitclaim parcel (Issue 5), the SCDHEC land use restriction (Issue 7), the yield maintenance formula "
            "(Issue 8), the guaranty architecture and its fourteen-month window (Issue 9), the conflict between the transfer "
            "restrictions and the operating agreement (Issue 10), the sources-and-uses gap for closing costs (Issue 11), "
            "tenant estoppel and SNDA exposure on the Lowcountry Provisions lease (Issue 12), the allocation of the net worth "
            "and liquidity covenant (Issue 13) and the absence of any interest rate cap on a five-year floating-rate loan "
            "(Issue 14). The remaining issues are operational, mechanical or confirmatory, and several of them \u2014 the draw "
            "schedule reconciliation at Issue 15 and the statutory confirmations at Issue 30 \u2014 still need to be closed "
            "before execution.")


def s2_scope(d):
    h1("2.  Scope, Sources and Method")
    h2("2.1  Deliverable")
    para(d, "Lender\u2019s form Mortgage and Security Agreement, drafted to the executed Term Sheet, suitable for recording "
            "in the RCM Office for Charleston County, with the absolute assignment of leases and rents incorporated into the "
            "body of the Mortgage (rather than documented as a separate instrument) in accordance with the instruction at "
            "paragraph 1 and paragraph 3 of your markup notes of March 18, 2025.")
    h2("2.2  Sources examined in full")
    rows = [
        ["Document", "Date / Reference", "Originator", "Use in the draft"],
        ["Executed Term Sheet (binding commitment)", "April 1, 2025", "Bank / Borrower",
         "Controlling commercial terms; every Article traced at Section 8"],
        ["Commitment for Title Insurance PT-2025-04-1178", "Eff. February 28, 2025; expires August 28, 2025",
         "Prestige Title & Settlement Services LLC / Commonwealth National Title Underwriters Inc.",
         "Legal description (Exhibit A), Permitted Exceptions (Exhibit C), Schedule B-I requirements, instructions to closer"],
        ["Summary Appraisal Report PVS-2025-0214-CHS", "Effective February 14, 2025", "Pinnacle Valuation Services LLC",
         "Values, occupancy, lease analysis, environmental treatment"],
        ["Phase I ESA, Report CLR-2025-0119 (Executive Summary)", "January 28, 2025",
         "Clearfield Environmental Consulting LLC", "CREC, LUR obligations, vapor barrier protocol (Exhibit E)"],
        ["Rent roll and lease abstracts (three worksheets)", "As delivered", "Borrower",
         "Exhibit D, lease representations, occupancy reconciliation, DSCR projections"],
        ["Renovation budget and draw schedule (two worksheets)", "As delivered", "Borrower",
         "Exhibit B, disbursement conditions, retainage"],
        ["Redacted summary of Amended and Restated Operating Agreement", "Effective January 12, 2024; amended March 1, 2025",
         "Cartwright & Lyons LLP (borrower\u2019s counsel)", "Authority representations, SPE and transfer analysis"],
        ["Partner markup notes (internal)", "March 18, 2025", "C. Ashworth (this firm)", "Drafting instructions and flagged issues"],
    ]
    table(d, rows, widths=[1.85, 1.3, 1.55, 1.8], size=8)
    h2("2.3  Method and limitations")
    para(d, "Each source was read in full rather than in summary. Every amount, percentage, ratio, date interval and "
            "cross-reference in the Term Sheet and the ancillary materials was recomputed independently (Section 5); where a "
            "recomputation departs from a stated figure, the departure is recorded rather than silently corrected. Recitals "
            "of fact are separated from legal characterisations and from recommendations: Section 4 states findings, then the "
            "treatment adopted in the draft, then the action required. Where a source is silent, the gap is identified as such "
            "rather than filled by assumption.")
    para(d, "Three express limitations apply. First, the redacted operating agreement summary is not the operating agreement; "
            "the SPE amendment required by Issue 6 cannot be conformed until the full unredacted document, including all "
            "exhibits and the March 1, 2025 amendment, is produced. Second, the metes and bounds description for Exhibit A is "
            "not in the record \u2014 the record description and the survey reference are used, with the surveyor\u2019s "
            "description to be inserted at closing. Third, we have not reviewed the full Phase I ESA report or its appendices, "
            "the construction contract, the Leases themselves (only the borrower-prepared abstracts), or the survey; each is "
            "identified in Section 6 as an outstanding diligence item.")


def s3_register(d):
    h1("3.  Top-Risk Register")
    para(d, "Risks are ordered by consequence to the Bank, not by order of appearance in the documents. \u201cC\u201d denotes "
            "a risk that can prevent closing or defeat the intended structure; \u201cH\u201d a risk that can produce a "
            "material loss of protection or a foreseeable default.")
    rows = [
        ["ID", "Risk", "Sev.", "Primary source", "Consequence if unresolved", "Action"],
        ["1", "DSCR covenant unattainable: best-case 0.554x, realistic 0.280x, against 1.25x required", "C",
         "Term Sheet \u00a77.1; rent roll, Vacancy Schedule",
         "Automatic Event of Default at the first or second quarterly test; enforcement against a performing asset; guarantor exposure",
         "Reset covenant, extend interest-only, add DSCR cure deposit and cash management (Issue 1)"],
        ["2", "No mechanic to cure or waive a DSCR failure; \u201cwithout cure\u201d default", "H",
         "Term Sheet \u00a7\u00a711.1(i), 11.2", "First test failure is immediately actionable", "Draft cure and equity-cure election (Issue 2)"],
        ["3", "Appraisal income approach does not support the concluded values", "C",
         "Appraisal \u00a7\u00a76.2, 6.3, 7", "As-is LTV 81.04% (already above customary 75\u201380%) rests on sales comparison alone",
         "Obtain appraisal review and reconciliation from Pinnacle (Issue 3)"],
        ["4", "Occupancy misstated at 68%; actual 56.13%", "H", "Term Sheet \u00a72.3; appraisal \u00a7\u00a71, 3.1",
         "False representation in a recorded instrument; skewed leasing and NOI assumptions", "Draft represents 56.13% (Issue 4)"],
        ["5", "Anson Lane strip held by quitclaim only; insurer reserves on coverage", "H",
         "Title Commitment Sch. A \u00a7\u00a73\u20134 and notes to closer \u00b63", "Collateral gap and impairment of rear access, loading and parking relied on by the Leases",
         "Affirmative coverage, ALTA 34/19/17, title counsel sign-off (Issue 5)"],
        ["6", "Operating agreement non-compliant with SPE and bankruptcy remoteness", "C",
         "Operating agreement summary \u00a7\u00a71.4, 3.1, 3.2, 8.1, 9.1", "Non-recourse structure defeated; unconstrained voluntary bankruptcy",
         "Executed amendment by all three members as a condition to closing (Issue 6)"],
        ["7", "SCDHEC land use restriction (vapor barrier) treated as \u201cstandard\u201d environmental risk", "H",
         "Title Commitment Req. 6 and notes to closer \u00b61; Phase I \u00a7\u00a75.3, 6(d)", "Loss of NFA status; reopening of site file; lender liability",
         "Dedicated covenants, inspections and Event of Default (Issue 7)"],
        ["8", "Yield maintenance: undefined index; 1% floor omitted by the markup; lockout internally inconsistent", "H",
         "Term Sheet \u00a7\u00a74.1\u20134.3; markup notes \u00a75", "Premium unenforceable as a penalty or indefinite; yield loss",
         "Draft to Term Sheet with defined index; confirm commercial interpretation (Issue 8)"],
        ["9", "Interest shortfall guaranty expires at month 14, before the DSCR test at month 24", "H",
         "Term Sheet \u00a75.5(c) vs \u00a77.1", "Guarantor relief ends exactly where the credit risk peaks",
         "Extend coverage to the DSCR test date or add a DSCR guaranty (Issue 9)"],
        ["10", "Transfer restrictions conflict with the operating agreement; no indirect or upstream control test", "H",
         "Term Sheet \u00a710.3; operating agreement \u00a7\u00a74.1, 4.2(c), 4.5",
         "18% interest may transfer to a \u201csuccessor fund\u201d without consent; a sale of the managing member is unrestricted",
         "Draft overrides with change-of-control covenant; confirm borrower acceptance (Issue 10)"],
        ["11", "Sources and uses do not fund closing costs", "H", "Term Sheet \u00a7\u00a73.3, 3.4; Exhibit B",
         "Funding shortfall of roughly $200,000\u2013$400,000 plus reserves", "Obtain certified sources and uses; increase equity or reduce fees (Issue 11)"],
        ["12", "Lowcountry lease has no estoppel, SNDA or assignment clause, yet estoppels and SNDAs are conditions to closing and to policy issuance", "H",
         "Term Sheet \u00a712.1(j)\u2013(k); Title Commitment Req. 11 and Exception 6; lease abstracts", "Closing and policy issuance exposed to a tenant the borrower cannot compel",
         "Obtain estoppel early; do not waive without compensating conditions (Issue 12)"],
        ["13", "Net worth and liquidity covenant allocated to the Borrower, not the Guarantor", "H",
         "Term Sheet \u00a77.2 vs markup notes \u00b66", "Covenant meaningless or unenforceable as drafted; guarantor untested",
         "Confirm intended obligor with credit (Issue 13)"],
        ["14", "Floating-rate loan with no interest rate cap requirement", "H", "Term Sheet (silent)",
         "A 200 bps move adds roughly $295,000 of annual interest and further depresses DSCR",
         "Require a cap through the DSCR test date (Issue 14)"],
        ["15", "Financial reporting: audited statements required, operating agreement provides only reviewed", "M",
         "Term Sheet \u00a77.3(a); operating agreement \u00a76.2", "Immediate technical default on first delivery", "Conform or obtain member approval (Issue 15)"],
        ["16", "Renovation draw schedule does not reconcile to the budget and ignores retainage", "M",
         "Draw schedule; budget detail", "Overstated equity and holdback balances; disbursement disputes", "Correct schedule before closing instructions (Issue 16)"],
        ["17", "Hard-coded dates assume an April 15, 2025 closing", "M", "Term Sheet \u00a7\u00a73.8, 8.3, 14.5",
         "Maturity and completion deadlines inconsistent if closing occurs as late as May 15, 2025", "Conform definitions at closing (Issue 17)"],
        ["18", "DSCR first test date stated three different ways", "L", "Term Sheet \u00a77.1; markup notes \u00b66; rent roll",
         "One-quarter difference in the first default window", "Confirm; conform Section 7.8(a) (Issue 18)"],
        ["19", "Balcony encroachment without evidence of a current licence", "M",
         "Title Commitment Exception 5 and notes to closer \u00b62; appraisal \u00a72.1", "City-mandated removal is an uninsured, unbudgeted cost",
         "Obtain licence or ALTA 28.1 with affirmative coverage (Issue 19)"],
        ["20", "Survey dated January 15, 2025 reaches the 90-day limit on the assumed closing date", "L",
         "Title Commitment Req. 9", "Re-certification required if closing slips", "Order re-certification now (Issue 20)"],
        ["21", "SOFR mechanics: one-day rate with daily accrual, no compounding convention stated", "M",
         "Term Sheet \u00a73.6", "Interest and yield maintenance computed differently from market convention; confirmation risk",
         "Confirm index convention with loan operations (Issue 21)"],
        ["22", "No evidence of Guarantor\u2019s $28,000,000 net worth; no personal financial statement in the file", "M",
         "Term Sheet \u00a71.3", "Guaranty of uncertain value against a fragile DSCR", "Obtain PFS and liquidity evidence (Issue 22)"],
        ["23", "Harborline\u2019s members and managers undisclosed", "M", "Operating agreement summary \u00a72.1",
         "Beneficial ownership and sanctions screening incomplete", "Obtain ownership chart and certifications (Issue 23)"],
        ["24", "Capital replacement reserve of $645.83 monthly is not a credible funding source for HVAC and elevator replacement", "L",
         "Term Sheet \u00a76.2", "Deferred capital risk passed to the Bank", "Consider a larger reserve or a capital plan condition (Issue 24)"],
    ]
    table(d, rows, widths=[0.3, 1.75, 0.35, 1.35, 1.5, 1.25], size=7.5)
    para(d, "", space_after=2)
    para(d, "Severity key: C = critical (can prevent closing or defeat the intended structure); H = high; M = medium; "
            "L = low or confirmatory.", size=8, italic=True)

def s4_issues(d):
    h1("4.  Issue Log")
    para(d, "Each issue states the finding, the treatment adopted in the enclosed draft, and the action required. Issue numbers "
            "correspond to the register at Section 3. Article and Section references are to the enclosed Mortgage unless the "
            "context indicates otherwise; \u201cTerm Sheet\u201d references are to the executed Term Sheet dated April 1, 2025.")

    h2("4.1  Debt service coverage and credit structure")
    issue(1, "The DSCR covenant cannot be satisfied on the Bank\u2019s own projections", "CRITICAL",
          "Term Sheet \u00a77.1; rent roll, Vacancy Schedule (\u201cCONCLUSION\u201d row)",
          "The Term Sheet requires DSCR of not less than 1.25x, first tested in month 24. The rent roll\u2019s own "
          "stabilised best-case projection produces NOI of $622,772 against annual debt service of $1,124,239, a DSCR of "
          "0.554x. Even on an interest-only basis the DSCR is 0.722x. On the realistic scenario at the test date (Bay 1, "
          "Bay 3 renewed and Suite A only), NOI of $314,782 produces 0.280x. A DSCR of 1.25x would require NOI of "
          "$1,405,299 on amortising debt service \u2014 2.26 times the best-case projection. There is no lease-up assumption "
          "set in the record that closes this gap. The covenant is therefore not a performance test but a scheduled default.",
          "Section 7.8(a) tracks the Term Sheet (1.25x, quarterly, trailing twelve months, from month 24) and defines Net "
          "Operating Income and Annual Debt Service precisely, because the Term Sheet leaves those definitions to the Loan "
          "Documents. We have not diluted the covenant; the draft is faithful to the Term Sheet. Sections 6.2 to 6.5 "
          "establish the reserve structure that any cash-management or cure mechanism would attach to.",
          "Credit decision, not a drafting choice. Four options, in order of our preference: (i) extend the interest-only "
          "period to month 36 and re-set the first test date to coincide with the expiry of the Tidemark lease at "
          "March 31, 2029; (ii) reduce the covenant to a level the asset can support on conservative assumptions, with a "
          "cash-sweep trigger at 1.10x; (iii) retain 1.25x but add a DSCR cure right permitting an equity deposit into a "
          "cure reserve; (iv) add a debt-service reserve funded at closing. We recommend (i) and (iii) together. If none is "
          "adopted, the Bank should recognise that it is underwriting to an enforcement event and should size the guaranty "
          "and the rate cap accordingly (Issues 9 and 14).")

    issue(2, "The DSCR default is expressly without cure, and no cure mechanism exists anywhere in the documents", "HIGH",
          "Term Sheet \u00a7\u00a711.1(i), 11.2(b)",
          "Section 11.1(i) of the Term Sheet makes two consecutive sub-1.25x quarters an Event of Default \u201cwithout "
          "cure\u201d, but the Term Sheet provides no mechanism by which a cure could ever be effected \u2014 there is no cure "
          "deposit, no equity cure right and no cash management waterfall. The carve-out of \u201cinsurance defaults\u201d and "
          "SPE and transfer defaults from the 30-day cure period leaves the DSCR default in a category of its own with no "
          "remedial path.",
          "Section 10.1(j) reflects the Term Sheet. Section 10.2(b) states the general cure periods and expressly withholds "
          "the extension from transfer and organizational-document breaches, but does not purport to create a DSCR cure that "
          "the Term Sheet does not contain.",
          "If option (iii) at Issue 1 is adopted, we will add a cure provision to Section 7.8(a) and carve the cured quarter "
          "out of Section 10.1(j). Pending instruction we have not invented one, because a cure right is a material economic "
          "concession that should appear in the Term Sheet or a side letter from the Bank.")

    issue(3, "The appraisal\u2019s income approach does not support either concluded value", "CRITICAL",
          "Appraisal \u00a7\u00a76.2, 6.3, 7 and \u00a78.5; Term Sheet \u00a72.4",
          "The appraisal states as-is NOI of $332,000 to $345,000 and a 6.25% capitalisation rate, then concludes an as-is "
          "value of $18,200,000. Capitalised at the stated rate, that NOI produces $5,312,000 to $5,520,000 \u2014 the "
          "concluded value implies a 1.82% to 1.90% capitalisation rate. The stabilized figures are the same problem in "
          "larger form: NOI of $582,000 to $592,000 at 5.85% produces $9,948,718 to $10,119,658 against a concluded "
          "$23,500,000, an implied 2.48% to 2.52%. To support $23,500,000 at 5.85% the property would need NOI of "
          "$1,374,750, or 2.3 times the appraiser\u2019s own stabilised NOI. Separately, the as-stabilized price of $758 per "
          "square foot exceeds every comparable the appraiser cites ($550 to $620), while the as-is $587 per square foot "
          "sits comfortably within that range. The as-is value is therefore a sales-comparison conclusion; the income "
          "approach as printed cannot be reconciled to it. Because the as-is LTV of 81.04% already exceeds the customary "
          "75% to 80% range (a point your markup notes raise at the closing paragraph), the Bank should not accept an "
          "81% LTV on a value whose income support is off by a factor of three.",
          "The draft does not depend on the appraisal for any covenant; no LTV covenant was requested and none is drafted. "
          "Section 2.5 states the secured amount, and the Permitted Exceptions and coverage requirements are drawn from the "
          "title commitment rather than the appraisal.",
          "Obtain from Pinnacle a written reconciliation or corrected pages, and commission an appraisal review before "
          "closing (FIRREA and the interagency guidelines require an independent review for a transaction of this size in "
          "any event). Until reconciled, we recommend that the credit approval record not rely on the as-stabilized LTV of "
          "62.77%. If the income approach is corrected rather than the conclusions, the collateral position changes "
          "materially and the loan size should be revisited.")

    h2("4.2  Data accuracy in the sources")
    issue(4, "Occupancy is 56.13%, not 68%; the Term Sheet is internally contradictory and the appraisal\u2019s area figures are impossible", "HIGH",
          "Term Sheet \u00a72.3; Appraisal \u00a7\u00a71, 3.1; rent roll, Summary worksheet",
          "Occupied space is Bay 1 (3,800 SF) plus Bay 3 (3,800 SF) plus Suite A (9,800 SF) = 17,400 SF of 31,000 SF, or "
          "56.13%. Vacancy is 13,600 SF, or 43.87% \u2014 which the Term Sheet itself states (\u201capproximately 43.9% of "
          "total building area\u201d) three lines after reciting 68% occupancy. The two statements cannot both be true. The "
          "appraisal repeats the error and compounds it: it states occupied area of 21,400 SF and vacant area of 13,600 SF, "
          "which total 35,000 SF against a 31,000 SF building. Its weighted average rent of $19.40 per square foot is "
          "$415,100 divided by 21,400; the correct figure on 17,400 SF is $23.86. A 68% occupancy representation in a "
          "recorded mortgage would be a false representation on which the Bank would be relying \u2014 and one that any "
          "tenant estoppel or post-closing rent roll would immediately contradict.",
          "Section 3.5 represents 31,000 SF gross, 17,400 SF occupied, 13,600 SF vacant, 56.13% occupancy, itemising the two "
          "vacant spaces, and states in-place annual base rent of $415,100 before giving effect to the January 1, 2025 "
          "escalation. Exhibit D carries the same figures and states the occupancy rate on its face.",
          "Correct the Term Sheet and appraisal records in the credit file. Confirm with credit whether the 68% figure was "
          "used in any approval metric. No client instruction is required to draft the correct figure, but the Bank should "
          "know that the error is repeated in a third-party appraisal in its file.")

    issue(5, "The Anson Lane strip is held through a quitclaim deed and the insurer has reserved on coverage", "HIGH",
          "Title Commitment Sch. A \u00a7\u00a73\u20134 and vesting notes; notes to closer \u00b63; Phase I ESA \u00a72",
          "Parcel Two (the vacated Anson Lane strip) was conveyed to the seller by quitclaim deed (Deed Book 1128, Page 443) "
          "under Ordinance 2019-084. The title company will insure fee simple, but it expressly states that \u201cno "
          "warranties of title were provided\u201d, that its willingness to insure \u201cshould not be construed as a "
          "representation that the chain of title for this parcel is equivalent to that of Parcel One\u201d, and that it "
          "\u201creserves the right to require an additional premium for extended coverage on this parcel and/or may limit "
          "such coverage by endorsement\u201d. The strip is not a formality: the Phase I ESA records that it runs along the "
          "rear boundary of Lots 7, 8 and 9 and \u201ccurrently provides rear access and loading for the building\u201d, and "
          "all three Leases give the tenants shared use of the rear lot (six spaces). The sources also differ on its extent "
          "\u2014 the title commitment describes a strip \u201cadjacent to and contiguous with Lot 7\u201d, the ESA a strip "
          "running along the rear of all three lots \u2014 which matters because the insurer\u2019s coverage must attach to "
          "the whole of what the Leases rely on.",
          "Section 3.4 contains a specific representation that the Title Policy will insure fee simple in both parcels "
          "without any exception, endorsement limitation or qualification reducing Parcel Two below fee simple; a "
          "representation that the acquisition deed conveys both parcels with general warranty; a representation that no "
          "adverse claim or gap is known; and a covenant prohibiting any conveyance, vacation, abandonment or obstruction of "
          "the strip without the Bank\u2019s consent. Section 7.6 requires ALTA 34 (identified exception) or equivalent "
          "affirmative coverage for Parcel Two, plus contiguity (19), access (17) and future-advance (14) endorsements. "
          "Section 7.1 requires the strip to be maintained free of obstruction.",
          "Require Prestige Title to commit in writing, before closing, to (a) the premium and terms on which it will insure "
          "Parcel Two, and (b) that no Schedule B-II exception will carve out or qualify the strip. If the insurer will not "
          "give affirmative coverage at acceptable cost, the Bank should treat the strip as uninsured collateral and "
          "consider an access easement or a survey-based confirmation of a prescriptive right, and should reflect the "
          "result in the LTV. Per your instruction we will raise this with Prestige immediately and copy you.")

    issue(6, "The operating agreement cannot support a non-recourse loan", "CRITICAL",
          "Operating agreement summary \u00a7\u00a71.4, 2.2, 3.1, 3.2, 4.1, 4.2, 8.1, 9.1; Term Sheet \u00a710.1",
          "The redacted summary discloses, in its own words, that the agreement contains no independent director or manager "
          "whose consent is required before a voluntary bankruptcy filing; no separateness covenants; no single-purpose "
          "restriction (the purpose clause ends with a catch-all permitting \u201cany and all activities necessary, "
          "incidental, or related thereto\u201d); no lender consent requirement for dissolution under \u00a78.1 or for "
          "amendment under \u00a79.1; and no restriction on additional indebtedness up to $1,000,000, which \u00a73.2(ii) "
          "permits with member approval only. The managing member may make capital calls unilaterally. Because the loan is "
          "non-recourse, these provisions are not housekeeping: without them a 72% managing member controlled by a single "
          "individual can place the borrower into bankruptcy and defeat the structure on which the Bank\u2019s recourse "
          "limitation depends. There is also an arithmetic constraint: Major Decisions require 75%, and Graydon Development "
          "Group holds 72%, so no Major Decision \u2014 including the amendment itself \u2014 can be approved without at "
          "least one passive member, and amendments affecting economic rights require each affected member under \u00a79.1. "
          "The amendment must therefore be signed by all three members.",
          "Section 7.5 contains the full separateness and single-purpose package, including the independent manager "
          "requirement at 7.5(j) and the representation at 7.5(k) that the organizational documents have already been "
          "amended. Section 8.3 prohibits amendment of the organizational documents, dissolution, merger or bankruptcy "
          "without the Bank\u2019s consent and expressly recites that the pre-closing agreement does not contain these "
          "provisions. Sections 10.1(h) and 10.2 make an SPE breach an immediate Event of Default with no cure period, "
          "consistent with Term Sheet \u00a711.2(c).",
          "Three deliverables, all as conditions to closing: (a) the operating agreement amendment adding the single-purpose "
          "restriction, separateness covenants, independent manager and unanimous bankruptcy consent, executed by Graydon "
          "Development Group LLC, Tidewater Opportunity Fund II LP and Harborline Capital Advisors LLC; (b) a certificate "
          "from Tidewater GP Holdings LLC evidencing authority to bind the fund; and (c) the full unredacted operating "
          "agreement and the March 1, 2025 amendment, without which we cannot confirm that the amendment achieves what the "
          "Mortgage represents. Note also that the appointment of an independent manager must be documented \u2014 the "
          "summary records that no officers have been appointed, so the mechanism needs to be built from scratch.")

    h2("4.3  Environmental")
    issue(7, "The SCDHEC land use restriction requires bespoke covenants, not \u201cstandard\u201d environmental language", "HIGH",
          "Title Commitment Req. 6, Exception 4 and notes to closer \u00b61; Phase I ESA \u00a7\u00a75.3, 5.4, 6(d); markup notes \u00b66",
          "Your markup notes direct that the \u201cstandard template environmental compliance covenant\u201d should suffice "
          "because the Phase I came back clean apart from the CREC with a no-further-action letter. With respect, the "
          "sources require more. The restriction is recorded in Deed Book 1203 at Page 89 (SCDHEC Site ID "
          "SC-29403-0772), and the No Further Action determination dated August 12, 2021 is expressly conditional on "
          "continued compliance with it \u2014 so a failure of the institutional controls jeopardises the regulatory "
          "closure itself, not merely the Bank\u2019s covenants. The title commitment\u2019s Requirement 6 requires the "
          "Environmental Indemnity Agreement to "
          "address the obligation to maintain and periodically inspect the vapor barrier and compliance with the land use "
          "restriction, and its note to the closer states that the Mortgage \u201cshould contain an event of default "
          "triggered by any failure to comply with or any modification, termination, or violation of said land use "
          "restriction\u201d. The Phase I ESA goes further, recommending at 6(d) that the Bank require a specific covenant "
          "with provisions addressing the consequences of non-compliance and the Bank\u2019s remedies. A \u201cstandard\u201d "
          "covenant would leave a condition to policy issuance unsatisfied and would miss the two things that actually "
          "matter: the vapor barrier beneath Bay 1 is not visible, cannot be inspected without opening the slab, and Bay 1 "
          "sits squarely within the renovation scope.",
          "Section 7.3 contains the general environmental covenants. Section 7.4 is dedicated to the institutional controls "
          "and contains seven specific obligations: the prohibition on residential use of the Lot 7 ground floor; vapor "
          "barrier maintenance; annual inspection by a South Carolina licensed environmental professional with a report and "
          "compliance certificate delivered to the Bank; prior SCDHEC notification and approval plus pre- and post-work "
          "inspection before any work affecting the Bay 1 slab; contractor and subcontractor acknowledgments; recordkeeping "
          "and prompt notice of any SCDHEC contact; and an express prohibition on amending, modifying or terminating the "
          "LUR without the Bank\u2019s consent and SCDHEC approval. Section 10.1(k) makes breach an Event of Default and "
          "Section 10.2(c) gives it a 30-day cure period extended up to 180 days where cure requires SCDHEC action, but no "
          "cure period at all for conversion of Bay 1 to residential use. Exhibit E consolidates the restriction and the "
          "protocol. Section 9.3(j) makes SCDHEC clearance a condition to the relevant draw.",
          "Confirm that the Bank accepts a cure period for LUR breaches (we recommend it, because a strict no-cure default "
          "for a slow-moving regulatory matter invites a foreclosure defence). Also consider requiring, as a condition to "
          "closing, a pre-acquisition vapor barrier inspection as the Phase I recommends at 6(b) \u2014 it is inexpensive "
          "and it establishes a baseline before the HVAC and façade work begins. Note that the HVAC replacement is a rooftop "
          "scope and the TI allowance relates to Bay 2 (Lot 8), so on the current scope no work should penetrate the Bay 1 "
          "slab; the draft protects against that changing.")

    h2("4.4  Prepayment and the note")
    issue(8, "The yield maintenance formula is under-specified, and the markup\u2019s substitute formula departs from the Term Sheet", "HIGH",
          "Term Sheet \u00a7\u00a74.1\u20134.3; markup notes \u00a75",
          "Four defects. First, the Term Sheet uses \u201ctreasury rate\u201d without defining the tenor, the source, the "
          "interpolation method or the measurement date. Second, the Term Sheet requires the premium to be the greater of "
          "1% of the outstanding balance and the present-value differential \u2014 a hard 1% floor \u2014 whereas the formula "
          "in your notes (\u201cgreater of the yield maintenance amount or some fixed minimum percentage\u201d posed as an "
          "open question) omits the floor and computes the differential on total debt service rather than on interest only. "
          "Because the Term Sheet is the binding commitment and the Loan Documents may not be materially inconsistent with "
          "it (Term Sheet \u00a714.4), the floor must be preserved. Third, the Term Sheet is internally inconsistent about "
          "the lockout: \u00a74.1 says no voluntary prepayment is permitted during months 1 to 24 and then says that any "
          "prepayment \u201cmade in violation of this restriction shall be subject to a prepayment premium as described in "
          "Section 4.2\u201d \u2014 but Section 4.2\u2019s premium is the yield maintenance premium, which by definition "
          "applies only in months 25 to 48. There is therefore no stated premium for a months 1 to 24 prepayment. Fourth, the "
          "Term Sheet is silent on casualty and condemnation proceeds, on the discount rate, and on whether the 50 basis "
          "points is added to the loan rate or to the Treasury rate.",
          "Section 4.7 resolves each point in favour of the Term Sheet. Section 4.7(b) sets the premium at the greater of 1% "
          "of principal prepaid and the present-value differential computed on interest only, with interest at the Note Rate "
          "against a comparison rate of Treasury plus 50 basis points, discounted at the Treasury Rate. The Treasury Rate is "
          "defined by reference to Federal Reserve Statistical Release H.15, to the security maturing closest to but not "
          "exceeding the end of the yield maintenance period, measured on the second business day before prepayment, with "
          "linear interpolation between the two nearest maturities and a fallback for non-publication. Section 4.7(a) treats "
          "the lockout as an absolute prohibition and, if the Bank nevertheless accepts a prepayment in months 1 to 24, "
          "prices it as if made at the end of the yield maintenance period. Section 4.7(d) applies casualty and condemnation "
          "proceeds at par, without premium.",
          "Confirm with Marcus three commercial elections: (i) that the 1% floor is intended to survive (we have preserved "
          "it); (ii) whether the 50 basis points belongs in the comparison leg as we have drafted it, or in the loan leg as "
          "your notes propose \u2014 the answers produce different premiums and the Term Sheet\u2019s phrase \u201ctreasury "
          "rate plus fifty basis points spread\u201d supports either reading; and (iii) that casualty and condemnation "
          "proceeds are applied at par. On enforceability, we agree with your note that South Carolina courts will enforce a "
          "yield maintenance premium only if it is mathematically determinate; the definition in Section 4.7(b) is designed "
          "to be computable from published data without judgement. We will run a sample calculation once the elections are "
          "confirmed, and we recommend retaining the worksheet methodology.")

    issue(9, "The guaranty package is described three ways and its payment coverage ends four months before the first DSCR test", "HIGH",
          "Term Sheet \u00a7\u00a75.5, 12.1(a), 14.3(e)",
          "Section 5.5 is headed \u201cfull recourse personal guaranty\u201d but sub-paragraph (a) then describes a "
          "non-recourse carve-out guaranty. The three components \u2014 carve-out, completion and interest shortfall \u2014 "
          "are functionally different guarantees with different triggers, different amounts and different durations, yet "
          "Section 14.3(e) and Section 12.1(a) list a single \u201cGuaranty Agreement\u201d. Most importantly, the interest "
          "shortfall guaranty covers only the first fourteen months following closing (to about June 15, 2026). Substantial "
          "completion is due on June 15, 2026, Suite B cannot realistically begin rent until February 2027, and the DSCR test "
          "is in April 2027. The guaranty therefore expires at precisely the moment the lease-up risk it is meant to cover "
          "begins \u2014 which, given Issue 1, is the single largest exposure in the transaction.",
          "Section 1.1 defines \u201cGuaranty\u201d to include the carve-out, completion and interest shortfall components "
          "\u201cdescribed in the Term Sheet to the extent set forth therein\u201d, so the Mortgage does not purport to "
          "resolve a question the guaranty documents must answer. Section 12.3 sets out the five carve-out events in the "
          "Term Sheet\u2019s order and states expressly that it must be read together with the corresponding provisions of "
          "the Note and the Guaranty, which are to be identical in scope. Section 10.1(m) makes any default by the Guarantor, "
          "or any repudiation of the Guaranty or Environmental Indemnity, an Event of Default.",
          "Two instructions are needed. First, confirm whether the Bank intends one instrument or three; we recommend three "
          "separate documents (carve-out, completion, interest shortfall), because combining them obscures the triggers and "
          "complicates enforcement. Second, extend the interest shortfall guaranty at least to the first DSCR test date, and "
          "we would recommend to the earlier of stabilisation and the Tidemark lease expiry. A carve-out guaranty alone will "
          "not respond to a payment shortfall caused by slow leasing, because slow leasing is not a bad-boy act.")

    h2("4.5  Transfers, entity and funding")
    issue(10, "The transfer restrictions are narrower than the operating agreement permits and capture no upstream change of control", "HIGH",
          "Term Sheet \u00a710.3; operating agreement summary \u00a7\u00a74.1, 4.2(c), 4.5",
          "The Term Sheet prohibits direct transfers of borrower interests above 10% individually or 25% in the aggregate, "
          "except transfers among existing members. Three gaps follow. First, the operating agreement treats as a permitted "
          "transfer, requiring no consent, any transfer of Tidewater\u2019s 18% interest directed by its general partner to "
          "\u201cany successor fund managed by Tidewater GP Holdings LLC or any Affiliate thereof\u201d \u2014 an 18% transfer "
          "that exceeds the Term Sheet\u2019s 10% threshold but which the borrower\u2019s own documents authorise. Second, "
          "neither the Term Sheet nor the operating agreement restricts indirect or upstream change: the summary states in "
          "terms that Neil Ashford Graydon \u201ccould sell or transfer his membership interest in GDG, the 72% Managing "
          "Member, to a third party\u201d without triggering any transfer restriction, because the borrower\u2019s member of "
          "record would not change. That is the most consequential transfer in the structure and it is currently "
          "unrestricted. Third, \u00a74.2(d) already permits transfers among existing members, so the Term Sheet\u2019s "
          "exception adds nothing but does leave open whether the aggregate 25% cap applies to a series of member-to-member "
          "transfers.",
          "Section 8.2(a) covers the Property; 8.2(b) adopts the 10% and 25% thresholds and the member-to-member exception, "
          "with conditions (no change of managing member or control, notice, confirmatory documents); 8.2(c) adds an express "
          "change-of-control covenant capturing transfers of interests in Graydon Development Group LLC, any change in the "
          "managing member or in the person exercising control, and any transfer by Mr. Graydon of his interest in the "
          "managing member, and states on its face that these are prohibited although the operating agreement would not "
          "capture them; 8.2(d) disapplies \u00a74.2(c) so that a Tidewater successor-fund transfer requires consent; and "
          "8.2(e) makes a breach void, an immediate Event of Default, and a carve-out event.",
          "Sections 8.2(c) and 8.2(d) go beyond the literal text of Term Sheet \u00a710.3. We regard them as consistent with "
          "its purpose and therefore permitted by Term Sheet \u00a714.4 (additional provisions not materially inconsistent), "
          "but they are the kind of term a borrower resists, and the borrower will point out that 8.2(d) contradicts its own "
          "operating agreement. Two options: (i) negotiate them into the Mortgage, coupled with the operating agreement "
          "amendment at Issue 6, so the two documents agree; or (ii) obtain the Bank\u2019s acceptance of the operating "
          "agreement\u2019s permitted transfers. We recommend (i). Please also confirm the Bank\u2019s position on transfers "
          "to estate-planning trusts, which the operating agreement permits and which are ordinarily acceptable.")

    issue(11, "The sources and uses do not fund closing costs or the reserves required at closing", "HIGH",
          "Term Sheet \u00a7\u00a73.3, 3.4, 6.3, 12.1(m), 13.1; Exhibit B; renovation budget worksheet",
          "The $6,200,000 equity contribution equals exactly the unscaled gap: total project cost of $20,950,000 less the "
          "loan of $14,750,000. Of that equity, $900,000 is allocated in Exhibit B to the renovation, leaving $5,300,000. "
          "The purchase price of $17,800,000 less the $12,500,000 initial advance is also exactly $5,300,000. The equity is "
          "therefore fully consumed by purchase price and renovation, leaving nothing for closing costs. The known costs "
          "alone \u2014 a 1% origination fee of $147,500 and the South Carolina deed recording fee of $54,575 \u2014 total "
          "$202,075, before title premiums, lender\u2019s legal fees, the survey, the appraisal, the Phase I ESA, UCC and "
          "search fees and construction inspection fees, none of which is quantified in the record. The $150,000 tenant "
          "improvement and leasing commission reserve is also required \u201cat closing\u201d. The Term Sheet makes the gap "
          "worse by providing that the initial advance is applied toward \u201cthe purchase price, closing costs, and funded "
          "reserves\u201d (Term Sheet \u00a73.3(a)), which necessarily reduces the amount reaching the seller.",
          "Section 6.4 requires the $150,000 reserve at closing; Section 6.5 pledges it; Section 7.12 puts costs and "
          "expenses on the borrower; Section 9.2 and Section 9.6 make cost overruns and excess renovation costs the "
          "borrower\u2019s responsibility. Exhibit B and Exhibit F state the reserve and equity allocations, and the note to "
          "Exhibit B records the $600,000 gap between the construction contract and the holdback. The draft does not pretend "
          "to close the funding gap; that is a closing mechanics item.",
          "Obtain a certified sources and uses statement before closing and confirm whether the $6,200,000 equity is "
          "exclusive of closing costs (it appears not to be). If it is inclusive, the equity requirement must be increased by "
          "the shortfall or the loan amount, the renovation scope or the fee must be reduced. The Bank should also confirm "
          "whether the initial advance may be applied to the $150,000 reserve, which would widen the gap at the seller.")

    h2("4.6  Leases, tenant cooperation and closing conditions")
    issue(12, "The largest ground-floor tenant owes the borrower nothing on estoppel, SNDA or assignment consent, yet all three are closing conditions", "HIGH",
          "Term Sheet \u00a7\u00a712.1(j)\u2013(k); Title Commitment Req. 11 and Exception 6; rent roll, Lease Abstracts",
          "The Lowcountry Provisions lease (Bay 1, 3,800 SF, $28.50 per square foot, expiring December 31, 2027) is silent "
          "on assignment and subletting, contains no subordination or non-disturbance provision and \u201cdoes not contain a "
          "provision requiring tenant to deliver estoppel certificates\u201d. It is the tenant that occupies the Lot 7 ground "
          "floor affected by the land use restriction, and it is therefore the tenant whose estoppel matters most. The Term "
          "Sheet makes estoppels (dated within 30 days of closing) and SNDAs from all existing tenants conditions "
          "precedent, and the title commitment makes tenant estoppels a condition to policy issuance. So a closing "
          "condition and a title requirement depend entirely on the goodwill of a tenant under no obligation to provide "
          "either. There is a second, quieter problem: because the Lowcountry lease is unrecorded but the tenant is in "
          "possession, the Bank\u2019s priority position relative to that lease is not secured by the recording statute and "
          "rests on inquiry notice.",
          "Section 5.1 effects an absolute and present assignment of rents under the South Carolina Uniform Assignment of "
          "Rents Act, and Section 5.3 permits collection upon notice to tenants without a court order, which protects "
          "enforcement regardless of what the lease says. Section 5.7 contains a representation that the borrower has full "
          "authority to assign all rents including under the Lowcountry lease, requires the estoppel and SNDA as conditions "
          "to the initial advance, acknowledges that the tenant is not obliged to give them, and imposes a post-closing "
          "covenant to obtain an assignment-consent, subordination and estoppel amendment at the first renewal, extension or "
          "amendment. Section 5.8 requires SNDAs from all three tenants. Section 5.5 sets the consent thresholds for future "
          "leases over 5,000 square feet or five years, and requires every new lease to carry subordination, estoppel and "
          "hazardous-materials provisions. Section 5.6 covers the $69,183 of security deposits.",
          "The Bank should decide now what it will do if Lowcountry declines. Your instruction was that the estoppel "
          "\u201cshould not be waived\u201d, and we agree; but the practical consequence is that closing is at risk. We "
          "recommend requesting the estoppel and SNDA immediately (not as a closing-week item), and, if refused, converting "
          "the requirement into a condition satisfied by (i) a lender\u2019s rent letter acknowledged by the tenant, (ii) an "
          "increased TI/LC or interest reserve, and (iii) an express carve-out event if the tenant later disputes the "
          "assignment. Please also confirm whether the Bank requires the Bay 3 and Suite A estoppels in its own form or will "
          "accept the tenants\u2019 forms.")

    issue(13, "The net worth and liquidity covenant is on the wrong party, and the audit standard conflicts with the operating agreement", "HIGH",
          "Term Sheet \u00a7\u00a77.2, 7.3(a); markup notes \u00b66; operating agreement summary \u00a76.2",
          "The Term Sheet imposes the $1,000,000 net worth and $500,000 liquidity covenants on the Borrower (Term Sheet "
          "\u00a77.2: \u201cBorrower shall maintain at all times\u201d), while your markup notes record them as Guarantor "
          "covenants. The ambiguity is material in both directions: a $1,000,000 net worth covenant on a single-purpose "
          "borrower holding a $18.2 million property is close to meaningless, whereas on a guarantor with an asserted "
          "$28,000,000 net worth it is close to irrelevant \u2014 in either case it does little work. Separately, the Term "
          "Sheet requires annual audited financial statements of the borrower, while the operating agreement requires only "
          "reviewed statements within 90 days; the borrower would be in technical default the first time it delivered what "
          "its own agreement requires.",
          "Section 7.8(b) and (c) draft the covenant as the Term Sheet allocates it, on the Borrower, tested annually; "
          "Section 7.7(a) requires audited statements within 120 days and Section 7.7 expressly acknowledges the mismatch "
          "with the operating agreement and obliges the borrower to obtain member approval or amend. Section 7.7(b) requires "
          "the Guarantor\u2019s annual personal financial statement, which is the only Guarantor reporting the Term Sheet "
          "requires. Section 10.1(j) makes a DSCR breach an Event of Default; a net worth or liquidity breach falls under "
          "the general covenant default in Section 10.1(b) with the Section 10.2(b) cure period.",
          "Confirm the intended obligor. If the covenant is meant to test the Guarantor \u2014 which we suspect, given "
          "\u00a71.3 recites his $28,000,000 net worth \u2014 we recommend a meaningful Guarantor net worth test (for "
          "example $10,000,000 and $1,000,000 of liquidity) rather than a nominal one, tied to the guaranty exposure at "
          "Issue 9. On the audit point, decide whether the Bank will accept reviewed statements with a CPA certificate, which "
          "is what most borrowers of this size can actually produce within 120 days.")

    issue(14, "A five-year floating-rate loan with no interest rate cap requirement", "HIGH", "Term Sheet (silent); Term Sheet \u00a7\u00a73.6",
          "The Term Sheet requires Daily SOFR plus 285 basis points with a 3.00% floor, but contains no provision requiring "
          "the borrower to maintain an interest rate cap or other hedge at any point. Combined with Issue 1 this is a "
          "compounding risk: annual interest at the floor rate of 5.85% is $862,875; a 200 basis point increase adds "
          "approximately $295,000 a year and pushes the best-case stabilised DSCR from 0.554x to roughly 0.44x. A floating-rate "
          "loan on a value-add asset with a covenant it cannot meet and no rate protection is exposed to a rate move it "
          "cannot absorb.",
          "The draft is silent on hedging, because a cap requirement is an economic term that should not be introduced by "
          "the lender\u2019s mortgage without the borrower\u2019s agreement; Section 1.1\u2019s definition of Loan Documents "
          "contemplates a hedging agreement \u201c(if any)\u201d.",
          "Recommend to credit that a cap be required at closing, struck at a rate that preserves a workable DSCR, running "
          "at least to the first DSCR test date, with the Bank named as an additional insured and a covenant to maintain it. "
          "If adopted we will add the covenant to Section 7 and the failure to maintain to Section 10.1.")

    h2("4.7  Operational, mechanical and drafting points")
    issue(15, "Renovation draw schedule does not reconcile to the budget, and does not model retainage", "MEDIUM",
          "Renovation budget and draw schedule worksheets; Term Sheet \u00a7\u00a76.4, 8.4",
          "The monthly figures sum to $2,250,000 of holdback (correct) but $905,000 of borrower equity against a budgeted "
          "$900,000, and $3,155,000 combined against a $3,150,000 budget; the schedule\u2019s own final row shows remaining "
          "borrower equity of negative $5,000. Line items also disagree with the budget detail: HVAC draws $900,000 of "
          "holdback against an $850,000 allocation and $1,250,000 in total against a $1,200,000 budget; the elevator draws "
          "$325,000 against a $375,000 allocation and $425,000 in total against $475,000; tenant improvements draw $110,000 "
          "of equity against $100,000 and $560,000 in total against $550,000; soft costs draw $145,000 of equity against "
          "$150,000 and $295,000 in total against $300,000. The schedule also disburses 100% of the holdback by month 14 "
          "without modelling the 10% retainage that Section 8.4 of the Term Sheet requires, which means gross draws must be "
          "higher than the schedule shows to leave a retainage balance at substantial completion.",
          "Section 9.4 imposes 10% retainage with defined release conditions, and the note to Exhibit B states that the "
          "schedule is illustrative only, does not model retainage, and that the Exhibit B line items control where the two "
          "differ. Section 9.2 caps unilateral change orders at $50,000 in the aggregate. Section 9.3(h) requires a "
          "cost-to-complete analysis with each draw.",
          "Have the borrower\u2019s construction consultant correct the schedule before it is attached to the closing "
          "instructions or used for disbursement control. As drafted, following the schedule would overdraw equity by "
          "$5,000 and overstate the HVAC line by $50,000.")

    issue(16, "Maturity, interest-only and substantial-completion dates are hard-coded to an assumed closing date", "MEDIUM",
          "Term Sheet \u00a7\u00a73.8, 3.9, 8.3, 14.5",
          "The Term Sheet fixes maturity at April 15, 2030, the interest-only period to April 15, 2027 and substantial "
          "completion to June 15, 2026, all derived from an assumed closing on April 15, 2025 \u2014 but the same Term Sheet "
          "permits closing as late as May 15, 2025. If closing slips a month, the 5-year term, the 14-month completion window "
          "and the 24-month interest-only period all silently change, and the recitals become wrong on their face in a "
          "recorded instrument.",
          "Section 1.1 defines Closing Date (April 15, 2025, or such later date as the initial advance is made, not later "
          "than May 15, 2025 without the Bank\u2019s consent), Maturity Date, Substantial Completion Deadline and the "
          "Interest-Only Period endpoint each both by stated date and by reference to the Closing Date. Sections 4.3 and 9.5 "
          "then operate on the defined terms.",
          "Because the stated dates and the date arithmetic currently agree only on an April 15 closing, one of them must be "
          "conformed at closing. We recommend that the stated dates be updated by a short closing-date confirmation "
          "certificate rather than by re-executing the Mortgage, and that the disburse schedule and Exhibit B be conformed "
          "at the same time.")

    issue(17, "DSCR testing commencement is described three different ways across the record", "LOW",
          "Term Sheet \u00a77.1; markup notes \u00b66; rent roll, Summary worksheet",
          "The Term Sheet says testing begins 24 months after closing with the first test being \u201cthe first full calendar "
          "quarter ending after the twenty-fourth month\u201d, anticipated to be about July 15, 2027 for the quarter ending "
          "June 30, 2027. Your markup notes and the rent roll both say the first test date is April 15, 2027. The two are a "
          "quarter apart, which matters because the earliest possible default moves with it.",
          "Section 7.8(a) follows the Term Sheet (first full calendar quarter ending after month 24) and does not hard-code a "
          "date.",
          "Confirm which the Bank intends; the definition in Section 7.8(a) can be shortened to a fixed first test date in "
          "one line once instructed.")

    issue(18, "The balcony encroachment has no documented licence, and its removal would be an uninsured and unbudgeted cost", "MEDIUM",
          "Title Commitment Exception 5 and notes to closer \u00b62; Appraisal \u00a72.1; renovation budget item 3.0",
          "A decorative iron balcony projects about 2.5 feet over the King Street right-of-way. The title company takes "
          "exception for it, recommends an ALTA 28.1 endorsement \u201cif coverage over this matter is desired\u201d, and "
          "states that it makes no representation as to the existence, validity or status of any permit, licence or "
          "encroachment agreement. The appraisal treats the encroachment as immaterial but advises confirming a valid permit "
          "and assessing removal risk. Nothing in the record includes a permit or licence. The risk is not only title: the "
          "façade restoration line of $625,000 includes repair of the encroachment area, and if the City required removal the "
          "additional façade work would fall outside the renovation budget, for which the borrower \u2014 not the Bank \u2014 "
          "would be responsible under Section 9.6, but which would nonetheless impair the collateral.",
          "Section 3.8 discloses the encroachment and qualifies the representation to the extent no current licence is "
          "evidenced; Section 7.6 requires the borrower to use commercially reasonable efforts to obtain and maintain a "
          "licence, to notify the Bank of any municipal assertion, and not to remove or modify the balcony without consent; "
          "Section 7.6 also requires ALTA 28.1 or equivalent; Section 10.1(p) makes uninsured municipal removal an Event of "
          "Default (which the Bank may prefer to waive); Exhibit C lists the endorsement as required.",
          "Request the encroachment licence from the borrower and the City now. If none exists, obtain ALTA 28.1 with "
          "affirmative coverage and consider whether the Bank will accept the risk or require an additional reserve. Note "
          "that Section 10.1(p) as drafted is aggressive; confirm whether the Bank wants a default for a municipal action "
          "outside the borrower\u2019s control, and we will soften it to a covenant plus notice obligation if preferred.")

    issue(19, "The survey reaches the title company\u2019s 90-day limit on the assumed closing date", "LOW",
          "Title Commitment Req. 9 and notes to closer \u00b64",
          "The ALTA/NSPS survey is dated January 15, 2025 and recorded in Plat Book 64 at Page 91. Requirement 9 requires it "
          "to be dated or re-certified to a date not more than ninety days before closing. Ninety days from January 15, "
          "2025 is April 15, 2025 \u2014 the assumed closing date, with no margin. Any slip in closing requires "
          "re-certification, and the standard exceptions at (b), (c), (d) and (e) of Schedule B-II cannot be removed without "
          "it. The title company also requires Table A items 1, 2, 3, 4, 6(a), 6(b), 8, 9, 11, 13, 14, 16 and 19.",
          "Section 1.1 builds re-certification into the definition of ALTA Survey; Section 7.6 requires cooperation in "
          "obtaining endorsements; Exhibit C records which standard exceptions must be deleted.",
          "Order the re-certification now so that it is dated within the window whenever closing occurs, and confirm with "
          "Cartwright Land Surveying that the Table A items the title company has listed are all shown.")

    issue(20, "SOFR mechanics and benchmark transition need confirmation against the Bank\u2019s operations convention", "MEDIUM",
          "Term Sheet \u00a73.6",
          "The Term Sheet uses \u201cDaily SOFR\u201d \u2014 a one-day rate \u2014 published on the applicable business day, "
          "with a predecessor-day fallback and a reference to \u201ca successor administrator\u201d. It does not say whether "
          "interest accrues on a simple daily basis or on a compounded-in-arrears basis, which is the market convention for "
          "term loans; nor does it provide a replacement waterfall. Two conventions produce different interest amounts over "
          "a month and, more importantly, different inputs to the yield maintenance calculation.",
          "Section 4.2 fixes simple daily accrual on an actual/360 basis, states that the Bank\u2019s determination is "
          "conclusive absent manifest error, and adds a benchmark replacement provision at 4.2(c) covering permanent "
          "discontinuation, loss of representativeness, administrator insolvency and regulatory prohibition, with a spread "
          "adjustment, conforming changes and continuation of the 3.00% floor. Section 4.8 is a standard usury savings clause, "
          "which also protects the Default Rate and late charge.",
          "Confirm the Bank\u2019s convention with loan operations. If compounded in arrears is used, Section 4.2 needs a "
          "single sentence and Exhibit B and the yield maintenance worksheet should be re-run. We also recommend asking "
          "whether the Bank intends to add the standard Adjustable Interest Rate (LIBOR) Act fallback language, which "
          "Section 4.2(c) references but does not reproduce.")

    issue(21, "No evidence of the Guarantor\u2019s asserted net worth", "MEDIUM", "Term Sheet \u00a7\u00a71.3, 5.5, 7.3(b)",
          "The Term Sheet recites an approximate net worth for Mr. Graydon of $28,000,000 but no personal financial "
          "statement, liquidity evidence or ownership statement is in the diligence record. The Guarantor is the sole "
          "member and manager of the managing member, so the guaranty is the Bank\u2019s only credit support beyond a "
          "property whose DSCR is 0.554x (Issue 1). Its value cannot be assessed from the file.",
          "Section 7.7(b) requires the annual personal financial statement; Section 12.3 preserves full recourse against the "
          "Guarantor for the carve-outs; the Guarantor\u2019s Consent and Agreement requires him to give the notices under "
          "Sections 7.11(f) and (g) and to be bound by the jurisdiction and jury-waiver provisions.",
          "Obtain a current personal financial statement with a schedule of liquid assets and an ownership chart of his "
          "interests before closing, and pair it with the revised covenant recommended at Issue 13.")

    issue(22, "Harborline\u2019s ownership is undisclosed; beneficial ownership and sanctions screening is incomplete", "MEDIUM",
          "Operating agreement summary \u00a7\u00a72.1; Term Sheet \u00a71.4",
          "The operating agreement summary records that \u201c[m]embers and managers of Harborline have not been disclosed\u201d, "
          "and says nothing about the ultimate beneficial owners of Tidewater beyond its general partner. The Bank is a "
          "federally insured depository institution and must complete customer identification, beneficial ownership "
          "(the certification requirement for legal entity customers) and sanctions screening before closing. The Term Sheet "
          "is silent on all three, though the title commitment requires good standing evidence for the borrower.",
          "Section 3.12 contains OFAC, ERISA and foreign-person representations; Section 13.12 contains the USA PATRIOT Act "
          "notice and the Bank\u2019s right to obtain and verify identifying information; Section 7.11(e) requires notice of "
          "changes in members, managers or registered agent.",
          "Obtain a full ownership chart to natural persons for each member, the beneficial ownership certification, and "
          "good standing certificates for the borrower in South Carolina and in each jurisdiction where it is qualified.")

    issue(23, "Flood insurance of $5,000,000 is required on a Zone X property, and the sources disagree on the FEMA panel", "MEDIUM",
          "Term Sheet \u00a79.3; Appraisal \u00a72.1; Phase I ESA \u00a72",
          "The Term Sheet requires $5,000,000 of flood coverage while acknowledging that the Property is in Zone X and that "
          "federal regulation does not require flood insurance there. That is permissible as a contractual requirement, but "
          "the Bank should record that it is a lender-imposed condition rather than a regulatory one, and borrowers "
          "sometimes resist the premium. The two technical sources also disagree on the map: the appraisal cites FEMA "
          "Community Panel No. 45019C0418J effective November 4, 2014, and the Phase I ESA cites Panel No. 45019C0520J "
          "effective December 4, 2020. Both conclude Zone X, so the conclusion is unaffected, but the file should carry the "
          "current panel.",
          "Section 6.6(c) states the $5,000,000 requirement and records expressly that it is required notwithstanding the "
          "Zone X designation and the absence of a federal requirement; Section 3.6 contains the corresponding representation.",
          "Confirm the current panel with the surveyor or the insurer and correct the file. Also confirm that the Bank wants "
          "the $5,000,000 requirement maintained given the premium cost and the Zone X designation \u2014 this is a pricing "
          "point the borrower will raise.")

    issue(24, "The capital replacement reserve is not a credible source of funding for the building systems it is meant to replace", "LOW",
          "Term Sheet \u00a76.2",
          "The reserve is $0.25 per square foot per year, or $7,750 annually and $645.83 monthly, on a building whose HVAC "
          "replacement is budgeted at $1,200,000 and whose elevator modernisation is budgeted at $475,000. Over the "
          "five-year term the reserve accumulates $38,750. The arithmetic in the Term Sheet is correct; the adequacy is not.",
          "Section 6.3 sets the deposit at $645.83 monthly with disbursement upon approval of qualifying capital "
          "expenditures, as the Term Sheet provides.",
          "Consider either a larger reserve (the renovation replaces the HVAC and modernises the elevator, so the risk is "
          "deferred rather than absent) or a condition requiring a capital plan and a post-renovation systems warranty "
          "assignment, which the draft already captures through Section 2.3(d) and Section 2.5.")

    issue(25, "Tenant improvement and leasing commission funding needs to be reconciled across three places", "LOW",
          "Term Sheet \u00a7\u00a76.3, 8.2; rent roll, Vacancy Schedule; renovation budget item 4.0",
          "Three separate pools touch the same cost: the $550,000 tenant improvement allowance line in the renovation budget, "
          "the $150,000 tenant improvement and leasing commission reserve funded at closing, and the leasing commissions "
          "which appear only in the rent roll projections (approximately $89,750 worst case) and are not separately "
          "budgeted, though they may sit within the $200,000 of soft costs. Projected tenant improvement cost in the rent "
          "roll is $310,600 for Bay 2 and Suite B, rising to $386,600 if Bay 3 is re-let to a new tenant. The combined "
          "budget and reserve exceed the projected need, so this is a reconciliation point rather than a shortfall \u2014 but "
          "the closing instructions should show which pool funds which cost, to avoid a double draw.",
          "Section 6.4 states expressly that the reserve is separate from, and additional to, the tenant improvement "
          "allowance line of the renovation budget; Exhibit F repeats the point; Section 5.5 requires the Bank\u2019s consent "
          "to leases over 5,000 square feet, which captures Suite B.",
          "Ask the borrower to map each projected tenant improvement and commission cost to its funding source. No credit "
          "decision required.")

    issue(26, "The registered agent is named differently in two source documents", "LOW", "Term Sheet \u00a71.2; operating agreement summary \u00a71.3",
          "The Term Sheet names the registered agent as \u201cCapitol Registered Agents Inc.\u201d and the operating agreement "
          "summary names \u201cStatehouse Registered Agents, Inc.\u201d, both at 1201 Main Street, Suite 410, Columbia. The "
          "title commitment requires evidence that the borrower is in good standing with a registered agent for service. A "
          "mismatch on a recorded instrument and in the Bank\u2019s credit file is an avoidable defect, and service of "
          "process in a foreclosure depends on the correct agent.",
          "The Mortgage does not name the registered agent; Section 7.11(e) requires notice to the Bank of any change in "
          "registered agent, and Section 3.1 represents good standing.",
          "Confirm the current registered agent from the South Carolina Secretary of State\u2019s records and correct the "
          "credit file and the Term Sheet record.")

    issue(27, "The Bank\u2019s contact email domain does not match its name", "LOW", "Term Sheet \u00a71.1",
          "The Term Sheet gives the relationship contact as mprideaux@coastalheritagebank.com while the lender is Calverley "
          "Heritage Bank. Either the domain is a legacy name or the Term Sheet is wrong; in either case a notice sent to that "
          "address should not be the operative notice channel.",
          "Section 13.4 provides for notice to the Bank at 412 Whitaker Street with a copy to this firm, permits email only "
          "for routine communications, and requires default, acceleration and foreclosure notices to be delivered by hand, "
          "courier or mail. The email address is not relied on in the Mortgage.",
          "Confirm the correct domain for future correspondence.")

    issue(28, "The construction contract is assigned without the contractor\u2019s acknowledgement", "MEDIUM",
          "Term Sheet \u00a7\u00a75.1(g), 8.1; renovation budget",
          "Section 5.1(g) of the Term Sheet assigns the borrower\u2019s interest in the construction contract with Beaufort "
          "Builders Group LLC, and the draft does so. But nothing in the record shows that the contractor has consented to "
          "the collateral assignment or agreed to the Bank\u2019s step-in rights, and construction contracts commonly "
          "prohibit assignment without consent. Section 7.4(e) separately requires contractor and subcontractor "
          "acknowledgments of the vapor barrier restriction \u2014 a different acknowledgement for a different purpose, and "
          "both are needed.",
          "Section 2.3(d) assigns all contracts, warranties, guaranties and indemnities relating to the renovation, "
          "expressly including the renovation contract; Section 8.7 prohibits termination, assignment or material amendment "
          "without consent and requires delivery of all change orders; Section 9.3 requires contractor insurance and lien "
          "waivers.",
          "Obtain (a) the contractor\u2019s consent to the collateral assignment and a lender step-in agreement or "
          "acknowledgment, and (b) the vapor barrier acknowledgments under Section 7.4(e) before the first draw.")

    issue(29, "Provisions of the Term Sheet that are inapplicable or deliberately relocated", "LOW", "Term Sheet \u00a7\u00a75.2, 5.3, 14.3",
          "Three items should be recorded so that the closing checklist does not chase documents that will not exist. The "
          "assignment of leases and rents is incorporated into the Mortgage rather than executed separately (permitted by "
          "Term Sheet \u00a75.2 and by title commitment Requirement 5), so the separate instrument listed at Term Sheet "
          "\u00a714.3(c) should be struck from the closing checklist and the Mortgage title should say so. The reference to "
          "\u201cas-extracted collateral (if any)\u201d at Term Sheet \u00a75.3 has no application to an improved commercial "
          "building. And the absolute assignment is recorded by means of the Mortgage, which satisfies the recording "
          "requirement of the Assignment of Rents Act.",
          "Section 2.6 states that the as-extracted collateral provision is inapplicable and explains why; the cover page and "
          "Article 5 title the instrument as including the absolute assignment; Section 5.1 characterises it as an absolute "
          "assignment under the Act and records that it is perfected on recording.",
          "Strike the separate assignment of leases and rents from the closing checklist. Confirm that the Bank is content "
          "with the combined instrument (it reduces recording cost, which is also the reason for the recommendation in your "
          "markup notes).")

    issue(30, "Statutory citations and foreclosure formalities require local confirmation", "MEDIUM",
          "Term Sheet \u00a7\u00a714.1, 14.3; general",
          "The draft relies on several South Carolina propositions that should be confirmed against current law before "
          "execution rather than taken from secondary sources: (a) the codification and current text of the Uniform "
          "Assignment of Rents Act, which the markup notes cite as S.C. Code Ann. \u00a7 29-3-100 et seq. and which we have "
          "adopted as cited but which should be verified; (b) the proposition that an absolute assignment is perfected on "
          "recording and enforceable on default upon notice to the tenant; (c) the requirement of two subscribing witnesses "
          "and an acknowledgment for recording, which the signature page assumes; (d) the conduct of a judicial foreclosure "
          "and the applicable upset-bid or redemption period, which the draft refers to generically and does not waive; and "
          "(e) the enforceability of the late charge and the Default Rate against a Georgia-chartered bank lending in South "
          "Carolina.",
          "The draft states each proposition with appropriate qualification: Section 5.1 cites the Act as recorded; Section "
          "11.2 states that foreclosure is judicial only, grants no power of sale, and preserves non-waivable rights; Section "
          "12.3 and Section 13.10 preserve only what may lawfully be waived (\u201cto the maximum extent permitted by "
          "Applicable Law\u201d); Section 4.8 is a usury savings clause; Section 13.10 requires the witness and acknowledgment "
          "formalities and the signature page implements them.",
          "Ask local counsel in Charleston to confirm (a) through (e) in a short written note before execution. We would not "
          "record the Mortgage without that confirmation.")

def s5_recompute(d):
    h1("5.  Independent Recomputation Worksheet")
    para(d, "Every amount, ratio, date interval and total used in the Mortgage was recomputed from its components rather than "
            "carried forward from a summary. Where the recomputation agrees, the entry records why the figure is reliable; "
            "where it does not, the variance and its effect are stated. Variances are not silently absorbed into the draft.")
    rows = [
        ["Figure", "Source states", "Recomputed", "Variance", "Effect / note"],
        ["Total Project Cost", "$20,950,000", "$17,800,000 + $3,150,000 = $20,950,000", "nil", "Reconciles. Used at Recital C."],
        ["Borrower equity", "$6,200,000 (29.6%)", "$20,950,000 \u2212 $14,750,000 = $6,200,000; 29.59%", "nil", "Reconciles, but see the funding gap row below."],
        ["Renovation Holdback", "$2,250,000", "$14,750,000 \u2212 $12,500,000 = $2,250,000", "nil", "Reconciles. Article 9."],
        ["Construction contract vs holdback", "$2,850,000 vs $2,250,000",
         "Budget items 1.0\u20134.0 = $1,200,000 + $475,000 + $625,000 + $550,000 = $2,850,000; gap $600,000", "nil (disclosed)",
         "Correctly disclosed in Term Sheet \u00a73.4 and Exhibit B. Borrower funds $900,000."],
        ["LTV, as-is", "81.04%", "$14,750,000 \u00f7 $18,200,000 = 81.044%", "nil",
         "Arithmetic correct. Above customary 75\u201380%. Value itself is unsupported \u2014 see Issue 3."],
        ["LTV, as-stabilized", "62.77%", "$14,750,000 \u00f7 $23,500,000 = 62.766%", "nil", "Arithmetic correct; value unsupported (Issue 3)."],
        ["Loan-to-cost", "70.41%", "$14,750,000 \u00f7 $20,950,000 = 70.406%", "nil", "Reconciles."],
        ["Occupancy (by area)", "68%", "17,400 \u00f7 31,000 = 56.13%", "\u221211.87 points",
         "Material misstatement repeated in Term Sheet and appraisal (Issue 4)."],
        ["Vacancy (by area)", "43.9%", "13,600 \u00f7 31,000 = 43.87%", "nil",
         "Correct \u2014 and irreconcilable with the 68% occupancy stated three lines earlier."],
        ["Occupied area (appraisal)", "21,400 SF", "3,800 + 3,800 + 9,800 = 17,400 SF", "\u22124,000 SF",
         "Appraisal states 21,400 occupied + 13,600 vacant = 35,000 SF in a 31,000 SF building (Issue 4)."],
        ["Weighted average rent (appraisal)", "$19.40/RSF", "$415,100 \u00f7 17,400 = $23.86/RSF", "+$4.46/RSF",
         "$19.40 is $415,100 \u00f7 21,400 \u2014 it inherits the area error."],
        ["In-place annual base rent", "$415,100", "3,800\u00d7$28.50 + 3,800\u00d7$24.00 + 9,800\u00d7$22.00 = $415,100", "nil",
         "Reconciles at pre-escalation rents. At closing, with the January 1, 2025 escalation, Bay 1 is $111,549 and the "
         "total is about $418,349 (Issue 4)."],
        ["Security deposits", "$69,183 (not stated in Term Sheet)", "$18,050 + $15,200 + $35,933 = $69,183", "nil",
         "Used at Sections 3.5 and 5.6 and Exhibit D."],
        ["As-is value support", "$18,200,000", "NOI $332,000\u2013$345,000 \u00f7 6.25% = $5,312,000\u2013$5,520,000", "\u2212$12.7M to \u2212$12.9M",
         "Income approach cannot produce the concluded value; implied cap on the conclusion is 1.82%\u20131.90% (Issue 3)."],
        ["Stabilized value support", "$23,500,000", "NOI $582,000\u2013$592,000 \u00f7 5.85% = $9,948,718\u2013$10,119,658", "\u2212$13.4M to \u2212$13.6M",
         "Implied cap on the conclusion is 2.48%\u20132.52% (Issue 3)."],
        ["NOI needed to support stabilized value", "\u2014", "$23,500,000 \u00d7 5.85% = $1,374,750", "\u2014",
         "2.3\u00d7 the appraiser\u2019s own stabilized NOI of $582,000\u2013$592,000."],
        ["Value per square foot", "$587 as-is / $758 stabilized", "$18,200,000 \u00f7 31,000 = $587; $23,500,000 \u00f7 31,000 = $758", "nil",
         "As-is is within the cited comparables ($550\u2013$620); stabilized exceeds all of them (Issue 3)."],
        ["Monthly P&I, 25-year amortization at 5.85%", "$93,500 (rent roll)", "$93,686.61", "+$187/month",
         "Annual debt service recomputes to $1,124,239, not $1,122,000 (rent roll rounds)."],
        ["DSCR \u2014 stabilized best case", "0.555x (rent roll)", "$622,772 \u00f7 $1,124,239 = 0.554x", "nil",
         "Confirms the rent roll\u2019s own conclusion. Against 1.25x (Issue 1)."],
        ["DSCR \u2014 interest-only basis", "0.72x (rent roll)", "$622,772 \u00f7 $862,875 = 0.722x", "nil", "Still far below covenant."],
        ["DSCR \u2014 realistic at first test date", "0.281x (rent roll)", "$314,782 \u00f7 $1,124,239 = 0.280x", "nil", "Issue 1."],
        ["NOI required for 1.25x", "\u2014", "$1,124,239 \u00d7 1.25 = $1,405,299 (amortizing); $862,875 \u00d7 1.25 = $1,078,594 (interest-only)",
         "\u2014", "Gap to best-case NOI is $782,527 (Issue 1)."],
        ["Capital replacement reserve", "$645.83/month", "$0.25 \u00d7 31,000 \u00f7 12 = $645.83", "nil",
         "Arithmetic correct; accumulates $38,750 over the term against $1,675,000 of budgeted system replacement (Issue 24)."],
        ["Origination fee", "$147,500", "1.00% \u00d7 $14,750,000 = $147,500", "nil", "Reconciles."],
        ["South Carolina recording fee", "$54,575", "$1.85 per $500 \u00d7 29,500 units = $54,575", "nil", "Reconciles (Issue 11)."],
        ["Draw schedule \u2014 borrower equity", "$900,000 (budget)", "Sum of 14 monthly borrower draws = $905,000", "+$5,000",
         "Schedule\u2019s own final row shows remaining equity of \u2212$5,000 (Issue 15)."],
        ["Draw schedule \u2014 combined draws", "$3,150,000 (budget)", "$2,250,000 + $905,000 = $3,155,000", "+$5,000", "Issue 15."],
        ["Draw schedule \u2014 HVAC line", "$1,200,000 / $850,000 holdback", "$1,250,000 total / $900,000 holdback", "+$50,000 each",
         "Line-item overdraw against budget detail (Issue 15)."],
        ["Draw schedule \u2014 elevator line", "$475,000 / $375,000 holdback", "$425,000 total / $325,000 holdback", "\u2212$50,000 each",
         "Line-item underdraw; holdback reallocated to HVAC (Issue 15)."],
        ["Substantial completion deadline", "June 15, 2026", "April 15, 2025 + 14 months = June 15, 2026", "nil on assumed date",
         "If closing occurs May 15, 2025 the deadline becomes July 15, 2026 (Issue 16)."],
        ["Maturity date", "April 15, 2030", "April 15, 2025 + 5 years = April 15, 2030", "nil on assumed date",
         "If closing occurs May 15, 2025, maturity becomes May 15, 2030 (Issue 16)."],
        ["First DSCR test", "About July 15, 2027 (Term Sheet) / April 15, 2027 (markup notes, rent roll)",
         "Month 24 = April 15, 2027; first full quarter ending after that = June 30, 2027, tested about July 15, 2027",
         "one quarter", "Three inconsistent statements (Issue 17)."],
        ["Interest-only period", "24 months to April 15, 2027", "Payments May 15, 2025 to April 15, 2027 inclusive = 24 payments", "nil",
         "Reconciles."],
        ["Survey age at closing", "Dated January 15, 2025", "January 15, 2025 + 90 days = April 15, 2025", "0 days",
         "No margin; re-certification required if closing slips (Issue 19)."],
    ]
    table(d, rows, widths=[1.32, 1.02, 1.92, 0.66, 1.58], size=7)
    para(d, "", space_after=2)
    para(d, "Figures recomputed and found correct without comment: the $1,000,000 net worth and $500,000 liquidity thresholds "
            "(used as stated), the 3.00% SOFR floor plus 285 basis points giving a 5.85% minimum Note Rate, the 5.00% "
            "default-rate spread, the 5.00% late charge, the 3% and 2.5% rent escalations, the $25,000 subcontractor lien "
            "waiver threshold, the $50,000 change-order tolerance in Section 9.2 (a firm concession, not a record figure), "
            "the six parking spaces, and the 31,000 SF / 16,553 SF (0.38 acre) area figures.", size=8.5)


def s6_open(d):
    h1("6.  Open Items and Diligence Requests")
    para(d, "The following items require a document, a third-party confirmation or a client instruction. Items marked "
            "\u201cCP\u201d are conditions to closing that the enclosed draft assumes will be satisfied; if any will not be, "
            "the Mortgage or the closing instructions must be amended before execution.")
    rows = [
        ["#", "Item required", "From", "Needed by", "CP"],
        ["1", "Executed operating agreement amendment (single purpose, separateness, independent manager, unanimous bankruptcy "
              "consent) signed by all three members", "Borrower\u2019s counsel", "Before closing", "Yes"],
        ["2", "Tidewater GP Holdings LLC authority certificate", "Borrower\u2019s counsel", "Before closing", "Yes"],
        ["3", "Full unredacted operating agreement, all exhibits and the March 1, 2025 amendment", "Borrower\u2019s counsel", "Before circulation of final", "No"],
        ["4", "Written confirmation from Prestige Title of coverage terms and premium for Parcel Two (Anson Lane)", "Title insurer", "Immediately", "Yes"],
        ["5", "Tenant estoppel certificates, all three tenants, dated within 30 days of closing", "Borrower / tenants", "Two weeks before closing", "Yes"],
        ["6", "SNDAs, all three tenants", "Borrower / tenants", "Two weeks before closing", "Yes"],
        ["7", "Evidence of City of Charleston encroachment licence or permit for the balcony, or ALTA 28.1 coverage", "Borrower / Title insurer", "Before closing", "Yes"],
        ["8", "Appraisal review and written reconciliation of the income approach", "Pinnacle / review appraiser", "Before closing", "Yes"],
        ["9", "Certified sources and uses statement", "Borrower", "Before closing", "Yes"],
        ["10", "Surveyor\u2019s metes and bounds description for Exhibit A, and re-certification within 90 days of closing", "Cartwright Land Surveying", "Before closing", "Yes"],
        ["11", "Contractor consent to collateral assignment and step-in, plus vapor barrier acknowledgments", "Beaufort Builders Group LLC", "Before first draw", "No"],
        ["12", "Current personal financial statement and liquidity schedule for the Guarantor", "Guarantor", "Before closing", "Yes"],
        ["13", "Ownership chart to natural persons, beneficial ownership certification, good standing certificates", "Borrower", "Before closing", "Yes"],
        ["14", "Corrected renovation draw schedule modelled to the budget and retainage", "Borrower\u2019s consultant", "Before closing instructions", "No"],
        ["15", "Local counsel note on the South Carolina points at Issue 30", "Local counsel", "Before execution", "Yes"],
        ["16", "Credit instructions on Issues 1, 2, 8, 9, 13, 14 and 18", "Mr. Prideaux", "Before finalizing", "No"],
        ["17", "Full Phase I ESA report with appendices, construction contract and all amendments, and the Leases themselves", "Borrower / Clearfield", "Before closing", "No"],
        ["18", "Confirmation of the registered agent and the Bank\u2019s email domain (Issues 26 and 27)", "Bank / Borrower", "Before finalizing", "No"],
    ]
    table(d, rows, widths=[0.3, 3.15, 1.35, 1.05, 0.65], size=8)


def s7_closing(d):
    h1("7.  Closing Conditions Against the Term Sheet")
    para(d, "Term Sheet Section 12 lists fourteen conditions precedent. The table tracks each against the evidence in the "
            "record and against the enclosed draft. Title Commitment Schedule B, Part I requirements are separately tracked at "
            "Exhibit C of the Mortgage.")
    rows = [
        ["Term Sheet \u00a712.1", "Condition", "Status on the record", "Comment"],
        ["(a)", "Execution and delivery of all Loan Documents",
         "Draft Mortgage, Exhibits A\u2013F, signature page and guarantor joinder completed; Note, Guaranty, Environmental Indemnity and UCC-1 to follow",
         "Separate assignment of leases and rents struck \u2014 incorporated into the Mortgage (Issue 29)"],
        ["(b)", "Title commitment and pro forma policy, fee simple in Borrower, first-priority lien, $14,750,000",
         "Commitment PT-2025-04-1178 issued effective February 28, 2025; expires August 28, 2025",
         "Parcel Two coverage unresolved (Issue 5); survey re-certification (Issue 19)"],
        ["(c)", "Satisfactory Phase I ESA, no RECs requiring remediation",
         "Report CLR-2025-0119 dated January 28, 2025: no RECs, no HRECs, one CREC with NFA letter dated August 12, 2021",
         "Satisfied, subject to Issue 7 covenants; Phase II waived by the Bank on January 22, 2025"],
        ["(d)", "Satisfactory appraisal conforming to USPAP and FIRREA",
         "Report PVS-2025-0214-CHS effective February 14, 2025", "Income approach does not support the values (Issue 3)"],
        ["(e)", "Current ALTA/NSPS survey", "Cartwright Land Surveying LLC dated January 15, 2025, recorded Plat Book 64 Page 91",
         "Reaches the 90-day limit on the assumed closing date (Issue 19)"],
        ["(f)", "Evidence of all required insurance, lender named", "Not in the record", "Includes $5,000,000 flood coverage in Zone X (Issue 23)"],
        ["(g)", "Organizational documents, good standing certificates", "Redacted summary only; no certificates", "Issue 22"],
        ["(h)", "Legal opinions of Borrower\u2019s counsel (organization, authorization, enforceability, no conflicts)", "Not in the record",
         "Obtain before closing; note that the SPE amendment affects the authorization opinion"],
        ["(i)", "Payment of origination fee, closing costs and Lender\u2019s legal fees", "Not evidenced",
         "Funding gap at Issue 11 \u2014 $202,075 of known costs alone"],
        ["(j)", "Estoppel certificates from all three tenants, dated within 30 days", "Not obtained; Lowcountry under no obligation to give one",
         "Issue 12 \u2014 principal closing risk"],
        ["(k)", "SNDAs from all three tenants", "Not obtained; Lowcountry lease contains no SNDA provision", "Issue 12"],
        ["(l)", "Complete copy of the executed construction contract with schedules and amendments", "Not in the record",
         "Also obtain the contractor\u2019s consent to assignment (Issue 28)"],
        ["(m)", "Receipt or evidence of the $6,200,000 equity contribution", "Not evidenced",
         "Confirm whether inclusive of closing costs (Issue 11)"],
        ["(n)", "Such other documents as Lender reasonably requires", "Open-ended",
         "SPE amendment (Issue 6), appraisal review (Issue 3), local counsel note (Issue 30)"],
    ]
    table(d, rows, widths=[0.75, 2.1, 1.9, 1.75], size=8)


def s8_trace(d):
    h1("8.  Traceability: Term Sheet Provision to Mortgage")
    para(d, "The table demonstrates that every operative provision of the Term Sheet has been carried into the Mortgage or "
            "deliberately relocated or recorded as inapplicable. Provisions implemented in other Loan Documents are noted as "
            "such so that nothing is assumed to have been dropped.")
    rows = [
        ["Term Sheet", "Subject", "Mortgage provision", "Treatment"],
        ["\u00a71.1\u20131.4", "Parties; guarantor; members", "Recitals; 3.1; 13.4", "Carried"],
        ["\u00a72.1", "Property; legal description; Anson Lane", "2.1; Exhibit A; 3.3; 3.4", "Carried, with quitclaim issue flagged"],
        ["\u00a72.2", "Improvements; area; zoning", "1.1 (Improvements); 3.6", "Carried"],
        ["\u00a72.3", "Existing tenancies; occupancy", "3.5; 5.5; Exhibit D", "Carried; occupancy corrected to 56.13%"],
        ["\u00a72.4", "Appraised value", "Not operative in the Mortgage", "Relied on for credit only; Issue 3"],
        ["\u00a73.1\u20133.3", "Loan amount; purpose; initial advance; holdback", "4.1; 9.1; Recitals B\u2013C", "Carried"],
        ["\u00a73.4", "Total project cost; equity; budget", "Exhibit B; 9.2; 9.6", "Carried; funding gap flagged (Issue 11)"],
        ["\u00a73.5", "Loan metrics", "Not operative", "Recomputed at Section 5; Issues 1 and 3"],
        ["\u00a73.6", "Interest rate; Daily SOFR; floor", "4.2; 4.2(c)", "Carried; convention confirmed at Issue 20"],
        ["\u00a73.7", "Default rate", "4.5", "Carried"],
        ["\u00a73.8", "Maturity", "4.3; 1.1", "Carried; date arithmetic at Issue 16"],
        ["\u00a73.9", "Amortization; interest-only period", "4.3", "Carried"],
        ["\u00a73.10", "Payment date", "4.3; 4.4", "Carried"],
        ["\u00a73.11", "Late charge", "4.6", "Carried"],
        ["\u00a74.1\u20134.3", "Lockout; yield maintenance; open period", "4.7(a)\u2013(e)", "Carried with formula completed (Issue 8)"],
        ["\u00a75.1", "Mortgage collateral description", "2.1\u20132.5; 2.6", "Carried; as-extracted collateral inapplicable"],
        ["\u00a75.2", "Assignment of leases and rents", "Article 5 (absolute assignment)", "Carried into the body, not separate (Issue 29)"],
        ["\u00a75.3", "UCC-1 and fixture filing", "2.4", "Carried"],
        ["\u00a75.4", "Environmental indemnity", "12.2 (cross-reference)", "Separate instrument; secured by the Mortgage"],
        ["\u00a75.5", "Guaranty structure", "1.1 (Guaranty); 12.3; 10.1(m)", "Carried; architecture flagged (Issue 9)"],
        ["\u00a75.6", "Title insurance and endorsements", "1.1 (Title Policy); 7.6; Exhibit C", "Carried; endorsement schedule expanded"],
        ["\u00a76.1\u20136.3", "Escrows and reserves", "6.2; 6.3; 6.4; 6.5; Exhibit F", "Carried; adequacy flagged (Issue 24)"],
        ["\u00a76.4", "Renovation holdback conditions", "9.3", "Carried and expanded"],
        ["\u00a77.1", "DSCR", "7.8(a); 10.1(j)", "Carried; definitions supplied; Issues 1, 2, 17"],
        ["\u00a77.2", "Net worth and liquidity", "7.8(b)\u2013(c)", "Carried on the Borrower as drafted; Issue 13"],
        ["\u00a77.3", "Financial reporting", "7.7(a)\u2013(h)", "Carried; audit conflict at Issue 13"],
        ["\u00a78.1\u20138.4", "Construction; budget; completion; draws", "9.1\u20139.7; 7.13", "Carried and expanded"],
        ["\u00a79.1\u20139.5", "Insurance", "6.6(a)\u2013(f); 3.6", "Carried; flood point at Issue 23"],
        ["\u00a710.1", "Single-purpose entity", "7.5(a)\u2013(m); 8.3", "Carried and made enforceable (Issue 6)"],
        ["\u00a710.2", "No subordinate financing", "8.1", "Carried"],
        ["\u00a710.3", "Transfer restrictions", "8.2(a)\u2013(e)", "Carried and extended to change of control (Issue 10)"],
        ["\u00a710.4\u201310.6", "Compliance; maintenance; leasing", "7.2; 7.1; 5.5", "Carried"],
        ["\u00a711.1", "Events of Default", "10.1(a)\u2013(t)", "Carried as (a)\u2013(o), with additions at (p)\u2013(t)"],
        ["\u00a711.2", "Cure periods", "10.2(a)\u2013(c)", "Carried; LUR cure period added (Issue 7)"],
        ["\u00a712.1", "Conditions precedent", "Not operative in the Mortgage", "Tracked at Section 7 of this memorandum"],
        ["\u00a713.1\u201313.2", "Fees and expenses", "7.12", "Carried"],
        ["\u00a714.1", "Governing law; venue", "13.1; 13.2", "Carried"],
        ["\u00a714.2", "Lender\u2019s counsel", "Cover page; 7.12", "Carried"],
        ["\u00a714.3", "Loan Documents; conflicts", "1.3; 13.8", "Carried; conflicts rule implemented"],
        ["\u00a714.4\u201314.7", "Binding nature; expiration; confidentiality; counterparts", "13.5; 13.6; 13.9; 13.12", "Carried"],
    ]
    table(d, rows, widths=[1.05, 2.05, 1.7, 1.7], size=7.5)


def s9_decisions(d):
    h1("9.  Drafting Decisions and Alternatives")
    para(d, "The following are judgement calls made in the draft that the Bank may wish to revisit. Each states the decision, "
            "the reason, and the alternative if the Bank prefers it.")
    rows = [
        ["Decision", "Reason", "Alternative"],
        ["Absolute assignment of rents incorporated into the Mortgage rather than a separate instrument",
         "Permitted by Term Sheet \u00a75.2 and title Requirement 5; reduces recording cost and centralises enforcement; "
         "satisfies the Assignment of Rents Act on recording",
         "Separate recorded assignment, at additional cost"],
        ["Yield maintenance premium preserves the 1% floor and computes the differential on interest only",
         "The Term Sheet is binding and requires the greater of 1% or the differential; the markup formula omitted the floor "
         "and would have been materially inconsistent",
         "Markup formula, if the Bank waives the floor \u2014 requires a Term Sheet amendment"],
        ["Lockout treated as an absolute prohibition, with a premium if the Bank nonetheless accepts a prepayment",
         "Resolves the contradiction between Term Sheet \u00a74.1 and \u00a74.2 without leaving a gap for months 1\u201324",
         "A free right to prepay on payment of a make-whole during months 1\u201324"],
        ["Casualty and condemnation proceeds applied at par without premium",
         "Term Sheet is silent; the majority position, and the borrower will expect it",
         "Premium on involuntary prepayments (minority position) \u2014 confirm with credit"],
        ["LUR breaches given a cure period (30 days, extended to 180 where SCDHEC action is required), with no cure for "
         "residential conversion",
         "Title commitment requires an Event of Default; an uncurable default for a slow regulatory process invites a "
         "foreclosure defence",
         "No cure period, matching the SPE and transfer defaults"],
        ["Change-of-control covenant added, and the operating agreement\u2019s successor-fund permission disapplied",
         "Neither the Term Sheet nor the operating agreement captures upstream transfers; without it the non-recourse "
         "structure can be circumvented",
         "Rely on the Term Sheet\u2019s literal 10%/25% thresholds, accepting the gap"],
        ["Net worth and liquidity drafted on the Borrower",
         "Faithful to Term Sheet \u00a77.2, which names the Borrower",
         "Move to the Guarantor and increase the thresholds \u2014 requires instruction (Issue 13)"],
        ["Guarantor joined for limited purposes only (LUR, carve-outs, transfer covenant, notices, jurisdiction)",
         "Guarantor is not a mortgagor; a limited joinder gives the Bank standing on the LUR covenants without making him a "
         "party to every covenant",
         "No joinder, leaving the LUR covenants enforceable only against the Borrower"],
        ["No power of sale; judicial foreclosure stated expressly",
         "South Carolina is a judicial foreclosure state; a power of sale would be void and would create confusion in "
         "enforcement",
         "None \u2014 this is a legal requirement, not a preference"],
        ["Two subscribing witnesses and a South Carolina notarial acknowledgment on the signature page",
         "Required for recording; the draft implements the formality rather than assuming it",
         "None \u2014 but confirm the current statutory requirement with local counsel (Issue 30)"],
        ["As-extracted collateral recorded as inapplicable",
         "The Property is an improved commercial building; the Term Sheet\u2019s reference is conditional (\u201cif any\u201d)",
         "None"],
    ]
    table(d, rows, widths=[2.25, 2.6, 1.65], size=8)


def s10_close(d):
    h1("10.  Assumptions and Limitations")
    pts = [
        "This memorandum and the enclosed draft are prepared for Calverley Heritage Bank for the purposes of this loan. They "
        "are not for the benefit of the borrower or any other party, and no other party may rely on them without our written "
        "consent.",
        "We have reviewed the sources listed at Section 2.2 in full, but we have not reviewed the full Phase I ESA report and "
        "appendices, the construction contract, the underlying Leases (only the borrower-prepared abstracts), the survey, the "
        "complete unredacted operating agreement, the limited partnership agreement of Tidewater Opportunity Fund II LP, or "
        "any of the Guarantor\u2019s financial information. Conclusions that depend on those documents are identified as open "
        "items at Section 6.",
        "Figures described as recomputed were derived independently from the components stated in the sources. Where a source "
        "figure is internally inconsistent, both the stated and the recomputed figure are reported and the inconsistency is "
        "identified; the draft adopts the figure that the components support and, in the case of occupancy, says so on the "
        "face of the instrument.",
        "Statements of South Carolina law in this memorandum and in the draft are based on the statutes and propositions "
        "referred to in the record and should be confirmed by local counsel before execution (Issue 30). Nothing in this "
        "memorandum is tax advice.",
        "The draft assumes that the loan closes on April 15, 2025. If the closing date changes, the defined dates in Section "
        "1.1, the interest-only period, the yield maintenance windows and the draw schedule must be conformed (Issue 16).",
        "Recommendations in this memorandum are directed to documentation and credit structure. The decisions at Issues 1, 2, "
        "3, 8, 9, 13, 14 and 18 are commercial or credit decisions for the Bank, and we have not made them.",
    ]
    for i, t in enumerate(pts, 1):
        rich(d, [(f"({chr(96+i)})", False, False), ("\u2003", False, False), (t, False, False)],
             left=0.4, first=-0.4, space_after=5)
    h1("11.  Next Steps")
    rows = [
        ["Step", "Owner", "Target"],
        ["Circulate the draft Mortgage and this memorandum to the Bank", "J. Vickers", "April 2, 2025"],
        ["Obtain credit instructions on Issues 1, 2, 8, 9, 13, 14 and 18", "M. Prideaux", "April 4, 2025"],
        ["Raise Parcel Two coverage with Prestige Title; engage the appraisal reviewer", "J. Vickers", "April 4, 2025"],
        ["Request the operating agreement amendment, estoppels, SNDAs, encroachment licence and Guarantor PFS", "J. Vickers", "April 4, 2025"],
        ["Commission the local counsel note on Issue 30", "C. Ashworth", "April 9, 2025"],
        ["Conform the draft to instructions and circulate the execution version", "J. Vickers", "April 11, 2025"],
        ["Confirm the final closing date and conform defined dates; obtain survey re-certification", "J. Vickers", "3 days before closing"],
    ]
    table(d, rows, widths=[4.0, 1.15, 1.35], size=8.5)
    para(d, "", space_after=14)
    para(d, "We are available to discuss any of the foregoing at your convenience. Please direct instruction on the open "
            "items to the undersigned, copied to Ms. Ashworth.", space_after=18)
    para(d, "Respectfully submitted,", space_before=6, space_after=24)
    para(d, "Jordan Vickers", bold=True, align="left", space_after=0)
    para(d, "Associate", size=10, italic=True, align="left", space_after=0)
    para(d, "Fielding, Ashworth & Cole LLP", size=10, align="left", space_after=0)
    para(d, "Charleston, South Carolina", size=10, align="left", space_after=10)
    para(d, "Reviewed by Catherine \u201cKit\u201d Ashworth, Partner, Real Estate Practice Group Chair", size=9.5, italic=True, align="left", space_after=0)
    hr(d, space_before=14, space_after=4)
    para(d, "Attachment: Mortgage and Security Agreement (with Absolute Assignment of Leases, Rents and Profits; Security "
            "Agreement; and Fixture Filing), with Exhibits A\u2013F.", size=8.5, italic=True)


def main():
    global doc
    doc = new_document()
    header(doc, "Privileged and Confidential \u2014 Attorney Work Product \u2014 CHB CRE Loan No. 2025-CHS-0047")
    footer(doc, "Drafting Issues Memorandum \u2014 CHB CRE Loan No. 2025-CHS-0047", size=7.5)
    doc.sections[0].different_first_page_header_footer = True
    front_matter(doc)
    s1_purpose(doc)
    s2_scope(doc)
    s3_register(doc)
    s4_issues(doc)
    s5_recompute(doc)
    s6_open(doc)
    s7_closing(doc)
    s8_trace(doc)
    s9_decisions(doc)
    s10_close(doc)
    out = "/workspace/output/drafting-issues-memorandum.docx"
    doc.save(out)
    print("wrote", out)

if __name__ == "__main__":
    main()
