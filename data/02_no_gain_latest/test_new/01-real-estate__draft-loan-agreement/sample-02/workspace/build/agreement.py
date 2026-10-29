# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, "/workspace/build")
from docxhelp import *
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK

doc = new_doc(1.0)
header_footer(doc,
    "DRAFT 02/03/2025 — PRIVILEGED AND CONFIDENTIAL — ATTORNEY WORK PRODUCT",
    "The Piedmont at Brightleaf — CRE-2025-0342")

# ---------------------------------------------------------------- cover page
para(doc, "", space_after=0)
para(doc, "DRAFT — FOR DISCUSSION PURPOSES ONLY", size=10, bold=True, align="center",
     space_after=2, color=RGBColor(0x8B,0x1A,0x1A))
para(doc, "This draft has not been executed and does not constitute an offer, commitment or agreement. "
          "Bracketed items represent open matters identified in the accompanying memorandum of even date.",
     size=9, italic=True, align="center", space_after=40)

para(doc, "CONSTRUCTION-TO-MINI-PERMANENT", size=17, bold=True, align="center", space_after=0)
para(doc, "LOAN AGREEMENT", size=17, bold=True, align="center", space_after=18)
para(doc, "by and among", size=10.5, italic=True, align="center", space_after=14)
para(doc, "HARBORVIEW CAPITAL PARTNERS LLC,", size=12, bold=True, align="center", space_after=2)
para(doc, "a North Carolina limited liability company, as Borrower,", size=10, align="center", space_after=10)
para(doc, "ELENA VASQUEZ-TORRES and REGINALD K. OSEI,", size=12, bold=True, align="center", space_after=2)
para(doc, "as Guarantors,", size=10, align="center", space_after=10)
para(doc, "and", size=10.5, italic=True, align="center", space_after=10)
para(doc, "PINNACLE SAVINGS BANK, N.A.,", size=12, bold=True, align="center", space_after=2)
para(doc, "a national banking association, as Lender", size=10, align="center", space_after=34)

para(doc, "Dated as of February 28, 2025", size=11, align="center", space_after=6)
para(doc, "(Anticipated Closing Date)", size=9, italic=True, align="center", space_after=30)

para(doc, "The Piedmont at Brightleaf", size=12, bold=True, align="center", space_after=2)
para(doc, "601 and 615 Foster Street, Durham, Durham County, North Carolina 27701", size=10, align="center", space_after=2)
para(doc, "Durham County Parcel Identification Nos. 0821-04-72-3341 and 0821-04-72-4102", size=10, align="center", space_after=30)
para(doc, "Bank Internal Loan No. CRE-2025-0342", size=10, bold=True, align="center", space_after=2)
para(doc, "Prepared by Ashford, Cromdale Consulting & Laine LLP, counsel to Lender", size=9, italic=True, align="center", space_after=0)

page_break(doc)

# ---------------------------------------------------------------- TOC
heading1(doc, "Table of Contents", before=0, after=12)
TOC = [
 ("ARTICLE I", "DEFINITIONS; INTERPRETATION"),
 ("1.1", "Defined Terms"), ("1.2", "Accounting Terms and Determinations"),
 ("1.3", "Interpretation; Construction"), ("1.4", "Rates and Computations"),
 ("ARTICLE II", "THE LOAN"),
 ("2.1", "Commitment Amount"), ("2.2", "Conforming Adjustment of Commitment Amount; LTC Equity Deposit"),
 ("2.3", "The Note"), ("2.4", "Purpose of the Loan"),
 ("2.5", "Interest; Applicable Rate"), ("2.6", "Daily Simple SOFR; Benchmark Replacement"),
 ("2.7", "Interest Reserve"), ("2.8", "Fees"), ("2.9", "Payments; Application"),
 ("2.10", "Prepayment; Exit Fee"), ("2.11", "Default Rate"),
 ("2.12", "Computation of Interest; Maximum Rate"), ("2.13", "Maturity; Extension Option"),
 ("2.14", "Increased Costs; Illegality; Taxes"), ("2.15", "No Reborrowing"),
 ("ARTICLE III", "CONDITIONS PRECEDENT TO CLOSING"),
 ("3.1", "Loan Documents"), ("3.2", "Title Insurance and Survey"), ("3.3", "Appraisal"),
 ("3.4", "Environmental Conditions"), ("3.5", "Intercreditor Agreement"),
 ("3.6", "Single-Purpose Entity Amendments; Independent Manager; Non-Consolidation Opinion"),
 ("3.7", "Equity Contribution; LTC Equity Deposit"), ("3.8", "Payoff of Existing Mortgage"),
 ("3.9", "Construction Contract; Architect’s Contract; Bonding"), ("3.10", "Insurance; Flood Determination"),
 ("3.11", "Organizational Documents; Authority"), ("3.12", "Zoning, Permits and Declaration Approval"),
 ("3.13", "Financial Condition of Borrower and Guarantors"), ("3.14", "Legal Opinions"),
 ("3.15", "Fees and Expenses"), ("3.16", "Mezzanine Loan Documentation and Certification"),
 ("3.17", "Due Diligence Currency"), ("3.18", "Additional Conditions"),
 ("ARTICLE IV", "ADVANCES; DISBURSEMENT MECHANICS"),
 ("4.1", "Draw Schedule"), ("4.2", "Draw Requests"), ("4.3", "Conditions to Each Advance"),
 ("4.4", "Retainage"), ("4.5", "Equity First"), ("4.6", "Cost Overruns"),
 ("4.7", "Inspections and Retainage of Advances"), ("4.8", "Lender Advances; Limitations"),
 ("4.9", "Advances Not a Waiver"), ("4.10", "Interest Reserve Account Mechanics"),
 ("4.11", "Title Bring-Down"), ("4.12", "Lien Waivers"), ("4.13", "Change Orders"),
 ("4.14", "Sufficiency of Funds; Completion"),
 ("ARTICLE V", "REPRESENTATIONS AND WARRANTIES"),
 ("5.1", "Organization; Existence; Authority"), ("5.2", "Ownership and Capital Structure"),
 ("5.3", "Title; Permitted Exceptions"), ("5.4", "No Litigation"),
 ("5.5", "Compliance with Laws; Zoning"), ("5.6", "Financial Statements"),
 ("5.7", "No Default"), ("5.8", "Permits and Approvals"),
 ("5.9", "Single-Purpose Entity"), ("5.10", "Environmental Representations"),
 ("5.11", "Construction Documents; GMP Contract"), ("5.12", "Insurance"),
 ("5.13", "Solvency"), ("5.14", "Affiliate Transactions"),
 ("5.15", "Mezzanine Loan; Intercreditor Agreement"), ("5.16", "Anti-Money Laundering; OFAC; Beneficial Ownership"),
 ("5.17", "Brokers"), ("5.18", "No Other Financing"), ("5.19", "No Reliance; Survival"),
 ("ARTICLE VI", "AFFIRMATIVE COVENANTS"),
 ("6.1", "Existence; Good Standing"), ("6.2", "Construction and Completion"),
 ("6.3", "Compliance with Laws, Permits and the Declaration"), ("6.4", "Insurance"),
 ("6.5", "Property Condition; Taxes, Assessments and Charges"), ("6.6", "Books and Records; Inspection Rights"),
 ("6.7", "Use of Proceeds"), ("6.8", "Further Assurances"),
 ("6.9", "Notices of Default and Other Material Events"), ("6.10", "Intercreditor Agreement"),
 ("6.11", "Maintenance of Guaranties"), ("6.12", "Expense Reimbursement"),
 ("ARTICLE VII", "NEGATIVE COVENANTS"),
 ("7.1", "Indebtedness"), ("7.2", "Liens"), ("7.3", "Transfers; Change in Control"),
 ("7.4", "Amendments to Organizational Documents"), ("7.5", "Affiliate Transactions"),
 ("7.6", "Distributions"), ("7.7", "Change in Business"), ("7.8", "Amendments to Construction Documents"),
 ("7.9", "Amendments to Mezzanine Documents"), ("7.10", "Capital Calls; Involuntary Dilution"),
 ("7.11", "Prepayment of Other Indebtedness"), ("7.12", "Fiscal Year; Accounting Changes"),
 ("ARTICLE VIII", "FINANCIAL COVENANTS AND REPORTING"),
 ("8.1", "Loan-to-Cost Ratio"), ("8.2", "Loan-to-Value Ratio"),
 ("8.3", "Debt Service Coverage Ratio"), ("8.4", "Borrower Net Worth"),
 ("8.5", "Guarantor Liquidity"), ("8.6", "Financial Reporting"),
 ("8.7", "Construction and Project Reporting"), ("8.8", "Interest Reserve Reporting"),
 ("8.9", "Compliance Certificates"), ("8.10", "Cure of Financial Covenant Breach"),
 ("8.11", "Calculations and Defined Financial Terms"),
 ("ARTICLE IX", "INSURANCE; CASUALTY AND CONDEMNATION"),
 ("9.1", "Required Insurance"), ("9.2", "Policy Requirements; Evidence; Notices"),
 ("9.3", "Casualty"), ("9.4", "Condemnation"), ("9.5", "Application of Proceeds"),
 ("ARTICLE X", "ENVIRONMENTAL MATTERS"),
 ("10.1", "Compliance with Environmental Laws"), ("10.2", "Compliance with the NFA Letter"),
 ("10.3", "Affected Area Use Restriction"), ("10.4", "Vapor Mitigation System"),
 ("10.5", "Soil Management Plan"), ("10.6", "Deed Notice"),
 ("10.7", "Environmental Notices and Reports"), ("10.8", "Lender’s Rights; No Lender Liability"),
 ("10.9", "Environmental Indemnity"), ("10.10", "Environmental Insurance"),
 ("ARTICLE XI", "SINGLE-PURPOSE ENTITY; SEPARATENESS"),
 ("11.1", "Single-Purpose Entity Covenants"), ("11.2", "Independent Manager"),
 ("11.3", "Non-Consolidation"), ("11.4", "Bankruptcy Limitations"),
 ("11.5", "Affiliate Separateness — Brightleaf Entities"),
 ("ARTICLE XII", "COLLATERAL; PLEDGED INTERESTS; INTERCREDITOR"),
 ("12.1", "Security Documents"), ("12.2", "Pledged Interests"),
 ("12.3", "Required Intercreditor Terms"), ("12.4", "Permitted Mezzanine Loan"),
 ("12.5", "Perfection; UCC Filings"), ("12.6", "Remedies Against Pledged Interests"),
 ("ARTICLE XIII", "GUARANTIES"),
 ("13.1", "Completion Guaranty"), ("13.2", "Carry Guaranty"),
 ("13.3", "Partial Repayment Guaranty"), ("13.4", "Environmental Indemnity"),
 ("13.5", "Nature of Guaranties; Waivers"), ("13.6", "Recourse Carve-Outs"),
 ("13.7", "Guarantor Reporting"), ("13.8", "Release of Guaranties"),
 ("ARTICLE XIV", "DEFAULT AND REMEDIES"),
 ("14.1", "Events of Default"), ("14.2", "Notice and Cure Periods"), ("14.3", "Remedies"),
 ("14.4", "Completion by Lender"), ("14.5", "Receiver"), ("14.6", "Cumulative Remedies"),
 ("14.7", "Application of Proceeds"), ("14.8", "Power of Attorney"),
 ("14.9", "North Carolina Enforcement Provisions"),
 ("ARTICLE XV", "MISCELLANEOUS"),
 ("15.1", "Notices"), ("15.2", "Governing Law"), ("15.3", "Venue; Waiver of Jury Trial"),
 ("15.4", "Expenses"), ("15.5", "Indemnity"), ("15.6", "Assignment and Participation"),
 ("15.7", "No Waiver"), ("15.8", "Severability"), ("15.9", "Entire Agreement"),
 ("15.10", "Counterparts; Electronic Signatures"), ("15.11", "Time of the Essence"),
 ("15.12", "Survival"), ("15.13", "Confidentiality"), ("15.14", "No Third-Party Beneficiaries"),
 ("15.15", "Marshalling"), ("15.16", "Amendments and Waivers"),
 ("15.17", "Relationship of the Parties"),
]
for num, title in TOC:
    p = doc.add_paragraph()
    pf = p.paragraph_format
    pf.left_indent = Inches(0.25 if num.startswith("ARTICLE") else 0.55)
    pf.first_line_indent = Inches(0)
    pf.space_after = Pt(1.0 if not num.startswith("ARTICLE") else 5)
    pf.space_before = Pt(5 if num.startswith("ARTICLE") else 0)
    r = p.add_run(f"{num}   {title}" if num.startswith("ARTICLE") else f"{num}    {title}")
    r.font.size = Pt(9.5 if not num.startswith("ARTICLE") else 10)
    r.font.name = FONT
    r.bold = num.startswith("ARTICLE")
page_break(doc)
para(doc, "SCHEDULES AND EXHIBITS", size=10.5, bold=True, align="center", space_before=0, space_after=10)
for s in [
    ("Schedule 1.1", "Certain Defined Terms and Capital Structure"),
    ("Schedule 5.2", "Membership Interests of Borrower; Pledged Interests"),
    ("Schedule 8.11", "Financial Covenant Calculations (Illustrative)"),
    ("Exhibit A", "Legal Description of the Property"),
    ("Exhibit B", "Permitted Exceptions"),
    ("Exhibit C", "Approved Project Budget"),
    ("Exhibit D", "Approved Draw Schedule"),
    ("Exhibit E", "Interest Reserve and Interest Rate Provisions"),
    ("Exhibit F", "NCDEQ No Further Action Letter — Compliance Schedule"),
    ("Exhibit G", "Form of Draw Request and Borrower’s Certificate"),
    ("Exhibit H", "Schedule of Open Items, Drafting Notes and Assumptions"),
]:
    p = doc.add_paragraph()
    p.paragraph_format.left_indent = Inches(1.0)
    p.paragraph_format.space_after = Pt(3)
    r = p.add_run(s[0] + "  —  ")
    r.bold = True; r.font.size = Pt(10); r.font.name = FONT
    r2 = p.add_run(s[1]); r2.font.size = Pt(10); r2.font.name = FONT

para(doc, "", space_after=20)

# ---------------------------------------------------------------- preamble
para(doc, "CONSTRUCTION-TO-MINI-PERMANENT LOAN AGREEMENT", size=13, bold=True,
     align="center", space_before=10, space_after=14)

rich(doc, [
    ("THIS CONSTRUCTION-TO-MINI-PERMANENT LOAN AGREEMENT", {"bold": True}),
    (" (this “Agreement”) is made and entered into as of February 28, 2025 (the “Effective Date”), by and among "),
    ("HARBORVIEW CAPITAL PARTNERS LLC", {"bold": True}),
    (", a North Carolina limited liability company (“Borrower”), "),
    ("ELENA VASQUEZ-TORRES", {"bold": True}),
    (", an individual resident of Durham County, North Carolina, and "),
    ("REGINALD K. OSEI", {"bold": True}),
    (", an individual resident of Orange County, North Carolina (each a “Guarantor” and together the “Guarantors”), and "),
    ("PINNACLE SAVINGS BANK, N.A.", {"bold": True}),
    (", a national banking association (“Lender”)."),
], first_indent=0.5)

heading1(doc, "Recitals", before=14, after=8, size=11.5)

rich(doc, [("A.", {"bold": True}),
    ("  Lender has agreed to make a construction-to-mini-permanent loan to Borrower in the original principal amount of up to the Commitment Amount (as defined below), the proceeds of which will be used to finance a portion of the costs of constructing the Project (as defined below) and to fund the Interest Reserve and certain Fees, all on the terms and subject to the conditions set forth in this Agreement.")],
    first_indent=0.0, left_indent=0.5)
rich(doc, [("B.", {"bold": True}),
    ("  The Loan is evidenced by the Note and secured by, among other things, the Deed of Trust encumbering the Property, the Assignment of Rents, the Security Agreement, the Pledge Agreements and the other Security Documents, and is guaranteed and supported by the Guaranties and the Environmental Indemnity.")],
    first_indent=0.0, left_indent=0.5)
rich(doc, [("C.", {"bold": True}),
    ("  Borrower has advised Lender that Brightleaf Mezzanine Capital LLC, a North Carolina limited liability company, has made or will make a mezzanine loan to Borrower in the original principal amount of $9,200,000, secured by a pledge of 100% of the membership interests in Borrower, and Lender has agreed to permit the Mezzanine Loan solely on the terms and subject to the conditions set forth in this Agreement and the Intercreditor Agreement.")],
    first_indent=0.0, left_indent=0.5)
rich(doc, [("D.", {"bold": True}),
    ("  This Agreement supersedes the terms of that certain Term Sheet dated January 10, 2025 between Lender and Borrower (the “Term Sheet”) with respect to the subject matter hereof, other than the provisions of Sections 22 and 23 of the Term Sheet, which survive in accordance with their terms. The Term Sheet was a non-binding indication of terms except as expressly provided therein; this Agreement is the definitive agreement of the parties with respect to the Loan.")],
    first_indent=0.0, left_indent=0.5)
rich(doc, [("NOW, THEREFORE", {"bold": True}),
    (", in consideration of the mutual covenants and agreements contained herein, and for other good and valuable consideration, the receipt and sufficiency of which are hereby acknowledged, the parties hereto agree as follows:")],
    first_indent=0.5)

# ================================================================ ARTICLE I
article(doc, "I", "Definitions; Interpretation")

section(doc, "1.1", "Defined Terms",
    "The following terms have the meanings set forth below. Capitalized terms used but not defined in this Section 1.1 "
    "have the meanings given to them elsewhere in this Agreement or in the other Loan Documents.")

DEFS = [
("Affected Area", "means the approximately 0.38-acre area in the northeast corner of Parcel 2 that is identified in the Phase II Report and Figure 3 of the Phase I ESA as the area of residual petroleum contamination exceeding NCDEQ residential Preliminary Soil Remediation Goals, and that is subject to the land use restriction described in the NFA Letter."),
("Affiliate", "means, with respect to any Person, any other Person that directly or indirectly controls, is controlled by, or is under common control with such Person, and, with respect to any individual, any member of such individual’s immediate family and any trust or estate-planning vehicle established for the benefit of such individual or such family members. For the avoidance of doubt, Brightleaf Investors Group LLC, Brightleaf Mezzanine Capital LLC, Thomas R. Chen and each of their respective Affiliates are Affiliates of Borrower."),
("Agreement", "means this Construction-to-Mini-Permanent Loan Agreement, as it may be amended, restated, supplemented or otherwise modified from time to time."),
("Applicable Spread", "means (a) during the Construction Period, 3.25% per annum, and (b) during the Mini-Perm Period, 3.50% per annum."),
("Approved Budget", "means the Project budget set forth on Exhibit C, as approved by Lender and as the same may be revised from time to time only with Lender’s prior written consent in accordance with Section 4.6 and Section 7.8."),
("Approved Draw Schedule", "means the draw schedule set forth on Exhibit D, as the same may be adjusted in accordance with Section 2.2 and Section 4.1."),
("Approved Plans", "means the plans and specifications for the Project prepared by Architect and approved by Lender, as the same may be modified only with Lender’s prior written consent in accordance with Section 4.13."),
("Architect", "means Meridian Design Collective PC, a North Carolina professional corporation, and its permitted successors and assigns approved by Lender."),
("Architect’s Contract", "means the agreement between Borrower and Architect for the design and construction administration of the Project, as collaterally assigned to Lender."),
("Business Day", "means any day other than a Saturday, a Sunday or a day on which commercial banks in Charlotte, North Carolina or New York, New York are authorized or required to be closed."),
("Closing Date", "means the date on which the first Advance is made under this Agreement, which is anticipated to be February 28, 2025."),
("Code", "means the Internal Revenue Code of 1986, as amended."),
("Commitment Amount", "means $47,500,000 (Forty-Seven Million Five Hundred Thousand and No/100 Dollars), subject to reduction in accordance with Section 2.2 and Section 2.15."),
("Completion Guaranty", "means the completion guaranty of even date herewith executed by the Guarantors in favor of Lender."),
("Construction Contract", "means that certain guaranteed maximum price construction contract between Borrower and General Contractor dated [●], 2024 (the “GMP Contract”), in the guaranteed maximum price amount of $34,750,000, as collaterally assigned to Lender and as the same may be modified only in accordance with Section 4.13."),
("Construction Maturity Date", "means August 28, 2027, being the date that is thirty (30) months after the anticipated Closing Date, as such date may be extended only pursuant to Section 2.13(c)."),
("Construction Period", "means the period commencing on the Closing Date and ending on the earlier of (a) the Construction Maturity Date and (b) the date on which the entire outstanding principal balance of the Loan is converted to the Mini-Perm Period in accordance with Section 2.13(b)."),
("Conversion Date", "means the first day of the Mini-Perm Period, being the Construction Maturity Date unless an earlier conversion occurs in accordance with Section 2.13(b)."),
("Daily Simple SOFR", "means, for any day, the Secured Overnight Financing Rate published by the Federal Reserve Bank of New York (or any successor administrator selected by Lender in accordance with Section 2.6) for the Business Day immediately preceding such day, as determined by Lender in accordance with Section 2.6; provided that if such rate is not so published for any reason, Daily Simple SOFR shall be determined in accordance with the Benchmark Replacement provisions of Section 2.6."),
("Deed Notice", "means the notice of residual contamination and land use restriction required to be recorded in the Durham County Registry of Deeds pursuant to Condition 4 of the NFA Letter."),
("Deed of Trust", "means the Deed of Trust, Assignment of Rents, Security Agreement and Fixture Filing of even date herewith from Borrower, as grantor, to the trustee named therein, for the benefit of Lender, encumbering the Property and securing the Obligations, as the same may be amended, restated, supplemented or otherwise modified from time to time."),
("Default", "means any event or condition that, with the giving of notice or the passage of time or both, would constitute an Event of Default."),
("Default Rate", "means a rate per annum equal to the lesser of (a) the Applicable Rate plus 5.00% and (b) the Maximum Rate."),
("Environmental Indemnity", "means the environmental indemnity agreement of even date herewith executed by Borrower and the Guarantors in favor of Lender, unlimited in amount, as the same may be amended, restated or modified from time to time."),
("Environmental Laws", "means all federal, state and local statutes, regulations, ordinances, orders and common law relating to pollution, the protection of human health or the environment, or the use, storage, generation, transportation, treatment, disposal or release of Hazardous Substances, including CERCLA, the Resource Conservation and Recovery Act, the Clean Water Act, the Clean Air Act, the Toxic Substances Control Act, the North Carolina Oil Pollution and Hazardous Substances Control Act (N.C.G.S. Chapter 143, Article 21), the North Carolina Inactive Hazardous Sites Response Act (N.C.G.S. Chapter 130A, Article 9) and the North Carolina Underground Storage Tank regulations (15A NCAC 2L and 2N), in each case as amended."),
("Equity Contribution", "means the LTC Equity Deposit required under Section 2.2 and Section 3.7, together with the Land (contributed at the Contribution Value), which together constitute Borrower’s equity in the Project for purposes of this Agreement."),
("Event of Default", "has the meaning set forth in Section 14.1."),
("Existing Mortgage", "means that certain Deed of Trust recorded in Book 6215, Page 892, Durham County Registry, dated September 14, 2018, from Foster Street Properties LLC (predecessor-in-title to Borrower, as applicable) to the trustee named therein for the benefit of Triangle Commercial Bank, securing an original indebtedness of $3,400,000, together with all modifications, extensions and renewals thereof."),
("Fees", "means the Origination Fee, the Unused Line Fee, the Exit Fee, the Extension Fee, the Servicing Fee (if any) and all other fees and charges payable by Borrower under the Loan Documents."),
("GAAP", "means generally accepted accounting principles in the United States, consistently applied."),
("General Contractor", "means Graystone Construction Group Inc., a North Carolina corporation (NC General Contractor License No. 78442), and its permitted successors and assigns approved by Lender."),
("Guaranties", "means, collectively, the Completion Guaranty, the Carry Guaranty, the Partial Repayment Guaranty and each other guaranty executed by any Guarantor in favor of Lender, together with the Environmental Indemnity."),
("Hazardous Substances", "means any substance, material or waste that is regulated under any Environmental Law, including petroleum and petroleum products, asbestos-containing materials, polychlorinated biphenyls, per- and polyfluoroalkyl substances, and volatile organic compounds."),
("Improvements", "means the six-story mixed-use building containing 212 residential units, approximately 18,400 square feet of retail space, and a four-level structured parking garage containing 276 spaces, together with all related site improvements, amenities and appurtenances, to be constructed on the Land in accordance with the Approved Plans."),
("Independent Manager", "means the independent manager of Borrower required under Section 11.2, who shall be an individual that is not, and has not been at any time during the five (5) years preceding appointment, an officer, director, manager, member, employee, creditor, supplier, customer or Affiliate of Borrower, any member of Borrower, Mezzanine Lender or any of their respective Affiliates."),
("Interest Reserve", "means the reserve in the amount of $4,850,000 funded from the proceeds of the Loan at Closing (plus any amounts deposited by Borrower under Section 2.7), held in the Interest Reserve Account and applied solely to the payment of interest accruing on the Loan during the Construction Period in accordance with Section 2.7."),
("Interest Reserve Account", "means the segregated sub-account of the Loan established and maintained by Lender in accordance with Section 2.7."),
("Intercreditor Agreement", "means the intercreditor and subordination agreement among Lender, Mezzanine Lender and Borrower, in form and substance satisfactory to Lender, to be executed and delivered as a condition to Closing in accordance with Section 3.5 and Section 12.3."),
("Land", "means the real property described on Exhibit A, consisting of Parcel 1 (PIN 0821-04-72-3341, 601 Foster Street, approximately 2.09 acres) and Parcel 2 (PIN 0821-04-72-4102, 615 Foster Street, approximately 1.38 acres), comprising approximately 3.47 acres in the aggregate."),
("Lender Parties", "means Lender, its Affiliates, and their respective officers, directors, employees, agents, attorneys, servicers, participants and assignees."),
("Loan", "means the construction-to-mini-permanent loan made by Lender to Borrower pursuant to this Agreement in the original principal amount of the Commitment Amount."),
("Loan Documents", "means this Agreement, the Note, the Deed of Trust, the Assignment of Rents, the Security Agreement, the Pledge Agreements, the Guaranties, the Environmental Indemnity, the Intercreditor Agreement, each Draw Request, each Compliance Certificate and each other agreement, instrument, certificate or document now or hereafter executed by Borrower or any Guarantor in connection with the Loan, as each may be amended, restated, supplemented or otherwise modified from time to time."),
("Loan-to-Cost Ratio", "means, as of any date of determination, the ratio, expressed as a percentage, of (a) the outstanding principal balance of the Loan (plus, for purposes of the closing test, the undrawn portion of the Commitment Amount) to (b) Total Project Costs."),
("Loan-to-Value Ratio", "means, as of any date of determination, the ratio, expressed as a percentage, of (a) the outstanding principal balance of the Loan to (b) the then-current Appraised Value of the Property (on an as-completed or as-stabilized basis, as the context requires)."),
("LTC Equity Deposit", "means cash equity in the amount of $2,140,000 deposited by Borrower with Lender at Closing, from sources verified by Lender to be independent of Mezzanine Lender, Brightleaf Investors Group LLC, Thomas R. Chen and their respective Affiliates, in accordance with Section 2.2 and Section 3.7."),
("Material Adverse Effect", "means any event, condition or circumstance that, individually or in the aggregate, (a) has or would reasonably be expected to have a material adverse effect on the business, assets, liabilities, financial condition, or results of operations of Borrower, any Guarantor or the Project, (b) materially impairs the value, use, occupancy or operation of the Property, (c) materially impairs the ability of Borrower or any Guarantor to perform its obligations under the Loan Documents, or (d) materially impairs the enforceability, validity or priority of any Lien granted to Lender under the Security Documents."),
("Maturity Date", "means the Mini-Perm Maturity Date, as such date may be extended to the Extended Maturity Date pursuant to Section 2.13(c)."),
("Maximum Rate", "means the maximum rate of interest permitted to be charged under applicable law, including N.C.G.S. § 24-1.1 et seq."),
("Mezzanine Lender", "means Brightleaf Mezzanine Capital LLC, a North Carolina limited liability company (NC Secretary of State File No. 2103988), and its successors and assigns permitted under the Intercreditor Agreement."),
("Mezzanine Loan", "means the mezzanine loan in the original principal amount of $9,200,000 made or to be made by Mezzanine Lender to Borrower, bearing interest at 12.50% per annum fixed, with payment-in-kind interest during the Construction Period and cash-pay interest thereafter, maturing coterminously with the Loan (including any extension), and secured by a pledge of 100% of the Pledged Interests, as more particularly described on Schedule 1.1."),
("Mezzanine Documents", "means the Mezzanine Loan agreement, the pledge and security documents delivered to Mezzanine Lender, and each other document evidencing or securing the Mezzanine Loan."),
("Mini-Perm Maturity Date", "means August 28, 2028, being the date that is twelve (12) months after the Construction Maturity Date."),
("Mini-Perm Period", "means the period commencing on the Conversion Date and ending on the Maturity Date."),
("Note", "means the promissory note of even date herewith executed by Borrower in favor of Lender in the principal amount of the Commitment Amount, as the same may be amended, restated, renewed, extended or replaced from time to time."),
("NFA Letter", "means the No Further Action determination letter issued by NCDEQ, Inactive Hazardous Sites Branch, dated September 30, 2024, for Site ID IHSB-24-1203 / Incident No. NONUST-24-0847, together with all conditions, land use restrictions and requirements set forth therein or in any modification thereof."),
("NCDEQ", "means the North Carolina Department of Environmental Quality, Inactive Hazardous Sites Branch, or any successor agency."),
("Obligations", "means all present and future obligations and liabilities of Borrower and each Guarantor to Lender under or in connection with the Loan Documents, whether for principal, interest, Fees, expenses, indemnities or otherwise, whether direct or indirect, absolute or contingent, and whether now existing or hereafter arising."),
("Origination Fee", "means a fee equal to 1.00% of the Commitment Amount, being $475,000 as of the Effective Date and $453,600 if the Commitment Amount is reduced pursuant to Section 2.2."),
("Parcel 1", "means the parcel identified as Durham County PIN 0821-04-72-3341, addressed as 601 Foster Street, Durham, North Carolina 27701, as more particularly described on Exhibit A."),
("Parcel 2", "means the parcel identified as Durham County PIN 0821-04-72-4102, addressed as 615 Foster Street, Durham, North Carolina 27701, as more particularly described on Exhibit A."),
("Partial Repayment Guaranty", "means the partial repayment guaranty of even date herewith executed by the Guarantors in favor of Lender in the maximum aggregate amount of $11,875,000 (being 25% of the Commitment Amount as of the Effective Date), as the same may be adjusted pursuant to Section 13.3."),
("Permitted Exceptions", "means those matters described on Exhibit B, together with such other exceptions to title as may be approved in writing by Lender."),
("Person", "means any individual, corporation, partnership, limited liability company, joint venture, association, trust, estate, unincorporated organization or governmental authority."),
("Phase I ESA", "means the Phase I Environmental Site Assessment prepared by Environmental Consultant, Project No. SEC-2024-1147, dated October 28, 2024, prepared in accordance with ASTM E1527-21 and 40 C.F.R. Part 312."),
("Phase II Report", "means the Phase II Environmental Site Assessment prepared by Environmental Consultant, Project No. SEC-2024-1089, dated August 30, 2024."),
("Environmental Consultant", "means Sentinel Environmental Consulting LLC, and any successor consultant approved by Lender."),
("Pledged Interests", "means 100% of the membership interests in Borrower, being the 62% membership interest held by Elena Vasquez-Torres, the 28% membership interest held by Brightleaf Investors Group LLC, and the 10% membership interest held by Reginald K. Osei, together with all economic and governance rights appurtenant thereto, all distributions thereon and all proceeds thereof."),
("Pledge Agreements", "means, collectively, the pledge and security agreements of even date herewith executed by each member of Borrower in favor of Lender, granting Lender a security interest in the Pledged Interests, as the same may be amended, restated or modified from time to time."),
("Project", "means the acquisition (previously completed), development, construction, ownership and operation of the Improvements on the Land, together with all site work, amenities, infrastructure and related work contemplated by the Approved Plans."),
("Property", "means the Land, the Improvements, all fixtures, personal property, intangibles, permits, plans, contracts, accounts, rents and other property rights described in the Security Documents, and all proceeds thereof."),
("Security Documents", "means the Deed of Trust, the Assignment of Rents, the Security Agreement, the Pledge Agreements, the collateral assignments of the Construction Contract and the Architect’s Contract, the collateral assignment of insurance proceeds and condemnation awards, and each other document granting or perfecting a Lien in favor of Lender."),
("SOFR Floor", "means 1.00% per annum."),
("Soil Management Plan", "means the soil management plan for the Affected Area required by Condition 3 of the NFA Letter, as approved by NCDEQ and approved by Lender."),
("SPE", "means a single-purpose, bankruptcy-remote entity satisfying the covenants set forth in Article XI."),
("Substantial Completion", "means substantial completion of the Improvements in accordance with the Approved Plans, as evidenced by (a) the architect’s certificate of substantial completion, (b) issuance by the City of Durham of a certificate of occupancy (temporary or permanent) permitting occupancy of the residential units and retail space, and (c) the construction inspector’s certification of substantial completion."),
("Title Company", "means Aldersgate Title & Escrow Inc., or such other title insurer approved by Lender."),
("Total Project Costs", "means the aggregate of all costs and expenses incurred or to be incurred in connection with the acquisition, development, construction and completion of the Project, calculated in accordance with the Approved Budget on a hard-cost, soft-cost and financing-cost basis, and including the Land at the Contribution Value, the Interest Reserve, the Origination Fee and the Developer Fee, but excluding the Mezzanine Loan, accrued interest on the Mezzanine Loan and any cost funded by Borrower equity that is not a Project cost. As of the Effective Date, Total Project Costs are $56,700,000, as reconciled on Exhibit C."),
("Contribution Value", "means $8,200,000, being the acquisition cost of the Land recorded on Borrower’s books, subject to verification by Lender in accordance with Section 3.7(d)."),
("Vapor Mitigation System", "means the passive sub-slab depressurization system, with capability for conversion to active depressurization, required by Condition 1 of the NFA Letter to be installed beneath any enclosed structure constructed over the Affected Area, designed by a professional engineer licensed in North Carolina and approved by NCDEQ."),
]
for term, txt in DEFS:
    definition(doc, term, txt)

