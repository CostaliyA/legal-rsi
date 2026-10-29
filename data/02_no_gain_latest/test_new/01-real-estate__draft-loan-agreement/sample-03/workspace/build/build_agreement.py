# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, "/workspace/build")
from docxlib import *
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

doc = new_doc(body_size=11, margins=(1.0, 1.1, 1.0, 1.1))
header_footer(doc, "THE PIEDMONT AT BRIGHTLEAF \u2014 LOAN AGREEMENT (DRAFT)",
              "", "Draft 2/12/2025 \u2014 Privileged & Confidential \u2014 Loan No. CRE-2025-0342", size=7)

# ------------------------------------------------------------------ COVER
doc.add_paragraph()
p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = p.add_run("DRAFT \u2014 FOR DISCUSSION PURPOSES ONLY\nNOT AN OFFER OR COMMITMENT")
r.bold = True; r.font.size = Pt(10); r.font.color.rgb = DARKRED
p.paragraph_format.space_after = Pt(4)
p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = p.add_run("SUBJECT TO SENIOR LOAN COMMITTEE APPROVAL, SATISFACTORY DUE DILIGENCE, AND REVIEW AND APPROVAL OF DEFINITIVE DOCUMENTATION BY LENDER AND LENDER\u2019S COUNSEL. BRACKETED TEXT DENOTES OPEN ITEMS IDENTIFIED IN THE COVER MEMORANDUM OF EVEN DATE.")
r.font.size = Pt(8.5); r.font.color.rgb = DARKRED
for _ in range(3):
    doc.add_paragraph()

title_block(doc, [
    ("LOAN AGREEMENT", 22, True, (0, 4)),
    ("(Construction-to-Mini-Permanent Loan)", 13, False, (0, 18)),
    ("by and among", 10, False, (0, 10)),
    ("HARBORVIEW CAPITAL PARTNERS LLC,", 12, True, (0, 2)),
    ("a North Carolina limited liability company, as Borrower,", 10, False, (0, 14)),
    ("ELENA VASQUEZ-TORRES and REGINALD K. OSEI,", 12, True, (0, 2)),
    ("as Guarantors (for the limited purposes set forth herein),", 10, False, (0, 14)),
    ("and", 10, False, (0, 10)),
    ("PINNACLE SAVINGS BANK, N.A.,", 12, True, (0, 2)),
    ("a national banking association, as Lender", 10, False, (0, 30)),
])
p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = p.add_run("Dated as of February 28, 2025")
r.bold = True; r.font.size = Pt(11)
p.paragraph_format.space_after = Pt(14)
table(doc, [
    ["Project", "The Piedmont at Brightleaf"],
    ["Property", "601 and 615 Foster Street, Durham, Durham County, North Carolina 27701\nDurham County Parcel Identification Nos. 0821-04-72-3341 and 0821-04-72-4102"],
    ["Loan Amount", "$47,500,000 [Alternative B: $45,360,000 \u2014 see Section 2.1 and Cover Memorandum Item A-1]"],
    ["Lender Loan No.", "CRE-2025-0342"],
    ["Lender", "Pinnacle Savings Bank, N.A., 215 South Tryon Street, 18th Floor, Charlotte, North Carolina 28202"],
    ["Lender\u2019s Counsel", "Ashford, Cromdale Consulting & Laine LLP, 411 South Tryon Street, Suite 2800, Charlotte, North Carolina 28202"],
    ["Borrower\u2019s Counsel", "Calloway & Strauss PLLC, 324 Blackwell Street, Suite 200, Durham, North Carolina 27701"],
], widths=[1.45, 4.65], header=False, size=8, bold_first_col=True)

doc.add_page_break()
h1(doc, "TABLE OF CONTENTS", size=11, space_before=0)
toc = [
    ("ARTICLE 1", "DEFINITIONS AND INTERPRETATION"),
    ("ARTICLE 2", "THE LOAN; INTEREST; FEES; PAYMENTS"),
    ("ARTICLE 3", "CONDITIONS PRECEDENT TO CLOSING"),
    ("ARTICLE 4", "CONDITIONS PRECEDENT TO EACH ADVANCE"),
    ("ARTICLE 5", "DISBURSEMENT, PROJECT BUDGET, RETAINAGE AND COST OVERRUNS"),
    ("ARTICLE 6", "REPRESENTATIONS AND WARRANTIES"),
    ("ARTICLE 7", "AFFIRMATIVE COVENANTS"),
    ("ARTICLE 8", "NEGATIVE COVENANTS"),
    ("ARTICLE 9", "FINANCIAL COVENANTS AND TESTING"),
    ("ARTICLE 10", "ENVIRONMENTAL MATTERS"),
    ("ARTICLE 11", "SINGLE-PURPOSE ENTITY AND SEPARATENESS"),
    ("ARTICLE 12", "INSURANCE"),
    ("ARTICLE 13", "COLLATERAL, TITLE, PERMITTED EXCEPTIONS AND SURVEY"),
    ("ARTICLE 14", "GUARANTIES AND RECOURSE"),
    ("ARTICLE 15", "EVENTS OF DEFAULT"),
    ("ARTICLE 16", "REMEDIES"),
    ("ARTICLE 17", "INDEMNITIES"),
    ("ARTICLE 18", "MEZZANINE LOAN; INTERCREDITOR AGREEMENT"),
    ("ARTICLE 19", "NOTICES"),
    ("ARTICLE 20", "ASSIGNMENT; PARTICIPATIONS; SALE OF THE LOAN"),
    ("ARTICLE 21", "MISCELLANEOUS"),
    ("ARTICLE 22", "EXTENSION OPTION"),
    ("", "SIGNATURE PAGES"),
    ("SCHEDULE 1", "LOAN TERMS"),
    ("SCHEDULE 2", "PERMITTED EXCEPTIONS"),
    ("SCHEDULE 3", "PROJECT BUDGET"),
    ("SCHEDULE 4", "DRAW SCHEDULE AND RETAINAGE"),
    ("SCHEDULE 5", "FINANCIAL COVENANTS AND TESTING"),
    ("SCHEDULE 6", "INSURANCE REQUIREMENTS"),
    ("SCHEDULE 7", "REPORTING CALENDAR"),
    ("SCHEDULE 8", "ENVIRONMENTAL COMPLIANCE REQUIREMENTS (NCDEQ NFA LETTER)"),
    ("EXHIBIT A", "LEGAL DESCRIPTION OF THE PROPERTY"),
    ("EXHIBIT B", "FORM OF DRAW REQUEST AND BORROWER\u2019S CERTIFICATE"),
    ("EXHIBIT C", "FORM OF COMPLIANCE CERTIFICATE"),
    ("EXHIBIT D", "FORM OF INTEREST RESERVE ADEQUACY CERTIFICATE"),
]
for a, b in toc:
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(3)
    p.paragraph_format.tab_stops.add_tab_stop(Inches(1.35))
    p.paragraph_format.left_indent = Inches(1.35)
    p.paragraph_format.first_line_indent = Inches(-1.35)
    if a:
        r = p.add_run(a); r.bold = True; r.font.size = Pt(9.5)
    p.add_run("\t")
    r = p.add_run(b); r.font.size = Pt(9.5)

# ------------------------------------------------------------------ ARTICLE 1
article(doc, "ARTICLE 1", "Definitions and Interpretation", page_break=True)
section(doc, "1.1", "Defined Terms.")
para(doc, "As used in this Agreement, the following terms have the following meanings. Terms defined in the singular include the plural and vice versa, and terms defined in any other Loan Document and not defined in this Agreement have the meanings given to them in such other Loan Document. Unless otherwise indicated, all references to Articles, Sections, Schedules and Exhibits are to Articles and Sections of, and Schedules and Exhibits to, this Agreement.")

D = [
("Advance", "means each disbursement of the Loan proceeds by Lender to or for the account of Borrower under this Agreement, including the Initial Advance."),
("Affiliate", "means, as to any Person, any other Person that directly or indirectly controls, is controlled by, or is under common control with such Person, and, with respect to any individual, any member of such individual\u2019s immediate family and any trust or estate-planning vehicle established for the benefit of such individual or such family. For purposes of this definition, \u201ccontrol\u201d means the possession, directly or indirectly, of the power to direct or cause the direction of the management or policies of a Person, whether through ownership of voting securities, by contract, or otherwise. Thomas R. Chen, Brightleaf Investors Group LLC, and Brightleaf Mezzanine Capital LLC are each acknowledged to be an Affiliate of one another."),
("Agreement", "means this Loan Agreement, as it may be amended, restated, supplemented, or otherwise modified from time to time."),
("Applicable Rate", "means, (a) during the Construction Period, Daily Simple SOFR plus three and one-quarter percent (3.25%) per annum, and (b) during the Mini-Perm Period, Daily Simple SOFR plus three and one-half percent (3.50%) per annum, in each case subject to the SOFR Floor and to Article 2."),
("Appraisal", "means the appraisal of the Property dated November 15, 2024 prepared by Ridgeline Appraisal Services Inc. (Linda M. Haverford, MAI), as reviewed and approved by Lender\u2019s appraisal review department, and any update, revision, or replacement appraisal obtained in accordance with this Agreement."),
("Approved Budget", "means the Project Budget set forth on Schedule 3, as approved in writing by Lender and as the same may be revised from time to time only with Lender\u2019s prior written consent in accordance with Section 5.12."),
("Approved Plans and Specifications", "means the plans, specifications, drawings, and construction documents for the Project prepared by Architect and approved by Lender in accordance with this Agreement, together with all approved changes thereto and all permits, zoning approvals, and restrictive covenants applicable thereto."),
("Architect", "means Meridian Design Collective PC, a North Carolina professional corporation, and its permitted successors and assigns."),
("Assignment of Leases and Rents", "means the Assignment of Rents and Leases executed by Borrower in favor of Lender, as the same may be amended, restated, or otherwise modified."),
("Business Day", "means any day other than a Saturday, a Sunday, or a day on which commercial banks in Charlotte, North Carolina or New York, New York are authorized or required by law to close; \u201cSOFR Business Day\u201d means any day on which the Securities Industry and Financial Markets Association (SIFMA) recommends that the bond markets be closed, subject to Article 2."),
("Casualty", "means any damage to or destruction of all or any portion of the Property or the Improvements from any cause."),
("Change Order", "means any change, amendment, addition, deletion, or other modification to the Construction Contract, the Approved Plans and Specifications, or the scope of the Project, whether or not resulting in an increase in the Guaranteed Maximum Price."),
("Closing Date", "means the date on which the Initial Advance is made."),
("Collateral", "means the Property, the Improvements, the Pledged Interests, and all other real and personal property, intangibles, and proceeds in which Lender is granted a Lien under the Loan Documents."),
("Commitment", "means Lender\u2019s commitment to make Advances in an aggregate principal amount not to exceed the Loan Amount, as such amount may be reduced under Section 2.1 or Article 22."),
("Completion Guaranty", "means the Completion Guaranty Agreement executed and delivered by each Guarantor in favor of Lender, as the same may be amended, restated, or otherwise modified."),
("Compliance Certificate", "means a certificate substantially in the form of Exhibit C, executed by the chief manager or chief financial officer of Borrower."),
("Condemnation", "means any taking of all or any portion of the Property or the Improvements, or any interest therein or right accruing thereto, by any Governmental Authority having the power of eminent domain, whether by exercise of such power or by agreement in lieu thereof."),
("Construction Contract", "means the guaranteed maximum price construction contract between Borrower, as owner, and Contractor, dated as of [__________], 2024, in the Guaranteed Maximum Price of $34,750,000, as collaterally assigned to Lender and as approved by Lender."),
("Construction Documents", "means, collectively, the Construction Contract and the Architect\u2019s Agreement, each as collaterally assigned to Lender."),
("Construction Inspector", "means an independent third-party construction consulting or inspection firm engaged by Lender, at Borrower\u2019s expense, to inspect the Project, verify milestone completion, and review each Draw Request."),
("Construction Maturity Date", "means August 28, 2027, being the last day of the Construction Period, as such date may be extended only in accordance with Article 22."),
("Construction Period", "means the period commencing on the Closing Date and ending on the Construction Maturity Date."),
("Contractor", "means Graystone Construction Group Inc., a North Carolina corporation (NC General Contractor License No. 78442), and its permitted successors and assigns."),
("Daily Simple SOFR", "means, for any day, SOFR for such day, as determined in accordance with Article 2 and after giving effect to the SOFR Floor."),
("Deed of Trust", "means the Deed of Trust, Assignment of Rents, Security Agreement and Fixture Filing executed by Borrower, as grantor, for the benefit of Lender, as beneficiary, encumbering the Property and the Improvements, as the same may be amended, restated, or otherwise modified."),
("Default Rate", "means the Applicable Rate plus five percent (5.00%) per annum."),
("Distribution", "means any dividend or distribution of cash or other property to any member or other equity holder of Borrower, any redemption or purchase of membership interests, any return of capital, any loan or advance to a member or Affiliate, or any payment of the Developer Fee or any other fee to any member or Affiliate, other than payments expressly permitted under Section 8.6."),
("Draw Request", "means a written request for an Advance substantially in the form of Exhibit B, together with all supporting documentation required under Article 4 and Section 5.2."),
("DSCR", "means, for any period, the ratio of (a) Net Operating Income for such period to (b) Debt Service for such period, in each case determined in accordance with Schedule 5."),
("Debt Service", "means, for any period, the aggregate amount of interest that would accrue on the outstanding principal balance of the Loan during such period at the Applicable Rate then in effect, calculated on an interest-only basis, together with all fees and Other Charges payable under the Loan Documents during such period other than the Origination Fee."),
("Environmental Indemnity", "means the Environmental Indemnity Agreement executed and delivered by Borrower and each Guarantor in favor of Lender, as the same may be amended, restated, or otherwise modified."),
("Environmental Laws", "means all federal, state, and local statutes, regulations, ordinances, orders, and common law relating to pollution, the protection of human health or the environment, or the use, generation, storage, treatment, transportation, Release, or disposal of Hazardous Substances, including CERCLA, the Resource Conservation and Recovery Act, the Clean Water Act, the Clean Air Act, the Toxic Substances Control Act, and the North Carolina Oil Pollution and Hazardous Substances Control Act (N.C.G.S. Chapter 143, Article 21A), the North Carolina Inactive Hazardous Sites Response Act (N.C.G.S. Chapter 130A, Article 9), and the North Carolina Brownfields Property Reuse Act (N.C.G.S. Chapter 130A, Article 9, Part 5)."),
("Equity Contribution", "means the aggregate cash equity contributions made by the members of Borrower for application to Project Costs from sources other than (a) the Mezzanine Loan or any Mezzanine Document, (b) any Affiliate of Mezzanine Lender, Brightleaf Investors Group LLC, or Thomas R. Chen, (c) any other Indebtedness, or (d) any reserve or escrow funded with Loan proceeds, in an amount not less than $2,140,000, the source of which shall be verified to Lender\u2019s reasonable satisfaction."),
("Equity Escrow Account", "means the segregated deposit account maintained with Lender (or with a financial institution acceptable to Lender under a deposit account control agreement in favor of Lender) into which the Equity Contribution is deposited and from which funds are disbursed solely in accordance with Section 5.4."),
("Event of Default", "means any event or condition described in Article 15."),
("GAAP", "means generally accepted accounting principles in the United States, consistently applied."),
("Governmental Authority", "means any federal, state, county, municipal, or other governmental or quasi-governmental body or agency having jurisdiction over Borrower, any Guarantor, the Property, or the Project, including the City of Durham, Durham County, the State of North Carolina, NCDEQ, and the OCC."),
("Guaranteed Maximum Price", "means $34,750,000, being the maximum price payable under the Construction Contract, subject only to approved Change Orders."),
("Guarantors", "means, collectively, Elena Vasquez-Torres and Reginald K. Osei, each an individual resident of the State of North Carolina, and their respective estates, heirs, successors, and permitted assigns."),
("Guaranties", "means, collectively, the Completion Guaranty, the Carry Guaranty, the Partial Repayment Guaranty, the Environmental Indemnity, and each other guaranty, indemnity, or surety agreement now or hereafter executed by any Guarantor in favor of Lender."),
("Guarantor Liquidity", "means, as to each Guarantor and in the aggregate, cash, cash equivalents, and marketable securities that are readily convertible into cash within thirty (30) days, determined in accordance with Schedule 5 and evidenced by a certificate of such Guarantor."),
("Hazardous Substances", "means petroleum and petroleum products (including gasoline, diesel fuel, and heating oil), asbestos and asbestos-containing materials, polychlorinated biphenyls, urea formaldehyde, radon, per- and polyfluoroalkyl substances, and any other substance, material, or waste that is regulated, listed, defined, or classified as hazardous, toxic, a pollutant, or a contaminant under any Environmental Law."),
("Improvements", "means the six-story mixed-use building to be constructed on the Property consisting of five residential levels over a one-level podium, containing 212 residential units (142 one-bedroom, 56 two-bedroom and 14 three-bedroom units), approximately 18,400 square feet of ground-floor retail space in seven retail bays, a structured parking garage containing 276 spaces, and the associated amenities, together with all appurtenances, fixtures, and site improvements."),
("Indebtedness", "means, as to any Person, without duplication, all obligations for borrowed money, all obligations evidenced by notes, bonds, or similar instruments, all capitalized lease obligations, all reimbursement obligations in respect of letters of credit, all guarantees of the obligations of any other Person, and all obligations secured by a Lien on any property of such Person."),
("Independent Manager", "means a natural person who (a) is not and has never been an officer, employee, manager, member, partner, shareholder, creditor, counsel, or Affiliate of Borrower, any member of Borrower, Mezzanine Lender, Brightleaf Investors Group LLC, Thomas R. Chen, or any of their respective Affiliates, (b) has at least five (5) years of experience in commercial real estate, structured finance, or corporate management, and (c) is approved in writing by Lender, which approval shall not be unreasonably withheld, conditioned, or delayed."),
("Initial Advance", "means the first Advance of Loan proceeds made on the Closing Date."),
("Insurance Requirements", "means the insurance requirements set forth in Article 12 and Schedule 6 and in the Deed of Trust."),
("Intercreditor Agreement", "means the intercreditor and subordination agreement among Lender, Mezzanine Lender, Borrower, and the members of Borrower, in form and substance satisfactory to Lender in its sole discretion, as required by Article 18."),
("Interest Reserve", "means the $4,850,000 amount funded from Loan proceeds at closing and held in the Interest Reserve Account for application to interest accruing during the Construction Period, as such amount may be increased in accordance with Section 5.5."),
("Interest Reserve Account", "means the segregated sub-account of the Loan established and maintained by Lender for the Interest Reserve, as described in Section 5.5."),
("Interest Reserve Adequacy Test", "means the test described in Section 5.5(d)."),
("Lien", "means any mortgage, deed of trust, deed to secure debt, pledge, security interest, hypothecation, lien, charge, encumbrance, judgment, or other preferential arrangement of any kind, including any conditional sale or title retention arrangement."),
("Loan", "means the construction-to-mini-permanent loan made by Lender to Borrower under this Agreement in the principal amount of the Loan Amount."),
("Loan Amount", "means $47,500,000 [Alternative B: $45,360,000], as such amount may be reduced in accordance with Section 2.1 or Article 22 and as such amount may be reflected in the ledger maintained by Lender."),
("Loan Documents", "means this Agreement, the Note, the Deed of Trust, the Assignment of Leases and Rents, the Security Agreement, the Guaranties, the Pledge Agreements, the Intercreditor Agreement, the Environmental Indemnity, the Construction Documents collateral assignments, the Equity Escrow Agreement, the Cash Management Agreement, and each other agreement, instrument, certificate, or document now or hereafter evidencing, securing, guaranteeing, or otherwise relating to the Loan."),
("Loan-to-Cost Ratio", "means, as of any date of determination, the ratio, expressed as a percentage, of (a) the Loan Amount to (b) Total Project Costs, determined in accordance with Schedule 5."),
("Loan-to-Value Ratio", "means, as of any date of determination, the ratio, expressed as a percentage, of (a) the outstanding principal balance of the Loan to (b) the As-Completed Value or the As-Stabilized Value of the Property, as applicable, determined in accordance with Schedule 5."),
("Material Adverse Effect", "means any circumstance, change, event, or effect that, individually or in the aggregate, (a) is or could reasonably be expected to be material and adverse to the business, assets, liabilities, financial condition, or results of operations of Borrower or any Guarantor, (b) materially and adversely impairs the value, use, or marketability of the Property or the Collateral, (c) materially and adversely impairs the ability of Borrower or any Guarantor to perform its obligations under the Loan Documents, or (d) materially and adversely affects the enforceability or priority of any Loan Document or any Lien granted to Lender."),
("Maturity Date", "means the Mini-Perm Maturity Date, or such earlier date on which the entire outstanding principal balance of the Loan becomes due and payable in accordance with the Loan Documents, including by acceleration."),
("Mezzanine Documents", "means the mezzanine loan agreement and all other documents evidencing, securing, or guaranteeing the Mezzanine Loan, including the pledge of the Pledged Interests in favor of Mezzanine Lender."),
("Mezzanine Lender", "means Brightleaf Mezzanine Capital LLC, a North Carolina limited liability company (NC Secretary of State File No. 2103988), and its successors and assigns."),
("Mezzanine Loan", "means the $9,200,000 subordinated mezzanine loan made or to be made by Mezzanine Lender to Borrower, secured by a subordinated pledge of the Pledged Interests and governed by the Intercreditor Agreement."),
("Mini-Perm Maturity Date", "means August 28, 2028, as such date may be extended only in accordance with Article 22."),
("Mini-Perm Period", "means the period commencing on the day immediately following the Construction Maturity Date and ending on the Mini-Perm Maturity Date."),
("Monthly Payment Date", "means the first Business Day of each calendar month during the term of the Loan."),
("NCDEQ", "means the North Carolina Department of Environmental Quality, Inactive Hazardous Sites Branch, and any successor agency."),
("Net Operating Income", "means, for any period, the actual gross operating revenues of the Property for such period (determined in accordance with GAAP on an accrual basis and in a manner consistent with the Appraisal), less actual operating expenses of the Property for such period (including real estate taxes, insurance, utilities, repairs and maintenance, management fees, and a replacement reserve of not less than $250 per residential unit per annum), excluding debt service, depreciation, amortization, income taxes, and capital expenditures. For purposes of the initial determination at stabilization, Net Operating Income may be determined on a projected basis in accordance with Schedule 5."),
("NFA Letter", "means the conditional No Further Action determination letter issued by NCDEQ dated September 30, 2024 for Site ID IHSB-24-1203 / Incident No. NONUST-24-0847, together with all conditions, restrictions, and requirements set forth therein or incorporated by reference."),
("Note", "means the Promissory Note dated as of the Closing Date in the original principal amount of the Loan Amount, executed by Borrower and payable to the order of Lender."),
("OCC", "means the Office of the Comptroller of the Currency."),
("OFAC", "means the U.S. Department of the Treasury\u2019s Office of Foreign Assets Control."),
("Origination Fee", "means $475,000, being one percent (1.00%) of the Loan Amount."),
("Other Charges", "means all fees, costs, expenses, indemnities, and other amounts payable by Borrower under the Loan Documents, including the Exit Fee, the Unused Line Fee, the Extension Fee, late charges, default interest, prepayment or breakage amounts, and Lender\u2019s expenses."),
("Partial Repayment Guaranty", "means the Partial Repayment Guaranty Agreement executed and delivered by each Guarantor in favor of Lender in an aggregate amount not to exceed $11,875,000, as described in Section 14.3."),
("Permitted Exceptions", "means, collectively, the matters described on Schedule 2 and such other matters as Lender may approve in writing."),
("Permitted Indebtedness", "means (a) the Loan, (b) the Mezzanine Loan in an original principal amount not to exceed $9,200,000, (c) trade payables incurred in the ordinary course of business and not more than sixty (60) days past due, and (d) equipment leases and purchase-money financing in an aggregate amount not to exceed $100,000 outstanding at any time."),
("Person", "means any individual, corporation, limited liability company, partnership, joint venture, trust, association, unincorporated organization, Governmental Authority, or other entity."),
("Pledged Interests", "means one hundred percent (100%) of the membership interests in Borrower, together with all certificates, distributions, and proceeds thereof, pledged to Lender (with a subordinated pledge to Mezzanine Lender) under the Pledge Agreements."),
("Pledge Agreements", "means, collectively, the membership interest pledge agreements executed by each member of Borrower in favor of Lender, together with all related transfer powers, undated instruments of assignment, and consents."),
("Project", "means the acquisition, development, construction, and completion of the Improvements on the Property, together with all related site work, on-site and off-site improvements, and the leasing and operation thereof."),
("Project Budget", "means the schedule of Total Project Costs attached as Schedule 3."),
("Project Costs", "means all costs and expenses incurred or to be incurred in connection with the acquisition, development, construction, and completion of the Project, as set forth in the Approved Budget."),
("Property", "means the real property described in Exhibit A, together with all Improvements, fixtures, and appurtenances thereto."),
("Release", "means any releasing, spilling, leaking, pumping, pouring, emitting, emptying, discharging, injecting, escaping, leaching, dumping, disposing, or migrating into or through the indoor or outdoor environment."),
("Restricted Area", "means the approximately 0.38-acre area in the northeast corner of Durham County Parcel Identification No. 0821-04-72-4102 that is subject to the non-residential land use restriction set forth in Condition 2 of the NFA Letter, as delineated on Figure 3 to the Phase I ESA and as the same may be more precisely established by the survey, boundary, and delineation work required under Section 10.5."),
("Retainage", "means the ten percent (10%) holdback withheld by Lender from each Advance allocable to Hard Costs in accordance with Section 5.3, which on the date hereof equals $3,475,000 (ten percent (10%) of the Guaranteed Maximum Price)."),
("Requisition Certificate", "means the certificate of the Architect accompanying each Draw Request certifying the percentage of completion of the Project and the amount of hard and soft costs then properly incurred and due."),
("Security Agreement", "means the Security Agreement executed by Borrower in favor of Lender granting a first-priority security interest in all personal property, fixtures, equipment, permits, plans and specifications, contract rights, accounts, and general intangibles relating to the Project."),
("SOFR", "means the Secured Overnight Financing Rate as published by the Federal Reserve Bank of New York (or a successor administrator selected by Lender in its reasonable discretion) for the applicable day; provided that if SOFR is less than one percent (1.00%), SOFR shall be deemed to be one percent (1.00%) for all purposes of the Loan Documents."),
("SOFR Floor", "means one percent (1.00%) per annum."),
("SPE", "means a single-purpose, bankruptcy-remote entity that satisfies the separateness covenants of Article 11."),
("Substantial Completion", "means completion of the Improvements in all material respects in accordance with the Approved Plans and Specifications, such that the Improvements may be lawfully occupied for their intended use and a certificate of occupancy (whether temporary or final) has been issued by the City of Durham for all residential units and retail space in the Project."),
("Survey", "means the ALTA/NSPS Land Title Survey of the Property prepared by a surveyor licensed in North Carolina and certified to Borrower, Lender, and Title Company, complying with the 2021 ALTA/NSPS Minimum Standard Detail Requirements and including such Table A optional items as Lender may require, dated or re-certified within ninety (90) days prior to the Closing Date."),
("Title Company", "means Aldersgate Title & Escrow Inc., 307 West Chapel Hill Street, Suite 400, Durham, North Carolina 27701, together with any successor title insurance company or agent approved by Lender."),
("Title Commitment", "means Title Company\u2019s Commitment for Title Insurance No. NC-2024-88712, effective December 5, 2024 at 8:00 a.m., together with all supplements, updates, and date-down endorsements."),
("Title Policy", "means the ALTA Loan Policy of title insurance (06-17-06) issued by Title Company to Lender in an amount not less than the Loan Amount, insuring the Deed of Trust as a valid first-priority lien on the fee simple estate in the Property, subject only to the Permitted Exceptions, together with all endorsements required by Lender."),
("Total Project Costs", "means the aggregate of all Project Costs set forth in the Approved Budget, as the same may be revised only with Lender\u2019s prior written consent."),
("Transfer", "means any sale, assignment, transfer, conveyance, gift, pledge, hypothecation, encumbrance, or other disposition, whether voluntary, involuntary, direct, or indirect, including any transfer resulting from a change in control of any member of Borrower, any issuance of additional membership interests, any dilution under Section 5.3 of Borrower\u2019s operating agreement, or any transfer by operation of law."),
("Unused Line Fee", "means the fee described in Section 2.6(c)."),
]

