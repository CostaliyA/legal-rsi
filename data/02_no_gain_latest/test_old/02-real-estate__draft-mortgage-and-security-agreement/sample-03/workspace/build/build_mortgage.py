# -*- coding: utf-8 -*-
"""Builds mortgage-and-security-agreement.docx"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from docxstyle import *
from docx.shared import Pt, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH

ARTICLES = []

# ============================================================ ARTICLE 1
ARTICLES.append(dict(num="1", title="Definitions and Rules of Construction", sections=[
 dict(num="1.1", title="Defined Terms", content=[
  ("p", "The following terms have the meanings set forth below whenever used in this Mortgage. Terms defined in the Uniform Commercial Code as in effect in the State of South Carolina (the \u201cCode\u201d) and not otherwise defined in this Mortgage have the meanings given to them in the Code."),
  ("def", "Affiliate", "means, with respect to any Person, any other Person that directly or indirectly Controls, is Controlled by, or is under common Control with, such Person. \u201cControl\u201d means the possession, directly or indirectly, of the power to direct or cause the direction of the management and policies of a Person, whether through ownership of voting interests, by contract, or otherwise."),
  ("def", "ALTA Survey", "means the ALTA/NSPS Land Title Survey of the Property prepared by Cartwright Land Surveying LLC, dated January 15, 2025, recorded in Plat Book 64 at Page 91 in the RMC Office, conforming to the 2021 Minimum Standard Detail Requirements for ALTA/NSPS Land Title Surveys, together with any re-certification thereof, recertified to a date not more than ninety (90) days prior to the Closing Date."),
  ("def", "Applicable Law", "means all present and future federal, state and local statutes, codes, ordinances, orders, rules, regulations, permits, licenses, judgments, decrees and requirements of any Governmental Authority applicable to Mortgagor, Guarantor or the Property, including Environmental Laws and the LUR."),
  ("def", "Bankruptcy Code", "means Title 11 of the United States Code, 11 U.S.C. \u00a7 101 et seq., as amended."),
  ("def", "Business Day", "means any day other than a Saturday, Sunday or day on which commercial banks in Savannah, Georgia or Charleston, South Carolina are authorized or required by law to be closed."),
  ("def", "Closing Date", "means April 15, 2025, or such later date on which the Initial Advance is made, which in no event shall be later than May 15, 2025 without Mortgagee\u2019s prior written consent."),
  ("def", "Condemnation", "means any taking of all or any part of the Property (including any transfer in lieu thereof) by any Governmental Authority having the power of eminent domain."),
  ("def", "Contractor", "means Beaufort Builders Group LLC, a South Carolina limited liability company, South Carolina General Contractor License No. SC-GC-47921, or any successor general contractor approved in writing by Mortgagee."),
  ("def", "DSCR", "means, for any period, Net Operating Income divided by Annual Debt Service, determined in accordance with Section 7.8(a)."),
  ("def", "Daily SOFR", "means the Secured Overnight Financing Rate as published by the Federal Reserve Bank of New York (or any successor administrator of the Secured Overnight Financing Rate) on the applicable Business Day, or, if such rate is not published on such Business Day, the rate published on the immediately preceding Business Day, in each case as determined pursuant to Section 4.2."),
  ("def", "Default Rate", "means a rate per annum equal to the Note Rate plus five percent (5.00%), as provided in Section 4.5."),
  ("def", "Environmental Indemnity Agreement", "means the Environmental Indemnity Agreement of even date herewith executed by Mortgagor and Guarantor in favor of Mortgagee, as the same may be amended, restated or supplemented from time to time."),
  ("def", "Environmental Laws", "means all federal, state and local laws, regulations, orders and permits relating to pollution, the protection of human health or the environment, or the use, storage, treatment, generation, transportation, handling, disposal or release of Hazardous Materials, including the Comprehensive Environmental Response, Compensation, and Liability Act, 42 U.S.C. \u00a7 9601 et seq., and the regulations and programs administered by SCDHEC, including those governing the Institutional Controls."),
  ("def", "Event of Default", "means any event or condition described in Section 10.1."),
  ("def", "GAAP", "means generally accepted accounting principles in the United States, consistently applied."),
  ("def", "Governmental Authority", "means the United States, the State of South Carolina, the City of Charleston, Charleston County, SCDHEC, and any other federal, state, regional, county or municipal body, agency, department, commission, board, bureau or instrumentality having jurisdiction over Mortgagor, Guarantor or the Property."),
  ("def", "Guarantor", "means Neil Ashford Graydon, an individual residing at 14 Church Street, Charleston, South Carolina 29401."),
  ("def", "Guaranty", "means the Guaranty Agreement of even date herewith executed by Guarantor in favor of Mortgagee, together with the completion guaranty and the interest shortfall payment guaranty described in the Term Sheet to the extent set forth therein, as the same may be amended, restated or supplemented from time to time."),
  ("def", "Hazardous Materials", "means petroleum and petroleum products, perchloroethylene and other chlorinated solvents, volatile organic compounds, asbestos, polychlorinated biphenyls, urea formaldehyde, radioactive materials, and any other substance, material or waste regulated as hazardous, toxic or a pollutant under any Environmental Law."),
  ("def", "Improvements", "means all buildings, structures, fixtures, building systems and other improvements of every kind now or hereafter located on or affixed to the Land, including without limitation all HVAC equipment (including the three (3) rooftop units and associated ductwork and controls), the passenger elevator and its cab, controls, door operators and related equipment, plumbing, electrical systems, fire protection and fire suppression systems, the vapor barrier referenced in Section 7.4, and the decorative iron balcony described in Section 3.8."),
  ("def", "Indebtedness", "means the principal of and interest on the Loan, all amounts advanced by Mortgagee under this Mortgage or the other Loan Documents (including protective advances, reserve advances, inspection fees, attorneys\u2019 fees and costs of collection), the Yield Maintenance Premium, late charges, Default Rate interest, indemnity obligations of Mortgagor hereunder, and all other sums now or hereafter owing by Mortgagor to Mortgagee under the Loan Documents."),
  ("def", "Institutional Controls", "means the institutional controls and engineering controls required by the LUR and by SCDHEC in connection with SCDHEC Site ID SC-29403-0772, including the prohibition on residential use of the ground floor of Lot 7 and the requirement to maintain, inspect and repair the Vapor Barrier."),
  ("def", "Land", "means the real property described in Exhibit A, consisting of Parcel One (Lots 7, 8 and 9 of the Hampstead Village Plat, Charleston County Tax Map Nos. 460-12-04-007, 460-12-04-008 and 460-12-04-009) and Parcel Two (the strip of land formerly known as Anson Lane, vacated by City of Charleston Ordinance No. 2019-084)."),
  ("def", "Lease(s)", "means each lease, sublease, license or other occupancy agreement affecting the Property, together with all amendments, extensions, renewals, guaranties and related security instruments, including those described in Exhibit D."),
  ("def", "Loan", "means the loan in the original principal amount of Fourteen Million Seven Hundred Fifty Thousand and No/100 Dollars ($14,750,000.00) made by Mortgagee to Mortgagor pursuant to the Loan Documents, consisting of the Initial Advance and the Renovation Holdback."),
  ("def", "Loan Documents", "means the Note, this Mortgage, the Assignment (to the extent not incorporated herein), the Environmental Indemnity Agreement, the Guaranty, the UCC-1 financing statement and fixture filing, each reserve or escrow agreement, each interest rate or hedging agreement (if any), the Term Sheet dated April 1, 2025 between Mortgagor and Mortgagee (solely to the extent it constitutes a binding commitment), and each other document, instrument or certificate now or hereafter executed by Mortgagor, Guarantor or any other Person in connection with the Loan, as each may be amended, restated, supplemented or replaced."),
  ("def", "Lockout Period", "means the period commencing on the Closing Date and ending on the date that is twenty-four (24) months thereafter (through April 15, 2027)."),
  ("def", "LUR", "means that certain land use restriction and institutional control recorded in Deed Book 1203 at Page 89 in the RMC Office for Charleston County, South Carolina, imposed by SCDHEC in connection with SCDHEC Site ID SC-29403-0772 and the No Further Action determination dated August 12, 2021, as the same may be modified only with Mortgagee\u2019s prior written consent and with SCDHEC approval."),
  ("def", "Maturity Date", "means April 15, 2030, being the date five (5) years after the Closing Date."),
  ("def", "Net Operating Income", "means, for any period, the gross revenues of the Property for such period (including base rent, additional rent, operating expense reimbursements and percentage rent actually collected, but excluding security deposits, capital contributions, loan proceeds and insurance or condemnation proceeds), less (a) vacancy and collection loss determined in accordance with Section 7.8(a), and (b) operating expenses of the Property for such period, determined in accordance with GAAP consistently applied and in a manner consistent with the annual operating statements delivered under Section 7.7(d)."),
  ("def", "Note", "means the Promissory Note of even date herewith in the original principal amount of $14,750,000.00 executed by Mortgagor and payable to the order of Mortgagee, as the same may be amended, restated, extended, renewed or replaced."),
  ("def", "Note Rate", "means a rate per annum equal to the greater of (a) Daily SOFR plus two hundred eighty-five (285) basis points, and (b) five and 85/100 percent (5.85%), being the sum of the SOFR Floor and such spread."),
  ("def", "Open Prepayment Period", "means the period commencing on the first day of the forty-ninth (49th) month following the Closing Date and ending on the Maturity Date (months 49 through 60)."),
  ("def", "Permitted Exceptions", "means those matters listed in Exhibit C, being the matters approved by Mortgagee in writing as exceptions to the Title Policy and to the warranties of title in this Mortgage."),
  ("def", "Person", "means any individual, corporation, partnership, limited liability company, joint venture, association, trust, estate, unincorporated organization or Governmental Authority."),
  ("def", "Personal Property Collateral", "means all personal property, fixtures, accounts, general intangibles and other collateral described in Sections 2.2 through 2.5, together with all proceeds and products thereof."),
  ("def", "Property", "means the Land, the Improvements, all appurtenances, easements, rights-of-way, strips, gores, riparian and other rights now or hereafter appurtenant to the Land (including the vacated right-of-way formerly known as Anson Lane), the Personal Property Collateral, all Leases and Rents, and all Reserve Funds, together with all proceeds of the foregoing."),
  ("def", "RMC Office", "means the Office of the Register of Mesne Conveyances for Charleston County, South Carolina."),
  ("def", "Renovation Budget", "means the renovation budget for the Property in the aggregate amount of Three Million One Hundred Fifty Thousand Dollars ($3,150,000.00) attached as Exhibit B, as the same may be revised only in accordance with Section 9.2."),
  ("def", "Renovation Contract", "means the construction contract of even date between Mortgagor, as owner, and Contractor, as general contractor, providing for a contract sum of Two Million Eight Hundred Fifty Thousand Dollars ($2,850,000.00) covering hard costs of construction, together with all schedules, exhibits, amendments and change orders thereto."),
  ("def", "Renovation Holdback", "means the Two Million Two Hundred Fifty Thousand Dollars ($2,250,000.00) portion of the Loan retained by Mortgagee and disbursed on a draw basis in accordance with Article 9."),
  ("def", "Reserve Funds", "means all funds held by Mortgagee under Article 6, including the Tax and Insurance Escrow, the Capital Replacement Reserve and the Tenant Improvement and Leasing Commission Reserve, together with all accounts, subaccounts, interest and earnings thereon."),
  ("def", "SCDHEC", "means the South Carolina Department of Health and Environmental Control, and any successor agency."),
  ("def", "Single-Purpose Entity or SPE", "means an entity that satisfies the separateness, purpose, capitalization, bankruptcy-remoteness and independent-manager requirements set forth in Sections 7.5 and 8.3."),
  ("def", "Substantial Completion", "means the completion of the renovation work in accordance with the approved plans and specifications, as certified by Mortgagor\u2019s architect of record, together with the issuance by the City of Charleston of a certificate of occupancy (or the equivalent) for all renovated portions of the Property."),
  ("def", "Substantial Completion Deadline", "means June 15, 2026, being the date fourteen (14) months after the Closing Date."),
  ("def", "Tenant", "means each tenant, subtenant or occupant under any Lease, including Lowcountry Provisions Inc., Harmon & Wren Design Studio LLC and Tidemark Consulting Group LLC."),
  ("def", "Term Sheet", "means the executed Term Sheet dated April 1, 2025 between Mortgagor and Mortgagee for Calverley Heritage Bank CRE Loan No. 2025-CHS-0047."),
  ("def", "Title Insurer", "means Commonwealth National Title Underwriters Inc., acting through its issuing agent Prestige Title & Settlement Services LLC."),
  ("def", "Title Policy", "means the ALTA Loan Policy (06-17-06) with South Carolina modifications issued by the Title Insurer to Mortgagee in the amount of $14,750,000.00 insuring the first priority lien of this Mortgage, subject only to the Permitted Exceptions, together with all endorsements required under Section 5.6 of the Term Sheet and Exhibit C."),
  ("def", "Transfer", "means any sale, conveyance, assignment, transfer, pledge, hypothecation, encumbrance or other disposition, whether direct or indirect, voluntary or involuntary, by operation of law or otherwise."),
  ("def", "Treasury Rate", "means the yield to maturity, as of the second (2nd) Business Day preceding the date of prepayment, of the United States Treasury security having a maturity date closest to, but not exceeding, the last day of the Yield Maintenance Period, as reported in Federal Reserve Statistical Release H.15 \u2014 Selected Interest Rates (or any successor publication), as described in Section 4.7(b)."),
  ("def", "UCC", "means the Uniform Commercial Code as in effect from time to time in the State of South Carolina, as codified at S.C. Code Ann. Title 36, Chapter 9 (and any corresponding provision of S.C. Code Ann. Title 36, Chapter 11 with respect to proceeds of accounts)."),
  ("def", "Vapor Barrier", "means the vapor barrier system installed beneath the concrete floor slab of the ground floor of Lot 7 (Bay 1, 520 King Street) as part of the remediation of SCDHEC Site ID SC-29403-0772, together with all related sub-slab depressurization or monitoring components."),
  ("def", "Yield Maintenance Period", "means the period commencing on the first day of the twenty-fifth (25th) month following the Closing Date and ending on the last day of the forty-eighth (48th) month following the Closing Date (months 25 through 48)."),
  ("def", "Yield Maintenance Premium", "has the meaning set forth in Section 4.7(b)."),
 ]),
 dict(num="1.2", title="Rules of Construction", content=[
  ("p", "In this Mortgage: (a) the words \u201cinclude,\u201d \u201cincludes\u201d and \u201cincluding\u201d are deemed to be followed by the words \u201cwithout limitation\u201d; (b) \u201cor\u201d is not exclusive; (c) references to Articles, Sections, Exhibits and Schedules are to Articles and Sections of, and Exhibits and Schedules to, this Mortgage; (d) the singular includes the plural and vice versa, and the masculine, feminine and neuter genders include each other; (e) headings are for convenience only and do not affect interpretation; (f) references to any agreement, instrument or statute are to that agreement, instrument or statute as amended, restated, supplemented or replaced from time to time, and to any rules and regulations promulgated thereunder; (g) accounting terms not otherwise defined have the meanings given under GAAP; (h) references to \u201cdays\u201d mean calendar days unless Business Days are specified; and (i) if any period expires on a day that is not a Business Day, the period is extended to the next Business Day."),
  ("p", "This Mortgage is the result of negotiation between Mortgagor and Mortgagee, each represented by counsel, and no rule of construction resolving ambiguities against the drafting party shall apply."),
 ]),
 dict(num="1.3", title="Relationship Among the Loan Documents", content=[
  ("p", "This Mortgage is one of the Loan Documents and secures the Indebtedness. The Loan Documents are intended to be read together, and a default under any Loan Document that is not cured within any applicable cure period constitutes an Event of Default under this Mortgage. If any provision of this Mortgage conflicts with the Note, the Note controls as to the amount, timing and rate of payment of principal and interest; if any provision of this Mortgage conflicts with any other Loan Document as to the creation, perfection or enforcement of any lien or security interest in the Property, this Mortgage controls. Consistent with Section 14.3 of the Term Sheet, if any provision of this Mortgage conflicts with the Term Sheet, this Mortgage controls."),
 ]),
]))

# ============================================================ ARTICLE 2
ARTICLES.append(dict(num="2", title="Granting Clauses; Security", sections=[
 dict(num="2.1", title="Mortgage of Real Property", content=[
  ("p", "For good and valuable consideration, the receipt and sufficiency of which are hereby acknowledged, and to secure the payment and performance of the Indebtedness, Mortgagor hereby grants, bargains, sells, conveys, mortgages, warrants and assigns to Mortgagee, and grants to Mortgagee a continuing first-priority mortgage lien on and security interest in, all of Mortgagor\u2019s right, title and interest in and to the following (collectively, the \u201cReal Property Collateral\u201d):"),
  ("sub", "(a)", "the fee simple estate in the Land described in Exhibit A, comprising all three (3) tax parcels designated Charleston County Tax Map Nos. 460-12-04-007, 460-12-04-008 and 460-12-04-009, together with the strip of land formerly known as Anson Lane conveyed to Mortgagor\u2019s predecessor in title by quitclaim deed recorded in Deed Book 1128 at Page 443 in the RMC Office;"),
  ("sub", "(b)", "all Improvements now or hereafter erected on or affixed to the Land, including the HVAC equipment, the passenger elevator, plumbing, electrical and fire protection systems, all other fixtures and building systems, and all replacements, additions, betterments and substitutions thereto;"),
  ("sub", "(c)", "all and singular the tenements, hereditaments, easements, rights-of-way, privileges, appurtenances, development rights, air rights, water, water rights, drainage rights and other rights and benefits now or hereafter appertaining to the Land, including the benefit of the SCE&G utility easement recorded in Deed Book 987 at Page 112 in the RMC Office to the extent not inconsistent with the Permitted Exceptions;"),
  ("sub", "(d)", "all right, title and interest of Mortgagor in and to any land lying within the right-of-way of any street, road, avenue or alley adjoining the Land, and any award made or to be made in respect thereof; and"),
  ("sub", "(e)", "all rents, issues, profits, revenues, income and other sums arising from the Property, which are absolutely and presently assigned to Mortgagee under Article 5."),
 ]),
 dict(num="2.2", title="Fixtures and Building Systems", content=[
  ("p", "All materials, equipment, fixtures and building systems now or hereafter installed in, affixed to or used in connection with the Improvements (including the rooftop HVAC units, ductwork, controls, elevator cab, elevator controls and door operators, fire protection systems, the Vapor Barrier, the decorative iron balcony and all other goods that become fixtures) are hereby declared to be, and shall be deemed to be, part of the realty and fixtures, whether or not physically attached to the Improvements, and are included in the Real Property Collateral. Mortgagor shall not remove or permit the removal of any such item except for replacement with items of equal or greater value and utility that are free of liens and are immediately subject to the lien of this Mortgage."),
 ]),
 dict(num="2.3", title="Security Interest in Personal Property Collateral", content=[
  ("p", "This Mortgage constitutes a Security Agreement within the meaning of the Code. Mortgagor hereby grants to Mortgagee a continuing first-priority security interest in all of Mortgagor\u2019s right, title and interest in and to the following, whether now owned or hereafter acquired, and wherever located:"),
  ("sub", "(a)", "all equipment, machinery, apparatus, fittings, furniture, furnishings, trade fixtures, tools, supplies and other goods used in or relating to the ownership, operation, renovation, leasing or maintenance of the Property;"),
  ("sub", "(b)", "all accounts, chattel paper, instruments, deposit accounts (other than any account designated by Mortgagee as a Mortgagor operating account), letter-of-credit rights, payment intangibles and general intangibles, including all rights to payment of rent and all rights under the Leases;"),
  ("sub", "(c)", "all permits, licenses, franchises, approvals, entitlements, development rights, zoning rights, variances, certificates of occupancy and other governmental authorizations relating to the Property, to the extent the same may lawfully be assigned;"),
  ("sub", "(d)", "all contracts, subcontracts, purchase orders, warranties, guaranties, indemnities, suretyship agreements and claims relating to the construction, renovation, operation, maintenance or repair of the Property, including without limitation all of Mortgagor\u2019s right, title and interest in, to and under the Renovation Contract, the architect\u2019s agreement and all other construction-phase agreements, together with all rights to receive performance and to enforce all warranties and indemnities thereunder;"),
  ("sub", "(e)", "all Reserve Funds and all other deposits, escrows and reserve accounts established in connection with the Loan, whether held by Mortgagee or by any other Person for the benefit of Mortgagee;"),
  ("sub", "(f)", "all insurance proceeds (including unearned premiums and return premiums), condemnation awards and other payments arising from damage, destruction, condemnation or taking of the Property or any portion thereof;"),
  ("sub", "(g)", "all books, records, files, plans, specifications, as-built drawings, surveys, testing reports, environmental reports, the Phase I Environmental Site Assessment described in Section 3.7, and other documents relating to the Property, whether in tangible or electronic form;"),
  ("sub", "(h)", "all inventory, and all accessions, additions, replacements, substitutions and products of, and all proceeds (including insurance proceeds and tort claims proceeds) of, any of the foregoing; and"),
  ("sub", "(i)", "all rights of Mortgagor to receive any payment or performance under any of the foregoing."),
 ]),
 dict(num="2.4", title="Fixture Filing; Financing Statements", content=[
  ("p", "This Mortgage shall be effective as a fixture filing under the Code with respect to all goods that are or become fixtures on the Land. Mortgagor authorizes Mortgagee to file (a) this Mortgage, or a financing statement substantially describing this Mortgage, in the real estate records of the RMC Office as a fixture filing, and (b) a UCC-1 financing statement naming Mortgagor, as debtor (Debtor organizational identification no. 2024-0011287; federal employer identification no. 84-6213750), and Mortgagee, as secured party, covering the Personal Property Collateral, filed with the South Carolina Secretary of State. Mortgagor shall execute and deliver such financing statements, continuation statements, amendments and other instruments as Mortgagee may reasonably request to create, perfect, maintain or continue the perfection of Mortgagee\u2019s security interests, and shall pay all filing and search fees in connection therewith. Mortgagor shall not change its name, organizational identification number, jurisdiction of organization, organizational form or location of its chief executive office without at least thirty (30) days\u2019 prior written notice to Mortgagee and, if required, the filing of amendments."),
 ]),
 dict(num="2.5", title="Secured Obligations; Reservations", content=[
  ("p", "This Mortgage secures the payment and performance of the Indebtedness, including the Initial Advance, the Renovation Holdback, all future advances and obligatory advances made by Mortgagee under Article 9, and all obligations of Mortgagor under the Environmental Indemnity Agreement. The lien of this Mortgage shall secure all future advances as fully as if made on the date hereof, and Mortgagor intends that Mortgagee obtain such priority with respect to all future advances as is afforded under the laws of the State of South Carolina."),
  ("p", "Mortgagor expressly acknowledges that the Loan proceeds are advanced in multiple disbursements, that the Renovation Holdback is advanced in stages over approximately fourteen (14) months, and that Mortgagee\u2019s obligation to make each future advance is subject to the conditions in Article 9. The existence of any unpaid portion of the Renovation Holdback shall not diminish the amount of the Indebtedness secured hereby, which shall at all times include the entire committed amount of $14,750,000.00 to the extent afforded priority under Applicable Law and the Title Policy."),
 ]),
 dict(num="2.6", title="As-Extracted Collateral", content=[
  ("p", "Mortgagee and Mortgagor acknowledge that the Property is improved commercial real property and that no minerals, oil, gas or other as-extracted collateral (within the meaning of the Code) are currently produced or severed from the Land. Accordingly, Section 5.3 of the Term Sheet (which addresses as-extracted collateral on an \u201cif any\u201d basis) is inapplicable. If any as-extracted collateral is hereafter produced from the Land, it shall be deemed included in the Personal Property Collateral and Mortgagor shall execute such fixture filings as Mortgagee requires."),
 ]),
]))

# ============================================================ ARTICLE 3
ARTICLES.append(dict(num="3", title="Representations and Warranties", sections=[
 dict(num="3.1", title="Organization, Authority and Enforceability", content=[
  ("p", "Mortgagor represents and warrants that it is a limited liability company duly organized, validly existing and in good standing under the laws of the State of South Carolina, South Carolina Secretary of State Filing No. 2024-0011287, with federal employer identification number 84-6213750; that it has full power and authority to own, operate, renovate, lease and mortgage the Property and to execute, deliver and perform this Mortgage and the other Loan Documents; that the execution, delivery and performance of this Mortgage have been duly authorized by all necessary action of Mortgagor, its managing member and its members; that this Mortgage has been duly executed and delivered and constitutes the legal, valid and binding obligation of Mortgagor, enforceable in accordance with its terms; and that the persons executing this Mortgage on behalf of Mortgagor are duly authorized to do so."),
  ("p", "Mortgagor further represents that Graydon Development Group LLC, a South Carolina limited liability company, is the Managing Member of Mortgagor and holds a seventy-two percent (72%) membership interest; that Neil Ashford Graydon is the sole member and sole manager of Graydon Development Group LLC and is the individual executing this Mortgage on Mortgagor\u2019s behalf; and that no consent, approval or action of any other member of Mortgagor is required for the execution, delivery or performance of this Mortgage, other than any consent obtained prior to the Closing Date and delivered to Mortgagee."),
 ]),
 dict(num="3.2", title="No Conflicts; Consents", content=[
  ("p", "The execution, delivery and performance of this Mortgage do not and will not (a) violate Mortgagor\u2019s certificate of formation or operating agreement, (b) violate any Applicable Law, (c) result in a breach of or default under any indenture, agreement or instrument to which Mortgagor is a party (including the Renovation Contract and any Lease), or (d) result in the creation or imposition of any lien on the Property other than in favor of Mortgagee. Except for the recording of this Mortgage and the filing of the financing statements described in Section 2.4, no consent, approval, authorization, order or filing with any Governmental Authority or other Person is required."),
 ]),
 dict(num="3.3", title="Title", content=[
  ("p", "Mortgagor represents and warrants that it holds good and marketable fee simple title to the Land and the Improvements, free and clear of all liens, encumbrances, easements, restrictions, covenants, conditions, encroachments, claims and other matters except the Permitted Exceptions, and that this Mortgage constitutes a valid first-priority mortgage lien on and security interest in the Property, subject only to the Permitted Exceptions. Mortgagor has not previously mortgaged, pledged, assigned or otherwise encumbered the Property or any interest therein."),
  ("p", "Mortgagor acknowledges that title to Parcel One will vest in Mortgagor by General Warranty Deed from Hampstead Village Holdings LLC, a South Carolina limited liability company, and that Parcel Two (the vacated Anson Lane strip) was conveyed to Mortgagor\u2019s predecessor in title by quitclaim deed recorded in Deed Book 1128 at Page 443 in the RMC Office, which conveyance carries no warranties of title."),
 ]),
 dict(num="3.4", title="Anson Lane Parcel; Title Coverage", content=[
  ("p", "Mortgagor represents and warrants that the Title Policy, when issued, will insure fee simple title to both Parcel One and Parcel Two in Mortgagor, subject only to the Permitted Exceptions, and that no Permitted Exception, and no endorsement limitation or coverage qualification, will except, carve out, reduce or qualify the estate insured in Parcel Two below fee simple. Mortgagor further represents that the acquisition deed from Hampstead Village Holdings LLC conveys both Parcel One and Parcel Two to Mortgagor with general warranty, and that Mortgagor has received no notice of any claim, gap, adverse possession, prescriptive right, unrecorded conveyance or other defect affecting Parcel Two."),
  ("p", "Mortgagor acknowledges that Parcel Two provides rear access and loading to the Improvements and serves the rear parking area (approximately six (6) spaces) that the Leases permit the Tenants to use in common, and that the loss of, or any material impairment of title to or access across, Parcel Two would materially impair the value and operation of the Property. Mortgagor shall not convey, release, vacate, abandon, dedicate or otherwise dispose of any interest in Parcel Two, and shall not consent to any closure, vacation, obstruction or narrowing of the Anson Lane strip, without Mortgagee\u2019s prior written consent."),
 ]),
 dict(num="3.5", title="Leases; Rent Roll; Tenant Matters", content=[
  ("p", "Mortgagor represents and warrants that Exhibit D is a true, correct and complete rent roll and schedule of all Leases affecting the Property as of the Closing Date; that no Lease, sublease, license or occupancy agreement exists other than those listed in Exhibit D; that each Lease is in full force and effect and has not been amended, modified, renewed, extended or supplemented except as shown on Exhibit D; that no Tenant is more than thirty (30) days in arrears in the payment of rent; that no rent has been prepaid more than one (1) month in advance; that no Tenant has any option to purchase or right of first refusal to purchase the Property or any portion thereof; and that security deposits held by Mortgagor total $69,183.00 as itemized on Exhibit D."),
  ("p", "Mortgagor further represents that, as of the Closing Date, the Property contains 31,000 square feet of gross building area, of which 17,400 square feet is occupied and 13,600 square feet is vacant, resulting in an occupancy rate of approximately 56.13% by area (Bay 2, containing approximately 3,800 square feet, and 2nd Floor Suite B, containing approximately 9,800 square feet, being vacant), and that in-place annual base rent under the Leases is $415,100.00 before giving effect to the rent escalations that have occurred or will occur under the Leases. Mortgagor acknowledges that Mortgagee is relying on these figures and that any material inaccuracy constitutes a representation default under Section 10.1."),
  ("p", "Mortgagor discloses, and Mortgagee acknowledges, that (a) the Lease with Harmon & Wren Design Studio LLC, covering Bay 3, contains a right of first refusal in favor of that Tenant with respect to Bay 2, exercisable within fifteen (15) business days after presentation of a bona fide third-party offer, which right survives renewal of the Harmon & Wren Lease; (b) the Harmon & Wren Lease expires June 30, 2026, and contains a single three-year renewal option requiring notice by December 31, 2025; and (c) the Lease with Lowcountry Provisions Inc., covering Bay 1, contains no assignment, subletting, subordination, non-disturbance or estoppel provision, as described in Section 5.7."),
 ]),
 dict(num="3.6", title="Condition of Property; Compliance with Law; Zoning", content=[
  ("p", "Mortgagor represents and warrants that the Improvements are in good and safe condition and repair, ordinary wear and tear excepted, and are structurally sound; that the Property and its use comply in all material respects with all Applicable Laws, including zoning, building, fire, health, safety, accessibility and life-safety requirements; that the Property is zoned GB (General Business) under the zoning ordinances of the City of Charleston and that such zoning permits the current mixed-use retail and office use as a matter of right; that all required certificates of occupancy, permits and licenses for the current use are in effect; and that Mortgagor has received no notice of any violation, non-conforming use, unsafe condition or code enforcement action."),
  ("p", "Mortgagor further represents that the Property is located in FEMA Flood Zone X, a zone of minimal flood hazard, and that no federally mandated flood insurance is required for the Property. Mortgagor acknowledges that Mortgagee nonetheless requires flood insurance in the amount specified in Section 6.6(c)."),
 ]),
 dict(num="3.7", title="Environmental Matters; the CREC and the LUR", content=[
  ("p", "Mortgagor represents and warrants that, except as disclosed in the Phase I Environmental Site Assessment prepared by Clearfield Environmental Consulting LLC, Report No. CLR-2025-0119, dated January 28, 2025 (the \u201cPhase I ESA\u201d), and in the LUR: (a) no Hazardous Materials are located on, under, in, at or migrating from the Property in violation of any Environmental Law; (b) the Property is not subject to any pending or threatened investigation, remediation, notice of violation, consent order, administrative order or claim under any Environmental Law; (c) Mortgagor has not received any request for information or notice of potential liability under CERCLA or any state equivalent; and (d) there are no underground or above-ground storage tanks on the Property."),
  ("p", "Mortgagor specifically represents and warrants that it has received and reviewed the Phase I ESA and the LUR; that it understands that a Controlled Recognized Environmental Condition (CREC) exists at the southwest corner of Lot 7 arising from a historical release of perchloroethylene and petroleum-based solvents from the former dry cleaning operation at 518 King Street; that SCDHEC issued a No Further Action determination dated August 12, 2021 for SCDHEC Site ID SC-29403-0772; that the No Further Action determination is conditioned on continued compliance with the Institutional Controls; that the ground floor of Lot 7 (Bay 1) is currently used as a specialty grocery, a use consistent with the LUR\u2019s prohibition on residential use; and that the Vapor Barrier is, to Mortgagor\u2019s knowledge and based on the Phase I ESA and Mortgagor\u2019s investigation, intact and has not been penetrated, removed, damaged or compromised."),
  ("p", "Mortgagor acknowledges the recommendations of the Phase I ESA and the special instructions to closer contained in Title Commitment No. PT-2025-04-1178, including that the Environmental Indemnity Agreement and this Mortgage contain specific covenants addressing the LUR and the Vapor Barrier and that a failure to comply with, or any modification, termination or violation of, the LUR constitute a default."),
 ]),
 dict(num="3.8", title="Balcony Encroachment", content=[
  ("p", "Mortgagor discloses that a decorative iron balcony extends approximately two and one-half (2.5) feet beyond the front façade of the Improvements over and across the King Street public right-of-way, as shown on the ALTA Survey and as excepted in Exception 5 of Schedule B, Part II of Title Commitment No. PT-2025-04-1178. Mortgagor represents that, to its knowledge, the encroachment has existed since the original construction of the Improvements in 1952, that no Governmental Authority has asserted any claim or required any removal or modification, and that Mortgagor has delivered to Mortgagee true and complete copies of all permits, licenses, encroachment agreements, Board of Architectural Review approvals and City of Charleston correspondence relating to the balcony that are in Mortgagor\u2019s possession or control. Mortgagor makes no representation that a current encroachment license or permit is in effect, and Mortgagee\u2019s acceptance of this representation is conditioned on the deliveries required under Section 7.6."),
 ]),
 dict(num="3.9", title="Litigation; Solvency; No Bankruptcy", content=[
  ("p", "There is no action, suit, proceeding, arbitration, claim or investigation pending or, to Mortgagor\u2019s knowledge, threatened against Mortgagor or Guarantor that, if adversely determined, would materially and adversely affect the Property, Mortgagor\u2019s ability to perform under the Loan Documents, or Guarantor\u2019s ability to perform under the Guaranty. Mortgagor is solvent, is able to pay its debts as they become due, owns property having a fair saleable value greater than the amount required to pay its probable liabilities, and has no intent to hinder, delay or defraud any creditor. No bankruptcy, receivership, insolvency, reorganization, assignment for the benefit of creditors or similar proceeding is pending or contemplated by or against Mortgagor, any member of Mortgagor, or Guarantor."),
 ]),
 dict(num="3.10", title="Financial Statements; No Material Adverse Change", content=[
  ("p", "All financial statements, rent rolls, operating statements, budgets and other information furnished to Mortgagee by or on behalf of Mortgagor or Guarantor in connection with the Loan are true, correct and complete in all material respects as of their respective dates and have been prepared in accordance with GAAP (except that unaudited statements are subject to normal year-end adjustments and lack footnotes). There has been no material adverse change in the financial condition, business, assets, operations or prospects of Mortgagor or Guarantor since the dates of such information."),
 ]),
 dict(num="3.11", title="Renovation Contract, Budget and Permits", content=[
  ("p", "Mortgagor represents and warrants that it has delivered to Mortgagee a true, correct and complete copy of the executed Renovation Contract, including all schedules, exhibits and amendments, and of the plans and specifications for the renovation; that the Renovation Contract is in full force and effect, is not in default, and provides for a contract sum of $2,850,000.00 covering hard costs of construction; that the Renovation Budget of $3,150,000.00 includes $2,850,000.00 of hard costs within the Renovation Contract and $300,000.00 of soft costs and contingency outside the Renovation Contract; that a building permit and all Board of Architectural Review approvals necessary to perform the renovation have been or will be obtained before the applicable work commences; and that no mechanic\u2019s or materialman\u2019s lien has been filed against the Property."),
 ]),
 dict(num="3.12", title="OFAC; ERISA; Not a Foreign Person", content=[
  ("p", "Neither Mortgagor, Guarantor, nor any member or beneficial owner of Mortgagor is (a) a person named on the Specially Designated Nationals and Blocked Persons List maintained by the U.S. Department of the Treasury\u2019s Office of Foreign Assets Control, or otherwise a person with whom transactions are prohibited under any economic sanctions program administered by OFAC, or (b) a \u201cforeign person\u201d within the meaning of Section 1445 of the Internal Revenue Code. Mortgagor is not, and will not be, an employee benefit plan subject to Title I of ERISA or a plan subject to Section 4975 of the Internal Revenue Code."),
 ]),
]))

# ============================================================ ARTICLE 4
ARTICLES.append(dict(num="4", title="Payment Terms, Interest and Prepayment", sections=[
 dict(num="4.1", title="The Note; Principal Indebtedness", content=[
  ("p", "The Loan is evidenced by the Note in the original principal amount of $14,750,000.00. The Loan is disbursed in two components: (a) the Initial Advance of $12,500,000.00, made on the Closing Date and applied toward the purchase price of the Property, closing costs and funded reserves; and (b) the Renovation Holdback of $2,250,000.00, retained by Mortgagee and disbursed in accordance with Section 6.4 of the Term Sheet and Article 9 of this Mortgage. The outstanding principal balance of the Loan at any time is the sum of the Initial Advance plus all Renovation Holdback disbursements then outstanding."),
 ]),
 dict(num="4.2", title="Interest Rate; Daily SOFR; SOFR Floor", content=[
  ("p", "The outstanding principal balance of the Loan bears interest at a floating rate per annum equal to Daily SOFR plus two hundred eighty-five (285) basis points (2.85%), subject to a SOFR floor such that in no event shall the rate of interest be less than five and 85/100 percent (5.85%) per annum (being the sum of a 3.00% SOFR floor and the 2.85% spread)."),
  ("p", "Daily SOFR shall be determined by Mortgagee for each day on which interest accrues, in accordance with the definition of \u201cDaily SOFR,\u201d and interest shall be computed on the basis of the actual number of days elapsed over a year of three hundred sixty (360) days. Mortgagee\u2019s determination of Daily SOFR and of the Note Rate shall be conclusive and binding on Mortgagor absent manifest error. Mortgagee shall provide Mortgagor, upon request, with evidence of the published Daily SOFR relied upon."),
  ("p", "If Mortgagee determines that (a) Daily SOFR has been permanently or indefinitely discontinued or is no longer representative, (b) the administrator of Daily SOFR is insolvent or has ceased publication, or (c) any Governmental Authority has determined that Daily SOFR is no longer permitted as a benchmark for new loans, then Mortgagee may, in consultation with Mortgagor, designate a successor benchmark rate conforming to then-prevailing market conventions (including any applicable recommended fallback under the Adjustable Interest Rate (LIBOR) Act, 12 U.S.C. \u00a7 5801 et seq., and related regulations, to the extent applicable), together with an applicable spread adjustment intended to make the successor rate economically comparable to Daily SOFR, and may make conforming changes to the timing and mechanics of interest determination, in each case in Mortgagee\u2019s reasonable discretion and without reducing the yield of the Note below the SOFR Floor. The SOFR Floor shall continue to apply to any successor benchmark."),
 ]),
 dict(num="4.3", title="Payment Dates; Amortization; Maturity", content=[
  ("p", "Accrued interest on the outstanding principal balance is payable monthly, in arrears, on the fifteenth (15th) day of each calendar month, commencing May 15, 2025 (each a \u201cPayment Date\u201d)."),
  ("p", "During the period commencing on the Closing Date and ending on April 15, 2027 (the \u201cInterest-Only Period\u201d), each monthly payment shall consist solely of accrued and unpaid interest on the outstanding principal balance, with no principal amortization. The Interest-Only Period comprises the first twenty-four (24) monthly installments of the Loan, commencing with the Payment Date occurring May 15, 2025 and ending with the Payment Date occurring April 15, 2027."),
  ("p", "Commencing with the Payment Date occurring May 15, 2027, and continuing on each Payment Date thereafter through and including the Maturity Date, monthly installments of principal and interest shall be payable in amounts calculated to fully amortize the then-outstanding principal balance over a twenty-five (25) year amortization schedule at the then-applicable Note Rate. Because the amortization period exceeds the remaining term of the Loan, a substantial balloon payment of principal will be due on the Maturity Date."),
  ("p", "The entire outstanding principal balance, together with all accrued and unpaid interest, the Yield Maintenance Premium (if any), late charges and all other amounts due under the Loan Documents, shall be due and payable in full on the Maturity Date, being April 15, 2030."),
 ]),
 dict(num="4.4", title="Manner of Payment; Application", content=[
  ("p", "All payments shall be made in lawful money of the United States, in immediately available funds, to Mortgagee at the address specified in Section 13.4 or by wire transfer to an account designated by Mortgagee in writing, without setoff, counterclaim, deduction or withholding. All payments received after 2:00 p.m. Eastern time on a Business Day shall be deemed received on the next Business Day. Mortgagor shall not assert any right of setoff against the Reserve Funds."),
  ("p", "Mortgagee shall apply payments in the following order: first, to reimburse Mortgagee for any protective advances, costs, expenses and attorneys\u2019 fees incurred under the Loan Documents; second, to late charges then due; third, to accrued and unpaid interest at the Note Rate and then at the Default Rate; fourth, to principal; and fifth, to any other amounts due. Mortgagee may apply any payment to the earliest matured unpaid installment notwithstanding Mortgagor\u2019s instructions, unless Mortgagee agrees otherwise in writing."),
 ]),
 dict(num="4.5", title="Default Rate", content=[
  ("p", "Upon the occurrence and during the continuance of an Event of Default, the outstanding principal balance of the Loan and, to the extent permitted by Applicable Law, all other amounts due under the Loan Documents, shall bear interest at the Default Rate, being the Note Rate plus five percent (5.00%) per annum. Interest at the Default Rate shall accrue from the date of the Event of Default until the earlier of the date the Event of Default is cured or the date all Indebtedness is paid in full, and shall be payable on demand."),
 ]),
 dict(num="4.6", title="Late Charge", content=[
  ("p", "If any installment of principal and/or interest or any other amount due under the Loan Documents is not received by Mortgagee within ten (10) calendar days after the applicable due date, Mortgagor shall pay to Mortgagee a late charge equal to five percent (5.00%) of the overdue installment or amount. The late charge is intended to compensate Mortgagee for the additional administrative expense occasioned by late payment, is not a penalty, and is in addition to interest at the Default Rate and all other remedies."),
 ]),
 dict(num="4.7", title="Prepayment", content=[
  ("p", "The Loan may be prepaid only as expressly permitted in this Section 4.7. Any prepayment of principal other than in compliance with this Section 4.7 shall constitute an Event of Default and shall also entitle Mortgagee to the Yield Maintenance Premium or the premium described in Section 4.7(a), as applicable."),
  ("sub", "(a)", "Lockout Period. The Loan may not be prepaid, in whole or in part, at any time during the Lockout Period (months 1 through 24 following the Closing Date, through April 15, 2027). Mortgagor shall not tender, and Mortgagee shall not be obligated to accept, any voluntary prepayment during the Lockout Period. If, notwithstanding the foregoing, Mortgagee in its sole discretion accepts any prepayment of principal during the Lockout Period, Mortgagor shall pay, in addition to all other amounts due, a prepayment premium equal to the greater of (i) one percent (1.00%) of the principal amount prepaid, and (ii) the Yield Maintenance Premium calculated as if the prepayment had occurred on the last day of the Yield Maintenance Period, it being the intention of the parties that no prepayment of the Loan occur before the expiration of the Lockout Period without compensating Mortgagee for the loss of its bargained-for yield."),
  ("sub", "(b)", "Yield Maintenance Period. From the expiration of the Lockout Period through the last day of the Yield Maintenance Period (months 25 through 48 following the Closing Date, through April 15, 2029), Mortgagor may prepay the Loan in whole, but not in part, upon not less than thirty (30) days\u2019 prior written notice to Mortgagee, which notice shall be irrevocable, and upon payment in full of the Indebtedness, including a yield maintenance premium (the \u201cYield Maintenance Premium\u201d) equal to the greater of:"),
  ("sub2", "(i)", "one percent (1.00%) of the outstanding principal balance of the Loan as of the date of prepayment; or"),
  ("sub2", "(ii)", "the present value of the excess, if any, of (A) the aggregate amount of interest that would have accrued on the principal amount prepaid at the Note Rate in effect on the date of prepayment for the period from the date of prepayment through the last day of the Yield Maintenance Period, over (B) the aggregate amount of interest that would accrue on such principal amount for the same period at a rate per annum equal to the Treasury Rate plus fifty (50) basis points (0.50%), which excess, if any, shall be discounted to present value at the Treasury Rate on a monthly basis."),
  ("p", "For purposes of this Section 4.7(b), the \u201cTreasury Rate\u201d means the yield to maturity, determined as of the second (2nd) Business Day preceding the date of prepayment, of the United States Treasury security having a maturity date closest to, but not exceeding, the last day of the Yield Maintenance Period, as reported in Federal Reserve Statistical Release H.15 \u2014 Selected Interest Rates (or any successor publication). If no published maturity exactly matches, the Treasury Rate shall be determined by linear interpolation between the yields of the two (2) United States Treasury securities having maturities nearest to, but above and below, the last day of the Yield Maintenance Period. If the Treasury Rate is not published for any reason, Mortgagee shall determine the Treasury Rate in a commercially reasonable manner from a comparable published source, and its determination shall be conclusive absent manifest error. Any calculation of the Yield Maintenance Premium by Mortgagee shall be conclusive and binding on Mortgagor absent manifest error, and Mortgagor shall be entitled upon request to receive Mortgagee\u2019s calculation worksheet."),
  ("sub", "(c)", "Open Prepayment Period. During the Open Prepayment Period (months 49 through 60 following the Closing Date, through the Maturity Date), Mortgagor may prepay the Loan in whole or in part, at any time and from time to time, without payment of any prepayment premium, penalty, make-whole amount or yield maintenance amount, upon not less than fifteen (15) days\u2019 prior written notice to Mortgagee. Any partial prepayment shall be applied to the installments of principal last due and shall not relieve Mortgagor of the obligation to make any scheduled installment thereafter."),
  ("sub", "(d)", "Involuntary Prepayments. Mortgagee shall apply casualty insurance proceeds or condemnation awards to the Indebtedness without premium, penalty or Yield Maintenance Premium when such application is required or permitted under Section 6.7. No prepayment premium, penalty or Yield Maintenance Premium shall be payable in connection with (i) any application of insurance proceeds or condemnation awards to the Indebtedness under Section 6.7, (ii) any payment of the Indebtedness following acceleration after an Event of Default, or (iii) any payment made from Reserve Funds to the extent Mortgagee applies such funds to the Indebtedness under this Mortgage."),
  ("sub", "(e)", "No Reamortization; No Reinstatement. No partial prepayment shall entitle Mortgagor to any reduction in, or reamortization of, the monthly installments of principal and interest, except as Mortgagee may expressly agree in writing."),
 ]),
 dict(num="4.8", title="Usury Savings", content=[
  ("p", "Notwithstanding anything to the contrary, no provision of this Mortgage or any other Loan Document shall require Mortgagor to pay, or permit Mortgagee to collect, interest or other charges in excess of the maximum amount permitted by Applicable Law. If any amount in excess of that maximum is provided for or received, the excess shall be deemed a mistake and shall be cancelled automatically, and any amount actually received in excess shall be credited against principal (or refunded if principal has been paid in full). To the extent permitted by Applicable Law, all amounts that constitute interest shall be amortized, prorated, allocated and spread over the full period of the Loan to determine the effective rate of interest."),
 ]),
]))

# ============================================================ ARTICLE 5
ARTICLES.append(dict(num="5", title="Absolute Assignment of Leases, Rents and Profits", sections=[
 dict(num="5.1", title="Absolute and Present Assignment", content=[
  ("p", "Mortgagor hereby unconditionally, absolutely and presently grants, transfers and assigns to Mortgagee all of Mortgagor\u2019s right, title and interest, whether now existing or hereafter arising, in, to and under (a) all present and future Leases and other agreements demising, licensing or otherwise conferring a right to occupy any portion of the Property, and (b) all rents, issues, profits, revenues, income, base rent, additional rent, percentage rent, expense reimbursements, tax and insurance reimbursements, parking income, income from licenses and concessions, and all other sums now or hereafter payable under or in connection with the Leases or the use or occupancy of the Property (collectively, the \u201cRents\u201d), without reservation and without any requirement that Mortgagee first resort to the Property or to any other security."),
  ("p", "This assignment is an absolute assignment of rents and not a collateral assignment, and is intended to constitute an \u201cassignment of rents\u201d within the meaning of the South Carolina Uniform Assignment of Rents Act, S.C. Code Ann. \u00a7 29-3-100 et seq. (the \u201cAssignment of Rents Act\u201d). Mortgagor acknowledges that, under the Assignment of Rents Act, this absolute assignment is effective upon execution and recording in the RMC Office, and that Mortgagee\u2019s right to collect the Rents is enforceable upon an Event of Default and the giving of notice to the Tenants in accordance with Section 5.3, without the necessity of foreclosure, appointment of a receiver, or any other action."),
  ("p", "Mortgagor shall, upon Mortgagee\u2019s request, execute and deliver such further assignments, notices, tenant letters, direction letters and confirmations as Mortgagee may reasonably require to give effect to this Article 5, and shall not execute any document that purports to assign, pledge or encumber the Rents in favor of any other Person."),
 ]),
 dict(num="5.2", title="Revocable License to Collect Rents", content=[
  ("p", "So long as no Event of Default has occurred and is continuing, Mortgagor is granted a revocable license to collect and apply the Rents in the ordinary course of business, subject to the terms of the Leases, this Mortgage and the Loan Documents. The license is revoked automatically upon the occurrence of an Event of Default, without notice or further action by Mortgagee, and may also be revoked by Mortgagee upon the occurrence of any event that, with notice or lapse of time or both, would constitute an Event of Default. Upon revocation, Mortgagor shall hold all Rents collected in trust for Mortgagee, shall not commingle them with other funds, and shall deliver them to Mortgagee within three (3) Business Days of receipt."),
  ("p", "The license granted in this Section 5.2 is not a waiver of the absolute assignment in Section 5.1, does not subordinate the assignment to any Lease, and does not limit Mortgagee\u2019s rights under the Assignment of Rents Act."),
 ]),
 dict(num="5.3", title="Enforcement; Notice to Tenants", content=[
  ("p", "Upon the occurrence and during the continuance of an Event of Default, Mortgagee may, without any requirement of court order, appointment of a receiver, or prior foreclosure, give written notice to each Tenant directing that all Rents thereafter be paid directly to Mortgagee or to a depository designated by Mortgagee, and each Tenant shall thereafter pay the Rents directly to Mortgagee until further written notice. Mortgagor irrevocably authorizes and directs each Tenant to rely on and comply with any such notice from Mortgagee, and Mortgagor shall have no claim against any Tenant for payments made in compliance with such notice."),
  ("p", "Mortgagor hereby irrevocably appoints Mortgagee as its attorney-in-fact, coupled with an interest, solely for the purposes of (a) executing and delivering notices to Tenants under this Section 5.3, (b) endorsing and depositing Rents checks payable to Mortgagor, and (c) taking such ministerial action as is necessary to collect the Rents following an Event of Default. This power of attorney is granted in addition to, and not in limitation of, Mortgagee\u2019s rights under the Assignment of Rents Act, and is not a power of sale."),
  ("p", "Mortgagee may, in addition, apply ex parte or otherwise to a court of competent jurisdiction in Charleston County, South Carolina, for the appointment of a receiver of the Property and the Rents in accordance with Section 11.3."),
 ]),
 dict(num="5.4", title="No Liability of Mortgagee; Mortgagor Remains Obligated", content=[
  ("p", "Mortgagee\u2019s acceptance of this assignment, and any collection of Rents by Mortgagee, shall not constitute an assumption by Mortgagee of any obligation under any Lease or otherwise, and Mortgagee shall not be liable for the performance of any covenant or condition of any Lease, for any tenant improvement obligation, for the return of any security deposit not actually received by Mortgagee, or for any act or omission of Mortgagor as landlord. Mortgagor shall remain fully liable for all landlord obligations under the Leases, including maintenance, repair, restoration, indemnification and tenant improvement obligations, and shall indemnify Mortgagee against all claims arising from any failure to perform them."),
 ]),
 dict(num="5.5", title="Leasing Covenants; Consent Thresholds", content=[
  ("p", "Mortgagor shall use commercially reasonable efforts to lease all vacant space at the Property at market rents and on terms consistent with those prevailing for comparable mixed-use commercial properties in the Charleston, South Carolina metropolitan area, on terms reasonably acceptable to Mortgagee, and in compliance with Applicable Law and the LUR."),
  ("p", "Mortgagor shall not, without Mortgagee\u2019s prior written consent (which shall not be unreasonably withheld, conditioned or delayed): (a) enter into any new Lease covering more than five thousand (5,000) square feet, or having a term (including renewal options exercisable at the Tenant\u2019s election) exceeding five (5) years; (b) amend, modify, terminate, accept a surrender of, or waive any material right under any Lease covering more than five thousand (5,000) square feet or having a remaining term exceeding five (5) years; (c) accept any rent prepayment exceeding one (1) month; (d) grant any option to purchase, right of first refusal to purchase, or any interest in the Property to any Tenant; or (e) release or reduce any Tenant security deposit."),
  ("p", "Every Lease entered into after the Closing Date shall (i) be subordinate to this Mortgage or, at Mortgagee\u2019s election, require the Tenant to execute a commercially reasonable subordination, non-disturbance and attornment agreement in Mortgagee\u2019s standard form; (ii) require the Tenant to deliver estoppel certificates within ten (10) Business Days of request; and (iii) contain a prohibition on the storage, use, generation or release of Hazardous Materials other than customary office and cleaning supplies."),
  ("p", "Mortgagor shall comply with the right of first refusal held by Harmon & Wren Design Studio LLC with respect to Bay 2, and shall not enter into any lease of, or letter of intent or other agreement to lease, Bay 2 without first presenting each bona fide third-party offer to that Tenant in accordance with its Lease and allowing the full fifteen (15) business day response period. Mortgagor shall promptly deliver to Mortgagee copies of all offers, notices and responses relating to the exercise or waiver of that right of first refusal."),
  ("p", "Mortgagor shall ensure that no Lease of the ground floor of Lot 7 (Bay 1) permits residential use, and that every such Lease expressly prohibits residential use in compliance with the LUR."),
 ]),
 dict(num="5.6", title="Security Deposits", content=[
  ("p", "Mortgagor represents that it holds tenant security deposits totaling $69,183.00, as itemized on Exhibit D. Mortgagor shall hold all security deposits in a segregated account in trust for the Tenants in accordance with Applicable Law, shall not apply any security deposit to any obligation of Mortgagor other than in accordance with the applicable Lease, and hereby grants to Mortgagee a security interest in all security deposits and the deposit account in which they are held. Upon an Event of Default, Mortgagor shall, upon Mortgagee\u2019s request, transfer all security deposits to Mortgagee or a depository designated by Mortgagee, to be held and applied in accordance with the Leases and Applicable Law."),
 ]),
 dict(num="5.7", title="Lowcountry Provisions Lease; Estoppel and Assignment Consent", content=[
  ("p", "Mortgagor represents and warrants that it has the full right, power and authority to assign to Mortgagee all Rents under all Leases affecting the Property, including specifically and without limitation the Lease with Lowcountry Provisions Inc. covering Bay 1, and that no Lease contains any provision that prohibits, restricts or conditions the assignment of Rents to Mortgagee or the payment of Rents to Mortgagee upon notice. Mortgagor acknowledges that the Lowcountry Provisions Lease is silent as to assignment and subletting and contains no consent requirement, prohibition, subordination, non-disturbance or estoppel provision."),
  ("p", "As a condition to the Initial Advance, Mortgagor shall deliver (a) an estoppel certificate from Lowcountry Provisions Inc., dated not more than thirty (30) days prior to the Closing Date, acknowledging the existence of this Mortgage and the absolute assignment of Rents, confirming the terms of its Lease and the status of rent and security deposits, and agreeing to pay Rents to Mortgagee upon written notice following an Event of Default; and (b) a subordination, non-disturbance and attornment agreement from Lowcountry Provisions Inc. in form satisfactory to Mortgagee. Because the Lowcountry Provisions Lease does not obligate the Tenant to provide such instruments, Mortgagor shall use its best efforts to obtain them and shall not be relieved of the condition except as Mortgagee may expressly waive in writing."),
  ("p", "Post-Closing Covenant. Mortgagor shall use commercially reasonable efforts to obtain, at the first renewal, extension or amendment of the Lowcountry Provisions Lease (or earlier if the Tenant agrees), an amendment adding a customary assignment and subletting consent provision, a subordination and non-disturbance provision and an estoppel obligation, in form reasonably acceptable to Mortgagee. Mortgagor shall deliver a copy of any such amendment to Mortgagee within ten (10) Business Days of execution."),
 ]),
 dict(num="5.8", title="Subordination, Non-Disturbance and Attornment", content=[
  ("p", "Mortgagor shall deliver to Mortgagee, as a condition to the Initial Advance, executed subordination, non-disturbance and attornment agreements from each Tenant then in occupancy (Lowcountry Provisions Inc., Harmon & Wren Design Studio LLC and Tidemark Consulting Group LLC), in form and substance satisfactory to Mortgagee, pursuant to which each Tenant subordinates its Lease to this Mortgage (to the extent the Lease is not already subordinate), and Mortgagee agrees not to disturb the Tenant\u2019s possession so long as the Tenant is not in default beyond applicable cure periods and attorns to Mortgagee or any purchaser at foreclosure."),
 ]),
]))

# ============================================================ ARTICLE 6
ARTICLES.append(dict(num="6", title="Taxes, Insurance and Reserves", sections=[
 dict(num="6.1", title="Taxes and Assessments", content=[
  ("p", "Mortgagor shall pay, before the same become delinquent and before any penalty or interest attaches, all real property taxes, assessments, water and sewer charges, utility charges and other governmental impositions levied against the Property or any part thereof, including all such amounts for Charleston County Tax Map Nos. 460-12-04-007, 460-12-04-008 and 460-12-04-009. Mortgagor shall deliver to Mortgagee receipts or other evidence of payment within thirty (30) days after payment and, in any event, upon Mortgagee\u2019s request."),
  ("p", "Mortgagor may contest in good faith any tax or assessment by appropriate proceedings, provided that (a) Mortgagor gives Mortgagee prior written notice, (b) Mortgagor deposits with Mortgagee such security as Mortgagee reasonably requires to prevent any sale, lien or forfeiture, (c) no lien attaches to the Property that is not bonded over, and (d) the contest does not impair the lien of this Mortgage or the Title Policy."),
  ("p", "Mortgagor acknowledges that the Property may be reassessed by Charleston County following the acquisition and renovation, and that the Tax and Insurance Escrow may require adjustment under Section 6.2. Mortgagor shall notify Mortgagee within ten (10) Business Days of receiving any notice of reassessment or valuation change."),
 ]),
 dict(num="6.2", title="Tax and Insurance Escrow", content=[
  ("p", "Mortgagor shall deposit with Mortgagee, on each Payment Date, an amount equal to one-twelfth (1/12) of the estimated annual real property taxes and casualty and liability insurance premiums for the Property, covering all three (3) tax parcels. Mortgagee shall hold such deposits in escrow and apply them to pay real property taxes and insurance premiums as they become due. Mortgagee may adjust the monthly escrow amount from time to time based on actual or anticipated tax assessments and insurance premiums, and Mortgagor shall pay any resulting deficiency within thirty (30) days of demand. Mortgagor shall have no right to direct the investment or application of escrow funds, and any interest earned shall be credited to the escrow account."),
  ("p", "If Mortgagor fails to maintain the required escrow balance, Mortgagee may, at its option, advance funds to pay taxes or premiums when due, and any such advance shall constitute a protective advance secured by this Mortgage, bearing interest at the Default Rate."),
 ]),
 dict(num="6.3", title="Capital Replacement Reserve", content=[
  ("p", "Mortgagor shall deposit with Mortgagee, on each Payment Date, the sum of Six Hundred Forty-Five Dollars and Eighty-Three Cents ($645.83), calculated as $0.25 per square foot per year multiplied by 31,000 square feet of gross building area ($7,750.00 per year), divided by twelve (12) months. Funds in the Capital Replacement Reserve shall be disbursed to Mortgagor upon Mortgagee\u2019s approval of qualifying capital expenditures (being replacements of or major repairs to building systems and structural components not funded from the Renovation Holdback), subject to Mortgagee\u2019s reasonable review and approval procedures, including a written request describing the work, a contract or invoice, and evidence of completion and lien-free payment."),
 ]),
 dict(num="6.4", title="Tenant Improvement and Leasing Commission Reserve", content=[
  ("p", "Mortgagor shall deposit at closing the sum of One Hundred Fifty Thousand Dollars ($150,000.00) into a tenant improvement and leasing commission reserve account held by Mortgagee. Disbursements shall be subject to Mortgagee\u2019s prior written approval and shall be used exclusively for tenant improvement costs and leasing commissions incurred in connection with the leasing of vacant space at the Property (other than costs funded from the Tenant Improvement Allowances line item of the Renovation Budget). Upon any drawdown, Mortgagor shall replenish the reserve to the full amount of $150,000.00 from Mortgagor\u2019s own funds within thirty (30) days of Mortgagee\u2019s written demand."),
  ("p", "Mortgagor acknowledges that the Tenant Improvement and Leasing Commission Reserve is a separate reserve and is not part of the Renovation Budget, and that the Tenant Improvement Allowances line item of the Renovation Budget ($550,000.00) and this reserve ($150,000.00) are distinct funding sources."),
 ]),
 dict(num="6.5", title="Reserve Funds Generally", content=[
  ("p", "As additional security for the Indebtedness, Mortgagor hereby grants to Mortgagee a first-priority security interest in, and pledges and assigns to Mortgagee, all Reserve Funds and all accounts in which they are held, together with all interest and earnings thereon. The Reserve Funds are pledged to Mortgagee as collateral and are not trust funds for the benefit of Mortgagor. Upon an Event of Default, Mortgagee may apply any or all Reserve Funds to the Indebtedness in such order as Mortgagee determines, and Mortgagor shall have no right to require their application to taxes, insurance, capital expenditures or leasing costs. Mortgagee shall not be obligated to pay interest to Mortgagor on the Reserve Funds except as expressly provided in this Mortgage or applicable law."),
 ]),
 dict(num="6.6", title="Insurance", content=[
  ("p", "Mortgagor shall maintain, at its sole cost and expense, the following insurance, with insurers licensed to do business in the State of South Carolina having an A.M. Best financial strength rating of not less than A- and a financial size category of not less than VII, and containing a provision requiring not less than thirty (30) days\u2019 prior written notice to Mortgagee of cancellation, non-renewal or material modification (ten (10) days\u2019 notice for non-payment of premium):"),
  ("sub", "(a)", "All-Risk Property Insurance. Comprehensive all-risk (special form) property insurance covering the Improvements and the Personal Property Collateral, on a replacement cost basis, with an agreed amount endorsement (waiver of coinsurance), with deductibles reasonably acceptable to Mortgagee, naming Mortgagee as mortgagee and loss payee pursuant to a standard mortgagee clause. Coverage shall include fire, windstorm, hail, explosion, vandalism, malicious mischief, sprinkler leakage and such other perils as Mortgagee may reasonably require."),
  ("sub", "(b)", "Commercial General Liability. Commercial general liability insurance with limits of not less than $2,000,000 per occurrence and $5,000,000 in the aggregate, naming Mortgagee as an additional insured, and including coverage for premises liability, operations liability, products and completed operations, and personal and advertising injury."),
  ("sub", "(c)", "Flood Insurance. Flood insurance on the Property in an amount not less than $5,000,000.00, naming Mortgagee as mortgagee and loss payee. Mortgagor acknowledges that the Property is located in FEMA Flood Zone X, that flood insurance may not be required by federal regulation for property in Zone X, and that Mortgagee nonetheless requires flood coverage in the stated amount as a condition of the Loan."),
  ("sub", "(d)", "Builder\u2019s Risk. During the period from the Closing Date through Substantial Completion, builder\u2019s risk insurance (on a completed value, non-reporting form) in an amount not less than the full Renovation Budget of $3,150,000.00, covering the Property and the renovation work against all risks of physical loss or damage, naming Mortgagee as mortgagee and loss payee, and including soft-cost and expediting expense coverage."),
  ("sub", "(e)", "Workers\u2019 Compensation and Employer\u2019s Liability. Workers\u2019 compensation insurance in the amounts required by the laws of the State of South Carolina, covering all employees of Mortgagor and, to the extent not covered by the Contractor\u2019s policies, all persons engaged in the renovation."),
  ("sub", "(f)", "Umbrella and Excess Liability. Umbrella or excess liability insurance in an amount not less than $5,000,000.00, providing excess coverage over the commercial general liability, automobile liability and employer\u2019s liability policies."),
  ("p", "Mortgagor shall deliver certificates of insurance and, upon request, certified copies of policies, prior to the Closing Date and thereafter not less than ten (10) days before each policy expiration. Mortgagor shall not cancel, permit to lapse, or materially modify any required policy without Mortgagee\u2019s prior written consent. Mortgagee may procure any required insurance that Mortgagor fails to maintain, and the cost shall be a protective advance secured by this Mortgage."),
 ]),
 dict(num="6.7", title="Casualty; Condemnation; Application of Proceeds", content=[
  ("p", "Mortgagor shall give Mortgagee prompt written notice of any material damage to or destruction of the Property and of any actual or threatened Condemnation. Mortgagee shall be entitled to receive and hold all insurance proceeds and condemnation awards, and Mortgagor irrevocably assigns such proceeds and awards to Mortgagee. Mortgagor shall not settle or compromise any claim for proceeds or any Condemnation in excess of $250,000.00 without Mortgagee\u2019s prior written consent."),
  ("p", "Mortgagee shall make the net proceeds or awards available to Mortgagor for restoration or repair if, in Mortgagee\u2019s reasonable judgment, each of the following conditions is satisfied: (a) no Event of Default has occurred and is continuing; (b) the Improvements can be restored to a condition and value at least equal to that existing before the casualty or taking, in compliance with Applicable Law and the LUR; (c) the net proceeds plus any additional amounts committed by Mortgagor are sufficient to complete restoration and pay all costs, including architectural, legal and leasing costs; (d) restoration will be completed within a reasonable period and in any event before the Maturity Date; and (e) the Property will continue to be used for a purpose permitted by Applicable Law and the LUR. If Mortgagee does not elect (or is not required) to make the proceeds available for restoration, Mortgagee may apply the proceeds or awards to the Indebtedness, without premium, penalty or Yield Maintenance Premium, in the order set forth in Section 4.4."),
  ("p", "Any surplus proceeds or awards remaining after payment in full of the Indebtedness shall be paid to Mortgagor or as otherwise required by Applicable Law."),
 ]),
]))

# ============================================================ ARTICLE 7
ARTICLES.append(dict(num="7", title="Affirmative Covenants", sections=[
 dict(num="7.1", title="Maintenance and Repair; No Waste", content=[
  ("p", "Mortgagor shall keep and maintain the Property, including all Improvements, fixtures, building systems, the Vapor Barrier, parking areas and common areas, in good order, condition and repair, and in a condition consistent with the standards of comparable mixed-use commercial properties in the Charleston, South Carolina metropolitan area. Mortgagor shall promptly make all repairs and replacements necessary to preserve the value, rentability and insurability of the Property; shall not commit or permit any waste of the Property or any portion thereof; and shall not remove, demolish or materially alter any Improvement except as expressly permitted under Section 9.2 in connection with the renovation."),
  ("p", "Mortgagor shall maintain and keep in effect the SCE&G utility easement area and all other appurtenant rights free of obstruction, and shall maintain the improvements, drainage and access serving the Property, including rear access and loading across the Anson Lane strip described in Section 3.4."),
 ]),
 dict(num="7.2", title="Compliance with Applicable Law", content=[
  ("p", "Mortgagor shall at all times comply in all material respects with all Applicable Laws applicable to the Property and to the conduct of its business, including all zoning, building, fire, health, safety, accessibility, life-safety, historic-preservation and Environmental Laws, and all conditions of any permit, license, certificate of occupancy or Board of Architectural Review approval. Mortgagor shall promptly cure any violation and shall deliver to Mortgagee copies of any notice of violation, citation or order within five (5) Business Days of receipt."),
 ]),
 dict(num="7.3", title="Environmental Covenants", content=[
  ("p", "Mortgagor shall: (a) comply with all Environmental Laws and with all Institutional Controls; (b) not cause or permit any Hazardous Materials to be stored, used, generated, released, discharged or disposed of on, under or from the Property, except customary office, cleaning and maintenance supplies in de minimis quantities and in compliance with Applicable Law; (c) not install any underground or above-ground storage tank on the Property; (d) promptly notify Mortgagee of any release, threatened release, notice of violation, information request, claim or regulatory inquiry relating to Hazardous Materials at the Property; (e) at its sole cost, promptly remediate any Hazardous Materials condition for which it is responsible and that is required to be remediated under Environmental Laws; (f) permit Mortgagee and its consultants to enter and inspect the Property and to conduct such testing as Mortgagee reasonably deems necessary following an Event of Default or a reasonable basis to believe a release has occurred; (g) not permit any lien to attach to the Property under any Environmental Law without promptly discharging or bonding over the same; and (h) deliver to Mortgagee copies of all SCDHEC correspondence, reports and submissions within five (5) Business Days of receipt or transmittal."),
  ("p", "Mortgagor shall not take any action, and shall not permit any Tenant or Contractor to take any action, that would cause the Property to lose the benefit of the No Further Action determination for SCDHEC Site ID SC-29403-0772 or that would cause SCDHEC to reopen that site file."),
 ]),
 dict(num="7.4", title="Institutional Controls; LUR and Vapor Barrier Compliance", content=[
  ("p", "Without limiting Section 7.3, and in order to give effect to Exception 4 of Schedule B, Part II of the Title Commitment, the instructions to closer contained in that Title Commitment, the recommendations in Section 6 of the Phase I ESA, and Requirement 6 of the Title Commitment, Mortgagor covenants as follows:"),
  ("sub", "(a)", "Prohibited Use. Mortgagor shall not convert, permit, suffer or allow the ground floor of Lot 7 (Charleston County Tax Map No. 460-12-04-007, Bay 1, 520 King Street) to be used for any residential purpose, and shall not permit any occupancy of that space that would violate the LUR. Mortgagor shall not seek or consent to any amendment, modification, variance, or termination of the LUR without Mortgagee\u2019s prior written consent in each instance and without SCDHEC\u2019s prior written approval."),
  ("sub", "(b)", "Vapor Barrier Maintenance. Mortgagor shall maintain the Vapor Barrier in good condition and working order, shall not penetrate, remove, breach, cover over, impair or otherwise compromise the Vapor Barrier, and shall promptly repair or replace any portion of the Vapor Barrier that is damaged, degraded or compromised, in each case in accordance with the LUR and any SCDHEC-approved plan."),
  ("sub", "(c)", "Periodic Inspection. Mortgagor shall cause the Vapor Barrier to be inspected not less frequently than annually (and at such other intervals as the LUR or SCDHEC may require) by a qualified environmental professional licensed in the State of South Carolina, shall deliver a written inspection report to Mortgagee within thirty (30) days after each inspection, and shall deliver a compliance certificate with each report certifying that the Vapor Barrier is intact and that the Property is in compliance with the Institutional Controls."),
  ("sub", "(d)", "Pre-Construction Notification. Before commencing any renovation, construction, demolition, alteration or repair work that penetrates, or is likely to disturb, the floor slab of Bay 1 on Lot 7, including any work under the Renovation Budget affecting that slab, Mortgagor shall (i) notify SCDHEC in writing and obtain any required SCDHEC approval, (ii) cause a qualified environmental professional to inspect the Vapor Barrier before and after the work, (iii) instruct the Contractor in writing regarding the existence, location and protection requirements of the Vapor Barrier, and (iv) deliver copies of all such notices, approvals, instructions and inspection reports to Mortgagee not less than ten (10) Business Days before the work commences."),
  ("sub", "(e)", "Contractor Acknowledgment. Mortgagor shall cause the Contractor, and each subcontractor performing work in or near Bay 1, to acknowledge in writing the existence and location of the Vapor Barrier and the requirements of the LUR, and shall deliver such acknowledgments to Mortgagee."),
  ("sub", "(f)", "Records; Notice. Mortgagor shall maintain complete records of all inspections, maintenance and repairs relating to the Vapor Barrier and the Institutional Controls for the term of the Loan and for three (3) years thereafter, and shall make them available to Mortgagee upon request. Mortgagor shall notify Mortgagee within three (3) Business Days of any SCDHEC inquiry, inspection, notice, determination or request relating to the LUR or the Institutional Controls."),
  ("sub", "(g)", "Costs. Mortgagor shall bear all costs of compliance with this Section 7.4. Any reasonable cost incurred by Mortgagee to monitor, verify or enforce compliance, or to cure any non-compliance, shall be a protective advance secured by this Mortgage and reimbursable on demand."),
  ("p", "A breach of this Section 7.4 is an Event of Default subject to the cure period provided in Section 10.2(c)."),
 ]),
 dict(num="7.5", title="Single-Purpose Entity and Separateness Covenants", content=[
  ("p", "Mortgagor shall at all times during the term of the Loan maintain its status as a Single-Purpose Entity and shall comply with the following separateness covenants:"),
  ("sub", "(a)", "Purpose. Mortgagor shall not engage in any business or activity other than the ownership, operation, renovation, leasing, management and disposition of the Property and activities incidental thereto, and shall not hold, acquire or own any asset other than the Property and incidental cash and reserves."),
  ("sub", "(b)", "Separate Books and Records. Mortgagor shall maintain its own separate books of account, financial records, minute books and other entity records separate and apart from those of any other Person, and shall maintain its books and records and financial statements in a manner that identifies its assets and liabilities separately."),
  ("sub", "(c)", "Separate Bank Accounts. Mortgagor shall maintain its own bank accounts, including the accounts funded with the Reserve Funds, in its own name, separate and apart from those of any other Person."),
  ("sub", "(d)", "No Commingling. Mortgagor shall not commingle its funds or assets with those of any Affiliate, member, manager or other Person."),
  ("sub", "(e)", "Public Identification. Mortgagor shall hold itself out to the public, and conduct its business, in its own name; shall use its own stationery, invoices, checks and business forms; and shall not hold itself out as being a division or part of any other Person."),
  ("sub", "(f)", "Adequate Capitalization. Mortgagor shall maintain adequate capitalization in light of its contemplated business operations, transactions and liabilities."),
  ("sub", "(g)", "Own Liabilities. Mortgagor shall pay its own liabilities and expenses from its own assets and shall not pay the liabilities of, or guarantee or become obligated for the debts of, any Affiliate, member, manager or other Person, except as expressly permitted by this Mortgage."),
  ("sub", "(h)", "Arm\u2019s-Length Dealings. Mortgagor shall maintain arm\u2019s-length relationships with its Affiliates, members and managers, and any transaction with an Affiliate shall be on commercially reasonable terms and shall be disclosed to Mortgagee."),
  ("sub", "(i)", "No Additional Indebtedness. Mortgagor shall not incur, assume or permit to exist any additional indebtedness, secured or unsecured, without Mortgagee\u2019s prior written consent, except ordinary-course trade payables incurred in the operation of the Property and not more than sixty (60) days past due."),
  ("sub", "(j)", "Independent Manager. Mortgagor shall not take, authorize, consent to or acquiesce in any of the following without the affirmative vote of the independent manager (or independent director) required by Mortgagor\u2019s organizational documents, who shall not be a member, manager, employee, officer, creditor or Affiliate of Mortgagor, any member or Guarantor: (i) the filing of a voluntary petition under the Bankruptcy Code or any state insolvency proceeding; (ii) consenting to the appointment of a receiver, trustee or custodian; (iii) making an assignment for the benefit of creditors; (iv) dissolution, liquidation, winding up, merger or consolidation; or (v) any amendment to Mortgagor\u2019s organizational documents that would eliminate the independent-manager requirement or any separateness covenant."),
  ("sub", "(k)", "Organizational Documents. Mortgagor represents and warrants that its certificate of formation and operating agreement have been amended, prior to the Closing Date, to include the single-purpose restriction, the separateness covenants, the independent-manager requirement and the bankruptcy-remoteness provisions required by this Section 7.5 and Section 8.3, in form and substance satisfactory to Mortgagee, and that all members of Mortgagor have executed and delivered that amendment."),
  ("sub", "(l)", "No Amendment. Mortgagor shall not amend, modify, waive, repeal or otherwise alter any single-purpose, separateness, bankruptcy-remoteness or independent-manager provision of its organizational documents without Mortgagee\u2019s prior written consent in each instance."),
  ("sub", "(m)", "Reporting. Mortgagor shall deliver to Mortgagee, within thirty (30) days after request, a certificate confirming its continued compliance with this Section 7.5."),
 ]),
 dict(num="7.6", title="Encroachment License; Further Deliverables", content=[
  ("p", "Mortgagor shall use commercially reasonable efforts to obtain and maintain in effect, at its sole cost, a valid encroachment license, permit or other authorization from the City of Charleston with respect to the decorative iron balcony encroaching approximately two and one-half (2.5) feet over the King Street right-of-way, and shall promptly deliver copies to Mortgagee. Mortgagor shall notify Mortgagee within three (3) Business Days of any assertion by any Governmental Authority that the balcony must be removed, modified or permitted, and shall not remove or materially modify the balcony without Mortgagee\u2019s prior written consent, except to the extent required by Applicable Law or by the order of a Governmental Authority having jurisdiction."),
  ("p", "Mortgagor shall cooperate with Mortgagee in obtaining the title endorsements contemplated by Exhibit C, including a survey/encroachment endorsement (ALTA Endorsement 28.1 or equivalent) with respect to the balcony encroachment, an owner\u2019s comprehensive endorsement, a zoning endorsement (ALTA 3.1), an access endorsement, a contiguity endorsement with respect to Lots 7, 8 and 9 and Parcel Two, a future advance endorsement (ALTA 14) with respect to the Renovation Holdback, and such identified-exception or affirmative-coverage endorsements as Mortgagee may require with respect to Parcel Two."),
 ]),
 dict(num="7.7", title="Financial Reporting", content=[
  ("p", "Mortgagor and Guarantor shall deliver to Mortgagee the following:"),
  ("sub", "(a)", "Annual audited financial statements of Mortgagor, prepared in accordance with GAAP by an independent certified public accounting firm reasonably acceptable to Mortgagee, within one hundred twenty (120) days after the end of each fiscal year;"),
  ("sub", "(b)", "An annual personal financial statement of Guarantor, in form and detail reasonably satisfactory to Mortgagee, within one hundred twenty (120) days after the end of each calendar year;"),
  ("sub", "(c)", "Quarterly rent rolls for the Property, certified by Mortgagor as true, correct and complete and identifying all vacant space, within thirty (30) days after the end of each calendar quarter;"),
  ("sub", "(d)", "Annual property operating statements for the Property, including a detailed income and expense report and a comparison to budget, within one hundred twenty (120) days after the end of each fiscal year;"),
  ("sub", "(e)", "Copies of all Leases, lease amendments, letters of intent, guaranties of lease and material leasing correspondence, within ten (10) Business Days after execution;"),
  ("sub", "(f)", "A quarterly compliance certificate, executed by an authorized officer or manager of Mortgagor, certifying compliance with Sections 7.4, 7.5 and 7.8 (or specifying any non-compliance), and setting forth in reasonable detail the computation of DSCR, net worth and liquidity;"),
  ("sub", "(g)", "The annual Vapor Barrier inspection report and certification required under Section 7.4(c); and"),
  ("sub", "(h)", "Promptly upon request, such other information regarding the Property, Mortgagor, Guarantor or the renovation as Mortgagee may reasonably require."),
  ("p", "Mortgagor acknowledges that Mortgagor\u2019s operating agreement requires only reviewed (not audited) annual financial statements to be delivered to its members, and that this Section 7.7(a) imposes a more stringent audit requirement. Mortgagor shall cause any necessary amendment to its operating agreement, or obtain any necessary member approval, to permit it to satisfy this Section 7.7(a)."),
 ]),
 dict(num="7.8", title="Financial Covenants", content=[
  ("sub", "(a)", "Debt Service Coverage Ratio. Mortgagor shall maintain a DSCR of not less than 1.25x. DSCR testing shall commence twenty-four (24) months after the Closing Date, with the first test date being the first full calendar quarter ending after the twenty-fourth month following the Closing Date, and shall thereafter be tested quarterly on a trailing twelve (12) month basis. \u201cAnnual Debt Service\u201d means, for the applicable period, the aggregate amount of principal and interest that would be payable on the Loan over such period based on the then-outstanding principal balance, the then-applicable Note Rate and, after the commencement of amortization, the twenty-five (25) year amortization schedule, without regard to any balloon payment. \u201cNet Operating Income\u201d has the meaning set forth in Section 1.1 and shall be calculated on a trailing twelve (12) month basis with vacancy and collection loss determined on an actual basis for occupied space and at market rent (less a five percent (5%) vacancy and collection allowance) for vacant space only to the extent such space has been leased and rent has commenced."),
  ("sub", "(b)", "Net Worth. Mortgagor shall maintain at all times a net worth of not less than One Million Dollars ($1,000,000.00), tested annually based on the financial statements delivered under Section 7.7(a), determined in accordance with GAAP."),
  ("sub", "(c)", "Liquidity. Mortgagor shall maintain at all times liquid assets (being cash, cash equivalents, marketable securities and unencumbered deposits held at federally insured depository institutions) of not less than Five Hundred Thousand Dollars ($500,000.00), tested annually based on the financial statements delivered under Section 7.7(a)."),
  ("p", "A breach of Section 7.8(a) continuing for two (2) consecutive calendar quarters following the commencement of DSCR testing, without cure, is an Event of Default under Section 10.1(j). A breach of Section 7.8(b) or Section 7.8(c) is a covenant default subject to the cure period in Section 10.2(b)."),
 ]),
 dict(num="7.9", title="Further Assurances; Perfection", content=[
  ("p", "Mortgagor shall execute, acknowledge, deliver and record such further instruments and take such further action as Mortgagee may reasonably request to create, perfect, maintain, continue or enforce the lien of this Mortgage and Mortgagee\u2019s security interests, including continuation statements (which must be filed within the six (6) month period before each fifth anniversary of the initial filing), date-down and modification endorsements to the Title Policy, and estoppel certificates. Mortgagor shall pay all recording, filing and endorsement costs, including the South Carolina deed recording fee of $1.85 per $500 of indebtedness (approximately $54,575.00 on the Loan amount)."),
 ]),
 dict(num="7.10", title="Access, Inspection and Books and Records", content=[
  ("p", "Mortgagor shall permit Mortgagee and its agents, appraisers, engineers, inspectors and consultants to enter upon the Property at reasonable times and upon reasonable prior notice (and without notice following an Event of Default) to inspect, examine, audit, test and appraise the Property and to review Mortgagor\u2019s books and records relating to the Property. Mortgagor shall cooperate with reasonable requests and shall pay the cost of inspections, appraisals and audits that Mortgagee reasonably requires, including the third-party construction inspections contemplated by Section 9.3(f)."),
 ]),
 dict(num="7.11", title="Notice Obligations", content=[
  ("p", "Mortgagor shall notify Mortgagee in writing within five (5) Business Days after Mortgagor obtains knowledge of: (a) any Event of Default or any event that with notice or lapse of time would become an Event of Default; (b) any litigation, arbitration or governmental proceeding affecting the Property, Mortgagor or Guarantor involving more than $100,000.00; (c) any casualty, Condemnation or material damage to the Property; (d) any environmental condition, release or regulatory inquiry; (e) any change in the members, managers, registered agent or principal place of business of Mortgagor; (f) any change in the ownership or control of any member of Mortgagor or of Guarantor; and (g) any default under any other indebtedness of Mortgagor, any member or Guarantor."),
 ]),
 dict(num="7.12", title="Payment of Costs and Expenses", content=[
  ("p", "Mortgagor shall pay on demand all costs and expenses incurred by Mortgagee in connection with the origination, documentation, closing, administration, servicing, enforcement and defense of the Loan and the Loan Documents, including the legal fees and disbursements of Mortgagee\u2019s counsel (Fielding, Ashworth & Cole LLP), appraisal, appraisal review and update fees, environmental review fees, title premiums and search charges, survey costs, recording fees and deed recording taxes, UCC filing and search fees, construction inspection fees, and all costs of collection, foreclosure, bankruptcy and appeal. Such amounts shall be secured by this Mortgage and shall bear interest at the Default Rate from the date incurred until paid."),
 ]),
 dict(num="7.13", title="Completion of Renovation", content=[
  ("p", "Mortgagor shall cause the renovation of the Property to be performed in a good and workmanlike manner, in accordance with the approved plans and specifications, the Renovation Budget, all building permits and Board of Architectural Review approvals, the LUR and Section 7.4, and shall cause Substantial Completion to occur on or before the Substantial Completion Deadline of June 15, 2026. This covenant is guaranteed by Guarantor under the completion guaranty described in Section 5.5(b) of the Term Sheet."),
 ]),
]))

# ============================================================ ARTICLE 8
ARTICLES.append(dict(num="8", title="Negative Covenants", sections=[
 dict(num="8.1", title="No Junior Financing; No Additional Indebtedness", content=[
  ("p", "Mortgagor shall not incur, create, assume, permit to exist or suffer any lien, mortgage, deed of trust, security interest, pledge, encumbrance or other charge on the Property or any portion thereof or interest therein, other than the Permitted Exceptions and the lien of this Mortgage; and shall not incur, create or assume any indebtedness, whether secured or unsecured, without Mortgagee\u2019s prior written consent, including any mezzanine loan, preferred equity interest, ground lease, sale-leaseback, or other financing arrangement that may affect Mortgagee\u2019s collateral position or priority. Mortgagor shall not enter into any agreement that restricts Mortgagor\u2019s ability to grant liens to Mortgagee or that gives any other Person a negative pledge with respect to the Property."),
 ]),
 dict(num="8.2", title="Transfer Restrictions", content=[
  ("sub", "(a)", "Property. Mortgagor shall not, without Mortgagee\u2019s prior written consent, sell, convey, transfer, assign, pledge, encumber, lease (other than Leases permitted under Section 5.5), option, or otherwise dispose of the Property or any portion thereof or any interest therein, whether voluntarily, involuntarily or by operation of law."),
  ("sub", "(b)", "Direct Interests. Mortgagor shall not permit any Transfer of any direct ownership interest in Mortgagor exceeding ten percent (10%) individually or twenty-five percent (25%) in the aggregate, without Mortgagee\u2019s prior written consent; provided that Transfers among the existing members of Mortgagor (Graydon Development Group LLC, Tidewater Opportunity Fund II LP and Harborline Capital Advisors LLC) are permitted without Mortgagee\u2019s consent if (i) the transferee is an existing member, (ii) the Managing Member and control of Mortgagor do not change, and (iii) Mortgagor gives Mortgagee at least thirty (30) days\u2019 prior written notice and executes such confirmatory documentation as Mortgagee requires."),
  ("sub", "(c)", "Indirect Interests and Change of Control. Mortgagor shall not permit, without Mortgagee\u2019s prior written consent, (i) any Transfer of any direct or indirect interest in Graydon Development Group LLC, (ii) any change in the identity of the Managing Member of Mortgagor or in the Person exercising Control over Mortgagor or over Graydon Development Group LLC, (iii) any Transfer by Neil Ashford Graydon of any direct or indirect interest in Graydon Development Group LLC, or (iv) any change in Control of Guarantor-affiliated entities holding interests in Mortgagor. Mortgagor acknowledges that a Transfer described in this Section 8.2(c) would not constitute a Transfer of a membership interest in Mortgagor under its operating agreement and therefore would not be captured by Mortgagor\u2019s internal transfer restrictions, and Mortgagor accordingly agrees that such Transfers are prohibited under this Mortgage without Mortgagee\u2019s consent."),
  ("sub", "(d)", "Tidewater Transfers. Notwithstanding any provision of Mortgagor\u2019s operating agreement (including Section 4.2(c) thereof, which designates as a \u201cPermitted Transfer\u201d any Transfer directed by Tidewater GP Holdings LLC to any successor fund managed by Tidewater GP Holdings LLC or an Affiliate thereof), any Transfer of Tidewater Opportunity Fund II LP\u2019s 18% membership interest, including a Transfer to a successor fund, is a Transfer subject to Section 8.2(b) requiring Mortgagee\u2019s prior written consent, unless Mortgagee consents in writing to treat such Transfer as a permitted transfer."),
  ("sub", "(e)", "Consequence. Any Transfer in violation of this Section 8.2 is void, is an immediate Event of Default without notice or opportunity to cure, and constitutes a carve-out event for purposes of Section 12.3 and the Guaranty."),
 ]),
 dict(num="8.3", title="No Amendment of Organizational Documents; No Dissolution or Bankruptcy", content=[
  ("p", "Mortgagor shall not, without Mortgagee\u2019s prior written consent: (a) amend, restate, modify or waive any provision of its certificate of formation or operating agreement, including any provision relating to its purpose, its single-purpose status, separateness, capitalization, dissolution, transfer restrictions, management, the approval threshold for Major Decisions, or the independent-manager requirement; (b) dissolve, liquidate, wind up, merge, consolidate, convert or reorganize; (c) file or consent to the filing of a voluntary petition under the Bankruptcy Code or any state insolvency proceeding, or consent to the appointment of a receiver, trustee or custodian; or (d) make an assignment for the benefit of creditors."),
  ("p", "Mortgagor represents and warrants that, as of the Closing Date, its operating agreement has been amended to (i) restrict its purpose to the ownership, operation, renovation, leasing and financing of the Property and activities incidental thereto; (ii) include the separateness covenants set forth in Section 7.5; (iii) require the affirmative vote of an independent manager before any bankruptcy filing, dissolution, merger or consolidation; (iv) require Mortgagee\u2019s prior written consent to any amendment of the single-purpose, separateness, bankruptcy-remoteness or independent-manager provisions; and (v) require the unanimous written consent of all members to any bankruptcy filing, dissolution or merger, in each case in form and substance satisfactory to Mortgagee."),
  ("p", "Mortgagor acknowledges that its operating agreement as in effect immediately before the Closing Date does not contain the provisions described in this Section 8.3, and that the delivery of an executed amendment satisfying this Section 8.3, signed by all three (3) members of Mortgagor, is a condition precedent to the Initial Advance under Section 12.1(a)."),
 ]),
 dict(num="8.4", title="No Change in Use; No Residential Conversion", content=[
  ("p", "Mortgagor shall not change the use of the Property or any portion thereof from the current mixed-use retail and office use without Mortgagee\u2019s prior written consent; shall not convert the ground floor of Lot 7 to residential use; shall not seek or consent to any rezoning or variance without Mortgagee\u2019s prior written consent; and shall not use or permit any use of the Property that would violate Applicable Law, the LUR or any Lease."),
 ]),
 dict(num="8.5", title="No Waste; No Alteration; No Demolition", content=[
  ("p", "Mortgagor shall not commit waste; shall not demolish or materially alter any Improvement except as expressly permitted in Article 9; and shall not permit any mechanic\u2019s, materialman\u2019s or other lien to attach to the Property. If any such lien is filed, Mortgagor shall discharge it of record, or bond over it in a manner reasonably satisfactory to Mortgagee and the Title Insurer, within thirty (30) days after notice of filing."),
 ]),
 dict(num="8.6", title="No Misapplication of Rents, Deposits or Proceeds", content=[
  ("p", "Mortgagor shall not misapply or misappropriate any Rents, tenant security deposits, insurance proceeds or condemnation awards. Any such misapplication is an immediate Event of Default and constitutes a carve-out event for purposes of Section 12.3 and the Guaranty."),
 ]),
 dict(num="8.7", title="Renovation Contract", content=[
  ("p", "Mortgagor shall not terminate, assign, amend in any material respect, or waive any material right under the Renovation Contract, and shall not replace the Contractor, without Mortgagee\u2019s prior written consent. Mortgagor shall deliver to Mortgagee, within ten (10) Business Days of execution, all change orders and amendments to the Renovation Contract."),
 ]),
]))

# ============================================================ ARTICLE 9
ARTICLES.append(dict(num="9", title="Renovation Holdback and Disbursement Provisions", sections=[
 dict(num="9.1", title="The Renovation Holdback", content=[
  ("p", "Of the total Loan commitment of $14,750,000.00, the sum of $2,250,000.00 is retained by Mortgagee as the Renovation Holdback and shall be disbursed to Mortgagor on a draw basis for renovation costs incurred at the Property, upon satisfaction of the conditions of this Article 9. The Renovation Holdback is a portion of the Loan, bears interest from the date of each disbursement, and is secured by this Mortgage. Mortgagee has no obligation to disburse any portion of the Renovation Holdback, and no disbursement constitutes a waiver of any condition or of any Event of Default."),
 ]),
 dict(num="9.2", title="Renovation Budget and Renovation Contract", content=[
  ("p", "The renovation shall be performed in accordance with the Renovation Budget of $3,150,000.00 (Exhibit B) and the Renovation Contract with the Contractor in the contract sum of $2,850,000.00. The Renovation Holdback of $2,250,000.00 is $600,000.00 less than the hard costs under the Renovation Contract, and Mortgagor shall be solely responsible, from its own funds and not from Loan proceeds, for renovation costs in excess of the Renovation Holdback, including the $900,000.00 of Borrower equity allocated in Exhibit B and any cost overrun, change order, design change, code compliance cost or unforeseen condition."),
  ("p", "Mortgagor shall not amend the Renovation Budget or reallocate amounts among line items without Mortgagee\u2019s prior written consent, and shall not enter into any change order that increases the Renovation Contract sum or the Renovation Budget without Mortgagee\u2019s prior written consent, except for change orders aggregating not more than $50,000.00 in the aggregate that do not affect the critical path, any building system, or any work affecting the Vapor Barrier. Mortgagor shall deliver copies of all change orders to Mortgagee within five (5) Business Days of execution."),
 ]),
 dict(num="9.3", title="Conditions to Each Disbursement", content=[
  ("p", "Mortgagee\u2019s obligation to make any disbursement of the Renovation Holdback is subject to satisfaction of each of the following conditions, in form and substance satisfactory to Mortgagee:"),
  ("sub", "(a)", "No Event of Default has occurred and is continuing, and no event has occurred that with notice or lapse of time would constitute an Event of Default;"),
  ("sub", "(b)", "Mortgagor has delivered a written draw request not less than ten (10) Business Days before the requested disbursement date, and draws shall be made no more frequently than once per calendar month and in no event more than fourteen (14) draws in the aggregate;"),
  ("sub", "(c)", "The draw request is accompanied by an AIA G702/G703 Application and Certificate for Payment, certified by Mortgagor\u2019s architect of record, detailing the work completed, amounts previously paid, retainage withheld and the amount currently requested;"),
  ("sub", "(d)", "The draw request is accompanied by a certification from Mortgagor\u2019s architect that the work for which payment is requested has been completed in accordance with the approved plans and specifications;"),
  ("sub", "(e)", "The draw request is accompanied by conditional lien waivers from the Contractor and each subcontractor or supplier performing work covered by the current draw, and unconditional lien waivers from the Contractor and each subcontractor performing work in an amount exceeding $25,000.00 for all prior draws;"),
  ("sub", "(f)", "Mortgagee has received a title date-down endorsement from the Title Insurer confirming that no intervening mechanic\u2019s, materialman\u2019s or other lien or encumbrance has been filed against the Property since the date of recording of this Mortgage or the most recent date-down endorsement;"),
  ("sub", "(g)", "Mortgagee has received evidence of its satisfactory inspection of the work in progress, which inspection may be conducted by a third-party inspector or architect retained by Mortgagee at Mortgagor\u2019s expense;"),
  ("sub", "(h)", "Mortgagor has demonstrated to Mortgagee\u2019s reasonable satisfaction that its equity contribution has been applied in accordance with Exhibit B and that sufficient funds, from equity, the remaining Renovation Holdback and any contingency, remain to complete the renovation within the Renovation Budget (a current cost-to-complete analysis);"),
  ("sub", "(i)", "All building permits, Board of Architectural Review approvals and certificates of occupancy required for the work covered by the draw are in effect;"),
  ("sub", "(j)", "If the work covered by the draw penetrates or is likely to disturb the floor slab of Bay 1 on Lot 7, Mortgagor has satisfied Section 7.4(d) and (e), including SCDHEC notification and approval and the environmental professional\u2019s inspections;"),
  ("sub", "(k)", "The Contractor\u2019s and all subcontractors\u2019 insurance, including builder\u2019s risk, is in effect with Mortgagee named as mortgagee and loss payee; and"),
  ("sub", "(l)", "Mortgagor has delivered such other certificates, lien waivers, invoices, paid receipts, test reports or documents as Mortgagee may reasonably require."),
 ]),
 dict(num="9.4", title="Retainage", content=[
  ("p", "Mortgagee shall retain ten percent (10%) of each disbursement from the Renovation Holdback (the \u201cRetainage\u201d) until Substantial Completion has been achieved. Retainage shall be released upon Mortgagee\u2019s receipt of (a) satisfactory evidence of Substantial Completion, including the architect\u2019s certificate and the certificate of occupancy; (b) final unconditional lien waivers from the Contractor and all subcontractors and suppliers; (c) a final title date-down endorsement confirming no intervening liens; (d) evidence that the Vapor Barrier has been inspected and is intact following completion of any work affecting it; and (e) evidence that all punch-list items have been completed or are covered by adequate escrow or retainage. Mortgagor acknowledges that the draw schedule attached as Exhibit B is illustrative of timing and does not reflect Retainage mechanics, and that actual disbursements shall be governed by this Section 9.4."),
 ]),
 dict(num="9.5", title="Substantial Completion Deadline", content=[
  ("p", "Mortgagor shall achieve Substantial Completion on or before the Substantial Completion Deadline of June 15, 2026. If Substantial Completion has not occurred by that date, an Event of Default exists under Section 10.1(n), and Guarantor shall be liable under the completion guaranty. Mortgagee may, in its sole discretion and upon such terms as it requires (including a completion deposit or additional guaranty), extend the Substantial Completion Deadline in writing."),
 ]),
 dict(num="9.6", title="Cost Overruns; No Obligation to Increase the Loan", content=[
  ("p", "Mortgagor shall bear all renovation costs in excess of the Renovation Budget and in excess of the Renovation Holdback. Mortgagee has no obligation to increase the Loan, to make protective advances for construction costs, or to advance any amount in excess of the Renovation Holdback. If Mortgagor fails to fund a cost overrun when required and the work is delayed or a lien attaches, Mortgagee may, at its option, advance funds to pay the cost, and any such advance shall be a protective advance secured by this Mortgage, bearing interest at the Default Rate and repayable on demand."),
 ]),
 dict(num="9.7", title="Suspension of Disbursements", content=[
  ("p", "Mortgagee may suspend disbursements of the Renovation Holdback if (a) an Event of Default has occurred, (b) any condition in Section 9.3 is not satisfied, (c) Mortgagee reasonably determines that the renovation cannot be completed within the Renovation Budget or by the Substantial Completion Deadline, (d) any mechanic\u2019s lien is filed and not discharged or bonded over within thirty (30) days, (e) any stop-payment notice or notice of non-payment is received from the Contractor or any subcontractor, or (f) the Title Insurer declines to issue a date-down endorsement. Suspension of disbursements is not an Event of Default and does not relieve Mortgagor of any obligation."),
 ]),
 dict(num="9.8", title="No Warranty by Mortgagee; Inspection Disclaimer", content=[
  ("p", "Mortgagee\u2019s review of plans, budgets, draw requests and inspections, and any disbursement of the Renovation Holdback, shall not constitute an approval, warranty or representation by Mortgagee as to the adequacy, sufficiency, quality, workmanship, compliance or completion of the renovation or the plans, and Mortgagee shall have no liability for any defect, deficiency, delay, cost overrun, lien claim or non-compliance with Applicable Law arising from the renovation. Mortgagor acknowledges that it bears sole responsibility for the renovation and that Mortgagee\u2019s interests are protected only by the Loan Documents and the Guaranty."),
 ]),
]))

# ============================================================ ARTICLE 10
ARTICLES.append(dict(num="10", title="Events of Default", sections=[
 dict(num="10.1", title="Events of Default", content=[
  ("p", "Each of the following constitutes an Event of Default under this Mortgage:"),
  ("sub", "(a)", "Payment. Failure by Mortgagor to pay any principal, interest, late charge or other amount due under the Loan Documents on the date due, subject to the cure period in Section 10.2(a);"),
  ("sub", "(b)", "Covenant Breach. Breach by Mortgagor of any covenant, agreement or obligation in this Mortgage or any other Loan Document, continuing beyond the applicable cure period in Section 10.2;"),
  ("sub", "(c)", "Misrepresentation. Any representation or warranty made by Mortgagor or Guarantor in any Loan Document or in any certificate or report delivered under the Loan Documents proves to be false, misleading or inaccurate in any material respect when made or deemed made;"),
  ("sub", "(d)", "Bankruptcy and Insolvency. The filing by or against Mortgagor or Guarantor of any petition under the Bankruptcy Code or any state insolvency proceeding (in the case of an involuntary petition, if not dismissed within sixty (60) days), the appointment of a receiver, trustee or custodian for any substantial part of the property or assets of Mortgagor or Guarantor, any assignment for the benefit of creditors, or any similar proceeding;"),
  ("sub", "(e)", "Cross-Default. A default by Mortgagor, any member of Mortgagor or Guarantor under any other indebtedness for borrowed money in an amount exceeding $250,000.00 individually or in the aggregate, which default is not cured within any applicable cure or grace period;"),
  ("sub", "(f)", "Insurance. Failure by Mortgagor to maintain any insurance required under Section 6.6, or failure to deliver evidence of insurance as required;"),
  ("sub", "(g)", "Transfer. Any Transfer in violation of Section 8.2, including any direct or indirect Transfer or change of Control described in Section 8.2(c) or 8.2(d);"),
  ("sub", "(h)", "Single-Purpose Entity. Breach of any covenant in Section 7.5 or Section 8.3, including any failure to maintain the independent-manager requirement, any commingling of funds, or any amendment of the organizational documents without Mortgagee\u2019s consent;"),
  ("sub", "(i)", "Junior Financing. Any breach of Section 8.1 or Section 8.7;"),
  ("sub", "(j)", "DSCR. The DSCR falling below 1.25x for two (2) consecutive calendar quarters following the commencement of DSCR testing under Section 7.8(a), without cure;"),
  ("sub", "(k)", "Institutional Controls. Any failure by Mortgagor to comply with the LUR or the Institutional Controls, including any conversion of the ground floor of Lot 7 to residential use, any penetration, removal or impairment of the Vapor Barrier not repaired in accordance with Section 7.4, any failure to obtain the inspections or deliver the reports required by Section 7.4(c), any failure to notify SCDHEC or Mortgagee before work affecting the Bay 1 slab, or any amendment, modification or termination of the LUR without Mortgagee\u2019s consent, subject to the cure period in Section 10.2(c);"),
  ("sub", "(l)", "Environmental. Any breach of Section 7.3, or any release of Hazardous Materials at the Property that is not remediated in accordance with Environmental Laws and this Mortgage, or any default under the Environmental Indemnity Agreement;"),
  ("sub", "(m)", "Guaranty. Any default by Guarantor under the Guaranty or the Environmental Indemnity Agreement, or any termination, repudiation or asserted unenforceability of either;"),
  ("sub", "(n)", "Substantial Completion. Failure by Mortgagor to achieve Substantial Completion by the Substantial Completion Deadline, subject to any written extension granted by Mortgagee;"),
  ("sub", "(o)", "Reserves. Failure by Mortgagor to make any deposit to any Reserve Fund, or failure to replenish the Tenant Improvement and Leasing Commission Reserve within thirty (30) days of demand;"),
  ("sub", "(p)", "Encroachment. Removal, demolition or material modification of the decorative iron balcony required by a Governmental Authority without Mortgagee\u2019s prior written consent, where such removal or modification is not covered by available insurance proceeds;"),
  ("sub", "(q)", "Title; Permitted Exceptions. Any failure to maintain the Title Policy in full force and effect, or the assertion of any lien, encumbrance or adverse claim against the Property (other than a Permitted Exception) that is not discharged or bonded over within thirty (30) days;"),
  ("sub", "(r)", "Material Adverse Change. A material adverse change in the financial condition, business, assets or operations of Mortgagor or Guarantor that, in Mortgagee\u2019s reasonable judgment, materially impairs the ability of Mortgagor to perform its obligations under the Loan Documents or of Guarantor to perform under the Guaranty;"),
  ("sub", "(s)", "Dissolution. The dissolution, liquidation, merger, consolidation or winding up of Mortgagor (other than as expressly permitted in writing by Mortgagee); and"),
  ("sub", "(t)", "Other. The occurrence of any other event or condition that constitutes an Event of Default under any other Loan Document."),
 ]),
 dict(num="10.2", title="Cure Periods and Notice", content=[
  ("sub", "(a)", "Payment Defaults. Five (5) Business Days after the date on which payment was due."),
  ("sub", "(b)", "Non-Monetary Defaults. Thirty (30) calendar days after written notice from Mortgagee to Mortgagor of the default; provided that if the default is of a nature that cannot reasonably be cured within thirty (30) calendar days and Mortgagor has commenced and is diligently pursuing cure, the cure period shall be extended for an additional period not to exceed sixty (60) calendar days (for a total cure period not to exceed ninety (90) calendar days), and provided further that no such extension is available for a breach of Section 8.2 (Transfers) or Section 8.3 (organizational documents and bankruptcy)."),
  ("sub", "(c)", "Institutional Controls Defaults. Thirty (30) calendar days after written notice from Mortgagee to Mortgagor; provided that if cure requires SCDHEC approval, notice or action, the cure period shall be extended for so long as Mortgagor is diligently pursuing cure and SCDHEC action is pending, not to exceed one hundred eighty (180) calendar days, and provided further that no cure period applies to any conversion of the ground floor of Lot 7 to residential use, which is an immediate Event of Default."),
  ("p", "No cure period applies to any Event of Default described in Section 10.1(d) (bankruptcy and insolvency), Section 10.1(g) (Transfers) or Section 10.1(h) (Single-Purpose Entity). Mortgagee shall not be required to give notice of any Event of Default more than once with respect to the same default, and notice of any default given for any purpose under any Loan Document shall be effective for all purposes. Acceptance of any payment after an Event of Default does not cure the default or waive Mortgagee\u2019s rights unless Mortgagee agrees in writing."),
 ]),
]))

# ============================================================ ARTICLE 11
ARTICLES.append(dict(num="11", title="Remedies", sections=[
 dict(num="11.1", title="Remedies Upon Default", content=[
  ("p", "Upon the occurrence and during the continuance of an Event of Default, Mortgagee may, at its option and in addition to all other rights and remedies available at law or in equity, exercise any one or more of the following remedies, concurrently or successively, without any requirement of notice except as expressly required by Applicable Law:"),
  ("sub", "(a)", "declare the entire Indebtedness immediately due and payable, whereupon it shall become due and payable without further presentment, demand, protest or notice of any kind, all of which Mortgagor waives to the maximum extent permitted by Applicable Law;"),
  ("sub", "(b)", "accelerate the maturity of the Note and bring suit on the Note, this Mortgage or any other Loan Document, in one or more actions, for the collection of the Indebtedness;"),
  ("sub", "(c)", "foreclose the lien of this Mortgage by judicial action in the Court of Common Pleas for Charleston County, South Carolina (or, at Mortgagee\u2019s election, in any other court of competent jurisdiction), and cause the Property to be sold in accordance with Applicable Law;"),
  ("sub", "(d)", "enforce the absolute assignment of Rents under Article 5, including by giving notice to the Tenants and collecting the Rents directly, without the necessity of foreclosure, court order or appointment of a receiver;"),
  ("sub", "(e)", "apply to a court of competent jurisdiction for the appointment of a receiver of the Property and the Rents;"),
  ("sub", "(f)", "exercise all rights and remedies of a secured party under the Code with respect to the Personal Property Collateral, including the right to take possession, to require Mortgagor to assemble the collateral and make it available, and to sell, lease or otherwise dispose of the collateral at public or private sale after notice as required by the Code;"),
  ("sub", "(g)", "enter upon and take possession of the Property, and manage, operate, maintain, repair, complete the renovation of, and lease the Property, and perform or cause to be performed all obligations of Mortgagor under the Leases;"),
  ("sub", "(h)", "apply the Reserve Funds to the Indebtedness in such order as Mortgagee determines;"),
  ("sub", "(i)", "seek specific performance, injunctive relief or declaratory relief to enforce any covenant, including the covenants in Sections 7.3, 7.4, 7.5 and 8.3;"),
  ("sub", "(j)", "pursue any remedy available under the Guaranty, the Environmental Indemnity Agreement or any other Loan Document; and"),
  ("sub", "(k)", "recover all costs of enforcement, including reasonable attorneys\u2019 fees, court costs, receiver\u2019s fees, appraisal fees, title charges and trustee or commissioner fees."),
 ]),
 dict(num="11.2", title="Judicial Foreclosure Only; No Power of Sale", content=[
  ("p", "The State of South Carolina is a judicial foreclosure jurisdiction. This Mortgage does not grant, and shall not be construed to grant, any power of sale or any right in Mortgagee to sell the Property without judicial proceedings. Mortgagee\u2019s remedy of foreclosure shall be exercised exclusively by judicial action in accordance with the laws of the State of South Carolina, including the applicable requirements governing the filing of the foreclosure action, the entry of judgment, the conduct of the judicial sale, and any statutory period for upset bids, redemption or confirmation of sale. Nothing in this Mortgage shall be construed to authorize a nonjudicial or statutory power-of-sale foreclosure."),
  ("p", "Mortgagor acknowledges that any waiver of notice, presentment, demand or protest contained in this Mortgage is intended to operate only to the maximum extent permitted by Applicable Law, and that any right that may not lawfully be waived (including any non-waivable statutory right, any applicable notice of the foreclosure action, and any applicable right of redemption or upset bid) is not waived by this Mortgage."),
 ]),
 dict(num="11.3", title="Receiver", content=[
  ("p", "Upon the occurrence and during the continuance of an Event of Default, Mortgagee shall be entitled, as a matter of right and without regard to the adequacy of the security or the solvency of Mortgagor, to the appointment of a receiver of the Property and the Rents in any judicial proceeding to enforce this Mortgage, and Mortgagor irrevocably consents to such appointment. The receiver may manage, operate, maintain, repair, complete the renovation of and lease the Property, collect the Rents, and apply them as the court directs. The appointment of a receiver shall not impair Mortgagee\u2019s right to enforce the absolute assignment of Rents under Article 5 or to pursue foreclosure."),
 ]),
 dict(num="11.4", title="Application of Proceeds; Deficiency", content=[
  ("p", "The proceeds of any foreclosure sale, receiver\u2019s collection or disposition of the Personal Property Collateral shall be applied in the order set forth in Section 4.4, and any surplus shall be paid to Mortgagor or as otherwise required by Applicable Law. If the proceeds are insufficient to pay the Indebtedness in full, Mortgagor (to the extent of its liability under Section 12.3) shall be liable for the deficiency, and Mortgagee may seek a deficiency judgment in accordance with Applicable Law."),
 ]),
 dict(num="11.5", title="Cumulative Remedies; No Waiver; Mortgagee\u2019s Right to Cure", content=[
  ("p", "All rights and remedies of Mortgagee are cumulative and not exclusive, and may be exercised concurrently or successively. No failure or delay by Mortgagee in exercising any right, and no acceptance of any payment, shall operate as a waiver, and no single or partial exercise of any right shall preclude any other or further exercise. Any waiver must be in writing and shall be limited to its terms."),
  ("p", "If Mortgagor fails to perform any obligation under this Mortgage, Mortgagee may (but shall not be obligated to) perform it on Mortgagor\u2019s behalf, including paying taxes, premiums, lien claims, SCDHEC fees, inspection costs and repair costs, and all amounts so expended shall be protective advances secured by this Mortgage, bearing interest at the Default Rate and repayable on demand. Mortgagee\u2019s performance shall not cure any default or waive any right."),
 ]),
 dict(num="11.6", title="No Marshalling; Waiver of Certain Defenses", content=[
  ("p", "Mortgagor waives, to the maximum extent permitted by Applicable Law, any right to require Mortgagee to marshal assets, to proceed first against any particular portion of the Property or against any other Person, or to exhaust any remedy before exercising any other remedy. Mortgagor waives any defense based on the adequacy of the security, the solvency of any other Person, or any statute of limitations to the extent permitted by Applicable Law."),
 ]),
]))

# ============================================================ ARTICLE 12
ARTICLES.append(dict(num="12", title="Indemnification; Environmental Indemnity; Exculpation", sections=[
 dict(num="12.1", title="General Indemnity", content=[
  ("p", "Mortgagor shall indemnify, defend (with counsel reasonably acceptable to Mortgagee) and hold harmless Mortgagee, its officers, directors, employees, agents and successors and assigns from and against all claims, demands, actions, losses, damages, liabilities, penalties, fines, judgments, costs and expenses (including reasonable attorneys\u2019 fees and costs of investigation and defense) arising out of or relating to (a) the Property or any use or condition of the Property; (b) any breach of any representation, warranty or covenant in this Mortgage; (c) any act or omission of Mortgagor, its members, managers, agents, employees, contractors or Tenants; (d) any mechanics\u2019 or materialmen\u2019s lien claim; (e) any claim by any Tenant under any Lease; and (f) the renovation, including any defect, delay, cost overrun or non-compliance with Applicable Law, except to the extent caused by Mortgagee\u2019s gross negligence or willful misconduct."),
 ]),
 dict(num="12.2", title="Environmental Indemnity", content=[
  ("p", "Mortgagor and Guarantor have executed and delivered the Environmental Indemnity Agreement, pursuant to which they indemnify Mortgagee against all losses, liabilities, damages, costs and expenses (including reasonable attorneys\u2019 fees) arising from or relating to the presence, release or threatened release of Hazardous Materials on, under or emanating from the Property, and from any failure to comply with the LUR or the Institutional Controls, including the obligation to maintain and periodically inspect the Vapor Barrier and the prohibition on residential use of the ground floor of Lot 7. The Environmental Indemnity Agreement is a separate Loan Document, is expressly secured by this Mortgage to the extent of Mortgagor\u2019s obligations thereunder, and survives repayment of the Loan with respect to conditions existing or arising before repayment."),
 ]),
 dict(num="12.3", title="Non-Recourse; Exculpation; Carve-Outs", content=[
  ("p", "Consistent with Section 5.5(a) of the Term Sheet, the Loan is structured as non-recourse to Mortgagor, and Mortgagee\u2019s recourse for the Indebtedness is limited to the Property and the other collateral for the Loan, except that Mortgagor shall be personally liable (and Guarantor shall be liable under the Guaranty) for the entire outstanding Indebtedness if any of the following carve-out events occurs:"),
  ("sub", "(i)", "fraud or intentional misrepresentation by Mortgagor or Guarantor, or any officer, manager, member or agent of either, in connection with the Loan or any Loan Document;"),
  ("sub", "(ii)", "misapplication or misappropriation of Rents, tenant security deposits, insurance proceeds or condemnation awards;"),
  ("sub", "(iii)", "the voluntary filing of a petition under the Bankruptcy Code or any state insolvency proceeding by or on behalf of Mortgagor, or Mortgagor\u2019s consent to the appointment of a receiver, trustee or custodian, or Mortgagor\u2019s collusive participation in an involuntary petition;"),
  ("sub", "(iv)", "liability arising from the acts or omissions of Mortgagor, Guarantor or their agents with respect to Hazardous Materials or Environmental Laws, or any breach of Section 7.3 or Section 7.4; and"),
  ("sub", "(v)", "any Transfer in violation of Section 8.2, or any breach of Section 7.5 or Section 8.3."),
  ("p", "Except as provided in this Section 12.3, no recourse shall be had against Mortgagor or any member, manager or Affiliate of Mortgagor for the payment of the Indebtedness. Nothing in this Section 12.3 limits (a) the obligations of Guarantor under the Guaranty or the Environmental Indemnity Agreement, (b) Mortgagor\u2019s obligations under the Environmental Indemnity Agreement, (c) Mortgagee\u2019s remedies against the Property and the collateral, or (d) Mortgagor\u2019s obligations under Sections 7.1, 7.2, 7.3, 7.4, 8.4 and 12.1, which are full recourse to Mortgagor to the extent of the costs of performance and any loss in value of the Property. Mortgagor acknowledges that this Section 12.3 must be read together with the corresponding non-recourse and carve-out provisions of the Note and the Guaranty, which are intended to be identical in scope."),
 ]),
 dict(num="12.4", title="Survival", content=[
  ("p", "The indemnities in this Article 12 and the obligations under Section 7.4 shall survive the repayment of the Loan, the release of this Mortgage and the foreclosure of the Property, and shall remain enforceable for so long as any claim may be asserted."),
 ]),
]))

# ============================================================ ARTICLE 13
ARTICLES.append(dict(num="13", title="Miscellaneous", sections=[
 dict(num="13.1", title="Governing Law", content=[
  ("p", "This Mortgage shall be governed by and construed in accordance with the laws of the State of South Carolina, without regard to principles of conflicts of law that would require the application of the laws of another jurisdiction. The parties acknowledge that the Property is located in South Carolina, that this Mortgage is intended to be recorded in South Carolina, and that South Carolina has a substantial relationship to the parties and the transaction."),
 ]),
 dict(num="13.2", title="Jurisdiction and Venue", content=[
  ("p", "Mortgagor irrevocably submits to the jurisdiction of the courts of the State of South Carolina and the United States District Court for the District of South Carolina, in each case sitting in Charleston County, for the purposes of any action or proceeding arising out of or relating to this Mortgage, and waives any objection to venue in those courts and any claim of inconvenient forum."),
 ]),
 dict(num="13.3", title="Waiver of Jury Trial", content=[
  ("p", "MORTGAGOR AND MORTGAGEE EACH KNOWINGLY, VOLUNTARILY AND IRREVOCABLY WAIVE ANY RIGHT TO A TRIAL BY JURY IN ANY ACTION OR PROCEEDING ARISING OUT OF OR RELATING TO THIS MORTGAGE, THE LOAN OR ANY OTHER LOAN DOCUMENT, TO THE MAXIMUM EXTENT PERMITTED BY APPLICABLE LAW. THIS WAIVER IS A MATERIAL INDUCEMENT TO MORTGAGEE\u2019S MAKING OF THE LOAN."),
 ]),
 dict(num="13.4", title="Notices", content=[
  ("p", "All notices, demands, consents and other communications under this Mortgage shall be in writing and shall be deemed given (a) when delivered personally, (b) one (1) Business Day after deposit with a nationally recognized overnight courier, (c) three (3) Business Days after deposit in the United States mail, certified or registered, return receipt requested, postage prepaid, or (d) when sent by electronic mail, if sent before 5:00 p.m. Eastern time on a Business Day and confirmation of transmission is received, provided that notices of default, acceleration, foreclosure, or any notice under Article 10 must also be delivered by one of the methods described in clauses (a) through (c)."),
  ("p", "Notices to Mortgagor shall be addressed to Palmetto Gateway Partners LLC, 88 Broad Street, Suite 200, Charleston, South Carolina 29401, Attention: Neil Ashford Graydon, Managing Member of Graydon Development Group LLC, with a copy to Cartwright & Lyons LLP, and notices to Mortgagee shall be addressed to Calverley Heritage Bank, 412 Whitaker Street, Savannah, Georgia 31401, Attention: Marcus Prideaux, Senior Vice President \u2014 Commercial Real Estate Lending, with a copy to Fielding, Ashworth & Cole LLP, Charleston, South Carolina, Attention: Catherine Ashworth. Either party may change its notice address by written notice given in accordance with this Section."),
 ]),
 dict(num="13.5", title="Amendments; No Oral Modification", content=[
  ("p", "This Mortgage may not be amended, modified, supplemented or waived, and no provision may be waived, except by a written instrument signed by Mortgagor and Mortgagee (and, if applicable, Guarantor). No course of dealing, course of performance, usage of trade or acceptance of late or partial payment shall amend, modify or waive any provision. Mortgagor acknowledges that no officer, employee or agent of Mortgagee has authority to make any oral modification of this Mortgage."),
 ]),
 dict(num="13.6", title="Successors and Assigns; No Assignment by Mortgagor", content=[
  ("p", "This Mortgage binds and benefits Mortgagor and Mortgagee and their respective heirs, executors, administrators, successors and permitted assigns. Mortgagor may not assign this Mortgage or any interest in the Property or the Loan Documents without Mortgagee\u2019s prior written consent. Mortgagee may assign the Loan and this Mortgage in whole or in part, and may disclose information concerning Mortgagor, Guarantor and the Property to any actual or prospective assignee, participant, servicer, investor or rating agency, subject to customary confidentiality obligations."),
 ]),
 dict(num="13.7", title="Severability; Time of Essence", content=[
  ("p", "If any provision of this Mortgage is held to be invalid, illegal or unenforceable in any respect, that provision shall be enforced to the maximum extent permitted by Applicable Law and the remaining provisions shall remain in full force and effect. Time is of the essence with respect to every obligation of Mortgagor under this Mortgage."),
 ]),
 dict(num="13.8", title="Entire Agreement; Conflicts", content=[
  ("p", "Together with the other Loan Documents, this Mortgage constitutes the entire agreement of the parties with respect to the Property and supersedes all prior or contemporaneous agreements, understandings, negotiations and discussions, whether written or oral, relating to the Property, including the Term Sheet to the extent inconsistent. Mortgagor acknowledges that it has received and reviewed the Term Sheet and that this Mortgage is not materially inconsistent with the Term Sheet."),
 ]),
 dict(num="13.9", title="Counterparts; Electronic Signatures", content=[
  ("p", "This Mortgage may be executed in counterparts, each of which is an original and all of which together constitute one instrument. Delivery of an executed counterpart by PDF or other electronic transmission has the same effect as delivery of an original. Electronic signatures are permitted in accordance with the South Carolina Uniform Electronic Transactions Act, provided that, for purposes of recording, the original executed and acknowledged instrument shall be delivered to the Title Insurer for recording."),
 ]),
 dict(num="13.10", title="Recording; Execution Formalities", content=[
  ("p", "This Mortgage shall be recorded in the RMC Office for Charleston County, South Carolina. Mortgagor shall pay all recording fees and South Carolina deed recording fees (approximately $54,575.00 based on the Loan amount of $14,750,000.00 at $1.85 per $500 of indebtedness), all documentary, intangible or stamp taxes, and all other charges in connection with the recording, filing and registration of this Mortgage and the other Loan Documents. Mortgagor shall execute this Mortgage with the attestation of two (2) subscribing witnesses and shall acknowledge it before a notary public so that this Mortgage is entitled to record under the laws of the State of South Carolina."),
 ]),
 dict(num="13.11", title="No Partnership; No Third-Party Beneficiaries", content=[
  ("p", "Nothing in this Mortgage creates a partnership, joint venture, agency or fiduciary relationship between Mortgagor and Mortgagee, and Mortgagee is not a partner, joint venturer, agent or fiduciary of Mortgagor. Except for Guarantor to the extent of the Guarantor\u2019s Consent and Agreement, no Person other than Mortgagor and Mortgagee is a third-party beneficiary of this Mortgage."),
 ]),
 dict(num="13.12", title="USA PATRIOT Act; Confidentiality", content=[
  ("p", "Mortgagee hereby notifies Mortgagor that, pursuant to the USA PATRIOT Act and applicable customer identification requirements, Mortgagee may be required to obtain, verify and record information that identifies Mortgagor and its beneficial owners, and Mortgagor shall provide such information upon request. Mortgagee shall keep confidential all non-public information concerning Mortgagor and Guarantor, except as required by Applicable Law, regulation, subpoena, or in connection with the enforcement of the Loan Documents or a permitted assignment or participation."),
 ]),
 dict(num="13.13", title="Attorneys\u2019 Fees", content=[
  ("p", "If any action or proceeding is brought to enforce or interpret this Mortgage, the prevailing party shall be entitled to recover its reasonable attorneys\u2019 fees, costs and expenses in addition to any other relief awarded."),
 ]),
 dict(num="13.14", title="Waiver of Homestead and Other Exemptions", content=[
  ("p", "To the extent permitted by Applicable Law, Mortgagor waives all rights of homestead, exemption and moratorium, and any other right or defense that would delay, prevent or impair the enforcement of this Mortgage. Mortgagor acknowledges that, as a limited liability company, it is not entitled to a homestead exemption with respect to the Property."),
 ]),
]))

# ============================================================ EXHIBITS DATA
EXHIBIT_A_NOTE = (
 "The metes and bounds description of Parcel One and Parcel Two shall be the description contained in "
 "Schedule A, Section 4 of Title Commitment No. PT-2025-04-1178, as confirmed by the ALTA/NSPS Land Title Survey "
 "of the Property prepared by Cartwright Land Surveying LLC, dated January 15, 2025 and recorded in Plat Book 64 "
 "at Page 91 in the RMC Office. The surveyor\u2019s metes and bounds description is to be inserted in this Exhibit A "
 "at closing, after certification and re-certification of the survey to a date not more than ninety (90) days "
 "before the Closing Date. The description below is the record description and is controlling for the plat, deed and "
 "tax reference information; the metes and bounds description, when inserted, shall control in the event of conflict "
 "as to boundaries only."
)

BUDGET_ROWS = [
 ["Line", "Category", "Hard Cost", "Soft/Cont.", "Total", "Holdback", "Borrower Eq."],
 ["1.0", "HVAC Replacement", "$1,200,000", "\u2014", "$1,200,000", "$850,000", "$350,000"],
 ["2.0", "Elevator Modernization", "$475,000", "\u2014", "$475,000", "$375,000", "$100,000"],
 ["3.0", "Fa\u00e7ade Restoration", "$625,000", "\u2014", "$625,000", "$425,000", "$200,000"],
 ["4.0", "Tenant Improvement Allowances", "$550,000", "\u2014", "$550,000", "$450,000", "$100,000"],
 ["5.0", "Soft Costs and Contingency", "\u2014", "$300,000", "$300,000", "$150,000", "$150,000"],
 ["", "Total Renovation Budget", "$2,850,000", "$300,000", "$3,150,000", "$2,250,000", "$900,000"],
]

LEASE_ROWS = [
 ["Unit", "Tenant", "RSF", "Type", "Rent/RSF", "Annual Rent", "Expiry", "Deposit"],
 ["Bay 1", "Lowcountry Provisions Inc.", "3,800", "NNN", "$28.50", "$108,300", "12/31/27", "$18,050"],
 ["Bay 2", "Vacant (H&W ROFR)", "3,800", "\u2014", "\u2014", "\u2014", "\u2014", "\u2014"],
 ["Bay 3", "Harmon & Wren Design Studio LLC", "3,800", "Mod. Gross", "$24.00", "$91,200", "06/30/26", "$15,200"],
 ["Suite A", "Tidemark Consulting Group LLC", "9,800", "NNN", "$22.00", "$215,600", "03/31/29", "$35,933"],
 ["Suite B", "Vacant", "9,800", "\u2014", "\u2014", "\u2014", "\u2014", "\u2014"],
 ["Total", "3 of 5 units occupied (17,400 RSF; 56.13%)", "31,000", "", "", "$415,100", "", "$69,183"],
]

EXC_ROWS = [
 ["No.", "Exception", "Source", "Treatment / Endorsement"],
 ["1", "Standard printed exceptions (gap; inspection and inquiry; survey matters; mechanics\u2019 liens); subitems (b)\u2013(e) to be deleted", "Sch. B-II, Pt. 1", "Delete (b), (c), (d), (e) on delivery of ALTA Survey, owner\u2019s affidavit and lien waivers; address gap by gap indemnity or disbursement"],
 ["2", "Real property taxes for 2025 and subsequent years on T.M. 460-12-04-007, -008, -009, not yet due and payable", "Sch. B-II", "Permitted; escrowed under Section 6.2; confirm Charleston County reassessment exposure"],
 ["3", "Utility easement in favor of South Carolina Electric & Gas (underground lines), Deed Book 987, Page 112, affecting westerly boundary of Lot 9", "Sch. B-II", "Permitted; survey to confirm no encroachment conflict"],
 ["4", "SCDHEC land use restriction (CREC \u2014 Lot 7), Deed Book 1203, Page 89, Site ID SC-29403-0772; prohibits residential use of Lot 7 ground floor and requires vapor barrier maintenance and periodic inspection", "Sch. B-II", "Permitted; cannot be removed. Specific covenants in Sections 7.3 and 7.4; Event of Default in Section 10.1(k)"],
 ["5", "Balcony encroachment approx. 2.5 ft over King Street right-of-way, per ALTA Survey (Cartwright Land Surveying LLC, 1/15/2025)", "Sch. B-II", "Permitted; ALTA Endorsement 28.1 (encroachments) required; evidence of City encroachment license required under Section 7.6"],
 ["6", "Rights of tenants under existing leases (Lowcountry Provisions, Harmon & Wren, Tidemark), as tenants only, without purchase option or right of first refusal on the Property", "Sch. B-II", "Permitted; estoppels and SNDAs required under Sections 5.7 and 5.8"],
 ["7", "Matters shown on plat recorded in Plat Book 41, Page 218 (setback lines, rights-of-way, drainage easements, notations)", "Sch. B-II", "Permitted; survey to confirm compliance with setback lines"],
 ["8", "Coverage qualification or endorsement limiting coverage on Parcel Two (vacated Anson Lane strip, quitclaim conveyance)", "Vesting deed notes", "NOT permitted unless affirmatively approved by Mortgagee in writing. Mortgagee requires fee simple coverage on Parcel Two without diminution; ALTA 34 (identified exception) or equivalent affirmative coverage required"],
]

RESERVE_ROWS = [
 ["Reserve", "Amount / Basis", "Timing", "Section"],
 ["Tax and Insurance Escrow", "1/12 of estimated annual taxes and casualty/liability premiums (all 3 parcels)", "Monthly, each Payment Date", "6.2"],
 ["Capital Replacement Reserve", "$645.83 per month ($0.25/RSF/yr \u00d7 31,000 RSF \u00f7 12)", "Monthly, each Payment Date", "6.3"],
 ["Tenant Improvement / Leasing Commission Reserve", "$150,000.00, replenished within 30 days of demand", "At closing, and on demand", "6.4"],
 ["Renovation Holdback", "$2,250,000.00 (draw basis; 10% retainage until Substantial Completion)", "Monthly draws, maximum 14 draws", "9.1\u20139.4"],
]

# ============================================================ RENDERER
def render_front_matter(doc):
    para(doc, "MORTGAGE AND SECURITY AGREEMENT", size=16, bold=True, align="center", space_before=36, space_after=4)
    para(doc, "(With Absolute Assignment of Leases, Rents and Profits;", size=11, align="center", space_after=0)
    para(doc, "Security Agreement; and Fixture Filing)", size=11, align="center", space_after=18)
    hr(doc)
    para(doc, "by and from", size=11, align="center", space_before=10, space_after=6)
    para(doc, "PALMETTO GATEWAY PARTNERS LLC,", size=12, bold=True, align="center", space_after=0)
    para(doc, "a South Carolina limited liability company,", size=11, align="center", space_after=4)
    para(doc, "as Mortgagor,", size=11, italic=True, align="center", space_after=14)
    para(doc, "to and in favor of", size=11, align="center", space_after=6)
    para(doc, "CALVERLEY HERITAGE BANK,", size=12, bold=True, align="center", space_after=0)
    para(doc, "a Georgia state-chartered commercial bank,", size=11, align="center", space_after=4)
    para(doc, "as Mortgagee", size=11, italic=True, align="center", space_after=16)
    hr(doc)
    para(doc, "Dated as of April 15, 2025", size=11, bold=True, align="center", space_before=8, space_after=10)
    rows = [
        ["Loan No.", "CHB CRE Loan No. 2025-CHS-0047"],
        ["Principal Amount", "$14,750,000.00"],
        ["Property", "520\u2013534 King Street, Charleston, South Carolina 29403"],
        ["Tax Map Nos.", "460-12-04-007, 460-12-04-008 and 460-12-04-009 (Charleston County)"],
        ["Title Commitment", "PT-2025-04-1178 (effective February 28, 2025)"],
        ["Recording", "Office of the Register of Mesne Conveyances, Charleston County, S.C."],
    ]
    table(doc, rows, widths=[1.7, 4.6], header=False, size=9.5, bold_first_col=True)
    para(doc, "", space_after=10)
    para(doc, "This instrument was prepared by:", size=9.5, align="center", space_before=8, space_after=0)
    para(doc, "FIELDSING, ASHWORTH & COLE LLP".replace("FIELDSING", "FIELDING"), size=9.5, align="center", space_after=0)
    para(doc, "Attorneys at Law \u2022 Charleston, South Carolina and Savannah, Georgia", size=9.5, align="center", space_after=12)
    p = para(doc, "", space_before=6, space_after=0)
    rich(doc, [("NOTICE REGARDING FORECLOSURE:  ", True, False),
               ("South Carolina is a judicial foreclosure jurisdiction. This Mortgage grants no power of sale. "
                "Mortgagee\u2019s foreclosure remedy is exercisable only by judicial action in the courts of the State of "
                "South Carolina. See Section 11.2.", False, False)], size=9.5)
    page_break(doc)


def render_toc(doc):
    para(doc, "TABLE OF CONTENTS", size=12, bold=True, align="center", space_before=0, space_after=14)
    for a in ARTICLES:
        toc_line(doc, "ARTICLE %s" % a["num"], a["title"].upper(), left=0.95, bold=True,
                 size=10, space_before=6, space_after=2)
        for sec in a["sections"]:
            toc_line(doc, "Section %s" % sec["num"], sec["title"], left=1.55,
                     size=9.5, space_before=0, space_after=1)
    rich(doc, [("Signature Pages", True, False)], align="left", size=10, space_before=6, space_after=1)
    rich(doc, [("Guarantor\u2019s Consent and Agreement", True, False)], align="left", size=10, space_before=0, space_after=1)
    for ex in ["A \u2014 Legal Description", "B \u2014 Renovation Budget, Sources and Allocation",
               "C \u2014 Permitted Exceptions and Required Title Endorsements",
               "D \u2014 Schedule of Leases and Rent Roll",
               "E \u2014 Environmental Institutional Controls (LUR) and Compliance Protocol",
               "F \u2014 Reserve and Escrow Schedule"]:
        rich(doc, [("Exhibit ", True, False), (ex, False, False)], align="left", size=10, space_before=0, space_after=1)
    page_break(doc)


def render_body(doc):
    # Preamble and recitals
    rich(doc, [("THIS MORTGAGE AND SECURITY AGREEMENT", True, False),
               (" (this \u201cMortgage\u201d) is made and entered into as of April 15, 2025, by and from ", False, False),
               ("PALMETTO GATEWAY PARTNERS LLC", True, False),
               (", a South Carolina limited liability company, having its principal office at 88 Broad Street, Suite 200, "
                "Charleston, South Carolina 29401 (the \u201cMortgagor\u201d), to and in favor of ", False, False),
               ("CALVERLEY HERITAGE BANK", True, False),
               (", a Georgia state-chartered commercial bank, having its principal office at 412 Whitaker Street, Savannah, "
                "Georgia 31401 (the \u201cMortgagee\u201d).", False, False)], space_before=0)
    para(doc, "RECITALS", size=11, bold=True, align="center", space_before=6, space_after=6)
    rec = [
        ("A.", "Mortgagor has requested that Mortgagee make a loan to Mortgagor in the principal amount of $14,750,000.00 (the \u201cLoan\u201d), and Mortgagee has agreed to make the Loan on the terms and subject to the conditions set forth in the executed Term Sheet dated April 1, 2025 for CHB CRE Loan No. 2025-CHS-0047, a Promissory Note of even date herewith in the stated principal amount (the \u201cNote\u201d), and the other Loan Documents."),
        ("B.", "The Loan is disbursed in two components: an Initial Advance of $12,500,000.00 at closing, and a Renovation Holdback of $2,250,000.00 retained by Mortgagee and advanced on a draw basis for the renovation of the Property."),
        ("C.", "The proceeds of the Loan are used to finance the acquisition of the Property for a purchase price of $17,800,000.00 and the renovation of the Property at a budgeted cost of $3,150,000.00, for a total project cost of $20,950,000.00, funded by the Loan and a $6,200,000.00 equity contribution by Mortgagor\u2019s members."),
        ("D.", "As a condition to making the Loan, Mortgagee requires that Mortgagor execute and deliver this Mortgage, which grants to Mortgagee a first-priority mortgage lien on and security interest in the Property, an absolute and present assignment of all Leases, Rents and profits, a security interest in all personal property and fixtures, and a fixture filing, and which contains the covenants, representations and remedies on which Mortgagee is relying."),
        ("E.", "Guarantor has executed and delivered the Guaranty, and Mortgagor and Guarantor have executed and delivered the Environmental Indemnity Agreement, each of even date herewith."),
    ]
    for lbl, txt in rec:
        rich(doc, [(lbl + "  ", True, False), (txt, False, False)], left=0.35, first=-0.35)
    rich(doc, [("NOW, THEREFORE", True, False),
               (", for and in consideration of the sum of Ten Dollars ($10.00) and other good and valuable consideration, "
                "the receipt and sufficiency of which are hereby acknowledged, and to secure the payment and performance "
                "of the Indebtedness, Mortgagor agrees, covenants, represents, warrants, grants, mortgages and assigns as "
                "follows:", False, False)], space_before=6)

    for a in ARTICLES:
        article_heading(doc, a["num"], a["title"])
        for s in a["sections"]:
            first = True
            for item in s["content"]:
                kind = item[0]
                if kind == "p":
                    if first:
                        section(doc, s["num"], s["title"], item[1]); first = False
                    else:
                        para(doc, item[1])
                elif kind == "sub":
                    if first:
                        section(doc, s["num"], s["title"]); first = False
                    sub(doc, item[1], item[2], level=1)
                elif kind == "sub2":
                    if first:
                        section(doc, s["num"], s["title"]); first = False
                    sub(doc, item[1], item[2], level=2)
                elif kind == "def":
                    term, definition = item[1], item[2]
                    rich(doc, [("\u201c" + term + "\u201d ", True, False), (definition, False, False)],
                         left=0.5, first=-0.25, space_after=4)
            if first:
                section(doc, s["num"], s["title"])


def render_signatures(doc):
    page_break(doc)
    para(doc, "SIGNATURE PAGE", size=11, bold=True, align="center", space_before=0, space_after=12)
    rich(doc, [("IN WITNESS WHEREOF", True, False),
               (", Mortgagor has executed this Mortgage and Security Agreement as of the date first written above, and has "
                "caused this Mortgage to be attested by two (2) subscribing witnesses and acknowledged before a notary public "
                "so that it is entitled to record in the Office of the Register of Mesne Conveyances for Charleston County, "
                "South Carolina.", False, False)])
    para(doc, "", space_after=10)
    para(doc, "MORTGAGOR:", size=11, bold=True, align="left", space_after=6)
    para(doc, "PALMETTO GATEWAY PARTNERS LLC,", size=11, bold=True, align="left", space_after=0)
    para(doc, "a South Carolina limited liability company", size=11, align="left", space_after=14)
    para(doc, "By:  GRAYDON DEVELOPMENT GROUP LLC,", size=11, align="left", space_after=0)
    para(doc, "      a South Carolina limited liability company,", size=11, align="left", space_after=0)
    para(doc, "      its Managing Member", size=11, align="left", space_after=26)
    para(doc, "_______________________________________", size=11, align="left", space_after=0)
    para(doc, "Neil Ashford Graydon, Managing Member of", size=11, align="left", space_after=0)
    para(doc, "Graydon Development Group LLC", size=11, align="left", space_after=18)
    # witnesses
    para(doc, "ATTEST (two subscribing witnesses required under S.C. Code Ann. \u00a7 30-5-30):", size=10, bold=True, align="left", space_after=14)
    t = doc.add_table(rows=3, cols=2)
    t.autofit = False
    cells = [("_________________________________", "Witness #1"), ("_________________________________", "Witness #2")]
    for ci, (line, lbl) in enumerate(cells):
        c = t.cell(0, ci); c.text = ""
        c.paragraphs[0].paragraph_format.space_after = Pt(0)
        c.paragraphs[0].runs and None
        from docxstyle import _set_font as sf
        sf(c.paragraphs[0].add_run(line), size=10)
        c2 = t.cell(1, ci); c2.text = ""
        sf(c2.paragraphs[0].add_run(lbl), size=10)
    for ci, w in enumerate([3.1, 3.1]):
        for ri in range(3):
            t.cell(ri, ci).width = Inches(w)
    para(doc, "", space_after=8)
    # notary
    para(doc, "STATE OF SOUTH CAROLINA", size=10.5, align="left", space_after=0)
    para(doc, "COUNTY OF CHARLESTON", size=10.5, align="left", space_after=8)
    rich(doc, [("I, the undersigned Notary Public, do hereby certify that ", False, False),
               ("Neil Ashford Graydon", True, False),
               (", as Managing Member of Graydon Development Group LLC, the Managing Member of Palmetto Gateway Partners LLC, "
                "personally appeared before me this _____ day of April, 2025, and acknowledged the foregoing instrument to be "
                "the act and deed of Palmetto Gateway Partners LLC, and that he was authorized to execute the same on behalf of "
                "such limited liability company.", False, False)], size=10.5)
    para(doc, "SWORN to and subscribed before me:", size=10.5, align="left", space_before=6, space_after=18)
    para(doc, "_______________________________________", size=10.5, align="left", space_after=0)
    para(doc, "Notary Public for South Carolina", size=10.5, align="left", space_after=0)
    para(doc, "My commission expires: ____________________", size=10.5, align="left", space_after=0)
    para(doc, "(Notarial Seal)", size=9, italic=True, align="left", space_after=6)

    # Guarantor consent
    page_break(doc)
    para(doc, "GUARANTOR\u2019S CONSENT AND AGREEMENT", size=11, bold=True, align="center", space_before=0, space_after=12)
    rich(doc, [("The undersigned, ", False, False), ("Neil Ashford Graydon", True, False),
               (" (\u201cGuarantor\u201d), is the sole member and sole manager of Graydon Development Group LLC, the Managing "
                "Member and 72% owner of Palmetto Gateway Partners LLC (the \u201cMortgagor\u201d), and has executed and delivered "
                "the Guaranty Agreement and the Environmental Indemnity Agreement of even date herewith. As a material "
                "inducement to Mortgagee to make the Loan, and for other good and valuable consideration, Guarantor, intending "
                "to be legally bound, agrees as follows:", False, False)])
    cons = [
        ("(a)", "Guarantor consents to the terms of the foregoing Mortgage and agrees not to take any action, and not to cause or permit Graydon Development Group LLC or Mortgagor to take any action, that would breach any provision of Article 5, Section 7.4, Section 7.5, Section 8.2 or Section 8.3 of the Mortgage, including any Transfer of Guarantor\u2019s direct or indirect interest in Graydon Development Group LLC, any dissolution, or any bankruptcy filing by Mortgagor without the affirmative vote of the independent manager and Mortgagee\u2019s prior written consent."),
        ("(b)", "Guarantor acknowledges and agrees that a breach of Section 7.4 (Institutional Controls; LUR and Vapor Barrier) or any carve-out event described in Section 12.3 constitutes an event for which Guarantor is liable under the Guaranty, and that Guarantor\u2019s obligations under the Guaranty and the Environmental Indemnity Agreement are independent of, and not released by, any foreclosure, deed in lieu, or acceptance of a deed in lieu by Mortgagee."),
        ("(c)", "Guarantor acknowledges receipt of true and complete copies of the Phase I Environmental Site Assessment (Report No. CLR-2025-0119, dated January 28, 2025), the recorded Land Use Restriction (Deed Book 1203, Page 89), the Term Sheet, the Note and the Mortgage, and understands the obligation to maintain and periodically inspect the Vapor Barrier and the prohibition on residential use of the ground floor of Lot 7."),
        ("(d)", "Guarantor agrees to furnish the annual personal financial statement required by Section 7.7(b) of the Mortgage and to give the notices required by Section 7.11(f) and (g) with respect to himself."),
        ("(e)", "Guarantor submits to the jurisdiction and venue provisions of Sections 13.1 through 13.3 of the Mortgage, including the waiver of jury trial, all of which apply to Guarantor."),
    ]
    for lbl, txt in cons:
        rich(doc, [(lbl + "\u2003", False, False), (txt, False, False)], left=0.5, first=-0.4)
    para(doc, "", space_after=12)
    para(doc, "GUARANTOR:", size=11, bold=True, align="left", space_after=30)
    para(doc, "_______________________________________", size=11, align="left", space_after=0)
    para(doc, "Neil Ashford Graydon, individually", size=11, align="left", space_after=0)
    para(doc, "14 Church Street, Charleston, South Carolina 29401", size=10, align="left", space_after=16)
    para(doc, "Date: ___________________________", size=10, align="left", space_after=0)


def render_exhibits(doc):
    # EXHIBIT A
    page_break(doc)
    para(doc, "EXHIBIT A", size=12, bold=True, align="center", space_before=0, space_after=2)
    para(doc, "LEGAL DESCRIPTION", size=11, bold=True, align="center", space_after=12)
    para(doc, "PARCEL ONE", size=11, bold=True, align="left", space_after=4)
    para(doc, "ALL that certain piece, parcel or lot of land, together with the improvements thereon, situate, lying and being in the City of Charleston, County of Charleston, State of South Carolina, being shown and designated as Lots 7, 8 and 9 of the Hampstead Village Plat, as recorded in Plat Book 41 at Page 218, in the Office of the Register of Mesne Conveyances (the \u201cRMC Office\u201d) for Charleston County, South Carolina, and having such shapes, metes, bounds and measurements as are shown on said plat, reference to which is hereby made for a more complete and accurate description thereof.", space_after=6)
    para(doc, "Being commonly known as 520\u2013534 King Street, Charleston, South Carolina 29403.", space_after=4)
    para(doc, "Tax Map Nos. 460-12-04-007 (Lot 7), 460-12-04-008 (Lot 8) and 460-12-04-009 (Lot 9).", space_after=12)
    para(doc, "PARCEL TWO", size=11, bold=True, align="left", space_after=4)
    para(doc, "TOGETHER WITH that certain strip or parcel of land formerly constituting a portion of Anson Lane, a public street, which was vacated and closed by the City of Charleston pursuant to Ordinance No. 2019-084, and conveyed to Mortgagor\u2019s predecessor in title by that certain Quitclaim Deed recorded in Deed Book 1128 at Page 443 in the RMC Office for Charleston County, South Carolina, said strip being adjacent to and contiguous with Lot 7 of the Hampstead Village Plat, and being more particularly described and shown on the plat prepared by Cartwright Land Surveying LLC dated January 15, 2025, recorded in Plat Book 64 at Page 91 in the RMC Office for Charleston County, South Carolina.", space_after=10)
    para(doc, "BEING the same property conveyed to Mortgagor by General Warranty Deed from Hampstead Village Holdings LLC, a South Carolina limited liability company, recorded simultaneously herewith in the RMC Office for Charleston County, South Carolina.", space_after=12)
    para(doc, "Note Regarding Metes and Bounds.", size=10, bold=True, align="left", space_after=2)
    para(doc, EXHIBIT_A_NOTE, size=10, space_after=12)
    rows = [["Parcel", "Tax Map No.", "Source of Title", "Area"],
            ["Parcel One", "460-12-04-007 / -008 / -009", "General Warranty Deed, Deed Book 1095, Page 322 (as part of acquisition deed)", "0.38 ac / \u00b116,553 SF"],
            ["Parcel Two", "Portion of Tax Map No. 460-12-04-007", "Quitclaim Deed, Deed Book 1128, Page 443 (Ordinance 2019-084)", "Strip adjacent to Lot 7"],
            ["Total assemblage", "Three parcels plus vacated right-of-way", "See Title Commitment PT-2025-04-1178, Schedule A", "31,000 SF GBA"]]
    table(doc, rows, widths=[0.95, 1.55, 2.4, 1.5], size=8.5)

    # EXHIBIT B
    page_break(doc)
    para(doc, "EXHIBIT B", size=12, bold=True, align="center", space_before=0, space_after=2)
    para(doc, "RENOVATION BUDGET, SOURCES AND ALLOCATION", size=11, bold=True, align="center", space_after=10)
    para(doc, "The Renovation Budget for the Property is $3,150,000.00, allocated between the Renovation Holdback ($2,250,000.00) and Mortgagor\u2019s equity ($900,000.00), as follows:", space_after=8)
    table(doc, BUDGET_ROWS, widths=[0.4, 1.55, 0.8, 0.9, 0.85, 0.9, 0.95], size=8)
    para(doc, "", space_after=6)
    rows2 = [["Budget Component", "Amount"],
             ["Hard costs within the Renovation Contract (Beaufort Builders Group LLC, SC-GC-47921): items 1.0\u20134.0", "$2,850,000"],
             ["Soft costs and contingency outside the Renovation Contract: item 5.0", "$300,000"],
             ["Total Renovation Budget", "$3,150,000"],
             ["Lender Renovation Holdback (from Loan proceeds)", "$2,250,000"],
             ["Mortgagor equity required for renovation", "$900,000"]]
    table(doc, rows2, widths=[5.4, 1.1], size=8.5)
    para(doc, "", space_after=6)
    para(doc, "Note. The Renovation Contract sum of $2,850,000.00 exceeds the Renovation Holdback of $2,250,000.00 by $600,000.00. Mortgagor is solely responsible for the $900,000.00 equity portion and for all cost overruns under Section 9.6. The draw schedule used for planning purposes contemplates fourteen (14) monthly draws over the fourteen (14) month renovation period ending at Substantial Completion on June 15, 2026; that schedule is illustrative only, does not model the ten percent (10%) Retainage required by Section 9.4, and does not amend this Exhibit. Disbursements are governed exclusively by Article 9.", size=9, space_after=6)
    para(doc, "Line-item amounts in this Exhibit are controlling over any line-item amounts in any draw schedule where the two differ. In the event of any discrepancy between the aggregate Renovation Budget stated here ($3,150,000.00) and the aggregate of any draw schedule, the amounts in this Exhibit control.", size=9, space_after=6)

    # EXHIBIT C
    page_break(doc)
    para(doc, "EXHIBIT C", size=12, bold=True, align="center", space_before=0, space_after=2)
    para(doc, "PERMITTED EXCEPTIONS AND REQUIRED TITLE ENDORSEMENTS", size=11, bold=True, align="center", space_after=10)
    para(doc, "The Permitted Exceptions are the matters identified in Schedule B, Part II of Title Commitment No. PT-2025-04-1178 (effective February 28, 2025, expiring August 28, 2025), as approved by Mortgagee in writing, as summarized below. Items 1(b), (c), (d) and (e) are to be deleted prior to or at closing upon satisfaction of the requirements of Schedule B, Part I.", space_after=8)
    table(doc, EXC_ROWS, widths=[0.4, 2.6, 0.95, 2.55], size=8)
    para(doc, "", space_after=8)
    para(doc, "Required Title Endorsements.", size=10, bold=True, align="left", space_after=4)
    rows = [["Endorsement", "Purpose"],
            ["ALTA 3.1 (Zoning)", "Confirms GB (General Business) zoning and permitted use"],
            ["ALTA 4 / 4.1 (Condominium/Planned Unit)", "As applicable; confirm inapplicability in writing"],
            ["ALTA 9 (Restrictions, Encroachments, Minerals)", "Covenants and restrictions, including the LUR"],
            ["ALTA 14 / 14.1\u201314.3 (Future Advances)", "Priority for Renovation Holdback future advances (Article 9)"],
            ["ALTA 17 / 17.1 (Access)", "Confirms legal and physical access, including rear access across Parcel Two"],
            ["ALTA 18 (Map/Plat) and ALTA 22 (Location)", "Location of Improvements per ALTA Survey"],
            ["ALTA 19 / 19.1 (Contiguity)", "Confirms contiguity of Lots 7, 8, 9 and the Anson Lane strip"],
            ["ALTA 28.1 / 28 (Encroachments \u2014 Easements and Boundaries)", "Affirmative coverage for balcony encroachment (Exception 5)"],
            ["ALTA 34 (Identified Exception \u2014 Parcel Two) or equivalent affirmative coverage", "Coverage for the quitclaim chain of title to Parcel Two"],
            ["ALTA 33 (Construction Loan \u2014 Disbursements) or equivalent", "Construction-phase coverage consistent with Article 9"]]
    table(doc, rows, widths=[2.9, 3.6], size=8.5)

    # EXHIBIT D
    page_break(doc)
    para(doc, "EXHIBIT D", size=12, bold=True, align="center", space_before=0, space_after=2)
    para(doc, "SCHEDULE OF LEASES AND RENT ROLL", size=11, bold=True, align="center", space_after=6)
    para(doc, "Rent roll as of the Closing Date. Gross building area: 31,000 RSF. Occupied: 17,400 RSF (56.13%). Vacant: 13,600 RSF (43.87%).", size=9, italic=True, align="center", space_after=8)
    table(doc, LEASE_ROWS, widths=[0.5, 1.45, 0.45, 0.72, 0.6, 0.72, 0.72, 0.62], size=8)
    para(doc, "", space_after=6)
    notes = [
        "Bay 1 \u2014 Lowcountry Provisions Inc. (SC corporation). NNN lease, 5-year term, expiration 12/31/2027. Rent escalates 3.0% each January 1 beginning 1/1/2025 (escalated rate $29.36/RSF; $111,549 annually). One 5-year renewal option at fair market value with a floor at then-current rent; notice due 3/31/2027. Exclusive specialty-grocery use. NO assignment, subletting, subordination, non-disturbance or estoppel provision. See Sections 5.7 and 5.8.",
        "Bay 2 \u2014 Vacant, 3,800 RSF. Subject to the right of first refusal of Harmon & Wren Design Studio LLC (15 business days; survives renewal). See Section 5.5.",
        "Bay 3 \u2014 Harmon & Wren Design Studio LLC (SC LLC). Modified gross lease, expiration 6/30/2026; rent escalates 2.5% each July 1 (7/1/2025 rate $25.85/RSF). One 3-year renewal option at 95% of fair market value; notice due 12/31/2025. Early termination right effective 6/30/2025 required notice by 12/31/2024 and was not exercised. Lease is subordinate to future mortgages conditioned on a commercially reasonable non-disturbance agreement; estoppel required within 15 business days of request.",
        "Suite A \u2014 Tidemark Consulting Group LLC (Delaware LLC registered in SC). NNN lease, expiration 3/31/2029; 2.5% escalation each April 1 beginning 4/1/2026. Two 3-year renewal options; first notice due 3/31/2028. Assignment requires Landlord\u2019s consent in its sole discretion; Tenant agrees to execute an SNDA upon request; estoppel within 10 business days.",
        "Suite B \u2014 Vacant, 9,800 RSF. Lease-up cannot meaningfully commence until Substantial Completion; tenant improvement allowance funded from Renovation Budget item 4.0 and the Tenant Improvement/Leasing Commission Reserve.",
        "No memorandum of lease has been recorded for any Lease. No Tenant holds an option to purchase or a right of first refusal to purchase the Property.",
    ]
    for n in notes:
        rich(doc, [("\u2022  ", False, False), (n, False, False)], size=8.5, left=0.25, first=-0.25, space_after=4)

    # EXHIBIT E
    page_break(doc)
    para(doc, "EXHIBIT E", size=12, bold=True, align="center", space_before=0, space_after=2)
    para(doc, "ENVIRONMENTAL INSTITUTIONAL CONTROLS (LUR) AND COMPLIANCE PROTOCOL", size=11, bold=True, align="center", space_after=10)
    rows = [["Item", "Detail"],
            ["Site", "SCDHEC Site ID SC-29403-0772 (source: former dry cleaning operation, 518 King Street)"],
            ["Regulatory status", "No Further Action determination dated August 12, 2021; conditional on continued compliance with institutional controls"],
            ["Recorded instrument", "Land Use Restriction recorded in Deed Book 1203 at Page 89, RMC Office for Charleston County; runs with the land"],
            ["Affected area", "Ground floor of Lot 7 (Tax Map No. 460-12-04-007), known as Bay 1, 520 King Street (approx. 3,800 RSF)"],
            ["Restriction (1)", "No residential use of the ground floor of Lot 7"],
            ["Restriction (2)", "Maintain, and periodically inspect, the vapor barrier beneath the concrete slab of Bay 1"],
            ["Current use", "Specialty grocery (Lowcountry Provisions Inc.), a commercial use consistent with the restriction"],
            ["Removal", "Cannot be removed or modified without SCDHEC approval and Mortgagee\u2019s prior written consent"],
            ["Title treatment", "Schedule B-II Exception 4; not removable"],
            ["Phase I reference", "Clearfield Environmental Consulting LLC, Report No. CLR-2025-0119, dated January 28, 2025 (CREC; no RECs; no HRECs)"]]
    table(doc, rows, widths=[1.35, 5.15], size=8.5)
    para(doc, "", space_after=8)
    para(doc, "Compliance Protocol (Section 7.4)", size=10, bold=True, align="left", space_after=4)
    rows = [["Requirement", "Frequency", "Deliverable to Mortgagee"],
            ["Vapor barrier inspection by SC-licensed environmental professional", "Annually, and before/after any work affecting the Bay 1 slab", "Written inspection report within 30 days"],
            ["Compliance certificate (vapor barrier intact; no residential use)", "With each inspection report", "Executed certificate"],
            ["SCDHEC notification and approval before any Bay 1 slab penetration", "Before each such work", "Copy of notice and approval, at least 10 Business Days in advance"],
            ["Contractor/subcontractor acknowledgment of vapor barrier and LUR", "Before commencement of relevant work", "Signed acknowledgments"],
            ["Reporting of SCDHEC inquiries, notices or determinations", "Within 3 Business Days", "Written notice with copies"],
            ["Lease restriction prohibiting residential use of Bay 1", "Each Lease of that space", "Copy of Lease under Section 7.7(e)"]]
    table(doc, rows, widths=[2.5, 1.7, 2.3], size=8.5)
    para(doc, "", space_after=6)
    para(doc, "Page References. This Exhibit summarizes, and does not modify, the LUR. In the event of any conflict between this Exhibit and the LUR, the LUR controls, and Mortgagor shall comply with the LUR. A breach of any requirement in this Exhibit or in Section 7.4 is an Event of Default under Section 10.1(k), subject to the cure period in Section 10.2(c).", size=9)

    # EXHIBIT F
    page_break(doc)
    para(doc, "EXHIBIT F", size=12, bold=True, align="center", space_before=0, space_after=2)
    para(doc, "RESERVE AND ESCROW SCHEDULE", size=11, bold=True, align="center", space_after=10)
    table(doc, RESERVE_ROWS, widths=[1.85, 2.55, 1.35, 0.75], size=8.5)
    para(doc, "", space_after=8)
    para(doc, "All Reserve Funds are pledged to Mortgagee under Section 6.5 and are subject to Mortgagee\u2019s security interest. Reserve amounts may be adjusted by Mortgagee as provided in Article 6. The Tenant Improvement and Leasing Commission Reserve ($150,000.00) is a separate funding source from, and is in addition to, the Tenant Improvement Allowances line item ($550,000.00) of the Renovation Budget set forth in Exhibit B.", size=9)


def main():
    doc = new_document()
    doc.sections[0].different_first_page_header_footer = True
    header(doc, "Mortgage and Security Agreement \u2014 CHB CRE Loan No. 2025-CHS-0047")
    footer(doc, "CHB CRE Loan No. 2025-CHS-0047 \u2014 Mortgage and Security Agreement", size=7.5)
    render_front_matter(doc)
    render_toc(doc)
    render_body(doc)
    render_signatures(doc)
    render_exhibits(doc)
    out = "/workspace/output/mortgage-and-security-agreement.docx"
    doc.save(out)
    print("wrote", out)

if __name__ == "__main__":
    main()
