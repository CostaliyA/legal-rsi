# -*- coding: utf-8 -*-
import sys; sys.path.insert(0,'/workspace/work')
from dh import *
from docx.enum.text import WD_ALIGN_PARAGRAPH as AL

def build_part8(doc):
    # ---------------- ARTICLE XV ----------------
    art(doc, "ARTICLE XV — SINGLE-PURPOSE ENTITY COVENANTS")
    para(doc, "Borrower shall at all times during the term of the Loan maintain its status as a single-purpose, bankruptcy-remote "
              "entity and shall, at its sole cost and expense:")
    spe = [
        "maintain its existence as a limited liability company separate and apart from any member, Affiliate or other Person, and "
        "maintain its assets and liabilities separate from those of any other Person;",
        "hold no assets other than the Property, the Project and related Project assets, and incur no liabilities other than the "
        "Loan, the Mezzanine Loan (as permitted by the Intercreditor Agreement) and trade payables incurred in the ordinary course "
        "of business;",
        "conduct no business other than the ownership, development, construction, leasing, management and operation of the Project;",
        "maintain its own books, records, financial statements, bank accounts and payroll, and not commingle its funds or other "
        "assets with those of any member, Affiliate or other Person;",
        "pay its own liabilities and expenses from its own funds, and not pay the liabilities of any member or Affiliate, and not "
        "guarantee or become obligated for the debts of any other Person (other than the Guaranties from the Guarantors, who are "
        "individuals who are also members);",
        "hold itself out to the public, to creditors and to all third parties as a legal entity separate and distinct from its "
        "members and their Affiliates, and conduct its business in its own name;",
        "observe all limited liability company formalities, including maintaining its records, holding required meetings or "
        "obtaining required written consents, maintaining its registered agent and registered office, and making all required "
        "filings with the North Carolina Secretary of State;",
        "allocate fairly and reasonably any overhead expenses shared with any member or Affiliate, and maintain an arm's-length "
        "relationship with each member and Affiliate, including with respect to any space, services or administrative support "
        "provided to Borrower;",
        "not hold itself out as responsible for the debts or obligations of any member or Affiliate, and not permit any member or "
        "Affiliate to hold itself out as responsible for the debts of Borrower;",
        "maintain the Equity Contribution in the Equity Escrow Account free of any claim of any member or creditor, and not "
        "distribute or return any portion of it while the Loan is outstanding;",
        "at all times maintain at least one independent manager who (i) is not, and has not been within five years, an officer, "
        "employee, director, manager, member, creditor, supplier or Affiliate of Borrower, any member, Mezzanine Lender or Thomas "
        "R. Chen, (ii) has no economic interest in Borrower other than a nominal fee for service as an independent manager, and "
        "(iii) is not a party to any agreement that would compromise such person's independence as determined by Lender;",
        "include in its operating agreement a provision requiring the affirmative written consent of the independent manager to "
        "the commencement of any voluntary bankruptcy, insolvency or reorganization case, the consent to the appointment of a "
        "receiver or trustee, the making of a general assignment for the benefit of creditors, or the admission in writing of an "
        "inability to pay debts generally as they become due;",
        "not amend, modify or repeal any SPE Covenant or any provision of its operating agreement relating to the independent "
        "manager without Lender's prior written consent; and",
        "provide Lender with an annual certificate of the independent manager, and such other evidence of separateness as Lender "
        "may reasonably request, and cause Borrower's counsel to deliver a further non-consolidation opinion upon any change in "
        "the identity of the independent manager or any amendment of the operating agreement.",
    ]
    for s in spe:
        numbered(doc, "(a)", s, indent=0.55, hang=0.25)
    para(doc, "The SPE Covenants in this Article are among the Recourse Events described in Section 11.4 and a breach of any of them "
              "is an Event of Default under Section 13.9. Borrower acknowledges that the presence of Brightleaf Investors Group LLC "
              "(28% member) and Brightleaf Mezzanine Capital LLC (mezzanine lender) under the common control of Thomas R. Chen "
              "increases the risk of substantive consolidation and that the requirements of this Article, of Section 3.9 and of "
              "Section 8.6 are intended to address that risk.", space_before=6)

    # ---------------- ARTICLE XVI ----------------
    art(doc, "ARTICLE XVI — INSURANCE, CASUALTY AND CONDEMNATION")
    sec_h(doc, "Section 16.1  Required Insurance")
    para(doc, "Borrower shall maintain at all times during the Construction Period the insurance coverages specified in Schedule 5, "
              "each in form and substance satisfactory to Lender and with insurers having a rating of not less than A- by A.M. Best.")
    sec_h(doc, "Section 16.2  Mini-Perm Period Coverage")
    para(doc, "Commencing at Substantial Completion and continuing throughout the Mini-Perm Period and any extension, Borrower "
              "shall maintain (a) special form property insurance covering the entire Project, on a replacement cost basis, in an "
              "amount not less than the full insurable replacement value of the Project, with an agreed amount endorsement and "
              "without coinsurance; (b) commercial general liability insurance with limits of not less than $5,000,000 per "
              "occurrence and $10,000,000 in the aggregate; (c) umbrella or excess liability insurance of not less than "
              "$10,000,000; (d) business income and rent loss insurance covering not less than twelve (12) months of gross rental "
              "income and continuing expenses, including debt service; (e) equipment breakdown, boiler and machinery coverage; (f) "
              "flood insurance at any time any portion of the Project is located in a Special Flood Hazard Area, in the amount "
              "required by applicable law; (g) builder's risk coverage until the earlier of final completion or expiration of the "
              "construction punch list period; and (h) such other coverage as Lender may reasonably require. Borrower acknowledges "
              "that Schedule 5 as delivered addresses only Construction Period coverage and must be supplemented for the Mini-Perm "
              "Period as provided in this Section.")
    para(doc, "[Drafting Note: Sections 11 and 19 of the Term Sheet, Section 8.1 of the Credit Memorandum and Schedule 5 of the "
              "project budget address builder's risk in the GMP amount of $34,750,000 only. No document specifies the property, "
              "rent loss or mini-perm period insurance limits. See Cover Memorandum Issue No. 21.]")
    sec_h(doc, "Section 16.3  Casualty")
    para(doc, "If the Property is damaged by fire or other casualty, Borrower shall promptly notify Lender and shall, at Lender's "
              "election (which election shall be made within a reasonable period and in good faith), either (a) cause the "
              "Insurance Proceeds to be held by Lender and disbursed for restoration in accordance with a restoration plan and "
              "budget approved by Lender, or (b) cause the Insurance Proceeds to be applied to the repayment of the Loan in "
              "accordance with Section 2.11. Lender's election shall be governed by whether (i) the cost of restoration exceeds "
              "the greater of $1,000,000 or five percent (5%) of the outstanding principal balance of the Loan, (ii) the loss is "
              "covered by insurance in an amount sufficient to restore, (iii) the Project can be restored to its pre-casualty "
              "condition within the remaining term of the Loan, and (iv) no Default or Event of Default exists.")
    sec_h(doc, "Section 16.4  Condemnation")
    para(doc, "If all or any material portion of the Property is taken by condemnation or eminent domain, the entire award shall be "
              "paid to Lender and, at Lender's election, either applied to the restoration of the Property or to the repayment of "
              "the Loan. Borrower shall promptly notify Lender of any actual or threatened taking and shall not settle or agree to "
              "any award without Lender's prior written consent. If the condemnation affects the Affected Area, the Vapor "
              "Mitigation System or any access to the Property, Lender may require the Loan to be repaid in full.")
    sec_h(doc, "Section 16.5  Flood Zone Determination")
    para(doc, "Borrower shall deliver a standard flood hazard determination with respect to the Property prior to Closing, and shall "
              "annually thereafter during the term of the Loan. Borrower acknowledges that the appraisal describes the Property as "
              "located in Flood Zone X on FIRM panel 3710406400J, effective May 2, 2019, while the Phase I ESA describes the "
              "Property as located in Zone X on FIRM panel 3720098700J, effective March 2, 2009. Borrower shall obtain and deliver "
              "a current determination from a nationally recognized flood zone determination service, and Lender's reliance shall "
              "be solely on such current determination.")

    # ---------------- ARTICLE XVII ----------------
    art(doc, "ARTICLE XVII — LEASING AND MINI-PERM MATTERS")
    sec_h(doc, "Section 17.1  Leasing Standards")
    para(doc, "Borrower shall lease the residential units and retail space of the Project in the ordinary course of business, on "
              "arm's-length terms, at market rents, without payment of leasing commissions to any Affiliate except as approved by "
              "Lender, and on a form of lease approved by Lender. No lease shall (a) have a term of more than five (5) years for "
              "retail space or fifteen (15) months for residential space, (b) grant any option to purchase, right of first refusal "
              "or right of first offer with respect to any portion of the Property, (c) grant any rent concession in excess of one "
              "(1) month of free rent, or (d) lease any portion of the Affected Area for residential occupancy. Borrower shall cause "
              "each residential lease to include a disclosure, in form approved by Lender and consistent with 40 C.F.R. Part 745 "
              "and applicable North Carolina law, regarding the environmental condition of the Property and the recorded land use "
              "restriction.")
    sec_h(doc, "Section 17.2  Rent Rolls and Leasing Reports")
    para(doc, "During the Mini-Perm Period, Borrower shall deliver to Lender monthly rent rolls, a leasing and occupancy report, "
              "and quarterly operating statements for the Property, each certified by the Managing Member, and shall promptly "
              "notify Lender of any tenant default, bankruptcy, early termination or vacancy exceeding five percent (5%) of the "
              "leased area.")
    sec_h(doc, "Section 17.3  Conversion to the Mini-Perm Period")
    para(doc, "The Loan shall convert to the Mini-Perm Period automatically upon the Construction Maturity Date, whether or not "
              "Substantial Completion has been achieved, and the Interest Rate shall increase to Daily Simple SOFR plus 3.50% per "
              "annum from and after that date. Conversion shall not constitute a waiver of any Event of Default, and if Substantial "
              "Completion has not occurred by the Construction Maturity Date, Lender may, in addition to its other remedies, "
              "suspend all further Advances other than the release of Retainage.")
    sec_h(doc, "Section 17.4  Take-Out Financing")
    para(doc, "Borrower shall use commercially reasonable efforts to obtain permanent take-out financing for the Loan, or to sell "
              "the Property, in each case on or before the date that is six (6) months prior to the Mini-Perm Maturity Date, and "
              "shall deliver to Lender, on a quarterly basis during the Mini-Perm Period, a written status report describing its "
              "take-out or sale efforts. Lender's receipt of any such report shall not constitute a commitment to extend, renew or "
              "refinance the Loan.")

    # ---------------- ARTICLE XVIII ----------------
    art(doc, "ARTICLE XVIII — INDEMNIFICATION AND EXPENSES")
    sec_h(doc, "Section 18.1  General Indemnity")
    para(doc, "Borrower and each Guarantor shall, jointly and severally, indemnify, defend (with counsel reasonably acceptable to "
              "Lender) and hold harmless the Lender Parties from and against any and all losses, claims, damages, liabilities, "
              "penalties, judgments, settlements, costs and expenses (including reasonable attorneys' fees and costs of "
              "investigation and appeal) arising out of or relating to (a) the Loan, the Loan Documents or the transactions "
              "contemplated thereby, (b) the Property, the Project or the construction thereof, (c) any claim by any contractor, "
              "subcontractor, material supplier, architect, consultant, tenant, purchaser or member relating to the Project or the "
              "Loan, (d) any failure by Borrower to comply with applicable law, (e) any brokerage or finder's fee asserted by any "
              "Person claiming by or through Borrower, and (f) any action taken or omitted by any Lender Party in connection with "
              "the administration or enforcement of the Loan, except to the extent resulting from such Lender Party's gross "
              "negligence, willful misconduct or breach of the Loan Documents as determined by a final, non-appealable judgment. "
              "This indemnity shall not apply to any loss that is covered by the Environmental Indemnity, as to which the "
              "Environmental Indemnity shall control.")
    sec_h(doc, "Section 18.2  Lender's Expenses")
    para(doc, "Borrower shall pay on demand all costs and expenses incurred by Lender in connection with the negotiation, "
              "documentation, closing, administration, servicing, enforcement and protection of the Loan, including (a) the fees "
              "and disbursements of Ashford, Cromdale Consulting & Laine LLP; (b) appraisal, reappraisal, environmental, engineering "
              "and construction inspection costs; (c) title insurance premiums, endorsements, escrow fees, recording fees and the "
              "North Carolina documentary excise tax payable on the Deed of Trust and the Note; (d) UCC and lien search and filing "
              "costs; (e) fees of any loan servicer, rating agency, auditor or syndication advisor; and (f) all costs of "
              "enforcement, foreclosure, bankruptcy, insolvency and appellate proceedings. Borrower's obligation to pay Lender's "
              "legal fees and expenses applies regardless of whether the Loan closes, as provided in Section 21.5 of the Term Sheet "
              "and subject only to the application of the expense deposit.")
    sec_h(doc, "Section 18.3  Environmental Indemnity")
    para(doc, "The Environmental Indemnity required by Section 11.5 is in addition to, and not in limitation of, this Article XVIII.")
    sec_h(doc, "Section 18.4  Survival")
    para(doc, "The obligations of Borrower and the Guarantors under this Article XVIII, under Section 11.5 and under the "
              "Environmental Indemnity shall survive the repayment of the Loan, the release or reconveyance of the Deed of Trust, "
              "foreclosure, deed in lieu of foreclosure and any transfer of the Property, and shall remain in effect for so long as "
              "any applicable statute of limitations permits a claim.")

    # ---------------- ARTICLE XIX ----------------
    art(doc, "ARTICLE XIX — NOTICES")
    para(doc, "All notices, requests, demands and other communications under the Loan Documents shall be in writing and shall be "
              "deemed duly given (a) when delivered personally, (b) one (1) Business Day after deposit with a nationally recognized "
              "overnight courier, (c) three (3) Business Days after deposit in the United States mail, certified or registered, "
              "postage prepaid, return receipt requested, or (d) when sent by electronic mail with confirmation of transmission, "
              "provided that any notice of default, acceleration, foreclosure or exercise of remedies shall also be sent by one of "
              "the methods described in clauses (a) through (c). Notices shall be addressed as set forth on Schedule 7, or to such "
              "other address or electronic mail address as a party may designate by notice given in accordance with this Article. "
              "Notices of default, notice of intention to accelerate and notices of acceleration shall be given in the manner "
              "required by applicable law, including N.C.G.S. \u00a7 45-21.16 with respect to any foreclosure proceeding.")

    # ---------------- ARTICLE XX ----------------
    art(doc, "ARTICLE XX — MISCELLANEOUS")
    misc = [
        ("Section 20.1  Governing Law",
         "The Loan Documents shall be governed by, and construed and enforced in accordance with, the laws of the State of North "
         "Carolina, without regard to its conflict of laws principles, except that the creation, perfection and priority of "
         "security interests in personal property shall be governed by the Uniform Commercial Code of the jurisdiction in which "
         "such property is located or in which the debtor is located, as applicable."),
        ("Section 20.2  Venue; Consent to Jurisdiction",
         "Each party irrevocably submits to the exclusive jurisdiction of the General Court of Justice of North Carolina, Durham "
         "County, and the United States District Court for the Middle District of North Carolina, for the purposes of any suit, "
         "action or proceeding arising out of or relating to the Loan Documents, waives any objection to venue in any such court, "
         "and agrees that service of process may be made in the manner provided in Article XIX. Nothing in this Section shall "
         "limit Lender's right to conduct a foreclosure sale pursuant to the Deed of Trust or to proceed in any other court of "
         "competent jurisdiction to enforce its security interests."),
        ("Section 20.3  Waiver of Jury Trial",
         "EACH PARTY HEREBY KNOWINGLY, VOLUNTARILY AND INTENTIONALLY WAIVES, TO THE FULLEST EXTENT PERMITTED BY APPLICABLE LAW, "
         "ANY RIGHT TO A TRIAL BY JURY IN ANY ACTION, PROCEEDING OR COUNTERCLAIM ARISING OUT OF OR RELATING TO THIS AGREEMENT, ANY "
         "OTHER LOAN DOCUMENT OR THE LOAN."),
        ("Section 20.4  Assignment and Participation",
         "Lender may sell, assign, syndicate or grant participations in all or any portion of the Loan and its rights under the "
         "Loan Documents without the consent of Borrower or any Guarantor, and may disclose all information relating to Borrower, "
         "the Guarantors and the Project to any actual or prospective participant or assignee and to any rating agency, subject to "
         "customary confidentiality undertakings. Borrower may not assign, delegate or transfer any of its rights or obligations "
         "under the Loan Documents without Lender's prior written consent, which consent may be withheld in Lender's sole "
         "discretion, and any purported assignment without such consent shall be void."),
        ("Section 20.5  Amendments and Waivers",
         "No amendment, modification, waiver or consent under the Loan Documents shall be effective unless in writing and signed by "
         "Lender and, in the case of an amendment or modification, by Borrower, and then only to the extent specifically set forth "
         "therein. No waiver of any provision shall be deemed a waiver of any other provision or of the same provision on any other "
         "occasion."),
        ("Section 20.6  Severability",
         "If any provision of any Loan Document is held to be invalid, illegal or unenforceable, such provision shall be enforced "
         "to the maximum extent permitted by applicable law, and the remaining provisions shall remain in full force and effect."),
        ("Section 20.7  Entire Agreement",
         "The Loan Documents constitute the entire agreement among the parties with respect to the Loan and supersede all prior "
         "and contemporaneous negotiations, understandings and agreements, including the Term Sheet (except to the extent Sections "
         "22 and 23 thereof are expressly binding) and the Credit Memorandum. Borrower acknowledges that it has not relied on any "
         "representation or warranty of any Lender Party except those expressly set forth in the Loan Documents."),
        ("Section 20.8  Counterparts; Electronic Signatures",
         "This Agreement may be executed in any number of counterparts, each of which shall be deemed an original and all of which "
         "together shall constitute one instrument. Signatures delivered by electronic means, including by PDF or by a "
         "nationally recognized e-signature platform, shall be deemed original signatures for all purposes and shall be "
         "admissible in any proceeding."),
        ("Section 20.9  Time of the Essence",
         "Time is of the essence with respect to the performance of each obligation under the Loan Documents, including the "
         "achievement of each construction milestone in Schedule 1 and the performance of each obligation subject to a cure "
         "period."),
        ("Section 20.10  No Third Party Beneficiaries",
         "The Loan Documents are solely for the benefit of Lender, Borrower and the Guarantors (and, as to the Intercreditor "
         "Agreement, Mezzanine Lender), and no other Person, including any contractor, subcontractor, tenant, member or creditor of "
         "Borrower, shall have any right to enforce any provision hereof."),
        ("Section 20.11  Relationship of the Parties",
         "Nothing in the Loan Documents shall be construed to create a partnership, joint venture, agency or fiduciary "
         "relationship between Lender and Borrower or any Guarantor. Lender's review and approval of the plans, the budget, the "
         "Construction Contract, draw requests and construction progress are for Lender's own protection only and shall not be "
         "construed as a representation, warranty or approval of the adequacy, design, workmanship or completion of the Project or "
         "as an assumption of any duty to Borrower or any third party."),
        ("Section 20.12  Usury Savings",
         "The provisions of Section 2.16 are incorporated in this Section by reference and shall control over any inconsistent "
         "provision of any Loan Document."),
        ("Section 20.13  Joint and Several Liability; Guarantor Acknowledgment",
         "The obligations of Borrower and each Guarantor under the Loan Documents are joint and several. Each Guarantor acknowledges "
         "that it has received a copy of this Agreement, that it has had the opportunity to consult with independent counsel, and "
         "that it executes the Loan Documents to which it is a party for valuable consideration, including Lender's agreement to "
         "make the Loan."),
        ("Section 20.14  Confidentiality",
         "Lender may disclose information relating to Borrower, the Guarantors and the Project as permitted by Section 20.4 and as "
         "required by applicable law, regulation, bank examination or subpoena, without notice to Borrower except where legally "
         "permitted. Borrower and the Guarantors shall keep the terms of the Loan Documents confidential except as required by law "
         "or as disclosed to their respective advisors, members and prospective transferees on a need-to-know basis."),
        ("Section 20.15  Further Documentation",
         "Borrower shall execute and deliver such additional documents, and shall cause the Title Company to issue such additional "
         "endorsements, as Lender may require to conform the Loan Documents to the requirements of Lender's regulators, of any "
         "rating agency or of any participant or assignee, provided that no such document shall increase the principal amount of "
         "the Loan, increase the Interest Rate or materially increase Borrower's obligations."),
    ]
    for h, t in misc:
        sec_h(doc, h)
        para(doc, t)