section(doc, "1.2", "Accounting Terms and Determinations",
    "All accounting terms not specifically defined in this Agreement shall be construed in accordance with GAAP "
    "consistently applied, except that for purposes of determining compliance with the financial covenants in Article VIII, "
    "all calculations shall be made on an unconsolidated basis and in a manner consistent with the calculations set forth "
    "on Schedule 8.11. All determinations by Lender of the Applicable Rate, the Loan-to-Cost Ratio, the Loan-to-Value Ratio, "
    "the Debt Service Coverage Ratio and the Appraised Value shall be made in good faith and shall be conclusive and binding "
    "on Borrower absent manifest error. Any reference to a fiscal period means the fiscal period of Borrower in effect on the date hereof.")

section(doc, "1.3", "Interpretation; Construction",
    "In this Agreement, unless the context otherwise requires: (a) the singular includes the plural and vice versa; "
    "(b) “including” means “including without limitation”; (c) references to Articles, Sections, Schedules and Exhibits are to "
    "Articles and Sections of, and Schedules and Exhibits to, this Agreement, each of which is incorporated herein by reference; "
    "(d) headings are for convenience only and do not affect interpretation; (e) references to any document are to that document "
    "as amended, restated, supplemented or otherwise modified from time to time in accordance with its terms and, where applicable, "
    "the Loan Documents; (f) references to any statute or regulation include any successor provision; and (g) “$” and “Dollars” "
    "refer to the lawful currency of the United States.")

section(doc, "1.4", "Rates and Computations",
    "All computations of interest and Fees under the Loan Documents shall be made on the basis of a 360-day year and the actual "
    "number of days elapsed. Interest shall accrue on the outstanding principal balance of the Loan at the Applicable Rate for each "
    "day such balance is outstanding. Each determination by Lender of an interest rate or Fee shall be conclusive and binding on "
    "Borrower absent manifest error. The parties acknowledge that the Term Sheet provides for a SOFR Floor of 1.00% applicable "
    "to both the Construction Period and the Mini-Perm Period and that the SOFR Floor is incorporated into the definition of "
    "Applicable Rate set forth in Section 2.5(b).")

# ================================================================ ARTICLE II
article(doc, "II", "The Loan")

section(doc, "2.1", "Commitment Amount",
    "Subject to the terms and conditions of this Agreement, Lender agrees to make the Loan to Borrower in one or more Advances "
    "in an aggregate principal amount not to exceed the Commitment Amount. The Loan is a construction-to-mini-permanent facility "
    "that converts from the Construction Period to the Mini-Perm Period in accordance with Section 2.13. Amounts repaid or prepaid "
    "may not be reborrowed, and the Commitment Amount shall automatically terminate on the earlier of (a) the Conversion Date and "
    "(b) the Construction Maturity Date, except with respect to the funding of the Interest Reserve and the release of Retainage "
    "in accordance with Section 4.4.")

section(doc, "2.2", "Conforming Adjustment of Commitment Amount; LTC Equity Deposit",
    "")
rich(doc, [("(a)  LTC Compliance.", {"bold": True}),
    ("  Borrower and Lender acknowledge that, as of the Effective Date, Total Project Costs are $56,700,000 and the Loan-to-Cost Ratio "
     "calculated on the basis of the Commitment Amount of $47,500,000 would be 83.77%, which exceeds the maximum Loan-to-Cost Ratio of "
     "80.00% permitted under Section 8.1. Borrower and Lender further acknowledge that the Loan-to-Value Ratio on an as-completed basis "
     "calculated on the basis of the Commitment Amount would be 65.25%, which exceeds the maximum Loan-to-Value Ratio of 65.00% permitted "
     "under Section 8.2.")],
    first_indent=0.0, left_indent=0.0, space_after=6)
rich(doc, [("(b)  Conforming Reduction.", {"bold": True}),
    ("  Notwithstanding Section 2.1, the Commitment Amount shall, on the Closing Date, be automatically reduced to $45,360,000 (the "
     "“Conforming Commitment Amount”), unless prior to the Closing Date Lender and Borrower execute a written amendment to this Agreement "
     "(i) increasing Total Project Costs by an amount sufficient to satisfy Section 8.1 with respect to the Commitment Amount of "
     "$47,500,000 (which, for the avoidance of doubt, would require Total Project Costs of not less than $59,375,000) and (ii) evidencing "
     "the funding of such increased Total Project Costs from additional equity contributions that satisfy Section 3.7(c). Any such "
     "amendment shall conform the Approved Budget, the Approved Draw Schedule, the Origination Fee and each other amount computed by "
     "reference to the Commitment Amount.")],
    first_indent=0.0, left_indent=0.0, space_after=6)
rich(doc, [("(c)  LTC Equity Deposit.", {"bold": True}),
    ("  Concurrently with the reduction described in Section 2.2(b), Borrower shall deposit the LTC Equity Deposit of $2,140,000 with "
     "Lender in the Equity Escrow Account. The LTC Equity Deposit shall be disbursed by Lender in accordance with Section 4.5 and "
     "the Equity Escrow Agreement. For the avoidance of doubt, the parties acknowledge that the deposit of the LTC Equity Deposit "
     "without the corresponding reduction of the Commitment Amount would not, and is not intended to, cure the exceedance described "
     "in Section 2.2(a), because the Loan-to-Cost Ratio is computed by reference to the Loan amount and not by reference to the "
     "sources of funds.")],
    first_indent=0.0, left_indent=0.0, space_after=6)
rich(doc, [("(d)  Conformed Sources and Uses.", {"bold": True}),
    ("  Upon the adjustment described in this Section 2.2, the sources and uses of funds for the Project shall be as follows and "
     "Exhibit C shall be deemed conformed accordingly:")],
    first_indent=0.0, left_indent=0.0, space_after=8)
table(doc, [
    ["Source", "Amount"],
    ["Senior Loan (Conforming Commitment Amount)", "$45,360,000"],
    ["Mezzanine Loan (Brightleaf Mezzanine Capital LLC)", "$9,200,000"],
    ["LTC Equity Deposit (independently sourced cash)", "$2,140,000"],
    ["**Total Sources**", "**$56,700,000**"],
], widths=[4.2, 1.8], size=9.5)
note(doc, "[Note to Draft: The reduction mechanism in Section 2.2(b)–(c) is the recommended resolution of the Loan-to-Cost exceedance "
          "identified in the Credit Memorandum dated January 22, 2025 (Section 5.3 and Condition 10.1.2). It is the only arithmetic combination "
          "that cures both the 80.00% Loan-to-Cost and the 65.00% as-completed Loan-to-Value covenants while retaining the approved size of the "
          "Project. See the accompanying Memorandum at Section 3.2. Conforming changes to the Origination Fee ($453,600), the Partial Repayment "
          "Guaranty ($11,340,000), the title policy amount and the Approved Draw Schedule are made in Sections 2.8, 13.3, 3.2 and Exhibit D. "
          "Lender’s business decision is requested.]")

section(doc, "2.3", "The Note",
    "The Loan shall be evidenced by the Note, which shall be payable to the order of Lender in the principal amount of the "
    "Commitment Amount, shall bear interest as provided in this Agreement and shall be repayable in accordance with the terms "
    "hereof and thereof. In the event of any inconsistency between the Note and this Agreement, this Agreement shall control.")

section(doc, "2.4", "Purpose of the Loan",
    "The proceeds of the Loan shall be used solely to (a) pay or reimburse costs of the Project set forth in the Approved Budget, "
    "(b) fund the Interest Reserve, and (c) pay the Origination Fee. No portion of the proceeds of the Loan shall be used for any "
    "other purpose, including any distribution to Borrower’s members (other than payment of the Developer Fee in accordance with "
    "Section 7.6), any payment in respect of the Mezzanine Loan, or any acquisition of the Land (which acquisition has already occurred).")

section(doc, "2.5", "Interest; Applicable Rate", "")
rich(doc, [("(a)  Accrual and Payment.", {"bold": True}),
    ("  Interest shall accrue on the outstanding principal balance of the Loan at the Applicable Rate for each day during which such "
     "principal balance is outstanding and shall be payable monthly in arrears on the first Business Day of each calendar month, "
     "commencing on the first Business Day of the first full calendar month following the Closing Date. During the Construction Period, "
     "accrued interest shall be paid from the Interest Reserve to the extent funds are available therein and, thereafter, by Borrower "
     "from its own funds. During the Mini-Perm Period, accrued interest shall be payable by Borrower from its own funds, and no "
     "portion of the Interest Reserve shall be available for such purpose.")],
    first_indent=0.0, space_after=6)
rich(doc, [("(b)  Applicable Rate.", {"bold": True}),
    ("  “Applicable Rate” means, for any day, the lesser of (i) the sum of (A) the greater of Daily Simple SOFR for such day and "
     "the SOFR Floor, plus (B) the Applicable Spread, and (ii) the Maximum Rate. Based on a Daily Simple SOFR rate of 4.35% per annum "
     "(the rate in effect as of the date of the Credit Memorandum), the Applicable Rate would be 7.60% per annum during the "
     "Construction Period and 7.85% per annum during the Mini-Perm Period.")],
    first_indent=0.0, space_after=6)
rich(doc, [("(c)  Interest-Only Payments.", {"bold": True}),
    ("  The Loan is an interest-only facility during both the Construction Period and the Mini-Perm Period. No scheduled principal "
     "amortization shall be required; provided that the outstanding principal balance of the Loan shall be due and payable in full "
     "on the Maturity Date, subject to Section 8.10 and Section 14.1.")],
    first_indent=0.0, space_after=6)
rich(doc, [("(d)  SOFR Floor.", {"bold": True}),
    ("  If Daily Simple SOFR is less than 1.00% on any day, Daily Simple SOFR shall be deemed to be 1.00% for purposes of determining "
     "the Applicable Rate for such day.")],
    first_indent=0.0, space_after=6)

section(doc, "2.6", "Daily Simple SOFR; Benchmark Replacement", "")
rich(doc, [("(a)  Determination.", {"bold": True}),
    ("  Daily Simple SOFR shall be determined by Lender from the rate published by the Federal Reserve Bank of New York (or any "
     "successor administrator) for the applicable Business Day. Lender shall not be required to notify Borrower of each daily "
     "determination; Lender’s records shall be conclusive absent manifest error.")],
    first_indent=0.0, space_after=6)
rich(doc, [("(b)  Benchmark Replacement.", {"bold": True}),
    ("  If Lender determines that (i) the administrator of Daily Simple SOFR has ceased or will cease to provide such rate permanently "
     "or indefinitely and no successor administrator has been appointed, (ii) any governmental authority has determined that Daily "
     "Simple SOFR is no longer representative or is not to be used, (iii) Daily Simple SOFR is not published or is not ascertainable for "
     "any reason on any Business Day, or (iv) any other Benchmark Transition Event has occurred, then Lender may (in consultation with "
     "Borrower) designate a Benchmark Replacement, together with any Benchmark Replacement Adjustment and any conforming changes to the "
     "mechanics of determining the Applicable Rate and computing interest, in each case consistent with the recommended best practices "
     "of the Alternative Reference Rates Committee (“ARRC”), or if no such recommendation is available, in a manner that preserves to the "
     "greatest extent practicable the economic intent of this Agreement.")],
    first_indent=0.0, space_after=6)
rich(doc, [("(c)  Notice; Effect.", {"bold": True}),
    ("  Lender shall give Borrower not less than five (5) Business Days’ prior written notice of any Benchmark Replacement, and any such "
     "replacement shall become effective on the date specified in such notice. Any determination by Lender under this Section 2.6 shall "
     "be conclusive and binding on Borrower absent manifest error, and no such determination shall increase the Applicable Spread.")],
    first_indent=0.0, space_after=6)
rich(doc, [("(d)  No Term SOFR.", {"bold": True}),
    ("  Borrower acknowledges that the Loan bears interest at Daily Simple SOFR rather than Term SOFR, that interest therefore accrues "
     "daily on the actual outstanding balance, and that the absence of a term look-back period means that the Applicable Rate will reset "
     "each Business Day.")],
    first_indent=0.0, space_after=6)

section(doc, "2.7", "Interest Reserve", "")
rich(doc, [("(a)  Funding.", {"bold": True}),
    ("  At Closing, Lender shall fund the Interest Reserve of $4,850,000 from the proceeds of the Loan and shall deposit the same in the "
     "Interest Reserve Account. The Interest Reserve Account shall be a segregated sub-account of the Loan maintained on Lender’s books "
     "and records; it is not a trust account, and Borrower shall have no right to direct the investment or withdrawal of funds therein "
     "except as expressly provided in this Section 2.7.")],
    first_indent=0.0, space_after=6)
rich(doc, [("(b)  Application; Scope.", {"bold": True}),
    ("  Funds in the Interest Reserve Account shall be applied solely to the payment of interest accruing on the Loan during the "
     "Construction Period. The Interest Reserve shall not be available for any other purpose, including the payment of principal, Fees, "
     "the Mezzanine Loan, or any cost of construction.")],
    first_indent=0.0, space_after=6)
rich(doc, [("(c)  Adequacy Testing.", {"bold": True}),
    ("  Lender shall test the adequacy of the Interest Reserve not less than quarterly during the Construction Period and in connection "
     "with each Draw Request, in each case by comparing (i) the remaining balance of the Interest Reserve against (ii) the projected "
     "interest cost through the earlier of (A) the next anticipated Advance date and (B) the date that is ninety (90) days following the "
     "date of the test, calculated at the Applicable Rate then in effect (but in no event at a Daily Simple SOFR rate lower than 4.35% per "
     "annum). If Lender determines that the projected interest cost exceeds the remaining balance, Lender shall notify Borrower in writing, "
     "and Borrower shall deposit additional funds into the Interest Reserve Account in an amount sufficient to eliminate the deficiency "
     "within five (5) Business Days of such notice. Funds deposited by Borrower under this Section 2.7(c) shall not constitute a Loan and "
     "shall not be repayable to Borrower until the Loan has been repaid in full.")],
    first_indent=0.0, space_after=6)
rich(doc, [("(d)  Replenishment Obligation.", {"bold": True}),
    ("  If at any time the Interest Reserve is insufficient to pay interest on the next succeeding interest payment date, Borrower shall "
     "fund the amount of such deficiency from its own funds (and not from the proceeds of the Loan, the Mezzanine Loan or any other "
     "subordinate financing) within five (5) Business Days of written notice from Lender. Borrower’s failure to do so shall constitute an "
     "Event of Default under Section 14.1(a). The Carry Guaranty is in addition to, and not in lieu of, this obligation.")],
    first_indent=0.0, space_after=6)
rich(doc, [("(e)  Interest Reserve Contingency Escrow.", {"bold": True}),
    ("  In addition to the Interest Reserve, Borrower shall deposit with Lender at Closing, from sources other than the proceeds of the "
     "Loan and other than sources described in Section 3.7(c), the sum of $500,000 (the “Interest Reserve Contingency Escrow”). The Interest "
     "Reserve Contingency Escrow shall be applied, at Lender’s election, to interest shortfalls and cost overruns before any other source "
     "of Borrower funds is required, and shall otherwise be released to Borrower upon the Conversion Date if no Default or Event of "
     "Default exists.")],
    first_indent=0.0, space_after=6)
rich(doc, [("(f)  Reporting.", {"bold": True}),
    ("  Borrower shall deliver to Lender, within fifteen (15) days after the end of each calendar month during the Construction Period, a "
     "reconciliation of the Interest Reserve Account showing the beginning balance, interest charges, deposits and ending balance, together "
     "with a projection of remaining interest cost through the Construction Maturity Date.")],
    first_indent=0.0, space_after=6)
rich(doc, [("(g)  Surplus.", {"bold": True}),
    ("  Any balance remaining in the Interest Reserve Account on the Conversion Date shall be applied to the outstanding principal balance "
     "of the Loan on such date, without premium or penalty, and shall not be released to Borrower.")],
    first_indent=0.0, space_after=6)
note(doc, "[Note to Draft: The Credit Memorandum (Section 6.2) acknowledged a projected interest reserve shortfall of approximately $565,000 "
          "at a Daily Simple SOFR rate of 4.35%, while the Borrower’s draw-schedule model concludes that the reserve is adequate by $221,325 "
          "on the assumption of a 3.50% SOFR rate (a rate approximately 85 basis points below the rate in effect). Section 2.7(c) fixes the "
          "floor for adequacy testing at 4.35% and Section 2.7(e) adds a $500,000 borrower-funded contingency escrow. See Memorandum Section 3.4.]")

section(doc, "2.8", "Fees", "")
rich(doc, [("(a)  Origination Fee.", {"bold": True}),
    ("  Borrower shall pay to Lender at Closing the Origination Fee in the amount of 1.00% of the Commitment Amount, being $475,000 "
     "(or $453,600 if the Commitment Amount is reduced pursuant to Section 2.2). The Origination Fee may be funded from the proceeds of "
     "the Loan in accordance with the Approved Budget and Exhibit D.")],
    first_indent=0.0, space_after=6)
rich(doc, [("(b)  Unused Line Fee.", {"bold": True}),
    ("  Borrower shall pay to Lender a fee equal to 0.25% per annum on the average daily undrawn portion of the Commitment Amount, payable "
     "quarterly in arrears commencing on the first quarterly date following the Closing Date. For purposes of this Section 2.8(b), the "
     "undrawn portion of the Commitment Amount shall be reduced by the amount of the Interest Reserve funded at Closing.")],
    first_indent=0.0, space_after=6)
rich(doc, [("(c)  Exit Fee.", {"bold": True}),
    ("  If the Loan is repaid in full (whether voluntarily, on the Maturity Date, or as a result of acceleration following an Event of "
     "Default), Borrower shall pay to Lender an exit fee equal to (i) 0.50% of the outstanding principal balance repaid, if repayment occurs "
     "during the Construction Period, (ii) 0.25% of the outstanding principal balance repaid, if repayment occurs during the first six (6) "
     "months of the Mini-Perm Period, and (iii) zero, if repayment occurs after the first six (6) months of the Mini-Perm Period.")],
    first_indent=0.0, space_after=6)
rich(doc, [("(d)  Extension Fee.", {"bold": True}),
    ("  If Borrower exercises the Extension Option, Borrower shall pay to Lender at the time of such exercise an extension fee equal to "
     "0.25% of the outstanding principal balance of the Loan as of the Mini-Perm Maturity Date.")],
    first_indent=0.0, space_after=6)
rich(doc, [("(e)  Late Charge.", {"bold": True}),
    ("  If any payment of principal, interest or Fees is not received by Lender within five (5) days after the date due, Borrower shall pay "
     "to Lender a late charge equal to 5.00% of the amount of such payment, in addition to interest at the Default Rate.")],
    first_indent=0.0, space_after=6)
rich(doc, [("(f)  Fees Earned.", {"bold": True}),
    ("  All Fees are non-refundable when paid, except as otherwise expressly provided in the Loan Documents.")],
    first_indent=0.0, space_after=6)

section(doc, "2.9", "Payments; Application",
    "All payments of principal, interest, Fees and other amounts under the Loan Documents shall be made in lawful money of the "
    "United States in immediately available funds to the account designated by Lender in writing, not later than 2:00 p.m. Eastern "
    "Time on the date due. Any payment received after that time shall be deemed received on the next Business Day, and interest "
    "shall continue to accrue. All payments received shall be applied in the following order: (a) to Lender’s expenses and "
    "indemnified amounts then due, (b) to Fees then due, (c) to accrued and unpaid interest, (d) to principal, and (e) to any other "
    "amounts due under the Loan Documents; provided that following an Event of Default, Lender may apply payments in any order it "
    "elects in its sole discretion.")