for term, text in D:
    definition(doc, term, text)

section(doc, "1.2", "Interpretation.")
para(doc, "In this Agreement, unless the context otherwise requires: (a) the words \u201cinclude,\u201d \u201cincludes,\u201d and \u201cincluding\u201d are deemed to be followed by the words \u201cwithout limitation\u201d; (b) the word \u201cor\u201d is not exclusive; (c) references to \u201cwritten\u201d or \u201cin writing\u201d include electronic transmission; (d) references to any statute or regulation include any amendment, successor, or re-codification thereof and all rules and regulations promulgated thereunder; (e) headings and captions are for convenience of reference only and do not affect interpretation; (f) all accounting terms not otherwise defined have the meanings given under GAAP; and (g) this Agreement is the product of negotiation between sophisticated parties, each represented by counsel, and no rule of construction resolving ambiguities against the drafting party shall apply.")

section(doc, "1.3", "Relationship to Term Sheet; Conflicts.")
para(doc, "This Agreement and the other Loan Documents constitute the definitive documentation contemplated by the Term Sheet dated January 10, 2025 between Lender and Borrower (the \u201cTerm Sheet\u201d) and supersede the Term Sheet in its entirety with respect to the subject matter hereof, except for those provisions of the Term Sheet stated therein to be binding (Sections 22 and 23 thereof), which survive in accordance with their terms. In the event of any conflict between the terms of this Agreement and the terms of any other Loan Document, the terms of this Agreement shall control as between Lender and Borrower; provided, however, that the terms of the Deed of Trust shall control with respect to matters of title, foreclosure, and the creation, perfection, and enforcement of Liens.")
draftnote(doc, "Section 1.3 resolves the non-binding/binding structure of the Term Sheet. Open items inherited from the Term Sheet that cannot be resolved by interpretation (e.g., the 80% LTC and 65% LTV covenants against a loan that computes to 83.77% LTC and 65.25% LTV) are bracketed in the operative sections and addressed in Cover Memorandum Items A-1, A-2, and A-3.")

# ------------------------------------------------------------------ ARTICLE 2
article(doc, "ARTICLE 2", "The Loan; Interest; Fees; Payments")

section(doc, "2.1", "The Loan; Loan Amount.")
para(doc, "Subject to the terms and conditions of this Agreement, Lender agrees to make Advances to Borrower from time to time during the Construction Period in an aggregate principal amount not to exceed at any time outstanding the Loan Amount of $47,500,000 [Alternative B: $45,360,000]. Borrower\u2019s obligation to repay the Loan shall be evidenced by the Note and by Lender\u2019s ledger, which shall be conclusive absent manifest error.")
para(doc, "Notwithstanding the foregoing, if on or before the Closing Date the Loan-to-Cost Ratio or the Loan-to-Value Ratio computed in accordance with Article 9 would exceed the applicable maximum set forth in Sections 9.1 or 9.2 (computed, on the date hereof, at 83.77% and 65.25%, respectively, against maximums of 80.00% and 65.00%), the Commitment shall automatically be reduced, without further action by any party, to the largest principal amount that, together with the Equity Contribution and the Mezzanine Loan, is fully applied to Total Project Costs and results in compliance with Sections 9.1 and 9.2 (which amount, on the basis of Total Project Costs of $56,700,000 and the As-Completed Value of $72,800,000, is $45,360,000). Borrower shall fund any resulting funding gap as an additional Equity Contribution.")
draftnote(doc, "Two mutually inconsistent constraints are inherited from the source documents: the Term Sheet (Sections 4, 5.2 and 6.1) fixes the Loan at $47,500,000 but caps LTC at 80% of $56,700,000 of Total Project Costs ($45,360,000) and caps as-completed LTV at 65% of $72,800,000 ($47,320,000); the Credit Memorandum records LTC of 83.77% and LTV of 65.25% yet marks as-completed LTV a \u201cPass\u201d by applying a 70% policy maximum rather than the 65% maximum stated in the Term Sheet. Section 2.1 is drafted to make the arithmetic self-correcting. Counsel recommends the Senior Loan Committee choose between (i) reducing the Commitment to $45,360,000 with a $2,140,000 cash Equity Contribution (the only arithmetic cure; see Cover Memorandum Item A-1), or (ii) approving the Loan at $47,500,000 with express Committee-approved covenant levels of 83.77% LTC and 65.25% LTV and compensating conditions.")

section(doc, "2.2", "Purpose; Nature of the Facility.")
para(doc, "The proceeds of the Loan shall be used solely to pay Project Costs in accordance with the Approved Budget and Section 2 of Schedule 3, and for no other purpose. Borrower shall not use any proceeds of the Loan for any purpose that would violate Regulation U or Regulation X of the Board of Governors of the Federal Reserve System or any other applicable law.")
para(doc, "The Term Sheet describes the Loan as a \u201csingle advance facility.\u201d For the avoidance of doubt, the Commitment is established once and is non-revolving; proceeds are advanced in multiple milestone-based Advances as provided in Article 5 and Schedule 4, and no amount repaid or prepaid may be re-borrowed. The \u201csingle advance\u201d characterization is not intended to limit, and does not limit, the number or timing of Advances, and any requirement that Borrower pay an unused line fee under Section 2.6(c) shall be construed consistently with this Section 2.2.")
draftnote(doc, "Term Sheet Section 3.1 characterizes the Loan as a \u201csingle advance facility\u201d while Section 9.2 provides for nine milestone draws and Section 3.4 imposes an unused line fee measured on \u201cthe average daily undrawn commitment amount.\u201d These three provisions are inconsistent (an unused line fee is a revolving-facility concept). Section 2.2 preserves the fee while clarifying that the Commitment is non-revolving. Confirm with the Senior Loan Committee whether the Committee intends to retain the Unused Line Fee (approximately $119,000 over a 30-month construction period on a $19,000,000 average undrawn balance), which is not included in the Approved Budget. See Cover Memorandum Item K-2.")

section(doc, "2.3", "Interest Rate.")
para(doc, "Interest on the outstanding principal balance of the Loan shall accrue at the Applicable Rate for each day such principal balance is outstanding, calculated on the basis of the actual number of days elapsed over a 360-day year. Interest shall be payable monthly in arrears on each Monthly Payment Date, commencing on the first Monthly Payment Date following the Closing Date, and on the Maturity Date.")
para(doc, "During the Construction Period, and for so long as funds remain available in the Interest Reserve Account, accrued interest shall be paid from the Interest Reserve Account in accordance with Section 5.5. If and to the extent the Interest Reserve Account is insufficient or exhausted, Borrower shall pay all accrued interest from its own funds on each Monthly Payment Date, time being of the essence.")

section(doc, "2.4", "Daily Simple SOFR; SOFR Floor; Conforming Changes.")
para(doc, "Daily Simple SOFR shall be determined by Lender for each day based on the SOFR published for such day (or, if such day is not a SOFR Business Day, the SOFR published for the immediately preceding SOFR Business Day). Lender\u2019s determination of Daily Simple SOFR and of the Applicable Rate shall be conclusive absent manifest error. In no event shall Daily Simple SOFR be less than the SOFR Floor of 1.00% per annum.")
para(doc, "If Lender determines that (a) SOFR has been permanently or indefinitely discontinued or is no longer representative, (b) the administrator of SOFR or its regulator has made a public statement announcing that SOFR will cease to be provided, or (c) SOFR is not available for any reason, then Lender and Borrower shall negotiate in good faith to establish a successor benchmark rate consistent with the recommended best practices of the Alternative Reference Rates Committee, including any applicable spread adjustment, and Lender may make conforming changes to the mechanics of determining and administering the rate (including the timing and frequency of determinations, the definition of \u201cBusiness Day,\u201d and the manner of calculating interest). Until a successor rate is established, interest shall continue to accrue at the Applicable Rate determined using the most recently available SOFR.")
para(doc, "If any change in law, regulation, or interpretation thereof after the Closing Date makes it unlawful or impracticable for Lender to maintain the Loan based on SOFR, Lender may, by notice to Borrower, convert the Loan to a successor rate of interest reasonably selected by Lender (including a cost-of-funds-based rate), and Borrower shall pay such rate from and after the date specified in such notice. If any change in law or regulation increases Lender\u2019s costs of making or maintaining the Loan, or reduces any amount received by Lender, Lender may require Borrower to pay such additional amounts as are necessary to compensate Lender, in each case upon delivery of a certificate setting forth in reasonable detail the basis for such determination, which certificate shall be conclusive absent manifest error.")
draftnote(doc, "Term Sheet Section 3.3 requires ARRC-consistent benchmark replacement provisions. The successor-rate mechanics are drafted to be operative without Lender discretion to select a rate unilaterally in the first instance, consistent with ARRC best practice. Confirm the SOFR Floor of 1.00% remains appropriate given a current SOFR of approximately 4.35%.")

section(doc, "2.5", "Default Rate.")
para(doc, "Upon the occurrence and during the continuance of an Event of Default, and after maturity of the Loan whether by acceleration or otherwise, the outstanding principal balance of the Loan and, to the extent permitted by applicable law, all accrued and unpaid interest, fees, and Other Charges, shall bear interest at the Default Rate. Interest at the Default Rate shall be payable on demand and shall accrue until the earlier of the date on which such Event of Default is cured or waived in writing by Lender or the date on which all amounts owing under the Loan Documents are indefeasibly paid in full.")

section(doc, "2.6", "Fees.")
sub(doc, "(a)", "Origination Fee. Borrower shall pay Lender a non-refundable origination fee of $475,000 (1.00% of the Loan Amount), earned upon the Closing Date. The Origination Fee may be funded from Loan proceeds as a Project Cost included in the Approved Budget and advanced with the Initial Advance, and Borrower irrevocably authorizes Lender to retain such amount from the Initial Advance in satisfaction of this Section 2.6(a).")
sub(doc, "(b)", "Exit Fee. Borrower shall pay Lender an exit fee in an amount equal to (i) 0.50% of the outstanding principal balance of the Loan at the time of repayment, if the Loan is repaid in full at any time during the Construction Period; (ii) 0.25% of the outstanding principal balance of the Loan at the time of repayment, if the Loan is repaid in full during the first six (6) months of the Mini-Perm Period; and (iii) zero, if the Loan is repaid in full after the first six (6) months of the Mini-Perm Period. The Exit Fee shall also be payable upon acceleration of the Loan or upon any repayment resulting from foreclosure, deed in lieu, or other realization on the Collateral.")
sub(doc, "(c)", "Unused Line Fee. Borrower shall pay Lender a fee at the rate of 0.25% per annum on the average daily undrawn amount of the Commitment (determined as the Loan Amount less the average daily outstanding principal balance of the Loan during the applicable period), payable quarterly in arrears commencing on the first quarterly date following the Closing Date.")
sub(doc, "(d)", "Extension Fee. If Borrower exercises the Extension Option, Borrower shall pay Lender an extension fee equal to 0.25% of the then-outstanding principal balance of the Loan, payable on or before the Mini-Perm Maturity Date as a condition to such extension.")
sub(doc, "(e)", "Other Fees and Charges. Borrower shall pay all Other Charges when due, including Lender\u2019s inspection fees, appraisal and reappraisal costs, environmental consulting costs, title premiums and endorsement charges, recording and filing fees, and Lender\u2019s reasonable attorneys\u2019 fees and disbursements.")
draftnote(doc, "Term Sheet Section 3.4 states that the Origination Fee is \u201cpayable in full at closing\u201d while Term Sheet Section 11 makes \u201cPayment of the origination fee in the amount of $475,000\u201d a condition precedent to closing, and Term Sheet Section 3.4 also permits the fee to be \u201cfunded from Loan proceeds.\u201d Section 2.6(a) adopts the funded-from-proceeds construction (which is consistent with Draw 1 of the Term Sheet draw schedule) and eliminates the circularity. The Exit Fee and the Unused Line Fee are not included in the Approved Budget and are not funded by any reserve; they must be paid from Borrower\u2019s own funds. See Cover Memorandum Items F-2 and K-2.")

section(doc, "2.7", "Late Charge.")
para(doc, "If any installment of principal, interest, or any Other Charge is not paid on or before the fifth (5th) Business Day after the date on which it is due, Borrower shall pay to Lender, on demand, a late charge equal to five percent (5.00%) of the amount so overdue, in addition to interest at the Default Rate. Borrower acknowledges that such late charge represents a fair and reasonable estimate of the costs Lender will incur by reason of late payment and is not a penalty, and Borrower agrees that it is reasonable and fair compensation for the additional administrative and processing costs and the loss of use of funds occasioned by such late payment.")
draftnote(doc, "The Term Sheet and Credit Memorandum are silent on late charges; the 5.00% late charge in Section 2.7 is a customary provision not addressed in the Term Sheet and requires Senior Loan Committee confirmation before delivery. See Cover Memorandum Item K-3. The five (5) Business Day threshold is conformed to the five (5) day monetary grace period in Term Sheet Section 15; see also Section 15.1(a) and Cover Memorandum Item K-3.")

section(doc, "2.8", "Payments; Application; Prepayment.")
para(doc, "All payments of principal, interest, fees, and Other Charges shall be made in lawful money of the United States, in immediately available funds, to the account designated by Lender in writing, not later than 2:00 p.m. Eastern Time on the due date. Any payment received after such time shall be deemed received on the next Business Day. All payments received shall be applied in the following order: (a) Other Charges (other than amounts added to principal); (b) fees; (c) accrued and unpaid interest; (d) principal then due; and (e) any remaining amounts, in such order as Lender determines, all in accordance with the Deed of Trust and applicable law.")
para(doc, "Borrower may prepay the Loan in whole or in part at any time, without premium or penalty other than payment of the Exit Fee expressly provided in Section 2.6(b) and any Other Charges then due, upon not less than five (5) Business Days\u2019 prior written notice to Lender. Any partial prepayment shall be applied to the outstanding principal balance and shall not relieve Borrower of its obligation to pay any subsequent installment of interest or of the obligation to make the Advances contemplated by this Agreement. No amount repaid or prepaid may be re-borrowed.")

section(doc, "2.9", "Maximum Lawful Rate.")
para(doc, "Notwithstanding anything to the contrary in this Agreement or any other Loan Document, no provision of the Loan Documents shall require the payment or permit the collection of interest in excess of the maximum rate permitted by applicable law. If any excess interest is provided for or determined to have been received by Lender, then (a) the excess shall be deemed to have been applied to reduce the principal balance of the Loan, and (b) if the Loan has been paid in full, Lender shall refund such excess to Borrower. To the extent permitted by law, all amounts constituting interest shall be amortized, prorated, allocated, and spread over the full term of the Loan.")

section(doc, "2.10", "Payments Not Set Aside.")
para(doc, "If any payment received by Lender is subsequently invalidated, declared to be fraudulent or preferential, set aside, or required to be repaid to a trustee, receiver, or any other Person under any bankruptcy, insolvency, or similar law, then the obligation to which such payment related shall be revived and shall continue in full force and effect as if such payment had not been received by Lender.")


LET = "abcdefghijklmnopqrstuvwxyz"
def lettered(items, reorder=None):
    idx = reorder if reorder is not None else list(range(len(items)))
    for lab, i in zip(LET, idx):
        sub(doc, "(%s)" % lab, items[i])

# ------------------------------------------------------------------ ARTICLE 3
article(doc, "ARTICLE 3", "Conditions Precedent to Closing")
section(doc, "3.1", "Conditions Precedent.")
para(doc, "Lender\u2019s obligation to make the Initial Advance is subject to the satisfaction (or written waiver by Lender in its sole discretion) of each of the following conditions on or before the Closing Date, each in form and substance satisfactory to Lender and Lender\u2019s counsel:")
CP = [
"Loan Documents. Borrower, each Guarantor, and each member of Borrower shall have executed and delivered each Loan Document to which it is a party, including this Agreement, the Note, the Deed of Trust, the Assignment of Leases and Rents, the Security Agreement, the Pledge Agreements, the Guaranties, the Environmental Indemnity, the Equity Escrow Agreement, the Cash Management Agreement, and the Intercreditor Agreement, each duly executed, acknowledged where required, and in recordable form.",
"Equity Contribution. Borrower shall have deposited not less than $2,140,000 in cash into the Equity Escrow Account as the Equity Contribution, and Lender shall have received documentation reasonably satisfactory to it demonstrating that the source of such funds is not the Mezzanine Loan, any Affiliate of Mezzanine Lender, Brightleaf Investors Group LLC, Thomas R. Chen, or any other Indebtedness.",
"Intercreditor Agreement. The Intercreditor Agreement shall have been executed and delivered by Lender, Mezzanine Lender, Borrower, and each member of Borrower in accordance with Article 18, resolving the conflicting pledges of the Pledged Interests in favor of Lender with a first-priority security interest and providing subordination, standstill, cure, purchase-option, and bankruptcy protections satisfactory to Lender.",
"Titles and Lien Priority. Title Company shall have irrevocably committed to issue the Title Policy in the amount of the Loan Amount, insuring the Deed of Trust as a valid first-priority Lien on the fee simple estate in the Property, subject only to the Permitted Exceptions, and shall have delivered a pro forma policy, a date-down endorsement to the Closing Date, and all endorsements required by Lender (including, without limitation, ALTA 9, 14, 18, 22, and 33 endorsements and such other endorsements as Lender may reasonably require).",
"Release of Prior Deed of Trust. The Deed of Trust recorded in Book 6215, Page 892, Durham County Registry, from Foster Street Properties LLC to the trustee therein named for the benefit of Triangle Commercial Bank, dated September 14, 2018, securing an original principal amount of $3,400,000, shall have been released, satisfied, or cancelled of record, or provision therefor shall have been made through Title Company\u2019s escrow in accordance with Schedule B-I, Requirement 4 of the Title Commitment, with funds sufficient to pay the outstanding balance (as evidenced by a payoff letter dated within thirty (30) days of the Closing Date) and an indemnity satisfactory to Title Company; and Lender shall have received evidence that no obligation secured by such Deed of Trust remains unpaid.",
"Environmental Deed Notice; Permitted Exception. Borrower shall have recorded, in the Durham County Registry, the deed notice and declaration of land use restriction required by Condition 4 of the NFA Letter, in form and substance satisfactory to Lender, and the Title Policy shall except to such recorded instrument as a Permitted Exception in accordance with Schedule 2.",
"Architectural Review Approval. Borrower shall have delivered evidence that the Brightleaf Historic District Association, Inc. Architectural Review Committee has approved the Approved Plans and Specifications (or has deemed approved them upon the lapse of sixty (60) days from complete submission), and that no appeal, challenge, or injunction proceeding is pending or, to Borrower\u2019s knowledge, threatened with respect thereto.",
"Survey. Lender and Title Company shall have received the Survey in compliance with Section 13.5, showing no encroachments, overlaps, or boundary disputes other than those approved by Lender and insured over by Title Company.",
"Appraisal. Lender shall have received and approved the Appraisal, which shall confirm an As-Is Value of not less than $8,900,000, an As-Completed Value of not less than $72,800,000, and an As-Stabilized Value of not less than $76,200,000.",
"Environmental Reports. Lender shall have received and approved (a) the Phase I ESA prepared by Sentinel Environmental Consulting LLC dated October 28, 2024; (b) the Phase II investigation report dated August 30, 2024; (c) the NFA Letter; (d) the reliance letter of Sentinel Environmental Consulting LLC dated October 28, 2024 addressed to Lender; and (e) evidence that all conditions of the NFA Letter have been satisfied (other than those conditions that by their terms are to be satisfied after the Closing Date, which shall be scheduled and accepted by Lender in writing).",
"Environmental Compliance Plan. Lender shall have received (a) the design of the soil vapor mitigation system required by Condition 1 of the NFA Letter, prepared by a professional engineer licensed in North Carolina, and evidence that such design is incorporated into the Approved Plans and Specifications and the Construction Contract; (b) the soil vapor mitigation system cost center in the Approved Budget; and (c) the NCDEQ-approved soil management plan required by Condition 3 of the NFA Letter, or evidence satisfactory to Lender that such plan has been submitted for approval.",
"Restricted Area Resolution. Lender shall have received evidence satisfactory to it that no residential unit, residential common area, or other residential occupancy space is located above the Restricted Area, or, in the alternative, (a) a written determination from NCDEQ approving residential use of the Restricted Area subject to the installation and maintenance of the soil vapor mitigation system, or (b) a redesign of the Approved Plans and Specifications eliminating residential occupancy above the Restricted Area. If Lender elects in its sole discretion to permit deferral, this condition may be satisfied as a condition to Advances allocable to the Restricted Area in accordance with Section 4.3.",
"Construction Contract. Borrower shall have delivered a true and complete copy of the fully executed Construction Contract with a Guaranteed Maximum Price of $34,750,000, together with the collateral assignment thereof in favor of Lender, the Contractor\u2019s consent to such assignment, payment and performance bonds in the full amount of the Guaranteed Maximum Price, and evidence of Contractor\u2019s financial capacity and bonding capacity satisfactory to Lender.",
"Architect\u2019s Agreement. Borrower shall have delivered a true and complete copy of the fully executed Architect\u2019s Agreement with Architect, together with the collateral assignment thereof in favor of Lender and Architect\u2019s consent thereto.",
"Organizational Documents; Authority. Lender shall have received (a) certificates of good standing or existence for Borrower, each member of Borrower, and Mezzanine Lender from the North Carolina Secretary of State dated within thirty (30) days of the Closing Date; (b) certified copies of the articles of organization and the operating agreement of Borrower, as amended to incorporate the SPE covenants of Article 11 and the Independent Manager requirement of Section 11.6; (c) a certified copy of the resolutions or written consents of the members of Borrower holding not less than seventy-five percent (75%) of the membership interests authorizing the Loan, the Loan Documents, the Pledges, and all related transactions; and (d) such consents of Brightleaf Investors Group LLC as are required under Section 3.2 and Section 9.1 of Borrower\u2019s operating agreement.",
"Non-Consolidation Opinion. Lender shall have received a non-consolidation opinion of Borrower\u2019s counsel, Calloway & Strauss PLLC, addressed to Lender, in form and substance satisfactory to Lender and Lender\u2019s counsel, opining that a court applying North Carolina law would not substantively consolidate Borrower with any of its members, Mezzanine Lender, Brightleaf Investors Group LLC, Thomas R. Chen, or any of their respective Affiliates.",
"Legal Opinions. Lender shall have received opinions of Borrower\u2019s counsel as to due organization, valid existence, due authorization, execution and delivery, enforceability of the Loan Documents, the valid creation and perfection of the Liens granted to Lender, and such other matters as Lender may reasonably require.",
"Insurance. Lender shall have received certificates of insurance and, where requested, certified copies of policies evidencing all coverages required by Article 12 and Schedule 6, naming Lender as mortgagee, loss payee, and additional insured as applicable, with lender\u2019s loss payable and additional interest endorsements and thirty (30) days\u2019 notice of cancellation.",
"Financial Information. Lender shall have received (a) the Borrower\u2019s balance sheet and income statement as of a date not more than ninety (90) days prior to the Closing Date, prepared in accordance with GAAP, together with a reconciliation of Borrower\u2019s stated net worth to its documented contributed capital and recorded liabilities; (b) current personal financial statements of each Guarantor; (c) federal income tax returns of each Guarantor for the two most recent taxable years; and (d) a Compliance Certificate demonstrating Net Worth of not less than $12,000,000 and Guarantor Liquidity of not less than $5,000,000.",
"Zoning and Permits. Lender shall have received a zoning compliance letter from the City of Durham confirming that the Project is permitted as of right in the MU-D district, together with evidence of all building permits, site plan approvals, utility availability letters, and other Governmental Authority approvals necessary to commence construction.",
"No Work Performed; Lien Waivers. Lender shall have received (a) an owner\u2019s affidavit of no prior work and no materials furnished, or, if any work has been performed or materials furnished prior to the recording of the Deed of Trust, unconditional lien waivers and releases from Contractor, the demolition contractor, Sentinel Environmental Consulting LLC, and each other Person that has furnished labor, materials, or services to the Property, together with a title endorsement insuring Lender against mechanic\u2019s and materialmen\u2019s lien claims arising from such prior work; and (b) such affidavits of possession, gap indemnities, and no-lien affidavits as Title Company may require.",
"Taxes. Lender shall have received evidence that all ad valorem real property taxes and assessments affecting the Property are paid current, including the 2024 taxes for both parcels.",
"UCC and Judgment Searches. Lender shall have received UCC, tax lien, judgment, and litigation searches against Borrower, each member of Borrower, and each Guarantor, in each jurisdiction reasonably required by Lender, showing no Liens or judgments other than those approved by Lender in writing.",
"OFAC and Patriot Act. Lender shall have completed its customer identification, beneficial ownership, and OFAC screening with respect to Borrower, each Guarantor, and each member of Borrower, and shall have received all information required under Lender\u2019s applicable anti-money laundering policies.",
"Fees and Expenses. Borrower shall have paid the Origination Fee, the Expense Deposit required by Section 22 of the Term Sheet (to the extent not previously paid and applied), and all fees, costs, and expenses of Lender and Lender\u2019s counsel then due, including any amounts payable under Section 21.6.",
"Compliance Certificate. Lender shall have received a Compliance Certificate dated the Closing Date certifying that (a) all representations and warranties are true and correct, (b) no Event of Default or Default exists, (c) the Loan-to-Cost Ratio does not exceed the maximum set forth in Section 9.1, and (d) the Loan-to-Value Ratio does not exceed the maximum set forth in Section 9.2.",
"No Material Adverse Change. Since the date of the Credit Memorandum there shall have occurred no Material Adverse Effect and no material adverse change in general real estate, capital markets, or interest rate conditions.",
]
lettered(CP, reorder=[0,1,2,3,4,5,6,7,8,9,10,12,13,14,15,16,18,20,19,21,22,23,25,24,11,26])

