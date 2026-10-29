# -*- coding: utf-8 -*-
import sys; sys.path.insert(0,'/workspace/work')
from dh import *
from docx.enum.text import WD_ALIGN_PARAGRAPH as AL

def build_part7(doc):
    # ---------------- ARTICLE XII ----------------
    art(doc, "ARTICLE XII — ENVIRONMENTAL MATTERS")
    sec_h(doc, "Section 12.1  Acknowledgement of Environmental Condition")
    para(doc, "Borrower and each Guarantor acknowledge that Lender has made the Loan in reliance on the Phase I ESA, the Phase "
              "II ESA, the NFA Letter and Borrower's representations in Section 6.10 and Section 6.11; that residual petroleum "
              "contamination remains in soil at the Affected Area at concentrations exceeding the NCDEQ residential Preliminary "
              "Soil Remediation Goals, including TPH-DRO at up to 847 mg/kg (against a residential goal of 100 mg/kg) and benzene "
              "at up to 0.42 mg/kg (against a residential goal of 0.065 mg/kg); that soil gas benzene at up to 185 \u00b5g/m\u00b3 "
              "exceeds the NCDEQ residential vapor intrusion screening level of 31 \u00b5g/m\u00b3 by approximately six times; and "
              "that the NFA Letter does not constitute a clean closure and may be reopened. Borrower shall not, in any lease, "
              "purchase and sale agreement, condominium declaration, offering document or disclosure to any tenant or purchaser, "
              "misstate the status of the environmental condition of the Property or the scope of the NFA Letter.")

    sec_h(doc, "Section 12.2  Affected Area; Non-Residential Use Restriction")
    para(doc, "Borrower shall not use, and shall not permit the use of, the Affected Area for any residential purpose, and shall "
              "not construct or permit to be constructed any dwelling unit within the Affected Area, unless and until (a) NCDEQ has "
              "issued a written modification of the NFA Letter expressly permitting residential use of the Affected Area, (b) "
              "Borrower has delivered to Lender an environmental consultant's report and, if required, a risk assessment "
              "demonstrating that residential use is protective of human health under a residential exposure scenario, (c) the "
              "Title Company has insured over any recorded land use restriction to Lender's satisfaction, and (d) Lender has "
              "consented in writing. Borrower shall incorporate the restriction into all construction drawings, the Construction "
              "Contract, its leasing materials and any unit-level disclosure, and shall cause the Architect to depict the Affected "
              "Area boundary on the approved floor plans for levels 1 through 6.")

    sec_h(doc, "Section 12.3  Soil Vapor Mitigation System")
    para(doc, "Borrower shall cause the Vapor Mitigation System to be (a) designed by a professional engineer licensed in North "
              "Carolina, (b) constructed as a passive sub-slab depressurization system with the capability of conversion to an "
              "active depressurization system, (c) installed beneath every enclosed structure constructed over the Affected Area, "
              "in accordance with Condition 1 of the NFA Letter and the NCDEQ Division of Waste Management vapor intrusion "
              "guidance, (d) commissioned and tested prior to occupancy of any space above the Affected Area, and (e) submitted to "
              "NCDEQ, together with as-built drawings and a performance verification report, within ninety (90) days after "
              "completion of the building foundation in the Affected Area. Borrower shall deliver copies of all such submissions "
              "and of all NCDEQ responses to Lender within five (5) Business Days. Borrower shall maintain, operate, test and, if "
              "required, convert the system for so long as the NFA Letter requires, and shall not remove, disable or impair the "
              "system without Lender's prior written consent.")

    sec_h(doc, "Section 12.4  Soil Management Plan")
    para(doc, "Borrower shall cause the Soil Management Plan to be prepared, submitted to NCDEQ and approved by NCDEQ before any "
              "excavation, grading, dewatering or other subsurface disturbance occurs in the Affected Area. Borrower shall "
              "incorporate the Soil Management Plan into the Construction Contract and the construction specifications, shall "
              "require the general contractor and all subcontractors to comply with it, shall provide the training required by the "
              "Soil Management Plan, and shall deliver to Lender a written certification of compliance from the Construction "
              "Inspector concurrently with each Draw Request for work in or adjacent to the Affected Area.")

    sec_h(doc, "Section 12.5  Deed Notice and Land Use Restriction")
    para(doc, "Borrower shall record the deed notice required by Condition 4 of the NFA Letter in the Durham County Registry of "
              "Deeds within the period specified in the NFA Letter and, in any event, prior to Closing, and shall deliver to "
              "Lender a certified copy of the recorded instrument, the recording stamp and a title date-down confirming "
              "recordation. Borrower shall not modify, amend, release, terminate or seek the release of the deed notice or the "
              "recorded land use restriction without Lender's prior written consent. Any such instrument shall be a Permitted "
              "Exception under the Title Policy.")

    sec_h(doc, "Section 12.6  Monitoring, Reporting and Regulatory Contact")
    para(doc, "Borrower shall (a) conduct the post-construction soil gas and indoor air monitoring recommended in the Phase I ESA "
              "at the frequency and according to the protocol approved by Lender's environmental consultant, and deliver the "
              "results to Lender within fifteen (15) days after receipt; (b) promptly notify Lender of any NCDEQ inspection, "
              "notice, information request or enforcement action; (c) not settle, compromise or agree to any modification of the "
              "NFA Letter without Lender's prior written consent; and (d) maintain complete records of all environmental "
              "investigation, remediation, monitoring, construction and reporting activity at the Property and make them "
              "available to Lender upon request.")

    sec_h(doc, "Section 12.7  Lender's Disbursement Conditions Relating to the Affected Area")
    para(doc, "Notwithstanding anything in Article IV to the contrary, Lender shall not be obligated to make any Advance for "
              "foundation, structural, podium, parking structure, MEP rough-in, interior finish or any other work located in or "
              "over the Affected Area unless Borrower has delivered (a) NCDEQ's written approval of the Soil Management Plan; (b) "
              "the final design of the Vapor Mitigation System and the engineer's certification described in Section 3.5(d); (c) "
              "the recorded deed notice; (d) the Architect's certification that no dwelling unit is located in the Affected Area "
              "or, if any is, evidence of the NCDEQ modification and Lender's consent required by Section 12.2; and (e) the "
              "Construction Inspector's confirmation that the work conforms to the foregoing.")

    sec_h(doc, "Section 12.8  Environmental Insurance")
    para(doc, "Borrower shall, if requested by Lender, obtain and maintain a pollution legal liability insurance policy, from an "
              "insurer and in an amount, with deductibles and on terms acceptable to Lender, naming Lender as additional insured "
              "and loss payee, covering third-party bodily injury and property damage, first-party cleanup costs, legal defense "
              "costs, and, if available, the cost of obtaining a modification of the NFA Letter or of re-remediation, for the term "
              "of the Loan and for such period thereafter as Lender may reasonably require given the survival of the Environmental "
              "Indemnity.")

    sec_h(doc, "Section 12.9  Lender's Environmental Rights")
    para(doc, "Lender may, at Borrower's expense (which expense shall be a guaranteed carrying cost under the Carry Guaranty), "
              "engage an environmental consultant to conduct such investigations, reviews and monitoring as Lender reasonably "
              "considers necessary (a) upon the occurrence of a Default or Event of Default, (b) upon Lender's reasonable belief "
              "that a release or violation has occurred, or (c) in connection with any renewal, extension, reappraisal or "
              "securitization of the Loan. Borrower shall cooperate with any such consultant and shall provide access to the "
              "Property, the construction documents and the environmental records.")

    sec_h(doc, "Section 12.10  No Assumption of Liability by Lender")
    para(doc, "Nothing in this Agreement or in any other Loan Document, and no inspection, review or approval by Lender or its "
              "consultants, shall (a) constitute an assumption by Lender of any obligation or liability relating to the "
              "environmental condition of the Property, (b) constitute a waiver of Borrower's representations, warranties, "
              "covenants or indemnities, (c) constitute approval of the adequacy of the Vapor Mitigation System or the Soil "
              "Management Plan, or (d) constitute a determination that the Property complies with any Environmental Law. Lender "
              "shall have no liability for any environmental condition at the Property, and Borrower and each Guarantor waive any "
              "claim against any Lender Party arising from any such condition.")

    # ---------------- ARTICLE XIII ----------------
    art(doc, "ARTICLE XIII — EVENTS OF DEFAULT")
    para(doc, "Each of the following shall constitute an Event of Default under the Loan Documents:")
    eods = [
        ("Section 13.1  Payment Default",
         "Borrower fails to pay any principal, interest, fee, expense reimbursement or other amount payable under the Loan "
         "Documents when due, whether at stated maturity, by acceleration or otherwise, and such failure continues for five (5) "
         "days; provided that no grace period shall apply to any payment due on the Mini-Perm Maturity Date or after "
         "acceleration."),
        ("Section 13.2  False Representations",
         "Any representation or warranty made or deemed made by Borrower or any Guarantor in any Loan Document or in any "
         "certificate, financial statement or other document delivered to Lender proves to have been false, incorrect or "
         "misleading in any material respect when made or deemed made."),
        ("Section 13.3  Covenant Defaults",
         "Borrower or any Guarantor fails to observe or perform any covenant, condition or agreement contained in this Agreement "
         "or any other Loan Document (other than a payment default under Section 13.1 or a default described in Sections 13.4 "
         "through 13.16) and such failure continues for thirty (30) days after the earlier of written notice from Lender or "
         "actual knowledge of Borrower; provided that if the failure is not capable of cure within thirty (30) days and Borrower "
         "is diligently pursuing cure, such period shall be extended by an additional thirty (30) days, but in no event shall the "
         "aggregate cure period exceed sixty (60) days. The cure periods in this Section shall not apply to a breach of Section "
         "4.6(c) (cost overruns), Section 5.3 (interest reserve replenishment), Article IX (financial covenants, which are "
         "governed by the cure rights stated therein) or Section 12.2 (use restriction)."),
        ("Section 13.4  Bankruptcy and Insolvency",
         "Borrower, any Guarantor or any member of Borrower (a) commences any case, proceeding or other action under any "
         "bankruptcy, insolvency or reorganization statute, (b) has an involuntary case commenced against it that is not "
         "dismissed within sixty (60) days, (c) makes a general assignment for the benefit of creditors, (d) admits in writing its "
         "inability to pay its debts as they become due, (e) suffers the appointment of a receiver, trustee, custodian or "
         "liquidator for it or for a substantial part of its property, which appointment is not vacated within sixty (60) days, "
         "or (f) suffers the attachment, execution or judicial seizure of a material portion of the Property or the Collateral."),
        ("Section 13.5  Material Adverse Change",
         "A Material Adverse Effect occurs, including any material adverse change in the financial condition of Borrower or any "
         "Guarantor as determined by Lender in its reasonable discretion."),
        ("Section 13.6  Construction Delay Default",
         "The Project is more than ninety (90) days behind the construction schedule approved by Lender at any time during the "
         "Construction Period, or Substantial Completion has not occurred on or before the Construction Maturity Date, or any "
         "construction milestone in Schedule 1 is not achieved within sixty (60) days after the scheduled milestone date."),
        ("Section 13.7  Abandonment",
         "Borrower or the general contractor abandons the Project, suspends construction for more than fifteen (15) consecutive "
         "days (other than as a result of an event of force majeure approved in writing by Lender or a Lender-caused delay), or "
         "the Construction Contract is terminated for any reason."),
        ("Section 13.8  Insurance",
         "Borrower fails to maintain any insurance required by Schedule 5 or Article XVI, or any insurer cancels, does not renew "
         "or denies coverage with respect to any required policy and Borrower fails to obtain replacement coverage within ten "
         "(10) days."),
        ("Section 13.9  Single-Purpose Entity",
         "Borrower breaches any SPE Covenant set forth in Article XV, or fails to maintain its status as a single-purpose entity, "
         "or the independent manager resigns or is removed and is not replaced with a qualified independent manager within "
         "fifteen (15) days."),
        ("Section 13.10  Mezzanine Loan or Intercreditor Default",
         "A default or event of default occurs under the Mezzanine Documents or the Intercreditor Agreement, Mezzanine Lender "
         "commences any remedy or enforcement action, or any member grants or permits any lien on its membership interest other "
         "than as permitted by the Intercreditor Agreement."),
        ("Section 13.11  Environmental Default",
         "Any material violation of any Environmental Law or of any condition of the NFA Letter occurs with respect to the "
         "Property; any environmental order, notice of violation, directive, information request, demand, lien or proceeding is "
         "issued or commenced against Borrower or the Property; the NFA Letter is revoked, reopened, modified adversely or "
         "appealed; the Vapor Mitigation System, the Soil Management Plan or the deed notice is not installed, maintained, "
         "implemented or recorded as required; or any residential occupancy occurs in the Affected Area in violation of "
         "Section 12.2."),
        ("Section 13.12  Judgments",
         "One or more judgments, orders or decrees for the payment of money in an aggregate amount exceeding $500,000 is entered "
         "against Borrower or any Guarantor and remains unsatisfied, unbonded or unstayed on appeal for thirty (30) days."),
        ("Section 13.13  Guarantor Default",
         "Any Guarantor revokes, terminates, disaffirms or contests the validity or enforceability of any Guaranty, fails to "
         "maintain the liquidity required by Section 9.5, transfers a material portion of such Guarantor's assets outside the "
         "ordinary course of business, dies or becomes incapacitated, or is the subject of any criminal indictment or any "
         "proceeding that could reasonably be expected to result in a Material Adverse Effect."),
        ("Section 13.14  Financial Covenant Default",
         "Borrower fails to comply with any financial covenant in Article IX and does not cure such failure within the period "
         "provided in the applicable Section."),
        ("Section 13.15  Security Documents and Priority",
         "Any Loan Document ceases to be in full force and effect or is declared void or unenforceable; any lien or security "
         "interest granted to Lender ceases to be a valid first priority lien (subject only to the Permitted Exceptions); the "
         "Title Policy is not issued or is cancelled; or Borrower or any member asserts that any Loan Document is not binding."),
        ("Section 13.16  Invalidity of Environmental Compliance",
         "Any certificate, report or notice delivered under Article III, Article XII or Schedule 4 is materially inaccurate, or "
         "Borrower fails to deliver any report or certification required by Section 12.6 within the applicable period."),
    ]
    for h, t in eods:
        sec_h(doc, h)
        para(doc, t)
    para(doc, "Lender may waive any Event of Default only by a written instrument signed by an authorized officer of Lender, and "
              "no such waiver shall extend to any subsequent or other Event of Default or impair any consequent right.", space_before=6)
    para(doc, "[Drafting Note: Sections 15 and 16 of the Term Sheet summarize the Events of Default and remedies and state that "
              "they will be \u201cfully set forth in the definitive Loan Agreement.\u201d The Events of Default above expand those "
              "summaries in several respects, including the addition of a construction milestone default, an interest reserve "
              "non-replenishment default and an environmental compliance default. Borrower should review the additions. Note also "
              "that the final bullet of Section 15 of the Term Sheet refers to a Guarantor's net worth falling below \u201cthe "
              "minimum threshold set forth in Section 6.4,\u201d but Section 6.4 is a Borrower net worth covenant, not a Guarantor "
              "covenant. See Cover Memorandum Issue No. 19.]")

    # ---------------- ARTICLE XIV ----------------
    art(doc, "ARTICLE XIV — REMEDIES")
    sec_h(doc, "Section 14.1  Remedies Upon Default")
    para(doc, "Upon the occurrence and during the continuance of an Event of Default, Lender may, at its option and in addition to "
              "all other rights and remedies available at law or in equity, exercise any one or more of the following remedies, "
              "concurrently or successively, without notice except as required by applicable law:")
    for x in [
        "declare the entire outstanding principal balance of the Loan, all accrued and unpaid interest, the Exit Fee, all "
        "prepayment and other fees, and all other amounts payable under the Loan Documents to be immediately due and payable, "
        "whereupon the same shall become immediately due and payable without further presentment, demand, protest or notice of "
        "any kind, all of which are hereby waived;",
        "cease making Advances, cancel the Commitment and apply the Interest Reserve, the Contingency and the Equity Contribution "
        "as Lender determines;",
        "apply the Default Rate to all outstanding amounts;",
        "exercise all rights and remedies under the Deed of Trust, including causing the Trustee to institute a foreclosure "
        "proceeding by power of sale under Article 2A of Chapter 45 of the North Carolina General Statutes, and to conduct the "
        "sale in accordance with the notice, upset bid and confirmation procedures of N.C.G.S. Chapter 45;",
        "exercise all rights and remedies of a secured party under the Uniform Commercial Code, including the right to take "
        "possession of, collect, sell or otherwise dispose of the Collateral, and, with respect to the pledged membership "
        "interests, to exercise all voting and consensual rights and to transfer the pledged interests to Lender or its designee;",
        "apply to a court of competent jurisdiction for the appointment of a receiver for the Property, the Project, Borrower or "
        "the rents and profits thereof, without notice and without regard to the adequacy of the security, and Borrower consents "
        "to such appointment;",
        "enforce the Guaranties and the Environmental Indemnity against the Guarantors;",
        "sue for specific performance of any covenant, including the covenant to complete the Project; and",
        "collect the rents and profits of the Property, whether by direct collection, assignment or otherwise, and apply them as "
        "provided in Section 2.11.",
    ]:
        numbered(doc, "(a)", x, indent=0.55, hang=0.25)

    sec_h(doc, "Section 14.2  Cumulative Remedies; No Waiver")
    para(doc, "All rights and remedies of Lender under the Loan Documents are cumulative and not exclusive of any other right or "
              "remedy. No delay or failure by Lender in exercising any right or remedy shall operate as a waiver thereof, and no "
              "single or partial exercise shall preclude any other or further exercise. Lender may exercise remedies in any order "
              "and against any obligor or collateral without affecting its rights against any other obligor or collateral.")

    sec_h(doc, "Section 14.3  Application of Foreclosure Proceeds")
    para(doc, "Proceeds of any foreclosure sale, trustee's sale, UCC sale or other realization shall be applied in the order set "
              "forth in Section 2.11 and, in the case of a trustee's sale, in the order required by N.C.G.S. \u00a7 45-21.31. "
              "Borrower and each Guarantor acknowledge that, in any proceeding to determine a deficiency, the fair value of the "
              "Property may be established under N.C.G.S. \u00a7 45-21.36 and that the amount of any deficiency, and therefore the "
              "amount recoverable under the Guaranties, may be reduced accordingly.")

    sec_h(doc, "Section 14.4  Lender's Right to Cure")
    para(doc, "If Borrower fails to perform any obligation under the Loan Documents, Lender may (but shall not be obligated to) "
              "perform such obligation on Borrower's behalf, including paying taxes, insurance premiums, mechanics' liens or "
              "other claims, completing construction, curing any environmental violation or complying with any NCDEQ requirement, "
              "and all amounts so expended, together with interest at the Default Rate, shall be promptly reimbursed by Borrower "
              "and shall be secured by the Loan Documents. Lender's exercise of this right shall not cure any Event of Default or "
              "waive any right of Lender.")

    sec_h(doc, "Section 14.5  Setoff")
    para(doc, "Upon the occurrence and during the continuance of an Event of Default, Lender and its Affiliates are authorized at "
              "any time, without prior notice, to set off and apply any and all deposits, balances, credits or other property of "
              "Borrower or any Guarantor in the possession of Lender or any of its Affiliates against any amount then due under "
              "the Loan Documents, and each of Borrower and each Guarantor grants Lender a security interest in all such property "
              "to secure such obligations.")