section(doc, "2.10", "Prepayment; Exit Fee",
    "Borrower may prepay the Loan in whole or in part at any time, without premium or penalty other than the Exit Fee payable "
    "under Section 2.8(c) and any amounts payable under Section 2.14. Borrower shall give Lender not less than ten (10) Business "
    "Days’ prior written notice of any prepayment in full. Any partial prepayment shall be applied to the outstanding principal "
    "balance and shall not relieve Borrower of the obligation to pay interest and Fees thereafter accruing, and shall not entitle "
    "Borrower to reborrow. Amounts deposited by Borrower in the Interest Reserve Account or the Interest Reserve Contingency "
    "Escrow shall not constitute prepayments.")

section(doc, "2.11", "Default Rate",
    "Upon the occurrence and during the continuance of an Event of Default, the outstanding principal balance of the Loan and, to "
    "the extent permitted by applicable law, all accrued and unpaid interest, Fees and other amounts shall bear interest at the "
    "Default Rate, payable on demand. Application of the Default Rate shall not constitute a waiver of any Event of Default or "
    "limit Lender’s remedies.")

section(doc, "2.12", "Computation of Interest; Maximum Rate",
    "Notwithstanding anything to the contrary in any Loan Document, in no event shall the aggregate of all amounts that constitute "
    "interest under applicable law exceed the Maximum Rate. If any amount in excess of the Maximum Rate is received by Lender, "
    "(a) such amount shall be applied to reduce the principal balance of the Loan or, if the principal balance has been paid in full, "
    "refunded to Borrower, and (b) the effective rate of interest shall be automatically reduced to the Maximum Rate. To the extent "
    "permitted by law, all amounts that are not “interest” under applicable law shall be excluded from the computation of interest. "
    "The parties intend to conform strictly to applicable usury laws, including N.C.G.S. § 24-1.1 et seq.")

section(doc, "2.13", "Maturity; Extension Option", "")
rich(doc, [("(a)  Maturity.", {"bold": True}),
    ("  The entire outstanding principal balance of the Loan, together with all accrued and unpaid interest, Fees and other amounts, shall "
     "be due and payable on the Maturity Date.")],
    first_indent=0.0, space_after=6)
rich(doc, [("(b)  Conversion to Mini-Perm Period.", {"bold": True}),
    ("  On the Construction Maturity Date, provided that no Default or Event of Default then exists, the Loan shall automatically convert "
     "to the Mini-Perm Period and the Applicable Spread shall increase to 3.50% per annum. If a Default or Event of Default exists on the "
     "Construction Maturity Date, Lender may, at its election, (i) decline to convert the Loan, in which case the entire outstanding "
     "principal balance together with all accrued interest, Fees and other amounts shall be immediately due and payable, or (ii) permit "
     "conversion subject to such conditions as Lender may impose in writing. Conversion of the Loan shall not constitute a waiver of any "
     "Default or Event of Default.")],
    first_indent=0.0, space_after=6)
rich(doc, [("(c)  Extension Option.", {"bold": True}),
    ("  Borrower shall have one (1) option (the “Extension Option”) to extend the Mini-Perm Maturity Date by six (6) months, to "
     "February 28, 2029 (the “Extended Maturity Date”), subject to satisfaction of each of the following conditions on or before the "
     "Mini-Perm Maturity Date:")],
    first_indent=0.0, space_after=4)
EXT = [
("(i)", "no Default or Event of Default shall exist under the Loan Documents or the Intercreditor Agreement, and no condition shall exist that, with notice or lapse of time or both, would constitute such a Default or Event of Default;"),
("(ii)", "Substantial Completion shall have occurred and a final, unconditional certificate of occupancy shall have been issued by the City of Durham for all residential units and retail space within the Project;"),
("(iii)", "not less than 75% of the residential units shall be leased under executed leases having initial terms of not less than twelve (12) months and physically occupied as of the date of Borrower’s notice of exercise;"),
("(iv)", "the Debt Service Coverage Ratio, calculated on the basis of in-place annualized net operating income for the trailing three (3) month period divided by annual debt service on the outstanding principal balance at the Applicable Rate then in effect, shall be not less than 1.15x;"),
("(v)", "Borrower shall have paid the Extension Fee;"),
("(vi)", "Borrower shall have delivered evidence of an interest rate cap agreement for the extended period, with a strike rate, notional amount and counterparty (having a long-term credit rating of not less than “A-” from S&P Global Ratings or “A3” from Moody’s Investors Service) reasonably satisfactory to Lender;"),
("(vii)", "the Intercreditor Agreement shall be in full force and effect and no default shall exist thereunder;"),
("(viii)", "Lender shall have received an updated appraisal from an MAI-designated appraiser acceptable to Lender confirming that the Loan-to-Value Ratio (on the basis of the as-stabilized appraised value and the outstanding principal balance) does not exceed 65.00%, consistent with Section 8.2;"),
("(ix)", "all representations and warranties in the Loan Documents shall be true and correct in all material respects; and"),
("(x)", "Borrower shall have delivered written notice of its election to exercise the Extension Option not less than sixty (60) days prior to the Mini-Perm Maturity Date."),
]
for lbl, txt in EXT:
    sub(doc, lbl, txt, level=1, size=10.5)
rich(doc, [("Time is of the essence with respect to each condition in this Section 2.13(c). If any condition is not satisfied, the "
            "Extension Option shall lapse and the entire outstanding principal balance shall be due and payable on the Mini-Perm Maturity Date.")],
    first_indent=0.0, space_after=6)
note(doc, "[Note to Draft: The Credit Memorandum (Section 11) recommends these ten conditions. Borrower may be expected to seek a lower "
          "occupancy threshold and a longer notice period, on the ground that the appraisal projects stabilization only in approximately May 2028 "
          "(nine months after the projected August 2027 substantial completion), which leaves little margin before the August 28, 2028 mini-perm "
          "maturity. The 75% occupancy and 1.15x conditions are, on the appraiser’s absorption assumptions, achievable but not comfortable. "
          "Condition (viii) is stated at 65.00%, consistent with Section 8.2 and Term Sheet Section 6.2; the Credit Memorandum (Section 11(h)) states "
          "70.00%, which is inconsistent with the as-stabilized Loan-to-Value covenant and would permit an extension while the Loan is in breach of "
          "Section 8.2. See Memorandum Sections 3.8 and 3.9.]")

section(doc, "2.14", "Increased Costs; Illegality; Taxes",
    "If, after the Effective Date, any change in applicable law or regulation (or in its interpretation or administration) or any change "
    "in the capital adequacy or liquidity requirements applicable to Lender shall impose on Lender any cost or reduction in return "
    "that Lender determines to be attributable to the Loan, Borrower shall pay to Lender such additional amounts as Lender determines "
    "are necessary to compensate Lender therefor, within thirty (30) days after written demand accompanied by a certificate setting "
    "forth the calculation. If Lender determines that it has become unlawful for Lender to maintain or fund the Loan based on Daily "
    "Simple SOFR, Lender may convert the interest basis to the Benchmark Replacement or to another lawful basis reasonably selected "
    "by Lender, and Borrower may prepay the Loan in full without payment of the Exit Fee within sixty (60) days thereafter. Borrower "
    "shall pay all amounts required to be withheld or deducted from any payment under the Loan Documents under applicable tax law, "
    "and shall pay such additional amounts as are necessary to ensure that Lender receives the amount it would have received absent "
    "such withholding, other than withholding resulting from Lender’s own failure to provide appropriate tax forms.")

section(doc, "2.15", "No Reborrowing; Termination of Commitment",
    "No amount repaid or prepaid may be reborrowed. The Commitment Amount shall terminate automatically, without further act of the "
    "parties, on the Construction Maturity Date (as to any unadvanced amounts other than the Retainage release and amounts deposited "
    "by Borrower). Any unadvanced portion of the Commitment Amount on such date shall cease to be available to Borrower.")

# ================================================================ ARTICLE III
article(doc, "III", "Conditions Precedent to Closing")
para(doc, "Lender’s obligation to make the initial Advance is subject to the satisfaction (or written waiver by Lender) of each of "
          "the following conditions on or before the Closing Date, each in form and substance satisfactory to Lender and its counsel:",
     first_indent=0.5)

section(doc, "3.1", "Loan Documents",
    "Execution and delivery by Borrower and each Guarantor, as applicable, of this Agreement, the Note, the Deed of Trust, the "
    "Assignment of Rents, the Security Agreement, the Pledge Agreements, the Completion Guaranty, the Carry Guaranty, the Partial "
    "Repayment Guaranty, the Environmental Indemnity, the Intercreditor Agreement, the collateral assignments of the Construction "
    "Contract and the Architect’s Contract, the Equity Escrow Agreement and each other Loan Document, each duly executed, acknowledged "
    "where required and, where applicable, in recordable form.")

section(doc, "3.2", "Title Insurance and Survey", "")
rich(doc, [("(a)  Title.", {"bold": True}),
    ("  Lender shall have received a pro forma lender’s title insurance policy (ALTA Loan Policy, 2006 form, as modified by the current "
     "North Carolina promissory note and survey endorsements) issued by Title Company in an amount not less than the Commitment Amount, "
     "insuring the Deed of Trust as a valid first-priority Lien on the fee simple estate in the Property, subject only to the Permitted "
     "Exceptions, and including such endorsements as Lender may require (including, without limitation, access, contiguity, survey, "
     "zoning (with parking), location, separate tax lot, usury, doing business, environmental protection lien (to the extent available), "
     "and, if available in North Carolina, creditors’ rights and non-imputation endorsements).")],
    first_indent=0.0, space_after=6)
rich(doc, [("(b)  Release of the Existing Mortgage.", {"bold": True}),
    ("  The Existing Mortgage shall be satisfied and released of record at or prior to Closing in accordance with Section 3.8, and the "
     "title policy shall contain no exception for the Existing Mortgage.")],
    first_indent=0.0, space_after=6)
rich(doc, [("(c)  Survey.", {"bold": True}),
    ("  Lender and Title Company shall have received an ALTA/NSPS Land Title Survey of the Property, prepared by a surveyor licensed in "
     "North Carolina, dated or re-certified within ninety (90) days of the Closing Date, certified to Lender, Borrower and Title Company, "
     "meeting the 2021 ALTA/NSPS Minimum Standard Detail Requirements and including such Table A optional items as Lender may specify "
     "(including items 1, 2, 3, 4, 6(b), 7(a), 7(b)(1), 8, 9, 10, 11, 13, 14, 15 and 16, to the extent applicable). The survey shall "
     "depict both parcels on a single sheet, shall confirm the area of each parcel and the aggregate area, and shall confirm that the "
     "Parcel 1 and Parcel 2 boundary is a common line of record.")],
    first_indent=0.0, space_after=6)
rich(doc, [("(d)  Boundary Resolution.", {"bold": True}),
    ("  If the survey discloses a gap, overlap, discrepancy or boundary line conflict between Parcel 1 and Parcel 2, Borrower shall, at its "
     "sole cost, deliver a boundary line agreement, quitclaim deed, corrected legal description or other instrument (executed by Borrower "
     "and each affected adjoining owner) sufficient to permit Title Company to delete the survey exception and to insure the Property as a "
     "single, contiguous and unified site, and Lender shall have received a revised legal description conforming to the survey for "
     "attachment as Exhibit A.")],
    first_indent=0.0, space_after=6)
rich(doc, [("(e)  Owner’s Affidavit; No Pre-Closing Work.", {"bold": True}),
    ("  Lender and Title Company shall have received an owner’s affidavit and a contractor’s affidavit, in each case in form satisfactory "
     "to Title Company, confirming (i) that the Land is vacant and unoccupied, and (ii) the status and payment of all work performed and "
     "materials furnished to the Property prior to Closing, together with conditional lien waivers for all such work and materials, so as "
     "to permit the deletion of the survey and mechanics’ lien exceptions and to address the relation-back provisions of N.C.G.S. § 44A-10.")],
    first_indent=0.0, space_after=6)
note(doc, "[Note to Draft: The legal descriptions in the December 5, 2024 title commitment describe Parcel 1 with a southern boundary of "
          "305.41 feet and Parcel 2 with a northern boundary of 297.63 feet along what is stated to be the same line — a 7.78-foot discrepancy. "
          "The commitment also states parcel areas of 2.09 and 1.38 acres, whereas the Phase I ESA states 1.89 and 1.58 acres. These matters "
          "must be resolved by survey before the Deed of Trust is recorded. See Memorandum Sections 4.2 and 4.3.]")

section(doc, "3.3", "Appraisal",
    "Lender shall have received an appraisal of the Property dated November 15, 2024 prepared by Ridgeline Appraisal Services Inc. "
    "(Linda M. Haverford, MAI) complying with the requirements of FIRREA and the applicable regulations of the Office of the Comptroller "
    "of the Currency and Lender’s appraisal policy, concluding to (a) an as-is land value of not less than $8,900,000, (b) an as-completed "
    "value of not less than $72,800,000, and (c) an as-stabilized value of not less than $76,200,000. The appraisal shall be subject to "
    "review and confirmation by Lender’s appraisal review department, and Lender shall have received a written confirmation that the "
    "appraisal remains current and valid as of the Closing Date.")

section(doc, "3.4", "Environmental Conditions",
    "")
rich(doc, [("(a)  Reports.", {"bold": True}),
    ("  Lender shall have received (i) the Phase I ESA, together with a reliance letter addressed to Lender dated October 28, 2024, and "
     "(ii) the Phase II Report, together with a reliance letter addressed to Lender, in each case in form and substance satisfactory to "
     "Lender.")],
    first_indent=0.0, space_after=6)
rich(doc, [("(b)  NFA Letter.", {"bold": True}),
    ("  Lender shall have received a complete copy of the NFA Letter (including all attachments, the delineation of the Affected Area and "
     "the form of Deed Notice) and evidence satisfactory to Lender that each condition of the NFA Letter is satisfied, or will be satisfied "
     "in accordance with the compliance schedule set forth on Exhibit F.")],
    first_indent=0.0, space_after=6)
rich(doc, [("(c)  Deed Notice.", {"bold": True}),
    ("  Borrower shall have delivered to Lender (i) evidence that the Deed Notice was recorded in the Durham County Registry of Deeds on or "
     "before November 29, 2024 (being sixty (60) days after the date of the NFA Letter), or (ii) if the Deed Notice was not timely recorded, "
     "(A) evidence of recordation prior to Closing, (B) written acknowledgment from NCDEQ that the late recordation does not affect the "
     "status of the NFA Letter, and (C) a title date-down endorsement disclosing the Deed Notice as an exception to title.")],
    first_indent=0.0, space_after=6)
rich(doc, [("(d)  Vapor Mitigation System Design.", {"bold": True}),
    ("  Lender shall have received the design for the Vapor Mitigation System, prepared by a professional engineer licensed in North Carolina "
     "and approved by NCDEQ, together with evidence that such design is incorporated into the Approved Plans and the Construction Contract "
     "and that the cost thereof is included in the Approved Budget.")],
    first_indent=0.0, space_after=6)
rich(doc, [("(e)  Soil Management Plan.", {"bold": True}),
    ("  Lender shall have received the Soil Management Plan as approved (or submitted for approval) by NCDEQ, together with evidence that "
     "the Soil Management Plan has been incorporated into the Construction Contract and the construction specifications.")],
    first_indent=0.0, space_after=6)
rich(doc, [("(f)  Affected Area Use Restriction.", {"bold": True}),
    ("  Lender shall have received either (i) a written modification of the NFA Letter issued by NCDEQ permitting residential use of the "
     "floors constructed above the Affected Area, subject to the installation, operation and maintenance of the Vapor Mitigation System and "
     "such other engineering controls as NCDEQ may require; or (ii) written confirmation from NCDEQ, in form and substance satisfactory to "
     "Lender, that residential occupancy of enclosed space above the Affected Area is not prohibited by the NFA Letter or the recorded land "
     "use restriction, provided the Vapor Mitigation System is installed and maintained; or (iii) evidence that the Approved Plans have been "
     "redesigned so that no residential unit, and no other “sensitive use” as defined by NCDEQ, is located above the Affected Area.")],
    first_indent=0.0, space_after=6)
rich(doc, [("(g)  Phase I Currency.", {"bold": True}),
    ("  If the Closing Date occurs after April 26, 2025 (being 180 days after the date of the Phase I ESA), Borrower shall have delivered an "
     "update to the Phase I ESA satisfying 40 C.F.R. § 312.20(c)(2) and a reliance letter with respect thereto.")],
    first_indent=0.0, space_after=6)
note(doc, "[Note to Draft: Section 3.4(f) is drafted as an alternative because neither the Phase I ESA nor the appraisal confirms that "
          "residential units are in fact located above the Affected Area. The Phase I ESA (Section 8.5 and Recommendation 1) expressly declined "
          "to make that determination, while the Credit Memorandum (Sections 8.2 and 9.5) asserts that 14 units sit above the affected area. The "
          "architect’s overlay must be delivered before this condition can be finally drafted. See Memorandum Section 3.5.]")

section(doc, "3.5", "Intercreditor Agreement",
    "Lender, Mezzanine Lender and Borrower shall have executed and delivered the Intercreditor Agreement, which shall contain each of "
    "the provisions described in Section 12.3, and Lender shall have received evidence that all conditions precedent to the effectiveness "
    "of the Intercreditor Agreement (other than the Closing) have been satisfied. The Intercreditor Agreement is a condition that may not "
    "be waived by Borrower or by any officer or employee of Lender other than in accordance with Section 15.16.")

section(doc, "3.6", "Single-Purpose Entity Amendments; Independent Manager; Non-Consolidation Opinion",
    "")
rich(doc, [("(a)  Operating Agreement.", {"bold": True}),
    ("  Borrower’s Amended and Restated Operating Agreement shall have been further amended (with all member consents required under "
     "Section 3.2 thereof) to incorporate each of the single-purpose entity covenants set forth in Article XI, to provide for the "
     "appointment of the Independent Manager and the bankruptcy limitations set forth in Section 11.4, and to delete or subordinate the "
     "member approval rights that would otherwise permit any member (including Brightleaf Investors Group LLC) to block a refinancing, "
     "sale, or other action approved by Lender under the Loan Documents. Lender shall have received a certified copy of such amendment "
     "and all member consents.")],
    first_indent=0.0, space_after=6)
rich(doc, [("(b)  Independent Manager.", {"bold": True}),
    ("  The Independent Manager shall have been appointed, shall have accepted such appointment in writing, and Borrower shall have "
     "delivered a certificate of the Managing Member confirming the Independent Manager’s independence in accordance with the definition "
     "in Section 1.1.")],
    first_indent=0.0, space_after=6)
rich(doc, [("(c)  Non-Consolidation Opinion.", {"bold": True}),
    ("  Borrower’s counsel (Calloway & Strauss PLLC) shall have delivered a substantive non-consolidation opinion addressed to Lender and "
     "reasonably satisfactory to Lender and its counsel, opining that, subject to customary assumptions and qualifications, a court "
     "applying North Carolina law would not order the substantive consolidation of the assets and liabilities of Borrower with those of "
     "Brightleaf Investors Group LLC, Brightleaf Mezzanine Capital LLC, Thomas R. Chen, Elena Vasquez-Torres or any other Affiliate in a "
     "case under the United States Bankruptcy Code.")],
    first_indent=0.0, space_after=6)

section(doc, "3.7", "Equity Contribution; LTC Equity Deposit", "")
rich(doc, [("(a)  Deposit.", {"bold": True}),
    ("  Borrower shall have deposited the LTC Equity Deposit of $2,140,000 with Lender in the Equity Escrow Account, to be disbursed in "
     "accordance with Section 4.5 and the Equity Escrow Agreement.")],
    first_indent=0.0, space_after=6)
rich(doc, [("(b)  Additional Borrower Funds.", {"bold": True}),
    ("  Borrower shall have deposited the Interest Reserve Contingency Escrow of $500,000 required under Section 2.7(e).")],
    first_indent=0.0, space_after=6)
rich(doc, [("(c)  Source Verification.", {"bold": True}),
    ("  Lender shall have received evidence satisfactory to it that the funds described in Sections 3.7(a) and 3.7(b) are derived from "
     "sources other than the Mezzanine Loan, Brightleaf Mezzanine Capital LLC, Brightleaf Investors Group LLC, Thomas R. Chen, or any "
     "entity under common control with any of the foregoing, such evidence to include (i) three (3) months of account statements for each "
     "source account, (ii) a source-of-funds certification executed by the contributing member or members, and (iii) such other "
     "documentation as Lender may reasonably request for purposes of its customer due diligence and beneficial ownership requirements.")],
    first_indent=0.0, space_after=6)
rich(doc, [("(d)  Verification of the Land Contribution.", {"bold": True}),
    ("  Lender shall have received evidence satisfactory to it of the actual acquisition of the Land by Borrower, including (i) the "
     "recorded Special Warranty Deed(s) conveying the Land to Borrower, (ii) the settlement statement for such acquisition, (iii) evidence "
     "of the source of the funds used to acquire the Land, (iv) the capital account records of Borrower reflecting the contribution of the "
     "Land and the Contribution Value, and (v) a certificate of the Managing Member as to the date of acquisition, the identity of the "
     "transferor, the total acquisition cost and the outstanding balance of the Existing Mortgage. If the evidence so delivered is "
     "inconsistent with the Contribution Value stated in Section 1.1, the Contribution Value and Total Project Costs shall be adjusted "
     "accordingly and Borrower shall make such additional equity contribution as is necessary to satisfy Section 8.1.")],
    first_indent=0.0, space_after=6)
rich(doc, [("(e)  No Circular Funding.", {"bold": True}),
    ("  Lender shall have received a certificate of the Managing Member that no portion of Borrower’s equity contribution consists of, or "
     "is derived from, the proceeds of the Mezzanine Loan, any other Indebtedness of Borrower, or any distribution from Borrower.")],
    first_indent=0.0, space_after=6)
note(doc, "[Note to Draft: The record is internally inconsistent as to the acquisition and funding of the Land. The title commitment shows "
          "a Special Warranty Deed from Foster Street Properties LLC recorded June 12, 2023; the Organizational Chart and Operating Agreement "
          "state that Ms. Vasquez-Torres contributed the Land in exchange for her 62% interest; the Credit Memorandum states that the Land was "
          "acquired through capital calls from all three members; the Phase I ESA states that Borrower acquired the Land in 2022; and the "
          "appraisal states that Borrower paid $8,200,000 in early 2024. Separately, the Borrower’s budget and draw schedule state that the "
          "Land was funded by $8,200,000 of Mezzanine Loan proceeds. These statements cannot all be correct. See Memorandum Section 3.1.]")

section(doc, "3.8", "Payoff of Existing Mortgage",
    "Lender shall have received (a) a payoff letter from Triangle Commercial Bank (or its successor or assign) dated not more than "
    "thirty (30) days prior to the Closing Date, setting forth the outstanding principal balance, accrued interest, per diem, prepayment "
    "premium (if any), and all other amounts required to satisfy the Existing Mortgage in full; (b) evidence that funds sufficient to pay "
    "such amounts have been deposited with Title Company for disbursement at Closing (which funds shall be identified as a separate use of "
    "funds in the closing statement and in the Approved Budget); and (c) either a recorded cancellation of the Existing Mortgage executed "
    "in accordance with N.C.G.S. § 45-37, or a certificate of satisfaction in recordable form, or an indemnity agreement from Title "
    "Company acceptable to Lender. The amount required to satisfy the Existing Mortgage is not included in the Total Project Costs set forth "
    "on Exhibit C, and the sources and uses of funds at Closing shall be conformed to include such payoff and the source of the funds "
    "applied to it.")
note(doc, "[Note to Draft: The $56,700,000 Approved Budget contains no line item for the payoff of the $3,400,000 Existing Mortgage, and no "
          "source of funds is identified for it. Borrower’s counsel has advised Title Company that the loan has been partially repaid and will "
          "be satisfied at closing. This is a material unbudgeted use. See Memorandum Section 3.3.]")

section(doc, "3.9", "Construction Contract; Architect’s Contract; Bonding",
    "")
rich(doc, [("(a)  GMP Contract.", {"bold": True}),
    ("  Lender shall have received a fully executed copy of the Construction Contract (including all exhibits, the guaranteed maximum price "
     "and the contract documents), together with a collateral assignment thereof in favor of Lender, a consent and recognition agreement "
     "executed by General Contractor, and evidence that the guaranteed maximum price is $34,750,000.")],
    first_indent=0.0, space_after=6)
rich(doc, [("(b)  Architect’s Contract.", {"bold": True}),
    ("  Lender shall have received a fully executed copy of the Architect’s Contract, a collateral assignment thereof in favor of Lender, and "
     "a consent and recognition agreement executed by Architect, together with a certificate of professional liability insurance in the "
     "amount of not less than $2,000,000.")],
    first_indent=0.0, space_after=6)
rich(doc, [("(c)  Contractor Diligence.", {"bold": True}),
    ("  Lender shall have received (i) General Contractor’s financial statements for the two most recent fiscal years and the most recent "
     "interim period, (ii) evidence of General Contractor’s bonding capacity, and (iii) a performance and payment bond (AIA A312 or "
     "equivalent) in the amount of 100% of the guaranteed maximum price, issued by a surety acceptable to Lender, unless Lender expressly "
     "waives such bond in writing.")],
    first_indent=0.0, space_after=6)

section(doc, "3.10", "Insurance; Flood Determination",
    "Lender shall have received certificates of insurance and, upon request, certified copies of each policy evidencing the coverages "
    "required under Section 9.1, each in form and substance satisfactory to Lender, together with a life-of-loan Standard Flood Hazard "
    "Determination and, if any portion of the Property is located in a Special Flood Hazard Area, evidence of flood insurance in the "
    "amount required by applicable law.")

section(doc, "3.11", "Organizational Documents; Authority",
    "Lender shall have received (a) certificates of good standing (or existence) for Borrower, General Contractor and each Guarantor "
    "entity, as applicable, issued by the North Carolina Secretary of State within thirty (30) days of the Closing Date; (b) certified "
    "copies of Borrower’s Articles of Organization and Amended and Restated Operating Agreement (including the amendments described in "
    "Section 3.6); (c) resolutions or written consents of the members of Borrower, executed by members holding not less than seventy-five "
    "percent (75%) of the membership interests (including Brightleaf Investors Group LLC), authorizing the Loan, the execution and "
    "delivery of the Loan Documents, the granting of the Liens, the pledge of the Pledged Interests and the transactions contemplated "
    "hereby; (d) a certificate of incumbency and specimen signatures; and (e) evidence of the authority of each Guarantor to execute the "
    "Guaranties.")

section(doc, "3.12", "Zoning, Permits and Declaration Approval",
    "Lender shall have received (a) a zoning compliance letter from the City of Durham confirming that the Project as designed is a "
    "permitted use in the MU-D district, complies with applicable height, floor area ratio, setback and open space requirements, and "
    "complies with any applicable maximum parking limitation; (b) evidence of all building permits required for the commencement of "
    "construction, or a permit schedule reasonably satisfactory to Lender; (c) evidence that all public art, tree preservation, "
    "stormwater and other development conditions imposed by the Durham Unified Development Ordinance have been satisfied or are included "
    "in the Approved Budget; and (d) either (i) written approval of the Project by the Architectural Review Committee of the Brightleaf "
    "Historic District Association, Inc., (ii) evidence that the sixty (60) day deemed-approval period under Article V of the Declaration "
    "(Book 6984, Page 1155, as amended by Book 7102, Page 388, Durham County Registry) has expired without written action by the "
    "Committee, or (iii) a written opinion of Borrower’s counsel, reasonably satisfactory to Lender, that the Declaration does not apply "
    "to the Project.")