section(doc, "3.2", "Waiver of Conditions.")
para(doc, "Lender may, in its sole discretion, fund the Initial Advance without the satisfaction of one or more of the conditions set forth in Section 3.1, and any such funding shall not constitute a waiver of such condition, which shall thereafter constitute a condition to each subsequent Advance and an affirmative covenant of Borrower to satisfy within the time period specified by Lender. No waiver of any condition shall be effective unless in writing signed by Lender.")

# ------------------------------------------------------------------ ARTICLE 4
article(doc, "ARTICLE 4", "Conditions Precedent to Each Advance")
section(doc, "4.1", "Conditions to Each Advance.")
para(doc, "Lender\u2019s obligation to make any Advance (including the Initial Advance) is subject to the satisfaction, on the date of such Advance, of each of the following conditions:")
AC = [
"No Default. No Event of Default and no Default (being any event that, with the giving of notice or the passage of time or both, would constitute an Event of Default) shall exist or would result from the making of such Advance.",
"Representations True. Each representation and warranty of Borrower and each Guarantor contained in the Loan Documents shall be true and correct in all material respects as of the date of such Advance, except to the extent such representation expressly relates to an earlier date.",
"Draw Request. Lender shall have received a complete Draw Request, executed by Borrower and, where required, certified by Contractor and Architect, not less than ten (10) Business Days prior to the requested funding date, together with the Requisition Certificate.",
"Construction Inspector Certification. Lender shall have received a written report of the Construction Inspector confirming that the milestone identified in the Draw Request has been achieved, that the percentage of completion represented by Borrower is accurate, and that the remaining undisbursed Loan proceeds together with available equity are sufficient to complete the Project in accordance with the Approved Budget.",
"Lien Waivers. Lender shall have received conditional lien waivers in statutory form under Chapter 44A of the North Carolina General Statutes from Contractor, each subcontractor, and each materialman for work performed and materials furnished through the date of the applicable Draw Request, and unconditional lien waivers for all amounts previously paid.",
"Title Date-Down. Lender shall have received a date-down endorsement to the Title Commitment (or the Title Policy, after issuance) from Title Company confirming that since the date of the prior endorsement no intervening Liens, encumbrances, or title defects have arisen, and that the Deed of Trust remains a first-priority Lien subject only to the Permitted Exceptions, together with such mechanic\u2019s lien and/or pending disbursement endorsements as Lender may require.",
"Insurance. Lender shall have received evidence that all insurance required by Article 12 is in full force and effect, with no lapse, cancellation, or reduction in coverage.",
"Equity First. The Equity Contribution in the Equity Escrow Account shall have been fully disbursed and applied to Project Costs before any Advance other than the Initial Advance is made, and in any event no Advance shall be made in an amount that would cause the ratio of the outstanding principal balance of the Loan to the aggregate Project Costs then funded and to be funded from all sources to exceed the maximum Loan-to-Cost Ratio set forth in Section 9.1.",
"Interest Reserve Adequacy. The Interest Reserve Adequacy Test shall have been satisfied in accordance with Section 5.5(d), or Borrower shall have deposited into the Interest Reserve Account the amount of any deficiency identified by such test.",
"Budget Reconciliation. Lender shall have received an updated sources and uses reconciliation demonstrating that the Project remains within the Approved Budget (as the same may have been modified with Lender\u2019s consent) and that no cost overrun exists. If any cost overrun exists, Borrower shall have funded such overrun from Equity Contribution funds (and not from Loan proceeds, Mezzanine Loan proceeds, or the Interest Reserve) before any further Advance is made.",
"Change Order Log. Lender shall have received an updated change order log identifying all Change Orders executed or pending, together with evidence of Lender\u2019s approval of each Change Order requiring consent under Section 5.7.",
"Governmental and Permit Compliance. All building permits, site plan approvals, and other approvals required for the work covered by the Draw Request shall be in full force and effect and no stop-work order, notice of violation, or other enforcement action shall be pending or threatened.",
"Environmental Compliance. Borrower shall have delivered evidence of compliance with all conditions of the NFA Letter then applicable, including (a) implementation of the soil vapor mitigation system in accordance with Section 10.3, (b) compliance with the soil management plan, and (c) submission of all required reports and filings to NCDEQ.",
"Representations and Compliance Certificate. Lender shall have received a Compliance Certificate dated the date of such Advance certifying that no Default or Event of Default exists and that all representations and warranties remain true and correct.",
"No Restricted Area Work. No Advance allocable to work located within or above the Restricted Area shall be made until the condition set forth in Section 4.3 has been satisfied.",
"No Material Adverse Change. No Material Adverse Effect shall have occurred since the date of the immediately preceding Advance or, in the case of the Initial Advance, since the date of the Credit Memorandum.",
]
lettered(AC)

section(doc, "4.2", "Advances Are Not a Waiver.")
para(doc, "The making of any Advance shall not constitute a waiver of any condition to any subsequent Advance, nor a waiver of any Default or Event of Default, whether known or unknown to Lender, nor an approval of any work, materials, or Change Order not theretofore approved in writing by Lender.")

section(doc, "4.3", "Restricted Area Holdback.")
para(doc, "Notwithstanding any other provision of this Agreement, Lender shall not be obligated to make any Advance (or any portion of an Advance) allocable to the design, construction, or improvement of any portion of the Improvements located within or directly above the Restricted Area, and Borrower shall not permit any residential unit, residential common area, or other residential occupancy space to be constructed, marketed, leased, or occupied within or above the Restricted Area, unless and until one of the following has occurred and Lender has received evidence thereof reasonably satisfactory to it: (a) NCDEQ has issued a written modification to the NFA Letter approving residential use of the Restricted Area, subject to the installation, operation, and maintenance of the soil vapor mitigation system and such other conditions as NCDEQ may impose; (b) the Approved Plans and Specifications have been revised, with Lender\u2019s written consent, to eliminate residential use within and above the Restricted Area, and Borrower has delivered updated pro forma income projections reflecting such revision; or (c) Borrower has delivered a written determination from NCDEQ, in form and substance acceptable to Lender, confirming that residential use of the floors above the Restricted Area is permitted provided that the soil vapor mitigation system is installed, operating, and maintained in accordance with the NFA Letter.")
para(doc, "Borrower acknowledges that the Approved Plans and Specifications referenced in the Phase I ESA (drawing set dated September 12, 2024 prepared by Architect) depict approximately fourteen (14) residential units above the Restricted Area, and that no evidence has been provided to Lender that NCDEQ has approved such use. Borrower further acknowledges that the environmental consultant has expressly declined to verify the spatial relationship between the Restricted Area and any proposed residential occupancy space, and that the Appraisal expressly assumes Borrower will obtain any modification, variance, or approval necessary to permit the planned use at Borrower\u2019s sole cost.")
draftnote(doc, "This is the single most important unresolved environmental issue in the file. Credit Memorandum Section 9.5 estimates that losing 14 units reduces stabilized NOI from $4,876,800 to $4,499,640 and reduces DSCR from 1.31x to 1.21x, below the 1.25x minimum, and observes that the Appraisal does not adjust value for the restriction. Because the delineation in Figure 3 to the Phase I ESA is described on an orientation (Foster Street \u201cto the north\u201d) that is inconsistent with the recorded legal descriptions (Foster Street lies along the western boundary), the affected area must be re-plotted against the Survey before the holdback can be administered. See Cover Memorandum Items D-1 and E-4.")

# ------------------------------------------------------------------ ARTICLE 5
article(doc, "ARTICLE 5", "Disbursement, Project Budget, Retainage and Cost Overruns")

section(doc, "5.1", "Advances in Accordance with Draw Schedule.")
para(doc, "Advances shall be made in accordance with the milestone draw schedule set forth on Schedule 4, subject to the conditions of Article 4. Lender shall use commercially reasonable efforts to process each complete Draw Request within ten (10) Business Days after Lender\u2019s receipt of a complete Draw Request and all required supporting documentation. Lender may, in its reasonable discretion, make Advances more or less frequently than indicated in Schedule 4, in each case consistent with the total amount of the Commitment and the conditions of this Agreement. The amount of any Advance may not exceed the lesser of (a) the amount requested in the applicable Draw Request and (b) the amount then available under the Approved Budget for the applicable budget line item, net of Retainage.")

section(doc, "5.2", "Draw Requests.")
para(doc, "Each Draw Request shall be submitted substantially in the form of Exhibit B, shall be signed by an authorized representative of Borrower, and shall include: (a) AIA Documents G702 (Application and Certificate for Payment) and G703 (Continuation Sheet), certified by Contractor and Architect; (b) the Requisition Certificate; (c) the Construction Inspector\u2019s report; (d) conditional and unconditional lien waivers as required by Section 4.1(e); (e) the title date-down endorsement required by Section 4.1(f); (f) evidence of insurance; (g) an updated construction schedule and change order log; (h) an updated sources and uses reconciliation; (i) the Interest Reserve Adequacy Certificate; and (j) such other information as Lender may reasonably require. Lender may decline to fund any Draw Request that is incomplete or that does not satisfy the conditions of Article 4.")

section(doc, "5.3", "Retainage.")
para(doc, "Lender shall withhold Retainage equal to ten percent (10%) of each Advance allocable to Hard Costs, and shall not disburse such Retainage except in accordance with Section 5.8. The aggregate Retainage on the Guaranteed Maximum Price of $34,750,000 is $3,475,000. Borrower shall cause Contractor to acknowledge the Retainage in the Construction Contract and in each Application for Payment, and no Advance shall be deemed to approve or accept any work in a manner that would limit Lender\u2019s right to withhold or recover Retainage. The Retainage shall be held by Lender (and not by Borrower or Contractor) and shall not be subject to any Lien of Contractor, any subcontractor, or any other Person.")
para(doc, "Borrower acknowledges that the draw schedule attached as Schedule 4 to the Term Sheet (and the Borrower-prepared draw schedule dated January 8, 2025 delivered to Lender) provides for each hard-cost draw to be funded at one hundred percent (100%) of the gross amount requested and then provides for a further \u201cRetainage Release\u201d draw following the certificate of occupancy, which would result in cumulative hard-cost disbursements of $38,225,000 against a Guaranteed Maximum Price of $34,750,000, an over-advance of $3,475,000. Schedule 4 to this Agreement restates the draw schedule to withhold Retainage from each Advance in accordance with this Section 5.3.")
draftnote(doc, "This paragraph records the discrepancy on the face of the Borrower\u2019s draw schedule so that it cannot later be characterized as a Lender-approved funding mechanism. Note that the Borrower\u2019s schedule also purports to fund $2,835,000 of Developer Fee and $1,440,000 of Contingency within the same draw lines, which is what creates the appearance of reconciliation. See Cover Memorandum Item F-1 for the full recomputation.")

section(doc, "5.4", "Equity First; Equity Escrow Account.")
para(doc, "Before any Advance other than the Initial Advance is made, the Equity Contribution shall have been deposited into the Equity Escrow Account and applied to Project Costs. Funds in the Equity Escrow Account shall be disbursed to pay Project Costs in the priority set forth in the Equity Escrow Agreement and shall be exhausted before any Loan proceeds are applied to the same Project Costs. Borrower shall not be entitled to any credit against the Commitment on account of the Equity Contribution, and no Advance shall be made if the making of such Advance would cause the Loan-to-Cost Ratio to exceed the maximum set forth in Section 9.1.")

section(doc, "5.5", "Interest Reserve.")
sub(doc, "(a)", "Establishment and Funding. Lender shall fund the Interest Reserve of $4,850,000 from Loan proceeds with the Initial Advance and shall hold the Interest Reserve in a segregated sub-account of the Loan (the \u201cInterest Reserve Account\u201d), which shall not constitute a deposit account of Borrower and shall bear no interest.")
sub(doc, "(b)", "Application. On each Monthly Payment Date during the Construction Period, Lender shall apply funds in the Interest Reserve Account to the payment of interest then due on the Loan (and, at Lender\u2019s election, to Other Charges then due), until the Interest Reserve Account is exhausted.")
sub(doc, "(c)", "Sole Source; No Reallocation. The Interest Reserve shall be used solely for the payment of interest and Other Charges during the Construction Period and may not be reallocated to any other budget line item, whether by budget modification, Change Order, or otherwise. Amounts remaining in the Interest Reserve Account after the Construction Maturity Date shall be applied to the outstanding principal balance of the Loan.")
sub(doc, "(d)", "Interest Reserve Adequacy Test. At each Draw Request and at least quarterly during the Construction Period, Borrower shall deliver to Lender an Interest Reserve Adequacy Certificate substantially in the form of Exhibit D, certified by the chief financial officer of Borrower, demonstrating that the remaining balance of the Interest Reserve Account, together with any additional funds Borrower has committed in writing to deposit, is sufficient to pay all projected interest on the Loan (calculated at the greater of the then-current Applicable Rate and the Applicable Rate assuming Daily Simple SOFR of 4.35%) through the earlier of (i) the next anticipated draw date and (ii) the date that is ninety (90) days after the date of such certificate. If the Interest Reserve Adequacy Test is not satisfied, Borrower shall deposit the amount of the deficiency into the Interest Reserve Account within five (5) Business Days after written demand by Lender, and no further Advance shall be made until such deposit is made.")
sub(doc, "(e)", "Replenishment; Shortfall. Borrower shall fund any shortfall in the Interest Reserve from its own funds (and not from Loan proceeds, Mezzanine Loan proceeds, or the proceeds of any other Indebtedness) within five (5) Business Days after written notice from Lender. Failure to fund any such shortfall within such period shall constitute an Event of Default under Section 15.1(a).")
sub(doc, "(f)", "Reporting. Borrower shall deliver to Lender, concurrently with each monthly construction progress report, a reconciliation of the Interest Reserve Account showing the opening balance, interest and Other Charges paid, deposits made, and closing balance, together with a projection of remaining interest costs through the Construction Maturity Date.")
draftnote(doc, "Reserve sizing is not settled in the record. The Term Sheet and Credit Memorandum fix the Interest Reserve at $4,850,000. The Credit Memorandum (Section 6.2) computes a shortfall of approximately $565,000 at a 7.60% all-in rate on an assumed $28,500,000 average outstanding balance. The Borrower\u2019s January 8, 2025 model computes a shortfall of $365,830 at the same 7.60% rate but concludes \u201cAPPEARS ADEQUATE\u201d because its headline case assumes SOFR of 3.50% (all-in 6.75%) rather than the 4.35% current rate used in the Credit Memorandum. Section 5.5(d) adopts the higher rate assumption and a draw-schedule-based projection. Senior Loan Committee should consider increasing the Interest Reserve to approximately $5,600,000 or accepting a hard replenishment covenant. See Cover Memorandum Item H-1.")

section(doc, "5.6", "Cost Overruns.")
para(doc, "Borrower shall bear all costs of completing the Project in excess of the Approved Budget and in excess of the Guaranteed Maximum Price, and shall fund each cost overrun from Equity Contribution funds within ten (10) Business Days after the earlier of (a) Borrower\u2019s knowledge of such overrun and (b) written demand by Lender. No Advance shall be made while any unfunded cost overrun exists. In no event shall any cost overrun be funded from (i) the Interest Reserve, (ii) the Retainage, (iii) any other reserve held by Lender, (iv) the Mezzanine Loan, or (v) any other borrowed funds. Lender shall have no obligation to increase the Commitment or the Loan Amount on account of any cost overrun.")

section(doc, "5.7", "Change Orders.")
para(doc, "Borrower shall not execute, and shall not permit Contractor or Architect to perform, any Change Order that (a) individually exceeds $250,000 or, together with all other Change Orders, exceeds $1,000,000 in the aggregate; (b) increases the Guaranteed Maximum Price or the Total Project Costs; (c) changes the residential unit count, the residential unit mix, the retail square footage, or the parking count; (d) affects any portion of the Improvements located within or above the Restricted Area, or the soil vapor mitigation system; (e) affects the structural system, the building envelope, or the building footprint; or (f) requires or relates to any approval of the Brightleaf Historic District Association, Inc. Architectural Review Committee, without the prior written consent of Lender in each case. Borrower shall deliver an updated change order log with each Draw Request and with each monthly construction progress report.")

section(doc, "5.8", "Retainage Release.")
para(doc, "Lender shall release the Retainage (and the final Advance identified as Draw 9 in the Term Sheet) only upon the satisfaction of each of the following conditions: (a) issuance of a final, unconditional certificate of occupancy by the City of Durham for all residential units and retail space in the Project; (b) delivery of final, unconditional lien waivers and releases from Contractor and from each subcontractor and materialman, in statutory form under Chapter 44A of the North Carolina General Statutes; (c) delivery of the Architect\u2019s certificate of final completion and the Construction Inspector\u2019s final report confirming completion in accordance with the Approved Plans and Specifications; (d) expiration of the 120-day statutory period for filing claims of lien under Chapter 44A of the North Carolina General Statutes (measured from the last furnishing of labor or materials) or, in the alternative, delivery of a lien bond or title insurance over such claims in form and amount satisfactory to Lender; (e) delivery of a final date-down endorsement of the Title Policy; (f) delivery of as-built plans and specifications, all warranties, guarantees, and operating manuals, and all Governmental Authority sign-offs; (g) confirmation that the soil vapor mitigation system has been installed, commissioned, and verified, and that all as-built drawings and performance verification reports required by the NFA Letter have been submitted to NCDEQ; and (h) no Default or Event of Default shall exist.")
para(doc, "No portion of the Retainage or of the final Advance shall be applied to the payment of the Developer Fee, Contingency, or any Distribution, and Borrower shall not submit, and Lender shall not fund, any Draw Request that includes the Developer Fee or Contingency within a Retainage Release.")
draftnote(doc, "The Borrower\u2019s draw schedule allocates $200,000 of Developer Fee and $600,000 of Contingency to Draw 9 (the \u201cRetainage Release\u201d), which is inconsistent with Section 9.1 of the Term Sheet and with the prohibition on Distributions during the Construction Period in Section 14 of the Term Sheet. See Cover Memorandum Item F-1.")

section(doc, "5.9", "Inspections.")
para(doc, "Lender and its agents, representatives, and the Construction Inspector shall have the right, at Borrower\u2019s expense, to enter upon the Property at any time during normal business hours and upon reasonable prior notice (and without notice during an emergency or following a Default) to inspect the Project, review construction documents, test materials, and interview Contractor and Architect. Borrower shall cooperate fully with all such inspections and shall cause Contractor and Architect to do the same. No inspection shall constitute an approval or acceptance of work or a waiver of any Default.")

section(doc, "5.10", "Construction Documents; Bonds; Contractor Requirements.")
para(doc, "Borrower shall cause Contractor to maintain in full force and effect throughout the Construction Period (a) payment and performance bonds in the full amount of the Guaranteed Maximum Price naming Lender as dual obligee, (b) its North Carolina general contractor\u2019s license (No. 78442), and (c) a surety rated not less than A- by A.M. Best. Borrower shall not terminate, replace, or permit the resignation of Contractor or Architect without Lender\u2019s prior written consent, and any such replacement shall be with a contractor or architect of comparable experience and financial capacity approved by Lender in writing, and shall be at Borrower\u2019s sole cost.")

section(doc, "5.11", "Protective Advances.")
para(doc, "If Borrower fails to perform any obligation required to preserve the Collateral, complete the Project, or comply with applicable law, Lender may (but shall not be obligated to) perform such obligation, and all amounts expended by Lender in doing so, together with interest thereon at the Default Rate, shall be an Advance under the Loan, shall be secured by the Collateral, and shall be repaid by Borrower on demand. Lender\u2019s exercise of this Section 5.11 shall not waive any Default or Event of Default arising from Borrower\u2019s failure.")

section(doc, "5.12", "Budget Modifications.")
para(doc, "Borrower may reallocate amounts among line items within the Approved Budget only if (a) the aggregate amount reallocated does not exceed five percent (5%) of Total Project Costs; (b) no reallocation increases the Contingency balance or any reserve line item; (c) no reallocation is made from the Interest Reserve, the Retainage, or any other Lender-held reserve; (d) no reallocation is made from Hard Costs to soft costs or financing costs, or from the soil vapor mitigation system cost center; and (e) Lender has consented in writing to each such reallocation. Any increase in Total Project Costs requires Lender\u2019s prior written consent and funding by Borrower from Equity Contribution funds.")

section(doc, "5.13", "Developer Fee.")
para(doc, "The Developer Fee in the amount of $2,835,000 (5.00% of Total Project Costs) shall be (a) fully subordinated to the Loan and to the Guaranties, (b) payable only from Project Cost savings and excess Loan proceeds actually available after all Hard Costs, soft costs, the Interest Reserve, and Contingency have been funded or reserved, (c) paid in installments not more frequently than monthly and only if no Default or Event of Default exists and no cost overrun is projected, and (d) reduced or eliminated, at Lender\u2019s election, to the extent necessary to fund any cost overrun or Interest Reserve shortfall. Borrower shall not pay, and shall not permit any Affiliate to receive, any portion of the Developer Fee from the Mezzanine Loan proceeds.")
draftnote(doc, "The Borrower\u2019s Detailed Budget funds $1,000,000 of the Developer Fee from the Mezzanine Loan and the balance ($1,835,000) from the senior Loan. Funding a developer fee from subordinated debt at closing is, in substance, a distribution of borrowed money to the sponsor at closing and is inconsistent with the Term Sheet\u2019s characterization of the land as equity and with the negative covenant on Distributions during the Construction Period (Term Sheet Section 14). Section 5.13 prohibits it. See Cover Memorandum Item A-4.")

