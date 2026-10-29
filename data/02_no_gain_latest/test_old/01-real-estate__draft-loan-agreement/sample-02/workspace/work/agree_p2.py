# -*- coding: utf-8 -*-
import sys; sys.path.insert(0,'/workspace/work')
from dh import *
from docx.enum.text import WD_ALIGN_PARAGRAPH as AL

DEFS = [
("Affected Area","means that portion of the Property consisting of approximately 0.38 acres in the northeast corner of "
 "Parcel 0821-04-72-4102, as delineated in the Phase II Environmental Investigation report prepared by Sentinel "
 "Environmental Consulting LLC dated August 30, 2024 and as described in the NFA Letter and in the recorded deed notice "
 "required by Section 12.5, the metes and bounds of which shall be confirmed by survey prior to Closing."),
("Affiliate","means, as to any Person, any other Person that directly or indirectly controls, is controlled by, or is under "
 "common control with, such Person, and, with respect to any individual, includes such individual's spouse, descendants and "
 "any trust or entity established for the benefit of any of them."),
("Agreement","means this Construction-to-Mini-Permanent Loan Agreement, as it may be amended, restated or supplemented from time to time."),
("Approved Plans and Specifications","means the plans and specifications for the Project prepared by Meridian Design "
 "Collective PC, drawing set dated September 12, 2024, as approved by Lender and as the same may be modified only in "
 "accordance with Section 8.8."),
("Approved Project Budget","means the project budget and sources and uses of funds set forth on Schedule 2, as the same may "
 "be revised only with Lender's prior written consent in accordance with Section 4.5."),
("Assignment of Leases and Rents","means the Assignment of Leases and Rents dated as of the Closing Date from Borrower to Lender."),
("Business Day","means any day other than a Saturday, Sunday or day on which commercial banks in Charlotte, North Carolina or "
 "New York, New York are authorized or required by law to be closed."),
("Carry Guaranty","means the Carry Guaranty dated as of the Closing Date executed by each Guarantor in favor of Lender."),
("Closing","and \u201cClosing Date\u201d mean the date on which the initial Advance is made under the Loan."),
("Code","means the Internal Revenue Code of 1986, as amended."),
("Commitment","means Lender's commitment to make Advances under the Loan in an aggregate principal amount not to exceed the Loan Amount."),
("Completion Guaranty","means the Completion Guaranty dated as of the Closing Date executed by each Guarantor in favor of Lender."),
("Construction Contract","means the guaranteed maximum price construction contract dated [__________], 2024 between Borrower "
 "and Graystone Construction Group Inc. (NC General Contractor License No. 78442), in the guaranteed maximum price amount of "
 "$34,750,000, as collaterally assigned to Lender."),
("Construction Inspector","means the third-party construction consulting and inspection firm engaged by Lender at Borrower's "
 "expense pursuant to Section 4.7, and any replacement thereof."),
("Construction Maturity Date","means August 28, 2027, being the date that is thirty (30) months after the anticipated Closing Date of February 28, 2025."),
("Construction Period","means the period from the Closing Date through and including the Construction Maturity Date."),
("Contingency","means the contingency line items of the Approved Project Budget in the aggregate amount of $1,440,000, "
 "consisting of the hard cost contingency of $1,140,000 and the soft cost contingency of $300,000."),
("Credit Memorandum","has the meaning given in Recital E."),
("Deed of Trust","means the Deed of Trust, Assignment of Rents, Security Agreement and Fixture Filing dated as of the Closing "
 "Date, granted by Borrower to the Trustee for the benefit of Lender, encumbering the Property and securing the Loan."),
("Default Rate","means a rate per annum equal to the sum of (a) the otherwise applicable Interest Rate plus (b) five percent (5.00%)."),
("Developer Fee","means the development fee payable to Borrower in the amount of $2,835,000, of which $1,835,000 is included in "
 "the Approved Project Budget as a cost to be funded from the proceeds of the Loan and $1,000,000 is to be funded from sources "
 "other than the Loan, as described in Schedule 2."),
("Draw Request","means a written request for an Advance substantially in the form attached as Exhibit B."),
("Draw Schedule","means the draw schedule and construction milestones set forth on Schedule 1, as the same may be adjusted only in accordance with Section 4.5."),
("Eligible Assignee","means a commercial bank, savings bank, savings and loan association, insurance company, pension fund, "
 "real estate investment trust, or other financial institution or institutional investor reasonably acceptable to Lender."),
("Environmental Indemnity","means the Environmental Indemnity Agreement dated as of the Closing Date executed by Borrower and each Guarantor in favor of Lender."),
("Environmental Laws","means all federal, state and local statutes, regulations, ordinances and orders relating to pollution, "
 "protection of human health or the environment, or to the presence, release, threatened release, storage, treatment, "
 "transportation or disposal of Hazardous Materials, including the Comprehensive Environmental Response, Compensation, and "
 "Liability Act, the Resource Conservation and Recovery Act, the Clean Water Act, the Clean Air Act, the North Carolina "
 "Oil Pollution and Hazardous Substances Control Act (N.C.G.S. Chapter 143, Article 21A), the North Carolina Inactive "
 "Hazardous Sites Program (N.C.G.S. Chapter 130A, Article 9), and the North Carolina Brownfields Property Reuse Act "
 "(N.C.G.S. Chapter 130A, Article 9, Part 5), in each case as amended."),
("Equity Contribution","means the equity contribution required to be made by Borrower pursuant to Section 3.7 in the amount of "
 "$[4,080,000], representing the amount by which Total Project Costs, as corrected and set forth in Schedule 2, exceed the sum "
 "of the Loan Amount and the Mezzanine Loan."),
("Equity Escrow Account","means the interest-bearing deposit account maintained by Lender (or by the Title Company as escrow "
 "agent, pursuant to escrow instructions acceptable to Lender) into which the Equity Contribution is deposited."),
("Event of Default","has the meaning given in Article XIII."),
("Extension Option","has the meaning given in Section 2.14."),
("Fees","means, collectively, the Origination Fee, the Exit Fee, the Unused Line Fee, the Extension Fee and any other fees payable under the Loan Documents."),
("GAAP","means generally accepted accounting principles in the United States of America, consistently applied."),
("GMP Contract","has the meaning given to \u201cConstruction Contract\u201d."),
("Guaranties","means, collectively, the Completion Guaranty, the Carry Guaranty, the Partial Repayment Guaranty and the Environmental Indemnity."),
("Hazardous Materials","means petroleum, petroleum products, petroleum hydrocarbons, asbestos, polychlorinated biphenyls, "
 "radon, mold, urea formaldehyde, per- and polyfluoroalkyl substances, and any other substance, material or waste that is "
 "regulated as hazardous, toxic or a pollutant under any Environmental Laws."),
("Indebtedness","means, without duplication, all obligations for borrowed money, all purchase money obligations, all "
 "capitalized lease obligations, all obligations evidenced by notes or bonds, all contingent reimbursement obligations, and "
 "all guarantees of any of the foregoing."),
("Initial Advance","means the Advance made on the Closing Date pursuant to Draw No. 1 of the Draw Schedule."),
("Insurance Proceeds","means all proceeds of insurance payable in respect of the Property or the Project."),
("Intercreditor Agreement","means the intercreditor and subordination agreement dated as of or prior to the Closing Date among "
 "Lender, Mezzanine Lender and Borrower, in form and substance satisfactory to Lender, satisfying the requirements of Section 3.8."),
("Interest Period","means each calendar month during the term of the Loan; interest shall be computed for each Interest Period "
 "on the basis of the actual number of days elapsed and a year of three hundred sixty (360) days."),
("Interest Rate","means, (a) during the Construction Period, the lesser of (i) Daily Simple SOFR plus 3.25% per annum and (ii) the "
 "Maximum Rate, and (b) during the Mini-Perm Period, the lesser of (i) Daily Simple SOFR plus 3.50% per annum and (ii) the Maximum Rate."),
("Interest Reserve","means the interest reserve in the amount of $4,850,000 funded from the proceeds of the Loan at Closing and held in the Interest Reserve Account."),
("Interest Reserve Account","means the segregated sub-account of the Loan maintained by Lender for the Interest Reserve pursuant to Article V."),
("Lender Parties","means Lender, its Affiliates, and their respective directors, officers, employees, agents, attorneys and advisors."),
("Loan","means the construction-to-mini-permanent loan in the maximum principal amount of the Loan Amount made by Lender to Borrower under this Agreement."),
("Loan Amount","means Forty-Seven Million Five Hundred Thousand and No/100 Dollars ($47,500,000)."),
("Loan Documents","means this Agreement, the Note, the Deed of Trust, the Assignment of Leases and Rents, the Security "
 "Agreement, the Assignments of Construction Contract and Architect's Agreement, the Collateral Assignment of Insurance "
 "Proceeds and Condemnation Awards, the Membership Interest Pledge Agreements, the Guaranties, the Environmental Indemnity, "
 "the Intercreditor Agreement, all UCC financing statements, and each other instrument, agreement, certificate or opinion "
 "delivered in connection with the Loan, in each case as amended, restated or supplemented from time to time."),
("Material Adverse Effect","means a material adverse effect on (a) the business, assets, operations or financial condition of "
 "Borrower or any Guarantor, (b) the value, marketability or condition of the Property or the Project, (c) the ability of "
 "Borrower or any Guarantor to perform its obligations under the Loan Documents, or (d) the validity, enforceability or "
 "priority of any Lien granted to Lender under the Loan Documents."),
("Maximum Rate","means the maximum rate of interest permitted by applicable law, including N.C.G.S. \u00a7 24-1.1 and related provisions."),
("Membership Interest Pledges","means the pledge agreements dated as of the Closing Date pursuant to which each member of "
 "Borrower pledges one hundred percent (100%) of its membership interest in Borrower to Lender as security for the Loan, "
 "subject and subordinate in priority only as expressly provided in the Intercreditor Agreement."),
("Mezzanine Documents","means the loan agreement, promissory note, pledge agreement and other documents evidencing and "
 "securing the Mezzanine Loan."),
("Mezzanine Lender","means Brightleaf Mezzanine Capital LLC, a North Carolina limited liability company (NC Secretary of State File No. 2103988)."),
("Mezzanine Loan","has the meaning given in Recital F, in the principal amount of $9,200,000, bearing interest at a fixed rate of 12.50% per annum."),
("Mini-Perm Maturity Date","means August 28, 2028, being the date that is twelve (12) months after the Construction Maturity Date, as the same may be extended to the Extended Maturity Date pursuant to Section 2.14."),
("Mini-Perm Period","means the period from and after the Construction Maturity Date through and including the Mini-Perm Maturity Date (as the same may be extended)."),
("NFA Letter","has the meaning given in Recital H, being the conditional No Further Action determination letter issued by NCDEQ "
 "(Inactive Hazardous Sites Branch) dated September 30, 2024, with respect to Site ID IHSB-24-1203 / Incident No. NONUST-24-0847."),
("NCDEQ","means the North Carolina Department of Environmental Quality, or any successor agency."),
("Note","means the Promissory Note dated as of the Closing Date in the principal amount of the Loan Amount, executed by Borrower and payable to the order of Lender."),
("Origination Fee","means a fee equal to one percent (1.00%) of the Loan Amount, or $475,000, payable at Closing."),
("Partial Repayment Guaranty","means the Partial Repayment Guaranty dated as of the Closing Date executed by each Guarantor in "
 "favor of Lender, in an aggregate amount not to exceed $11,875,000 as provided in Section 11.3."),
("Permitted Exceptions","means those matters listed on Schedule 3 and such other matters as Lender may approve in writing."),
("Person","means any individual, corporation, partnership, limited liability company, trust, association, joint venture, governmental authority or other entity."),
("Phase I ESA","means the Phase I Environmental Site Assessment prepared by Sentinel Environmental Consulting LLC dated October 28, 2024 (Sentinel Project No. SEC-2024-1147)."),
("Phase II ESA","means the Phase II Environmental Investigation prepared by Sentinel Environmental Consulting LLC dated August 30, 2024 (Sentinel Project No. SEC-2024-1089)."),
("Project Budget","has the meaning given to \u201cApproved Project Budget\u201d."),
("Retainage","means, with respect to each Advance for hard construction costs, an amount equal to ten percent (10%) of the "
 "gross amount of such Advance, to be held by Lender and released as provided in Section 4.4, in the aggregate amount of $3,475,000."),
("SOFR","means Daily Simple SOFR."),
("Daily Simple SOFR","means, for any day, the Secured Overtime Financing Rate published by the Federal Reserve Bank of New "
 "York (or a successor administrator selected by Lender in its reasonable discretion) for such day, in each case giving "
 "effect to the SOFR Floor and to the Benchmark Replacement provisions of Section 2.6."),
("SOFR Floor","means one percent (1.00%) per annum; if Daily Simple SOFR for any day is less than 1.00%, Daily Simple SOFR shall be deemed to be 1.00% for such day."),
("Security Agreement","means the Security Agreement dated as of the Closing Date between Borrower and Lender."),
("Soil Management Plan","means the soil management plan for the Affected Area required by Condition 3 of the NFA Letter, as approved by NCDEQ, and any approved amendments thereto."),
("SPE Covenants","means the single-purpose entity covenants set forth in Article XV."),
("Substantial Completion","means completion of the Project in accordance with the Approved Plans and Specifications such that "
 "a final unconditional certificate of occupancy has been issued by the City of Durham for all residential units and retail "
 "spaces in the Project and the Project is ready for its intended occupancy and use."),
("Title Company","means Aldersgate Title & Escrow Inc., or such other title insurance company as Lender may approve."),
("Title Policy","means the ALTA Loan Policy of title insurance (2006 form, as amended) issued by the Title Company in the "
 "amount of the Loan Amount, insuring the Deed of Trust as a first priority lien on the Property subject only to the "
 "Permitted Exceptions, together with such endorsements as Lender may require."),
("Total Project Costs","means the aggregate of all costs and expenses incurred or to be incurred in connection with the "
 "acquisition, development, construction and completion of the Project, as set forth in the Approved Project Budget, "
 "including the land acquisition cost of $8,200,000 and all costs identified in Section 9.1(c)."),
("Uniform Commercial Code","or \u201cUCC\u201d means the Uniform Commercial Code as in effect in the State of North Carolina."),
("Unused Line Fee","means the fee described in Section 2.10(c)."),
("Vapor Mitigation System","means the passive sub-slab depressurization system (with capability for conversion to active "
 "depressurization) required by Condition 1 of the NFA Letter to be installed and maintained beneath any enclosed structure "
 "constructed over the Affected Area."),
]