note(doc, "[Note to Draft: The appraisal (Section 2) states that the design “has been reviewed and approved by the Brightleaf Historic "
          "District Association in accordance with the CC&Rs,” while the title commitment (Schedule B-II, item 11, Title Officer’s Note) states "
          "that no evidence of submission or approval has been furnished to Title Company. Approval status must be confirmed directly with the "
          "Association. See Memorandum Section 4.4.]")

section(doc, "3.13", "Financial Condition of Borrower and Guarantors",
    "Lender shall have received (a) current financial statements of Borrower, certified by the Managing Member, demonstrating net worth "
    "of not less than $12,000,000 computed in accordance with Section 8.4 and with the assets and liabilities of Borrower identified "
    "separately (including the carrying value of the Land, the accrued Developer Fee and all intercompany and member balances); (b) the "
    "personal financial statements of each Guarantor dated not earlier than December 15, 2024, together with supporting statements for "
    "each material asset; (c) federal income tax returns for the two most recent taxable years of Borrower and each Guarantor; and "
    "(d) evidence that combined Guarantor liquidity is not less than $5,000,000.")

section(doc, "3.14", "Legal Opinions",
    "Lender shall have received opinions of Borrower’s counsel (Calloway & Strauss PLLC) addressed to Lender and satisfactory to Lender "
    "and its counsel as to due organization, valid existence, due authorization, execution and delivery, enforceability of the Loan "
    "Documents, the security interests granted thereunder, the non-consolidation opinion required by Section 3.6(c), and such other "
    "matters as Lender may reasonably require.")

section(doc, "3.15", "Fees and Expenses",
    "Borrower shall have paid (a) the Origination Fee, (b) all fees and expenses of Lender’s counsel and the third-party consultants "
    "required to be paid at Closing, (c) the premiums for the title policy and all endorsements, and (d) all recording and filing fees, "
    "in each case net of the $75,000 expense deposit previously paid by Borrower under Section 22 of the Term Sheet, to the extent such "
    "deposit has been received by Lender.")

section(doc, "3.16", "Mezzanine Loan Documentation and Certification",
    "Lender shall have received (a) true, correct and complete copies of each Mezzanine Document, including all amendments and "
    "restatements; (b) a disbursement history of the Mezzanine Loan showing each advance made to date, the amount applied to the "
    "acquisition of the Land (if any), and the outstanding principal balance including capitalized or paid-in-kind interest as of the "
    "Closing Date; (c) a certificate of Mezzanine Lender as to the outstanding principal balance and the amount of undrawn commitment; "
    "(d) an intercreditor-compliant UCC, Lien and judgment search with respect to Borrower and each Pledged Interest; and "
    "(e) evidence that the Mezzanine Lender has not declared a default under the Mezzanine Documents.")

section(doc, "3.17", "Due Diligence Currency",
    "If the Closing Date occurs after June 5, 2025, Lender shall have received an extension or re-issuance of the title commitment "
    "(Commitment No. NC-2024-88712) and a date-down endorsement through the Closing Date. If the Closing Date occurs after April 26, "
    "2025, the Phase I ESA update required by Section 3.4(g) shall have been delivered.")

section(doc, "3.18", "Additional Conditions",
    "Lender shall have received such other documents, certificates, opinions, consents and information as Lender or its counsel may "
    "reasonably require, all in form and substance satisfactory to Lender.")

# ================================================================ ARTICLE IV
article(doc, "IV", "Advances; Disbursement Mechanics")

section(doc, "4.1", "Draw Schedule",
    "Advances shall be made in accordance with the Approved Draw Schedule attached as Exhibit D, which is tied to the construction "
    "milestones described therein. Each Advance shall be in the amount set forth in Exhibit D for the applicable milestone, subject to "
    "retention of the Retainage in accordance with Section 4.4 and to the adjustments contemplated by Section 2.2 and Section 4.6. If "
    "the Commitment Amount is reduced pursuant to Section 2.2, Exhibit D shall be conformed as provided in Section 2.2(b) and in Exhibit D. "
    "Lender shall not be obligated to make any Advance in excess of the amount then available under Exhibit D, and Borrower shall not be "
    "entitled to any Advance for a milestone that has not been achieved and certified in accordance with this Article IV.")
note(doc, "[Note to Draft: Exhibit D conforms the draw schedule to the 10% Retainage requirement and to the funding of the Developer Fee from "
          "senior and mezzanine sources. The schedule as presented in the Term Sheet (Section 9.2) and the Credit Memorandum (Section 7.1) "
          "disburses 100% of the $34,750,000 guaranteed maximum price in Draws 2 through 8 and then “releases” $3,275,000 of Retainage in Draw 9 "
          "that was never withheld, and its Draw 9 components do not foot ($4,275,000 of components against a stated $3,275,000). See "
          "Memorandum Section 3.6 and Exhibit D hereto.]")

section(doc, "4.2", "Draw Requests",
    "Borrower shall submit each Draw Request to Lender not less than fifteen (15) days prior to the proposed Advance date, in the form "
    "attached as Exhibit G, accompanied by:")
DRAWREQ = [
("(a)", "an AIA Application and Certificate for Payment (Form G702) and Continuation Sheet (Form G703), certified by Architect and General Contractor;"),
("(b)", "a current construction progress report and updated construction schedule, certified by Borrower and General Contractor;"),
("(c)", "a certification from the Construction Inspector confirming achievement of the applicable milestone and the percentage of completion stated in the Draw Request;"),
("(d)", "conditional and unconditional partial lien waivers, in the statutory form prescribed by N.C.G.S. Chapter 44A, from General Contractor and each subcontractor and materialman for work performed and materials furnished through the date of the Draw Request;"),
("(e)", "a title date-down endorsement from Title Company confirming the continued first-priority status of the Deed of Trust and the absence of any intervening Lien;"),
("(f)", "evidence that all insurance required under Article IX remains in full force and effect;"),
("(g)", "a budget reconciliation demonstrating that the remaining undisbursed Loan proceeds, the LTC Equity Deposit and Borrower’s other committed funds are sufficient to complete the Project in accordance with the Approved Budget;"),
("(h)", "a Borrower’s certificate that no Default or Event of Default exists, that all representations and warranties remain true and correct in all material respects, and that the Interest Reserve adequacy test required by Section 2.7(c) has been satisfied; and"),
("(i)", "such other documentation as Lender may reasonably require."),
]
for lbl, txt in DRAWREQ:
    sub(doc, lbl, txt, level=1, size=10.5)

section(doc, "4.3", "Conditions to Each Advance",
    "Lender’s obligation to make any Advance (including the initial Advance) is subject to the satisfaction (or written waiver by "
    "Lender) of each of the following conditions as of the date of such Advance:")
ADVC = [
("(a)", "all conditions precedent to Closing set forth in Article III shall have been satisfied or waived in writing;"),
("(b)", "no Default or Event of Default shall exist, and no condition shall exist that with notice or lapse of time or both would constitute a Default or Event of Default;"),
("(c)", "all representations and warranties of Borrower and each Guarantor in the Loan Documents shall be true and correct in all material respects;"),
("(d)", "Lender shall have received a complete Draw Request complying with Section 4.2 and a satisfactory report from the Construction Inspector;"),
("(e)", "the Interest Reserve adequacy test described in Section 2.7(c) shall have been satisfied, or Borrower shall have deposited the required deficiency;"),
("(f)", "the LTC Equity Deposit shall have been fully disbursed and applied to Project costs before any Advance other than the initial Advance, except as otherwise provided in the Equity Escrow Agreement;"),
("(g)", "no Material Adverse Effect shall have occurred;"),
("(h)", "all permits, approvals and the architectural review approvals described in Section 3.12 shall remain in full force and effect;"),
("(i)", "each condition of the NFA Letter applicable to the stage of construction then underway shall have been satisfied, and the Vapor Mitigation System shall have been installed in accordance with Section 10.4 before any Advance is made for work above the podium level in the Affected Area; and"),
("(j)", "the Intercreditor Agreement shall remain in full force and effect and no default shall exist thereunder."),
]
for lbl, txt in ADVC:
    sub(doc, lbl, txt, level=1, size=10.5)

section(doc, "4.4", "Retainage",
    "Lender shall retain ten percent (10%) of each Advance attributable to hard construction costs (the “Retainage”), which for the "
    "Project equals $3,475,000. The Retainage shall be held by Lender and released as Draw 9 under Exhibit D, and only upon Lender’s "
    "receipt of (a) a final, unconditional certificate of occupancy issued by the City of Durham for all residential units and retail "
    "space; (b) final, unconditional lien waivers from General Contractor, each subcontractor and each materialman; (c) Architect’s "
    "certificate of final completion; (d) evidence of the expiration of the lien filing period under N.C.G.S. Chapter 44A (being 120 days "
    "from the date of last furnishing of labor or materials to the Property) or, in the alternative, the posting of a lien bond in form and "
    "amount satisfactory to Lender; (e) a final title date-down endorsement; and (f) evidence of compliance with each condition of the "
    "NFA Letter. Lender may, in its discretion, apply all or any portion of the Retainage to cure any Default, to complete any incomplete "
    "work, or to pay any Lien asserted against the Property.")

section(doc, "4.5", "Equity First",
    "Borrower’s equity in the Project, consisting of the Land (at the Contribution Value) and the LTC Equity Deposit, shall be fully "
    "invested in the Project before any Advance other than the initial Advance is made. Lender shall disburse the LTC Equity Deposit "
    "in accordance with the Equity Escrow Agreement and prior to, and in any event not later than the corresponding, Advances of Loan "
    "proceeds. Borrower shall not be entitled to any reimbursement of its equity contribution from Loan proceeds.")

section(doc, "4.6", "Cost Overruns",
    "If at any time Lender determines that the undisbursed portion of the Loan, together with the undisbursed LTC Equity Deposit and "
    "Borrower’s other committed funds, is insufficient to complete the Project in accordance with the Approved Plans and the Approved "
    "Budget (a “Cost Overrun”), Lender shall notify Borrower, and Borrower shall, within ten (10) Business Days after such notice, deposit "
    "with Lender funds sufficient to fund such Cost Overrun. Funds deposited under this Section 4.6 shall be disbursed before any further "
    "Advance and shall not be repaid to Borrower except from amounts remaining after completion. Borrower shall not fund a Cost Overrun "
    "with the proceeds of the Mezzanine Loan, any other Indebtedness, or any Affiliate loan without Lender’s prior written consent. "
    "Borrower’s failure to fund a Cost Overrun shall constitute an Event of Default and shall entitle Lender to exercise its rights under "
    "the Completion Guaranty.")

section(doc, "4.7", "Inspections and Retainage of Advances",
    "Lender may, at Borrower’s expense, cause the Construction Inspector to inspect the Property and the Project prior to authorizing "
    "each Advance and at such other times as Lender may reasonably determine. Lender shall use commercially reasonable efforts to process "
    "each complete Draw Request within ten (10) Business Days after receipt. Lender may withhold any Advance, in whole or in part, if "
    "(a) the work covered by the Draw Request has not been completed in accordance with the Approved Plans, (b) the Construction "
    "Inspector’s report does not support the requested percentage of completion, (c) a Lien has been asserted against the Property, "
    "(d) the cost to complete exceeds the remaining sources of funds, or (e) any other condition in this Article IV has not been satisfied.")

section(doc, "4.8", "Lender Advances; Limitations",
    "If Borrower fails to perform any obligation required to be performed as a condition to an Advance, Lender may, at its option and "
    "after five (5) Business Days’ prior written notice to Borrower (or without notice if an Event of Default exists), perform such "
    "obligation or advance funds directly to the applicable contractor, subcontractor, materialman or governmental authority, and any "
    "amounts so advanced shall constitute part of the Obligations, shall bear interest at the Default Rate from the date advanced, and "
    "shall be secured by the Security Documents. Lender shall not be obligated to make any Advance (a) after the Construction Maturity "
    "Date except for the release of Retainage in accordance with Section 4.4, or (b) in excess of the Commitment Amount.")

section(doc, "4.9", "Advances Not a Waiver",
    "No Advance shall constitute a waiver of any condition, Default or Event of Default, whether or not known to Lender, and no Advance "
    "shall be deemed an approval of the work, materials or costs for which it is made.")

section(doc, "4.10", "Interest Reserve Account Mechanics",
    "Lender shall maintain the Interest Reserve Account on its books. On each interest payment date during the Construction Period, "
    "Lender shall apply funds in the Interest Reserve Account to accrued interest, and Borrower shall pay any deficiency in accordance "
    "with Section 2.7(d). Borrower hereby grants Lender a security interest in the Interest Reserve Account, the Interest Reserve "
    "Contingency Escrow and the Equity Escrow Account and all funds therein as additional collateral for the Obligations, and Lender may "
    "apply such funds upon the occurrence of an Event of Default. Lender shall provide Borrower with a monthly statement of the Interest "
    "Reserve Account.")

section(doc, "4.11", "Title Bring-Down",
    "Borrower shall cause Title Company to deliver a date-down endorsement to Lender with each Draw Request and at such other times as "
    "Lender may request, and shall bear the cost of such endorsements. If any endorsement discloses a Lien, encumbrance or other matter "
    "not constituting a Permitted Exception, Borrower shall, within ten (10) Business Days (or such shorter period as Lender may require), "
    "cause such matter to be removed, bonded over or otherwise addressed to Lender’s satisfaction.")

section(doc, "4.12", "Lien Waivers",
    "Borrower shall obtain and deliver to Lender conditional partial lien waivers with each Draw Request and unconditional partial lien "
    "waivers for the preceding period, in each case from General Contractor and each subcontractor and materialman having a contract "
    "with Borrower or General Contractor in excess of $50,000. Borrower shall not make any payment to General Contractor or any "
    "subcontractor for work that is not covered by a lien waiver delivered to Lender.")

section(doc, "4.13", "Change Orders",
    "Borrower shall not approve or permit any change order, change directive, field order or other modification of the Approved Plans or "
    "the Construction Contract without Lender’s prior written consent if such change (a) individually or in the aggregate exceeds "
    "$250,000, (b) reduces the scope, quality or quantity of the Improvements, (c) affects the structural, mechanical, electrical or "
    "life-safety systems, (d) affects the Vapor Mitigation System or any other element of the NFA compliance, or (e) would cause the "
    "Project to exceed the guaranteed maximum price or the Approved Budget. Borrower shall deliver a change order log with each monthly "
    "construction report. Change orders requiring Architectural Review Committee approval under the Declaration shall not be submitted "
    "for Lender’s consent until such approval (or deemed approval) has been obtained.")

section(doc, "4.14", "Sufficiency of Funds; Completion",
    "Borrower acknowledges that the Approved Budget and the Approved Draw Schedule are based on the guaranteed maximum price of the "
    "Construction Contract and that the Loan, together with the LTC Equity Deposit and Borrower’s other committed funds, is sufficient "
    "to complete the Project. Borrower shall complete the Project in accordance with the Approved Plans on or before the Completion Date "
    "(as defined in the Completion Guaranty), free and clear of all Liens other than Permitted Exceptions, and shall fund all costs of "
    "completion in excess of the Loan proceeds and Borrower’s committed funds.")

# ================================================================ ARTICLE V
article(doc, "V", "Representations and Warranties")
para(doc, "Borrower and each Guarantor, as to itself and (where applicable) as to Borrower and the Property, represent and warrant to "
          "Lender as of the Effective Date, the Closing Date and each date on which an Advance is made:", first_indent=0.5)

REPS = [
("5.1", "Organization; Existence; Authority",
 "Borrower is a limited liability company duly organized, validly existing and in good standing under the laws of the State of North "
 "Carolina, with full power and authority to own and operate the Property, to carry on its business as presently conducted and as "
 "proposed to be conducted, and to execute, deliver and perform its obligations under the Loan Documents. Each Guarantor has full legal "
 "capacity and authority to execute, deliver and perform the Guaranties. The execution, delivery and performance of the Loan Documents "
 "have been duly authorized by all requisite action of Borrower and its members and of each Guarantor, and do not conflict with, or "
 "result in a breach of, Borrower’s Articles of Organization or Operating Agreement, any judgment, order or decree, or any material "
 "agreement to which Borrower or any Guarantor is a party."),
("5.2", "Ownership and Capital Structure",
 "The membership interests in Borrower are held as set forth on Schedule 5.2, being 62% by Elena Vasquez-Torres, 28% by Brightleaf "
 "Investors Group LLC and 10% by Reginald K. Osei, and there are no other membership interests, options, warrants, convertible "
 "instruments, profits interests, phantom equity or other rights to acquire any interest in Borrower. Borrower has no subsidiaries. "
 "Thomas R. Chen controls, directly or indirectly, both Brightleaf Investors Group LLC and Mezzanine Lender. Except for the Pledged "
 "Interests and the pledge in favor of Mezzanine Lender described in Schedule 5.2, no membership interest in Borrower is subject to any "
 "pledge, Lien, option, right of first refusal or transfer restriction. The Land was acquired by Borrower on June 12, 2023 from Foster "
 "Street Properties LLC for a total acquisition cost of $8,200,000, funded as described in the certificate delivered under Section 3.7(d)."),
("5.3", "Title; Permitted Exceptions",
 "Borrower holds good, marketable and insurable fee simple title to the Property, free and clear of all Liens and encumbrances other "
 "than the Permitted Exceptions and the Deed of Trust. The Deed of Trust, when recorded, will constitute a valid first-priority Lien on "
 "the Property, subject only to the Permitted Exceptions. The Land consists of two contiguous parcels comprising approximately 3.47 "
 "acres in the aggregate, is a single, unified development site, and has direct access to a public right-of-way."),
("5.4", "No Litigation",
 "There is no action, suit, proceeding, arbitration, investigation or governmental inquiry pending or, to Borrower’s knowledge, "
 "threatened against Borrower, any Guarantor, any member of Borrower or the Property that, if adversely determined, would reasonably be "
 "expected to have a Material Adverse Effect, and neither Borrower nor any Guarantor is in default under any material agreement."),
("5.5", "Compliance with Laws; Zoning",
 "The Property and the Project comply, and will comply, in all material respects with all applicable laws, ordinances, rules, "
 "regulations and orders, including Environmental Laws, building codes, the Durham Unified Development Ordinance and the Declaration. "
 "The Property is zoned MU-D (Mixed Use — Downtown), and the Project as designed is permitted as of right without any variance, special "
 "use permit, conditional zoning or other discretionary approval, subject only to the issuance of building permits and the architectural "
 "review approval described in Section 3.12."),
("5.6", "Financial Statements",
 "The financial statements of Borrower and each Guarantor delivered to Lender are true, correct and complete in all material respects, "
 "have been prepared in accordance with GAAP (or, in the case of personal financial statements, on a basis consistently applied) and "
 "fairly present the financial condition of Borrower and such Guarantor as of the dates thereof and the results of operations for the "
 "periods then ended. Borrower’s net worth, computed in accordance with Section 8.4, is not less than $12,000,000 as of the Effective "
 "Date. There has been no material adverse change in the financial condition of Borrower or any Guarantor since the dates of such "
 "statements."),
("5.7", "No Default",
 "No Default or Event of Default exists, and no default or event of default exists under the Mezzanine Documents, the Construction "
 "Contract, the Architect’s Contract or any other material agreement to which Borrower is a party."),
("5.8", "Permits and Approvals",
 "All permits, licenses, approvals and authorizations necessary for the commencement of construction of the Project have been obtained "
 "or will be obtained prior to the commencement of the applicable phase of construction, and all such permits will be maintained in full "
 "force and effect. Borrower has not received any notice of violation, stop-work order or revocation with respect to any permit."),
("5.9", "Single-Purpose Entity",
 "Borrower is, and at all times since its formation has been, a single-purpose entity that has conducted no business other than the "
 "acquisition, development, construction, ownership and operation of the Project, and Borrower will maintain such status in accordance "
 "with Article XI. Borrower has no assets other than the Property and the other assets described in Article XI, and has no liabilities "
 "other than the Loan, the Mezzanine Loan, trade payables incurred in the ordinary course of business and the accrued Developer Fee."),
("5.10", "Environmental Representations",
 "Except as disclosed in the Phase I ESA, the Phase II Report and the NFA Letter: (a) no Hazardous Substances are present at, on, "
 "under or migrating from the Property in violation of Environmental Laws or in concentrations exceeding applicable NCDEQ standards for "
 "the intended use; (b) neither Borrower nor any Guarantor has received any notice of violation, request for information, demand, claim "
 "or order relating to Environmental Laws or Hazardous Substances at the Property; (c) there are no underground or aboveground storage "
 "tanks, asbestos-containing materials, polychlorinated biphenyls or lead-based paint at the Property, except as remediated or abated as "
 "described in the Phase I ESA; (d) all remediation, investigation and reporting obligations with respect to the Property have been "
 "completed except for the ongoing obligations described in the NFA Letter and on Exhibit F; (e) the Deed Notice has been recorded as "
 "described in Section 3.4(c); and (f) Borrower has not assumed, by contract or operation of law, any liability of any other Person "
 "under any Environmental Law. Borrower acknowledges that Lender is relying on these representations in making the Loan and in "
 "determining that Lender qualifies for the secured creditor exemption under CERCLA, 42 U.S.C. § 9601(20)(A)."),
("5.11", "Construction Documents; GMP Contract",
 "The copies of the Construction Contract, the Architect’s Contract and the Approved Plans delivered to Lender are true, correct and "
 "complete, and constitute the entire agreement between the parties with respect thereto. The guaranteed maximum price of $34,750,000 "
 "is inclusive of all general conditions, overhead, profit, the Vapor Mitigation System and all other work required by the Approved "
 "Plans. There are no pending or asserted claims, change orders or disputes under the Construction Contract or the Architect’s Contract."),
("5.12", "Insurance",
 "Borrower maintains, and will maintain, the insurance required under Article IX, and all such insurance is in full force and effect "
 "with insurers acceptable to Lender, with all premiums paid."),
("5.13", "Solvency",
 "Borrower is, and after giving effect to the Loan and the Mezzanine Loan will be, solvent, able to pay its debts as they become due, "
 "and possessed of property having a fair saleable value greater than its liabilities. Borrower is not entering into the Loan Documents "
 "with the intent to hinder, delay or defraud any creditor."),
("5.14", "Affiliate Transactions",
 "Borrower has not entered into any transaction with any Affiliate other than on arm’s-length terms for fair and reasonable "
 "consideration, except as disclosed in writing to Lender. The Developer Fee is the only fee payable to any Affiliate of Borrower in "
 "connection with the Project, and no other development, construction management, asset management, leasing, brokerage or guarantee fee "
 "is payable to any Affiliate of Borrower or any member of Borrower."),
("5.15", "Mezzanine Loan; Intercreditor Agreement",
 "The Mezzanine Loan is in the original principal amount of $9,200,000, bears interest at 12.50% per annum fixed, and matures on the "
 "Maturity Date. No default exists under the Mezzanine Documents, and no advance under the Mezzanine Loan has been applied to any "
 "purpose other than as disclosed to Lender in the certificate delivered under Section 3.16. The Intercreditor Agreement, when executed, "
 "will be in full force and effect and will constitute the legal, valid and binding obligation of Borrower and Mezzanine Lender."),
("5.16", "Anti-Money Laundering; OFAC; Beneficial Ownership",
 "Neither Borrower, any Guarantor, any member of Borrower nor any of their respective beneficial owners is a person named on the "
 "Specially Designated Nationals and Blocked Persons List maintained by the Office of Foreign Assets Control, or is owned or controlled "
 "by any such person. Borrower has delivered to Lender all information required for Lender to comply with its customer identification, "
 "customer due diligence, beneficial ownership and anti-money laundering obligations, including with respect to the members of "
 "Brightleaf Investors Group LLC, and all such information is true, correct and complete."),
("5.17", "Brokers",
 "No broker, finder or agent has acted for Borrower or any Guarantor in connection with the Loan in a manner that would entitle any "
 "such Person to a fee or commission payable by Lender."),
("5.18", "No Other Financing",
 "Borrower has not obtained, and shall not obtain, any financing for the Project other than the Loan, the Mezzanine Loan and the "
 "Indebtedness expressly permitted under Section 7.1."),
("5.19", "No Reliance; Survival",
 "Borrower and each Guarantor acknowledge that they have not relied on any statement, representation or warranty of Lender other than "
 "those expressly set forth in the Loan Documents. The representations and warranties in this Article V shall survive the Closing, the "
 "making of each Advance and the repayment of the Loan."),
]
for num, title, txt in REPS:
    section(doc, num, title, txt)

note(doc, "[Note to Draft: Section 5.2 states the acquisition date and transferor by reference to the recorded deeds described in the title "
          "commitment, and the acquisition cost by reference to the Approved Budget and the appraisal. The representation must be conformed to the "
          "verified facts described in Section 3.7(d) before execution; if the verified cost of the Land differs from $8,200,000, Total Project Costs, "
          "the Loan-to-Cost Ratio and the amount of the LTC Equity Deposit will change. See Memorandum Section 3.1.]")

# ================================================================ ARTICLE VI
article(doc, "VI", "Affirmative Covenants")
para(doc, "Until the Obligations have been paid and performed in full, Borrower shall, and shall cause each Guarantor to, comply with "
          "each of the following covenants:", first_indent=0.5)

section(doc, "6.1", "Existence; Good Standing",
    "Maintain its existence, good standing and qualification to do business in North Carolina and each other jurisdiction in which "
    "such qualification is required, and maintain in full force and effect its organizational documents, licenses, permits and "
    "franchises necessary to the conduct of its business.")

section(doc, "6.2", "Construction and Completion",
    "Cause the Project to be constructed and completed in a good and workmanlike manner, in accordance with the Approved Plans, the "
    "Approved Budget, the Construction Contract, all applicable laws and permits, and the construction schedule, and cause Substantial "
    "Completion to occur on or before August 31, 2027 and final completion (including all punch-list and retainage-release items) to occur "
    "not later than one hundred twenty (120) days thereafter.")

section(doc, "6.3", "Compliance with Laws, Permits and the Declaration",
    "Comply in all material respects with all applicable laws, ordinances, rules, regulations, orders and permits, including "
    "Environmental Laws, the Durham Unified Development Ordinance and the Declaration, and maintain in full force and effect all "
    "permits, approvals and architectural review approvals necessary for the construction and operation of the Project.")

section(doc, "6.4", "Insurance",
    "Maintain in full force and effect at all times the insurance required under Article IX, with insurers, limits, deductibles and "
    "endorsements satisfactory to Lender, and deliver evidence of such insurance at Closing and at each renewal.")

section(doc, "6.5", "Property Condition; Taxes, Assessments and Charges",
    "Keep the Property in good condition and repair, and pay and discharge before delinquency all taxes, assessments, water and sewer "
    "charges, association assessments under the Declaration, and other governmental or private charges imposed upon the Property or the "
    "Loan, except to the extent contested in good faith by appropriate proceedings with adequate reserves and without risk of Lien or "
    "sale. Borrower shall pay when due all assessments levied by the Brightleaf Historic District Association, Inc., currently assessed "
    "at $0.12 per square foot of gross building area per annum.")