# ------------------------------------------------------------------ ARTICLE 6
article(doc, "ARTICLE 6", "Representations and Warranties")
section(doc, "6.1", "Representations and Warranties of Borrower.")
para(doc, "Borrower represents and warrants to Lender, as of the Closing Date and as of the date of each Advance, that:")
R = [
"Organization; Good Standing. Borrower is a limited liability company duly organized, validly existing, and in good standing under the laws of the State of North Carolina, with NC Secretary of State File No. 1923847, and has full power and authority to own the Property, conduct its business, execute and deliver the Loan Documents, and perform all of its obligations thereunder.",
"Authority; Enforceability. The execution, delivery, and performance of the Loan Documents have been duly authorized by all necessary action on the part of Borrower and its members, and the Loan Documents constitute the legal, valid, and binding obligations of Borrower, enforceable against Borrower in accordance with their terms, subject to applicable bankruptcy, insolvency, reorganization, moratorium, and similar laws affecting creditors\u2019 rights generally and to general principles of equity.",
"No Conflicts. The execution, delivery, and performance of the Loan Documents do not and will not (a) violate Borrower\u2019s articles of organization or operating agreement, (b) violate any applicable law, order, or judgment, (c) result in a breach of or default under any material agreement, or (d) result in the creation of any Lien on the Property other than in favor of Lender.",
"Membership; Operating Agreement. The membership interests in Borrower are held as follows: Elena Vasquez-Torres \u2014 62% (Managing Member); Brightleaf Investors Group LLC \u2014 28%; and Reginald K. Osei \u2014 10%. The operating agreement of Borrower dated March 14, 2019, as amended through December 1, 2024 and as further amended in connection with this Agreement, is in full force and effect, and no amendment has been made thereto except as delivered to Lender. Borrower has delivered to Lender a true, correct, and complete copy of such operating agreement.",
"Capital Structure; Contributions. Attached as Schedule 3-A is a complete and accurate statement of all capital contributions made to Borrower, the date and amount of each, and the contributing member. Except as set forth on Schedule 3-A, no member of Borrower has made, and no member is obligated to make, any capital contribution to Borrower, and there are no outstanding subscriptions, options, warrants, or rights to acquire any membership interest in Borrower.",
"Litigation. There is no action, suit, proceeding, arbitration, investigation, or governmental inquiry pending or, to Borrower\u2019s knowledge, threatened against Borrower, any Guarantor, the Property, or the Project that could reasonably be expected to have a Material Adverse Effect, and Borrower is not aware of any basis for any such action.",
"Financial Statements. The financial statements and other financial information of Borrower and each Guarantor previously delivered to Lender are true, complete, and accurate in all material respects and fairly present the financial condition of Borrower and such Guarantor as of the dates thereof and the results of operations for the periods then ended. There has been no material adverse change in the financial condition of Borrower or any Guarantor since the dates of such statements.",
"Solvency. Borrower is solvent, has assets having a fair value in excess of its liabilities, and is able to pay its debts as they become due. Borrower has not entered into the Loan Documents with the intent to hinder, delay, or defraud any creditor.",
"No Default. No default or event of default exists under any material agreement, instrument, or obligation to which Borrower or any Guarantor is a party, including the Mezzanine Documents and the operating agreement of Borrower.",
"Project Budget; Plans. The Approved Budget and the Approved Plans and Specifications are true, correct, and complete, and the Approved Budget includes all costs necessary to complete the Project in accordance with the Approved Plans and Specifications. The Guaranteed Maximum Price is $34,750,000 and the Construction Contract has not been modified except as disclosed to Lender in writing.",
"Title. Borrower has good and marketable fee simple title to the Property, free and clear of all Liens except the Permitted Exceptions and the Deed of Trust, and the Deed of Trust constitutes a valid first-priority Lien on the Property subject only to the Permitted Exceptions.",
"Zoning; Permits. The Property is zoned MU-D (Mixed Use \u2014 Downtown) under the City of Durham Unified Development Ordinance, and the Project is permitted as of right without any variance, special use permit, conditional zoning, or rezoning. All permits, licenses, and approvals necessary for the construction of the Project have been obtained or will be obtained prior to the commencement of the applicable phase of construction, and all permits obtained to date are in full force and effect.",
"Compliance with Laws. The Property and the Project comply, and will comply, with all applicable laws, ordinances, rules, regulations, zoning requirements, building codes, and Environmental Laws.",
"Flood Zone. No portion of the Property is located within a Special Flood Hazard Area as designated by FEMA, and Borrower has delivered to Lender the flood zone determination required by Section 12.1(f).",
"Environmental Representations. (a) The Property is not subject to any Release of Hazardous Substances except as specifically disclosed in the Phase I ESA and the Phase II report delivered to Lender; (b) Borrower has not received any notice of violation, notice of responsibility, information request, or demand from any Governmental Authority or any other Person relating to Hazardous Substances at the Property except as disclosed in writing to Lender; (c) there are no underground storage tanks, asbestos-containing materials, polychlorinated biphenyls, or lead-based paint at the Property except as disclosed in the Phase I ESA; (d) the Property is not listed on the National Priorities List or any analogous state list, and Borrower has no knowledge of any threatened listing; (e) Borrower has complied in all respects with all conditions of the NFA Letter then applicable, including the recording of the deed notice required by Condition 4 thereof (or, if such recording has not occurred, Borrower has disclosed such non-compliance to Lender in writing and has scheduled the recording as a condition to closing under Section 3.1(f)); (f) the NFA Letter constitutes the only regulatory determination affecting the Property and has not been revoked, modified, or reopened; and (g) the soil vapor mitigation system has been designed in conformity with Condition 1 of the NFA Letter and will be installed in accordance therewith.",
"Prior Work; Liens. All labor, materials, and services furnished to the Property prior to the Closing Date have been paid for in full and unconditionally released, or will be released at closing in accordance with Section 3.1(r), and no Person has any right to claim a Lien against the Property on account of any such work. Borrower has delivered to Lender all lien waivers and affidavits required by Section 3.1(r).",
"Single-Purpose Entity. Borrower is, and at all times since its formation has been, a single-purpose entity owning no assets and conducting no business other than the ownership, development, construction, leasing, and operation of the Project.",
"Beneficial Ownership; OFAC. Neither Borrower, any Guarantor, nor any member of Borrower is (a) a Person named on any list maintained by OFAC, (b) organized or resident in a country subject to comprehensive sanctions, or (c) owned or controlled by any such Person. The information delivered to Lender pursuant to any applicable \u201cknow your customer,\u201d anti-money laundering, or beneficial ownership requirement is true and correct.",
"Investment Company; ERISA. Borrower is not an \u201cinvestment company\u201d within the meaning of the Investment Company Act of 1940 and is not a \u201cbenefit plan investor\u201d within the meaning of Section 3(42) of ERISA.",
"Brokers. No broker, finder, or placement agent is entitled to any commission or fee in connection with the Loan based on any arrangement made by Borrower.",
"Pledge; Perfection. The Pledge Agreements create in favor of Lender a valid, perfected security interest in the Pledged Interests, subject only to the subordinated pledge in favor of Mezzanine Lender created under the Intercreditor Agreement, and all consents required under Borrower\u2019s operating agreement and from each member of Borrower to the pledge have been obtained.",
"Taxes. All federal, state, and local tax returns required to be filed by Borrower have been filed, and all taxes shown thereon to be due have been paid. There are no tax Liens on the Property other than the Permitted Exceptions.",
"Insurance. Borrower maintains, and will maintain, all insurance required by Article 12, and each insurer is authorized to do business in North Carolina and has a rating of not less than A- by A.M. Best.",
"Use of Proceeds. The proceeds of the Loan will be used solely for the purposes described in Section 2.2, and no portion of the proceeds will be used to purchase or carry margin stock or to fund any Distribution.",
]
lettered(R)

section(doc, "6.2", "Representations and Warranties of Guarantors.")
para(doc, "Each Guarantor represents and warrants to Lender, as of the Closing Date and as of the date of each Advance, that: (a) such Guarantor has full capacity, power, and authority to execute, deliver, and perform the Guaranties, and the Guaranties constitute the legal, valid, and binding obligations of such Guarantor, enforceable in accordance with their terms; (b) all financial statements and personal financial statements delivered by such Guarantor to Lender are true, correct, and complete in all material respects, and such Guarantor\u2019s representations as to net worth and liquidity are accurate; (c) there is no pending or threatened litigation, judgment, bankruptcy, or insolvency proceeding against such Guarantor; (d) such Guarantor is not subject to any OFAC sanctions; and (e) such Guarantor is not a member, officer, employee, or Affiliate of Mezzanine Lender, Brightleaf Investors Group LLC, or Thomas R. Chen, other than, in the case of Elena Vasquez-Torres, her membership in Borrower.")

section(doc, "6.3", "Survival; Reliance.")
para(doc, "All representations and warranties in this Article 6 shall survive the Closing Date and the making of each Advance and shall remain in full force and effect until the Loan has been indefeasibly paid in full and all obligations of Lender under the Loan Documents have terminated. Borrower acknowledges that Lender has relied, and will rely, on such representations and warranties in making the Loan, and that any material inaccuracy shall constitute an Event of Default under Section 15.1(b).")

# ------------------------------------------------------------------ ARTICLE 7
article(doc, "ARTICLE 7", "Affirmative Covenants")
section(doc, "7.1", "Affirmative Covenants.")
para(doc, "Until the Loan has been indefeasibly paid in full, Borrower shall, at its sole cost and expense:")
AFF = [
"Maintenance of Existence; Compliance. Maintain its existence and good standing under the laws of the State of North Carolina, remain qualified to do business in each jurisdiction in which qualification is required, and comply with all applicable laws, ordinances, rules, regulations, and orders, including all Environmental Laws and all conditions of the NFA Letter.",
"Construction and Completion. Complete the construction of the Project in accordance with the Approved Plans and Specifications, the Approved Budget, the Construction Contract, and the construction schedule, and achieve Substantial Completion on or before the Construction Maturity Date.",
"Performance of Contracts. Perform all of its obligations under the Construction Documents and cause Contractor and Architect to perform theirs, and enforce all warranties, guarantees, and indemnities relating to the Project.",
"Books and Records; Inspections. Maintain complete and accurate books and records in accordance with GAAP, and permit Lender and its agents to examine and audit such books and records and to inspect the Property at any time upon reasonable notice.",
"Insurance. Maintain in full force and effect all insurance required by Article 12, with Lender named as mortgagee, loss payee, and additional insured as applicable, and deliver evidence of renewal not less than ten (10) days prior to each expiration.",
"Taxes and Assessments. Pay all real estate taxes, assessments, and governmental charges affecting the Property before they become delinquent, and deliver evidence of payment upon request.",
"Reporting. Deliver the reports, certificates, and financial information set forth on Schedule 7 at the times specified therein, each in form and substance reasonably satisfactory to Lender.",
"Compliance with Financial Covenants. Comply with each of the financial covenants set forth in Article 9 and Schedule 5, and deliver a Compliance Certificate with each annual and quarterly report.",
"Notice of Material Events. Promptly, and in any event within five (5) Business Days, notify Lender in writing of (a) any Default or Event of Default; (b) any litigation, arbitration, or governmental proceeding against Borrower, any Guarantor, the Property, or the Project involving an amount in excess of $100,000; (c) any material adverse change in the financial condition of Borrower or any Guarantor; (d) any casualty, condemnation, or taking affecting the Property; (e) any notice of violation, information request, or enforcement action from any Governmental Authority, including NCDEQ, relating to the Property or the Project; (f) any Release of Hazardous Substances at, on, under, or migrating from the Property; (g) any default or event of default under the Mezzanine Documents or the Intercreditor Agreement; (h) any change in the identity of the Independent Manager; and (i) any event that could reasonably be expected to delay Substantial Completion beyond the Construction Maturity Date.",
"Environmental Compliance. Comply with Article 10 and Schedule 8 in all respects, including all conditions of the NFA Letter and all requirements of the soil management plan, and maintain the soil vapor mitigation system in good working order.",
"Permitted Exceptions. Comply with all covenants, conditions, and restrictions affecting the Property, including the Declaration of Covenants, Conditions, and Restrictions recorded in Book 6984, Page 1155, Durham County Registry, and all requirements of the Brightleaf Historic District Association, Inc.",
"Further Assurances. Execute, deliver, and record such further instruments, financing statements, continuation statements, affidavits, and other documents as Lender may reasonably require to create, perfect, maintain, or enforce the Liens granted to Lender or to carry out the purposes of the Loan Documents.",
"Separate Accounts. Maintain its own bank accounts, books, records, and financial statements, separate and apart from those of any member, Affiliate, or other Person, and hold itself out as a separate and distinct entity.",
"Leasing. Conduct all leasing of the Property on commercially reasonable terms and on forms approved by Lender, and deliver copies of all leases, and thereafter all leasing reports, to Lender upon request.",
"Management. Cause the Property to be managed by a professional property management firm approved by Lender in writing, pursuant to a management agreement in form and substance satisfactory to Lender and collaterally assigned to Lender.",
"Interest Rate Protection. If the Extension Option is exercised, obtain and maintain an interest rate cap agreement for the duration of the extended Mini-Perm Period, with a strike rate and counterparty acceptable to Lender, and collaterally assign such agreement to Lender.",
"Required Reserve Deposits. Fund the Interest Reserve shortfall, the Equity Contribution, and all other reserves and deposits required under this Agreement within the time periods specified.",
"Guarantor Obligations. Cause each Guarantor to perform its obligations under the Guaranties, and cause each Guarantor to deliver the financial information and certifications required by Schedule 7.",
]
lettered(AFF, reorder=[0,1,2,3,4,5,6,7,8,9,10,11,13,15,12,14,16,17])

# ------------------------------------------------------------------ ARTICLE 8
article(doc, "ARTICLE 8", "Negative Covenants")
section(doc, "8.1", "Negative Covenants.")
para(doc, "Until the Loan has been indefeasibly paid in full, Borrower shall not, without Lender\u2019s prior written consent:")
NEG = [
"Additional Indebtedness. Incur, assume, guarantee, or permit to exist any Indebtedness other than the Permitted Indebtedness.",
"Liens. Create, incur, assume, or permit to exist any Lien on the Property, the Collateral, or any membership interest in Borrower, other than the Permitted Exceptions, the Liens in favor of Lender, and the subordinated pledge in favor of Mezzanine Lender permitted under the Intercreditor Agreement.",
"Transfers. Sell, assign, transfer, convey, or otherwise dispose of the Property, any interest therein, or any direct or indirect interest in Borrower, or permit any Transfer (including any dilution arising under Section 5.3 of Borrower\u2019s operating agreement or any change in control of any member of Borrower).",
"Change of Ownership or Structure. Change, modify, or otherwise alter the ownership structure, membership interests, or governing documents of Borrower, or admit any new member, or permit any member to withdraw.",
"Amendments to Operating Agreement. Amend, restate, or otherwise modify the operating agreement or articles of organization of Borrower in any material respect, including any amendment affecting capital contributions, distributions, management authority, major decision thresholds, or bankruptcy authority.",
"Affiliate Transactions. Enter into, or permit to exist, any transaction or agreement with any member, Guarantor, Affiliate, Mezzanine Lender, Brightleaf Investors Group LLC, or Thomas R. Chen, except on arm\u2019s-length terms and for fair and reasonable consideration, and only with Lender\u2019s prior written consent (which shall not be required for the Mezzanine Loan and the Intercreditor Agreement as in effect on the Closing Date).",
"Distributions. Make any Distribution during the Construction Period, other than payment of the Developer Fee strictly in accordance with Section 5.13; and thereafter make any Distribution at any time when a Default or Event of Default exists, when any Interest Reserve shortfall, cost overrun, or Equity Contribution funding obligation remains unfunded, or when any financial covenant in Article 9 is not satisfied.",
"Modifications to Construction Documents. Amend, modify, terminate, or waive any provision of the Construction Contract or the Architect\u2019s Agreement in any material respect, or execute any Change Order not permitted under Section 5.7.",
"Change in Use or Scope. Change the use of the Property, the residential unit count or mix, the retail square footage, the parking count, the building height, or the scope of the Project.",
"Restricted Area. Construct, market, lease, or permit occupancy of any residential space within or above the Restricted Area except in compliance with Section 4.3, or take any action that would violate any condition of the NFA Letter or any recorded land use restriction.",
"Environmental Actions. Cause or permit any Release of Hazardous Substances at, on, under, or from the Property; install or permit any underground storage tank; or fail to comply with any Environmental Law or any condition of the NFA Letter.",
"Change of Contractor or Architect. Terminate, replace, or permit the resignation of Contractor or Architect, or approve any substitution of any major subcontractor, without Lender\u2019s prior written consent.",
"Change in Fiscal Year or Accounting. Change its fiscal year or its method of accounting, except as required by GAAP.",
"Nature of Business. Engage in any business or activity other than the ownership, development, construction, leasing, management, and operation of the Project.",
"Mezzanine Documents. Amend, modify, or waive any provision of the Mezzanine Documents in any manner that would increase the principal amount, change the maturity, increase the interest rate, or expand the collateral, without Lender\u2019s prior written consent.",
"Judgments. Permit any judgment or judgments in the aggregate exceeding $500,000 to remain unsatisfied, unbonded, or unstayed for a period of thirty (30) days.",
"Independent Manager. Remove or replace the Independent Manager without Lender\u2019s prior written consent, or take any action requiring the vote of the Independent Manager without obtaining such vote.",
]
lettered(NEG)
draftnote(doc, "Section 8.1(j) is a Lender-protective addition not found in the Term Sheet: the Term Sheet\u2019s environmental covenant (Section 17) requires compliance with the NFA Letter but does not expressly prohibit residential use of the Restricted Area, which is the operative restriction. The negative covenant closes that gap and is reinforced by Section 4.3.")

# ------------------------------------------------------------------ ARTICLE 9
article(doc, "ARTICLE 9", "Financial Covenants and Testing")
section(doc, "9.1", "Loan-to-Cost Ratio.")
para(doc, "Borrower shall not permit the Loan-to-Cost Ratio to exceed 80.00% at any time during the term of the Loan, tested (a) on the Closing Date, (b) at each Advance, and (c) upon each modification of the Approved Budget or the Project Budget.")
para(doc, "For purposes of this Section 9.1, \u201cTotal Project Costs\u201d means $56,700,000, being the aggregate of all Project Costs set forth in the Approved Budget, as the same may be increased with Lender\u2019s written consent to reflect costs actually incurred or to be incurred, including any increase in the Interest Reserve under Section 5.5, any budget line item omitted from the Project Budget as originally delivered (including the Unused Line Fee, the Exit Fee, and pre-closing demolition and remediation costs), and any other cost of completing the Project. On the date of this Agreement, the Loan-to-Cost Ratio computed as of the Closing Date on the basis of Loan Amount of $47,500,000 and Total Project Costs of $56,700,000 equals 83.77%, which exceeds the maximum permitted by this Section 9.1 by 3.77 percentage points, or $2,140,000. Compliance with this Section 9.1 therefore requires either that the Commitment be reduced to $45,360,000 in accordance with Section 2.1, or that Total Project Costs be increased to not less than $59,375,000 through the addition of omitted Project Costs funded by the Equity Contribution.")
draftnote(doc, "The second paragraph is intentionally transparent about the non-compliance. An equity escrow deposit of $2,140,000 does not, by itself, cure an LTC breach, because it changes neither the numerator (the Loan Amount) nor the denominator (Total Project Costs). The Credit Memorandum\u2019s proposed remedy (Section 5.3 and Condition 10.1.2) therefore does not achieve what it states. See Cover Memorandum Item A-1 for the full analysis and the recommended cure.")

section(doc, "9.2", "Loan-to-Value Ratio.")
para(doc, "Borrower shall not permit (a) the Loan-to-Value Ratio based on the As-Completed Value to exceed 65.00%, or (b) the Loan-to-Value Ratio based on the As-Stabilized Value to exceed 65.00%, in each case tested on the Closing Date and thereafter upon each reappraisal and each extension of the Loan. On the basis of the Appraisal and the Loan Amount, the As-Completed Loan-to-Value Ratio is 65.25% ($47,500,000 \u00f7 $72,800,000) and the As-Stabilized Loan-to-Value Ratio is 62.34% ($47,500,000 \u00f7 $76,200,000); compliance with clause (a) of this Section 9.2 therefore requires that the Loan Amount not exceed $47,320,000 (65.00% of $72,800,000).")
draftnote(doc, "Term Sheet Sections 4 and 6.2 impose a 65% maximum as-completed LTV, but the Loan as sized computes to 65.25%, exceeding that maximum by $180,000. The Credit Memorandum\u2019s underwriting table (Section 6.1) shows the same 65.25% but marks it \u201cPass\u201d against a stated \u201cBank Policy\u201d maximum of 70%, which conflicts with the Term Sheet. Section 9.2 preserves the Term Sheet\u2019s 65% cap and discloses the arithmetic. If the Committee intends a 70% maximum, Sections 4 and 6.2 of the Term Sheet and Section 6.1 of the Credit Memorandum must be conformed. See Cover Memorandum Item A-2.")

section(doc, "9.3", "Debt Service Coverage Ratio.")
para(doc, "Borrower shall maintain a DSCR of not less than 1.25x, tested (a) at the commencement of the Mini-Perm Period on a projected basis determined in accordance with Schedule 5, using projected stabilized Net Operating Income and interest-only Debt Service at the Applicable Rate then in effect, (b) annually thereafter on the basis of actual trailing twelve-month Net Operating Income, and (c) at the time of any extension of the Loan under Article 22.")
para(doc, "If the DSCR is less than 1.25x at any testing date, Borrower shall, at Lender\u2019s election, either (a) make a principal curtailment of the Loan in the amount necessary to restore the DSCR to not less than 1.25x, or (b) deposit cash collateral with Lender in an amount determined by Lender to be sufficient to restore the DSCR to not less than 1.25x, in either case within thirty (30) days after written demand. Amounts so deposited shall be held by Lender as additional Collateral, shall not bear interest, and shall be applied to the Loan at maturity or upon acceleration.")
para(doc, "Borrower acknowledges that the Project is projected to achieve Substantial Completion on or about August 31, 2027 and stabilized occupancy on or about May 2028, and that accordingly there will be no actual trailing twelve-month Net Operating Income for the Property as of the commencement of the Mini-Perm Period. The testing described in clause (a) of this Section 9.3 shall therefore be performed on a projected basis, and the first actual trailing twelve-month test shall be performed as of the last day of the twelfth full calendar month following the issuance of the final certificate of occupancy.")
draftnote(doc, "Term Sheet Section 6.3 requires the DSCR to be \u201ctested at the commencement of the Mini-Perm Period and annually thereafter based on actual trailing twelve-month net operating income.\u201d Because the Construction Maturity Date (August 28, 2027) precedes the projected substantial completion date (August 31, 2027) and stabilization (approximately May 2028, per the Appraisal), a literal application of the covenant would produce a DSCR of zero and an immediate Event of Default. Section 9.3 resolves this by prescribing a projected test at the commencement of the Mini-Perm Period. See Cover Memorandum Item G-3.")

section(doc, "9.4", "Borrower Net Worth.")
para(doc, "Borrower shall maintain a minimum Net Worth of $12,000,000, tested annually as of the last day of each fiscal year, evidenced by a Compliance Certificate delivered within one hundred twenty (120) days after the end of such fiscal year. For purposes of this Section 9.4, \u201cNet Worth\u201d means Total Assets less Total Liabilities determined in accordance with GAAP, [Alternative: excluding the outstanding principal amount of the Loan and the Mezzanine Loan and valuing the Property at its most recent As-Completed or As-Stabilized Value, as applicable].")
draftnote(doc, "As drafted in the Term Sheet (Section 6.4) and the Credit Memorandum (Section 10.3), the $12,000,000 minimum net worth covenant cannot be satisfied once the Loan is funded. The Project is 100% debt-financed ($47,500,000 senior plus $9,200,000 mezzanine equal to Total Project Costs of $56,700,000), so Borrower\u2019s book equity after closing and full draw is approximately zero. The Credit Memorandum reconciles the stated $14,200,000 net worth to \u201ccapital contributions\u201d of only $8,200,000 (the land, per the organizational chart) and shows a cushion of only $2,200,000 over the covenant; the organizational chart, the Appraisal, the Phase I ESA, and the Title Commitment give three different acquisition dates and two different sources of the land, so the $14,200,000 figure is not supported by any document in the record. The bracketed alternative (net worth excluding Project debt, i.e., an equity-value test) is the commercially workable formulation. See Cover Memorandum Item B-1.")

section(doc, "9.5", "Guarantor Liquidity.")
para(doc, "The Guarantors shall maintain combined Guarantor Liquidity of not less than $5,000,000, tested quarterly, evidenced by a certificate of each Guarantor delivered within forty-five (45) days after the end of each fiscal quarter. For purposes of this Section 9.5, Guarantor Liquidity excludes (a) any interest in Borrower, (b) any asset pledged to another lender, (c) any asset subject to a Lien, and (d) any asset that is not convertible to cash within thirty (30) days.")

