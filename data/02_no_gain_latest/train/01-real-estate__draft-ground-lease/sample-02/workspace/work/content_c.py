from helpers import *

def blocks(doc):
    art(doc, "Article 6. Impositions and the Tax Abatement")
    sec(doc, "6.1", "Triple-Net Obligation", "Subject to Sections 6.3 and 6.8, Tenant shall pay, before delinquency "
        "and without demand, all Impositions levied or assessed against the Premises, the Improvements, the leasehold "
        "estate, or this Lease, and all Impositions asserted against Landlord arising from Landlord's ownership of the "
        "Premises (other than Landlord's income, franchise, inheritance and transfer taxes).")
    sec(doc, "6.2", "Impositions", "\"**Impositions**\" means all ad valorem real property taxes, general and special "
        "assessments, benefit assessments, sewer, water and utility charges, business improvement district charges, "
        "and any other governmental charge, fee or imposition of every kind now or hereafter levied upon the Premises, "
        "the Improvements or the leasehold estate, together with all interest and penalties thereon, and including "
        "Tenant's share of any assessment benefiting the Premises.")
    sec(doc, "6.3", "Exclusions", "Impositions shall **not** include: (a) Landlord's income, franchise, inheritance, "
        "estate, gift, corporate or transfer taxes; (b) any tax or charge based on Landlord's net income or receipts "
        "(other than any rent or receipts tax expressly measured by rent from the Premises and imposed on the landlord "
        "as such); (c) any principal, interest or other amounts payable under any mortgage or other financing of "
        "Landlord; (d) any charge arising from Landlord's own act, negligence or violation of Applicable Law, or from "
        "any condition existing before the Lease Commencement Date; (e) any penalty or interest attributable to "
        "Landlord's failure to deliver a bill or notice to Tenant within a reasonable time; and (f) any documentary "
        "stamp, conveyance or recording tax payable on the recording of this Lease or the Memorandum of Lease, which "
        "shall be borne by Landlord except as provided in Section 2.10.")
    sec(doc, "6.4", "Contest and Payment", "Tenant may, at its sole cost and in its own name or, if required, in "
        "Landlord's name (with Landlord's reasonable cooperation and without expense to Landlord), contest by "
        "appropriate proceedings the validity or amount of any Imposition, and may defer payment during the pendency "
        "of any such contest provided that Tenant furnishes such security as is reasonably required to prevent "
        "delinquency, lien or sale. Tenant may pay any special assessment in installments over the longest period "
        "permitted by Applicable Law. Landlord shall deliver to Tenant copies of all tax bills, assessment notices and "
        "assessor communications within ten (10) Business Days after receipt.")
    sec(doc, "6.5", "Proration", "Impositions for the fiscal year in which the Lease Commencement Date, the Rent "
        "Commencement Date, the Termination Date or the Expiration Date occurs shall be prorated between Landlord and "
        "Tenant as of such date on a per diem basis based on the bills for the applicable fiscal year (or, if not yet "
        "issued, on the most recent available bills, subject to reproration).")
    sec(doc, "6.6", "Tax Abatement", "Landlord shall cause the City of Port Calloway to grant to Tenant a fifteen "
        "(15) year phased abatement of real property taxes applicable to the Premises and the Improvements, pursuant to "
        "which the taxable portion of the Assessor's assessed value of the Premises and the Improvements shall be as "
        "follows for each year of the Tax Abatement Period:")
    table(doc,
          [["Years of Tax Abatement Period", "Percentage of Assessed Value Subject to Tax",
            "Estimated Annual Taxes at Projected $178,000,000 Assessed Value and 34.75 Mills"],
           ["1 through 5", "25%", "$1,546,375"],
           ["6 through 10", "50%", "$3,092,750"],
           ["11 through 15", "75%", "$4,639,125"],
           ["16 and thereafter", "100% (no abatement)", "$6,185,500"]],
          [1.65, 1.75, 2.65], size=9, align_right=[1, 2],
          caption="Table 6.6 — Tax Abatement Schedule (estimated amounts are illustrative only)")
    para(doc, "The dollar amounts in the third column are estimates computed from the Authority's projected "
              "post-development assessed value of $178,000,000 and the current mill rate of 34.75 mills, as stated in "
              "the Term Sheet. The abatement shall apply to the assessed value actually determined by the Port "
              "Calloway Tax Assessor from time to time, and the parties acknowledge that actual assessed values and "
              "mill rates will vary over the Term. In no event shall the percentage of assessed value subject to tax "
              "in any year of the Tax Abatement Period exceed the applicable percentage set forth above.")
    sec(doc, "6.7", "Abatement Commencement Date", "The \"**Tax Abatement Period**\" shall be the fifteen (15) "
        "consecutive full fiscal years of the City of Port Calloway commencing on the \"**Abatement Commencement "
        "Date**,\" which shall be the later of (a) the Rent Commencement Date and (b) the first day of the City of Port "
        "Calloway fiscal year in which the first assessment by the Port Calloway Tax Assessor that reflects the "
        "completed Improvements becomes effective. The parties agree that the Tax Abatement is intended to benefit "
        "Tenant during the operating years of the Project and that no portion of the Tax Abatement Period shall be "
        "consumed during the construction period before the Improvements are reflected in the tax assessment.")
    sec(doc, "6.8", "Tax Abatement Backstop", "If (a) the Tax Abatement Agreement has not been executed and delivered "
        "by the City of Port Calloway on or before the Lease Commencement Date, (b) the Tax Abatement is not "
        "implemented in accordance with Section 6.6 for any fiscal year during the Tax Abatement Period, or (c) the Tax "
        "Abatement is repealed, reduced, suspended or otherwise rendered ineffective in whole or in part (unless "
        "caused solely by Tenant's failure to comply with the conditions of the Tax Abatement Agreement), then Tenant "
        "shall be entitled to a credit against the next installments of Base Rent in an amount equal to the excess of "
        "(i) the real property taxes actually payable by Tenant for the affected fiscal year over (ii) the taxes that "
        "would have been payable had the Tax Abatement been implemented in accordance with Section 6.6, and Landlord "
        "shall reimburse Tenant for any such excess that cannot be so credited within thirty (30) days after written "
        "demand. Landlord shall not support, petition for or consent to any repeal, reduction or suspension of the Tax "
        "Abatement during the Tax Abatement Period.")
    sec(doc, "6.9", "Landlord's Undertakings", "Landlord acknowledges that the Tax Abatement is to be granted and "
        "administered by the City of Port Calloway and not by Landlord. Landlord shall use diligent efforts to obtain "
        "all approvals and authorizations necessary to implement the Tax Abatement, including any required action of "
        "the Port Calloway Board of Finance, the City Council, the Port Calloway Tax Assessor and the Connecticut "
        "Office of Policy and Management, and shall notify Tenant promptly of any condition, hearing or approval "
        "required. Landlord shall render all assistance reasonably requested by Tenant in connection with any "
        "application, hearing, appeal, assessment challenge or administrative proceeding relating to the Tax Abatement "
        "or the assessment of the Premises.")

    # ================= ARTICLE 7 =================
    art(doc, "Article 7. Environmental Matters and the Remediation Credit")
    sec(doc, "7.1", "Acknowledgments", "The parties acknowledge that (a) the Premises were operated as a ship repair "
        "and dry dock facility from approximately 1942 through 1987; (b) the Phase II Environmental Site Assessment "
        "dated May 2, 2025 identified petroleum hydrocarbon contamination in an approximately 4,200 square foot area "
        "in the northwest corner of the Premises (maximum total petroleum hydrocarbons of 3,800 mg/kg) and an "
        "approximately 1,600 square foot area in the former dry dock area (maximum total petroleum hydrocarbons of "
        "1,200 mg/kg), in each case exceeding the Connecticut Remediation Standard Regulations Residential Direct "
        "Exposure Criteria of 500 mg/kg; (c) the Halcyon cost estimate of $2,400,000 ($1,850,000 for the northwest "
        "corner area and $550,000 for the former dry dock area) is a preliminary, opinion-level estimate and not a "
        "guaranteed maximum price; (d) the ELUR imposes use restrictions, engineered barrier requirements, ground "
        "disturbance limitations, a prohibition on potable water supply wells, and annual compliance certification "
        "obligations; and (e) all of the foregoing constitute Pre-Existing Environmental Conditions for which Tenant "
        "bears no responsibility except as expressly allocated in this Article 7.")
    sec(doc, "7.2", "Remediation Credit", "Landlord shall provide to Tenant a credit against Base Rent in the aggregate "
        "amount of **One Million Eight Hundred Thousand Dollars ($1,800,000)** (the \"**Remediation Credit**\"), "
        "which shall be applied against the first monthly installments of Base Rent due after the Rent Commencement "
        "Date as follows:")
    table(doc,
          [["Monthly Installment after Rent Commencement Date", "Base Rent Due", "Remediation Credit Applied",
            "Tenant Payment"],
           ["Months 1 through 7", "$237,500 each", "$237,500 each ($1,662,500 total)", "$0"],
           ["Month 8", "$237,500", "$137,500", "$100,000"],
           ["Month 9 and thereafter", "$237,500 (subject to escalation)", "None", "$237,500"]],
          [1.9, 1.35, 1.75, 1.0], size=8.5, align_right=[1, 2, 3],
          caption="Table 7.2 — Application of the Remediation Credit")
    para(doc, "The Remediation Credit shall not reduce or be reduced by any other credit, offset or abatement under "
              "this Lease, including the Tax Abatement Backstop under Section 6.8. If this Lease expires or is "
              "terminated for any reason before the Remediation Credit has been fully applied, Landlord shall pay to "
              "Tenant, in cash within thirty (30) days after the Expiration Date or Termination Date, the amount of "
              "the Remediation Credit that remains unapplied. If Base Rent is insufficient to absorb the Remediation "
              "Credit in any month (by reason of setoff, abatement or otherwise), Tenant may apply the unabsorbed "
              "portion against any other Rent next coming due, and Landlord shall pay any remainder in cash within "
              "thirty (30) days after written demand. The Remediation Credit is a payment obligation of Landlord and "
              "not merely a rent concession, and it survives any termination of this Lease.")
    sec(doc, "7.3", "Environmental Remediation Work", "Tenant shall perform, or cause to be performed, the "
        "excavation and off-site disposal of contaminated soil in the two areas identified in the Phase II "
        "Environmental Site Assessment, together with such additional investigation, remediation, confirmation "
        "sampling, backfill, capping, monitoring and reporting as is required to achieve compliance with the "
        "Connecticut Remediation Standard Regulations and the ELUR and to obtain a DEEP approval of the remediation "
        "(collectively, the \"**Environmental Remediation Work**\"). The Environmental Remediation Work shall be "
        "performed in conjunction with the Project's site development earthwork where practicable, under a "
        "DEEP-approved Remedial Action Plan and Soil Management Plan, and under the oversight of a Licensed "
        "Environmental Professional engaged by Tenant. Tenant shall deliver to Landlord copies of the Remedial Action "
        "Plan, the Soil Management Plan, all confirmation sampling results and any post-remediation verification report "
        "within ten (10) Business Days after submission to or receipt from DEEP.")
    sec(doc, "7.4", "Allocation of Environmental Costs", "The cost of the Environmental Remediation Work shall be "
        "allocated as follows:")
    sub(doc, "(a)", "Landlord shall bear $1,800,000 of the estimated cost through the Remediation Credit, and Tenant "
        "shall bear the remaining $600,000 of the $2,400,000 estimate, in each case as set forth in Section 7.2.")
    sub(doc, "(b)", "Subject to Sections 7.4(c) and 7.4(d), Tenant shall bear actual costs of the Environmental "
        "Remediation Work in excess of $2,400,000.")
    sub(doc, "(c)", "Landlord shall bear all costs of the Environmental Remediation Work attributable to a "
        "Pre-Existing Environmental Condition that was not identified, delineated or quantified in the Phase II "
        "Environmental Site Assessment, including contamination discovered outside the two delineated areas, "
        "contamination extending beyond the depths described in the Phase II report, off-site migration, sediment or "
        "groundwater impacts, contamination attributable to the former underground storage tanks or the dry dock "
        "beyond the delineated areas, and any DEEP-imposed requirement (including any requirement to remediate to "
        "unrestricted-use or Residential Direct Exposure Criteria, or to address the engineered barrier as a "
        "condition of ground disturbance) that was not contemplated by the Phase II Environmental Site Assessment, "
        "and Landlord shall reimburse Tenant for such costs within thirty (30) days after written demand with "
        "supporting documentation.")
    sub(doc, "(d)", "Tenant shall bear the incremental costs of the Environmental Remediation Work attributable to "
        "Tenant's design, means and methods, or the negligent or improper performance of the work (including, for "
        "example, over-excavation required by Tenant's below-grade parking configuration beyond that required by "
        "Applicable Law, but excluding the volume of contaminated soil and fill that must be removed or managed to "
        "comply with Applicable Law and the ELUR in connection with Tenant's approved development program).")
    sub(doc, "(e)", "If the actual cost of the Environmental Remediation Work is less than $2,400,000, Tenant shall "
        "retain the benefit of the difference; the Remediation Credit is a fixed dollar amount and shall not be "
        "reduced by reason of any such saving.")
    sec(doc, "7.5", "Landlord Environmental Indemnity", "Landlord shall indemnify, defend (with counsel reasonably "
        "acceptable to Tenant) and hold harmless Tenant, its members, managers, officers, employees, agents, "
        "contractors and each Leasehold Mortgagee from and against all claims, liabilities, losses, damages, penalties, "
        "fines, costs and expenses (including reasonable attorneys' and consultants' fees, and natural resource "
        "damages) arising out of or relating to (a) any Pre-Existing Environmental Condition, (b) any violation of "
        "Environmental Laws or the ELUR occurring before the Lease Commencement Date, (c) any act or omission of "
        "Landlord or its predecessors, agents or contractors with respect to Hazardous Materials at the Premises, "
        "(d) Landlord's failure to perform its obligations under this Article 7, and (e) any claim by a third party "
        "(including any former owner or operator of the Premises or any governmental authority) relating to any of "
        "the foregoing. Landlord's obligations under this Section 7.5 shall not be limited by, and shall be in "
        "addition to, the Remediation Credit.")
    sec(doc, "7.6", "Tenant Environmental Indemnity", "Tenant shall indemnify, defend and hold harmless Landlord from "
        "and against all claims, liabilities, losses, damages, costs and expenses arising out of or relating to "
        "(a) Hazardous Materials introduced at, on, under or migrating from the Premises by Tenant or its agents, "
        "contractors, subtenants or invitees after the Lease Commencement Date, (b) Tenant's failure to perform the "
        "Environmental Remediation Work in compliance with Environmental Laws, the ELUR and this Lease, and (c) "
        "Tenant's breach of this Article 7. Tenant's indemnity shall not apply to any Pre-Existing Environmental "
        "Condition or to any matter for which Landlord is obligated to indemnify Tenant under Section 7.5. Tenant's "
        "aggregate liability under this Section 7.6 shall not exceed [**Tenant position:** $[●], escalated annually by "
        "the CPI-U Northeast, together with available environmental insurance proceeds].")
    sec(doc, "7.7", "ELUR Compliance", "Tenant shall, at its sole cost, comply with all restrictions, obligations and "
        "activity and use limitations of the ELUR for the Term, including (a) maintaining an engineered barrier "
        "consisting of not less than twenty-four (24) inches of documented clean fill or an equivalent "
        "geomembrane/concrete barrier system over all areas requiring a barrier; (b) conducting annual inspections of "
        "the barrier; (c) reporting any breach or compromise of the barrier to DEEP within thirty (30) days after "
        "discovery and repairing it within ninety (90) days after discovery (or such longer period as DEEP may "
        "approve); (d) performing no ground disturbance below a depth of two (2) feet below existing grade except in "
        "accordance with a DEEP-approved Soil Management Plan; (e) installing no potable water supply wells on the "
        "Premises and obtaining all water supply from the municipal water system; (f) submitting the annual ELUR "
        "compliance certification to DEEP; and (g) giving DEEP notice of any change in use as required by the ELUR. "
        "Landlord shall cooperate with and join in any filing or certification that requires the signature of the fee "
        "owner, within ten (10) Business Days after request.")
    sec(doc, "7.8", "Ground-Floor Uses; ELUR Interpretation", "The parties acknowledge the interpretive ambiguity "
        "identified in the Phase II Environmental Site Assessment regarding whether non-habitable ancillary spaces "
        "serving a residential tower (including a residential lobby, mail room, package room, resident lounge, fitness "
        "center and leasing office) constitute \"residential use\" for purposes of the ELUR, which prohibits "
        "residential use on the ground floor. Landlord acknowledges that this Lease permits such ancillary spaces and "
        "ground-floor retail and commercial uses, and agrees that:")
    sub(doc, "(a)", "Landlord shall, at Tenant's request, join in and support an application to DEEP for a formal "
        "interpretation, variance or modification of the ELUR to confirm the permissibility of the ground-floor "
        "lobby, amenity and retail program contemplated by this Lease, and Landlord shall bear the reasonable costs of "
        "such application (including DEEP fees and third-party consultant costs) to the extent the application is "
        "required solely because of the Pre-Existing Environmental Condition.")
    sub(doc, "(b)", "If DEEP determines that any portion of Tenant's ground-floor program constitutes residential use "
        "prohibited by the ELUR, Tenant may redesign that portion of the Project to comply, and any resulting delay "
        "shall constitute a Force Majeure Event and a permitting delay for purposes of Section 3.4, and Tenant shall "
        "not be in default hereunder by reason thereof.")
    sub(doc, "(c)", "For the avoidance of doubt, Tenant's design shall place all dwelling units on floors two (2) and "
        "above, and the Project's finished floor elevation at the ground-floor level shall be not less than fifteen "
        "(15) feet NAVD88, as required by Section 15.3.")
    sec(doc, "7.9", "Environmental Insurance", "Tenant shall maintain pollution legal liability insurance satisfying "
        "Section 12.1(f). All proceeds of any environmental insurance applicable to a Pre-Existing Environmental "
        "Condition shall be applied first to the cost of the Environmental Remediation Work, and Tenant shall be "
        "entitled to a credit against Base Rent for any such proceeds applied to costs that Tenant would otherwise "
        "have borne.")
    sec(doc, "7.10", "Landlord's Access and Monitoring", "Landlord and its consultants may, upon not less than five (5) "
        "Business Days' prior notice and subject to Tenant's reasonable construction and safety requirements, inspect "
        "the Premises and review Tenant's environmental records not more than twice in any calendar year, at "
        "Landlord's cost, and subject to a customary confidentiality undertaking. Landlord shall not perform any "
        "invasive sampling or ground disturbance without Tenant's prior written consent.")
    sec(doc, "7.11", "Survival", "The obligations of the parties under this Article 7 shall survive the expiration or "
        "termination of this Lease for so long as any claim may be asserted.")