section(doc, "6.6", "Books and Records; Inspection Rights",
    "Maintain complete and accurate books and records in accordance with GAAP, and permit Lender and its agents, at reasonable times "
    "and upon reasonable prior notice, to examine and copy such books and records and to inspect the Property.")

section(doc, "6.7", "Use of Proceeds",
    "Use the proceeds of the Loan solely for the purposes set forth in Section 2.4.")

section(doc, "6.8", "Further Assurances",
    "Execute, deliver, record and file such further documents, instruments, financing statements, continuation statements, affidavits "
    "and certificates as Lender may reasonably request to evidence, perfect, maintain or confirm the Liens granted to Lender or to carry "
    "out the purposes of the Loan Documents.")

section(doc, "6.9", "Notices of Default and Other Material Events",
    "Deliver to Lender prompt written notice (and in any event within five (5) Business Days) after Borrower obtains knowledge of "
    "(a) any Default or Event of Default; (b) any default under the Mezzanine Documents, the Intercreditor Agreement, the Construction "
    "Contract or the Architect’s Contract; (c) any litigation, arbitration or governmental proceeding that could reasonably be expected "
    "to have a Material Adverse Effect; (d) any Environmental Claim, any release of Hazardous Substances at the Property, any notice of "
    "violation under Environmental Laws, or any communication from NCDEQ relating to the Property or the NFA Letter; (e) any casualty, "
    "condemnation or threatened condemnation; (f) any Lien asserted against the Property; (g) any stop-work order, permit revocation or "
    "denial of any approval; (h) any default under the Declaration or any action by the Brightleaf Historic District Association relating "
    "to the Project; and (i) any material adverse change in the financial condition of Borrower or any Guarantor.")

section(doc, "6.10", "Intercreditor Agreement",
    "Comply with the Intercreditor Agreement and cause Mezzanine Lender to comply with the Intercreditor Agreement, and deliver to "
    "Lender copies of all notices delivered to or received from Mezzanine Lender under the Mezzanine Documents or the Intercreditor Agreement.")

section(doc, "6.11", "Maintenance of Guaranties",
    "Cause each Guaranty and the Environmental Indemnity to remain in full force and effect, and cause each Guarantor to comply with "
    "the terms of the Guaranties and of this Agreement.")

section(doc, "6.12", "Expense Reimbursement",
    "Pay, within ten (10) days after demand, all reasonable costs, expenses and attorneys’ fees incurred by Lender in connection with "
    "the preparation, negotiation, execution, delivery, administration, amendment, enforcement and protection of the Loan Documents and "
    "the Property, including all appraisal, environmental, engineering, inspection, title, recording, filing and legal fees and expenses.")

# ================================================================ ARTICLE VII
article(doc, "VII", "Negative Covenants")
para(doc, "Until the Obligations have been paid and performed in full and except as approved in advance by Lender in writing (and, "
          "where required, as permitted under the Intercreditor Agreement), Borrower shall not, and shall not permit any member of "
          "Borrower to:", first_indent=0.5)

NEG = [
("7.1", "Indebtedness",
 "Incur, assume, guarantee or otherwise become liable for any Indebtedness other than (a) the Loan, (b) the Mezzanine Loan as permitted "
 "under Section 12.4, (c) trade payables incurred in the ordinary course of business and payable within sixty (60) days, and (d) the "
 "accrued Developer Fee."),
("7.2", "Liens",
 "Create, incur, assume or permit to exist any Lien on the Property, the Pledged Interests or any other collateral securing the Loan, "
 "other than the Permitted Exceptions and the Liens securing the Obligations."),
("7.3", "Transfers; Change in Control",
 "Sell, transfer, convey, assign, encumber, pledge or otherwise dispose of the Property or any interest therein, or any membership "
 "interest in Borrower, whether directly or indirectly, voluntarily or involuntarily, including by operation of law, or permit any "
 "change in the control or management of Borrower; provided that the pledge of the Pledged Interests to Mezzanine Lender contemplated by "
 "the Intercreditor Agreement and the pledge of the Pledged Interests to Lender are permitted."),
("7.4", "Amendments to Organizational Documents",
 "Amend, restate, supplement or otherwise modify Borrower’s Articles of Organization or Operating Agreement in any manner that would "
 "(a) change the membership interests or the relative rights of the members, (b) delete, weaken or fail to enforce any single-purpose "
 "entity or separateness covenant, (c) delete or weaken the Independent Manager provisions, or (d) create any right of any member to "
 "block, delay or condition any action that Lender is entitled to take under the Loan Documents, in each case without Lender’s prior "
 "written consent."),
("7.5", "Affiliate Transactions",
 "Enter into, amend or perform any transaction, contract or arrangement with any Affiliate of Borrower or any member of Borrower except "
 "on arm’s-length terms for fair and reasonable consideration and with prior written notice to Lender, including any management, "
 "development, construction, leasing or guarantee fee."),
("7.6", "Distributions",
 "Make any distribution, dividend, return of capital or other payment to any member of Borrower during the Construction Period, except "
 "for payment of the Developer Fee in accordance with the Approved Budget and only if no Default or Event of Default exists or would "
 "result therefrom; and, during the Mini-Perm Period, make any such distribution unless (a) no Default or Event of Default exists or "
 "would result, (b) the Debt Service Coverage Ratio is not less than 1.25x on a trailing twelve-month basis, and (c) Borrower maintains "
 "net worth of not less than $12,000,000."),
("7.7", "Change in Business",
 "Engage in any business other than the ownership, development, construction, leasing and operation of the Project, or acquire any "
 "asset other than in the ordinary course of such business."),
("7.8", "Amendments to Construction Documents",
 "Amend, modify, terminate or waive any material right under the Construction Contract, the Architect’s Contract or the Approved Plans, "
 "except in accordance with Section 4.13."),
("7.9", "Amendments to Mezzanine Documents",
 "Amend, restate, supplement, modify, waive or forbear under any Mezzanine Document, or permit the principal amount, interest rate, "
 "maturity, amortization, collateral or other material economic term of the Mezzanine Loan to be changed, without Lender’s prior "
 "written consent and except as permitted under the Intercreditor Agreement."),
("7.10", "Capital Calls; Involuntary Dilution",
 "Make any capital call under Section 5.3 of Borrower’s Operating Agreement, or permit the dilution of any member’s interest under "
 "Section 5.3 or Schedule B thereof, without Lender’s prior written consent, it being acknowledged that any such call or dilution would "
 "constitute a prohibited transfer under Section 7.3."),
("7.11", "Prepayment of Other Indebtedness",
 "Pay, prepay, defease, redeem or otherwise satisfy any Indebtedness other than the Loan, except scheduled payments of the Mezzanine "
 "Loan as permitted under the Intercreditor Agreement and payments of trade payables in the ordinary course of business."),
("7.12", "Fiscal Year; Accounting Changes",
 "Change its fiscal year (currently the calendar year) or make any material change in its accounting policies or reporting practices "
 "without Lender’s prior written consent."),
]
for num, title, txt in NEG:
    section(doc, num, title, txt)

# ================================================================ ARTICLE VIII
article(doc, "VIII", "Financial Covenants and Reporting")

section(doc, "8.1", "Loan-to-Cost Ratio",
    "The Loan-to-Cost Ratio shall not at any time exceed 80.00%. Borrower acknowledges that, on the basis of the Commitment Amount of "
    "$47,500,000 and Total Project Costs of $56,700,000, the Loan-to-Cost Ratio would be 83.77%, and that the conforming adjustment "
    "provided in Section 2.2 is required to satisfy this covenant at Closing. The Loan-to-Cost Ratio shall be tested at Closing and at "
    "each Advance.")

section(doc, "8.2", "Loan-to-Value Ratio",
    "The Loan-to-Value Ratio shall not at any time exceed (a) 65.00% on an as-completed basis or (b) 65.00% on an as-stabilized basis. "
    "Borrower acknowledges that, on the basis of the Commitment Amount of $47,500,000, the as-completed Loan-to-Value Ratio would be "
    "65.25%, exceeding the covenant, and that the conforming adjustment provided in Section 2.2 reduces the as-completed Loan-to-Value "
    "Ratio to 62.31% and the as-stabilized Loan-to-Value Ratio to 59.53%. The Loan-to-Value Ratio shall be tested at Closing, upon "
    "receipt of any updated appraisal, and at the time of any Advance.")

section(doc, "8.3", "Debt Service Coverage Ratio",
    "")
rich(doc, [("(a)  Minimum Ratio.", {"bold": True}),
    ("  The Debt Service Coverage Ratio shall not be less than 1.25x, tested initially on the Conversion Date and thereafter annually on "
     "each anniversary of the Conversion Date, in each case on the basis of the trailing twelve (12) month period ending on the last day of "
     "the most recently completed calendar quarter.")],
    first_indent=0.0, space_after=6)
rich(doc, [("(b)  Lease-Up Accommodation.", {"bold": True}),
    ("  Notwithstanding Section 8.3(a), for any test occurring prior to the date that is twelve (12) months after the date on which "
     "Substantial Completion occurs, the Debt Service Coverage Ratio shall be calculated on the basis of in-place annualized net operating "
     "income for the most recently completed calendar quarter and shall not be required to exceed 1.15x. Borrower acknowledges that a "
     "1.25x test applied on the Conversion Date, when the Project will not yet have achieved stabilized occupancy, would be unachievable "
     "(the appraisal projects stabilization in approximately May 2028) and that this accommodation is intended to avoid a covenant breach at "
     "inception.")],
    first_indent=0.0, space_after=6)
rich(doc, [("(c)  Failure; Cure.", {"bold": True}),
    ("  If the Debt Service Coverage Ratio is less than the applicable minimum, Borrower shall, at Lender’s election, either (i) prepay "
     "principal in an amount sufficient to restore the Debt Service Coverage Ratio to the applicable minimum, or (ii) deposit cash "
     "collateral with Lender in an amount determined by Lender to be sufficient to restore the Debt Service Coverage Ratio, in either case "
     "within thirty (30) days after written notice from Lender. Borrower’s failure to do so shall constitute an Event of Default under "
     "Section 14.1(j).")],
    first_indent=0.0, space_after=6)
note(doc, "[Note to Draft: The Term Sheet (Section 6.3) requires the Debt Service Coverage Ratio to be tested “at the commencement of the "
          "Mini-Perm Period,” which falls on August 28, 2027 — approximately nine months before the appraiser’s projected stabilization date of "
          "May 2028. As drafted in the Term Sheet, the covenant would fail at the first test by design. Sections 8.3(b)–(c) cure this. See "
          "Memorandum Section 3.8.]")

section(doc, "8.4", "Borrower Net Worth",
    "Borrower shall maintain net worth, determined in accordance with GAAP on an unconsolidated basis and excluding any receivable from "
    "any member or Affiliate and any asset that is not a Project asset, of not less than $12,000,000, tested annually within one hundred "
    "twenty (120) days after the end of each fiscal year and at Closing. Borrower acknowledges that its net worth reported to Lender of "
    "approximately $14,200,000 is supported only by its interest in the Land, and that the certificate required under Section 3.13(a) must "
    "reconcile such reported net worth to the carrying value of the Land and identify each other asset and liability.")

section(doc, "8.5", "Guarantor Liquidity",
    "The Guarantors shall maintain combined liquidity of not less than $5,000,000, tested quarterly, within forty-five (45) days after "
    "the end of each fiscal quarter. For purposes of this Section 8.5, “liquidity” means cash, cash equivalents and marketable securities "
    "readily convertible into cash within thirty (30) days, determined on a basis consistent with the personal financial statements "
    "delivered under Section 3.13. Each Guarantor shall also deliver, within the same period, a certification of such Guarantor’s "
    "individual net worth and liquidity.")

section(doc, "8.6", "Financial Reporting",
    "Borrower shall deliver to Lender: (a) monthly construction progress reports in accordance with Section 8.7, within fifteen (15) days "
    "after the end of each calendar month during the Construction Period and until Substantial Completion; (b) quarterly unaudited "
    "financial statements of Borrower, within forty-five (45) days after the end of each fiscal quarter; (c) annual audited financial "
    "statements of Borrower prepared by a nationally or regionally recognized independent certified public accounting firm, within one "
    "hundred twenty (120) days after the end of each fiscal year; (d) annual personal financial statements of each Guarantor and annual "
    "federal income tax returns of Borrower and each Guarantor, within one hundred twenty (120) days after the end of each fiscal year; "
    "(e) quarterly guarantor liquidity certifications within forty-five (45) days after the end of each fiscal quarter; (f) annual net "
    "worth certificates of Borrower within one hundred twenty (120) days after the end of each fiscal year; (g) copies of all material "
    "notices, permits, governmental correspondence and regulatory communications relating to the Property or the Project, promptly upon "
    "receipt; and (h) such other financial information as Lender may reasonably request.")

section(doc, "8.7", "Construction and Project Reporting",
    "During the Construction Period and until Substantial Completion, Borrower shall deliver to Lender, within fifteen (15) days after "
    "the end of each calendar month: (a) a construction progress report comparing actual progress to the approved schedule, certified by "
    "Borrower and General Contractor; (b) a budget reconciliation comparing actual and committed costs to the Approved Budget by line "
    "item; (c) a change order log; (d) the Construction Inspector’s report; (e) a schedule of all pending claims, disputes and liens; and "
    "(f) the Interest Reserve reconciliation required under Section 2.7(f). Borrower shall promptly deliver to Lender any notice of delay, "
    "any notice of default received from General Contractor or Architect, and any revised construction schedule.")

section(doc, "8.8", "Interest Reserve Reporting",
    "Borrower shall deliver the monthly Interest Reserve reconciliation required under Section 2.7(f), together with a rolling projection "
    "of interest through the Construction Maturity Date calculated at the greater of the Applicable Rate then in effect and a Daily Simple "
    "SOFR rate of 4.35% per annum.")

section(doc, "8.9", "Compliance Certificates",
    "Together with each financial statement delivered under Section 8.6, Borrower shall deliver a certificate of the Managing Member "
    "(a) setting forth in reasonable detail the calculations necessary to demonstrate compliance with each covenant in this Article VIII, "
    "(b) certifying that no Default or Event of Default exists or, if one exists, describing it and the actions being taken to cure it, "
    "and (c) certifying that all representations and warranties remain true and correct in all material respects.")

section(doc, "8.10", "Cure of Financial Covenant Breach",
    "If Borrower breaches any covenant in Sections 8.1 through 8.5, Borrower may cure such breach within thirty (30) days after the "
    "earlier of (a) the date on which Borrower obtains knowledge of the breach and (b) the date on which Lender delivers written notice "
    "of the breach, by (i) prepaying principal, (ii) depositing cash collateral, (iii) contributing additional equity to Borrower, or "
    "(iv) a combination of the foregoing, in each case in an amount sufficient to cause Borrower to be in compliance with the applicable "
    "covenant on a pro forma basis. A breach that is not cured within such period shall constitute an Event of Default.")

section(doc, "8.11", "Calculations and Defined Financial Terms",
    "For purposes of this Article VIII: (a) “Debt Service Coverage Ratio” means, for any period, the ratio of (i) net operating income "
    "for such period to (ii) the annualized amount of interest that would accrue on the outstanding principal balance of the Loan at the "
    "Applicable Rate then in effect (the Loan being interest-only); (b) “net operating income” means gross revenues from the Property "
    "actually collected, less vacancy and credit loss, less operating expenses (including real estate taxes, insurance, utilities, "
    "repairs and maintenance, management fees, reserves for replacement and all assessments payable under the Declaration), determined in "
    "a manner consistent with the appraiser’s stabilized income and expense analysis, adjusted for actual results; (c) “Appraised Value” "
    "means the most recent as-completed or as-stabilized value conclusion in an appraisal of the Property prepared by an MAI-designated "
    "appraiser acceptable to Lender and complying with FIRREA; and (d) illustrative calculations of each covenant are set forth on "
    "Schedule 8.11.")

# ================================================================ ARTICLE IX
article(doc, "IX", "Insurance; Casualty and Condemnation")

section(doc, "9.1", "Required Insurance",
    "Borrower shall procure and maintain, at its sole cost and expense, the following insurance at all times during the term of the Loan:")
INS = [
("(a)", "Builder’s risk insurance, on an all-risk, agreed-value, replacement-cost basis, in an amount not less than the full replacement cost of the Improvements upon completion (which, based on the as-completed value of $72,800,000, is materially in excess of the $34,750,000 hard construction cost), covering materials in transit, materials stored off-site, soft costs and delayed opening, and naming Lender as mortgagee and loss payee as its interests may appear;"),
("(b)", "Commercial general liability insurance, written on an occurrence basis, with limits of not less than $5,000,000 per occurrence and $10,000,000 in the aggregate, covering premises liability, products and completed operations, contractual liability, personal and advertising injury, and liability arising from the Vapor Mitigation System and the environmental condition of the Property, naming Lender as an additional insured;"),
("(c)", "Umbrella or excess liability insurance with limits of not less than $10,000,000 per occurrence and in the aggregate, in excess of the commercial general liability, automobile liability and employer’s liability coverages, naming Lender as an additional insured;"),
("(d)", "Workers’ compensation insurance as required by N.C.G.S. Chapter 97 and employer’s liability insurance with limits of not less than $1,000,000;"),
("(e)", "Professional liability (errors and omissions) insurance maintained by Architect in an amount not less than $2,000,000 per claim, and by the engineer responsible for the design of the Vapor Mitigation System in an amount not less than $1,000,000 per claim;"),
("(f)", "Flood insurance, if any portion of the Property is determined to be located within a Special Flood Hazard Area, in the amount required by the National Flood Insurance Act and Lender’s policy;"),
("(g)", "Ordinance or law, boiler and machinery, equipment breakdown, and such other coverage as Lender may reasonably require; and"),
("(h)", "During the Mini-Perm Period, a permanent property policy on the completed Improvements, on an all-risk, replacement-cost basis, in an amount not less than the as-completed appraised value, together with rent loss or business income insurance covering not less than twelve (12) months of gross income and continuing expenses."),
]
for lbl, txt in INS:
    sub(doc, lbl, txt, level=1, size=10.5)

section(doc, "9.2", "Policy Requirements; Evidence; Notices",
    "All insurance policies shall be issued by insurers having an A.M. Best rating of not less than A-VIII, shall name Lender as "
    "mortgagee, loss payee or additional insured as applicable, shall provide that no cancellation, non-renewal, material reduction in "
    "coverage or material modification shall be effective without at least thirty (30) days’ prior written notice to Lender, and shall "
    "provide that Lender’s interest shall not be invalidated by any act or omission of Borrower or any other Person. Borrower shall "
    "deliver certificates of insurance at Closing and at each renewal, and shall deliver certified copies of each policy upon Lender’s "
    "request. Deductibles and self-insured retentions shall be commercially reasonable and acceptable to Lender.")

section(doc, "9.3", "Casualty",
    "Upon any damage, destruction or loss to the Property, Borrower shall promptly notify Lender and shall diligently repair and restore "
    "the Property in accordance with Section 9.5 and Section 4.14. Borrower shall adjust and settle any insurance claim only with "
    "Lender’s prior written consent if the claim exceeds $500,000. Lender may, but shall not be obligated to, join in the adjustment of "
    "any claim.")

section(doc, "9.4", "Condemnation",
    "If all or any material portion of the Property is taken or threatened to be taken by eminent domain, Borrower shall promptly notify "
    "Lender and shall not settle or compromise any claim without Lender’s prior written consent. Lender shall be entitled to participate "
    "in all proceedings and to receive all awards to the extent of its interest, and Borrower irrevocably assigns to Lender all awards "
    "to the extent of the Obligations.")

section(doc, "9.5", "Application of Proceeds",
    "Lender shall apply casualty insurance proceeds and condemnation awards as follows: (a) if no Default or Event of Default exists, "
    "Lender shall make such proceeds available to Borrower to repair and restore the Property, provided that (i) in Lender’s reasonable "
    "judgment the Property can be restored to its pre-casualty condition and use within twelve (12) months and prior to the Maturity "
    "Date, (ii) the available proceeds, together with Borrower’s committed funds, are sufficient to complete the restoration, and "
    "(iii) Borrower has delivered a restoration plan and budget approved by Lender and has satisfied all other conditions Lender may "
    "reasonably impose; and (b) otherwise, Lender may apply such proceeds and awards to the Obligations in such order as Lender may elect, "
    "or hold the same as cash collateral. Any proceeds or awards not made available for restoration and not applied to the Obligations "
    "shall be held in a segregated account as additional collateral.")

# ================================================================ ARTICLE X
article(doc, "X", "Environmental Matters")

section(doc, "10.1", "Compliance with Environmental Laws",
    "Borrower shall, at its sole cost and expense, comply and cause the Property to comply with all Environmental Laws; shall not cause "
    "or permit any release of Hazardous Substances at, on, under or from the Property; shall not install or permit any underground or "
    "aboveground storage tank at the Property; and shall not conduct any activity at the Property that would reasonably be expected to "
    "result in liability under CERCLA or any other Environmental Law. Borrower shall maintain and implement the Soil Management Plan for "
    "any excavation, grading or soil disturbance within the Affected Area, and shall provide copies of all related manifests, disposal "
    "receipts and confirmation sampling results to Lender within ten (10) days after receipt.")

section(doc, "10.2", "Compliance with the NFA Letter",
    "Borrower shall comply strictly with each condition of the NFA Letter in accordance with the compliance schedule set forth on "
    "Exhibit F, including: (a) the design, installation, operation and maintenance of the Vapor Mitigation System; (b) the restriction of "
    "the Affected Area to non-residential use as provided in Section 10.3; (c) the preparation, approval and implementation of the Soil "
    "Management Plan; and (d) the recording and maintenance of the Deed Notice. Borrower shall submit to NCDEQ, within ninety (90) days "
    "after completion of the building foundation in the Affected Area, the as-built drawings and the system performance verification report "
    "required by Condition 1 of the NFA Letter, and shall deliver copies thereof to Lender. Borrower shall not permit or suffer any "
    "modification of the Property, the Project or the use thereof that would require a reopening of NCDEQ Site ID IHSB-24-1203 without "
    "Lender’s prior written consent and any required NCDEQ approval.")

section(doc, "10.3", "Affected Area Use Restriction",
    "Borrower shall not use, occupy, lease or permit the occupancy of the Affected Area, or any enclosed space constructed over the "
    "Affected Area, for any residential or other “sensitive use” (as that term is applied by NCDEQ) unless and until Lender has received "
    "evidence that NCDEQ has modified the NFA Letter, or has confirmed in writing, that such use is permitted subject to the installation, "
    "operation and maintenance of the Vapor Mitigation System. Borrower shall not apply for, and shall not permit any tenant to apply for, "
    "a residential certificate of occupancy for any space located over the Affected Area unless the condition in the preceding sentence has "
    "been satisfied. Borrower shall incorporate this restriction into the Approved Plans, into the Construction Contract and into each lease "
    "of space over the Affected Area, and shall cause each such lease to disclose the existence of the Deed Notice and the NFA Letter.")
note(doc, "[Note to Draft: The Credit Memorandum (Sections 8.2 and 9.5) states that 14 residential units are planned above the Affected Area, "
          "while the Phase I ESA (Section 8.5) expressly declined to verify that fact. If the architect’s overlay confirms that no residential "
          "unit is located over the Affected Area, Section 10.3 should be simplified to a negative covenant; if the overlay confirms the "
          "conflict, the resolution alternatives in Section 3.4(f) must be selected before execution. Loss of the 14 units would reduce stabilized "
          "net operating income to $4,499,640, the Debt Service Coverage Ratio to 1.21x and the as-stabilized value to approximately $70,306,875 "
          "(an as-stabilized Loan-to-Value Ratio of 67.56%, exceeding the 65.00% covenant). See Memorandum Section 3.5.]")

section(doc, "10.4", "Vapor Mitigation System",
    "Borrower shall cause the Vapor Mitigation System to be (a) designed by a professional engineer licensed in North Carolina, "
    "(b) approved by NCDEQ, (c) installed in accordance with the Approved Plans and the NFA Letter before any enclosed structure is "
    "constructed over the Affected Area, and (d) thereafter maintained, inspected and, if required, converted to an active "
    "depressurization system at Borrower’s cost. Borrower shall not make any Advance request for work above the podium level within the "
    "Affected Area until the Vapor Mitigation System has been installed and inspected. Borrower shall deliver to Lender the as-built "
    "drawings and performance verification report required by the NFA Letter and shall provide Lender with an annual certification of "
    "continued operation and maintenance of the Vapor Mitigation System.")

section(doc, "10.5", "Soil Management Plan",
    "Borrower shall not commence any excavation, grading or other subsurface disturbance within the Affected Area unless and until the "
    "Soil Management Plan has been approved by NCDEQ and delivered to Lender, and shall cause General Contractor and each applicable "
    "subcontractor to comply with the Soil Management Plan. Borrower shall deliver to Lender a copy of each NCDEQ approval and each "
    "disposal manifest.")

section(doc, "10.6", "Deed Notice",
    "Borrower shall maintain the Deed Notice of record in the Durham County Registry of Deeds and shall not modify, release or "
    "subordinate the Deed Notice without Lender’s prior written consent and any required NCDEQ approval. Borrower shall promptly deliver "
    "to Lender any amendment to or release of the Deed Notice and any notice received from NCDEQ relating thereto.")

section(doc, "10.7", "Environmental Notices and Reports",
    "Borrower shall deliver to Lender, promptly and in any event within five (5) Business Days after receipt or delivery, copies of all "
    "reports, notices, correspondence, orders, directives, consent agreements and submissions relating to the Property and any "
    "Environmental Law, including all communications with NCDEQ, the United States Environmental Protection Agency and the City of Durham, "
    "and all monitoring, sampling and verification results relating to the Vapor Mitigation System or the Affected Area.")

section(doc, "10.8", "Lender’s Rights; No Lender Liability",
    "Lender shall have the right, but not the obligation, to cure any breach of this Article X at Borrower’s expense, and any amounts so "
    "expended shall be part of the Obligations, shall bear interest at the Default Rate and shall be secured by the Security Documents. "
    "Nothing in the Loan Documents, and no inspection, review or approval by Lender of any environmental report, shall (a) constitute a "
    "representation or warranty by Lender as to the environmental condition of the Property, (b) constitute an assumption by Lender of any "
    "liability under any Environmental Law, or (c) be relied upon by Borrower or any other Person. Lender’s rights under this Article X are "
    "in addition to, and not in limitation of, its rights under the Environmental Indemnity.")

section(doc, "10.9", "Environmental Indemnity",
    "Borrower and each Guarantor shall indemnify, defend and hold harmless the Lender Parties from and against all liabilities, losses, "
    "claims, damages, penalties, fines, judgments, remediation costs, consultant fees and attorneys’ fees arising out of or relating to "
    "(a) the presence, release or threatened release of Hazardous Substances at, on, under, from or migrating to or from the Property, "
    "(b) any violation of or liability under any Environmental Law with respect to the Property, (c) the residual contamination in the "
    "Affected Area, the Vapor Mitigation System, the Soil Management Plan or the Deed Notice, and (d) any breach of this Article X or of "
    "the representations in Section 5.10, in each case regardless of whether such liability arises before or after the Closing Date and "
    "regardless of the source of the contamination. The obligations under this Section 10.9 and under the Environmental Indemnity are "
    "unlimited in amount and shall survive repayment of the Loan, the release or reconveyance of the Deed of Trust, foreclosure, a deed in "
    "lieu of foreclosure and any transfer of the Property.")