section(doc, "9.6", "Testing; Cure; Remedies.")
para(doc, "Each financial covenant shall be tested as provided in Schedule 5, and Borrower shall deliver with each Compliance Certificate a detailed calculation of each covenant. If Borrower fails to comply with any financial covenant, Borrower may, within thirty (30) days after written demand by Lender, cure such failure by (a) making a principal prepayment of the Loan, (b) depositing cash collateral with Lender, or (c) making an additional Equity Contribution, in each case to the extent such action would restore compliance, provided that Borrower may not exercise such cure right more than twice during the term of the Loan and may not exercise such cure right with respect to the Loan-to-Cost Ratio covenant or the Loan-to-Value Ratio covenant. The failure to comply with any financial covenant (after the expiration of any applicable cure period) shall constitute an Event of Default under Section 15.1(d).")

# ------------------------------------------------------------------ ARTICLE 10
article(doc, "ARTICLE 10", "Environmental Matters")
section(doc, "10.1", "Compliance with Environmental Laws.")
para(doc, "Borrower shall comply, and shall cause Contractor and all tenants and occupants of the Property to comply, in all material respects with all Environmental Laws. Borrower shall not cause or permit any Release of Hazardous Substances at, on, under, or migrating from the Property, and shall not install or permit to exist any underground or aboveground storage tank at the Property.")

section(doc, "10.2", "Compliance with the NFA Letter.")
para(doc, "Borrower shall comply in all respects with each condition of the NFA Letter and with all requirements of Schedule 8. Without limiting the foregoing, Borrower shall:")
sub(doc, "(a)", "Soil Vapor Mitigation System. Design, install, commission, operate, and maintain the passive sub-slab depressurization system required by Condition 1 of the NFA Letter, with capability for conversion to an active depressurization system, in accordance with a design prepared by a professional engineer licensed in the State of North Carolina and in accordance with NCDEQ Division of Waste Management guidance for vapor intrusion mitigation. Borrower shall submit as-built drawings and a system performance verification report to NCDEQ within ninety (90) days after completion of the building foundation in the Restricted Area, and shall deliver copies of each such submission to Lender concurrently.");
sub(doc, "(b)", "Land Use Restriction. Restrict the Restricted Area to non-residential use and refrain from constructing, marketing, leasing, or permitting occupancy of any residential space within or above the Restricted Area, except in compliance with Section 4.3.");
sub(doc, "(c)", "Soil Management Plan. Conduct all excavation, grading, and subsurface disturbance within the Restricted Area in accordance with the NCDEQ-approved soil management plan required by Condition 3 of the NFA Letter, and submit such plan to NCDEQ for approval prior to the commencement of any such disturbance. Borrower shall incorporate the soil management plan into the Construction Contract and the Approved Plans and Specifications and shall cause Contractor and all subcontractors to comply with it.");
sub(doc, "(d)", "Deed Notice. Record, and cause to remain of record, the deed notice and declaration of land use restriction required by Condition 4 of the NFA Letter, in form and substance satisfactory to Lender, and provide Lender with a recorded copy and evidence of the recording date.");
sub(doc, "(e)", "Ongoing Monitoring. Conduct such soil gas and indoor air monitoring as may be required by the NFA Letter and, at Lender\u2019s request, such additional monitoring as Lender may reasonably require, and deliver all results to Lender within ten (10) Business Days after receipt.");
sub(doc, "(f)", "Regulatory Communications. Deliver to Lender, within five (5) Business Days after receipt or transmittal, copies of all correspondence, notices, orders, reports, and submissions relating to the NFA Letter, the Restricted Area, or the environmental condition of the Property.");

section(doc, "10.3", "Environmental Reports and Reliance.")
para(doc, "Lender acknowledges receipt of the Phase I ESA prepared by Sentinel Environmental Consulting LLC dated October 28, 2024 (Sentinel Project No. SEC-2024-1147), the Phase II investigation report dated August 30, 2024 (Sentinel Project No. SEC-2024-1089), and the NFA Letter dated September 30, 2024. Borrower shall deliver, or cause Sentinel Environmental Consulting LLC to deliver, a reliance letter addressed to Lender in form and substance satisfactory to Lender, and Lender shall be entitled to rely on such reports for all purposes. The Phase I ESA is subject to a shelf life of one hundred eighty (180) days from its date (through April 26, 2025); if the Closing Date occurs after such date, Borrower shall deliver an updated Phase I ESA in accordance with 40 C.F.R. § 312.20(c) as a condition to closing.")

section(doc, "10.4", "Notice of Environmental Events; Remedial Action.")
para(doc, "Borrower shall notify Lender in writing within three (3) Business Days after Borrower obtains knowledge of (a) any Release or threatened Release of Hazardous Substances at, on, under, or from the Property; (b) any notice, order, directive, or information request from any Governmental Authority relating to the environmental condition of the Property; (c) any revocation, modification, reopening, or challenge of the NFA Letter; (d) any failure of the soil vapor mitigation system; or (e) any lien arising under any Environmental Law. Borrower shall, at its sole cost, promptly undertake and diligently prosecute all investigative, remedial, removal, and response actions required by any Environmental Law, any Governmental Authority, or any condition of the NFA Letter, and shall deliver to Lender copies of all work plans, reports, and agency approvals.")

section(doc, "10.5", "Delineation of the Restricted Area.")
para(doc, "Within thirty (30) days after the Closing Date, Borrower shall deliver to Lender, prepared by a licensed North Carolina land surveyor and a qualified environmental professional and certified to Lender, (a) a metes-and-bounds description of the Restricted Area, (b) a plat or exhibit depicting the Restricted Area overlaid on the Survey and on the building floor plans for each level of the Improvements, and (c) a written determination, signed by the Architect, identifying precisely which portions of the Improvements, if any, are located within or directly above the Restricted Area and whether any residential unit, residential common area, or other residential occupancy space is so located. Borrower shall record a supplemental memorandum of the metes-and-bounds description if requested by Lender or Title Company.")

section(doc, "10.6", "Environmental Indemnity.")
para(doc, "Borrower and each Guarantor shall indemnify, defend, and hold harmless Lender and its officers, directors, employees, agents, and assigns from and against all claims, liabilities, losses, damages, penalties, fines, costs, and expenses (including reasonable attorneys\u2019 fees, consultant fees, and remediation costs) arising out of or relating to (a) the presence, Release, or threatened Release of any Hazardous Substances at, on, under, or migrating from the Property, whenever occurring and whether or not known to Lender; (b) any violation of any Environmental Law with respect to the Property; (c) any failure to comply with any condition of the NFA Letter; (d) any claim by any tenant, occupant, or other Person relating to indoor air quality or vapor intrusion; and (e) any assertion of lender liability under any Environmental Law, in each case as more particularly set forth in the Environmental Indemnity. The Environmental Indemnity shall be unlimited in amount, shall survive repayment of the Loan, the release or reconveyance of the Deed of Trust, and any foreclosure, deed in lieu of foreclosure, or other realization on the Collateral, and shall not be subject to any cap or to the exculpation provisions of Section 14.6, except that the indemnity shall not extend to liabilities to the extent arising from the gross negligence or willful misconduct of Lender.")

# ------------------------------------------------------------------ ARTICLE 11
article(doc, "ARTICLE 11", "Single-Purpose Entity and Separateness")
section(doc, "11.1", "Status.")
para(doc, "Borrower shall at all times maintain its status as a single-purpose, bankruptcy-remote entity and shall not engage in any business or activity other than the ownership, development, construction, leasing, management, and operation of the Project.")

section(doc, "11.2", "Assets and Liabilities.")
para(doc, "Borrower shall hold no assets other than the Property, the Improvements, and related Project assets, and shall incur no liabilities other than the Permitted Indebtedness and ordinary-course operating liabilities.")

section(doc, "11.3", "Separateness Covenants.")
para(doc, "Borrower shall: (a) maintain its own books, records, financial statements, and bank accounts separate from those of any member, Affiliate, or other Person; (b) not commingle its funds or other assets with those of any member, Affiliate, or other Person; (c) hold itself out as a separate and distinct entity and conduct its affairs in its own name; (d) observe all organizational formalities, including holding member and manager meetings, maintaining minutes and records, and making all required filings with the North Carolina Secretary of State; (e) pay its own liabilities and expenses from its own funds and allocate shared expenses with Affiliates on a reasonable and consistently applied basis; (f) not guarantee or become obligated for the debts of any other Person; (g) not pledge its assets for the benefit of any other Person other than in connection with the Loan and the Mezzanine Loan; (h) maintain an arm\u2019s-length relationship with its members and Affiliates and conduct all transactions with them on arm\u2019s-length terms; and (i) correct any known misunderstanding regarding its separate identity.")

section(doc, "11.4", "No Consolidation.")
para(doc, "Borrower shall not (a) take any action that would cause it to be substantively consolidated with any member, Affiliate, Mezzanine Lender, Brightleaf Investors Group LLC, Thomas R. Chen, or any other Person in any bankruptcy or insolvency proceeding, or (b) file any voluntary petition for relief under any bankruptcy, insolvency, or reorganization law without the affirmative vote of the Independent Manager.")

section(doc, "11.5", "Non-Consolidation Opinion.")
para(doc, "Borrower has delivered, and shall maintain as a condition of the Loan, the non-consolidation opinion described in Section 3.1(o). Borrower shall deliver an updated or bring-down non-consolidation opinion at the time of any extension of the Loan or upon any change in the ownership or governance of Borrower, if requested by Lender.")

section(doc, "11.6", "Independent Manager.")
para(doc, "Borrower shall cause its operating agreement to require, at all times, the appointment and retention of at least one Independent Manager, and shall cause the affirmative vote of the Independent Manager to be required for (a) any voluntary filing for bankruptcy, reorganization, or insolvency protection, (b) any consent to the appointment of a receiver, trustee, or custodian, (c) any admission in writing of Borrower\u2019s inability to pay its debts generally as they become due, (d) any amendment to the provisions of the operating agreement governing the Independent Manager, and (e) any dissolution or winding up of Borrower. The Independent Manager shall not be removable without Lender\u2019s prior written consent, and Borrower shall notify Lender within five (5) Business Days after any vacancy in the office of Independent Manager and shall fill such vacancy within thirty (30) days with a Person approved by Lender in writing.")
draftnote(doc, "Section 11.6 is drawn from Credit Memorandum Section 9.3 and Condition 10.1.4. Note that Borrower\u2019s operating agreement (excerpted in the organizational chart at Section 2.2) requires the affirmative vote of members holding 75% of the membership interests for any voluntary bankruptcy filing. Elena Vasquez-Torres holds 62% and Reginald K. Osei holds 10%; together they hold 72%, which is below the threshold. Brightleaf Investors Group LLC (28%), whose affiliate is the Mezzanine Lender and whose managing member is Thomas R. Chen, therefore holds an effective veto over bankruptcy filings, over any financing or refinancing exceeding $1,000,000, and over any amendment to the operating agreement. This is the inverse of the bankruptcy-remoteness the independent manager is intended to achieve: the party with the veto is an Affiliate of the subordinate lender. The 75% threshold must be addressed in the amended operating agreement. See Cover Memorandum Item C-3.")

# ------------------------------------------------------------------ ARTICLE 12
article(doc, "ARTICLE 12", "Insurance")
section(doc, "12.1", "Required Coverages.")
para(doc, "Borrower shall procure and maintain, at its sole cost and expense, the insurance coverages set forth on Schedule 6, which shall include, without limitation:")
sub(doc, "(a)", "Builder\u2019s Risk. All-risk builder\u2019s risk insurance on a replacement cost basis, including soft costs, materials in transit, and materials stored off-site, in an amount not less than the full replacement cost of the Improvements upon completion (which, based on the Appraisal, is not less than $56,700,000, and in no event less than the sum of the Guaranteed Maximum Price and all soft costs), naming Lender as mortgagee and loss payee as its interests may appear;")
sub(doc, "(b)", "Commercial General Liability. Commercial general liability insurance with limits of not less than $5,000,000 per occurrence and $10,000,000 in the aggregate, including premises liability, products and completed operations, contractual liability, and personal and advertising injury, naming Lender as additional insured;")
sub(doc, "(c)", "Umbrella or Excess Liability. Umbrella or excess liability insurance with limits of not less than $10,000,000 per occurrence and in the aggregate, providing excess coverage over the commercial general liability, employer\u2019s liability, and automobile liability policies, naming Lender as additional insured;")
sub(doc, "(d)", "Workers\u2019 Compensation and Employer\u2019s Liability. Statutory workers\u2019 compensation insurance as required by Article 97 of the North Carolina General Statutes, and employer\u2019s liability insurance with limits of not less than $1,000,000, covering all persons employed in connection with the construction of the Project;")
sub(doc, "(e)", "Property and Rental Loss Insurance for the Mini-Perm Period. Upon Substantial Completion and throughout the Mini-Perm Period, permanent property insurance on a special form, replacement cost basis, in an amount not less than the full insurable value of the Improvements, together with business income and rental loss insurance covering not less than twelve (12) months of Net Operating Income and continuing expenses, naming Lender as mortgagee and loss payee;")
sub(doc, "(f)", "Flood Insurance. If any portion of the Property is determined to be located in a Special Flood Hazard Area, flood insurance in the maximum amount available under the National Flood Insurance Program or such greater amount as Lender may require; and")
sub(doc, "(g)", "Professional Liability. Evidence that Architect maintains professional liability (errors and omissions) insurance with limits of not less than $2,000,000 per claim and in the aggregate, and that Contractor maintains contractor\u2019s pollution liability insurance covering the Restricted Area and the soil management plan work in an amount not less than $2,000,000.")
para(doc, "All policies shall be issued by insurers authorized to do business in North Carolina with an A.M. Best rating of not less than A- VIII, shall name Pinnacle Savings Bank, N.A. as mortgagee, loss payee, and/or additional insured as applicable, shall contain lender\u2019s loss payable and additional interest endorsements, shall provide for not less than thirty (30) days\u2019 prior written notice of cancellation, non-renewal, or material modification (ten (10) days for non-payment of premium), and shall waive subrogation against Lender. Borrower shall deliver certificates of insurance prior to closing and at each renewal, and shall deliver certified copies of policies within ten (10) days after Lender\u2019s request.")
draftnote(doc, "Term Sheet Sections 11 and 19 and Credit Memorandum Section 8.1 require builder\u2019s risk insurance in an amount \u201cnot less than the total hard construction costs ($34,750,000),\u201d on an \u201call-risk, replacement cost basis.\u201d Those two requirements are mutually inconsistent: the completed Improvements have an as-completed value of $72,800,000 per the Appraisal and a total development cost of $56,700,000, so insuring to $34,750,000 would leave the Improvements materially underinsured and would expose the Borrower to a coinsurance penalty. Section 12.1(a) insures to full replacement cost. See Cover Memorandum Item I-1. The Term Sheet also contains no property or rental loss requirement for the Mini-Perm Period; Section 12.1(e) fills that gap.")

section(doc, "12.2", "Failure to Maintain.")
para(doc, "If Borrower fails to maintain any required insurance, Lender may, at its option, obtain such insurance and charge the cost thereof to Borrower, which amount shall be an Advance under the Loan bearing interest at the Default Rate and secured by the Collateral, without constituting a waiver of any Default.")

section(doc, "12.3", "Casualty and Condemnation.")
para(doc, "In the event of any Casualty or Condemnation, Borrower shall promptly notify Lender, and Lender shall have the right to participate in the adjustment of any insurance claim or condemnation award. All insurance proceeds and condemnation awards shall be paid to Lender and applied in accordance with the Deed of Trust and the Intercreditor Agreement. Lender may, at its election, apply such proceeds to the outstanding principal balance of the Loan or make such proceeds available for restoration of the Improvements, subject to Lender\u2019s reasonable conditions, including that no Default or Event of Default exists and that Lender determines that the remaining undisbursed Loan proceeds and available insurance proceeds are sufficient to complete the restoration.")

# ------------------------------------------------------------------ ARTICLE 13
article(doc, "ARTICLE 13", "Collateral, Title, Permitted Exceptions and Survey")
section(doc, "13.1", "Collateral.")
para(doc, "The Loan shall be secured by: (a) a first-priority Deed of Trust on the Property and the Improvements; (b) a first-priority Assignment of Leases and Rents; (c) a first-priority security interest in all personal property, fixtures, equipment, permits, plans and specifications, contract rights, accounts, licenses, approvals, and general intangibles relating to the Project, perfected by the filing of UCC-1 financing statements; (d) collateral assignments of the Construction Contract and the Architect\u2019s Agreement; (e) a collateral assignment of all insurance proceeds and condemnation awards; (f) a first-priority pledge of 100% of the Pledged Interests, subject to the subordinated pledge in favor of Mezzanine Lender under the Intercreditor Agreement; (g) a first-priority security interest in the Interest Reserve Account, the Equity Escrow Account, and all other reserve and escrow accounts; and (h) such other Collateral as Lender may reasonably require.")

section(doc, "13.2", "Permitted Exceptions.")
para(doc, "The Deed of Trust shall be a first-priority Lien on the Property, subject only to the Permitted Exceptions listed on Schedule 2. The Permitted Exceptions have been conformed to the exceptions shown on Schedule B-II of the Title Commitment dated December 5, 2024, as follows: (a) the standard printed exceptions (Items 1 through 6 of Schedule B-II) shall be deleted or modified to the extent permitted by the Survey and the owner\u2019s affidavit of possession, and shall otherwise be Permitted Exceptions only as so modified; (b) the 2025 and subsequent years\u2019 ad valorem taxes (Item 7) are Permitted Exceptions; (c) the Duke Energy Carolinas easement recorded in Book 4387, Page 621 affecting a 20-foot strip along the western boundary of Parcel 0821-04-72-3341 (Item 8) is a Permitted Exception; (d) the City of Durham stormwater management easement recorded in Book 7421, Page 212 affecting approximately 0.22 acres in the southern portion of Parcel 0821-04-72-3341 (Item 9) is a Permitted Exception; (e) the Declaration of Covenants, Conditions, and Restrictions recorded in Book 6984, Page 1155, as amended in Book 7102, Page 388 (Item 11), is a Permitted Exception, subject to Borrower\u2019s compliance with its terms and to satisfaction of the architectural review condition in Section 3.1(g); (f) the provisions of the City of Durham Unified Development Ordinance and the MU-D zoning district (Item 12) are Permitted Exceptions; and (g) the deed notice and declaration of land use restriction required by Condition 4 of the NFA Letter, once recorded, shall be a Permitted Exception, subject to Borrower\u2019s compliance with Article 10. The Deed of Trust recorded in Book 6215, Page 892 in favor of Triangle Commercial Bank (Item 10) is not a Permitted Exception and must be released of record at or before closing.")
draftnote(doc, "Term Sheet Section 18 lists only four Permitted Exceptions (standard printed exceptions, the Duke Energy easement, the stormwater easement, and the CC&Rs) and provides that \u201call other exceptions shown on Schedule B-II \u2026 including but not limited to any prior deeds of trust\u201d shall be removed or satisfied. That formulation is not achievable: the 2025 tax exception (Item 7), the zoning exception (Item 12), and the parties-in-possession exception (Item 13) cannot be removed, and the environmental deed notice, once recorded, will appear as an additional exception. Section 13.2 reconciles the Term Sheet to the Title Commitment so that the Title Policy can actually be issued. See Cover Memorandum Item E-2.")

section(doc, "13.3", "Title Policy.")
para(doc, "Borrower shall cause Title Company to issue the Title Policy at closing in the amount of the Loan Amount, insuring the Deed of Trust as a valid first-priority Lien on the fee simple estate in the Property, subject only to the Permitted Exceptions, together with such endorsements as Lender may require, including an ALTA 9 comprehensive endorsement (restricting survey, mechanic\u2019s lien, and access exceptions), an ALTA 14 future advances endorsement, an ALTA 18 encoding endorsement, an ALTA 22 location endorsement, an ALTA 33 disbursement endorsement, and such other endorsements as Lender may reasonably require to confirm the priority of future Advances.")

section(doc, "13.4", "Mechanic\u2019s Lien Priority; Prior Work.")
para(doc, "Borrower acknowledges that, under N.C.G.S. § 44A-10, a claim of lien on real property relates back to and is effective from the time of first furnishing of labor or materials at the site of the improvement, and that demolition of the former warehouse structures (completed in August 2024) and environmental remediation activities (completed in September 2024) occurred before the recording of the Deed of Trust. Borrower shall therefore deliver, as a condition to closing under Section 3.1(r), unconditional lien waivers and releases from the demolition contractor, from Sentinel Environmental Consulting LLC, from Contractor, and from each other Person that has furnished labor, materials, or services at the Property prior to the Closing Date, together with such owner\u2019s affidavits and title endorsements as Title Company may require to insure Lender against such claims. Borrower shall not permit any work to commence, or any materials to be delivered to the Property, before the Deed of Trust is recorded.")
draftnote(doc, "The Title Commitment (Note 4) expressly warns of the relation-back risk under N.C.G.S. § 44A-10 and recommends owner and contractor affidavits. Neither the Term Sheet nor the Credit Memorandum addresses the fact that demolition and remediation work was performed in August and September 2024, well before the closing. Because claims arising from that work could prime the Deed of Trust, this is a priority issue, not merely a documentation item. See Cover Memorandum Item E-3.")

section(doc, "13.5", "Survey.")
para(doc, "Borrower shall deliver the Survey, certified to Borrower, Lender, and Title Company, complying with the 2021 ALTA/NSPS Minimum Standard Detail Requirements and including Table A optional items 1, 2, 3, 4, 6, 7(a), 8, 9, 10, 11, 13, and 14, or such other Table A items as Lender may require. The Survey shall confirm (a) the acreage and dimensions of each parcel, (b) the location of all easements and rights-of-way, (c) the location of the Improvements relative to all setback and building lines, and (d) the absence of encroachments, overlaps, and boundary disputes other than those approved by Lender. Borrower acknowledges that the Title Commitment legal descriptions reflect Parcel 0821-04-72-3341 as approximately 2.09 acres and Parcel 0821-04-72-4102 as approximately 1.38 acres, while the Phase I ESA describes the same parcels as approximately 1.89 acres and 1.58 acres, respectively, and that the Survey must reconcile such discrepancy.")
draftnote(doc, "The recorded legal descriptions are internally consistent with their metes and bounds (298.62\u2032 \u00d7 305.41\u2032 = 2.094 acres; 201.88\u2032 \u00d7 297.63\u2032 = 1.379 acres; combined frontage along Foster Street of 500.50\u2032), which suggests that the Phase I ESA acreage figures and its Figure 3 orientation description (Foster Street \u201cto the north\u201d; Parcel 2 as the \u201ceastern\u201d parcel) are incorrect. The Survey controls. See Cover Memorandum Item E-4.")

section(doc, "13.6", "Release; Future Advances.")
para(doc, "Lender shall release the Deed of Trust and the other Collateral only upon (a) payment in full of the principal, interest, fees, and Other Charges due under the Loan Documents, (b) payment of all amounts due under the Guaranties and the Environmental Indemnity (or, in the case of the Environmental Indemnity, the satisfaction of the conditions to release set forth therein), and (c) delivery of such releases, satisfactions, and termination statements as Borrower may reasonably request. All Advances under this Agreement shall be obligatory advances secured by the Deed of Trust with the same priority as the initial Advance, and Lender shall be entitled to the benefit of all applicable law governing the priority of obligatory future advances.")

# ------------------------------------------------------------------ ARTICLE 14
article(doc, "ARTICLE 14", "Guaranties and Recourse")
section(doc, "14.1", "Completion Guaranty.")
para(doc, "Each Guarantor shall jointly and severally guarantee the lien-free completion of the Project in accordance with the Approved Plans and Specifications, the Approved Budget, and the construction schedule, on or before the Construction Maturity Date, and shall fund all costs of completion in excess of the Loan proceeds and the Equity Contribution. The Completion Guaranty shall remain in full force and effect until Lender has received satisfactory evidence that construction of the Project has been completed in all material respects, that a final certificate of occupancy has been issued by the City of Durham, and that all construction liens have been released or bonded off.")
para(doc, "Borrower acknowledges that the projected Substantial Completion date set forth in the Appraisal is August 31, 2027, three (3) days after the Construction Maturity Date of August 28, 2027, and that the Completion Guaranty date and the Project schedule shall be conformed by Lender and Borrower prior to closing so that the guaranteed completion date is not earlier than the scheduled Substantial Completion date.")
draftnote(doc, "This is a small but real inconsistency: Term Sheet Sections 2 and 7.1 require completion on or before August 28, 2027 and the Credit Memorandum (Section 9.6) and Appraisal both project August 31, 2027. As drafted, the Completion Guaranty would be in default at inception. See Cover Memorandum Item G-1.")

section(doc, "14.2", "Carry Guaranty.")
para(doc, "Each Guarantor shall jointly and severally guarantee the payment of all interest and other carrying costs on the Loan, including interest, real estate taxes, insurance premiums, and other carrying expenses, throughout the term of the Loan. The Carry Guaranty is in addition to, and not in lieu of, the Interest Reserve, and shall apply to all interest and carrying costs accruing after the Interest Reserve is exhausted or in the event the Interest Reserve is insufficient.")

