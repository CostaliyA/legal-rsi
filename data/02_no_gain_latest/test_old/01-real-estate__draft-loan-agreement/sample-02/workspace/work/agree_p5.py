# -*- coding: utf-8 -*-
import sys; sys.path.insert(0,'/workspace/work')
from dh import *
from docx.enum.text import WD_ALIGN_PARAGRAPH as AL

def build_part5(doc):
    # ---------------- ARTICLE VII ----------------
    art(doc, "ARTICLE VII — AFFIRMATIVE COVENANTS")
    para(doc, "From the Closing Date until the Loan and all other amounts payable under the Loan Documents have been paid in "
              "full and the Loan Documents have been terminated, Borrower shall, and shall cause each Guarantor to (as to "
              "matters applicable to such Guarantor), do each of the following:")

    covs = [
        ("Section 7.1  Completion of the Project",
         "Cause the Project to be constructed and completed in a good and workmanlike manner, lien-free, in accordance with the "
         "Approved Plans and Specifications, the Approved Project Budget and the Construction Contract, and cause Substantial "
         "Completion to be achieved on or before the Construction Maturity Date. Borrower acknowledges that Projected Substantial "
         "Completion under the Construction Contract is August 31, 2027, which is three (3) days after the Construction Maturity "
         "Date, and that Borrower bears the risk of that gap."),
        ("Section 7.2  Inspections and Progress Reports",
         "Deliver to Lender, within fifteen (15) days after the end of each calendar month during the Construction Period, a "
         "construction progress report (on AIA Form G702/G703 or in such other form as Lender may approve) certified by Borrower, "
         "the general contractor and the Architect, together with the Construction Inspector's certification, an updated "
         "construction schedule, a change order log and a budget reconciliation. Permit Lender and the Construction Inspector to "
         "inspect the Property at any time during normal business hours upon reasonable prior notice."),
        ("Section 7.3  Financial Reporting",
         "Deliver to Lender: (a) quarterly unaudited financial statements of Borrower within forty-five (45) days after the end of "
         "each fiscal quarter; (b) annual audited financial statements of Borrower, prepared by a nationally or regionally "
         "recognized independent certified public accounting firm, within one hundred twenty (120) days after the end of each "
         "fiscal year; (c) annual personal financial statements of each Guarantor, with supporting asset schedules, within one "
         "hundred twenty (120) days after the end of each calendar year; (d) quarterly certifications of guarantor liquidity "
         "within forty-five (45) days after the end of each fiscal quarter; (e) annual net worth certifications of Borrower within "
         "one hundred twenty (120) days after the end of each fiscal year; (f) annual rent rolls and operating statements during "
         "the Mini-Perm Period within thirty (30) days after the end of each calendar quarter; (g) copies of the annual federal "
         "income tax returns of Borrower and each Guarantor within thirty (30) days after filing; and (h) such other financial "
         "information as Lender may reasonably request."),
        ("Section 7.4  Compliance Certificates",
         "Deliver to Lender, concurrently with the financial statements required by Section 7.3 and at each Draw Request, a "
         "compliance certificate substantially in the form of Exhibit C, executed by the Managing Member of Borrower, certifying "
         "compliance with each financial covenant in Article IX (with supporting calculations) and stating that no Default or "
         "Event of Default exists or, if one exists, describing it in reasonable detail."),
        ("Section 7.5  Insurance",
         "Maintain at all times the insurance required by Schedule 5 and by Article XVI, with insurers, deductibles, limits and "
         "endorsements acceptable to Lender, naming Lender as mortgagee, loss payee and additional insured as its interests "
         "appear, and deliver evidence of renewal not less than fifteen (15) days before each policy expiration."),
        ("Section 7.6  Taxes and Charges",
         "Pay and discharge, before delinquency, all taxes, assessments, water charges, sewer rents and other governmental "
         "charges imposed on the Property, the Project or Borrower, and deliver evidence of payment upon request. Borrower may "
         "contest in good faith, by appropriate proceedings promptly instituted and diligently conducted, any such item, provided "
         "that it has established reserves satisfactory to Lender and that no lien attaches to the Property."),
        ("Section 7.7  Compliance with Laws",
         "Comply in all material respects with all applicable laws, ordinances, rules, regulations and orders, including building "
         "and life-safety codes, accessibility requirements, the Durham Unified Development Ordinance, the Declaration of "
         "Covenants, Conditions and Restrictions applicable to the Property, and all Environmental Laws."),
        ("Section 7.8  Environmental Compliance and NFA Conditions",
         "Comply, and cause the general contractor and each subcontractor to comply, with each condition of the NFA Letter and "
         "with the Soil Management Plan, including (a) the installation, operation, maintenance, testing and, if required, "
         "conversion of the Vapor Mitigation System; (b) the submission to NCDEQ of the as-built drawings and the system "
         "performance verification report within ninety (90) days after completion of the building foundation in the Affected "
         "Area; (c) the maintenance of the recorded deed notice and land use restriction; (d) the implementation of the Soil "
         "Management Plan for all subsurface disturbance in the Affected Area; and (e) the preservation of all records relating "
         "to the foregoing for not less than ten (10) years, and provide Lender with copies of all correspondence with NCDEQ "
         "within five (5) Business Days after sending or receipt."),
        ("Section 7.9  Permits and Approvals",
         "Maintain in full force and effect all permits, licenses, consents and approvals necessary for the construction and "
         "operation of the Project, and deliver copies to Lender upon request. Borrower shall promptly notify Lender of any "
         "suspension, revocation, expiration or threatened revocation of any such permit."),
        ("Section 7.10  Books and Records; Access",
         "Maintain complete and accurate books and records in accordance with GAAP, and permit Lender and its representatives to "
         "examine and audit such books and records and to discuss Borrower's affairs with its officers, managers, accountants and "
         "consultants at reasonable times upon reasonable prior notice."),
        ("Section 7.11  Single-Purpose Entity",
         "Maintain its status as a single-purpose entity in compliance with the SPE Covenants set forth in Article XV."),
        ("Section 7.12  Guarantor Obligations",
         "Cause each Guarantor to maintain the minimum combined liquidity required by Section 9.5, to deliver the financial "
         "information required by Section 7.3, to preserve and not to transfer any material portion of such Guarantor's assets "
         "outside the ordinary course of business, and not to revoke, terminate, disaffirm or attempt to limit the enforceability "
         "of any Guaranty."),
        ("Section 7.13  Notices of Material Events",
         "Notify Lender in writing within five (5) Business Days after Borrower or any Guarantor obtains knowledge of (a) any "
         "Default or Event of Default; (b) any litigation, arbitration or governmental proceeding commenced or threatened against "
         "Borrower, any Guarantor or the Property involving a claim in excess of $100,000; (c) any material adverse change in the "
         "financial condition of Borrower or any Guarantor; (d) any casualty, condemnation or taking affecting the Property; (e) "
         "any environmental claim, notice of violation, information request, notice of potential responsibility, spill, release or "
         "agency inspection relating to the Property; (f) any default or event of default under the Mezzanine Documents or the "
         "Intercreditor Agreement; (g) any notice from the Brightleaf Historic District Association alleging a violation of the "
         "Declaration; and (h) any change in the identity of the members of Borrower or of the independent manager."),
        ("Section 7.14  Further Assurances",
         "Execute, acknowledge and deliver such further instruments and take such further action as Lender may reasonably request "
         "to carry out the purposes of the Loan Documents, to perfect or maintain the priority of Lender's security interests, or "
         "to comply with applicable law, including any request arising from Lender's participation or securitization of the Loan "
         "that does not materially increase Borrower's obligations or costs."),
        ("Section 7.15  Lender's Expenses",
         "Reimburse Lender on demand for all costs and expenses incurred in connection with the administration, servicing, "
         "enforcement and protection of the Loan, including the fees of the Construction Inspector, appraisal and reappraisal "
         "costs, environmental consultants, title endorsements, UCC and lien searches, and the fees and disbursements of Lender's "
         "counsel, in each case in accordance with Section 18.2."),
        ("Section 7.16  Leasing During the Mini-Perm Period",
         "Upon commencement of the Mini-Perm Period, (a) lease the residential units and retail space in the ordinary course on "
         "arm's-length terms and in accordance with Section 17.1; (b) deliver to Lender, within fifteen (15) days after the end of "
         "each month, a rent roll and a leasing status report; and (c) apply all rents and other income from the Property as "
         "required by the Assignment of Leases and Rents."),
        ("Section 7.17  Annual Budgets",
         "Deliver to Lender, not less than thirty (30) days prior to the beginning of each fiscal year during the Mini-Perm "
         "Period, an annual operating budget for the Property, and not less than thirty (30) days prior to the commencement of "
         "each calendar year during the Construction Period, an updated construction budget and schedule."),
    ]
    for h, t in covs:
        sec_h(doc, h)
        para(doc, t)

    # ---------------- ARTICLE VIII ----------------
    art(doc, "ARTICLE VIII — NEGATIVE COVENANTS")
    para(doc, "From the Closing Date until the Loan and all other amounts payable under the Loan Documents have been paid in "
              "full, Borrower shall not, and shall not permit any Guarantor to, without Lender's prior written consent (which "
              "consent may be withheld in Lender's sole and absolute discretion):")

    negs = [
        ("Section 8.1  Indebtedness",
         "Incur, assume, guarantee or permit to exist any Indebtedness other than (a) the Loan, (b) the Mezzanine Loan as "
         "permitted by the Intercreditor Agreement, and (c) trade payables and accrued expenses incurred in the ordinary course "
         "of business and not more than ninety (90) days past due."),
        ("Section 8.2  Liens",
         "Create, incur, assume or permit to exist any lien, mortgage, deed of trust, pledge, security interest, encumbrance, "
         "judgment lien, mechanics' or materialmen's lien, or other charge on the Property, the Collateral or any membership "
         "interest in Borrower, other than the Permitted Exceptions, the liens in favor of Lender, and the subordinated pledge in "
         "favor of Mezzanine Lender expressly permitted by the Intercreditor Agreement."),
        ("Section 8.3  Transfers",
         "Sell, transfer, convey, assign, option, ground lease, contribute or otherwise dispose of the Property or any portion "
         "thereof or any interest therein, whether directly or indirectly, or enter into any agreement to do any of the foregoing."),
        ("Section 8.4  Ownership Changes",
         "Cause or permit any change in the ownership structure of Borrower or in the membership interests of Borrower, including "
         "any sale, assignment, transfer, pledge, hypothecation, encumbrance, dilution, redemption or issuance of any membership "
         "interest, other than the Membership Interest Pledges to Lender and the subordinated pledge to Mezzanine Lender permitted "
         "by the Intercreditor Agreement. Any change in the identity of the managing member, any admission of a new member, or any "
         "change of control of Brightleaf Investors Group LLC or of Mezzanine Lender shall require Lender's prior written consent."),
        ("Section 8.5  Organizational Documents",
         "Amend, restate, modify or waive any provision of Borrower's articles of organization or operating agreement in any "
         "manner that affects management, capital contributions, distributions, transfer restrictions or the SPE Covenants, or "
         "that could reasonably be expected to have a Material Adverse Effect."),
        ("Section 8.6  Affiliate Transactions",
         "Enter into, amend or permit to exist any transaction, contract or arrangement with any member, manager, Affiliate of "
         "Borrower, Mezzanine Lender or Thomas R. Chen, except on arm's-length terms and for fair and reasonable consideration "
         "and with prior written notice to Lender. Borrower shall not pay any management, oversight, monitoring, guarantee, "
         "development, construction management or similar fee to any Affiliate other than the Developer Fee in accordance with "
         "Section 8.7."),
        ("Section 8.7  Distributions and Developer Fee",
         "Declare or make any dividend, distribution, return of capital, redemption, loan or advance to any member, or pay any "
         "portion of the Developer Fee, (a) during the Construction Period; (b) while any Default or Event of Default exists; (c) "
         "while the Interest Reserve is less than the amount required by Section 5.4; or (d) unless Substantial Completion has been "
         "achieved and the Debt Service Coverage Ratio is not less than 1.25x. Amounts deposited as the Equity Contribution may "
         "not be returned to any member before the Loan is repaid in full. The Loan-funded portion of the Developer Fee "
         "($1,835,000) shall be disbursed only as provided in the Draw Schedule and only if no Default or Event of Default exists."),
        ("Section 8.8  Construction Documents",
         "Amend, modify, supplement, terminate or waive any provision of the Construction Contract, the architect's agreement or "
         "the Approved Plans and Specifications, or approve any change order, except in accordance with Section 4.5."),
        ("Section 8.9  Change of Business, Name or Location",
         "Change its name, its jurisdiction of organization, its organizational identification number, its principal place of "
         "business or its state of organization, or engage in any business other than the ownership, development, construction, "
         "leasing, management and operation of the Project."),
        ("Section 8.10  Fiscal Year",
         "Change its fiscal year, which is the calendar year as of the Closing Date."),
        ("Section 8.11  Subsidiaries; Joint Ventures",
         "Create or acquire any subsidiary, or enter into any partnership, joint venture or similar arrangement with respect to "
         "the Property or the Project."),
        ("Section 8.12  Environmental",
         "Cause or permit any release, discharge, disposal, storage or threatened release of Hazardous Materials at, on, under or "
         "from the Property; conduct any excavation, grading or other subsurface disturbance in the Affected Area other than in "
         "compliance with the Soil Management Plan; use any portion of the Affected Area for residential purposes unless and until "
         "NCDEQ has modified the NFA Letter to permit such use and Lender has consented in writing; or take any action that would "
         "cause the NFA Letter to be revoked, modified adversely, reopened or rendered inapplicable."),
        ("Section 8.13  Mezzanine Loan Modifications and Prepayments",
         "Amend, modify, waive or supplement any Mezzanine Document; increase the principal amount of, or the rate of interest on, "
         "the Mezzanine Loan; prepay, defease or repay the Mezzanine Loan other than in accordance with the Intercreditor "
         "Agreement; or make any payment in respect of the Mezzanine Loan while a Default or Event of Default exists."),
        ("Section 8.14  Use of Proceeds",
         "Use any proceeds of the Loan for any purpose other than as provided in Section 2.2."),
        ("Section 8.15  Zoning and Easements",
         "Seek or consent to any rezoning, variance, special use permit, amendment of the Durham Unified Development Ordinance as "
         "applicable to the Property, or modification, relocation or release of any recorded easement, without Lender's prior "
         "written consent."),
        ("Section 8.16  Related Party Leasing",
         "Lease any portion of the Property to any member, manager, Affiliate or immediate family member of any of them, except "
         "on arm's-length terms approved in writing by Lender."),
    ]
    for h, t in negs:
        sec_h(doc, h)
        para(doc, t)

    # ---------------- ARTICLE IX ----------------
    art(doc, "ARTICLE IX — FINANCIAL COVENANTS")
    sec_h(doc, "Section 9.1  Loan-to-Cost Ratio")
    numbered(doc, "(a)", "Borrower shall not permit the Loan-to-Cost Ratio to exceed eighty percent (80%) at any time during the "
             "term of the Loan. The \u201cLoan-to-Cost Ratio\u201d means the outstanding principal balance of the Loan divided by "
             "Total Project Costs.")
    numbered(doc, "(b)", "Total Project Costs means the aggregate of all costs and expenses incurred or to be incurred in "
             "connection with the acquisition, development, construction and completion of the Project, as set forth in the "
             "Approved Project Budget as the same may be revised with Lender's consent, including the land acquisition cost of "
             "$8,200,000, the GMP of $34,750,000, soft costs of $4,150,000, the Interest Reserve of $4,850,000, the Origination "
             "Fee of $475,000, the Developer Fee of $2,835,000 and the Contingency of $1,440,000.")
    numbered(doc, "(c)", "Total Project Costs shall also include, without duplication, (i) all demolition, abatement, "
             "investigation, remediation and regulatory compliance costs incurred with respect to the Property prior to Closing, "
             "including the approximately $680,000 of demolition and remediation costs described in the appraisal and the Phase I "
             "ESA; (ii) all amounts paid or payable to satisfy and release any prior lien on the Property; (iii) all interest "
             "accrued and capitalized on the Loan and the Mezzanine Loan; (iv) all costs of the Vapor Mitigation System, the Soil "
             "Management Plan and any environmental monitoring or reporting required by the NFA Letter; and (v) all "
             "documentary excise taxes, title premiums and recording costs paid in connection with the Loan.")
    numbered(doc, "(d)", "As of the Closing Date, on the basis of the Approved Project Budget of $56,700,000 and the Loan Amount, "
             "the Loan-to-Cost Ratio is 83.77%, which exceeds the maximum permitted ratio by 3.77 percentage points, or "
             "$2,140,000 (the amount by which the Loan Amount exceeds 80% of Total Project Costs, being $45,360,000). The parties "
             "acknowledge that compliance with this Section 9.1 on and after the Closing Date depends on the accuracy of Total "
             "Project Costs as restated pursuant to Section 3.7 and on the funding of the Equity Contribution, and that a "
             "recomputation of Total Project Costs to include the items described in Section 9.1(c) must be delivered at Closing.")
    para(doc, "[Drafting Note: On a corrected budget of $60,780,000 (which includes the payoff of the Triangle Commercial Bank "
              "deed of trust and the pre-closing site costs), the Loan-to-Cost Ratio would be 78.15% and would comply with this "
              "Section without reducing the Loan Amount, provided the Equity Contribution is increased to approximately "
              "$4,080,000. Conversely, if the payoff and site costs are not added to Total Project Costs, the Loan-to-Cost Ratio "
              "is 83.77% and this covenant is breached at Closing. The two positions cannot both be right. See Cover Memorandum "
              "Issue No. 4.]")

    sec_h(doc, "Section 9.2  Loan-to-Value Ratios")
    numbered(doc, "(a)", "Borrower shall not permit the Loan-to-Value Ratio on an as-completed basis to exceed sixty-five percent "
             "(65%), determined by dividing the outstanding principal balance of the Loan by the as-completed appraised value of "
             "the Property, which as of the Closing Date is $72,800,000.")
    numbered(doc, "(b)", "Borrower shall not permit the Loan-to-Value Ratio on an as-stabilized basis to exceed sixty-five percent "
             "(65%), determined by dividing the outstanding principal balance of the Loan by the as-stabilized appraised value, "
             "which as of the Closing Date is $76,200,000.")
    numbered(doc, "(c)", "Lender may obtain, at Borrower's expense, a reappraisal of the Property at any time after the occurrence "
             "of a Default or Event of Default, at the commencement of the Mini-Perm Period, in connection with any extension of "
             "the Loan, and otherwise not more than once in any twelve (12) month period, and each such appraisal shall be used "
             "for purposes of this Section.")
    numbered(doc, "(d)", "Borrower acknowledges that, as of the Closing Date, the Loan-to-Value Ratio on an as-completed basis is "
             "65.25% ($47,500,000 \u00f7 $72,800,000), which exceeds the sixty-five percent (65%) maximum by 0.25 percentage "
             "points, equivalent to $180,000 of principal (65% of $72,800,000 being $47,320,000). Borrower shall cure such "
             "exceedance at Closing either by reducing the Loan Amount to $47,320,000, by depositing additional equity in an "
             "amount sufficient to cause the Loan-to-Value Ratio on an as-completed basis to be not greater than 64.75%, or by "
             "such other means as Lender may approve in writing.")
    para(doc, "[Drafting Note: Sections 4 and 6.2 of the Term Sheet impose a 65% as-completed maximum, yet the Loan Amount of "
              "$47,500,000 against the $72,800,000 as-completed value yields 65.25%. Section 6.1 of the Credit Memorandum instead "
              "applies a 70% policy maximum and reports the ratio as a \u201cPass.\u201d The covenant above states the Term Sheet "
              "test and the resulting cure requirement. See Cover Memorandum Issue No. 13.]")

    sec_h(doc, "Section 9.3  Debt Service Coverage Ratio")
    numbered(doc, "(a)", "Borrower shall maintain a Debt Service Coverage Ratio of not less than 1.25x, tested (i) as of the "
             "commencement of the Mini-Perm Period, (ii) as of the end of each fiscal quarter thereafter, on a trailing twelve "
             "(12) month basis, and (iii) at any other time when required by Lender in connection with an extension or "
             "reappraisal. \u201cDebt Service Coverage Ratio\u201d means the net operating income of the Property for the "
             "applicable period, annualized, divided by annual debt service on the outstanding principal balance of the Loan at "
             "the then-current Interest Rate.")
    numbered(doc, "(b)", "If the Debt Service Coverage Ratio is less than 1.25x at any testing date, Borrower shall, at Lender's "
             "election, either (i) prepay the principal of the Loan in an amount sufficient to restore the Debt Service Coverage "
             "Ratio to not less than 1.25x, or (ii) deposit cash collateral with Lender in an amount determined by Lender to be "
             "sufficient to restore the Debt Service Coverage Ratio to not less than 1.25x, in either case within thirty (30) days "
             "after Lender's written demand and without any obligation of Lender to make further Advances during such period.")
    numbered(doc, "(c)", "Interest-only coverage. Borrower acknowledges that the Debt Service Coverage Ratio is calculated on an "
             "interest-only basis, does not include debt service on the Mezzanine Loan, and does not assume any amortization. "
             "Borrower further acknowledges that (i) including the Mezzanine Loan, combined debt service at the mini-perm rate of "
             "7.85% on the Loan and the fixed rate of 12.50% on the Mezzanine Loan would total approximately $4,878,750 per "
             "annum against stabilized net operating income of $4,876,800, for combined coverage of approximately 1.00x, and (ii) "
             "a 200 basis point increase in Daily Simple SOFR would reduce the Loan's coverage to approximately 1.04x. The 1.25x "
             "covenant therefore does not evidence the Project's ability to service its aggregate debt, and repayment of the Loan "
             "is expected to depend on refinancing or sale.")
    para(doc, "[Drafting Note: A test of trailing twelve month actual net operating income as of the commencement of the "
              "Mini-Perm Period is likely to fail mechanically, because Substantial Completion is projected for August 31, 2027, "
              "three days after the Construction Maturity Date. The covenant should be conformed to a trailing three-month "
              "annualized or forward-looking test at that first testing date. See Cover Memorandum Issue No. 14.]")

    sec_h(doc, "Section 9.4  Borrower Net Worth")
    numbered(doc, "(a)", "Borrower shall maintain a Net Worth of not less than $12,000,000, tested annually within one hundred "
             "twenty (120) days after the end of each fiscal year and at Closing.")
    numbered(doc, "(b)", "If Borrower's Net Worth is less than the required amount at any testing date, Borrower shall, within "
             "thirty (30) days after Lender's written demand, make an additional capital contribution in the amount of the "
             "deficiency, which amount shall not be returned to any member while the Loan remains outstanding.")
    numbered(doc, "(c)", "\u201cNet Worth\u201d means, as of any date, the excess of Borrower's total assets over its total "
             "liabilities determined in accordance with GAAP, excluding (i) any asset consisting of capitalized interest or "
             "capitalized fees, (ii) any receivable from any member or Affiliate, and (iii) any unrealized appreciation or "
             "revaluation of the Property. For the avoidance of doubt, Net Worth shall not include the amount of the Interest "
             "Reserve, the Contingency or any undisbursed Loan proceeds as an asset if the corresponding amount is also included "
             "as a liability.")
    para(doc, "[Drafting Note: The $12,000,000 minimum net worth covenant was set against an asserted Borrower net worth of "
              "$14,200,000. If the Project is funded 100% with debt (Loan of $47,500,000 plus Mezzanine Loan of $9,200,000 against "
              "Total Project Costs of $56,700,000) and the land carries the $3,400,000 Triangle deed of trust until Closing, a "
              "GAAP balance sheet for a single-purpose entity owning only the Property will show net worth of approximately "
              "$4,800,000 to $5,500,000, not $14,200,000. The definition in Section 9.4(c) and the Closing test in Section "
              "9.4(a) will require the parties to confront this discrepancy. See Cover Memorandum Issue No. 15.]")

    sec_h(doc, "Section 9.5  Guarantor Liquidity")
    para(doc, "The Guarantors shall maintain combined Liquidity of not less than $5,000,000, tested quarterly, with a compliance "
              "certificate delivered within forty-five (45) days after the end of each fiscal quarter. \u201cLiquidity\u201d means "
              "cash, cash equivalents and marketable securities that are readily convertible to cash within thirty (30) days, "
              "determined without duplication and net of any margin debt, pledged balances or other encumbrance. As of the "
              "Closing Date, the Guarantors' combined Liquidity is represented to be approximately $9,300,000, consisting of "
              "approximately $6,100,000 attributable to Ms. Vasquez-Torres and approximately $3,200,000 attributable to Mr. Osei. "
              "If combined Liquidity falls below the required amount, the Guarantors shall restore compliance within thirty (30) "
              "days after Lender's written demand.")

    sec_h(doc, "Section 9.6  Testing; Certificates; Modification of Covenants")
    para(doc, "Each financial covenant in this Article shall be tested as set forth in the applicable Section and shall be "
              "evidenced by a compliance certificate substantially in the form of Exhibit C, with supporting calculations and "
              "such backup documentation as Lender may reasonably request. If Lender determines that a covenant has not been "
              "satisfied, Lender shall notify Borrower in writing and Borrower shall have thirty (30) days to cure, except that "
              "the cure rights in Section 9.2(d), Section 9.3(b) and Section 9.4(b) shall govern where applicable. Failure to "
              "cure within the applicable period shall constitute an Event of Default under Section 13.3, without regard to any "
              "additional cure period in that Section.")
