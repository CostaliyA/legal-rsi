# -*- coding: utf-8 -*-
import sys; sys.path.insert(0,'/workspace/work')
from dh import *
from docx.enum.text import WD_ALIGN_PARAGRAPH as AL

def build_part6(doc):
    art(doc, "ARTICLE X — COLLATERAL, SECURITY DOCUMENTS AND INTERCREDITOR MATTERS")
    sec_h(doc, "Section 10.1  Deed of Trust")
    para(doc, "As security for the payment and performance of all obligations under the Loan Documents, Borrower shall grant, "
              "pursuant to the Deed of Trust, a first priority deed of trust lien on and security interest in the fee simple "
              "estate in the Property, including both parcels (Durham County Parcel Identification Nos. 0821-04-72-3341 and "
              "0821-04-72-4102) and all improvements, fixtures and appurtenances thereto, subject only to the Permitted "
              "Exceptions. The Deed of Trust shall be in recordable form, shall contain a power of sale exercisable by the "
              "Trustee in accordance with Article 2A of Chapter 45 of the North Carolina General Statutes, and shall be recorded "
              "in the Durham County Registry of Deeds at Closing.")

    sec_h(doc, "Section 10.2  Assignment of Leases and Rents")
    para(doc, "Borrower shall collaterally assign to Lender, pursuant to the Assignment of Leases and Rents, all of its right, "
              "title and interest in and to all present and future leases, licenses, concession agreements and occupancy "
              "agreements affecting the Property, together with all rents, income, receipts, profits, security deposits and "
              "proceeds thereof. The Assignment shall constitute a present, absolute assignment, shall constitute a security "
              "interest in favor of Lender in all personal property and general intangibles now or hereafter arising, and shall "
              "provide Lender with the right, upon the occurrence and during the continuance of an Event of Default, to collect "
              "rents directly.")

    sec_h(doc, "Section 10.3  Security Interest in Personal Property")
    para(doc, "Pursuant to the Security Agreement, Borrower shall grant Lender a first priority security interest in all "
              "personal property relating to the Project, including fixtures, equipment, materials, inventory, accounts, "
              "contract rights, permits, licenses, plans, specifications, drawings, warranties, guarantees, approvals, general "
              "intangibles and proceeds, whether now owned or hereafter acquired. Borrower shall execute and deliver all UCC-1 "
              "financing statements and fixture filings necessary to perfect such security interest, and shall maintain at its "
              "principal office all records relating to such collateral.")

    sec_h(doc, "Section 10.4  Assignments of Construction and Architect's Contracts")
    para(doc, "Borrower shall collaterally assign to Lender, pursuant to the collateral assignments delivered at Closing, all of "
              "its right, title and interest in and to the Construction Contract and the architect's agreement, including all "
              "claims, causes of action, warranties, retainage rights, change order rights and proceeds thereof. Each assignment "
              "shall be consented to in writing by the counterparty, and each such consent shall include a notice, cure and "
              "assumption provision acceptable to Lender. Upon an Event of Default, Borrower shall, upon Lender's request, "
              "assign the Construction Contract and the architect's agreement to Lender or to Lender's designee, free and clear "
              "of any claim of Borrower.")

    sec_h(doc, "Section 10.5  Insurance Proceeds and Condemnation Awards")
    para(doc, "Borrower shall collaterally assign to Lender all Insurance Proceeds and all awards, damages and compensation "
              "payable on account of any condemnation, expropriation or other taking of the Property or any part thereof, and "
              "shall hold any such amounts in trust for Lender pending Lender's determination under Article XVI.")

    sec_h(doc, "Section 10.6  Pledge of Membership Interests")
    numbered(doc, "(a)", "Each member of Borrower shall pledge to Lender one hundred percent (100%) of its membership interest in "
             "Borrower pursuant to a Membership Interest Pledge, as follows: Elena Vasquez-Torres, a 62% membership interest; "
             "Brightleaf Investors Group LLC, a 28% membership interest; and Reginald K. Osei, a 10% membership interest.")
    numbered(doc, "(b)", "The Membership Interest Pledges shall constitute a first priority security interest in the pledged "
             "membership interests, subject only to the subordinated pledge in favor of Mezzanine Lender permitted by the "
             "Intercreditor Agreement. Borrower and each member acknowledge that the pledge to Mezzanine Lender of the same "
             "membership interests, as described in Section 1.4 of the Term Sheet and in the organizational materials delivered "
             "to Lender, is in conflict with Section 8 of the Term Sheet and with this Section, and that the only permitted "
             "resolution is the subordination of the Mezzanine Lender's pledge under the Intercreditor Agreement.")
    numbered(doc, "(c)", "The Operating Agreement of Borrower provides that a member may pledge its membership interest only with "
             "the written approval of the Managing Member. Borrower shall deliver such approval, and the written consent of the "
             "members holding not less than seventy-five percent (75%) of the membership interests to each pledge, as a "
             "condition to Closing under Section 3.9.")
    numbered(doc, "(d)", "If any membership interest is evidenced by a certificate, Borrower shall cause each certificate to be "
             "delivered to Lender together with an undated assignment separate from certificate, and Borrower shall amend its "
             "operating agreement and articles of organization as necessary to provide that the pledged membership interests are "
             "certificated and subject to the pledge. If any pledged membership interest is uncertificated, Lender's security "
             "interest in the UCC \u00a7 8-102 general intangibles or in the uncertificated interests, as the case may be, shall "
             "be perfected by the filing of UCC-1 financing statements against the applicable pledgor and the applicable debtor.")

    sec_h(doc, "Section 10.7  Intercreditor Matters; Mezzanine Loan")
    para(doc, "The lien and security interest of Mezzanine Lender in the membership interests shall be subordinate and junior in "
              "all respects to the liens and security interests of Lender, as provided in the Intercreditor Agreement. Borrower "
              "acknowledges that Lender would not make the Loan without the Intercreditor Agreement in effect, that the "
              "Intercreditor Agreement is for the benefit of Lender and Mezzanine Lender, and that Borrower has no right to "
              "enforce any provision of the Intercreditor Agreement. Borrower shall not take any action, and shall not permit any "
              "member to take any action, that would cause the Mezzanine Loan to be in default or that would give Mezzanine "
              "Lender any right to exercise remedies against the membership interests.")

    sec_h(doc, "Section 10.8  Further Assurances; Protection of Collateral")
    para(doc, "Borrower shall execute, deliver, record and file such further instruments and take such further action as Lender "
              "may reasonably request to create, perfect, maintain and evidence the first priority of Lender's liens and security "
              "interests, including UCC continuation statements, title date-down endorsements, estoppel certificates, landlord and "
              "mortgagee waivers, consents to assignment, and, upon Lender's request, an assignment of the Soil Management Plan and "
              "all environmental permits and approvals relating to the Affected Area.")

    sec_h(doc, "Section 10.9  Release of Collateral")
    para(doc, "Lender shall release the lien of the Deed of Trust and the other security interests upon payment in full of the "
              "Loan and all other amounts payable under the Loan Documents and the expiration of all applicable periods under "
              "Section 18.4 and the Environmental Indemnity. Lender may release portions of the Collateral only with Lender's "
              "written consent and on terms approved by Lender. No release of any collateral, and no sale, transfer or other "
              "disposition of any collateral, shall relieve Borrower or any Guarantor of any obligation under the Loan Documents.")

    # ---------------- ARTICLE XI ----------------
    art(doc, "ARTICLE XI — GUARANTIES AND ENVIRONMENTAL INDEMNITY")
    sec_h(doc, "Section 11.1  Completion Guaranty")
    para(doc, "Each Guarantor shall execute and deliver the Completion Guaranty, pursuant to which the Guarantors, jointly and "
              "severally, guarantee to Lender the lien-free completion of the Project in accordance with the Approved Plans and "
              "Specifications, the Approved Project Budget and the Draw Schedule, on or before the Construction Maturity Date, and "
              "the payment of all costs of such completion, including all costs of the Vapor Mitigation System, the Soil Management "
              "Plan and any environmental remediation required by the NFA Letter or any governmental authority. The Completion "
              "Guaranty shall remain in full force and effect until (a) Substantial Completion, (b) issuance of a final "
              "unconditional certificate of occupancy for all residential units and retail space, (c) release or bonding of all "
              "mechanics' and materialmen's liens, and (d) delivery to NCDEQ of the as-built drawings and performance verification "
              "for the Vapor Mitigation System.")

    sec_h(doc, "Section 11.2  Carry Guaranty")
    para(doc, "Each Guarantor shall execute and deliver the Carry Guaranty, pursuant to which the Guarantors, jointly and "
              "severally, guarantee to Lender the payment of interest on the Loan and all other carrying costs of the Property and "
              "the Project during the term of the Loan, including real estate taxes, insurance premiums, utilities, ground rents "
              "(if any), assessments under the Brightleaf Historic District Declaration, and Lender's expenses under Section 18.2. "
              "The Carry Guaranty is in addition to, and not in lieu of, the Interest Reserve, and shall be applicable to any "
              "interest and carrying costs that accrue after the Interest Reserve is exhausted or that exceed the amount available "
              "in the Interest Reserve. The Carry Guaranty shall not be reduced by any limitation on the amount of the Loan "
              "remaining undisbursed.")

    sec_h(doc, "Section 11.3  Partial Repayment Guaranty")
    numbered(doc, "(a)", "Each Guarantor shall execute and deliver the Partial Repayment Guaranty, pursuant to which the "
             "Guarantors, jointly and severally, guarantee to Lender the repayment of a portion of the Loan equal to twenty-five "
             "percent (25%) of the Loan Amount.")
    numbered(doc, "(b)", "The aggregate liability of the Guarantors under the Partial Repayment Guaranty shall not exceed "
             "$11,875,000 (being 25% of $47,500,000) in the aggregate for all Guarantors, and shall not be $11,875,000 per "
             "Guarantor. Payment by any Guarantor shall reduce, dollar for dollar, the aggregate amount recoverable from all "
             "Guarantors. Lender may proceed against any Guarantor for the full amount, but in no event shall Lender collect more "
             "than $11,875,000 in the aggregate under the Partial Repayment Guaranty.")
    numbered(doc, "(c)", "The obligation of each Guarantor under the Partial Repayment Guaranty shall be reduced by the amount of "
             "any net recovery actually received by Lender from the realization on the Collateral, determined after deducting all "
             "costs and expenses of realization (including attorneys' fees) and, in the case of a foreclosure, after giving effect "
             "to any determination of fair value under N.C.G.S. \u00a7 45-21.36. [Drafting Note: Section 7.3 of the Term Sheet "
             "and Section 4.3 of the Credit Memorandum describe the Partial Repayment Guaranty inconsistently, the Credit "
             "Memorandum referring to \u201c$11,875,000 per guarantor\u201d and describing a payment guaranty triggered by "
             "\u201ca payment default or other event of default.\u201d The parties must elect between a 25% recourse/loss guaranty "
             "and a full payment guaranty in that amount. See Cover Memorandum Issue No. 17.]")

    sec_h(doc, "Section 11.4  Recourse Carve-Outs (Bad Boy Acts)")
    para(doc, "The Partial Repayment Guaranty is a limited recourse obligation except that, upon the occurrence of any of the "
              "following (each, a \u201cRecourse Event\u201d), the Guarantors shall be liable on a joint and several basis for the "
              "entire outstanding principal balance of the Loan, all accrued and unpaid interest, all fees (including the Exit "
              "Fee), all costs and expenses of enforcement, and all other amounts payable under the Loan Documents, without "
              "limitation to the $11,875,000 cap:")
    for x in [
        "fraud, intentional misrepresentation, material misstatement or omission, or willful misconduct by Borrower, any member "
        "of Borrower, any Guarantor or any of their Affiliates, in connection with the Loan, the Project or any Loan Document;",
        "any voluntary bankruptcy, insolvency, receivership or reorganization filing or proceeding by or on behalf of Borrower, "
        "any Guarantor or any member of Borrower, or any collusive involuntary filing, or any admission of insolvency or general "
        "assignment for the benefit of creditors;",
        "any sale, transfer, pledge, encumbrance or other disposition of the Property, the Project, any membership interest in "
        "Borrower or any material asset of Borrower in violation of the Loan Documents;",
        "any release, disposal, migration or presence of Hazardous Materials at, on, under or from the Property, or any "
        "violation of any Environmental Law or of any condition of the NFA Letter, in each case caused or permitted by Borrower, "
        "any Guarantor, any member of Borrower or any of their Affiliates or contractors;",
        "the failure to maintain the Vapor Mitigation System, the Soil Management Plan, the recorded deed notice or the "
        "non-residential use restriction in the Affected Area, or any use of the Affected Area for residential purposes in "
        "violation of the NFA Letter;",
        "any material violation of the SPE Covenants, including the failure to maintain separate books, records and accounts, "
        "any commingling of funds, or the failure to obtain the independent manager's consent to a bankruptcy filing;",
        "waste, arson, physical injury to or destruction of the Property, or the misapplication or conversion of rents, "
        "Insurance Proceeds, condemnation awards, tenant security deposits, the Interest Reserve, the Equity Contribution or any "
        "other collateral or funds held in trust;",
        "any failure to pay real estate taxes, assessments or insurance premiums, or any failure to maintain the insurance "
        "required by Schedule 5; and",
        "any amendment, modification or waiver of the Loan Documents, or any other act, in each case in violation of the Loan "
        "Documents and to the material detriment of Lender.",
    ]:
        numbered(doc, "(a)", x, indent=0.55, hang=0.25)
    para(doc, "The provisions of this Section are intended to define the circumstances in which the limitation on recourse is "
              "inapplicable, and shall not be construed to limit the liability of any Guarantor for fraud or for any other "
              "obligation that may not be waived or limited as a matter of applicable law.")

    sec_h(doc, "Section 11.5  Environmental Indemnity")
    para(doc, "Borrower and each Guarantor shall execute and deliver the Environmental Indemnity, pursuant to which they shall, "
              "jointly and severally, indemnify, defend and hold harmless the Lender Parties from and against all losses, "
              "liabilities, damages, penalties, fines, costs, expenses (including reasonable attorneys', consultants' and "
              "engineers' fees), remediation costs, diminution in value, response costs and claims arising out of or relating to "
              "(a) the presence, release, threatened release, storage, transport or disposal of Hazardous Materials at, on, under "
              "or from the Property, whenever occurring, including the condition described in the Phase I ESA and the Phase II "
              "ESA; (b) the Affected Area, the Vapor Mitigation System, the Soil Management Plan or the deed notice; (c) any "
              "violation of any Environmental Law with respect to the Property; (d) any failure to comply with any condition of "
              "the NFA Letter; and (e) any claim asserted by any tenant, occupant, purchaser or governmental authority arising out "
              "of any of the foregoing. The Environmental Indemnity shall be unlimited in amount, shall not be subject to any "
              "limitation on recourse, and shall survive repayment of the Loan, the release or reconveyance of the Deed of Trust, "
              "foreclosure, deed in lieu of foreclosure and any transfer of the Property.")
    para(doc, "[Drafting Note: Section 7.4 of the Term Sheet describes the Environmental Indemnity as guaranteed by each "
              "Guarantor; Section 8.2 of the Credit Memorandum requires it from the Borrower and the Guarantors. This Section "
              "follows the Credit Memorandum. See Cover Memorandum Issue No. 17.]")

    sec_h(doc, "Section 11.6  Guarantor Waivers; Joint and Several Liability")
    para(doc, "Each Guarantor's obligations under the Guaranties are primary, absolute, unconditional and joint and several and "
              "shall not be affected by any extension, renewal, modification or amendment of the Loan Documents; any release, "
              "substitution or impairment of any collateral; any bankruptcy, insolvency or reorganization of Borrower or any other "
              "Guarantor; the failure of Lender to perfect any security interest; the invalidity or unenforceability of any Loan "
              "Document against Borrower; or any other circumstance that might otherwise constitute a defense. Each Guarantor waives "
              "notice of acceptance, presentment, demand, protest, notice of dishonor, notice of default, notice of acceleration, "
              "and all defenses based on suretyship and the statutes of limitations to the fullest extent permitted by applicable "
              "law, including the provisions of Article 3 of the Uniform Commercial Code as in effect in North Carolina and the "
              "suretyship defenses codified in N.C.G.S. \u00a7 26-7, to the extent such waivers are enforceable.")

    sec_h(doc, "Section 11.7  Subordination of Guarantor Claims")
    para(doc, "All claims of any Guarantor against Borrower, whether now existing or hereafter arising, are and shall be "
              "subordinate in right of payment and in all other respects to the prior payment in full of all amounts payable under "
              "the Loan Documents, and each Guarantor shall not accept any payment on any such claim while any amount remains "
              "outstanding under the Loan Documents.")

    sec_h(doc, "Section 11.8  North Carolina Deficiency and Fair Value Matters")
    para(doc, "The parties acknowledge that real property foreclosure in North Carolina is conducted by the Trustee under a power "
              "of sale in a special proceeding before the Clerk of Superior Court pursuant to Article 2A of Chapter 45 of the "
              "North Carolina General Statutes, that a deficiency determination is subject to the fair value provisions of "
              "N.C.G.S. \u00a7 45-21.36 and the upset bid procedures of N.C.G.S. \u00a7 45-21.27 et seq., and that Lender's "
              "recovery from the Guarantors may be affected by the outcome of those proceedings. Lender may elect to pursue the "
              "Guarantors and the Collateral simultaneously, in any order, and no election of remedies shall operate as a waiver "
              "of any right of Lender. [Drafting Note: Section 4.3 of the Credit Memorandum characterizes North Carolina as "
              "a \u201cjudicial foreclosure state.\u201d Counsel should confirm the accuracy of that characterization and its "
              "consistency with the Deed of Trust and the Credit Memorandum's discussion of anti-deficiency protections before "
              "the credit file is finalized. See Cover Memorandum Issue No. 22.]")