section(doc, "10.10", "Environmental Insurance",
    "Borrower shall use commercially reasonable efforts to obtain a pollution legal liability insurance policy, in form and amount and "
    "with an insurer reasonably satisfactory to Lender, covering third-party claims, first-party remediation and the cost of obtaining any "
    "modification of the NFA Letter, and shall provide a copy of such policy to Lender prior to the Closing Date or, if such insurance is "
    "not then available on commercially reasonable terms, within ninety (90) days after the Closing Date. Lender may, in its discretion, "
    "require such insurance as a condition to any Advance for work in the Affected Area.")

# ================================================================ ARTICLE XI
article(doc, "XI", "Single-Purpose Entity; Separateness")

section(doc, "11.1", "Single-Purpose Entity Covenants",
    "Borrower shall at all times maintain its status as a single-purpose, bankruptcy-remote entity and shall:")
SPE = [
("(a)", "hold no assets other than the Property, the Equity Escrow Account, the Interest Reserve Account and the Interest Reserve Contingency Escrow, and incidental assets related to the Project;"),
("(b)", "incur no liabilities other than the Loan, the Mezzanine Loan, trade payables incurred in the ordinary course of business and the accrued Developer Fee;"),
("(c)", "conduct no business other than the ownership, development, construction, leasing, management and operation of the Project;"),
("(d)", "maintain its own books, records, financial statements, bank accounts and payroll separate from those of any member, Affiliate or other Person;"),
("(e)", "not commingle its funds or other assets with those of any member, Affiliate or other Person;"),
("(f)", "hold itself out as, and conduct its business in its own name as, a separate and distinct entity;"),
("(g)", "observe all limited liability company formalities, including maintaining minutes and consents, holding required meetings, filing all required reports with the North Carolina Secretary of State and maintaining its principal office and records;"),
("(h)", "pay its own liabilities and expenses from its own funds and not pay the liabilities of, or guarantee the obligations of, any member, Affiliate or other Person, except as expressly permitted in writing by Lender;"),
("(i)", "conduct all transactions with Affiliates on arm’s-length terms;"),
("(j)", "not pledge its assets to secure the obligations of any other Person and not permit its assets to be listed as assets of any other Person;"),
("(k)", "maintain adequate capital in light of its contemplated business operations, and not transfer any asset to any member or Affiliate except for fair value or as expressly permitted under this Agreement; and"),
("(l)", "not acquire obligations or securities of any member or Affiliate."),
]
for lbl, txt in SPE:
    sub(doc, lbl, txt, level=1, size=10.5)

section(doc, "11.2", "Independent Manager",
    "Borrower shall at all times have at least one Independent Manager whose affirmative vote is required for Borrower to (a) file a "
    "voluntary petition for relief under the United States Bankruptcy Code or under any state insolvency law, (b) consent to the "
    "appointment of a receiver, trustee, custodian or assignee for the benefit of creditors, (c) make a general assignment for the benefit "
    "of creditors, or (d) admit in writing its inability to pay its debts generally as they become due. The Independent Manager shall be "
    "appointed pursuant to Borrower’s Operating Agreement, shall not be removable without Lender’s prior written consent, and shall have "
    "no equity interest in Borrower. Borrower shall provide Lender with not less than ten (10) days’ prior written notice of any proposed "
    "change in the Independent Manager, together with evidence of the proposed successor’s independence.")

section(doc, "11.3", "Non-Consolidation",
    "Borrower shall maintain the separateness described in this Article XI so that it will not be substantively consolidated with "
    "Brightleaf Investors Group LLC, Brightleaf Mezzanine Capital LLC, Thomas R. Chen, Elena Vasquez-Torres, Reginald K. Osei, any member "
    "of Borrower or any other Affiliate in any bankruptcy or insolvency proceeding, and shall deliver an updated non-consolidation opinion "
    "upon Lender’s reasonable request following any material change in Borrower’s organizational structure or ownership.")

section(doc, "11.4", "Bankruptcy Limitations",
    "Borrower shall not, without the prior written consent of Lender and the affirmative vote of the Independent Manager, commence any "
    "case or proceeding under any bankruptcy, insolvency, receivership or similar law, or consent to the entry of an order for relief in an "
    "involuntary case. Borrower shall not, and shall not permit any member to, file or join in the filing of an involuntary petition against "
    "Borrower. Any such filing without the Independent Manager’s affirmative vote shall constitute an Event of Default and shall constitute "
    "a Recourse Trigger under Section 13.6.")

section(doc, "11.5", "Affiliate Separateness — Brightleaf Entities",
    "Borrower acknowledges that Brightleaf Investors Group LLC, a 28% member of Borrower, and Brightleaf Mezzanine Capital LLC, the "
    "Mezzanine Lender, are under the common control of Thomas R. Chen, and that this relationship creates heightened substantive "
    "consolidation risk. Borrower shall (a) maintain separate management, books, records, bank accounts and stationery from each Brightleaf "
    "entity, (b) not share any employee, officer, office space or material asset with any Brightleaf entity, except as disclosed to Lender "
    "in writing, (c) cause each Brightleaf entity to observe its own corporate and limited liability company formalities, and (d) not "
    "permit the Mezzanine Lender to exercise any right or remedy in a manner inconsistent with the Intercreditor Agreement.")

# ================================================================ ARTICLE XII
article(doc, "XII", "Collateral; Pledged Interests; Intercreditor")

section(doc, "12.1", "Security Documents",
    "The Obligations shall be secured by (a) the Deed of Trust, creating a first-priority Lien on the Property; (b) the Assignment of "
    "Rents and Leases; (c) the Security Agreement, creating a first-priority security interest in all personal property, fixtures, "
    "equipment, permits, plans, contracts, licenses, approvals, accounts, deposit accounts and general intangibles relating to the "
    "Project, perfected by UCC-1 financing statements filed with the North Carolina Secretary of State and, as to fixtures, in the Durham "
    "County Registry; (d) the collateral assignments of the Construction Contract and the Architect’s Contract; (e) the collateral "
    "assignment of all insurance proceeds and condemnation awards; (f) the Pledge Agreements; and (g) all other Security Documents.")

section(doc, "12.2", "Pledged Interests",
    "As additional security for the Obligations, each member of Borrower shall pledge to Lender 100% of the membership interests in "
    "Borrower held by such member, together with all certificates, instruments, distributions, proceeds and rights appurtenant thereto, "
    "pursuant to the Pledge Agreements. Borrower and each member acknowledge that the pledge to Lender and the pledge to Mezzanine Lender "
    "encumber the same collateral, and that the relative priority of, and the exercise of remedies with respect to, the two pledges shall "
    "be governed exclusively by the Intercreditor Agreement. Borrower shall cause each pledge to be noted on Schedule 5.2 and in "
    "Borrower’s books and records, and shall not permit any other pledge, hypothecation or transfer of any membership interest.")
note(doc, "[Note to Draft: The Credit Memorandum (Section 4.2) recommends that Lender hold a first-priority pledge of the Pledged Interests and "
          "that Mezzanine Lender hold a second-priority pledge. Section 12.2 is drafted to the approved credit decision but does not fix priority, "
          "which is left to the Intercreditor Agreement. Lender’s counsel recommends that the Committee reconsider the priority allocation: because "
          "a pledge of 100% of the equity is the Mezzanine Lender’s only collateral, subordinating it to Lender’s pledge renders the Mezzanine Loan "
          "effectively unsecured, invites a recharacterization or equitable subordination challenge, and increases both substantive consolidation risk "
          "and Lender’s own environmental and lender-liability exposure upon a foreclosure of the equity. The recommended structure is a "
          "first-priority pledge in favor of Mezzanine Lender, with Lender holding a springing, second-priority pledge, step-in rights and a "
          "90-day standstill. See Memorandum Section 5.1.]")

section(doc, "12.3", "Required Intercreditor Terms",
    "The Intercreditor Agreement shall, at a minimum, provide that:")
IC = [
("(a)", "the Liens of Lender in the Property and the other collateral (other than the Pledged Interests) are and shall remain senior to the Liens of Mezzanine Lender, and Mezzanine Lender shall have no Lien on the Property;"),
("(b)", "the relative priority of the pledges of the Pledged Interests is as specified in the Intercreditor Agreement, and Mezzanine Lender subordinates its claim to the extent necessary to give effect to such priority;"),
("(c)", "Mezzanine Lender is subject to a standstill period of not less than ninety (90) days following a default under the Mezzanine Loan before exercising any remedy against Borrower or the Pledged Interests, and may not exercise any remedy at all while a Default or Event of Default under the Loan exists and Lender is diligently pursuing its remedies;"),
("(d)", "Lender shall deliver to Mezzanine Lender copies of all default notices delivered to Borrower, and Mezzanine Lender shall have the right, but not the obligation, to cure defaults under the Loan within the applicable cure period (plus five (5) Business Days);"),
("(e)", "Mezzanine Lender has an option, exercisable within thirty (30) days after receiving notice of an Event of Default, to purchase the Loan at par plus accrued and unpaid interest, Fees, expenses and indemnified amounts;"),
("(f)", "Mezzanine Lender shall not amend, modify or waive any material term of the Mezzanine Documents (including principal amount, interest rate, maturity, amortization, collateral or any increase in the amount thereof) without Lender’s prior written consent;"),
("(g)", "Mezzanine Lender shall not file, or join in the filing of, any involuntary bankruptcy petition against Borrower, and shall not contest or interfere with Lender’s exercise of remedies;"),
("(h)", "Mezzanine Lender acknowledges the affiliate relationship between Brightleaf Investors Group LLC and Mezzanine Lender and agrees not to exercise any right as an Affiliate of a member of Borrower in a manner that would impair Lender’s rights or remedies;"),
("(i)", "all payments received by Mezzanine Lender in contravention of the Intercreditor Agreement are held in trust for Lender; and"),
("(j)", "the Intercreditor Agreement constitutes the entire agreement of Lender and Mezzanine Lender with respect to the priorities, rights and remedies described therein and may not be amended without Lender’s written consent."),
]
for lbl, txt in IC:
    sub(doc, lbl, txt, level=1, size=10.5)

section(doc, "12.4", "Permitted Mezzanine Loan",
    "The Mezzanine Loan is permitted solely on the following terms: (a) original principal amount not exceeding $9,200,000; (b) interest "
    "at 12.50% per annum fixed, with payment-in-kind interest permitted during the Construction Period and cash-pay interest thereafter; "
    "(c) no scheduled principal amortization; (d) maturity coterminous with the Maturity Date, without any right of Mezzanine Lender to "
    "extend beyond the Maturity Date; (e) no Liens on the Property; (f) no cross-default giving Mezzanine Lender rights against Borrower "
    "that are broader than those set forth in the Intercreditor Agreement; and (g) no advance under the Mezzanine Loan after the Closing "
    "Date other than as disclosed to Lender under Section 3.16.")

section(doc, "12.5", "Perfection; UCC Filings",
    "Borrower shall, at its cost, execute and deliver such UCC financing statements, control agreements, certificates and instruments as "
    "Lender may require to perfect its security interests, including control agreements with respect to deposit accounts and, if "
    "applicable, delivery of any certificated membership interests with undated transfer powers. Borrower shall not file, and shall not "
    "permit any member to file, any financing statement or other public notice with respect to the Property or the Pledged Interests "
    "except in favor of Lender and, as permitted under the Intercreditor Agreement, Mezzanine Lender.")

section(doc, "12.6", "Remedies Against Pledged Interests",
    "Upon the occurrence and during the continuance of an Event of Default, Lender may exercise all rights and remedies of a secured "
    "party under Article 9 of the Uniform Commercial Code as in effect in North Carolina with respect to the Pledged Interests, including "
    "the right to vote the Pledged Interests, to receive distributions thereon and to sell or otherwise dispose of the Pledged Interests "
    "at a public or private sale, in each case subject to the Intercreditor Agreement. Borrower and each member waive any right to notice "
    "of sale to the extent permitted by law and agree that ten (10) days’ prior written notice constitutes reasonable notification.")

# ================================================================ ARTICLE XIII
article(doc, "XIII", "Guaranties")

section(doc, "13.1", "Completion Guaranty",
    "Each Guarantor shall, jointly and severally, guarantee the lien-free completion of the Project in accordance with the Approved "
    "Plans, the Approved Budget and the construction schedule, and the payment of all costs of such completion in excess of the Loan "
    "proceeds, the LTC Equity Deposit and Borrower’s other committed funds. The Completion Guaranty shall remain in full force and effect "
    "until Lender has received (a) evidence satisfactory to Lender that the Project has been completed in all material respects, (b) a "
    "final, unconditional certificate of occupancy for all residential units and retail space, (c) final unconditional lien waivers and "
    "evidence of the expiration of the lien period under N.C.G.S. Chapter 44A, and (d) evidence of compliance with each condition of the "
    "NFA Letter. The “Completion Date” under the Completion Guaranty shall be October 31, 2027, which is sixty (60) days after the "
    "Construction Maturity Date and consistent with the construction schedule (projected substantial completion August 31, 2027); "
    "provided that the Guarantors shall not be relieved of liability for any failure to complete the Project by the Construction Maturity "
    "Date as required under Section 6.2.")

section(doc, "13.2", "Carry Guaranty",
    "Each Guarantor shall, jointly and severally, guarantee the payment of interest and all other carrying costs on the Loan (including "
    "real estate taxes, insurance premiums and Lender’s enforcement expenses) during the term of the Loan, to the extent such amounts are "
    "not paid from the Interest Reserve or by Borrower. The Carry Guaranty is in addition to, and not in lieu of, the Interest Reserve, the "
    "Interest Reserve Contingency Escrow and the replenishment obligations under Section 2.7.")

section(doc, "13.3", "Partial Repayment Guaranty",
    "Each Guarantor shall, jointly and severally, guarantee the repayment of 25% of the Commitment Amount, being $11,875,000 as of the "
    "Effective Date and $11,340,000 if the Commitment Amount is reduced pursuant to Section 2.2 (the “Guaranteed Amount”). The liability of "
    "the Guarantors under the Partial Repayment Guaranty is joint and several, and Lender shall be entitled to collect the Guaranteed "
    "Amount once in the aggregate and not once from each Guarantor; provided that each Guarantor remains liable for the full Guaranteed "
    "Amount until it has been paid in full. The Partial Repayment Guaranty is a payment guaranty and is not conditioned on Lender "
    "exhausting its remedies against Borrower or the Property; it is subject to the Recourse Carve-Outs set forth in Section 13.6.")
note(doc, "[Note to Draft: The Term Sheet (Section 7.3) and the Credit Memorandum (Sections 2.3.1–2.3.3) describe the guaranty as “25% × "
          "$47,500,000 = $11,875,000” and as “joint and several, meaning that each Guarantor shall be individually liable for the full "
          "guaranteed amount,” while also describing “each Guarantor’s partial repayment guaranty of $11,875,000” as measured against each "
          "Guarantor’s net worth. Those descriptions are capable of being read as creating $23,750,000 of aggregate exposure. Section 13.3 "
          "fixes the aggregate at the Guaranteed Amount and should be confirmed with the Credit Committee. See Memorandum Section 6.1.]")

section(doc, "13.4", "Environmental Indemnity",
    "Borrower and each Guarantor shall execute and deliver the Environmental Indemnity, unlimited in amount, as described in "
    "Section 10.9. The Environmental Indemnity shall be a full recourse obligation of Borrower and each Guarantor, shall not be limited "
    "by the Guaranteed Amount, and shall survive repayment of the Loan, the release or reconveyance of the Deed of Trust, foreclosure and "
    "any deed in lieu of foreclosure.")

section(doc, "13.5", "Nature of Guaranties; Waivers",
    "The Guaranties are continuing, absolute and unconditional guaranties of payment and performance, and not of collection. Each "
    "Guarantor waives (a) notice of acceptance, presentment, demand, protest and notice of dishonor, (b) any requirement that Lender first "
    "proceed against Borrower, the Property or any other Person or collateral, (c) any defense arising from any modification, extension, "
    "renewal, forbearance or release granted by Lender to Borrower or any other Person, (d) any defense based on the incapacity, "
    "bankruptcy or dissolution of Borrower, and (e) all rights of subrogation, contribution and reimbursement against Borrower until the "
    "Obligations have been paid and performed in full. The Guaranties are in addition to, and not in limitation of, the Environmental "
    "Indemnity and the Recourse Carve-Outs.")

section(doc, "13.6", "Recourse Carve-Outs",
    "The obligations of the Guarantors under the Partial Repayment Guaranty and of Borrower under the Loan Documents shall become full "
    "recourse obligations of Borrower and the Guarantors, without limitation as to amount, upon the occurrence of any of the following "
    "(each, a “Recourse Trigger”): (a) fraud or intentional misrepresentation by Borrower, any Guarantor or any member of Borrower in any "
    "Loan Document or in any certificate delivered to Lender; (b) a voluntary petition for relief under the United States Bankruptcy Code "
    "or any state insolvency law filed by Borrower, or the consent by Borrower to the appointment of a receiver or trustee, in each case "
    "without the affirmative vote of the Independent Manager as required by Section 11.4; (c) any transfer, encumbrance or hypothecation "
    "of the Property or the Pledged Interests in violation of the Loan Documents; (d) any release of Hazardous Substances at the Property "
    "caused or permitted by Borrower or any Guarantor, and any liability arising under any Environmental Law with respect to the Property; "
    "(e) waste or destruction of the Property; (f) any breach of Article XI; (g) any failure to maintain the insurance required under "
    "Article IX; (h) any misapplication of insurance proceeds, condemnation awards, rents, security deposits or tenant improvement "
    "allowances; and (i) any failure to comply with the NFA Letter, the Deed Notice or the Vapor Mitigation System requirements. The "
    "foregoing Recourse Triggers are in addition to, and shall not limit, any other liability of Borrower or any Guarantor under the Loan "
    "Documents, including the Environmental Indemnity.")

section(doc, "13.7", "Guarantor Reporting",
    "Each Guarantor shall deliver (a) annual personal financial statements, prepared on a basis consistent with the statements delivered "
    "under Section 3.13, within one hundred twenty (120) days after the end of each calendar year; (b) quarterly certifications of "
    "liquidity within forty-five (45) days after the end of each calendar quarter; (c) copies of federal income tax returns within thirty "
    "(30) days after filing; and (d) prompt notice of any material adverse change in such Guarantor’s financial condition, any litigation "
    "or judgment exceeding $500,000, any bankruptcy or insolvency proceeding involving such Guarantor, and any revocation or attempted "
    "revocation of any Guaranty.")

section(doc, "13.8", "Release of Guaranties",
    "The Completion Guaranty and the Carry Guaranty shall be released upon satisfaction of the conditions described in Section 13.1 and "
    "the payment in full of all carrying costs, respectively. The Partial Repayment Guaranty shall be released upon payment in full of the "
    "Obligations. The Environmental Indemnity shall not be released. No release shall be effective unless in writing and executed by Lender.")

# ================================================================ ARTICLE XIV
article(doc, "XIV", "Default and Remedies")

section(doc, "14.1", "Events of Default",
    "Each of the following shall constitute an Event of Default:")
EOD = [
("(a)", "Borrower fails to pay any principal, interest, Fees or other amount due under the Loan Documents on the date due, and such failure continues for five (5) days; provided that no grace period shall apply to the payment due on the Maturity Date or to any payment made from the Interest Reserve to the extent funds are available therein;"),
("(b)", "any representation or warranty made by Borrower or any Guarantor in any Loan Document or in any certificate delivered thereunder proves to have been false or misleading in any material respect when made or deemed made;"),
("(c)", "Borrower fails to observe or perform any non-monetary covenant or obligation under the Loan Documents (other than a covenant for which a specific remedy or cure period is provided), and such failure continues for thirty (30) days after the earlier of notice from Lender or knowledge of Borrower; provided that if the failure is capable of cure but cannot reasonably be cured within such period and Borrower is diligently pursuing cure, the period shall be extended by an additional thirty (30) days;"),
("(d)", "Borrower, any Guarantor or any member of Borrower commences any case or proceeding under any bankruptcy, insolvency, reorganization, receivership or similar law, consents to the appointment of a receiver or trustee, makes an assignment for the benefit of creditors, or admits in writing its inability to pay its debts generally as they become due; or an involuntary petition is filed against any of them and is not dismissed within sixty (60) days;"),
("(e)", "a Material Adverse Effect occurs in the financial condition of Borrower or any Guarantor;"),
("(f)", "the Project is more than ninety (90) days behind the approved construction schedule at any time during the Construction Period, or Borrower fails to achieve Substantial Completion on or before August 31, 2027;"),
("(g)", "Borrower or General Contractor abandons the Project, or construction ceases for more than thirty (30) consecutive days for any reason other than a force majeure event approved by Lender;"),
("(h)", "Borrower fails to maintain the insurance required under Article IX;"),
("(i)", "Borrower breaches any covenant set forth in Article XI, Article X or Section 7.3;"),
("(j)", "Borrower fails to comply with any financial covenant in Article VIII and does not cure such failure within the period provided in Section 8.10;"),
("(k)", "a default or event of default occurs under the Mezzanine Documents, the Intercreditor Agreement, the Construction Contract or the Architect’s Contract;"),
("(l)", "any material violation of an Environmental Law occurs, any release of Hazardous Substances occurs at the Property, any environmental order, directive or Lien (other than a Permitted Exception) is issued or recorded against the Property, or Borrower fails to comply with any condition of the NFA Letter, the Soil Management Plan, the Deed Notice or the Vapor Mitigation System requirements;"),
("(m)", "one or more final judgments in an aggregate amount exceeding $500,000 is entered against Borrower, any Guarantor or any member of Borrower and remains unsatisfied, unbonded or unstayed for thirty (30) days;"),
("(n)", "any Guarantor revokes, terminates, disaffirms, or asserts any defense to, any Guaranty, or any Guaranty ceases to be in full force and effect;"),
("(o)", "any Guarantor fails to satisfy the liquidity covenant in Section 8.5 and such failure is not cured within the period provided in Section 8.10;"),
("(p)", "Borrower or any member of Borrower fails to perform any obligation under the Pledge Agreements, or any Pledged Interest is subject to any Lien, pledge or transfer (other than as permitted under the Intercreditor Agreement);"),
("(q)", "the Deed of Trust or any other Security Document ceases to create a valid, perfected Lien on the collateral described therein (other than as a result of Lender’s own act or omission); or"),
("(r)", "Borrower fails to comply with Section 7.1 through Section 7.12 and such failure continues for ten (10) days after notice from Lender."),
]
for lbl, txt in EOD:
    sub(doc, lbl, txt, level=1, size=10.5)
note(doc, "[Note to Draft: Section 14.1(e), (o) and (n) replace the corresponding provisions of the Term Sheet (Section 15), which provided for "
          "an Event of Default if “any Guarantor’s net worth falls below the minimum threshold set forth in Section 6.4.” Section 6.4 of the Term "
          "Sheet is a Borrower net worth covenant; the Term Sheet contains no guarantor net worth covenant. The cross-reference was therefore "
          "inoperative. See Memorandum Section 6.3.]")

section(doc, "14.2", "Notice and Cure Periods",
    "The notice and cure periods set forth in Section 14.1 are exclusive, and no other notice or cure period (whether statutory or "
    "otherwise) shall apply, except as required by applicable law. Lender’s failure to give any notice permitted or required under this "
    "Article XIV shall not constitute a waiver of any Event of Default or of any remedy.")

section(doc, "14.3", "Remedies",
    "Upon the occurrence and during the continuance of an Event of Default, Lender may, at its option and without further notice (except "
    "as required by applicable law or expressly provided in Section 14.1), exercise any or all of the following remedies, in any order and "
    "simultaneously: (a) declare the entire outstanding principal balance of the Loan, together with all accrued and unpaid interest, Fees, "
    "the Exit Fee and other amounts, immediately due and payable; (b) terminate the Commitment Amount and cease making Advances; "
    "(c) apply the Default Rate; (d) foreclose the Deed of Trust and exercise all rights and remedies available at law or in equity, "
    "including those under N.C.G.S. Chapter 45 and Article 9 of the Uniform Commercial Code; (e) exercise all rights and remedies under the "
    "Guaranties, the Pledge Agreements and the Environmental Indemnity; (f) take possession of the Property, complete construction, and "
    "collect and apply rents and other income; (g) set off any amounts held by Lender, including the Interest Reserve Account, the Interest "
    "Reserve Contingency Escrow and the Equity Escrow Account, against the Obligations; and (h) exercise any other right or remedy available "
    "under the Loan Documents, at law or in equity.")

section(doc, "14.4", "Completion by Lender",
    "Upon the occurrence and during the continuance of an Event of Default, Lender may, but shall not be obligated to, complete the "
    "Project or any part thereof, employ contractors, architects, engineers and consultants, pay any Lien, obtain insurance, and take such "
    "other action as Lender deems necessary to protect its collateral. All amounts so expended shall be part of the Obligations, shall bear "
    "interest at the Default Rate and shall be secured by the Security Documents. Borrower hereby irrevocably appoints Lender as its "
    "attorney-in-fact, coupled with an interest, to take such actions in Borrower’s name, including endorsing checks, executing change "
    "orders, and dealing with any governmental authority; provided that Lender shall exercise this power of attorney only upon and during "
    "the continuance of an Event of Default.")

section(doc, "14.5", "Receiver",
    "Upon the occurrence and during the continuance of an Event of Default, Lender shall be entitled to the appointment of a receiver "
    "for the Property, without notice and without regard to the adequacy of the collateral or the solvency of Borrower, and Borrower "
    "consents to such appointment.")

section(doc, "14.6", "Cumulative Remedies",
    "All remedies of Lender are cumulative and non-exclusive, and no delay or failure to exercise any right or remedy shall constitute "
    "a waiver thereof. Lender may exercise any remedy without prejudice to its right to exercise any other remedy, and no exercise of any "
    "remedy shall be deemed an election of remedies.")

section(doc, "14.7", "Application of Proceeds",
    "All amounts received by Lender in connection with the exercise of its remedies, whether from foreclosure, from the Guaranties, from "
    "the sale of collateral or otherwise, shall be applied as provided in Section 2.9, and any surplus shall be paid to Borrower or as "
    "required by applicable law.")

section(doc, "14.8", "Power of Attorney",
    "Borrower hereby irrevocably appoints Lender as its attorney-in-fact, coupled with an interest, solely for the purposes described in "
    "Section 14.4 and Section 4.8, and for the purpose of executing and filing any UCC financing statement, continuation statement, "
    "termination statement or similar instrument necessary to perfect or maintain Lender’s security interests.")