def build_part2(doc):
    art(doc, "ARTICLE I — DEFINITIONS AND INTERPRETATION")
    sec_h(doc, "Section 1.1  Defined Terms")
    para(doc, "Capitalized terms used in this Agreement have the meanings set forth below or elsewhere in this Agreement. "
              "Terms defined in the singular have the same meaning in the plural and vice versa.")
    for term, defn in DEFS:
        p = doc.add_paragraph()
        p.paragraph_format.left_indent = Inches(0.35)
        p.paragraph_format.first_line_indent = Inches(-0.35)
        p.paragraph_format.space_after = Pt(5)
        p.paragraph_format.tab_stops.add_tab_stop(Inches(0.35))
        r = p.add_run("\u201c" + term + "\u201d\t"); r.bold = True; r.font.name = FONT; r.font.size = Pt(10.5)
        add_runs(p, defn, size=10.5)

    sec_h(doc, "Section 1.2  Interpretation")
    para(doc, "In this Agreement, unless the context otherwise requires: (a) the words \u201cinclude,\u201d \u201cincludes\u201d "
              "and \u201cincluding\u201d are deemed to be followed by the words \u201cwithout limitation\u201d; (b) \u201cor\u201d "
              "is not exclusive; (c) references to Articles, Sections, Schedules and Exhibits are to Articles and Sections of, and "
              "Schedules and Exhibits to, this Agreement, each of which is incorporated herein by reference; (d) headings are for "
              "convenience only and do not affect interpretation; (e) references to any statute or regulation include any amendment, "
              "successor or re-enactment thereof; and (f) references to any agreement or instrument mean such agreement or instrument "
              "as amended, restated, supplemented or otherwise modified from time to time in accordance with its terms.")
    para(doc, "This Agreement and the other Loan Documents were negotiated by the parties with the benefit of counsel and shall "
              "not be construed more strictly against either party by reason of the identity of the drafting party.")

    sec_h(doc, "Section 1.3  Accounting Terms; Rounding")
    para(doc, "All accounting terms not otherwise defined herein have the meanings assigned to them in accordance with GAAP. "
              "All financial covenant calculations shall be made in accordance with GAAP, except that (a) Total Project Costs "
              "shall be determined on the cost basis set forth in the Approved Project Budget and not on a GAAP basis, and "
              "(b) Borrower's Net Worth for purposes of Section 9.4 shall be determined in accordance with Section 9.4(c).")
    para(doc, "Percentages and ratios shall be calculated to two decimal places and, except as otherwise provided, financial "
              "covenants shall be tested as of the last day of each calendar quarter or fiscal year, as applicable, and shall be "
              "measured against the immediately preceding twelve (12) months of operations unless the relevant Section specifies otherwise.")

    sec_h(doc, "Section 1.4  Conflict Among Loan Documents")
    para(doc, "In the event of any conflict between the terms of this Agreement and the terms of any other Loan Document, the "
              "terms of this Agreement shall control. In the event of any conflict between the terms of this Agreement and the "
              "Term Sheet or the Credit Memorandum, the terms of this Agreement shall control as between Lender and Borrower, it "
              "being understood that the Term Sheet is binding only to the extent expressly provided in Sections 22 and 23 thereof "
              "(confidentiality, exclusivity and the expense deposit). Nothing in this Section shall limit the effect of any "
              "condition to closing that is restated herein.")

    # ---------------- ARTICLE II ----------------
    art(doc, "ARTICLE II — THE LOAN")
    sec_h(doc, "Section 2.1  The Commitment")
    para(doc, "Subject to the terms and conditions of this Agreement and the other Loan Documents, Lender agrees to make "
              "Advances to Borrower from time to time during the Construction Period in an aggregate principal amount not to "
              "exceed the Loan Amount. The Loan is a single facility with multiple disbursements and is not a revolving "
              "facility; no amount repaid or prepaid may be reborrowed. [Drafting Note: Section 3.1 of the Term Sheet describes "
              "the Loan as a \u201csingle advance facility\u201d while Section 9 of the Term Sheet contemplates nine milestone "
              "draws. The formulation above preserves the single-commitment structure while confirming the milestone disbursement "
              "mechanics. See Cover Memorandum Issue No. 19.]",
         )
    sec_h(doc, "Section 2.2  Purpose and Use of Proceeds")
    para(doc, "The proceeds of the Loan shall be used solely to finance (a) hard construction costs of the Project under the "
              "Construction Contract, (b) soft costs of the Project, in each case as set forth in the Approved Project Budget, "
              "(c) interest on the Loan through the Interest Reserve, (d) the Origination Fee, and (e) that portion of the "
              "Developer Fee identified in Schedule 2 as funded from the Loan. No proceeds of the Loan shall be used (i) to pay "
              "any dividend, distribution, return of capital or other payment to any member of Borrower other than the Developer "
              "Fee as permitted by Section 8.7, (ii) to pay any amount in respect of the Mezzanine Loan, (iii) to pay any cost "
              "that is not an approved line item of the Approved Project Budget, or (iv) for any purpose that would violate any "
              "applicable law, including any anti-terrorism, anti-money laundering or sanctions law.")

    sec_h(doc, "Section 2.3  The Note")
    para(doc, "The Loan shall be evidenced by the Note, which shall be executed by Borrower at Closing and shall be payable to "
              "the order of Lender in the principal amount of the Loan Amount, bearing interest at the Interest Rate and "
              "maturing on the Mini-Perm Maturity Date. The Note shall be entitled to the benefits of this Agreement and the "
              "other Loan Documents, and all payments made on the Note shall be applied as provided in Section 2.11.")

    sec_h(doc, "Section 2.4  Advances; Minimum and Maximum Amounts")
    para(doc, "Advances shall be made only in accordance with the Draw Schedule and Article IV. Except for the Initial Advance "
              "and the final Advance, each Advance for hard construction costs shall be in a minimum amount of $500,000, and no "
              "Advance shall exceed the applicable line item amount shown on the Draw Schedule. Lender shall not be obligated to "
              "make any Advance after the Construction Maturity Date except for (a) the release of Retainage in accordance with "
              "Section 4.4, (b) Advances from the Contingency approved by Lender in accordance with Section 4.5, and (c) any "
              "Advance of the Interest Reserve as permitted by Article V.")

    sec_h(doc, "Section 2.5  Interest Rate")
    para(doc, "The outstanding principal balance of the Loan shall bear interest at the applicable Interest Rate. During the "
              "Construction Period the applicable spread over Daily Simple SOFR is 3.25% per annum; during the Mini-Perm Period "
              "the applicable spread is 3.50% per annum. In no event shall the Interest Rate be less than the sum of the SOFR "
              "Floor plus the applicable spread. Interest shall accrue on the basis of the actual number of days elapsed over a "
              "360-day year and shall be computed on the daily outstanding principal balance of the Loan.")
    para(doc, "Illustration (for informational purposes only). At a Daily Simple SOFR of 4.35% per annum, the all-in "
              "construction period rate would be 7.60% per annum and the all-in Mini-Perm Period rate would be 7.85% per annum. "
              "The SOFR Floor of 1.00% produces a minimum all-in rate of 4.25% during the Construction Period and 4.50% during the "
              "Mini-Perm Period.")

    sec_h(doc, "Section 2.6  Benchmark Replacement; Conforming Changes")
    para(doc, "If Lender determines in its reasonable discretion that (a) Daily Simple SOFR has been permanently or indefinitely "
              "discontinued or is no longer representative, (b) the administrator of SOFR or its supervisor has publicly announced "
              "that it has ceased or will cease to provide SOFR, or (c) the Federal Reserve Bank of New York or any successor "
              "administrator has ceased to publish SOFR, then Lender may designate a Benchmark Replacement, together with any "
              "mathematically applied spread adjustment, in each case giving due consideration to the recommended best practices "
              "of the Alternative Reference Rates Committee (or any successor or similar committee). Lender shall provide Borrower "
              "with not less than thirty (30) days' prior written notice of any Benchmark Replacement, and any Benchmark "
              "Replacement shall be a rate substantially comparable to SOFR, determined without reference to Borrower's credit "
              "standing. Lender may make conforming changes to the mechanics of calculating interest, the timing of interest "
              "payments and related provisions to reflect the Benchmark Replacement.")

    sec_h(doc, "Section 2.7  Payments of Interest")
    para(doc, "Interest on the outstanding principal balance of the Loan shall be payable monthly in arrears on the first (1st) "
              "Business Day of each calendar month, commencing on the first Business Day of the first full calendar month "
              "following the Closing Date, and continuing on each such day thereafter through and including the Mini-Perm "
              "Maturity Date, when the entire outstanding principal balance of the Loan, all accrued and unpaid interest and all "
              "other amounts payable under the Loan Documents shall be due and payable in full.")
    para(doc, "During the Construction Period, interest shall be paid from the Interest Reserve Account in accordance with "
              "Article V until the Interest Reserve is exhausted; thereafter, and in any event upon exhaustion of the Interest "
              "Reserve, interest shall be paid by Borrower from its own funds, and Borrower's obligation to pay interest is "
              "absolute and unconditional. There is no scheduled amortization of principal; the Loan is interest only throughout "
              "the Construction Period and the Mini-Perm Period.")

    sec_h(doc, "Section 2.8  Default Rate")
    para(doc, "Upon the occurrence and during the continuance of an Event of Default, the outstanding principal balance of the "
              "Loan and, to the extent permitted by applicable law, all accrued and unpaid interest and other amounts payable "
              "under the Loan Documents, shall bear interest at the Default Rate, from the date of the occurrence of the Event of "
              "Default until such Event of Default is waived in writing by Lender or cured. Interest at the Default Rate shall be "
              "payable on demand and shall be secured by the Loan Documents.")

    sec_h(doc, "Section 2.9  Computation of Interest and Fees")
    para(doc, "All computations of interest and fees shall be made on the basis of the actual number of days elapsed over a "
              "360-day year. Each determination by Lender of the Interest Rate, the Default Rate or the amount of interest or any "
              "fee payable under the Loan Documents shall be conclusive and binding on Borrower absent manifest error, and Lender "
              "shall provide Borrower with a statement of any such determination upon request.")

    sec_h(doc, "Section 2.10  Fees")
    numbered(doc, "(a)", "Origination Fee. Borrower shall pay Lender an origination fee equal to one percent (1.00%) of the Loan "
             "Amount, or $475,000, which is fully earned and non-refundable on the Closing Date and which may be funded from the "
             "Initial Advance in accordance with the Approved Project Budget.")
    numbered(doc, "(b)", "Exit Fee. Borrower shall pay Lender an exit fee on the date of repayment of the Loan in accordance with "
             "the following schedule: (i) if the Loan is repaid in full at any time during the Construction Period, an amount "
             "equal to one-half of one percent (0.50%) of the outstanding principal balance of the Loan at the time of "
             "repayment; (ii) if the Loan is repaid in full during the first six (6) months of the Mini-Perm Period, an amount "
             "equal to one-quarter of one percent (0.25%) of the outstanding principal balance of the Loan at the time of "
             "repayment; and (iii) no exit fee shall be payable if the Loan is repaid in full after the first six (6) months of "
             "the Mini-Perm Period. The Exit Fee shall also be payable upon acceleration of the Loan following an Event of "
             "Default or upon any repayment with proceeds of a foreclosure or deed in lieu of foreclosure.")
    numbered(doc, "(c)", "Unused Line Fee. Borrower shall pay Lender a fee equal to one-quarter of one percent (0.25%) per annum "
             "on the average daily undrawn amount of the Commitment, payable quarterly in arrears commencing on the first "
             "quarterly payment date following the Closing Date and continuing until the Commitment is fully drawn or the Loan "
             "is repaid. For purposes of this Section, the undrawn amount of the Commitment shall be reduced by the full amount "
             "of the Interest Reserve and the Contingency as of the Closing Date, it being acknowledged that such amounts are "
             "reserved for identified uses and are not available for general disbursement.")
    numbered(doc, "(d)", "Extension Fee. Borrower shall pay Lender an extension fee equal to one-quarter of one percent (0.25%) "
             "of the then-outstanding principal balance of the Loan as a condition to the effectiveness of the Extension Option.")
    numbered(doc, "(e)", "Expense Deposit. Lender acknowledges receipt of the expense deposit of $75,000 paid by Borrower under "
             "Section 22 of the Term Sheet, which shall be credited against the amounts payable by Borrower under Section 18.2 "
             "and, to the extent not so applied, against the Origination Fee at Closing. [Drafting Note: The expense deposit is "
             "not reflected in the Sources and Uses on Schedule 2 and the Approved Project Budget funds Lender's counsel and "
             "title costs of $310,000 from Loan proceeds. The parties should confirm that no costs are funded twice. See Cover "
             "Memorandum Issue No. 17.]")

    sec_h(doc, "Section 2.11  Manner and Application of Payments")
    para(doc, "All payments under the Loan Documents shall be made in immediately available funds in lawful money of the United "
              "States, without setoff, counterclaim, deduction or withholding, to an account designated by Lender in writing, not "
              "later than 2:00 p.m. Eastern Time on the due date. Any payment received after 2:00 p.m. Eastern Time shall be "
              "deemed received on the next Business Day. All payments shall be applied in the following order: (a) to amounts "
              "payable to Lender under Section 18.2; (b) to fees and other charges then due; (c) to accrued and unpaid interest; "
              "and (d) to principal. Lender may, in its discretion, apply any payment received during the continuance of an Event "
              "of Default in such order as Lender determines.")

    sec_h(doc, "Section 2.12  Prepayment")
    para(doc, "The Loan may be prepaid in whole or in part at any time, without premium or penalty, other than the Exit Fee "
              "provided in Section 2.10(b), upon not less than five (5) Business Days' prior written notice to Lender. No "
              "prepayment shall relieve Borrower of any obligation to pay the Exit Fee, the Unused Line Fee, Lender's expenses "
              "under Section 18.2 or any other amount then due under the Loan Documents, and no amount prepaid may be reborrowed.")

    sec_h(doc, "Section 2.13  Maturity")
    para(doc, "The entire outstanding principal balance of the Loan, together with all accrued and unpaid interest and all other "
              "amounts owing under the Loan Documents, shall be due and payable in full on the Mini-Perm Maturity Date, subject "
              "only to Borrower's exercise of the Extension Option in accordance with Section 2.14. Borrower acknowledges that "
              "Lender has made no commitment to extend, renew or refinance the Loan and that the Loan is a balloon obligation.")

    sec_h(doc, "Section 2.14  Extension Option")
    para(doc, "Borrower shall have one option (the \u201cExtension Option\u201d) to extend the Mini-Perm Maturity Date by six (6) "
              "months, to February 28, 2029 (the \u201cExtended Maturity Date\u201d), exercisable only upon satisfaction of each of "
              "the following conditions on or before the Mini-Perm Maturity Date:")
    ext = [
        "No Default. No Event of Default shall exist, and no event shall have occurred that, with the giving of notice or the "
        "lapse of time, or both, would constitute an Event of Default under any Loan Document or under the Intercreditor Agreement.",
        "Notice. Borrower shall have delivered written notice of its election to exercise the Extension Option not less than "
        "sixty (60) days prior to the Mini-Perm Maturity Date, together with payment of the Extension Fee.",
        "Completion. Substantial Completion shall have been achieved and a final, unconditional certificate of occupancy shall "
        "have been issued by the City of Durham for all residential units and retail spaces in the Project.",
        "Occupancy. Not less than seventy-five percent (75%) of the residential units in the Project shall be leased to tenants "
        "under executed leases having initial terms of not less than twelve (12) months and shall be physically occupied as of "
        "the date of the extension request.",
        "Minimum DSCR. The Debt Service Coverage Ratio, calculated as set forth in Section 9.3 using the annualized in-place net "
        "operating income for the most recent three (3) month period, divided by the annual debt service on the outstanding "
        "principal balance of the Loan at the then-current Interest Rate (interest only), shall be not less than 1.15x.",
        "Updated Appraisal. Lender shall have received an updated appraisal from an MAI-designated appraiser acceptable to "
        "Lender confirming that the ratio of the outstanding principal balance of the Loan to the as-stabilized appraised value "
        "of the Property does not exceed seventy percent (70%).",
        "Interest Rate Cap. If required by Lender, Borrower shall have delivered an interest rate cap agreement, in form and "
        "substance satisfactory to Lender, with a strike rate not greater than the rate reasonably required by Lender, from a "
        "counterparty having a long-term unsecured credit rating of not less than A- (S&P) or A3 (Moody's), covering the "
        "outstanding principal balance of the Loan through the Extended Maturity Date, together with an assignment of the cap "
        "to Lender and Lender's confirmation of control.",
        "Third-Party Consents. The Intercreditor Agreement shall remain in full force and effect, no default shall exist "
        "thereunder, and the Mezzanine Loan shall have been extended to a maturity date not earlier than the Extended Maturity "
        "Date.",
        "Reaffirmation. Borrower and each Guarantor shall have executed and delivered such reaffirmations, certificates and "
        "opinions as Lender may reasonably request, and each representation and warranty in Article VI shall be true and correct "
        "in all material respects as of the date of the extension.",
    ]
    for i, e in enumerate(ext, 1):
        numbered(doc, "(i)" if i == 1 else "(%s)" % "ii iii iv v vi vii viii ix".split()[i-2], e)
    para(doc, "[Drafting Note: Section 3.2 of the Term Sheet states only that the Extension Option is \u201csubject to "
              "satisfaction of customary conditions to be determined and set forth in the definitive Loan Agreement.\u201d The "
              "conditions above are drawn from Section 11 of the Credit Memorandum. Note that the Credit Memorandum's 1.15x "
              "extension test uses annualized three-month in-place NOI, which is inconsistent with the 1.25x trailing-twelve-month "
              "test in Section 6.3 of the Term Sheet; see Cover Memorandum Issue No. 14.]")

    sec_h(doc, "Section 2.15  Late Charges")
    para(doc, "If any amount payable under the Loan Documents (other than an amount payable on the Mini-Perm Maturity Date or "
              "upon acceleration) is not paid within five (5) days after its due date, Borrower shall pay Lender a late charge "
              "equal to five percent (5.00%) of the overdue amount, which late charge shall be in addition to interest at the "
              "Default Rate and shall be secured by the Loan Documents.")

    sec_h(doc, "Section 2.16  Maximum Rate; Usury Savings")
    para(doc, "Nothing in the Loan Documents shall require Borrower to pay, or permit Lender to collect, interest or other "
              "charges in excess of the Maximum Rate. If any amount in excess of the Maximum Rate would otherwise be payable, "
              "(a) such excess shall be applied to reduce the principal balance of the Loan, and (b) if the principal balance has "
              "been paid in full, such excess shall be refunded to Borrower. To the extent permitted by applicable law, all "
              "amounts paid or agreed to be paid to Lender for the use, forbearance or detention of money shall, to the maximum "
              "extent permitted, be amortized, prorated, allocated and spread over the full period of the Loan. [Drafting Note: "
              "Counsel should confirm at signing that the Default Rate (the applicable contract rate plus 5.00%) and the late "
              "charge are within the maximum lawful rate for a commercial loan of this size under N.C.G.S. \u00a7 24-1.1 and the "
              "exemptions in N.C.G.S. \u00a7 24-8.]")

    sec_h(doc, "Section 2.17  Conditions to Lender's Obligations Absolute")
    para(doc, "Borrower's obligation to repay the Loan and to perform its obligations under the Loan Documents is absolute and "
              "unconditional and is not subject to any right of setoff, counterclaim, recoupment, defense or abatement. No "
              "failure of the Project to be completed, no dispute with any contractor, architect, consultant or tenant, no "
              "failure of any condition to an Advance to be satisfied and no other event shall affect Borrower's obligations, "
              "except to the extent expressly provided in this Agreement.")
