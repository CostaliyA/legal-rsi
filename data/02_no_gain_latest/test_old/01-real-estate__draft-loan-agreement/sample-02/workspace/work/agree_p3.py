# -*- coding: utf-8 -*-
import sys; sys.path.insert(0,'/workspace/work')
from dh import *
from docx.enum.text import WD_ALIGN_PARAGRAPH as AL

def build_part3(doc):
    art(doc, "ARTICLE III — CONDITIONS PRECEDENT TO CLOSING")
    para(doc, "Lender's obligation to make the Initial Advance is subject to the satisfaction (or written waiver by Lender) of "
              "each of the following conditions, each in form and substance satisfactory to Lender and its counsel:")

    sec_h(doc, "Section 3.1  Loan Documents")
    para(doc, "Borrower and each Guarantor, as applicable, shall have executed and delivered each of the Loan Documents, "
              "including this Agreement, the Note, the Deed of Trust, the Assignment of Leases and Rents, the Security "
              "Agreement, the Assignments of the Construction Contract and the Architect's Agreement, the Collateral Assignment "
              "of Insurance Proceeds and Condemnation Awards, the Membership Interest Pledges, the Guaranties, the Environmental "
              "Indemnity and the Intercreditor Agreement, together with all UCC financing statements, fixture filings and other "
              "instruments necessary to perfect Lender's security interests.")

    sec_h(doc, "Section 3.2  Due Diligence Reports")
    para(doc, "Lender shall have received and approved (a) the appraisal of the Property prepared by Ridgeline Appraisal "
              "Services Inc. dated November 15, 2024, confirming an as-is land value of not less than $8,900,000, an as-completed "
              "value of not less than $72,800,000 and an as-stabilized value of not less than $76,200,000, together with "
              "Lender's internal appraisal review and a FIRREA-compliant evaluation; (b) the Phase I ESA; (c) the Phase II ESA; "
              "(d) the NFA Letter; (e) a geotechnical report from Carolina Geotechnical Associates acceptable to Lender; and "
              "(f) an updated market study or rent survey if requested by Lender. If the Closing Date occurs after April 26, "
              "2025, Borrower shall deliver an updated Phase I ESA satisfying 40 C.F.R. \u00a7 312.20(c) at its expense.")

    sec_h(doc, "Section 3.3  Title Insurance")
    para(doc, "The Title Company shall have issued a pro forma Title Policy, in the amount of the Loan Amount, insuring the "
              "Deed of Trust as a valid first priority lien on the fee simple estate in the Property, subject only to the "
              "Permitted Exceptions, and shall have committed to issue at Closing such endorsements as Lender may require, "
              "including an ALTA 9 series (restrictions, encroachments and minerals) endorsement, access and contiguity "
              "endorsements, a survey endorsement, a zoning 3.0 endorsement (if available), a variable rate endorsement and an "
              "environmental protection lien endorsement. The Title Policy shall contain no exception for any mechanics' or "
              "materialmen's lien, for the deed of trust described in Section 3.14, or for the matters identified in Schedule 3 "
              "as matters to be released at Closing.")

    sec_h(doc, "Section 3.4  Survey")
    para(doc, "Lender shall have received an ALTA/NSPS Land Title Survey of the Property, dated or re-certified not more than "
              "ninety (90) days prior to the Closing Date, prepared by a surveyor licensed in North Carolina, certified to "
              "Lender, Borrower and the Title Company, meeting the 2021 ALTA/NSPS Minimum Standard Detail Requirements and "
              "including Table A items 1, 2, 4, 6, 8, 9, 11, 13 and 14 and such other optional items as Lender may require. The "
              "survey shall depict (a) the legal description of each parcel and the aggregate acreage, (b) the Duke Energy "
              "Carolinas easement and the City of Durham stormwater management easement, (c) the Affected Area by metes and "
              "bounds or by reference to the recorded deed notice, and (d) the building footprint and the relationship of the "
              "Affected Area to the proposed residential floors. [Drafting Note: The Phase I ESA description of the parcels "
              "(1.89 and 1.58 acres; western and eastern parcels; frontage on Foster Street to the north) is inconsistent with "
              "the metes and bounds legal descriptions in the Title Commitment (2.09 and 1.38 acres; north and south parcels; "
              "Foster Street along the western boundary), which See Cover Memorandum "
              "Issue No. 7.]")

    sec_h(doc, "Section 3.5  Environmental Conditions")
    para(doc, "Without limiting Section 3.2, Lender shall have received and approved:")
    for x in [
        "the NFA Letter in full, together with NCDEQ's written confirmation of the then-current compliance status of Site ID "
        "IHSB-24-1203, and evidence that each condition of the NFA Letter other than the installation of the Vapor Mitigation "
        "System has been satisfied or is not yet due;",
        "evidence that the deed notice required by Condition 4 of the NFA Letter has been recorded in the Durham County "
        "Registry of Deeds within the sixty (60) day period specified in the NFA Letter, together with a copy of the recorded "
        "instrument, a title date-down search confirming its recording, and confirmation that the Title Company has taken all "
        "appropriate exception therefor;",
        "evidence that the Soil Management Plan has been submitted to and approved by NCDEQ prior to the commencement of any "
        "subsurface disturbance in the Affected Area;",
        "the final design of the Vapor Mitigation System, prepared by a professional engineer licensed in North Carolina and "
        "stated in the quantities of the Construction Contract, together with the engineer's certification that the design "
        "satisfies Condition 1 of the NFA Letter and permits conversion to an active depressurization system;",
        "an overlay plan prepared by the Architect confirming the relationship between the Affected Area and the building "
        "footprint, and identifying with specificity each dwelling unit, if any, located above the Affected Area, together with "
        "written confirmation from Borrower of how compliance with the non-residential use restriction will be maintained;",
        "a reliance letter in favor of Lender from Sentinel Environmental Consulting LLC with respect to the Phase I ESA and the "
        "Phase II ESA; and",
        "if required by Lender, evidence of a pollution legal liability insurance policy covering the Affected Area, in an amount "
        "and with terms acceptable to Lender, naming Lender as additional insured and loss payee.",
    ]:
        numbered(doc, "(a)", x, indent=0.55, hang=0.25)
    para(doc, "[Drafting Note: The Phase I ESA establishes that as of October 28, 2024 the consultant had not been provided "
              "evidence that the deed notice was recorded. The Title Commitment effective December 5, 2024 does not list a "
              "recorded deed notice or declaration of land use restriction in Schedule B-II. The appraisal states that a "
              "Declaration of Land Use Restrictions has been recorded. These statements cannot all be correct. See Cover "
              "Memorandum Issues Nos. 8 and 11.]")

    sec_h(doc, "Section 3.6  Historic District Covenant Compliance")
    para(doc, "Borrower shall have delivered either (a) the written approval of the Brightleaf Historic District Association "
              "Architectural Review Committee of the final plans and specifications for the Project, (b) evidence that the sixty "
              "(60) day deemed-approval period under Article V of the Declaration of Covenants, Conditions and Restrictions "
              "recorded in Book 6984, Page 1155, as amended by First Amendment recorded in Book 7102, Page 388, Durham County "
              "Registry, has elapsed following a complete submission made not less than ninety (90) days prior to the anticipated "
              "commencement of construction, or (c) a written opinion of North Carolina counsel reasonably acceptable to Lender "
              "that the architectural review provisions do not apply to the Project. Borrower shall have also delivered a current "
              "statement from the Association of all assessments and charges due with respect to the Property.")
    para(doc, "[Drafting Note: The appraisal states that the Project's design \u201chas been reviewed and approved by the "
              "Brightleaf Historic District Association in accordance with the CC&Rs.\u201d The Title Commitment states that the "
              "Title Company \u201chas not received evidence that the current project plans have been submitted to or approved "
              "by\u201d the Architectural Review Committee, and that the Association has a right to seek injunctive relief to halt "
              "unapproved construction. See Cover Memorandum Issue No. 7.]")

    sec_h(doc, "Section 3.7  Equity Contribution and Sources and Uses")
    para(doc, "Borrower shall have deposited the Equity Contribution in the amount of $[4,080,000] in immediately available funds "
              "into the Equity Escrow Account, and Lender shall have received evidence reasonably satisfactory to it that the "
              "Equity Contribution and the balance of the land acquisition cost were funded from sources that are not, directly "
              "or indirectly, the Mezzanine Loan, the proceeds of any other Indebtedness, Brightleaf Mezzanine Capital LLC, "
              "Brightleaf Investors Group LLC, Thomas R. Chen, or any Affiliate of any of the foregoing. Lender shall have also "
              "received a corrected and reconciled sources and uses of funds statement, certified by Borrower and approved by "
              "Lender, reflecting (a) the Total Project Costs including all costs described in Section 9.1(c), (b) the payoff of "
              "the deed of trust described in Section 3.14, (c) the amount of the Interest Reserve, and (d) the Equity "
              "Contribution, in each case reconciling to the dollar.")
    para(doc, "[Drafting Note: The Equity Contribution of $2,140,000 required by Section 10.1(2) of the Credit Memorandum was "
              "computed against a $56,700,000 budget that omits (i) the payoff of the Triangle Commercial Bank deed of trust "
              "(original principal $3,400,000) and (ii) approximately $680,000 of demolition and remediation costs incurred before "
              "Closing. Applying the $56,700,000 budget, Loan of $47,500,000 and Mezzanine Loan of $9,200,000, no equity is "
              "required at all \u2014 the problem is that the budget does not include the payoff. On a corrected budget of "
              "$[60,780,000], the Equity Contribution required is $[4,080,000] and LTC is 78.15%. See Cover Memorandum Issue No. 8 and 11.]")

    sec_h(doc, "Section 3.8  Intercreditor Agreement")
    para(doc, "Lender, Mezzanine Lender and Borrower shall have executed and delivered the Intercreditor Agreement, which shall "
              "provide, among other things, that:")
    for x in [
        "Lender holds a first priority security interest in the Property, the other Collateral and the membership interests in "
        "Borrower, and Mezzanine Lender holds a security interest in the membership interests that is subordinate in all respects "
        "to Lender's security interest;",
        "Mezzanine Lender is subject to a standstill period of not less than ninety (90) days following the occurrence of a "
        "default under the Mezzanine Documents, during which Mezzanine Lender may not exercise any remedy against Borrower, the "
        "membership interests or the Property;",
        "Mezzanine Lender receives copies of all default and acceleration notices delivered by Lender and has the right, but not "
        "the obligation, to cure defaults under the Loan within the periods specified in the Intercreditor Agreement and to "
        "purchase the Loan at par plus accrued and unpaid interest, fees, costs and the Exit Fee;",
        "Mezzanine Lender may not amend, waive or modify any material term of the Mezzanine Documents, increase the principal "
        "amount of the Mezzanine Loan, or accept any prepayment thereof, without Lender's prior written consent;",
        "Mezzanine Lender may not file, or join in the filing of, an involuntary petition against Borrower, and will not contest "
        "or interfere with Lender's exercise of remedies;",
        "all payments in respect of the Mezzanine Loan are subject to a standstill upon the occurrence of an Event of Default, and "
        "no payment (whether in cash or in kind) may be made in respect of the Mezzanine Loan if a Default or Event of Default "
        "exists under the Loan Documents;",
        "the affiliate relationship between Mezzanine Lender and Brightleaf Investors Group LLC (each under the common control of "
        "Thomas R. Chen) is expressly acknowledged, and Mezzanine Lender waives any claim arising from that relationship; and",
        "the Mezzanine Loan matures no earlier than the Mini-Perm Maturity Date as extended, and any accrual of interest that is "
        "not paid in cash is capitalized and reported to Lender monthly.",
    ]:
        numbered(doc, "(a)", x, indent=0.55, hang=0.25)

    sec_h(doc, "Section 3.9  Single-Purpose Entity Amendments; Non-Consolidation Opinion")
    para(doc, "Borrower shall have delivered (a) an amendment to its Amended and Restated Operating Agreement, in form and "
              "substance satisfactory to Lender and duly adopted by all members, adding the SPE Covenants, requiring the "
              "appointment and retention of an independent manager who is not an officer, employee, member, manager or Affiliate "
              "of Borrower, any member, Mezzanine Lender or Thomas R. Chen, and requiring such independent manager's affirmative "
              "written consent to any voluntary bankruptcy filing, insolvency filing or general assignment for the benefit of "
              "creditors, and (b) a non-consolidation opinion of Borrower's counsel addressed to Lender, in form and substance "
              "satisfactory to Lender and its counsel, opining that a court applying North Carolina law would not substantively "
              "consolidate Borrower with any member, Affiliate of any member or Mezzanine Lender.")
    para(doc, "Borrower shall also have delivered the written consent of the Managing Member to the pledge by each member of its "
              "membership interest as required by Section 9.1 of the Operating Agreement, together with the consent of members "
              "holding not less than seventy-five percent (75%) of the membership interests to the borrowing and the granting of "
              "security as required by Section 3.2 of the Operating Agreement.")
    para(doc, "[Drafting Note: Section 2 of the organizational materials confirms that the Operating Agreement currently contains "
              "no independent manager or separateness provisions, and that the 75% major decisions threshold gives Brightleaf "
              "Investors Group LLC (28%) an effective veto because Ms. Vasquez-Torres (62%) and Mr. Osei (10%) hold only 72% "
              "between them. Both the loan authorization and the membership interest pledges therefore require the written "
              "consent of the affiliated member. See Cover Memorandum Issue No. 9.]")

    sec_h(doc, "Section 3.10  Organizational Documents and Authority")
    para(doc, "Borrower shall have delivered (a) a certificate of existence and good standing from the North Carolina Secretary "
              "of State dated within thirty (30) days of Closing; (b) certified copies of its articles of organization and "
              "operating agreement as amended; (c) a certificate of the Managing Member as to the incumbency of the officers and "
              "authorized signatories executing the Loan Documents, together with copies of the resolutions or written consents "
              "required by Section 3.9; (d) certificates of good standing or equivalent for Brightleaf Investors Group LLC; and "
              "(e) evidence of the good standing and identity of each Guarantor, including a copy of a government-issued "
              "identification document for each Guarantor.")

    sec_h(doc, "Section 3.11  Construction Documents")
    para(doc, "Lender shall have received and approved (a) the Construction Contract, executed and in full force and effect, in "
              "the GMP amount of $34,750,000, together with all exhibits, allowance schedules, unit price schedules and the full "
              "set of general conditions, and a collateral assignment thereof to Lender acknowledged by the contractor; (b) the "
              "architect's agreement with Meridian Design Collective PC, together with the collateral assignment thereof and the "
              "architect's consent; (c) the Approved Plans and Specifications, and evidence of all required plan reviews and "
              "permit approvals; (d) a construction schedule showing achievement of Substantial Completion no later than the "
              "Construction Maturity Date; (e) the contractor's current financial statements, a certificate of insurance and "
              "evidence of payment and performance bonding or of the contractor's stated bonding capacity; (f) a subcontractor "
              "list and a schedule of values for the Construction Contract; and (g) confirmation that the scope of the "
              "Construction Contract excludes work already completed at the Property, including the demolition completed in "
              "August 2024 and the environmental remediation completed in September 2024, or that an appropriate credit has been "
              "given therefor.")
    para(doc, "[Drafting Note: Line item 2.01 of the project budget describes $3,180,000 of site work as including "
              "\u201cDemolition, grading, utilities, paving.\u201d The warehouse demolition described in the Phase I ESA was "
              "completed in August 2024 and the remediation, at a cost of approximately $485,000, in September 2024. The GMP "
              "scope should be confirmed to exclude completed work. See Cover Memorandum Issue No. 3.]")

    sec_h(doc, "Section 3.12  Permits, Zoning and Governmental Approvals")
    para(doc, "Borrower shall have delivered (a) all building permits, grading permits, utility permits and other governmental "
              "approvals necessary for the commencement of construction; (b) a zoning compliance letter or equivalent "
              "determination from the City of Durham confirming that the Project is permitted as of right in the MU-D zoning "
              "district without variance, special use permit or conditional zoning; (c) evidence of the payment of all impact "
              "fees and utility tap fees; and (d) evidence of compliance with the North Carolina Sedimentation Pollution Control "
              "Act, including an approved erosion control plan.")

    sec_h(doc, "Section 3.13  Insurance")
    para(doc, "Borrower shall have delivered certificates of insurance and, if requested, certified copies of policies evidencing "
              "the coverages described in Schedule 5, each naming Lender as mortgagee, loss payee and/or additional insured as "
              "its interests appear, each with the endorsements required by Lender, and each providing for not less than thirty "
              "(30) days' prior written notice of cancellation, non-renewal or material change (ten (10) days' for non-payment of "
              "premium).")

    sec_h(doc, "Section 3.14  Payoff and Release of Prior Deed of Trust")
    para(doc, "Borrower shall have caused the deed of trust dated September 14, 2018 from Foster Street Properties LLC to the "
              "Trustee named therein for the benefit of Triangle Commercial Bank, recorded in Book 6215, Page 892, Durham County "
              "Registry, securing an original principal amount of $3,400,000, to be satisfied and released of record at or prior "
              "to Closing. Borrower shall have delivered (a) a payoff letter from Triangle Commercial Bank dated within thirty "
              "(30) days of the Closing Date stating the outstanding principal balance, accrued interest and per diem, and the "
              "amount required to obtain a release; (b) a certificate of satisfaction or cancellation of deed of trust in "
              "recordable form executed by Triangle Commercial Bank; and (c) a settlement statement reflecting the disbursement of "
              "the payoff from sources identified in the corrected sources and uses. The Title Policy shall contain no exception "
              "for such deed of trust.")
    para(doc, "[Drafting Note: The Title Commitment records that the indebtedness secured by this deed of trust has been "
              "\u201cpartially repaid\u201d and that the Title Company has not independently verified the outstanding balance. No "
              "payoff amount appears anywhere in the record, and no use of funds line item exists in the $56,700,000 budget for "
              "the payoff. See Cover Memorandum Issue No. 16.]")

    sec_h(doc, "Section 3.15  Lien Waivers and No Prior Work")
    para(doc, "Borrower shall have delivered (a) final unconditional lien waivers, in statutory form under N.C.G.S. Chapter 44A, "
              "from the demolition contractor, the environmental remediation contractor and each other contractor, subcontractor "
              "and material supplier that has furnished labor or materials at the Property prior to Closing, together with "
              "evidence of payment in full of the amounts so waived; (b) an owner's affidavit and a contractor's affidavit as to "
              "the date of first furnishing and the absence of unpaid claims; and (c) if any labor or materials have been "
              "furnished prior to the recording of the Deed of Trust, such additional protections as Lender or the Title Company "
              "may require by reason of the relation-back provisions of N.C.G.S. \u00a7 44A-10.")
    para(doc, "[Drafting Note: Because demolition and remediation work was performed in 2024, mechanics' liens for that work "
              "could relate back to a date before recordation of the Deed of Trust. The Title Company's Note 4 to the Commitment "
              "raises the same point. See Cover Memorandum Issue No. 5.]")

    sec_h(doc, "Section 3.16  Financial Information")
    para(doc, "Lender shall have received and approved (a) Borrower's financial statements as of a date not more than ninety (90) "
              "days prior to Closing, prepared in accordance with GAAP (audited or reviewed), together with a certified schedule "
              "of Borrower's assets and liabilities reconciling to the $14,200,000 net worth representation; (b) each Guarantor's "
              "current personal financial statement, dated not more than ninety (90) days prior to Closing, together with "
              "supporting statements for each depository and brokerage account listed therein; (c) two years of federal income tax "
              "returns for Borrower and each Guarantor; (d) Borrower's operating pro forma for the Project; and (e) such other "
              "credit information as Lender may reasonably require.")
    para(doc, "[Drafting Note: The $14,200,000 Borrower net worth and $9,300,000 guarantor liquidity figures are repeated "
              "throughout the record but are not supported by any financial statement in the documents provided. A single-purpose "
              "entity holding only the Property at a cost of $8,200,000, subject to the $3,400,000 Triangle deed of trust and to "
              "the remediation and site costs, cannot readily support a $14,200,000 net worth. See Cover Memorandum Issue No. 2.]")

    sec_h(doc, "Section 3.17  Legal Opinions")
    para(doc, "Lender shall have received from Calloway & Strauss PLLC, counsel to Borrower, (a) an opinion as to the due "
              "organization, valid existence and good standing of Borrower, the due authorization, execution and delivery of the "
              "Loan Documents, and the enforceability of the Loan Documents against Borrower and each Guarantor; (b) the "
              "non-consolidation opinion required by Section 3.9; (c) an opinion as to the perfection and first priority of "
              "Lender's security interests in the Collateral; and (d) such other opinions as Lender may reasonably require, "
              "including with respect to the valid creation and first priority of the Deed of Trust under North Carolina law.")

    sec_h(doc, "Section 3.18  Fees, Expenses and Deposits")
    para(doc, "Borrower shall have paid the Origination Fee, all fees of Lender's counsel and the Title Company, the title "
              "insurance premiums, the recording and documentary excise taxes payable on the Deed of Trust and the Note, and all "
              "other costs and expenses payable by Borrower under Section 18.2, in each case to the extent then due.")

    sec_h(doc, "Section 3.19  No Material Adverse Change; Committee Approval")
    para(doc, "No Material Adverse Effect shall have occurred, no material adverse change shall have occurred in the financial "
              "condition of Borrower or either Guarantor or in general real estate market conditions, and Lender shall have "
              "received all internal credit approvals required for the Loan (including any required re-approval by Lender's "
              "Senior Loan Committee of any change from the terms approved on January 22, 2025).")

    sec_h(doc, "Section 3.20  Additional Conditions")
    para(doc, "Lender shall have received such other documents, instruments, certificates, consents, estoppels and opinions as "
              "Lender may reasonably require in connection with the Loan, including estoppel certificates from the Brightleaf "
              "Historic District Association, the City of Durham and Duke Energy Carolinas with respect to the recorded "
              "easements, and evidence of the matters described in Section 3.5 in form satisfactory to Lender's environmental "
              "counsel.")

    # ---------------- ARTICLE IV ----------------
    art(doc, "ARTICLE IV — DISBURSEMENT OF LOAN PROCEEDS")
    sec_h(doc, "Section 4.1  Draw Schedule")
    para(doc, "Loan proceeds shall be disbursed in accordance with the Draw Schedule attached as Schedule 1, which is keyed to "
              "construction milestones and to the line items of the Approved Project Budget. The Draw Schedule reflects (a) the "
              "Initial Advance at Closing in the amount of $9,475,000, consisting of soft costs of $4,150,000, the Interest "
              "Reserve of $4,850,000 and the Origination Fee of $475,000; (b) Advances for hard construction costs in the "
              "aggregate gross amount of $34,750,000, from which Retainage in the aggregate amount of $3,475,000 shall be "
              "withheld; (c) Advances from the Contingency in the aggregate amount of $1,440,000; (d) Advances of the "
              "Loan-funded portion of the Developer Fee in the aggregate amount of $1,835,000; and (e) the release of Retainage "
              "in the amount of $3,475,000 following Substantial Completion. The aggregate of all Advances shall not exceed "
              "$47,500,000.")
    para(doc, "[Drafting Note: The draw table in Section 9.2 of the Term Sheet does not withhold the 10% retainage that Section "
              "9.1 of the Term Sheet requires: its Draws 2 through 8 total $34,750,000, or 100% of the GMP, and its Draw 9 of "
              "$3,275,000 is described as a \u201cRetainage Release\u201d although 10% of the GMP is $3,475,000. In fact $3,275,000 "
              "equals exactly the sum of the Contingency ($1,440,000) and the Loan-funded portion of the Developer Fee "
              "($1,835,000). The Draw Schedule on Schedule 1 conforms the disbursements to the stated 10% retainage and "
              "separately identifies the Contingency and Developer Fee. The draw schedule delivered by Borrower (dated January 8, "
              "2025) contains a related $1,000,000 imbalance in its component columns. See Cover Memorandum Issue No. 10.]")

    sec_h(doc, "Section 4.2  Draw Requests")
    para(doc, "Borrower shall submit a Draw Request to Lender not less than fifteen (15) days prior to the requested Advance "
              "date, on not more than one occasion per calendar month, accompanied by:")
    for x in [
        "a completed AIA Application and Certificate for Payment (AIA Forms G702 and G703), certified by the Architect and the "
        "general contractor, and an updated schedule of values;",
        "the Construction Inspector's report and certification that the applicable milestone has been achieved and that the "
        "undisbursed Loan proceeds, the Contingency and Borrower's remaining equity are sufficient to complete the Project;",
        "conditional partial lien waivers in statutory form from the general contractor, each subcontractor and each material "
        "supplier for work performed and materials furnished through the date of the Draw Request;",
        "a title date-down endorsement from the Title Company confirming that no intervening lien, encumbrance or title defect "
        "has arisen since the prior endorsement;",
        "evidence that all insurance required by Schedule 5 remains in full force and effect;",
        "the interest reserve adequacy certification required by Section 5.4;",
        "Borrower's certification that no Default or Event of Default exists, that all representations and warranties remain "
        "true and correct in all material respects, and that the Draw Request is within the line items of the Approved Project "
        "Budget; and",
        "an updated budget reconciliation, certified by Borrower and the Construction Inspector, demonstrating that the "
        "remaining undisbursed Loan proceeds, Contingency and Borrower equity are sufficient to complete the Project.",
    ]:
        numbered(doc, "(a)", x, indent=0.55, hang=0.25)

    sec_h(doc, "Section 4.3  Conditions to Each Advance")
    para(doc, "Lender's obligation to make any Advance (including the Initial Advance) is subject to the satisfaction of each of "
              "the following conditions as of the date of the Advance: (a) no Default or Event of Default shall exist; (b) each "
              "representation and warranty in Article VI shall be true and correct in all material respects; (c) Lender shall have "
              "received a complete Draw Request and all accompanying documentation; (d) the Construction Inspector shall have "
              "confirmed achievement of the applicable milestone; (e) the conditions of Section 3.5 shall remain satisfied with "
              "respect to the portion of the work then being performed; (f) no Material Adverse Effect shall have occurred; (g) "
              "the interest reserve adequacy test in Section 5.4 shall have been satisfied or Borrower shall have replenished the "
              "Interest Reserve; and (h) Borrower shall have satisfied the equity-first requirement of Section 4.6.")

    sec_h(doc, "Section 4.4  Retainage")
    para(doc, "Lender shall withhold Retainage equal to ten percent (10%) of each Advance for hard construction costs, such that "
              "Retainage in the aggregate amount of $3,475,000 (being 10% of the $34,750,000 GMP) is held at Substantial "
              "Completion. Lender shall release the Retainage as the final Advance (Draw No. 9) upon satisfaction of each of the "
              "following: (a) Substantial Completion and issuance of a final, unconditional certificate of occupancy by the City "
              "of Durham for all residential units and retail space; (b) delivery of final, unconditional lien waivers from the "
              "general contractor, each subcontractor and each material supplier; (c) delivery of the Architect's certificate of "
              "final completion and the Construction Inspector's final report; (d) expiration of the one hundred twenty (120) day "
              "period for filing claims of lien under N.C.G.S. Chapter 44A following the last furnishing of labor or materials, "
              "or posting of a lien bond satisfactory to Lender; and (e) delivery of an as-built survey, an updated title "
              "date-down, and evidence that the Vapor Mitigation System has been installed and, if required, that the as-built "
              "drawings and performance verification have been submitted to NCDEQ. No Retainage shall be released while a Default "
              "or Event of Default exists.")

    sec_h(doc, "Section 4.5  Change Orders; Contingency; Budget Reallocations")
    para(doc, "Borrower shall not authorize or permit any change order, change directive, allowance draw, field order or other "
              "modification of the Construction Contract that (a) increases the GMP, (b) reduces the scope, quality or quantity of "
              "the work in any material respect, (c) affects the structural, mechanical, electrical, plumbing, fire protection, "
              "building envelope or soil vapor mitigation systems, or (d) would cause the Project to be completed later than the "
              "Construction Maturity Date, without Lender's prior written consent, which consent may be withheld in Lender's sole "
              "and absolute discretion with respect to clauses (b) and (c).")
    para(doc, "Change orders that do not require Lender's consent and that are funded entirely from the Contingency may be paid "
              "from the Contingency upon Lender's approval of the applicable Draw Request, provided that (i) the aggregate of all "
              "hard cost contingency draws does not exceed $1,140,000 and of all soft cost contingency draws does not exceed "
              "$300,000, and (ii) Borrower provides a revised budget reconciliation demonstrating that the Project remains fully "
              "funded. Any change order that causes Total Project Costs to exceed the Approved Project Budget shall be funded by "
              "Borrower from sources other than the Loan and the Mezzanine Loan, in accordance with Section 4.6(c).")

    sec_h(doc, "Section 4.6  Equity First; Cost Overruns")
    numbered(doc, "(a)", "Equity Escrow. The Equity Contribution shall be deposited into the Equity Escrow Account prior to "
             "Closing and shall be disbursed to pay Project costs in accordance with Lender's escrow disbursement instructions. "
             "Except for the Initial Advance, no Advance shall be made unless and until the entire Equity Contribution has been "
             "disbursed and applied to Project costs.")
    numbered(doc, "(b)", "Land Contribution Not a Source. Borrower acknowledges that the land at 601 and 615 Foster Street was "
             "acquired for $8,200,000 and is included in the Total Project Costs as a cost incurred prior to Closing, and that "
             "the land acquisition cost is not a source of funds for the Project. Borrower shall not represent, in any "
             "certificate, draw request, compliance certificate or other document delivered to Lender, that the land "
             "contribution constitutes the Equity Contribution or otherwise satisfies the equity requirement of Section 3.7.")
    numbered(doc, "(c)", "Cost Overruns. Borrower shall pay all costs of the Project in excess of the Approved Project Budget, "
             "and all interest payable on the Loan after exhaustion of the Interest Reserve, from its own funds (and not from "
             "the proceeds of the Loan, the Mezzanine Loan or any other Indebtedness) within five (5) Business Days after demand "
             "by Lender. Failure to do so shall constitute an Event of Default under Section 13.3.")
    para(doc, "[Drafting Note: The record contains three inconsistent descriptions of how the $8,200,000 land cost was funded: "
              "(i) Section 5.2 of the Term Sheet and Section 2.2 of the Credit Memorandum state that the land was contributed as "
              "Borrower equity, funded by member capital calls including capital from Brightleaf Investors Group LLC; (ii) "
              "Section 1.3 of the organizational materials states that the land was acquired by Ms. Vasquez-Torres from personal "
              "resources and contributed at cost, and that Brightleaf Investors Group LLC has contributed $0; and (iii) line "
              "item 1.01 of the project budget states that the land is \u201cFunded by Mezzanine Loan\u201d in the amount of "
              "$8,200,000 and describes it as funded \u201cby mezzanine loan proceeds and member capital calls.\u201d Only "
              "description (iii) balances the sources and uses as presented. See Cover Memorandum Issue No. 15.]")

    sec_h(doc, "Section 4.7  Construction Inspector; Lender's Right to Inspect")
    para(doc, "Lender shall engage, at Borrower's expense, a Construction Inspector to review and certify construction progress "
              "prior to each Advance and at such other times as Lender may reasonably require. Borrower shall afford Lender, the "
              "Construction Inspector and their consultants access to the Property at all reasonable times upon reasonable prior "
              "notice, and shall cause the general contractor and the Architect to cooperate with the Construction Inspector, "
              "including by providing access to the work, the schedule of values, subcontracts, change orders and payment records.")

    sec_h(doc, "Section 4.8  Suspension and Termination of Advances")
    para(doc, "Lender may suspend or terminate its obligation to make further Advances upon the occurrence of any Default or "
              "Event of Default, upon the failure of any condition in Section 4.3 to be satisfied, upon any material deviation "
              "from the Approved Plans and Specifications, upon any stop-work order or other governmental action affecting the "
              "Project, or if Lender reasonably determines that the undisbursed Loan proceeds, the Contingency and Borrower's "
              "committed equity are insufficient to complete the Project. No suspension shall relieve Borrower of any obligation "
              "under the Loan Documents or constitute a waiver of any right of Lender.")

    sec_h(doc, "Section 4.9  No Obligation to Disburse for Non-Compliant Work")
    para(doc, "Lender shall have no obligation to make any Advance with respect to work that has not been performed in "
              "accordance with the Approved Plans and Specifications, work located in the Affected Area prior to satisfaction of "
              "the requirements of Section 12.3 and Section 12.4, or work that would violate any condition of the NFA Letter. "
              "Lender may withhold any Advance for work located over the Affected Area until Borrower has delivered the "
              "certifications described in Section 12.7.")