section(doc, "14.9", "North Carolina Enforcement Provisions",
    "Borrower acknowledges that North Carolina is a power-of-sale state, that the Deed of Trust may be enforced by foreclosure under "
    "power of sale in accordance with N.C.G.S. Chapter 45, and that any deficiency following foreclosure may be subject to the "
    "confirmation-of-sale and fair-value requirements of N.C.G.S. § 45-21.36. Borrower waives, to the fullest extent permitted by law, "
    "any right to a hearing prior to foreclosure other than as required by N.C.G.S. § 45-21.16, and any right to assert that the "
    "guaranties are discharged by reason of the foreclosure or by reason of any anti-deficiency protection, except to the extent such "
    "waiver is prohibited by law. Lender’s counsel shall review the enforceability of each Guaranty under North Carolina law prior to "
    "execution, including the effect of N.C.G.S. §§ 45-21.36 and 45-21.38.")

# ================================================================ ARTICLE XV
article(doc, "XV", "Miscellaneous")

section(doc, "15.1", "Notices",
    "All notices, requests, demands and other communications under the Loan Documents shall be in writing and shall be deemed given "
    "(a) when delivered personally, (b) one (1) Business Day after deposit with a nationally recognized overnight courier, (c) three (3) "
    "Business Days after deposit in the United States mail, certified or registered, return receipt requested, postage prepaid, or (d) when "
    "sent by electronic mail with confirmation of transmission, provided that notices of Default or Event of Default, acceleration, "
    "foreclosure or exercise of remedies shall not be effective if sent solely by electronic mail. Notices shall be addressed: (i) if to "
    "Lender, to Pinnacle Savings Bank, N.A., 215 South Tryon Street, 18th Floor, Charlotte, North Carolina 28202, Attention: David "
    "Forsythe, Senior Vice President, with a copy to Ashford, Cromdale Consulting & Laine LLP, 411 South Tryon Street, Suite 2800, "
    "Charlotte, North Carolina 28202, Attention: Katharine Drummond; (ii) if to Borrower, to Harborview Capital Partners LLC, 400 West Main "
    "Street, Suite 310, Durham, North Carolina 27701, Attention: Elena Vasquez-Torres, Managing Member, with a copy to Calloway & Strauss "
    "PLLC, 324 Blackwell Street, Suite 200, Durham, North Carolina 27701, Attention: Jonathan F. Ngo; and (iii) if to a Guarantor, to the "
    "address set forth on the signature page hereto. Any party may change its notice address by notice given in accordance with this "
    "Section 15.1.")

section(doc, "15.2", "Governing Law",
    "The Loan Documents shall be governed by and construed in accordance with the laws of the State of North Carolina, without regard to "
    "its conflict-of-laws principles.")

section(doc, "15.3", "Venue; Waiver of Jury Trial",
    "Each party irrevocably submits to the exclusive jurisdiction of the General Court of Justice of North Carolina, Durham County, and "
    "the United States District Court for the Middle District of North Carolina, for any action or proceeding arising out of or relating to "
    "the Loan Documents, and irrevocably waives any objection to venue in such courts. EACH PARTY HEREBY KNOWINGLY, VOLUNTARILY AND "
    "INTENTIONALLY WAIVES ANY RIGHT TO A TRIAL BY JURY IN ANY ACTION OR PROCEEDING ARISING OUT OF OR RELATING TO THE LOAN DOCUMENTS.")

section(doc, "15.4", "Expenses",
    "Borrower shall pay all costs and expenses incurred by Lender in connection with the origination, documentation, closing, "
    "administration, amendment, syndication, enforcement and protection of the Loan and the Property, including the legal fees and "
    "disbursements of Ashford, Cromdale Consulting & Laine LLP, appraisal fees, environmental assessment fees, title insurance premiums, "
    "survey costs, recording and filing fees, construction inspection fees, and all other out-of-pocket costs. Borrower shall pay Lender’s "
    "legal fees and expenses regardless of whether the Loan closes, subject to the terms of Section 22 of the Term Sheet.")

section(doc, "15.5", "Indemnity",
    "Borrower and each Guarantor shall, jointly and severally, indemnify, defend and hold harmless the Lender Parties from and against any "
    "and all claims, liabilities, losses, damages, penalties, costs and expenses (including attorneys’ fees and costs of defense) arising "
    "out of or relating to (a) the Loan Documents or the transactions contemplated thereby, (b) the Property, including any environmental "
    "matter (which is also governed by Section 10.9 and the Environmental Indemnity), (c) any claim by any member, Affiliate, contractor or "
    "third party relating to the Project, and (d) any claim arising from the failure of Borrower or any Guarantor to perform its "
    "obligations, except to the extent resulting from the gross negligence or willful misconduct of the applicable Lender Party as "
    "determined by a final, non-appealable judgment. This indemnity shall survive repayment of the Loan and the release of the Security "
    "Documents.")

section(doc, "15.6", "Assignment and Participation",
    "Lender may assign, transfer, pledge or grant participations in all or any portion of the Loan and its rights under the Loan "
    "Documents without the consent of Borrower or any Guarantor, and may disclose all information relating to Borrower, the Guarantors, the "
    "Property and the Loan to any actual or prospective assignee, participant or rating agency, subject to customary confidentiality "
    "undertakings. Borrower may not assign or delegate its rights or obligations under the Loan Documents without Lender’s prior written "
    "consent, which may be withheld in Lender’s sole discretion.")

section(doc, "15.7", "No Waiver",
    "No failure or delay by Lender in exercising any right, power or remedy shall operate as a waiver thereof, and no single or partial "
    "exercise of any right, power or remedy shall preclude any other or further exercise thereof. No waiver shall be effective unless in "
    "writing and signed by Lender.")

section(doc, "15.8", "Severability",
    "If any provision of any Loan Document is held to be invalid, illegal or unenforceable, such provision shall be deemed modified to "
    "the minimum extent necessary to make it valid, legal and enforceable, and the remaining provisions shall remain in full force and effect.")

section(doc, "15.9", "Entire Agreement",
    "The Loan Documents constitute the entire agreement of the parties with respect to the Loan and supersede all prior and "
    "contemporaneous negotiations, understandings and agreements, whether written or oral, including the Term Sheet (except for Sections 22 "
    "and 23 thereof, which survive to the extent provided therein). Borrower and each Guarantor acknowledge that they have not relied on any "
    "statement, projection or representation not expressly set forth in the Loan Documents.")

section(doc, "15.10", "Counterparts; Electronic Signatures",
    "This Agreement may be executed in any number of counterparts, each of which shall be deemed an original and all of which together "
    "shall constitute one instrument. Electronic signatures and signatures transmitted by electronic mail in portable document format "
    "shall be deemed original signatures for all purposes.")

section(doc, "15.11", "Time of the Essence",
    "Time is of the essence with respect to each obligation of Borrower and each Guarantor under the Loan Documents, including each "
    "construction milestone, each reporting deadline and each condition to an Advance.")

section(doc, "15.12", "Survival",
    "The representations, warranties, indemnities, covenants and agreements of Borrower and each Guarantor in the Loan Documents shall "
    "survive the execution and delivery of the Loan Documents, the making of each Advance, the repayment of the Loan and the release of the "
    "Security Documents, to the extent provided therein.")

section(doc, "15.13", "Confidentiality",
    "Lender shall keep confidential all non-public information regarding Borrower and the Guarantors, except for disclosure (a) to its "
    "officers, employees, counsel, auditors, examiners, servicers and actual or prospective assignees and participants, (b) as required by "
    "law, regulation, subpoena or the requirements of any regulatory authority, (c) in connection with the exercise of its remedies, and "
    "(d) to any rating agency, insurer or reinsurer.")

section(doc, "15.14", "No Third-Party Beneficiaries",
    "The Loan Documents are for the sole benefit of the parties thereto and their permitted successors and assigns, and nothing therein, "
    "express or implied, shall confer upon any other Person any legal or equitable right, benefit or remedy, except that the Lender Parties "
    "are intended third-party beneficiaries of the indemnities.")

section(doc, "15.15", "Marshalling",
    "Borrower and each Guarantor waive any right to require Lender to marshal assets, to exhaust its remedies against any Person or "
    "collateral, or to pursue any particular remedy before pursuing another.")

section(doc, "15.16", "Amendments and Waivers",
    "No amendment, modification or waiver of any provision of any Loan Document shall be effective unless in a writing signed by Lender "
    "and Borrower (and, if applicable, each Guarantor), and then only to the extent specifically set forth therein. Notwithstanding the "
    "foregoing, Lender may, without the consent of Borrower or any Guarantor, (a) amend Exhibit B to add any exception to title approved by "
    "Lender in writing, (b) conform Exhibit C, Exhibit D or Exhibit E to any adjustment made in accordance with Section 2.2 or Section 4.6, "
    "and (c) amend any Schedule to reflect information furnished by Borrower and approved by Lender.")

section(doc, "15.17", "Relationship of the Parties",
    "The relationship between Lender, on the one hand, and Borrower and the Guarantors, on the other hand, is solely that of creditor and "
    "debtor (and guarantor). Nothing in the Loan Documents shall be construed to create a partnership, joint venture, agency or fiduciary "
    "relationship, and Lender shall not be deemed a partner, joint venturer, agent or fiduciary of Borrower or any Guarantor. Lender has not "
    "approved, and shall not be deemed to have approved, any aspect of the Project for purposes of any Environmental Law or building code, "
    "and Borrower expressly acknowledges that Lender’s review of the Approved Plans, the Approved Budget or any environmental report is for "
    "its own credit purposes only.")

# ---------------------------------------------------------------- signatures
page_break(doc)
para(doc, "SIGNATURE PAGES", size=11, bold=True, align="center", space_after=14)
rich(doc, [("IN WITNESS WHEREOF", {"bold": True}),
    (", the parties hereto have executed this Construction-to-Mini-Permanent Loan Agreement as of the Effective Date.")],
    first_indent=0.5, space_after=18)

def sig_block(doc, party_label, entity, name_line, title_line, by="By: ______________________________",
              date_line="Date: ____________________"):
    para(doc, party_label, size=10, bold=True, space_after=4)
    p = doc.add_paragraph(); p.paragraph_format.space_after = Pt(0)
    r = p.add_run(entity); r.bold = True; r.font.size = Pt(11); r.font.name = FONT
    for line in [by, "", f"Name: {name_line}", f"Title: {title_line}", "", date_line]:
        p2 = doc.add_paragraph()
        p2.paragraph_format.space_after = Pt(0)
        p2.paragraph_format.line_spacing = 1.0
        if line:
            r2 = p2.add_run(line); r2.font.size = Pt(10.5); r2.font.name = FONT
    para(doc, "", space_after=16)

sig_block(doc, "LENDER:", "PINNACLE SAVINGS BANK, N.A.,\na national banking association",
          "David Forsythe", "Senior Vice President, Commercial Real Estate Lending")
sig_block(doc, "BORROWER:", "HARBORVIEW CAPITAL PARTNERS LLC,\na North Carolina limited liability company",
          "Elena Vasquez-Torres", "Managing Member")
sig_block(doc, "GUARANTORS:", "ELENA VASQUEZ-TORRES, individually",
          "Elena Vasquez-Torres", "Individual (address: ______________________________)")
sig_block(doc, "", "REGINALD K. OSEI, individually",
          "Reginald K. Osei", "Individual (address: ______________________________)")


# ================================================================ SCHEDULES
page_break(doc)
para(doc, "SCHEDULE 1.1", size=12, bold=True, align="center", space_after=4)
para(doc, "CERTAIN DEFINED TERMS AND CAPITAL STRUCTURE", size=11, bold=True, align="center", space_after=12)

para(doc, "Part A — Mezzanine Loan Summary (as represented by Borrower)", size=10, bold=True, space_after=6)
MS = [
["Term", "Description"],
["Mezzanine Lender", "Brightleaf Mezzanine Capital LLC, a North Carolina limited liability company (NC Secretary of State File No. 2103988)"],
["Original principal amount", "$9,200,000"],
["Interest rate", "12.50% per annum, fixed"],
["Interest payment", "Payment-in-kind during the Construction Period; cash-pay during the Mini-Perm Period [to be confirmed from the Mezzanine Documents]"],
["Maturity", "Coterminous with the Maturity Date of the Loan, including any extension"],
["Collateral", "Pledge of 100% of the Pledged Interests"],
["Priority", "Second priority behind Lender’s pledge, as provided in the Intercreditor Agreement [priority allocation subject to confirmation — see Section 12.2 note]"],
["Affiliate relationship", "Brightleaf Mezzanine Capital LLC and Brightleaf Investors Group LLC (28% member of Borrower) are both controlled by Thomas R. Chen"],
["Outstanding principal balance at the Effective Date", "[▪] — to be certified by Mezzanine Lender under Section 3.16"],
["Undrawn commitment at the Effective Date", "[▪] — to be certified by Mezzanine Lender under Section 3.16"],
["Application of prior advances", "[▪] — including any amount applied to the acquisition of the Land"],
]
table(doc, MS, widths=[1.9, 4.6], size=8.5)

para(doc, "Part B — Capital Structure Reconciliation", size=10, bold=True, space_before=6, space_after=6)
CS = [
["Component", "Amount", "Verification Source"],
["Land (Contribution Value)", "$8,200,000", "Recorded deeds; settlement statement; capital accounts (Section 3.7(d))"],
["LTC Equity Deposit", "$2,140,000", "Equity Escrow Account; source certification (Section 3.7(c))"],
["Interest Reserve Contingency Escrow", "$500,000", "Escrow account (Section 2.7(e))"],
["**Total Borrower equity at Closing**", "**$10,840,000**", ""],
["Mezzanine Loan", "$9,200,000", "Mezzanine Documents (Section 3.16)"],
["Loan (Conforming Commitment Amount)", "$45,360,000", "Section 2.2(b)"],
["**Total capital sources**", "**$65,400,000**", "Includes both project uses of $56,700,000 and the equity escrows"],
]
table(doc, CS, widths=[2.4, 1.4, 2.7], size=8.5)
note(doc, "[Note to Draft: Part B is illustrative and depends on the resolutions required under Sections 2.2 and 3.7. Cash equity at Closing "
          "($2,640,000) represents approximately 4.7% of Total Project Costs; total equity including the Land ($10,840,000) represents approximately "
          "19.1% of Total Project Costs. The Credit Memorandum states 18.2% on the basis of a $2,140,000 equity deposit only.]")

page_break(doc)
para(doc, "SCHEDULE 5.2", size=12, bold=True, align="center", space_after=4)
para(doc, "MEMBERSHIP INTERESTS OF BORROWER; PLEDGED INTERESTS", size=11, bold=True, align="center", space_after=12)
MEM = [
["Member", "Membership Interest", "Role", "Capital Contribution to Date", "Pledge to Lender", "Pledge to Mezzanine Lender"],
["Elena Vasquez-Torres", "62%", "Managing Member; Guarantor", "Land at Contribution Value ($8,200,000) [to be verified — see Section 3.7(d)]", "Yes — Pledge Agreement", "Yes — [subject to confirmation]"],
["Brightleaf Investors Group LLC", "28%", "Member", "$0 cash; interest issued in consideration of commitment to arrange mezzanine financing", "Yes — Pledge Agreement", "Yes — [subject to confirmation]"],
["Reginald K. Osei", "10%", "Member; Guarantor", "$0 cash; interest issued in consideration of development management services", "Yes — Pledge Agreement", "Yes — [subject to confirmation]"],
["**Total**", "**100%**", "", "", "", ""],
]
table(doc, MEM, widths=[1.35, 0.75, 1.15, 1.55, 0.85, 0.85], size=7.5)
para(doc, "Managerial authority: Elena Vasquez-Torres, as Managing Member, has authority over day-to-day operations and any individual "
          "expenditure not exceeding $500,000. Members holding at least 75% of the membership interests must approve any sale or encumbrance "
          "of substantially all assets, any financing or refinancing in excess of $1,000,000, the admission of a new member, any amendment "
          "of the Operating Agreement, and any voluntary dissolution or bankruptcy filing. As a result, Brightleaf Investors Group LLC "
          "(28%) holds an effective veto over each such action, including the permanent take-out refinancing of the Loan.",
     first_indent=0.5, size=9.5, space_after=8)
note(doc, "[Note to Draft: Borrower’s Operating Agreement, Section 5.1, states that Brightleaf Investors Group LLC contributed $0 cash and "
          "received its 28% interest “in consideration of its commitment to arrange third-party mezzanine financing for the Project.” That is, on "
          "the face of the document, an equity interest issued for the arrangement of affiliate debt. The Credit Memorandum (Section 2.2) "
          "states that the Land was funded “through capital calls from all three members, including Brightleaf Investors Group LLC.” The two "
          "statements are irreconcilable and must be resolved before Closing. See Memorandum Section 5.2.]")

page_break(doc)
para(doc, "SCHEDULE 8.11", size=12, bold=True, align="center", space_after=4)
para(doc, "FINANCIAL COVENANT CALCULATIONS (ILLUSTRATIVE)", size=11, bold=True, align="center", space_after=12)
FC = [
["Covenant", "Computation", "Result at Term Sheet Amount", "Result at Conforming Commitment Amount", "Requirement"],
["Loan-to-Cost Ratio", "Loan ÷ Total Project Costs", "$47,500,000 ÷ $56,700,000 = 83.77% (FAIL)", "$45,360,000 ÷ $56,700,000 = 80.00% (PASS)", "≤ 80.00%"],
["Loan-to-Value (as-completed)", "Loan ÷ $72,800,000", "$47,500,000 ÷ $72,800,000 = 65.25% (FAIL)", "$45,360,000 ÷ $72,800,000 = 62.31% (PASS)", "≤ 65.00%"],
["Loan-to-Value (as-stabilized)", "Loan ÷ $76,200,000", "62.34% (PASS)", "59.53% (PASS)", "≤ 65.00%"],
["Debt Service Coverage Ratio", "NOI ÷ interest at 7.85%", "$4,876,800 ÷ $3,728,750 = 1.31x (PASS)", "$4,876,800 ÷ $3,560,760 = 1.37x (PASS)", "≥ 1.25x"],
["Debt Service Coverage Ratio — reduced NOI (loss of 14 units)", "$4,499,640 ÷ interest at 7.85%", "1.21x (FAIL)", "$4,499,640 ÷ $3,560,760 = 1.26x (PASS)", "≥ 1.25x"],
["Debt Service Coverage Ratio — CC&R assessments deducted", "$4,842,300 ÷ $3,728,750", "1.30x (PASS)", "1.36x (PASS)", "≥ 1.25x"],
["Debt Service Coverage Ratio — stress test (+200 bps)", "$4,876,800 ÷ $4,678,750", "1.04x (FAIL)", "$4,876,800 ÷ $4,467,960 = 1.09x (FAIL)", "≥ 1.25x"],
["Borrower net worth", "Per certified balance sheet", "$14,200,000 as reported (unverified)", "[to be verified]", "≥ $12,000,000"],
["Guarantor combined liquidity", "Cash + marketable securities", "$9,300,000 (PASS)", "$9,300,000 (PASS)", "≥ $5,000,000"],
]
table(doc, FC, widths=[1.35, 1.25, 1.45, 1.55, 0.9], size=7.5)
note(doc, "[Note to Draft: Interest at the Mini-Perm rate on $45,360,000 is $45,360,000 × 7.85% = $3,560,760; at the stressed rate of 9.85% it "
          "is $4,467,960. The stress test fails at both loan sizes, which supports the interest rate cap condition in Section 2.13(c)(vi). The reduced "
          "net operating income in the fourth row reflects the loss of 14 residential units at $2,245 per month (14 × $2,245 × 12 = $377,160), as "
          "described in the Credit Memorandum (Section 9.5).]")

# ================================================================ EXHIBITS
page_break(doc)
para(doc, "EXHIBIT A", size=12, bold=True, align="center", space_after=4)
para(doc, "LEGAL DESCRIPTION OF THE PROPERTY", size=11, bold=True, align="center", space_after=14)

para(doc, "Parcel 1 (Durham County PIN 0821-04-72-3341) — 601 Foster Street", size=10.5, bold=True, space_after=4)
para(doc, "Being all of that certain lot, tract or parcel of land situated in the City of Durham, Durham County, North Carolina, and being "
          "more particularly described as follows:", first_indent=0.5, size=10)
para(doc, "BEGINNING at an existing iron pipe located in the eastern right-of-way margin of Foster Street (60-foot public right-of-way), "
          "said iron pipe being located South 02°14′33″ West, 312.47 feet from the intersection of the eastern right-of-way margin of Foster "
          "Street with the southern right-of-way margin of West Corporation Street; running thence from said Beginning point along the "
          "eastern right-of-way margin of Foster Street, South 02°14′33″ West, 298.62 feet to an existing iron pipe; thence departing said "
          "right-of-way margin, South 87°45′27″ East, 305.41 feet to an existing iron pipe; thence North 02°14′33″ East, 298.62 feet to an "
          "existing iron pipe; thence North 87°45′27″ West, 305.41 feet to the point and place of BEGINNING; containing approximately 2.09 "
          "acres as shown on that survey plat recorded in Plat Book 218, Page 47, Durham County Registry.", first_indent=0.5, size=10)
para(doc, "Being the same property conveyed to Harborview Capital Partners LLC by Special Warranty Deed recorded in Book 7598, Page 443, "
          "Durham County Registry.", first_indent=0.5, size=10, space_after=12)

para(doc, "Parcel 2 (Durham County PIN 0821-04-72-4102) — 615 Foster Street", size=10.5, bold=True, space_after=4)
para(doc, "Being all of that certain lot, tract or parcel of land situated in the City of Durham, Durham County, North Carolina, and being "
          "more particularly described as follows:", first_indent=0.5, size=10)
para(doc, "BEGINNING at an existing iron pipe located in the eastern right-of-way margin of Foster Street (60-foot public right-of-way), "
          "said iron pipe being the southwestern corner of Parcel 1 described above; running thence from said Beginning point along the "
          "eastern right-of-way margin of Foster Street, South 02°14′33″ West, 201.88 feet to a new iron pipe; thence departing said "
          "right-of-way margin, South 87°45′27″ East, 297.63 feet to a new iron pipe; thence North 02°14′33″ East, 201.88 feet to an existing "
          "iron pipe, being the southeastern corner of Parcel 1 described above; thence along the southern boundary of Parcel 1, North "
          "87°45′27″ West, 297.63 feet to the point and place of BEGINNING; containing approximately 1.38 acres as shown on that survey plat "
          "recorded in Plat Book 218, Page 48, Durham County Registry.", first_indent=0.5, size=10)
para(doc, "Being the same property conveyed to Harborview Capital Partners LLC by Special Warranty Deed recorded in Book 7598, Page 445, "
          "Durham County Registry.", first_indent=0.5, size=10, space_after=10)
para(doc, "Total combined land area: approximately 3.47 acres (151,153 square feet).", size=10, bold=True, space_after=8)
note(doc, "[Note to Draft: The descriptions above are reproduced from Schedule A of title commitment NC-2024-88712. They are internally "
          "inconsistent: Parcel 1 has a southern boundary of 305.41 feet, while the call in Parcel 2 that returns to the southwestern corner of "
          "Parcel 1 runs only 297.63 feet along that same line, leaving an unclosed 7.78-foot discrepancy. The described areas (2.09 + 1.38 = "
          "3.47 acres) also conflict with the Phase I ESA, which states 1.89 acres for Parcel 1 and 1.58 acres for Parcel 2. This Exhibit will be "
          "replaced by the ALTA/NSPS survey metes and bounds delivered under Section 3.2 following resolution of the boundary under Section 3.2(d). "
          "The Declaration of Land Use Restrictions required by the NFA Letter (if recorded) must be added as a Permitted Exception.]")

page_break(doc)
para(doc, "EXHIBIT B", size=12, bold=True, align="center", space_after=4)
para(doc, "PERMITTED EXCEPTIONS", size=11, bold=True, align="center", space_after=12)
para(doc, "The Deed of Trust shall be insured as a valid first-priority Lien on the Property, subject only to the following matters "
          "(each, a “Permitted Exception”), as the same are shown on Schedule B of Title Commitment No. NC-2024-88712 (effective "
          "December 5, 2024) as modified in accordance with this Exhibit:", first_indent=0.5, size=10)
PE = [
["No.", "Matter", "Treatment under the Loan Documents"],
["1", "Real property taxes and assessments for fiscal year 2025 and subsequent years, not yet due and payable (Schedule B-II, item 7). 2024 taxes for PIN 0821-04-72-3341 ($29,847.12) and PIN 0821-04-72-4102 ($19,218.44) are paid in full.", "Permitted. Borrower shall pay when due and shall escrow if required by Lender."],
["2", "Duke Energy Carolinas, LLC easement, 20 feet in width, along the western boundary of Parcel 1, recorded in Book 4387, Page 621, Durham County Registry (Schedule B-II, item 8).", "Permitted, subject to Lender’s receipt of the ALTA survey depicting the easement and confirmation that no Improvement encroaches thereon."],
["3", "Stormwater management easement in favor of the City of Durham affecting approximately 0.22 acres in the southern portion of Parcel 1, recorded in Book 7421, Page 212, Durham County Registry (Schedule B-II, item 9).", "Permitted, subject to confirmation by survey that no building footprint, parking structure or foundation encroaches on the easement area."],
["4", "Declaration of Covenants, Conditions and Restrictions recorded in Book 6984, Page 1155, as amended by First Amendment recorded in Book 7102, Page 388, Durham County Registry (Brightleaf Historic District Association, Inc.), including architectural review requirements and assessments of $0.12 per square foot of gross building area per annum (Schedule B-II, item 11).", "Permitted, subject to the architectural review approval condition in Section 3.12(d). Assessments are an operating expense for purposes of the Debt Service Coverage Ratio and shall be paid when due."],
["5", "Terms, conditions, easements and restrictions imposed by the City of Durham Unified Development Ordinance and the MU-D zoning district, including height, setback, floor area ratio, parking minimums and maximums, open space and public art requirements (Schedule B-II, item 12).", "Permitted. Borrower shall deliver the zoning compliance letter required by Section 3.12(a) confirming compliance, including with any maximum parking limitation."],
["6", "Facts, rights, interests and claims that are not shown by the public records but that could be ascertained by an inspection of the Land, or that may be asserted by persons in possession (Schedule B-II, item 13).", "To be deleted at Closing upon delivery of the owner’s affidavit and the ALTA survey required by Section 3.2(e)."],
["7", "Standard printed exceptions 1 through 6 (Schedule B-II), including rights of parties in possession, encroachments and boundary disputes, easements not of record, mechanics’ and materialmen’s liens, unrecorded taxes and assessments, and utility charges.", "Exceptions 1, 2, 3, 5 and 6 shall be deleted at Closing on the basis of the ALTA survey, the owner’s affidavit and the customary North Carolina endorsements. The mechanics’ lien exception (exception 4) shall be modified to exclude work performed or materials furnished prior to recording of the Deed of Trust, in accordance with the lien waivers and affidavits required by Section 3.2(e) and Section 4.12."],
["8", "Declaration of Land Use Restrictions recorded with respect to the Affected Area pursuant to Condition 4 of the NFA Letter.", "[To be inserted upon delivery of evidence of recordation under Section 3.4(c). If the Deed Notice has not been recorded, this Permitted Exception is inapplicable and the failure to record is a condition precedent to Closing.]"],
["9", "The Existing Mortgage (Book 6215, Page 892).", "NOT PERMITTED. The Existing Mortgage shall be satisfied, released and cancelled of record at or prior to Closing in accordance with Section 3.8, and the title policy shall contain no exception for it."],
]
table(doc, PE, widths=[0.45, 3.15, 2.9], size=8.5)
note(doc, "[Note to Draft: Term Sheet Section 18 lists as Permitted Exceptions only the standard printed exceptions, the Duke Energy easement, "
          "the stormwater easement and the Declaration, and then requires that “all other exceptions shown on Schedule B-II … including but not "
          "limited to any prior deeds of trust” be removed. Schedule B-II items 12 and 13 cannot be removed (item 12 is the zoning ordinance; item "
          "13 can only be modified), so the Term Sheet provision is incapable of literal performance. Exhibit B conforms the list to what Title "
          "Company can actually insure. See Memorandum Section 4.1.]")