section(doc, "14.3", "Partial Repayment Guaranty.")
para(doc, "Each Guarantor shall jointly and severally guarantee the payment of an amount equal to twenty-five percent (25%) of the Loan Amount, being $11,875,000 in the aggregate (and not $11,875,000 per Guarantor), upon the occurrence of an Event of Default. The Partial Repayment Guaranty shall be a guarantee of payment and not of collection, and Lender may proceed directly against either Guarantor without first proceeding against Borrower or the Collateral. The aggregate liability of the Guarantors under the Partial Repayment Guaranty, together with all amounts recovered from the Guarantors thereunder, shall not exceed $11,875,000.")
draftnote(doc, "Term Sheet Section 7.3 and Credit Memorandum Section 4.3 describe a \u201c25% partial repayment guaranty in the amount of $11,875,000\u201d that is \u201cjoint and several, meaning that each Guarantor shall be individually liable for the full guaranteed amount,\u201d and the Credit Memorandum\u2019s guarantor analysis (Section 2.3.3) assesses that amount separately against each Guarantor\u2019s net worth. Read literally, the documents could support an aggregate claim of $23,750,000 (25% per Guarantor). Section 14.3 fixes the aggregate limit at $11,875,000 to match the 25%-of-Loan-Amount economic term. See Cover Memorandum Item C-6.")

section(doc, "14.4", "Recourse Carve-Outs.")
para(doc, "The Guaranties shall convert to a full recourse obligation of Borrower and each Guarantor (for the entire outstanding principal balance, accrued interest, fees, costs, and expenses, and not merely 25% thereof) upon the occurrence of any of the following: (a) fraud or intentional misrepresentation by Borrower, any Guarantor, or any member of Borrower in connection with the Loan; (b) any voluntary filing by Borrower of a petition for relief under any bankruptcy, insolvency, or reorganization law, or any collusive involuntary filing; (c) any Transfer in violation of the Loan Documents; (d) any Release of Hazardous Substances at the Property caused or permitted by Borrower or any Guarantor, or any failure to comply with any Environmental Law or any condition of the NFA Letter; (e) waste of the Collateral; (f) any breach of the SPE covenants in Article 11; (g) any misapplication of rents, insurance proceeds, condemnation awards, or reserve funds; or (h) any failure to maintain insurance required by Article 12. The full recourse obligations created by this Section 14.4 shall be in addition to, and not in lieu of, the obligations under the Environmental Indemnity, which shall be unlimited in amount.")
draftnote(doc, "Credit Memorandum Section 4.3 states that \u201cNorth Carolina is a judicial foreclosure state\u201d and that deficiencies are subject to the \u201cfair price confirmation\u201d requirements of N.C.G.S. § 45-21.36. That characterization is inaccurate: North Carolina deeds of trust are ordinarily foreclosed by a non-judicial power-of-sale proceeding before the clerk of superior court under Article 2A of Chapter 45 of the North Carolina General Statutes (N.C.G.S. §§ 45-21.1 through 45-21.33), with the deficiency sought by separate civil action and subject to the fair-price limitation of N.C.G.S. § 45-21.36. The draft reflects the correct framework. See Cover Memorandum Item J-1.")

section(doc, "14.5", "Waivers by Guarantors.")
para(doc, "Each Guarantor shall waive all defenses based on suretyship, including the defenses of subrogation, reimbursement, exoneration, and contribution until the Loan has been indefeasibly paid in full, and all defenses arising from any modification, extension, or waiver of the Loan Documents, any release or substitution of Collateral, or any election of remedies by Lender.")

section(doc, "14.6", "Exculpation.")
para(doc, "Except as provided in Section 14.4 and in the Environmental Indemnity, the obligations of Borrower under the Loan Documents shall be without recourse to Borrower or any member of Borrower, and Lender\u2019s remedies shall be limited to the Collateral; provided, however, that nothing in this Section 14.6 shall limit the obligations of the Guarantors under the Guaranties or the liability of Borrower or any Guarantor for fraud, misrepresentation, or any of the matters described in Section 14.4.")

# ------------------------------------------------------------------ ARTICLE 15
article(doc, "ARTICLE 15", "Events of Default")
section(doc, "15.1", "Events of Default.")
para(doc, "Each of the following shall constitute an Event of Default:")
ED = [
"Payment. Failure by Borrower to pay any principal, interest, fee, or Other Charge when due, whether at maturity, by acceleration, or otherwise, subject to a grace period of five (5) days after the due date; provided that no grace period shall apply to any payment due on the Maturity Date or to any payment funded from the Interest Reserve Account.",
"Representations. Any representation or warranty made by Borrower or any Guarantor in any Loan Document proves to have been untrue or misleading in any material respect when made or deemed made.",
"Non-Monetary Covenants. Failure by Borrower to observe or perform any non-monetary covenant or obligation under the Loan Documents, subject to a cure period of thirty (30) days after written notice from Lender; provided that if such failure cannot reasonably be cured within thirty (30) days and Borrower is diligently pursuing such cure, the cure period shall be extended for an additional thirty (30) days, but in no event beyond sixty (60) days in the aggregate.",
"Financial Covenants. Failure by Borrower to comply with any covenant in Article 9, subject only to the cure rights expressly provided in Section 9.6.",
"Bankruptcy; Insolvency. The commencement by or against Borrower, any Guarantor, or any member of Borrower of any case, proceeding, or other action under any bankruptcy, insolvency, reorganization, or similar law, whether voluntary or involuntary, which in the case of an involuntary proceeding is not dismissed within sixty (60) days; or the appointment of a receiver, trustee, custodian, or assignee for the benefit of creditors for Borrower, any Guarantor, or any member of Borrower or any material part of its property; or any admission in writing of inability to pay debts generally as they become due.",
"Material Adverse Change. Any Material Adverse Effect, including any material adverse change in the financial condition of Borrower or any Guarantor, as determined by Lender in its reasonable discretion.",
"Construction Delays. Failure to achieve the construction milestones set forth in Schedule 4 within the time frames specified therein, or any Construction Delay Default, being a determination that the Project is more than ninety (90) days behind the approved construction schedule at any time during the Construction Period.",
"Abandonment. Abandonment of the Project by Borrower or by Contractor, or cessation of construction for a period of thirty (30) consecutive days other than as a result of a force majeure event approved by Lender.",
"Insurance. Failure to maintain any insurance required by Article 12.",
"SPE Covenants. Breach of any covenant in Article 11 or of any separateness covenant in Borrower\u2019s operating agreement.",
"Mezzanine Default; Intercreditor. Any default or event of default under the Mezzanine Documents or the Intercreditor Agreement, or any failure of Mezzanine Lender to comply with the Intercreditor Agreement.",
"Environmental. Any material violation of any Environmental Law; any Release of Hazardous Substances at the Property; the issuance of any environmental order, directive, or lien affecting the Property; any failure to comply with any condition of the NFA Letter, including the failure to record or maintain the deed notice required by Condition 4; any revocation, modification, or reopening of the NFA Letter; or any failure to install, operate, or maintain the soil vapor mitigation system as required by Condition 1.",
"Judgments. Entry of one or more judgments against Borrower or any Guarantor in an aggregate amount exceeding $500,000 that remains unsatisfied, unbonded, or unstayed for a period of thirty (30) days.",
"Guarantor Net Worth or Revocation. Any Guarantor\u2019s net worth falls below $10,000,000 or such Guarantor\u2019s Guarantor Liquidity falls below $2,500,000; or any Guarantor revokes, terminates, disaffirms, or contests the validity or enforceability of any Guaranty or any obligation thereunder.",
"Title or Collateral Impairment. Any Lien (other than a Permitted Exception) attaches to the Property or any other Collateral, or the Title Policy is cancelled, not issued, or otherwise impaired.",
"Independent Manager. Borrower fails to maintain an Independent Manager as required by Section 11.6.",
"Interest Reserve. Failure to fund any Interest Reserve shortfall or any other required deposit within the period specified in this Agreement.",
"Adverse Change in Ownership. Any Transfer, any change in the identity of the Managing Member, or any admission of a new member of Borrower without Lender\u2019s prior written consent.",
"Other Loan Documents. Any default under any other Loan Document not otherwise described in this Section 15.1 and not cured within any applicable notice and cure period.",
]
lettered(ED)
draftnote(doc, "Term Sheet Section 15 provides that an Event of Default occurs if \u201cAny Guarantor\u2019s net worth falls below the minimum threshold set forth in Section 6.4.\u201d Section 6.4 of the Term Sheet sets the minimum net worth of the Borrower, not of any Guarantor; the Guarantors are subject only to the $5,000,000 combined liquidity covenant in Section 6.5, and no Guarantor net worth covenant exists anywhere in the record. Section 15.1(n) fills the gap with a $10,000,000 per-Guarantor net worth threshold and a $2,500,000 per-Guarantor liquidity threshold, which should be confirmed by the Committee. See Cover Memorandum Item K-1.")

# ------------------------------------------------------------------ ARTICLE 16
article(doc, "ARTICLE 16", "Remedies")
section(doc, "16.1", "Remedies.")
para(doc, "Upon the occurrence and during the continuance of an Event of Default, Lender may, at its option and without further notice to Borrower except as required by applicable law, exercise any or all of the following remedies, which are cumulative and non-exclusive:")
RM = [
"accelerate the Loan and declare all outstanding principal, accrued and unpaid interest, fees, and Other Charges immediately due and payable;",
"cease making any further Advances, terminate the Commitment, and apply all amounts in the Interest Reserve Account, the Equity Escrow Account, and any other reserve held by Lender to the Loan;",
"apply the Default Rate to all outstanding amounts;",
"exercise all rights and remedies under the Deed of Trust, including foreclosure by power of sale in accordance with Article 2A of Chapter 45 of the North Carolina General Statutes (N.C.G.S. §§ 45-21.1 through 45-21.33), or, at Lender\u2019s election, by judicial foreclosure, and obtain a deficiency judgment in a separate action subject to the fair-price limitation of N.C.G.S. § 45-21.36;",
"exercise all rights and remedies under the Assignment of Leases and Rents, including the right to collect all rents and revenues directly from tenants;",
"exercise all rights and remedies under the Guaranties, including the Completion Guaranty, the Carry Guaranty, the Partial Repayment Guaranty, and the Environmental Indemnity;",
"exercise all rights and remedies of a secured party under Article 9 of the Uniform Commercial Code as enacted in North Carolina, including with respect to the Pledged Interests, subject to the Intercreditor Agreement;",
"obtain the appointment of a receiver for the Property and the Project in accordance with applicable North Carolina law; and",
"exercise any other right or remedy available at law or in equity.",
]
for i, t in enumerate(RM, start=1):
    sub(doc, "(%d)" % i, t)

section(doc, "16.2", "No Waiver; No Marshalling.")
para(doc, "No delay or failure by Lender in exercising any right or remedy shall constitute a waiver thereof, and no single or partial exercise of any right or remedy shall preclude any other or further exercise thereof. Lender shall not be required to marshal any assets in favor of Borrower or any Guarantor, or to resort to any particular Collateral in any particular order.")

section(doc, "16.3", "Notice of Default.")
para(doc, "Lender shall give Borrower written notice of any Default promptly upon Lender\u2019s determination thereof, but the giving of such notice shall not be a condition to the exercise of any remedy other than as expressly provided in Section 15.1 with respect to the specific cure and grace periods stated therein.")

# ------------------------------------------------------------------ ARTICLE 17
article(doc, "ARTICLE 17", "Indemnities")
section(doc, "17.1", "General Indemnity.")
para(doc, "Borrower and each Guarantor shall jointly and severally indemnify, defend, and hold harmless Lender and its officers, directors, employees, agents, successors, and assigns (collectively, the \u201cIndemnified Parties\u201d) from and against any and all claims, demands, actions, liabilities, losses, damages, penalties, fines, judgments, settlements, costs, and expenses (including reasonable attorneys\u2019 fees and costs of investigation and defense) arising out of or relating to (a) the Loan or the Loan Documents; (b) any act or omission of Borrower, any Guarantor, Contractor, Architect, or any of their respective agents in connection with the Project; (c) any claim of any contractor, subcontractor, materialman, tenant, or other Person relating to the Project or the Property; (d) any accident, injury, or death occurring at the Property; and (e) any failure of Borrower to comply with any law or any provision of the Loan Documents, other than to the extent arising from the gross negligence or willful misconduct of the applicable Indemnified Party.")

section(doc, "17.2", "Environmental Indemnity.")
para(doc, "The environmental indemnity provided in Section 10.6 and in the Environmental Indemnity Agreement is unlimited in amount, is independent of the other Loan Documents, and shall survive repayment of the Loan and any foreclosure, deed in lieu of foreclosure, or other realization on the Collateral.")

section(doc, "17.3", "Survival.")
para(doc, "The indemnities in this Article 17 shall survive the repayment of the Loan and the termination of the other Loan Documents.")

# ------------------------------------------------------------------ ARTICLE 18
article(doc, "ARTICLE 18", "Mezzanine Loan; Intercreditor Agreement")
section(doc, "18.1", "Acknowledgment of Mezzanine Loan.")
para(doc, "Lender acknowledges that Borrower intends to obtain the Mezzanine Loan from Mezzanine Lender in the original principal amount of $9,200,000, bearing interest at a fixed rate of 12.50% per annum, coterminous in maturity with the Loan (including any extension thereof), and secured by a pledge of the Pledged Interests. Borrower acknowledges that neither Lender nor any of its Affiliates is providing any financing to Mezzanine Lender in connection with the Mezzanine Loan and that Lender has no obligation with respect thereto.")

section(doc, "18.2", "Intercreditor Agreement as Condition Precedent.")
para(doc, "The execution and delivery of the Intercreditor Agreement by Lender, Mezzanine Lender, Borrower, and each member of Borrower is a condition precedent to closing under Section 3.1(c) and may not be waived. The Intercreditor Agreement shall provide, at a minimum: (a) that Lender holds a first-priority security interest in the Pledged Interests and Mezzanine Lender holds a subordinated second-priority security interest therein; (b) a standstill period of not less than ninety (90) days following the occurrence of a default under the Mezzanine Loan, during which Mezzanine Lender may not exercise any remedy against Borrower, the Pledged Interests, or the Project; (c) notice and cure rights permitting Mezzanine Lender to receive copies of all default notices issued by Lender and to cure defaults under the Loan within the applicable cure period; (d) a purchase option granting Mezzanine Lender the right, but not the obligation, to purchase the Loan at par plus accrued and unpaid interest, fees, and costs; (e) a prohibition on Mezzanine Lender modifying any material term of the Mezzanine Loan without Lender\u2019s prior written consent; (f) a prohibition on Mezzanine Lender filing or joining in the filing of an involuntary bankruptcy petition against Borrower; (g) Mezzanine Lender\u2019s acknowledgment that it will not contest or interfere with Lender\u2019s exercise of remedies; and (h) express acknowledgment of the affiliate relationship among Mezzanine Lender, Brightleaf Investors Group LLC, and Thomas R. Chen, together with provisions preventing Mezzanine Lender from using such relationship to the detriment of Lender.")

section(doc, "18.3", "Mezzanine Fees and Distributions.")
para(doc, "Borrower shall not pay any mezzanine-related fee, non-utilization fee, exit fee, or other compensation to Mezzanine Lender or any Affiliate thereof other than interest and principal due under the Mezzanine Loan as in effect on the Closing Date, without Lender\u2019s prior written consent. All distributions on account of the Mezzanine Loan shall be subject to the negative covenants in Article 8 and the Intercreditor Agreement.")

section(doc, "18.4", "Affiliate Disclosure.")
para(doc, "Borrower acknowledges and discloses that Brightleaf Investors Group LLC, which holds a 28% membership interest in Borrower, and Mezzanine Lender are under the common control of Thomas R. Chen, who serves as Managing Member of both entities. Borrower acknowledges that this relationship creates a conflict of interest and agrees to take all actions reasonably required by Lender to mitigate the resulting risks, including the SPE covenants in Article 11, the Independent Manager requirement in Section 11.6, the non-consolidation opinion required by Section 3.1(o), and the affiliate provisions of the Intercreditor Agreement.")
draftnote(doc, "The organizational chart discloses that Brightleaf Investors Group LLC received its 28% membership interest for no cash consideration, \u201cin consideration of its commitment to arrange third-party mezzanine financing,\u201d and that the mezzanine financing was then arranged through an entity controlled by the same individual. Brightleaf Investors Group LLC has contributed $0 to date and is not a Guarantor. A 28% equity holder with no capital at risk, an affiliate that is the subordinate lender, and a blocking 75% supermajority is an unusual structure that warrants, at a minimum, the additional credit support described in Cover Memorandum Item C-4.")

# ------------------------------------------------------------------ ARTICLE 19
article(doc, "ARTICLE 19", "Notices")
section(doc, "19.1", "Notices.")
para(doc, "All notices, demands, consents, approvals, and other communications under the Loan Documents shall be in writing and shall be deemed given: (a) when delivered personally; (b) one (1) Business Day after deposit with a nationally recognized overnight courier; (c) three (3) Business Days after deposit in the United States mail, certified or registered, return receipt requested, postage prepaid; or (d) when sent by electronic mail, if sent during normal business hours and confirmed by a read receipt or other acknowledgment, and otherwise on the next Business Day. Notices shall be addressed as follows, or to such other address as a party may designate by notice given in accordance with this Section:")
table(doc, [
    ["Party", "Notice Address"],
    ["Borrower", "Harborview Capital Partners LLC\n400 West Main Street, Suite 310\nDurham, North Carolina 27701\nAttn: Elena Vasquez-Torres, Managing Member\nEmail: evasquez@harborviewcapital.com"],
    ["Borrower\u2019s Counsel", "Calloway & Strauss PLLC\n324 Blackwell Street, Suite 200\nDurham, North Carolina 27701\nAttn: Jonathan F. Ngo\nEmail: jngo@callowaystrauss.com"],
    ["Lender", "Pinnacle Savings Bank, N.A.\n215 South Tryon Street, 18th Floor\nCharlotte, North Carolina 28202\nAttn: David Forsythe, SVP, Commercial Real Estate Lending\nEmail: dforsythe@pinnaclesavings.com"],
    ["Lender\u2019s Counsel", "Ashford, Cromdale Consulting & Laine LLP\n411 South Tryon Street, Suite 2800\nCharlotte, North Carolina 28202\nAttn: Katharine Drummond; Marcus Webb\nEmail: kdrummond@aclllp.com"],
    ["Guarantors", "Elena Vasquez-Torres: 400 West Main Street, Suite 310, Durham, NC 27701\nReginald K. Osei: 118 East Rosemary Street, Chapel Hill, NC 27514"],
    ["Title Company", "Aldersgate Title & Escrow Inc.\n307 West Chapel Hill Street, Suite 400\nDurham, North Carolina 27701\nAttn: Patricia Langley, Escrow Officer\nEmail: plangley@crestviewtitle.com"],
    ["Mezzanine Lender", "Brightleaf Mezzanine Capital LLC\nc/o Thomas R. Chen\n[Address to be confirmed]\nEmail: [to be confirmed]"],
], widths=[1.35, 4.75], header=True, size=8.5, bold_first_col=True)

# ------------------------------------------------------------------ ARTICLE 20
article(doc, "ARTICLE 20", "Assignment; Participations; Sale of the Loan")
section(doc, "20.1", "Assignment by Lender.")
para(doc, "Lender may sell, assign, transfer, or grant participations in all or any portion of the Loan, the Commitment, and the Loan Documents at any time without the consent of Borrower or any Guarantor. Borrower acknowledges that Lender may provide to any actual or prospective assignee or participant, and to any rating agency, data provider, or regulatory authority, such information regarding Borrower, the Guarantors, the Property, and the Project as Lender deems appropriate, subject to customary confidentiality undertakings. Borrower shall cooperate with Lender in connection with any such sale or participation, including by executing customary estoppel certificates and providing financial information reasonably requested.")

section(doc, "20.2", "Assignment by Borrower.")
para(doc, "Borrower may not assign or delegate any of its rights or obligations under the Loan Documents without Lender\u2019s prior written consent, which may be withheld in Lender\u2019s sole and absolute discretion. Any purported assignment in violation of this Section shall be void.")

section(doc, "20.3", "Participation Disclosures.")
para(doc, "Borrower acknowledges that Lender is a national bank subject to supervision by the OCC, and that Lender may be required to disclose information regarding the Loan to the OCC and other regulatory authorities.")

# ------------------------------------------------------------------ ARTICLE 21
article(doc, "ARTICLE 21", "Miscellaneous")
section(doc, "21.1", "Governing Law.")
para(doc, "The Loan Documents shall be governed by and construed in accordance with the laws of the State of North Carolina, without regard to its conflict-of-laws principles, except that the creation, perfection, and enforcement of Liens on real property shall be governed by the law of the jurisdiction in which the Property is located.")

section(doc, "21.2", "Venue; Consent to Jurisdiction; Waiver of Jury Trial.")
para(doc, "Each party irrevocably submits to the exclusive jurisdiction of the General Court of Justice of North Carolina, Durham County, and the United States District Court for the Middle District of North Carolina, for any action or proceeding arising out of or relating to the Loan or the Loan Documents, and irrevocably waives any objection to venue in such courts. EACH PARTY KNOWINGLY, VOLUNTARILY, AND INTENTIONALLY WAIVES ANY RIGHT IT MAY HAVE TO A TRIAL BY JURY IN ANY ACTION OR PROCEEDING ARISING OUT OF OR RELATING TO THE LOAN OR THE LOAN DOCUMENTS, AND ACKNOWLEDGES THAT THIS WAIVER IS A MATERIAL INDUCEMENT TO LENDER\u2019S ENTRY INTO THIS AGREEMENT.")

section(doc, "21.3", "Expenses.")
para(doc, "Borrower shall pay all costs and expenses incurred by Lender in connection with the origination, documentation, closing, administration, and enforcement of the Loan, including the reasonable legal fees and disbursements of Ashford, Cromdale Consulting & Laine LLP, appraisal and reappraisal fees, environmental assessment and consulting fees, title insurance premiums and endorsement charges, survey costs, recording and filing fees, construction inspection fees, and all other out-of-pocket costs and expenses. Borrower\u2019s obligation to pay Lender\u2019s legal fees and expenses shall apply regardless of whether the Loan closes, subject to the application of the $75,000 expense deposit delivered under Section 22 of the Term Sheet.")

section(doc, "21.4", "Amendments; Waivers.")
para(doc, "No amendment or waiver of any provision of any Loan Document, and no consent to any departure by Borrower therefrom, shall be effective unless in writing signed by Lender and, where applicable, Borrower, and then only in the specific instance and for the specific purpose for which given.")

section(doc, "21.5", "Entire Agreement.")
para(doc, "The Loan Documents constitute the entire agreement among the parties with respect to the subject matter hereof and supersede all prior and contemporaneous negotiations, discussions, correspondence, term sheets, commitments, and understandings, whether written or oral, including the Term Sheet, except as provided in Section 1.3.")

section(doc, "21.6", "Severability; Counterparts; Electronic Signatures.")
para(doc, "If any provision of any Loan Document is held to be invalid, illegal, or unenforceable, such provision shall be enforced to the maximum extent permissible, and the remaining provisions shall remain in full force and effect. The Loan Documents may be executed in any number of counterparts, each of which shall be deemed an original, and all of which together shall constitute one and the same instrument. Signatures delivered by electronic means or in portable document format shall be deemed original signatures for all purposes.")

section(doc, "21.7", "No Partnership; No Third-Party Beneficiaries.")
para(doc, "Nothing in the Loan Documents shall be deemed to create a partnership, joint venture, or fiduciary relationship between Lender and Borrower or any Guarantor. The Loan Documents are for the sole benefit of the parties thereto and their permitted successors and assigns, and no other Person shall have any rights thereunder, except that the Indemnified Parties are intended third-party beneficiaries of Article 17.")

section(doc, "21.8", "Time of the Essence; Cumulative Remedies.")
para(doc, "Time is of the essence with respect to each obligation of Borrower and each Guarantor under the Loan Documents. All rights and remedies of Lender are cumulative and non-exclusive and may be exercised in any order.")

section(doc, "21.9", "Confidentiality.")
para(doc, "Each party shall maintain the confidentiality of the Loan Documents and of all non-public information regarding the other parties, except as required by law, regulation, legal process, or the requirements of any regulatory authority, or as necessary to enforce the Loan Documents, and except that Lender may disclose such information in accordance with Article 20. The confidentiality obligations set forth in Section 22 of the Term Sheet shall survive in accordance with their terms.")

section(doc, "21.10", "Usury; Savings.")
para(doc, "The Loan Documents are subject to the savings clause set forth in Section 2.9.")

section(doc, "21.11", "Setoff.")
para(doc, "Upon the occurrence and during the continuance of an Event of Default, Lender shall have the right to set off against the obligations of Borrower any and all balances, credits, deposits, accounts, or moneys of Borrower then or thereafter held by Lender, to the extent permitted by applicable law.")

section(doc, "21.12", "Joint and Several Liability.")
para(doc, "The obligations of Borrower and each Guarantor under the Loan Documents shall be joint and several, and each reference to \u201cBorrower\u201d or \u201cGuarantor\u201d shall be deemed to include each such Person. Lender may proceed against any one or more of them, in any order, without affecting the liability of the others.")

section(doc, "21.13", "Estoppel Certificates.")
para(doc, "Within fifteen (15) Business Days after written request by Lender, Borrower and each Guarantor shall deliver a certificate certifying as to the outstanding principal balance of the Loan, the status of the Loan Documents, the existence of any Default or Event of Default, and such other matters as Lender may reasonably request.")

