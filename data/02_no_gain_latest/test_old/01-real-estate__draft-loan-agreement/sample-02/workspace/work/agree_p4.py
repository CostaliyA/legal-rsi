# -*- coding: utf-8 -*-
import sys; sys.path.insert(0,'/workspace/work')
from dh import *
from docx.enum.text import WD_ALIGN_PARAGRAPH as AL

def build_part4(doc):
    art(doc, "ARTICLE V — INTEREST RESERVE")
    sec_h(doc, "Section 5.1  Funding of the Interest Reserve")
    para(doc, "At Closing, Lender shall fund the Interest Reserve in the amount of $4,850,000 from the proceeds of the Initial "
              "Advance and shall deposit the same in the Interest Reserve Account. The Interest Reserve shall not constitute a "
              "trust fund, shall not bear interest to the benefit of Borrower (except that Lender may, in its discretion, credit "
              "interest actually earned on the Interest Reserve Account against interest payable on the Loan), and shall secure "
              "the Loan on a parity with all other obligations under the Loan Documents.")

    sec_h(doc, "Section 5.2  Application of the Interest Reserve")
    para(doc, "Amounts in the Interest Reserve Account shall be applied solely to the payment of interest accruing on the "
              "outstanding principal balance of the Loan during the Construction Period, on each interest payment date, until the "
              "Interest Reserve is exhausted. No amount in the Interest Reserve Account may be applied to principal, fees, costs, "
              "construction costs or any other purpose.")

    sec_h(doc, "Section 5.3  Replenishment Obligation")
    para(doc, "If at any time Lender determines that the balance of the Interest Reserve Account is or will be insufficient to "
              "pay interest on the Loan through the Construction Maturity Date, Lender shall notify Borrower in writing, and "
              "Borrower shall deposit additional funds into the Interest Reserve Account, from sources other than the Loan, the "
              "Mezzanine Loan or any other Indebtedness, within five (5) Business Days after such notice, in the amount specified "
              "by Lender. Borrower's obligation to fund any deficiency in the Interest Reserve is absolute, is in addition to "
              "the Carry Guaranty, and shall not be limited by the amount of any advance of the Loan then remaining undisbursed.")

    sec_h(doc, "Section 5.4  Interest Reserve Adequacy Testing")
    para(doc, "At each Draw Request and in any event not less than quarterly, Borrower shall deliver to Lender a certification, "
              "in form satisfactory to Lender, demonstrating that the balance of the Interest Reserve Account, together with any "
              "additional amounts Borrower has committed to deposit, is sufficient to pay projected interest on the Loan through "
              "the earlier of (a) the next anticipated Advance date or (b) the date that is ninety (90) days after the date of "
              "the certification, in each case calculated at the then-current Daily Simple SOFR and the then-projected "
              "outstanding principal balance of the Loan. If the certification is not delivered or the test is not satisfied, "
              "Borrower shall deposit the deficiency into the Interest Reserve Account before any further Advance will be made.")

    sec_h(doc, "Section 5.5  Monthly Reconciliation and Reporting")
    para(doc, "Borrower shall deliver to Lender, within fifteen (15) days after the end of each calendar month during the "
              "Construction Period, a reconciliation of the Interest Reserve Account showing the opening balance, interest "
              "accrued and paid, any deposits, the closing balance, and projected interest through the Construction Maturity Date "
              "at both the then-current rate and at a rate 100 basis points higher.")

    sec_h(doc, "Section 5.6  Interest Reserve Analysis; Acknowledgement")
    para(doc, "Borrower acknowledges that (a) the Interest Reserve was sized by Borrower using an assumed Daily Simple SOFR of "
              "3.50% per annum, which was approximately 85 basis points below the rate prevailing when the Credit Memorandum was "
              "prepared; (b) on the Draw Schedule, the Interest Reserve is sufficient to pay projected interest through the "
              "Construction Maturity Date only if Daily Simple SOFR averages approximately 3.82% per annum or less; and (c) at "
              "the Daily Simple SOFR of 4.35% assumed in the Credit Memorandum, the Interest Reserve would be exhausted before the "
              "Construction Maturity Date by approximately $360,000 to $565,000, depending on the method used, and the shortfall "
              "would exceed $1,000,000 at a Daily Simple SOFR of 5.35%. Borrower accordingly acknowledges that the replenishment "
              "obligation in Section 5.3 is a material inducement to Lender and is likely to be called upon. Borrower further "
              "acknowledges that Lender makes no representation that the Interest Reserve is adequate.")
    para(doc, "[Drafting Note: Borrower's interest reserve model (draw schedule tab, dated January 8, 2025) concludes "
              "\u201cAPPEARS ADEQUATE\u201d with a $221,325 surplus at 3.50% SOFR, while the Credit Memorandum concludes the reserve "
              "is $565,000 short at 4.35% SOFR, and Borrower's own sensitivity table shows a $365,830 shortfall at 4.35%. The "
              "three conclusions cannot be reconciled; the arithmetic above reflects an independent recomputation of Borrower's "
              "model. See Cover Memorandum Issue No. 13.]")

    # ---------------- ARTICLE VI ----------------
    art(doc, "ARTICLE VI — REPRESENTATIONS AND WARRANTIES")
    para(doc, "Borrower and each Guarantor (as to itself and, where applicable, as to Borrower) represent and warrant to Lender "
              "as of the Closing Date and as of the date of each Advance that:")

    reps = [
        ("Section 6.1  Organization; Power; Authorization",
         "Borrower is a limited liability company duly organized, validly existing and in good standing under the laws of the "
         "State of North Carolina, has all requisite power and authority to own the Property, to carry on its business as now "
         "conducted and as proposed to be conducted, and to execute, deliver and perform the Loan Documents. The execution, "
         "delivery and performance of the Loan Documents have been duly authorized by all necessary action of Borrower, its "
         "members and its managing member, including the consents required by Sections 3.2 and 9.1 of its operating agreement."),
        ("Section 6.2  Enforceability; No Conflicts",
         "The Loan Documents constitute the legal, valid and binding obligations of Borrower and each Guarantor, enforceable in "
         "accordance with their terms, subject to applicable bankruptcy, insolvency, reorganization, moratorium and similar laws "
         "and to general principles of equity. The execution and performance of the Loan Documents do not violate Borrower's "
         "articles of organization or operating agreement, any applicable law, or any material agreement, order or judgment "
         "binding on Borrower or any Guarantor, and do not result in the creation of any lien on the Property other than in "
         "favor of Lender."),
        ("Section 6.3  Title to the Property",
         "Borrower holds good, marketable and insurable fee simple title to the Property, free and clear of all liens, "
         "encumbrances and exceptions other than the Permitted Exceptions and the deed of trust to be released at Closing "
         "pursuant to Section 3.14. Borrower has not granted any option, right of first refusal or right of first offer with "
         "respect to the Property, and no person other than Borrower has any ownership, leasehold or occupancy interest in the "
         "Property."),
        ("Section 6.4  Litigation",
         "There is no action, suit, proceeding, investigation, arbitration or governmental inquiry pending or, to the knowledge "
         "of Borrower or any Guarantor, threatened against Borrower, any Guarantor, any member of Borrower or the Property that "
         "(a) could reasonably be expected to have a Material Adverse Effect, (b) questions the validity of any Loan Document, or "
         "(c) relates to any environmental condition at the Property. There are no unsatisfied judgments against Borrower or any "
         "Guarantor."),
        ("Section 6.5  Compliance with Laws; Zoning",
         "The Property and the Project comply, and will comply, in all material respects with all applicable laws, ordinances, "
         "rules, regulations and orders, including the Durham Unified Development Ordinance, building, fire, accessibility and "
         "life-safety codes, and all Environmental Laws. The Project is permitted as of right in the MU-D zoning district without "
         "variance, special use permit, conditional zoning or other discretionary approval. All governmental approvals required "
         "for the construction of the Project have been obtained or will be obtained before the applicable stage of construction."),
        ("Section 6.6  Financial Statements",
         "The financial statements and other financial information of Borrower and each Guarantor delivered to Lender are true, "
         "complete and correct in all material respects and fairly present the financial condition of Borrower and such Guarantor "
         "as of the dates and for the periods indicated. Borrower's net worth is not less than $14,200,000 as of the date of its "
         "most recent financial statements, and the combined liquid assets of the Guarantors are not less than $9,300,000 as of "
         "the dates of their respective personal financial statements. Neither Borrower nor any Guarantor has any material "
         "contingent liability not disclosed in such statements."),
        ("Section 6.7  No Default",
         "No Default or Event of Default exists, and no event has occurred that with the giving of notice or the passage of time, "
         "or both, would constitute a Default or Event of Default under any Loan Document, the Mezzanine Documents or any other "
         "material agreement to which Borrower or any Guarantor is a party."),
        ("Section 6.8  Permits and Approvals",
         "Borrower has obtained all permits, licenses, consents and approvals necessary to commence construction of the Project, "
         "and each such permit is in full force and effect. Borrower has not received any notice of any violation, stop-work order "
         "or revocation with respect to any such permit."),
        ("Section 6.9  Single-Purpose Entity",
         "Borrower is, and since its formation has been, a single-purpose entity that (a) owns no assets other than the Property "
         "and related Project assets, (b) has incurred no liabilities other than the Loan, the Mezzanine Loan and trade payables "
         "in the ordinary course, and (c) has conducted no business other than the acquisition, development, construction and "
         "ownership of the Project. Borrower has not commingled its funds with those of any member or Affiliate and has observed "
         "all limited liability company formalities."),
        ("Section 6.10  Environmental Matters",
         "Except as disclosed in the Phase I ESA, the Phase II ESA and the NFA Letter, and to Borrower's knowledge: (a) no "
         "Hazardous Materials are present at, on, under or migrating from the Property in violation of any Environmental Law or in "
         "a condition that requires reporting, investigation, remediation or other response action; (b) the Property has not been "
         "used for the generation, treatment, storage, disposal or release of Hazardous Materials except in compliance with "
         "Environmental Laws; (c) there are no underground or aboveground storage tanks, sumps, dry wells, landfills or disposal "
         "areas at the Property other than the former tank identified in the Phase I ESA; (d) neither Borrower nor any Guarantor "
         "has received any notice of violation, information request, demand, claim, order or notice of potential responsibility "
         "under any Environmental Law relating to the Property; (e) the Property is not listed on any federal, state or local "
         "list of hazardous sites, other than the NCDEQ listings associated with Site ID IHSB-24-1203 and Incident No. "
         "NONUST-24-0847; and (f) there is no asbestos-containing material, lead-based paint, polychlorinated biphenyl or mold at "
         "the Property except as previously abated in accordance with the pre-demolition survey completed in July 2024."),
        ("Section 6.11  NFA Letter Compliance",
         "The NFA Letter is in full force and effect and has not been revoked, modified, conditioned further or appealed. Borrower "
         "has complied in all respects with each condition of the NFA Letter as and to the extent such condition is currently due "
         "and applicable, including the recording of the deed notice required by Condition 4 within the period specified in the "
         "NFA Letter. The Soil Management Plan and the design of the Vapor Mitigation System satisfy the requirements of the NFA "
         "Letter and have been incorporated into the Approved Plans and Specifications and into the Construction Contract. No "
         "portion of the building footprint that contains, or is designed or intended to contain, residential dwelling units "
         "overlaps the Affected Area in a manner inconsistent with the non-residential use restriction of Condition 2 of the NFA "
         "Letter, except as disclosed in the overlay plan delivered pursuant to Section 3.5 and approved in writing by Lender."),
        ("Section 6.12  Construction Documents",
         "The Construction Contract and the architect's agreement are in full force and effect, have not been modified except as "
         "disclosed to Lender in writing, and represent the entire agreement between Borrower and the contractor and the "
         "Architect with respect to the Project. The GMP of $34,750,000 covers the complete scope of work described in the "
         "Approved Plans and Specifications, and Borrower knows of no defect, omission or gap in the scope, the plans or the "
         "budget that would prevent completion of the Project for the Total Project Costs. No work has been performed at the "
         "Property except the demolition and remediation described in the Phase I ESA."),
        ("Section 6.13  Project Budget; Sources and Uses",
         "The Approved Project Budget and the sources and uses of funds delivered to Lender are true, complete and correct, "
         "include all costs of the Project, and reconcile to the dollar. No portion of the Equity Contribution has been or will be "
         "funded, directly or indirectly, with the proceeds of the Mezzanine Loan or any other Indebtedness or with funds provided "
         "by Mezzanine Lender, Brightleaf Investors Group LLC, Thomas R. Chen or any of their Affiliates."),
        ("Section 6.14  Insurance",
         "Borrower has obtained, and will maintain, the insurance required by Schedule 5, and each policy is in full force and "
         "effect with all premiums paid. Borrower has not received any notice of cancellation, non-renewal, denial of coverage or "
         "material increase in premium with respect to any such policy."),
        ("Section 6.15  Taxes",
         "All federal, state and local tax returns required to be filed by Borrower and each Guarantor have been filed, and all "
         "taxes shown thereon to be due have been paid. All real property taxes, assessments and governmental charges affecting "
         "the Property that are due and payable have been paid. Borrower has not received any notice of deficiency, lien or "
         "proposed assessment with respect to the Property."),
        ("Section 6.16  No Additional Indebtedness; Solvency",
         "Borrower has no Indebtedness other than the Loan and the Mezzanine Loan, and has no material liabilities other than "
         "those disclosed to Lender. Borrower and each Guarantor are solvent, are able to pay their debts as they become due, and "
         "have no intent to hinder, delay or defraud any creditor. Neither Borrower nor any Guarantor is contemplating any "
         "voluntary bankruptcy, insolvency or reorganization proceeding."),
        ("Section 6.17  Guaranties",
         "Each Guaranty has been duly authorized, executed and delivered by each Guarantor and constitutes the legal, valid and "
         "binding obligation of such Guarantor, enforceable in accordance with its terms, and is not subject to any condition, "
         "defense, setoff or counterclaim."),
        ("Section 6.18  Mezzanine Loan and Intercreditor Agreement",
         "The Mezzanine Documents have been delivered to Lender in complete form and, together with the Intercreditor Agreement, "
         "constitute the entire agreement between Borrower and Mezzanine Lender with respect to the Mezzanine Loan. The "
         "outstanding principal amount of the Mezzanine Loan does not exceed $9,200,000, no default exists thereunder and no "
         "interest, fee or other amount has been paid in cash in respect thereof except as disclosed to Lender in writing."),
        ("Section 6.19  Membership Interests",
         "Schedule 6.19 sets forth a complete and correct list of the members of Borrower and their respective membership "
         "interests, and there are no other equity interests, options, warrants, profits interests, phantom equity or rights to "
         "acquire any interest in Borrower. Borrower has no subsidiaries. The membership interests of Borrower are uncertificated "
         "or, to the extent certificated, have been delivered to Lender together with undated transfer powers."),
        ("Section 6.20  Anti-Terrorism; Anti-Money Laundering",
         "Neither Borrower, any Guarantor, any member of Borrower nor any Person holding a direct or indirect interest in Borrower "
         "is a person identified on the Specially Designated Nationals and Blocked Persons List maintained by the U.S. Department "
         "of the Treasury's Office of Foreign Assets Control, or is otherwise subject to any economic or trade sanction. Borrower "
         "has complied with all applicable anti-money laundering and know-your-customer requirements."),
        ("Section 6.21  Brokers",
         "No broker, finder, investment banker or similar intermediary is entitled to any commission or fee in connection with "
         "the Loan based on any arrangement made by or on behalf of Borrower or any Guarantor."),
    ]
    for h, t in reps:
        sec_h(doc, h)
        para(doc, t)
    para(doc, "The representations and warranties in this Article shall survive the Closing and the making of each Advance, and "
              "shall be deemed repeated and restated as of the date of each Advance and each extension of the Loan, except that "
              "representations as to financial statements shall be deemed to refer to the most recent financial statements "
              "delivered to Lender.", space_before=6)