page_break(doc)
para(doc, "EXHIBIT C", size=12, bold=True, align="center", space_after=4)
para(doc, "APPROVED PROJECT BUDGET", size=11, bold=True, align="center", space_after=12)
para(doc, "Panel 1 — Project Budget at the Term Sheet Commitment Amount ($47,500,000)", size=10, bold=True, space_after=6)
BUD = [
["Line Item", "Amount", "Senior Loan", "Mezzanine Loan", "Borrower Equity"],
["Land Acquisition (contributed at Contribution Value)", "$8,200,000", "—", "$8,200,000", "—"],
["Hard Construction Costs (GMP — Graystone)", "$34,750,000", "$34,750,000", "—", "—"],
["Soft Costs (see detail below)", "$4,150,000", "$4,150,000", "—", "—"],
["Interest Reserve", "$4,850,000", "$4,850,000", "—", "—"],
["Loan Origination Fee (1.00%)", "$475,000", "$475,000", "—", "—"],
["Developer Fee (5.00% of Total Project Costs)", "$2,835,000", "$1,835,000", "$1,000,000", "—"],
["Contingency (hard cost $1,140,000; soft cost $300,000)", "$1,440,000", "$1,440,000", "—", "—"],
["**Total**", "**$56,700,000**", "**$47,500,000**", "**$9,200,000**", "**$0**"],
]
table(doc, BUD, widths=[2.5, 1.0, 1.0, 1.0, 1.0], size=8.5, right_align_from=1)
para(doc, "Panel 2 — Conformed Budget upon reduction of the Commitment Amount under Section 2.2", size=10, bold=True,
     space_before=6, space_after=6)
BUD2 = [
["Line Item", "Amount", "Senior Loan", "Mezzanine Loan", "Borrower Equity"],
["Land Acquisition (contributed at Contribution Value)", "$8,200,000", "—", "$8,200,000", "—"],
["Hard Construction Costs (GMP)", "$34,750,000", "$34,750,000", "—", "—"],
["Soft Costs", "$4,150,000", "$4,150,000", "—", "—"],
["Interest Reserve", "$4,850,000", "$4,850,000", "—", "—"],
["Loan Origination Fee (1.00% of $45,360,000)", "$453,600", "$453,600", "—", "—"],
["Developer Fee", "$2,835,000", "—", "$1,000,000", "$1,835,000"],
["Contingency", "$1,461,400", "$1,156,400", "—", "$305,000"],
["**Total**", "**$56,700,000**", "**$45,360,000**", "**$9,200,000**", "**$2,140,000**"],
]
table(doc, BUD2, widths=[2.5, 1.0, 1.0, 1.0, 1.0], size=8.5, right_align_from=1)
note(doc, "[Note to Draft: Panel 2 preserves Total Project Costs at $56,700,000 and shows the Origination Fee at 1.00% of the reduced Commitment "
          "Amount. The $6,400 reduction in the Origination Fee is offset within Contingency; the Committee may prefer to reduce Soft Costs instead. "
          "The allocation of the Developer Fee and Contingency between senior and equity funding is a business decision to be confirmed. Panel 1 "
          "reflects the Borrower’s own detailed budget, which states that the Land was funded with $8,200,000 of Mezzanine Loan proceeds and that "
          "$1,000,000 of the Developer Fee is funded by the Mezzanine Lender — a representation that is inconsistent with the Term Sheet and the "
          "Credit Memorandum and that must be verified under Section 3.16. If the Mezzanine Loan has in fact been drawn to fund the Land, only "
          "$1,000,000 of the Mezzanine commitment remains available and this Exhibit must be restated. See Memorandum Section 3.1.]")

para(doc, "Soft Cost Detail", size=10, bold=True, space_before=6, space_after=6)
SOFT = [
["Line Item", "Vendor", "Amount"],
["Architecture and Engineering", "Meridian Design Collective PC", "$1,680,000"],
["Permits and Impact Fees", "City of Durham / Durham County", "$685,000"],
["Legal Fees — Borrower", "Calloway & Strauss PLLC", "$425,000"],
["Legal Fees — Lender (estimated) and title/escrow", "Ashford, Cromdale Consulting & Laine LLP / Aldersgate Title & Escrow Inc.", "$310,000"],
["Environmental and Geotechnical", "Sentinel Environmental Consulting LLC", "$185,000"],
["Appraisal", "Ridgeline Appraisal Services Inc.", "$35,000"],
["Title Insurance and Recording", "Aldersgate Title & Escrow Inc.", "$245,000"],
["Construction Inspection and Monitoring", "To be selected by Lender", "$125,000"],
["Builder’s Risk Insurance", "To be placed", "$210,000"],
["Marketing and Lease-Up", "To be determined", "$250,000"],
["**Total Soft Costs**", "", "**$4,150,000**"],
]
table(doc, SOFT, widths=[2.6, 2.6, 1.3], size=8.5, right_align_from=2)
note(doc, "[Note to Draft: The Approved Budget contains no line item for (a) the payoff of the Existing Mortgage ($3,400,000 original principal "
          "amount; current balance unknown), (b) the Unused Line Fee (approximately $125,000 over the 30-month Construction Period), (c) the Exit Fee "
          "(up to $237,500), (d) the Extension Fee (approximately $118,750), (e) accrued interest on the Mezzanine Loan (approximately $2,875,000 "
          "over 30 months at 12.50% on $9,200,000, if payment-in-kind), (f) the assessments payable under the Declaration ($0.12 × 287,500 gross "
          "building area = $34,500 per annum, which is also omitted from the appraiser’s operating expenses), (g) the public art requirement referenced "
          "in Schedule B-II item 12, and (h) lease-up costs of approximately $680,000 (the appraisal’s as-completed valuation deducts $680,000 of "
          "lease-up cost, while the budget contains $250,000). Items (a) and (e) must be added to the uses of funds before Closing. See Memorandum "
          "Section 3.7.]")

page_break(doc)
para(doc, "EXHIBIT D", size=12, bold=True, align="center", space_after=4)
para(doc, "APPROVED DRAW SCHEDULE", size=11, bold=True, align="center", space_after=6)
para(doc, "The following draw schedule conforms the schedule in Section 9.2 of the Term Sheet and Section 7.1 of the Credit Memorandum to "
          "(a) a 10% Retainage on hard construction costs of $3,475,000, and (b) the division of the Developer Fee between senior and "
          "mezzanine funding shown on Exhibit C. Amounts are based on the Commitment Amount of $47,500,000 and shall be adjusted in "
          "accordance with Section 2.2 and Section 4.6.", first_indent=0.5, size=9.5, space_after=8)
DRAW = [
["Draw", "Milestone", "Cum. %", "Gross Hard Cost", "Retainage 10%", "Net Advance", "Cont. / Dev. Fee", "Total Advance", "Cumulative"],
["1", "Closing — soft costs, interest reserve, fee", "0%", "—", "—", "—", "—", "$9,475,000", "$9,475,000"],
["2", "Foundation complete", "15%", "$5,212,500", "$521,250", "$4,691,250", "—", "$4,691,250", "$14,166,250"],
["3", "Frame — Level 3", "35%", "$6,950,000", "$695,000", "$6,255,000", "—", "$6,255,000", "$20,421,250"],
["4", "Topped out", "55%", "$6,950,000", "$695,000", "$6,255,000", "—", "$6,255,000", "$26,676,250"],
["5", "Envelope complete", "70%", "$5,212,500", "$521,250", "$4,691,250", "—", "$4,691,250", "$31,367,500"],
["6", "MEP rough-in", "80%", "$3,475,000", "$347,500", "$3,127,500", "$1,000,000", "$4,127,500", "$35,495,000"],
["7", "Interior — 50% of units", "90%", "$3,475,000", "$347,500", "$3,127,500", "$1,000,000", "$4,127,500", "$39,622,500"],
["8", "Substantial completion / TCO", "100%", "$3,475,000", "$347,500", "$3,127,500", "$1,275,000", "$4,402,500", "$44,025,000"],
["9", "Retainage release (conditions in § 4.4)", "Post-CO", "—", "—", "$3,475,000", "—", "$3,475,000", "$47,500,000"],
]
table(doc, DRAW, widths=[0.32, 1.24, 0.44, 0.68, 0.82, 0.68, 0.68, 0.68, 0.80], size=7, right_align_from=2)
para(doc, "Totals: gross hard cost value $34,750,000; Retainage withheld and released $3,475,000 (net zero); net hard cost advances "
          "$31,275,000; Contingency and Developer Fee advances $3,275,000; total advances $47,500,000.", size=8.5, italic=True,
     space_after=8)
para(doc, "Reconciliation to the Term Sheet Schedule", size=9.5, bold=True, space_before=4, space_after=4)
REC = [
["Item", "Term Sheet / Credit Memorandum", "Exhibit D", "Difference"],
["Draws 2 through 8 — hard cost", "$34,750,000", "$31,275,000", "($3,475,000)"],
["Draw 9 — retainage release", "$3,275,000", "$3,475,000", "$200,000"],
["Aggregate of Draws 2 through 9", "$38,025,000", "$38,025,000", "—"],
["Developer fee funded by the senior loan", "$2,835,000", "$1,835,000", "($1,000,000)"],
["**Total advances**", "**$47,500,000**", "**$47,500,000**", "**$0**"],
]
table(doc, REC, widths=[2.3, 1.85, 1.35, 1.0], size=8, right_align_from=1)
para(doc, "The Term Sheet’s Draw 9 equals 9.42% of the guaranteed maximum price; Exhibit D equals 10.00%. The Term Sheet’s draws 2 through 8 "
          "equal 100% of the guaranteed maximum price, confirming that no retainage is withheld in those draws.", size=8.5, italic=True,
     space_after=8)
note(doc, "[Note to Draft: The Term Sheet schedule disburses the entire $34,750,000 guaranteed maximum price in Draws 2 through 8 and then "
          "releases $3,275,000 of “retainage” in Draw 9 that was never withheld; it also implicitly funds the full $2,835,000 Developer Fee from "
          "senior proceeds, whereas the Borrower’s own budget allocates $1,000,000 of that fee to the Mezzanine Lender. In the Borrower’s "
          "spreadsheet, the components of Draw 9 total $4,275,000 against a stated draw of $3,275,000 — a $1,000,000 footing error. Exhibit D "
          "corrects both. The Committee should also note that Draw 9 is scheduled for October 2027 in the Borrower’s schedule, which is after the "
          "August 28, 2027 Construction Maturity Date; Section 4.4 permits release of Retainage after the Construction Maturity Date only upon the "
          "conditions stated, and Lender’s consent to an advance during the Mini-Perm Period must be expressly documented. See Memorandum Section 3.6.]")

page_break(doc)
para(doc, "EXHIBIT E", size=12, bold=True, align="center", space_after=4)
para(doc, "INTEREST RESERVE AND INTEREST RATE PROVISIONS", size=11, bold=True, align="center", space_after=12)
para(doc, "Interest Reserve Adequacy — Sensitivity to Daily Simple SOFR", size=10, bold=True, space_after=6)
IR = [
["Daily Simple SOFR", "All-In Rate (Spread 3.25%)", "Estimated Total Interest — Construction Period", "Excess / (Shortfall) Against $4,850,000 Reserve"],
["3.50%", "6.75%", "$4,628,675", "$221,325"],
["4.00%", "7.25%", "$4,975,690", "($125,690)"],
["4.35% (rate in effect per Credit Memorandum)", "7.60%", "$5,215,830", "($365,830)"],
["4.75%", "8.00%", "$5,490,165", "($640,165)"],
["5.25%", "8.50%", "$5,832,060", "($982,060)"],
]
table(doc, IR, widths=[1.8, 1.25, 1.85, 1.6], size=8.5, right_align_from=1)
para(doc, "The foregoing estimates are derived from the Borrower’s draw-schedule model (30 monthly periods, average outstanding balance of "
          "approximately $27,429,000). The Credit Memorandum (Section 6.2) estimates total interest of approximately $5,415,000 and a shortfall "
          "of approximately $565,000 at a 4.35% SOFR rate using an assumed average outstanding balance of $28,500,000. The two methodologies "
          "differ by approximately $199,000; the difference results solely from the average balance assumption and not from any difference in "
          "rate. Lender shall use the draw-schedule model for purposes of the adequacy test in Section 2.7(c), updated for actual draws.",
     first_indent=0.5, size=9.5, space_after=10)
para(doc, "Interest Rate Provisions", size=10, bold=True, space_after=6)
IRT = [
["Provision", "Construction Period", "Mini-Perm Period"],
["Index", "Daily Simple SOFR", "Daily Simple SOFR"],
["Spread", "3.25% per annum", "3.50% per annum"],
["SOFR Floor", "1.00% per annum", "1.00% per annum"],
["Minimum all-in rate (at the floor)", "4.25% per annum", "4.50% per annum"],
["All-in rate at SOFR of 4.35%", "7.60% per annum", "7.85% per annum"],
["Interest payment", "Monthly in arrears, first Business Day", "Monthly in arrears, first Business Day"],
["Source of payment", "Interest Reserve, then Borrower", "Borrower"],
["Default Rate", "Applicable Rate + 5.00%", "Applicable Rate + 5.00%"],
["Day count", "Actual days / 360", "Actual days / 360"],
]
table(doc, IRT, widths=[2.3, 2.05, 2.15], size=8.5)

page_break(doc)
para(doc, "EXHIBIT F", size=12, bold=True, align="center", space_after=4)
para(doc, "NCDEQ NO FURTHER ACTION LETTER — COMPLIANCE SCHEDULE", size=11, bold=True, align="center", space_after=6)
para(doc, "NCDEQ Site ID IHSB-24-1203 / Incident No. NONUST-24-0847 — NFA Letter dated September 30, 2024", size=9.5, italic=True,
     align="center", space_after=10)
NFA = [
["Condition", "Requirement", "Deadline", "Evidence Required", "Loan Document Reference"],
["1 — Soil Vapor Mitigation System", "Passive sub-slab depressurization system, with capability of conversion to active, beneath any enclosed structure constructed over the Affected Area; designed by a North Carolina licensed professional engineer in accordance with NCDEQ Division of Waste Management guidelines.", "Installed before construction of any enclosed structure over the Affected Area; as-built drawings and performance verification report submitted to NCDEQ within 90 days after completion of the building foundation in the Affected Area.", "Engineer’s design; NCDEQ approval; building permit documents; as-built drawings; performance verification report; annual O&M certification.", "§ 3.4(d); § 10.4; § 4.3(i)"],
["2 — Land Use Restriction (Non-Residential)", "Future use of the approximately 0.38-acre Affected Area restricted to non-residential (commercial or industrial) purposes. Any change to residential or other sensitive use requires additional investigation and/or remediation and a modification of the NFA determination.", "Ongoing.", "NFA modification or NCDEQ written confirmation (if residential occupancy above the Affected Area is proposed); architect’s overlay confirming unit locations; lease disclosure.", "§ 3.4(f); § 10.3"],
["3 — Soil Management Plan", "Any excavation, grading or soil disturbance within the Affected Area conducted in accordance with an NCDEQ-approved soil management plan addressing screening, stockpiling, dust control, worker safety and disposal.", "Submitted to and approved by NCDEQ before commencement of any subsurface disturbance within the Affected Area.", "Approved Soil Management Plan; incorporation into the Construction Contract and specifications; disposal manifests and confirmation sampling.", "§ 3.4(e); § 10.1; § 10.5"],
["4 — Deed Notice", "Notice recorded in the Durham County Registry of Deeds describing the Affected Area, the nature and extent of residual contamination and the non-residential use restriction.", "November 29, 2024 (60 days after the NFA Letter).", "Recorded Deed Notice; title date-down endorsement; NCDEQ acknowledgment if recorded late.", "§ 3.4(c); § 10.6; Exhibit B item 8"],
["Ongoing — Monitoring", "Post-remediation groundwater monitoring and reporting as required by the NFA Letter and NCDEQ.", "As required by NCDEQ.", "Monitoring reports; NCDEQ correspondence.", "§ 6.9; § 10.7"],
]
table(doc, NFA, widths=[1.05, 2.05, 1.15, 1.35, 0.9], size=7.5)
note(doc, "[Note to Draft: The 60-day Deed Notice deadline expired November 29, 2024. The Phase I ESA (October 28, 2024) states that the notice "
          "had not been recorded, and the title commitment (effective December 5, 2024) does not list any recorded environmental land use "
          "restriction among its Schedule B-II exceptions (it disclaims environmental matters entirely at Note 5). Either the notice was never "
          "recorded — an apparent violation of Condition 4 of the NFA Letter and a Recourse Trigger under Section 13.6(i) — or it was recorded and "
          "omitted from the title commitment. Borrower must produce the recorded instrument and a date-down endorsement before Closing.]")

page_break(doc)
para(doc, "EXHIBIT G", size=12, bold=True, align="center", space_after=4)
para(doc, "FORM OF DRAW REQUEST AND BORROWER’S CERTIFICATE", size=11, bold=True, align="center", space_after=12)
para(doc, "Draw Request No. ____", size=10.5, bold=True, space_after=4)
G = [
["Item", "Description", "Amount"],
["1", "Milestone for which this Draw Request is submitted (per Exhibit D)", ""],
["2", "Percentage of completion certified by Architect and Construction Inspector", ""],
["3", "Gross hard construction cost value of work completed to date", ""],
["4", "Less Retainage (10%)", ""],
["5", "Net hard cost requested", ""],
["6", "Soft costs requested (with invoice detail)", ""],
["7", "Contingency or Developer Fee requested", ""],
["8", "**Total amount requested**", ""],
["9", "Amount remaining undrawn under the Commitment Amount after this Advance", ""],
["10", "Balance in the Interest Reserve Account", ""],
["11", "Projected interest cost through the next anticipated Draw Request", ""],
["12", "Balance in the Equity Escrow Account (undisbursed)", ""],
]
table(doc, G, widths=[0.45, 4.3, 1.4], size=8.5, right_align_from=2)
para(doc, "The undersigned, on behalf of Harborview Capital Partners LLC, certifies that: (a) each condition in Article IV of the Loan "
          "Agreement has been satisfied; (b) no Default or Event of Default exists; (c) each representation and warranty in Article V of "
          "the Loan Agreement is true and correct in all material respects; (d) all work for which payment is requested has been completed "
          "in accordance with the Approved Plans and the Construction Contract, and all materials for which payment is requested have been "
          "incorporated into the Improvements or suitably stored; (e) the attached lien waivers, title date-down endorsement, insurance "
          "evidence and budget reconciliation are true, correct and complete; (f) the remaining undisbursed sources of funds are sufficient "
          "to complete the Project in accordance with the Approved Budget; (g) each condition of the NFA Letter applicable to the stage of "
          "construction then underway has been satisfied; and (h) the Interest Reserve adequacy test in Section 2.7(c) has been satisfied.",
     first_indent=0.5, size=9.5, space_after=16)
para(doc, "HARBORVIEW CAPITAL PARTNERS LLC", size=10, bold=True, space_after=16)
para(doc, "By: ______________________________    Name: Elena Vasquez-Torres    Title: Managing Member    Date: ______________",
     size=9.5, space_after=16)
para(doc, "Certified by Architect: ______________________________   Date: ______________", size=9.5, space_after=6)
para(doc, "Certified by Construction Inspector: ______________________________   Date: ______________", size=9.5, space_after=6)

page_break(doc)
para(doc, "EXHIBIT H", size=12, bold=True, align="center", space_after=4)
para(doc, "SCHEDULE OF OPEN ITEMS, DRAFTING NOTES AND ASSUMPTIONS", size=11, bold=True, align="center", space_after=6)
para(doc, "The following items are open as of the date of this draft. Each is described in the accompanying memorandum of even date "
          "(the “Memorandum”), to which reference is made for the supporting analysis, source citations and recommended resolution.",
     first_indent=0.5, size=9.5, space_after=8)
OPEN = [
["No.", "Provision", "Open Item", "Resolution Required", "Memorandum Ref."],
["1", "§ 2.2, § 8.1, § 8.2, Exhibit C", "Loan-to-Cost Ratio of 83.77% and as-completed Loan-to-Value Ratio of 65.25% exceed the 80.00% and 65.00% covenants. The Credit Memorandum’s $2,140,000 escrow condition does not cure the Loan-to-Cost ratio unless the Commitment Amount is reduced.", "Confirm reduction of the Commitment Amount to $45,360,000 with a $2,140,000 LTC Equity Deposit, or approve an increase in Total Project Costs to at least $59,375,000 funded by at least $2,675,000 of additional verified equity.", "§ 3.2"],
["2", "§ 1.1, § 3.7(d), § 5.2, § 3.16, Exhibit C", "The record contains five inconsistent accounts of the acquisition and funding of the Land (recorded deed June 12, 2023; Operating Agreement contribution at formation; Credit Memorandum capital calls; Phase I ESA acquisition in 2022; appraisal acquisition in early 2024), and the Borrower’s budget states that the Land was funded with $8,200,000 of Mezzanine Loan proceeds.", "Verify from deeds, settlement statements, capital account records and Mezzanine disbursement history; conform Sections 1.1, 5.2 and Exhibit C; obtain certificate under § 3.16.", "§ 3.1"],
["3", "§ 3.8, Exhibit C", "No use of funds and no source of funds is provided for the payoff of the Triangle Commercial Bank deed of trust ($3,400,000 original principal; current balance unknown).", "Obtain payoff letter and add a separate use and corresponding source at Closing.", "§ 3.3"],
["4", "§ 3.4(c), § 3.4(f), § 10.3, Exhibit F", "Deed Notice was required by November 29, 2024 and is not evidenced; the NFA Letter restricts the Affected Area to non-residential use while the Credit Memorandum asserts that 14 residential units sit above it; the Phase I ESA declined to verify unit locations.", "Produce recorded Deed Notice; obtain architect’s overlay; obtain NFA modification or NCDEQ confirmation, or redesign the affected floors.", "§ 3.5"],
["5", "§ 2.7, § 8.3, Exhibit E", "The interest reserve is characterized as adequate ($221,325 surplus at a 3.50% SOFR) and inadequate ($365,830 shortfall at 4.35%; $565,000 per the Credit Memorandum) in the same record; the Debt Service Coverage Ratio test in Term Sheet § 6.3 is set at a date before stabilization.", "Approve the adequacy testing convention in § 2.7(c), the $500,000 Interest Reserve Contingency Escrow, and the lease-up accommodation in § 8.3(b).", "§ 3.4 and § 3.8"],
["6", "§ 4.4, § 4.1, Exhibit D", "The Term Sheet draw schedule disburses 100% of the guaranteed maximum price in Draws 2–8 and then releases $3,275,000 of retainage never withheld; 10% retainage is $3,475,000; the Borrower’s schedule foots Draw 9 at $4,275,000 against $3,275,000; Draws 8 and 9 are dated after the Construction Maturity Date.", "Approve Exhibit D and the timing of the retainage release during the Mini-Perm Period.", "§ 3.6"],
["7", "§ 12.2, § 12.3, § 3.5", "Both the senior loan and the mezzanine loan take a pledge of 100% of the membership interests. The Credit Memorandum recommends a first-priority pledge for Lender; Lender’s counsel recommends the reverse allocation with a springing second-priority pledge and standstill.", "Confirm priority allocation and obtain executed Intercreditor Agreement before Closing.", "§ 5.1"],
["8", "§ 3.6, § 7.4, § 11.2, § 11.3", "The Operating Agreement requires 75% member approval for any financing over $1,000,000, any bankruptcy filing and any amendment; the 28% member (an Affiliate of the Mezzanine Lender) therefore holds an effective veto over the take-out refinancing and the SPE amendments themselves. No independent manager, separateness covenants or non-consolidation opinion currently exist.", "Obtain member consents and an amended Operating Agreement; obtain the non-consolidation opinion.", "§ 5.2"],
["9", "§ 3.2, § 5.3, Exhibit A", "Parcel 1 and Parcel 2 do not close: a 305.41-foot line is described on one side and a 297.63-foot line on the other, a 7.78-foot discrepancy; parcel areas conflict (2.09/1.38 acres per title versus 1.89/1.58 per the Phase I ESA); parcel orientation and street frontage conflict among the sources.", "Obtain ALTA/NSPS survey, boundary agreement or corrective deed, and a conformed legal description.", "§ 4.2 and § 4.3"],
["10", "§ 3.12(d), § 6.5, § 8.11", "The appraisal states that the Brightleaf Historic District Association has approved the design; the title commitment states that no evidence of submission or approval was furnished. The Association assessment of $0.12 per square foot ($34,500 per annum) is absent from the appraiser’s operating expenses.", "Obtain ARC approval or deemed approval; conform the operating expense and Debt Service Coverage Ratio calculations.", "§ 4.4"],
["11", "§ 13.3", "The partial repayment guaranty is described both as $11,875,000 in the aggregate (joint and several) and as $11,875,000 per Guarantor; Mr. Osei’s exposure equals 103.3% of his stated net worth.", "Confirm the aggregate cap and consider a separate cap or additional collateral for Mr. Osei.", "§ 6.1"],
["12", "§ 8.4, § 3.13", "Borrower’s reported net worth of $14,200,000 is not supported by any document in the record and appears inconsistent with a sole asset consisting of land carried at $8,200,000.", "Obtain a current balance sheet and set the covenant accordingly.", "§ 6.2"],
["13", "§ 3.2(e), § 4.12", "Demolition (August 2024) and remediation (September 2024) preceded Closing, and the $3,180,000 site work line is within the guaranteed maximum price; under N.C.G.S. § 44A-10 a claim of lien relates back to first furnishing.", "Obtain owner’s and contractor’s affidavits, conditional and unconditional lien waivers for all pre-Closing work, and consider a payment bond.", "§ 4.5"],
["14", "§ 9.1(a), § 9.1(e)", "Builder’s risk is specified in the Term Sheet at $34,750,000 (hard costs only) although the as-completed value is $72,800,000; the Term Sheet omits the architect’s professional liability coverage that the Credit Memorandum requires.", "Confirm builder’s risk at full replacement value with agreed-value endorsement; confirm architect’s and engineer’s professional liability limits.", "§ 6.4"],
["15", "§ 1.1 (Mezzanine Loan), § 12.4", "The Mezzanine Loan terms are described only in summary form; payment-in-kind interest at 12.50% is not quantified or budgeted and the current balance is unknown.", "Obtain the Mezzanine Documents and disbursement history; conform the definition and the sources and uses.", "§ 3.1"],
]
table(doc, OPEN, widths=[0.35, 1.15, 2.35, 1.65, 0.65], size=7.5)

out = "/workspace/output/loan-agreement-draft.docx"
doc.save(out)
print("saved", out)