section(doc, "21.14", "Further Assurances.")
para(doc, "Borrower and each Guarantor shall execute, acknowledge, deliver, record, and file such further instruments and take such further actions as Lender may reasonably require to carry out the purposes of the Loan Documents, including all instruments necessary to perfect and maintain the Liens granted to Lender.")

section(doc, "21.15", "Interpretation of Source Documents; Open Items.")
para(doc, "Borrower acknowledges that certain terms of the Term Sheet, the Credit Memorandum, the Appraisal, the Phase I ESA, the Title Commitment, the organizational materials, and the draw schedule delivered by Borrower are inconsistent, and that this Agreement resolves such inconsistencies in the manner described in the Cover Memorandum delivered concurrently herewith and incorporated herein by reference for the limited purpose of identifying the resolved and unresolved items. Bracketed provisions and provisions marked with a Drafting Note remain subject to Lender\u2019s Senior Loan Committee approval and to further documentation.")


# ------------------------------------------------------------------ ARTICLE 22
article(doc, "ARTICLE 22", "Extension Option")
section(doc, "22.1", "Extension Option.")
para(doc, "Borrower shall have one (1) option to extend the Mini-Perm Maturity Date by six (6) months, to February 28, 2029 (the \u201cExtended Maturity Date\u201d), subject to satisfaction of each of the following conditions on or before the date that is sixty (60) days prior to the Mini-Perm Maturity Date:")
EX = [
"no Event of Default and no Default shall exist, and no event of default shall exist under the Intercreditor Agreement;",
"Substantial Completion of the Project shall have been achieved and a final, unconditional certificate of occupancy shall have been issued by the City of Durham for all residential units and retail space;",
"not less than seventy-five percent (75%) of the residential units shall be leased under executed leases with terms of at least twelve (12) months and shall be physically occupied;",
"the DSCR, determined on the basis of actual trailing three-month annualized in-place Net Operating Income divided by annual Debt Service on the outstanding principal balance at the then-current Applicable Rate, shall be not less than 1.15x;",
"Borrower shall have paid the Extension Fee in the amount of 0.25% of the then-outstanding principal balance of the Loan;",
"Borrower shall have delivered and collaterally assigned to Lender an interest rate cap agreement for the Extended Maturity Date period, with a strike rate and counterparty acceptable to Lender (having a long-term credit rating of not less than A- from S&P Global Ratings or A3 from Moody\u2019s Investors Service);",
"the Intercreditor Agreement shall remain in full force and effect and Mezzanine Lender shall have consented to the extension on terms satisfactory to Lender;",
"Lender shall have received an updated appraisal from an MAI-designated appraiser acceptable to Lender confirming that the Loan-to-Value Ratio based on the outstanding principal balance and the as-stabilized value does not exceed 70%;",
"all representations and warranties shall be true and correct in all material respects, and Borrower shall have delivered a Compliance Certificate to that effect;",
"Lender shall have received evidence of compliance with all conditions of the NFA Letter and no revocation, modification, or reopening of the NFA Letter shall have occurred; and",
"Borrower shall have delivered written notice of its election to exercise the Extension Option in accordance with this Section 22.1.",
]
lettered(EX)

section(doc, "22.2", "No Further Extension.")
para(doc, "The Extension Option may be exercised only once. If the conditions in Section 22.1 are not satisfied by the required date, the Extension Option shall lapse, and the Loan shall be due and payable on the Mini-Perm Maturity Date.")

doc.add_page_break()
h1(doc, "SIGNATURE PAGE", size=11, space_before=0)
para(doc, "IN WITNESS WHEREOF, the parties have executed this Agreement as of the date first written above.")
para(doc, "", space_after=6)
table(doc, [
    ["BORROWER:\n\nHARBORVIEW CAPITAL PARTNERS LLC,\na North Carolina limited liability company\n\nBy: _________________________________\nName: Elena Vasquez-Torres\nTitle: Managing Member\n\nDate: ______________________",
     "LENDER:\n\nPINNACLE SAVINGS BANK, N.A.,\na national banking association\n\nBy: _________________________________\nName: David Forsythe\nTitle: Senior Vice President,\nCommercial Real Estate Lending\n\nDate: ______________________"],
], widths=[3.0, 3.0], header=False, size=9.5)
para(doc, "GUARANTORS (for the limited purposes of Articles 6, 14, 17, and 21):", space_after=6)
table(doc, [
    ["_________________________________\nELENA VASQUEZ-TORRES, individually\n\nDate: ______________________",
     "_________________________________\nREGINALD K. OSEI, individually\n\nDate: ______________________"],
], widths=[3.0, 3.0], header=False, size=9.5)
h_note(doc, "Guarantors execute this Agreement solely for the purposes of Article 6 (Representations and Warranties), Article 14 (Guaranties and Recourse), Article 17 (Indemnities), Article 21 (Miscellaneous), and any other provision expressly applicable to the Guarantors. The operative guaranty obligations are set forth in the separate Guaranty agreements.")

# ================================================================== SCHEDULES
def sched_header(num, name, note=None):
    doc.add_page_break()
    p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_after = Pt(2)
    r = p.add_run("SCHEDULE %s" % num); r.bold = True; r.font.size = Pt(11); r.font.color.rgb = NAVY
    p2 = doc.add_paragraph(); p2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p2.paragraph_format.space_after = Pt(10)
    r2 = p2.add_run(name.upper()); r2.bold = True; r2.font.size = Pt(10.5); r2.font.color.rgb = NAVY

sched_header("1", "Loan Terms")
table(doc, [
    ["Term", "Provision", "Reference"],
    ["Loan Amount", "$47,500,000 [Alternative B: $45,360,000]", "Section 2.1"],
    ["Loan Type", "Construction-to-mini-permanent; non-revolving commitment; milestone Advances", "Section 2.2"],
    ["Construction Period", "Closing Date through August 28, 2027 (30 months from a February 28, 2025 closing)", "Section 1.1"],
    ["Mini-Perm Period", "August 29, 2027 through August 28, 2028 (12 months)", "Section 1.1"],
    ["Extension Option", "One 6-month extension to February 28, 2029, on the conditions in Article 22", "Article 22"],
    ["Interest Rate \u2014 Construction", "Daily Simple SOFR + 3.25% per annum", "Section 2.3"],
    ["Interest Rate \u2014 Mini-Perm", "Daily Simple SOFR + 3.50% per annum", "Section 2.3"],
    ["SOFR Floor", "1.00% per annum, applicable to both periods", "Section 2.4"],
    ["Default Rate", "Applicable Rate + 5.00% per annum", "Section 2.5"],
    ["Interest Calculation", "Actual days elapsed / 360-day year; payable monthly in arrears on the first Business Day of each month", "Section 2.3"],
    ["Origination Fee", "$475,000 (1.00%), funded from Loan proceeds with the Initial Advance", "Section 2.6(a)"],
    ["Exit Fee", "0.50% of outstanding principal if repaid during the Construction Period; 0.25% if repaid during the first six months of the Mini-Perm Period; zero thereafter", "Section 2.6(b)"],
    ["Unused Line Fee", "0.25% per annum on the average daily undrawn Commitment, payable quarterly in arrears", "Section 2.6(c)"],
    ["Extension Fee", "0.25% of the then-outstanding principal balance", "Section 2.6(d)"],
    ["Late Charge", "5.00% of any amount more than five (5) days overdue", "Section 2.7"],
    ["Interest Reserve", "$4,850,000, funded at closing, applied monthly, with adequacy testing and replenishment", "Section 5.5"],
    ["Retainage", "10% of each hard-cost Advance ($3,475,000 in the aggregate), held by Lender and released post-CO", "Sections 5.3 and 5.8"],
    ["Equity Contribution", "$2,140,000, deposited to the Equity Escrow Account and disbursed before Loan proceeds", "Sections 5.4 and 9.1"],
    ["Mezzanine Loan", "$9,200,000; 12.50% fixed; coterminous; subordinated pledge of membership interests", "Article 18"],
    ["Financial Covenants", "LTC \u2264 80.00%; LTV (as-completed) \u2264 65.00%; LTV (as-stabilized) \u2264 65.00%; DSCR \u2265 1.25x; Net Worth \u2265 $12,000,000; Guarantor Liquidity \u2265 $5,000,000", "Article 9"],
    ["Guaranties", "Completion Guaranty; Carry Guaranty; Partial Repayment Guaranty ($11,875,000 aggregate); Environmental Indemnity (unlimited)", "Article 14"],
    ["Governing Law; Venue", "North Carolina; Durham County (state or federal)", "Sections 21.1 and 21.2"],
], widths=[1.55, 3.55, 1.0], header=True, size=8.5, bold_first_col=True)

sched_header("2", "Permitted Exceptions")
para(doc, "The Deed of Trust shall be a first-priority Lien on the Property, subject only to the following Permitted Exceptions, which are conformed to Schedule B \u2014 Part II of the Title Commitment No. NC-2024-88712 dated December 5, 2024:", size=9.5)
table(doc, [
    ["No.", "Permitted Exception", "Status / Requirement"],
    ["1", "Rights or claims of parties in possession not shown by the public records", "To be deleted upon delivery of a satisfactory Survey and an owner\u2019s affidavit of possession"],
    ["2", "Encroachments, overlaps, boundary line disputes, or other matters disclosed by an accurate survey", "To be deleted to the extent the Survey discloses none; otherwise insured over"],
    ["3", "Easements, or claims of easements, not shown by the public records", "To be deleted upon delivery of a satisfactory Survey"],
    ["4", "Liens for services, labor, or materials not shown by the public records (N.C.G.S. Chapter 44A)", "Retained as a standard exception; Lender to receive an ALTA 9 endorsement, owner\u2019s and contractor\u2019s no-lien affidavits, and unconditional waivers for all pre-closing work"],
    ["5", "Taxes or special assessments not shown as existing liens by the public records", "Retained as a standard exception"],
    ["6", "Utility service, connection, maintenance, tap, capacity, and construction charges", "Retained as a standard exception"],
    ["7", "Ad valorem real property taxes for fiscal year 2025 and subsequent years, not yet due and payable (2024 taxes of $29,847.12 and $19,218.44 paid in full)", "Permitted Exception"],
    ["8", "Easement in favor of Duke Energy Carolinas, LLC, 20 feet in width along the western boundary of Parcel 0821-04-72-3341 (Book 4387, Page 621, Durham County Registry, dated March 22, 1997)", "Permitted Exception \u2014 Lender confirms the proposed Improvements do not encroach upon the easement strip"],
    ["9", "Stormwater Management Easement in favor of the City of Durham affecting approximately 0.22 acres in the southern portion of Parcel 0821-04-72-3341 (Book 7421, Page 212, dated April 8, 2022; plat at Plat Book 232, Page 91)", "Permitted Exception \u2014 Lender confirms no Improvements are constructed within the easement area"],
    ["\u2014", "Deed of Trust from Foster Street Properties LLC to the trustee therein for the benefit of Triangle Commercial Bank, dated September 14, 2018, recorded in Book 6215, Page 892, securing $3,400,000", "NOT a Permitted Exception. Must be released, satisfied, or cancelled of record at or before closing (Section 3.1(e)). Outstanding balance not established in the record"],
    ["11", "Declaration of Covenants, Conditions, and Restrictions recorded by Brightleaf Historic District Association, Inc. in Book 6984, Page 1155 (dated November 3, 2014), as amended in Book 7102, Page 388 (dated June 19, 2017)", "Permitted Exception, subject to (a) satisfaction of the architectural review condition in Section 3.1(g) and (b) Borrower\u2019s compliance with Articles IV, V, VII, and IX of the Declaration, including the $0.12 per square foot annual assessment (approximately $34,500 per annum based on 287,500 gross square feet)"],
    ["12", "Terms, conditions, easements, and restrictions imposed by the City of Durham Unified Development Ordinance and the MU-D zoning district", "Permitted Exception, subject to the zoning compliance letter required by Section 3.1(s)"],
    ["13", "Facts, rights, interests, or claims not shown by the public records but ascertainable by inspection or asserted by persons in possession", "To be deleted upon delivery of the Survey and an owner\u2019s affidavit of possession"],
    ["\u2014", "Deed notice and declaration of land use restriction required by Condition 4 of the NCDEQ NFA Letter (Site ID IHSB-24-1203)", "Permitted Exception once recorded \u2014 recording is a condition precedent under Section 3.1(f). NOTE: not shown on the Title Commitment dated December 5, 2024, although the NFA Letter required recording by November 29, 2024"],
], widths=[0.45, 2.9, 2.75], header=True, size=8)
draftnote(doc, "Item numbering follows the Title Commitment except where the Term Sheet\u2019s four-item list conflicts with it. The Term Sheet\u2019s instruction that all Schedule B-II exceptions other than its four items must be \u201cremoved, released, or otherwise satisfied\u201d is not achievable for Items 4 through 7, 12, and 13. The absence of the environmental deed notice from the December 5, 2024 Title Commitment is significant: the NFA Letter required recording by November 29, 2024, and the Appraisal asserts (Section 8) that the restriction \u201cis memorialized in a Declaration of Land Use Restrictions recorded at the Durham County Register of Deeds.\u201d Both cannot be correct. See Cover Memorandum Item D-2.")

sched_header("3", "Project Budget")
para(doc, "PART 1 \u2014 Uses of Funds (Total Project Costs: $56,700,000). The following budget is the Borrower-prepared detailed budget dated January 8, 2025, adopted as the initial Approved Budget subject to the corrections and qualifications noted.", size=9.5)
budget = [
    ["Line", "Category / Description", "Amount", "Note"],
    ["1.01", "LAND ACQUISITION \u2014 601 & 615 Foster Street (3.47 acres); previously closed", "8,200,000", "Funded per Borrower\u2019s budget from Mezzanine Loan proceeds; see Cover Memo Item A-3"],
    ["", "Subtotal \u2014 Land Acquisition", "8,200,000", ""],
    ["2.01", "Site work \u2014 demolition, grading, utilities, paving (Graystone)", "3,180,000", ""],
    ["2.02", "Foundations \u2014 deep foundations, mat slab, waterproofing", "2,950,000", ""],
    ["2.03", "Structural \u2014 concrete & steel, podium and superstructure", "6,420,000", ""],
    ["2.04", "Building envelope \u2014 cladding, windows, roofing", "4,275,000", ""],
    ["2.05", "MEP systems \u2014 mechanical, electrical, plumbing, fire protection", "5,850,000", ""],
    ["2.06", "Interior finishes \u2014 residential (212 units)", "5,940,000", ""],
    ["2.07", "Interior finishes \u2014 retail core & shell (18,400 SF, 7 bays)", "920,000", "Tenant improvements for retail are not budgeted"],
    ["2.08", "Parking structure \u2014 4 levels, 276 spaces", "3,590,000", "Includes soil vapor mitigation system per NFA Letter Condition 1"],
    ["2.09", "Amenities and common areas", "1,625,000", ""],
    ["", "Subtotal \u2014 Hard Construction Costs (GMP)", "34,750,000", "10% Retainage = $3,475,000"],
    ["3.01", "Architecture and engineering (Meridian Design Collective PC)", "1,680,000", ""],
    ["3.02", "Permits and impact fees (City of Durham / Durham County)", "685,000", ""],
    ["3.03", "Legal fees \u2014 Borrower (Calloway & Strauss PLLC)", "425,000", ""],
    ["3.04", "Legal fees \u2014 Lender and title/escrow (Ashford, Cromdale / Aldersgate)", "310,000", "Funded from Loan proceeds; see Section 21.3"],
    ["3.05", "Environmental and geotechnical (Sentinel Environmental Consulting LLC)", "185,000", "Excludes $485,000 of pre-closing remediation already incurred (Phase I ESA \u00a76.3)"],
    ["3.06", "Appraisal (Ridgeline Appraisal Services Inc.)", "35,000", ""],
    ["3.07", "Title insurance and recording (Aldersgate Title & Escrow Inc.)", "245,000", ""],
    ["3.08", "Construction inspection and monitoring", "125,000", "Vendor to be designated"],
    ["3.09", "Builder\u2019s risk insurance", "210,000", "Premium budgeted only for the construction period"],
    ["3.10", "Marketing and lease-up", "250,000", "No leasing commissions or retail tenant improvements budgeted"],
    ["", "Subtotal \u2014 Soft Costs", "4,150,000", ""],
    ["4.01", "Interest reserve \u2014 capitalized interest, 30 months", "4,850,000", "See Section 5.5 and Cover Memo Item H-1"],
    ["4.02", "Loan origination fee (1.00% of $47,500,000)", "475,000", ""],
    ["", "Subtotal \u2014 Financing Costs", "5,325,000", ""],
    ["5.01", "Developer fee \u2014 5.00% of Total Project Costs", "2,835,000", "Borrower\u2019s budget allocates $1,835,000 to the senior Loan and $1,000,000 to the Mezzanine Loan; see Section 5.13"],
    ["", "Subtotal \u2014 Developer Fee", "2,835,000", ""],
    ["6.01", "Hard cost contingency (3.28% of hard costs)", "1,140,000", ""],
    ["6.02", "Soft cost contingency (7.23% of soft costs)", "300,000", ""],
    ["", "Subtotal \u2014 Contingency", "1,440,000", ""],
    ["", "TOTAL PROJECT COSTS", "56,700,000", "Recomputed and confirmed: 8,200,000 + 34,750,000 + 4,150,000 + 4,850,000 + 475,000 + 2,835,000 + 1,440,000 = 56,700,000"],
]
rows = [budget[0]] + [[r[0], r[1], "$" + r[2] if r[2] else "", r[3]] for r in budget[1:]]
table(doc, rows, widths=[0.42, 3.35, 0.9, 1.45], header=True, size=7.8, align_right_cols=(2,))
para(doc, "Costs not included in the Approved Budget. The following costs are not included in the Approved Budget and must be funded by Borrower from Equity Contribution funds or added to Total Project Costs with Lender\u2019s written consent: (a) the Unused Line Fee (approximately $119,000 over the Construction Period, assuming an average undrawn balance of $19,000,000); (b) the Exit Fee ($237,500 if repaid during the Construction Period or $118,750 if repaid during the first six months of the Mini-Perm Period); (c) pre-closing demolition and remediation costs of approximately $680,000 (per the Appraisal) or $485,000 of remediation costs alone (per the Phase I ESA); (d) the outstanding balance of the Triangle Commercial Bank deed of trust in an amount not established in the record; (e) retail tenant improvements and leasing commissions; and (f) any Interest Reserve shortfall identified under Section 5.5(d).", size=9)
h2(doc, "PART 2 \u2014 Sources of Funds")
table(doc, [
    ["Source", "As Proposed in Term Sheet and Credit Memorandum", "Recommended Conforming Structure (Alternative B)", "% of Total (Alt. B)"],
    ["Senior Construction Loan \u2014 Pinnacle Savings Bank, N.A.", "$47,500,000", "$45,360,000", "80.00%"],
    ["Mezzanine Loan \u2014 Brightleaf Mezzanine Capital LLC", "$9,200,000", "$9,200,000", "16.23%"],
    ["Borrower Equity Contribution (verified cash)", "$0", "$2,140,000", "3.77%"],
    ["Borrower land contribution (in kind)", "$0 / not reflected", "$0 \u2014 land funded by Mezzanine Loan per Borrower\u2019s budget", "0.00%"],
    ["TOTAL SOURCES", "$56,700,000", "$56,700,000", "100.00%"],
], widths=[2.35, 1.7, 1.55, 0.7], header=True, size=8, shade_last_row=True)
h_note(doc, "Reconciliation note: Total sources equal Total Project Costs of $56,700,000 in both columns. In the as-proposed column, the $47,500,000 senior Loan plus the $9,200,000 Mezzanine Loan equal Total Project Costs with no equity; the Borrower\u2019s detailed budget achieves this by applying $8,200,000 of Mezzanine Loan proceeds to the land acquisition and $1,000,000 to the Developer Fee. The land is therefore not, as the Term Sheet (Section 5) and Credit Memorandum (Section 5.1) describe it, a Borrower equity contribution. See Cover Memorandum Items A-1, A-3, and A-4.")

h2(doc, "PART 3 \u2014 Schedule 3-A: Statement of Member Capital Contributions")
table(doc, [
    ["Member", "Interest", "Contribution to Date", "Form / Source", "Guarantor?"],
    ["Elena Vasquez-Torres", "62%", "$8,200,000", "Land contribution at cost basis (per Borrower\u2019s operating agreement and organizational chart). NOTE: the Title Commitment shows title vested in Borrower by Special Warranty Deed dated June 12, 2023 from Foster Street Properties LLC (Book 7598, Pages 443 and 445); the Phase I ESA states acquisition in 2022; the Appraisal states acquisition in early 2024", "Yes"],
    ["Brightleaf Investors Group LLC", "28%", "$0", "Issued in consideration of a commitment to arrange mezzanine financing (Operating Agreement \u00a75.1(b)); common control with Mezzanine Lender through Thomas R. Chen", "No"],
    ["Reginald K. Osei", "10%", "$0", "Issued in consideration of development management services (Operating Agreement \u00a75.1(c))", "Yes"],
    ["TOTAL", "100%", "$8,200,000", "No member has contributed cash to Borrower", "\u2014"],
], widths=[1.35, 0.55, 1.05, 2.55, 0.6], header=True, size=7.8, shade_last_row=True)
draftnote(doc, "Borrower must deliver documentation substantiating the land contribution and the identity of the contributing member. The four documents in the record give three different acquisition dates (2022 per the Phase I ESA; June 12, 2023 per the Title Commitment; \u201cearly 2024\u201d per the Appraisal), and the operating agreement recital that Ms. Vasquez-Torres acquired the land personally and contributed it to Borrower \u201cupon formation\u201d (March 14, 2019) is inconsistent with a 2023 conveyance directly from a third party to Borrower. See Cover Memorandum Item A-5.")

sched_header("4", "Draw Schedule and Retainage")
para(doc, "The following draw schedule restates the Term Sheet draw schedule (Section 9.2) and the Borrower\u2019s draw schedule dated January 8, 2025 to (a) withhold 10% Retainage from each hard-cost Advance, (b) remove the Developer Fee and Contingency from the Retainage Release, and (c) fund the Developer Fee and Contingency only as separate, condition-governed line items.", size=9.5)
draws = [
    ["Draw", "Milestone / Purpose", "Gross Hard Costs", "Retainage Withheld", "Hard Cost Net", "Soft / Reserve / Fee", "Total Advance", "Cumulative"],
    ["1", "Closing \u2014 soft costs, interest reserve, origination fee (0% complete)", "\u2014", "\u2014", "\u2014", "9,475,000", "9,475,000", "9,475,000"],
    ["2", "Foundation complete (15%)", "5,212,500", "(521,250)", "4,691,250", "\u2014", "4,691,250", "14,166,250"],
    ["3", "Structural frame \u2014 level 3 (35%)", "6,950,000", "(695,000)", "6,255,000", "\u2014", "6,255,000", "20,421,250"],
    ["4", "Structural frame \u2014 topped out (55%)", "6,950,000", "(695,000)", "6,255,000", "\u2014", "6,255,000", "26,676,250"],
    ["5", "Building envelope complete (70%)", "5,212,500", "(521,250)", "4,691,250", "\u2014", "4,691,250", "31,367,500"],
    ["6", "MEP rough-in complete (80%)", "3,475,000", "(347,500)", "3,127,500", "\u2014", "3,127,500", "34,495,000"],
    ["7", "Interior finish \u2014 50% of units (90%)", "3,475,000", "(347,500)", "3,127,500", "\u2014", "3,127,500", "37,622,500"],
    ["8", "Substantial completion / TCO (100%)", "3,475,000", "(347,500)", "3,127,500", "\u2014", "3,127,500", "40,750,000"],
    ["", "Subtotal \u2014 Hard Costs", "34,750,000", "(3,475,000)", "31,275,000", "\u2014", "31,275,000", ""],
    ["9", "Retainage release (post-CO; conditions in Section 5.8)", "\u2014", "3,475,000", "3,475,000", "\u2014", "3,475,000", "44,225,000"],
    ["10", "Developer Fee (senior-funded portion; conditions in Section 5.13)", "\u2014", "\u2014", "\u2014", "1,835,000", "1,835,000", "46,060,000"],
    ["11", "Contingency (only as approved Change Orders require)", "\u2014", "\u2014", "\u2014", "1,440,000", "1,440,000", "47,500,000"],
    ["", "TOTAL COMMITMENT", "34,750,000", "\u2014", "34,750,000", "13,750,000", "47,500,000", ""],
]
table(doc, draws, widths=[0.35, 2.05, 0.78, 0.8, 0.78, 0.78, 0.72, 0.78], header=True, size=7.5, align_right_cols=(2, 3, 4, 5, 6, 7), shade_last_row=True)
h2(doc, "Reconciliation to the Term Sheet and Borrower Draw Schedule")
table(doc, [
    ["Item", "Term Sheet \u00a79.2 / Borrower Schedule", "Restated (this Schedule 4)", "Difference"],
    ["Draw 1 \u2014 closing", "$9,475,000", "$9,475,000", "\u2014"],
    ["Draws 2\u20138 \u2014 hard costs", "$34,750,000 (funded at 100% of gross, no retainage withheld)", "$31,275,000 (90% of gross; 10% withheld)", "($3,475,000)"],
    ["Draw 9 \u2014 labeled \u201cRetainage Release\u201d", "$3,275,000 \u2014 which equals $1,835,000 of Developer Fee plus $1,440,000 of Contingency, not the $3,475,000 of retainage", "$3,475,000 retainage only", "+$200,000"],
    ["Developer Fee funded by senior Loan", "$1,835,000 (embedded in draws)", "$1,835,000 (separate Draw 10)", "\u2014"],
    ["Contingency funded by senior Loan", "$1,440,000 (embedded in draws)", "$1,440,000 (separate Draw 11)", "\u2014"],
    ["Cumulative hard-cost cash disbursed", "$38,225,000 against a $34,750,000 GMP \u2014 over-advance of $3,475,000", "$34,750,000", "($3,475,000)"],
    ["Column totals as presented in the Borrower\u2019s schedule", "$48,500,000 (sum of column cells) vs. $47,500,000 stated", "$47,500,000", "($1,000,000)"],
], widths=[1.9, 2.35, 1.35, 0.85], header=True, size=7.5, align_right_cols=(3,))
h_note(doc, "Recomputation notes. (1) The Borrower\u2019s Draw Schedule worksheet (\u201cDraw Schedule\u201d tab, Section 1) presents a TOTAL row of $47,500,000, but its column cells sum to $48,500,000 (hard costs net of retainage $34,750,000 + soft costs $4,150,000 + interest reserve $4,850,000 + origination fee $475,000 + developer fee $2,835,000 + contingency $1,440,000). The $1,000,000 difference is the portion of the Developer Fee that the Borrower\u2019s Detailed Budget allocates to the Mezzanine Loan, which does not belong in a senior-loan draw schedule. (2) The Developer Fee column cells total $923,750 against a stated total of $2,835,000; the Contingency column cells total $3,351,250 against a stated total of $1,440,000; the Retainage column cells total $(3,475,000) against a stated total of $0. (3) Draw 9\u2019s row does not foot: $3,475,000 \u2212 $3,475,000 + $200,000 + $600,000 = $800,000, not the $3,275,000 presented. These are arithmetic errors in a document the Lender will rely upon to fund the Loan; the Borrower must deliver a corrected schedule before closing. See Cover Memorandum Item F-1.")

sched_header("5", "Financial Covenants and Testing")
table(doc, [
    ["Covenant", "Requirement", "Testing / Measurement", "Cure"],
    ["Loan-to-Cost Ratio", "Not more than 80.00%", "Closing Date, each Advance, and each budget modification. Numerator: the Loan Amount. Denominator: Total Project Costs. As computed at closing on the stated figures: 83.77%", "No cure available; requires Commitment reduction to $45,360,000 or increase of Total Project Costs to $59,375,000"],
    ["Loan-to-Value \u2014 As-Completed", "Not more than 65.00%", "Closing Date, upon each reappraisal, and at each extension. $47,500,000 \u00f7 $72,800,000 = 65.25%", "Requires Loan reduction to $47,320,000 or reappraisal"],
    ["Loan-to-Value \u2014 As-Stabilized", "Not more than 65.00%", "$47,500,000 \u00f7 $76,200,000 = 62.34% \u2014 compliant", "\u2014"],
    ["DSCR", "Not less than 1.25x", "At commencement of the Mini-Perm Period on a projected stabilized basis; annually thereafter on actual trailing 12-month NOI; at any extension. NOI $4,876,800 \u00f7 interest-only debt service $3,728,750 (at 7.85%) = 1.31x", "Principal curtailment or cash collateral deposit within 30 days"],
    ["DSCR \u2014 stress", "Reference only", "+200 bps: rate 9.85%, debt service $4,678,750, DSCR 1.04x \u2014 below the 1.25x minimum", "Interest rate cap required on extension (Section 22.1(f))"],
    ["DSCR \u2014 without 14 restricted units", "Reference only", "NOI $4,499,640 \u00f7 $3,728,750 = 1.21x \u2014 below the 1.25x minimum", "Resolution of the Restricted Area issue under Section 4.3"],
    ["Borrower Net Worth", "Not less than $12,000,000", "Annually within 120 days of fiscal year end", "Additional Equity Contribution (limited)"],
    ["Guarantor Liquidity", "Not less than $5,000,000 combined", "Quarterly within 45 days of quarter end; excludes interests in Borrower, pledged assets, and non-liquid assets", "Additional Equity Contribution (limited)"],
], widths=[1.35, 1.4, 2.35, 1.35], header=True, size=7.8)
h_note(doc, "Definitions and computational conventions: (a) interest is computed on an actual/360 basis at the Applicable Rate in effect on the testing date; (b) Net Operating Income is computed on an accrual basis consistent with the Appraisal methodology and reflects a replacement reserve of not less than $250 per unit per annum; (c) the property management fee is 3.5% of Effective Gross Income; (d) Debt Service is interest-only, consistent with the interest-only payment structure of the Loan. All figures above have been independently recomputed from the source documents.")

sched_header("6", "Insurance Requirements")
table(doc, [
    ["Coverage", "Minimum Limit / Form", "Required Endorsements", "Period"],
    ["Builder\u2019s risk (all-risk, special form, replacement cost)", "Not less than full replacement cost of the completed Improvements; not less than $56,700,000 in any event (Term Sheet figure: $34,750,000)", "Mortgagee and loss payee; soft cost and materials-in-transit; waiver of subrogation; 30 days\u2019 notice", "Construction Period"],
    ["Commercial general liability", "$5,000,000 per occurrence / $10,000,000 aggregate; premises, products-completed operations, contractual, personal and advertising injury", "Additional insured (primary and non-contributory); waiver of subrogation", "Loan term"],
    ["Umbrella / excess liability", "$10,000,000 per occurrence and aggregate, excess of CGL, employer\u2019s liability, and automobile", "Additional insured; 30 days\u2019 notice", "Loan term"],
    ["Workers\u2019 compensation and employer\u2019s liability", "Statutory (N.C.G.S. Chapter 97); employer\u2019s liability $1,000,000", "Waiver of subrogation in favor of Lender", "Loan term"],
    ["Property \u2014 special form, replacement cost", "Full insurable value of the Improvements", "Mortgagee and loss payee", "Mini-Perm Period"],
    ["Business income / rental loss", "Not less than 12 months of Net Operating Income and continuing expenses", "Mortgagee and loss payee", "Mini-Perm Period"],
    ["Flood", "Maximum available under NFIP if any portion of the Property is in a Special Flood Hazard Area. The Phase I ESA and the Appraisal both place the Property in Zone X (minimal hazard), so flood insurance is not currently required", "\u2014", "Loan term"],
    ["Professional liability \u2014 Architect", "$2,000,000 per claim and aggregate", "Certificate naming Lender", "Loan term plus 3 years"],
    ["Contractor\u2019s pollution liability", "$2,000,000 covering work in the Restricted Area and under the soil management plan", "Additional insured; certificate naming Lender", "Construction Period"],
    ["Builder\u2019s risk \u2014 deductible", "Not more than $25,000 without Lender\u2019s consent", "\u2014", "Construction Period"],
], widths=[1.5, 2.2, 1.75, 0.9], header=True, size=7.6)

sched_header("7", "Reporting Calendar")
table(doc, [
    ["Deliverable", "Frequency", "Deadline", "Source Provision"],
    ["Monthly construction progress report, budget reconciliation, schedule update, change order log, and Interest Reserve reconciliation", "Monthly", "15 days after month end", "Term Sheet \u00a721.1; Section 5.5(f)"],
    ["Quarterly unaudited financial statements of Borrower", "Quarterly", "45 days after quarter end", "Term Sheet \u00a721.1"],
    ["Quarterly guarantor liquidity certification and personal financial statement", "Quarterly", "45 days after quarter end", "Term Sheet \u00a7\u00a76.5, 21.1; Section 9.5"],
    ["Annual audited (or reviewed) financial statements of Borrower", "Annually", "120 days after fiscal year end", "Term Sheet \u00a721.1"],
    ["Annual personal financial statements of each Guarantor, with tax returns", "Annually", "120 days after fiscal year end", "Term Sheet \u00a721.1"],
    ["Annual net worth certificate and Compliance Certificate", "Annually", "120 days after fiscal year end", "Sections 9.4 and 9.6"],
    ["Leasing report (units leased, rents, concessions, occupancy)", "Monthly, after CO", "15 days after month end", "Section 7.1(m)"],
    ["Interest Reserve Adequacy Certificate", "Each Draw Request and quarterly", "With each Draw Request", "Section 5.5(d)"],
    ["NCDEQ correspondence, monitoring results, and system verification reports", "As received / as submitted", "5 Business Days", "Section 10.2(f)"],
    ["Notice of Default, litigation, environmental event, casualty, or material adverse change", "Event-driven", "3 to 5 Business Days", "Section 7.1(i)"],
    ["Copies of all material governmental notices, permits, and regulatory communications", "Event-driven", "Promptly upon receipt", "Term Sheet \u00a721.1"],
], widths=[2.6, 1.0, 1.35, 1.4], header=True, size=7.8)

sched_header("8", "Environmental Compliance Requirements (NCDEQ NFA Letter)")
para(doc, "Site ID IHSB-24-1203 / Incident No. NONUST-24-0847. Each of the following is a condition of the NFA Letter dated September 30, 2024 and is an affirmative covenant of Borrower under Article 10. Non-compliance with any of the following is an Event of Default under Section 15.1(l).", size=9.5)
table(doc, [
    ["Condition", "Requirement", "Deadline / Frequency", "Evidence to be Delivered to Lender"],
    ["1 \u2014 Soil vapor mitigation system", "Passive sub-slab depressurization system beneath any enclosed structure over the Restricted Area, convertible to active; designed by a North Carolina licensed professional engineer in accordance with NCDEQ Division of Waste Management guidance", "Design before foundation construction; as-builts and performance verification to NCDEQ within 90 days after completion of the foundation in the Restricted Area", "Design drawings and PE certification; construction photographs; as-built drawings; performance verification report; NCDEQ transmittal"],
    ["2 \u2014 Land use restriction (non-residential)", "Restricted Area (approx. 0.38 acres, northeast corner of Parcel 0821-04-72-4102) restricted to non-residential use. NCDEQ states that any change to residential or other sensitive use would require additional investigation and/or remediation and a modification of the NFA determination", "Continuing", "Annual certification of use; floor plan overlay under Section 10.5; any NCDEQ modification"],
    ["3 \u2014 Soil management plan", "NCDEQ-approved plan governing all excavation, grading, and subsurface disturbance within the Restricted Area (screening, stockpiling, dust control, worker safety, disposal)", "Approved before any subsurface disturbance; complied with throughout construction", "Approved plan; contractor acknowledgment; soil disposal manifests"],
    ["4 \u2014 Deed notice", "Notice recorded in the Durham County Registry describing the Restricted Area, the nature and extent of residual contamination, and the non-residential use restriction", "Required by the NFA Letter within 60 days of September 30, 2024, i.e., by November 29, 2024. Not reflected on the Title Commitment dated December 5, 2024", "Recorded instrument; recording stamp; title bring-down confirming recordation"],
    ["\u2014 Additional \u2014 delineation", "Metes-and-bounds description of the Restricted Area overlaid on the Survey and on each building floor plan; written Architect determination of any residential occupancy space within or above the Restricted Area", "Within 30 days after the Closing Date", "Surveyor certification; Architect certification; recorded memorandum (if required)"],
    ["\u2014 Additional \u2014 Phase I shelf life", "Phase I ESA dated October 28, 2024; AAI shelf life 180 days (through April 26, 2025) under 40 C.F.R. \u00a7 312.20(c)", "If the Closing Date occurs after April 26, 2025, an updated Phase I ESA is required", "Updated report; reliance letter addressed to Lender"],
], widths=[1.1, 2.4, 1.75, 1.0], header=True, size=7.5)
draftnote(doc, "The remediation volumes stated in the record are inconsistent: the Phase I ESA (\u00a76.1) states that approximately 1,200 cubic yards of soil were excavated; the Credit Memorandum (\u00a78.2) states approximately 340 cubic yards; and the Appraisal (\u00a78) states approximately 320 cubic yards and that the UST itself was removed during remediation. The Phase I ESA (\u00a72.2) in fact states that the UST was decommissioned and removed in approximately 1998, and describes a 2,000-gallon diesel tank installed circa 1972 for a backup generator, whereas the Appraisal describes a tank installed in the 1950s for heating oil and out of service since approximately 1988. These discrepancies do not affect the covenant requirements but must be reconciled in the reliance letter and in the NCDEQ file before closing. See Cover Memorandum Item D-5.")

# ================================================================== EXHIBITS
doc.add_page_break()
p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = p.add_run("EXHIBIT A"); r.bold = True; r.font.size = Pt(11); r.font.color.rgb = NAVY
p2 = doc.add_paragraph(); p2.alignment = WD_ALIGN_PARAGRAPH.CENTER
r2 = p2.add_run("LEGAL DESCRIPTION OF THE PROPERTY"); r2.bold = True; r2.font.size = Pt(10.5); r2.font.color.rgb = NAVY
para(doc, "The following descriptions are taken from Schedule A, Item 6 of Title Commitment No. NC-2024-88712 dated December 5, 2024 and are the recorded descriptions of the Property. They are subject to confirmation by the Survey required under Section 13.5.", size=9.5)
h2(doc, "Parcel 1 \u2014 Durham County PIN 0821-04-72-3341 (601 Foster Street) \u2014 approximately 2.09 acres")
para(doc, "Being all of that certain lot, tract, or parcel of land situated in the City of Durham, Durham County, North Carolina, and being more particularly described as follows:", size=9.5)
para(doc, "BEGINNING at an existing iron pipe located in the eastern right-of-way margin of Foster Street (60-foot public right-of-way), said iron pipe being located South 02\u00b014\u203233\u2033 West, 312.47 feet from the intersection of the eastern right-of-way margin of Foster Street with the southern right-of-way margin of West Corporation Street; running thence from said Beginning point along the eastern right-of-way margin of Foster Street, South 02\u00b014\u203233\u2033 West, 298.62 feet to an existing iron pipe; thence departing said right-of-way margin, South 87\u00b045\u203227\u2033 East, 305.41 feet to an existing iron pipe; thence North 02\u00b014\u203233\u2033 East, 298.62 feet to an existing iron pipe; thence North 87\u00b045\u203227\u2033 West, 305.41 feet to the point and place of BEGINNING; containing approximately 2.09 acres as shown on that survey plat recorded in Plat Book 218, Page 47, Durham County Registry.", size=9.5, indent=0.4, italic=True)
para(doc, "Being the same property conveyed to Harborview Capital Partners LLC by Special Warranty Deed recorded in Book 7598, Page 443, Durham County Registry, dated June 12, 2023, from Foster Street Properties LLC.", size=9.5, indent=0.4)
h2(doc, "Parcel 2 \u2014 Durham County PIN 0821-04-72-4102 (615 Foster Street) \u2014 approximately 1.38 acres")
para(doc, "Being all of that certain lot, tract, or parcel of land situated in the City of Durham, Durham County, North Carolina, and being more particularly described as follows:", size=9.5)
para(doc, "BEGINNING at an existing iron pipe located in the eastern right-of-way margin of Foster Street (60-foot public right-of-way), said iron pipe being the southwestern corner of Parcel 1 described above; running thence from said Beginning point along the eastern right-of-way margin of Foster Street, South 02\u00b014\u203233\u2033 West, 201.88 feet to a new iron pipe; thence departing said right-of-way margin, South 87\u00b045\u203227\u2033 East, 297.63 feet to a new iron pipe; thence North 02\u00b014\u203233\u2033 East, 201.88 feet to an existing iron pipe, being the southeastern corner of Parcel 1 described above; thence along the southern boundary of Parcel 1, North 87\u00b045\u203227\u2033 West, 297.63 feet to the point and place of BEGINNING; containing approximately 1.38 acres as shown on that survey plat recorded in Plat Book 218, Page 48, Durham County Registry.", size=9.5, indent=0.4, italic=True)
para(doc, "Being the same property conveyed to Harborview Capital Partners LLC by Special Warranty Deed recorded in Book 7598, Page 445, Durham County Registry, dated June 12, 2023, from Foster Street Properties LLC.", size=9.5, indent=0.4)
draftnote(doc, "Verification performed: Parcel 1 dimensions 298.62\u2032 \u00d7 305.41\u2032 = 91,202 square feet = 2.094 acres (stated 2.09); Parcel 2 dimensions 201.88\u2032 \u00d7 297.63\u2032 = 60,086 square feet = 1.379 acres (stated 1.38); combined 3.473 acres, which agrees with the 3.47 acres stated in every other document and with the Appraisal\u2019s 151,153 square feet. The Phase I ESA states 1.89 acres and 1.58 acres for the same two parcels; those figures do not reconcile to the metes and bounds and appear to be erroneous. Combined frontage along Foster Street is 500.50 feet (298.62 + 201.88), not the 420 feet stated in the Appraisal. The descriptions must be conformed to the Survey and the Title Policy must insure the surveyed acreage.")

doc.add_page_break()
p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = p.add_run("EXHIBIT B"); r.bold = True; r.font.size = Pt(11); r.font.color.rgb = NAVY
p2 = doc.add_paragraph(); p2.alignment = WD_ALIGN_PARAGRAPH.CENTER
r2 = p2.add_run("FORM OF DRAW REQUEST AND BORROWER\u2019S CERTIFICATE"); r2.bold = True; r2.font.size = Pt(10.5); r2.font.color.rgb = NAVY
para(doc, "Draw Request No. ____   Requested funding date: ____________   Milestone (Schedule 4): ____________   Cumulative % complete: ______%", size=9.5)
para(doc, "Borrower hereby requests an Advance in the total amount of $______________, allocated as follows:", size=9.5)
table(doc, [
    ["Budget line", "Description", "Amount requested (gross)", "Less: Retainage 10%", "Net amount requested"],
    ["2.01\u20132.09", "Hard construction costs (GMP)", "", "", ""],
    ["3.01\u20133.10", "Soft costs", "n/a", "n/a", ""],
    ["4.01", "Interest reserve (only with Draw 1)", "n/a", "n/a", ""],
    ["4.02", "Origination fee (only with Draw 1)", "n/a", "n/a", ""],
    ["5.01", "Developer Fee (Draw 10 only)", "n/a", "n/a", ""],
    ["6.01\u20136.02", "Contingency (Draw 11 only)", "n/a", "n/a", ""],
    ["", "TOTAL", "", "", ""],
], widths=[0.8, 2.3, 1.05, 1.0, 1.15], header=True, size=8, align_right_cols=(2, 3, 4))
para(doc, "Borrower certifies that: (a) the work, materials, and costs for which reimbursement is requested have been completed or incurred in accordance with the Approved Plans and Specifications and the Approved Budget; (b) all conditions precedent in Article 4 have been satisfied; (c) all representations and warranties remain true and correct in all material respects; (d) no Default or Event of Default exists; (e) all subcontractors and materialmen have been paid all amounts previously funded; (f) the Interest Reserve Adequacy Certificate attached as Annex 1 is true and correct; (g) the sources and uses reconciliation attached as Annex 2 demonstrates that no cost overrun exists; (h) no Advance is requested for any work within or above the Restricted Area unless the conditions of Section 4.3 have been satisfied; and (i) the remaining undisbursed Loan proceeds, together with available equity, are sufficient to complete the Project.", size=9.5)
table(doc, [
    ["Attachments required", "Delivered"],
    ["AIA G702 Application and Certificate for Payment, certified by Contractor and Architect", "\u2610"],
    ["AIA G703 Continuation Sheet", "\u2610"],
    ["Architect\u2019s Requisition Certificate", "\u2610"],
    ["Construction Inspector\u2019s report (Lender-engaged)", "\u2610"],
    ["Conditional lien waivers (statutory form, N.C.G.S. Chapter 44A) \u2014 Contractor and all subcontractors", "\u2610"],
    ["Unconditional lien waivers for all previously funded amounts", "\u2610"],
    ["Title date-down endorsement from Aldersgate Title & Escrow Inc.", "\u2610"],
    ["Certificates of insurance / evidence of continued coverage", "\u2610"],
    ["Updated construction schedule and change order log", "\u2610"],
    ["Updated sources and uses reconciliation", "\u2610"],
    ["Interest Reserve Adequacy Certificate (Exhibit D)", "\u2610"],
    ["Evidence of NFA Letter compliance and Restricted Area status", "\u2610"],
], widths=[5.6, 0.9], header=True, size=8.5)
para(doc, "HARBORVIEW CAPITAL PARTNERS LLC       By: ____________________________       Name: Elena Vasquez-Torres       Title: Managing Member       Date: ______________", size=9.5)

doc.add_page_break()
p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = p.add_run("EXHIBIT C"); r.bold = True; r.font.size = Pt(11); r.font.color.rgb = NAVY
p2 = doc.add_paragraph(); p2.alignment = WD_ALIGN_PARAGRAPH.CENTER
r2 = p2.add_run("FORM OF COMPLIANCE CERTIFICATE"); r2.bold = True; r2.font.size = Pt(10.5); r2.font.color.rgb = NAVY
para(doc, "The undersigned, the Managing Member and chief financial officer of Harborview Capital Partners LLC, certifies to Pinnacle Savings Bank, N.A. as of ______________, 20__ that:", size=9.5)
table(doc, [
    ["Covenant", "Required", "Actual", "Compliant"],
    ["Loan-to-Cost Ratio (Section 9.1)", "\u2264 80.00%", "________%", "\u2610 Yes  \u2610 No"],
    ["Loan-to-Value, as-completed (Section 9.2)", "\u2264 65.00%", "________%", "\u2610 Yes  \u2610 No"],
    ["Loan-to-Value, as-stabilized (Section 9.2)", "\u2264 65.00%", "________%", "\u2610 Yes  \u2610 No"],
    ["DSCR (Section 9.3)", "\u2265 1.25x", "________x", "\u2610 Yes  \u2610 No"],
    ["Borrower Net Worth (Section 9.4)", "\u2265 $12,000,000", "$__________", "\u2610 Yes  \u2610 No"],
    ["Guarantor Liquidity, combined (Section 9.5)", "\u2265 $5,000,000", "$__________", "\u2610 Yes  \u2610 No"],
], widths=[2.5, 1.0, 1.4, 1.6], header=True, size=8.5)
para(doc, "The undersigned further certifies that: (a) no Default or Event of Default exists and no event has occurred that with notice or lapse of time would constitute a Default or Event of Default; (b) all representations and warranties in Article 6 are true and correct in all material respects; (c) Borrower is in compliance with the SPE covenants in Article 11 and maintains an Independent Manager approved by Lender; (d) Borrower is in compliance with all conditions of the NFA Letter, including the recorded deed notice, the soil management plan, and the soil vapor mitigation system; (e) no residential space has been constructed, leased, or occupied within or above the Restricted Area except as permitted under Section 4.3; (f) no Transfer has occurred; (g) Borrower has made no Distribution other than as permitted under Section 8.1(g); and (h) attached hereto are the computations supporting each covenant set forth above.", size=9.5)
para(doc, "HARBORVIEW CAPITAL PARTNERS LLC       By: ____________________________       Name: Elena Vasquez-Torres       Title: Managing Member       Date: ______________", size=9.5)

doc.add_page_break()
p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = p.add_run("EXHIBIT D"); r.bold = True; r.font.size = Pt(11); r.font.color.rgb = NAVY
p2 = doc.add_paragraph(); p2.alignment = WD_ALIGN_PARAGRAPH.CENTER
r2 = p2.add_run("FORM OF INTEREST RESERVE ADEQUACY CERTIFICATE"); r2.bold = True; r2.font.size = Pt(10.5); r2.font.color.rgb = NAVY
table(doc, [
    ["Item", "Amount / Input"],
    ["1. Interest Reserve Account balance as of the date hereof", "$__________"],
    ["2. Committed additional deposits by Borrower (documented)", "$__________"],
    ["3. Total available (line 1 + line 2)", "$__________"],
    ["4. Outstanding principal balance of the Loan", "$__________"],
    ["5. Daily Simple SOFR as of the date hereof", "________%"],
    ["6. Spread applicable to the current period", "3.25% / 3.50%"],
    ["7. All-in rate (greater of line 5 + line 6 and 4.35% + line 6)", "________%"],
    ["8. Projected interest through the next anticipated draw date", "$__________"],
    ["9. Projected interest for the 90-day period following the date hereof", "$__________"],
    ["10. Projected obligation (greater of line 8 and line 9)", "$__________"],
    ["11. Surplus / (Deficiency) (line 3 \u2212 line 10)", "$__________"],
    ["12. Deposit required under Section 5.5(d)", "$__________"],
], widths=[4.6, 1.9], header=True, size=8.5, align_right_cols=(1,))
para(doc, "Basis of projection: Draws are projected in accordance with Schedule 4; interest accrues on the average daily outstanding balance at the all-in rate in line 7; the projection assumes no unscheduled prepayment and no Event of Default. The undersigned certifies that the foregoing is true and correct and that any deficiency identified in line 11 has been or will be deposited into the Interest Reserve Account within five (5) Business Days.", size=9.5)

doc.save("/workspace/output/loan-agreement-draft.docx")
print("saved")
