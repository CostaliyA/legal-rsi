from helpers import *

def blocks(doc):
    art(doc, "Article 2. Premises; Term; Conditions Precedent; Delivery")
    sec(doc, "2.1", "Lease of the Premises", "Landlord hereby leases the Premises to Tenant, and Tenant hereby "
        "leases the Premises from Landlord, together with all rights, easements, privileges and appurtenances "
        "thereto, including the bulkhead and all riparian and waterfront rights appurtenant to the Premises to the "
        "extent permitted by Applicable Law, for the Term and subject to the Permitted Exceptions and the terms and "
        "conditions of this Lease. Landlord reserves no right to use, occupy or enter upon the Premises except as "
        "expressly provided in this Lease.")
    sec(doc, "2.2", "Term", "The term of this Lease (the \"**Term**\") shall commence on the Lease Commencement Date "
        "and shall expire at 11:59 p.m. on September 30, 2124 (the \"**Expiration Date**\"), unless sooner terminated "
        "or extended in accordance with this Lease. The \"**Lease Commencement Date**\" shall be the later of "
        "(a) October 1, 2025, and (b) the date on which the conditions precedent set forth in Section 2.3 have been "
        "satisfied or waived in writing by the party entitled to the benefit thereof. No renewal, extension or "
        "purchase option is granted hereby except as expressly set forth in Section 2.7.")
    sec(doc, "2.3", "Conditions Precedent to Lease Commencement", "The obligation of each party to proceed to the "
        "Lease Commencement Date is conditioned upon satisfaction (or written waiver by the party entitled to the "
        "benefit thereof) of the following on or before the Lease Commencement Date:")
    cps = [
        "(a) Execution and delivery of this Lease by Landlord and Tenant, and adoption by the Board of Commissioners "
        "of Landlord of a resolution, in form reasonably satisfactory to Tenant, approving this Lease in its executed "
        "form and authorizing the Executive Director to execute and deliver this Lease, the SNDA, the Memorandum of "
        "Lease and each New Lease required under Article 9;",
        "(b) Delivery by Ridgepoint Title & Escrow Co. of a pro forma ALTA leasehold owner's policy (or an updated "
        "title commitment marked to issue) in the amount of not less than the total project cost, insuring Tenant's "
        "leasehold estate subject only to the Permitted Exceptions, with the ALTA 13-06 (Leasehold — Owner's) and "
        "environmental protection lien endorsements, and with the legal description corrected and conformed to "
        "**Exhibit A**;",
        "(c) Delivery of a current ALTA/NSPS Land Title Survey of the Premises satisfactory to Tenant, each Leasehold "
        "Mortgagee and the title company, and dated not more than ninety (90) days prior to the Lease Commencement "
        "Date;",
        "(d) Delivery by Tenant of the Letter of Credit (or the cash Security Deposit) required by Article 8;",
        "(e) Execution and delivery by Landlord of the SNDA in favor of the Construction Lender, in the form required "
        "by Article 9 and **Exhibit F**, and recordation thereof;",
        "(f) Execution and delivery by Landlord and the City of Port Calloway of the Tax Abatement Agreement in form "
        "and substance reasonably satisfactory to Tenant, providing for the Tax Abatement in accordance with "
        "Section 6.6;",
        "(g) Receipt by Tenant of all governmental approvals, permits and authorizations necessary to commence the "
        "Project, including final site plan approval, zoning approvals, building permits (or confirmation that "
        "building permit applications have been accepted for review), coastal and tidal wetlands approvals, and "
        "environmental approvals from DEEP, including approval of the Soil Management Plan and any approval required "
        "under the ELUR for ground disturbance; and",
        "(h) Discharge of record, or bonding in a manner reasonably satisfactory to Tenant, each Leasehold Mortgagee "
        "and the title company, of the mechanics' lien described in **Exhibit B**, Part 6, and delivery of evidence "
        "thereof.",
    ]
    for c in cps: sub(doc, c.split(")")[0] + ")", c.split(")", 1)[1].strip())
    para(doc, "If any condition precedent set forth in Section 2.3 (other than those set forth in Sections 2.3(a) and "
              "2.3(h), which are conditions to Tenant's obligation only) has not been satisfied or waived by "
              "December 31, 2025, then either party may, by written notice to the other, elect to (i) extend the date "
              "for satisfaction to a date not later than March 31, 2026, or (ii) terminate this Lease, whereupon the "
              "Security Deposit shall be returned to Tenant and neither party shall have any further obligation "
              "except for those obligations that expressly survive termination. The Exclusivity Period under the Term "
              "Sheet shall be deemed extended to correspond to any such extension.")
    sec(doc, "2.4", "Pre-Commencement Access License and Permitting Rights", "From and after the Effective Date and "
        "prior to the Lease Commencement Date, Landlord grants to Tenant and its consultants, surveyors, engineers, "
        "environmental scientists and contractors a non-exclusive license to enter upon the Premises for the purposes "
        "of survey, subsurface investigation, environmental sampling, geotechnical borings, bulkhead inspection, "
        "design, and the preparation and prosecution of permit applications, subject to Tenant's indemnity under "
        "Section 7.6 and Tenant's restoration of the Premises. Landlord shall, at Tenant's request and without charge, "
        "execute such consents, owner's authorizations, letters of authorization and permit applications as are "
        "reasonably necessary for Tenant to obtain governmental approvals, and shall join in any application that "
        "requires the signature of the fee owner. Tenant's rights under this Section 2.4 shall not constitute a "
        "leasehold interest or an obligation to pay Rent.")
    sec(doc, "2.5", "Rent Commencement Date; Partial Occupancy Protection",
        "The \"**Rent Commencement Date**\" shall be the earlier of (a) the date that is thirty-six (36) months after "
        "the Lease Commencement Date (which, if the Lease Commencement Date is October 1, 2025, is October 1, 2028) "
        "and (b) the Rent Trigger Date. The \"**Rent Trigger Date**\" means the first date on which Certificates of "
        "Occupancy have been issued for portions of the Project representing, in the aggregate, not less than fifty "
        "percent (50%) of the aggregate rentable square footage of all residential, office and retail space in the "
        "Project, determined on a building-by-building basis. If a Certificate of Occupancy is issued for less than "
        "such 50% threshold, no Rent shall accrue by reason thereof. During the period from the Lease Commencement "
        "Date to the Rent Commencement Date, Tenant shall have no obligation to pay Base Rent or Percentage Rent but "
        "shall be responsible for Impositions (subject to Article 6), insurance premiums and other carrying costs "
        "expressly allocated to Tenant under this Lease.")
    sec(doc, "2.6", "Lease Years and the Measurement Base", "Lease Year 1 shall commence on the Rent Commencement "
        "Date. For the avoidance of doubt: (a) Base Rent escalations, Rent Reset Dates, the commencement of "
        "Percentage Rent and all other Lease Year-based economic provisions of this Lease shall be measured from the "
        "Rent Commencement Date and not from the Lease Commencement Date; and (b) the Milestones, the Tax Abatement "
        "and the periods under Sections 10.5 and 10.6 shall be measured from the Lease Commencement Date as "
        "expressly provided in those provisions.")
    sec(doc, "2.7", "No Renewal; Tenant's Extension Option", "Tenant has no right to renew or extend the Term. "
        "[**Tenant position, to be negotiated:** Tenant shall have the right, exercisable by written notice delivered "
        "not less than twenty-four (24) months prior to the Expiration Date, to extend the Term for one (1) "
        "additional term of twenty-five (25) years on the same terms and conditions (including the then-current rent "
        "escalation and Percentage Rent mechanics, with the Breakpoint redetermined as provided in Section 5.3), "
        "provided that no Event of Default is then continuing. Any such extension shall be effected by a written "
        "supplemental lease, and Landlord shall execute and deliver the same within thirty (30) days following "
        "Tenant's notice.]")
    sec(doc, "2.8", "Landlord's Title and Authority", "Landlord represents, warrants and covenants that (a) it holds "
        "good and marketable fee simple title to the Premises free and clear of all liens and encumbrances other than "
        "the Permitted Exceptions; (b) it has full right, power and authority under Connecticut General Statutes "
        "§ 8-125 *et seq.* and its enabling resolutions to execute, deliver and perform this Lease and to grant the "
        "leasehold estate and the rights (including the New Lease right) contemplated hereby; (c) the execution, "
        "delivery and performance of this Lease have been duly authorized by all necessary action of its Board of "
        "Commissioners, and the resolutions effecting such authorization have not been amended, modified or "
        "rescinded; (d) no consent, approval or authorization of any governmental body is required in connection "
        "herewith that has not been obtained, other than as expressly described in Section 2.3; and (e) there is no "
        "existing lease, license, tenancy, option, right of first refusal (other than as described on **Exhibit B** "
        "and in Article 11), or other agreement granting any Person any interest in or right to acquire any interest "
        "in the Premises.")
    sec(doc, "2.9", "Delivery Condition of the Premises", "On the Lease Commencement Date, Landlord shall deliver, and "
        "Tenant shall accept, the Premises in their \"AS IS, WHERE IS\" condition, subject to the representations, "
        "warranties and covenants expressly set forth in this Lease and subject further to the following:")
    sub(doc, "(a)", "Landlord shall have discharged (or bonded, or obtained affirmative insurance over) the "
        "mechanics' lien filed by Calloway Marine Demolition Inc. on April 3, 2025 in the amount of $187,500 and "
        "recorded at Volume 418, Page 302 of the Port Calloway Land Records, at Landlord's sole cost, and shall "
        "deliver the leasehold title policy without exception therefor. Tenant shall have no obligation in respect "
        "of such lien, which arose from work performed for Landlord before the Effective Date.")
    sub(doc, "(b)", "Landlord shall, at its sole cost and expense, pay for the independent structural engineering "
        "assessment of the bulkhead recommended in the Phase II Environmental Site Assessment and shall, prior to "
        "the Lease Commencement Date, deliver such assessment to Tenant. [**Alternative position, to be negotiated:** "
        "Landlord shall repair or replace the bulkhead so as to put the approximately 480 linear feet of bulkhead and "
        "the associated backfill in a sound and watertight condition, including restoration of the approximately 40 "
        "linear feet of concrete cap removed by or for Landlord; and if Landlord fails to do so, Tenant may perform "
        "such work and receive a dollar-for-dollar credit against Base Rent (in addition to the Remediation Credit) "
        "for the reasonable cost thereof, together with interest at the Default Interest Rate.]")
    sub(doc, "(c)", "Landlord shall deliver to Tenant all environmental reports, LUST records, UST closure records, "
        "DEEP correspondence, ELUR files, and building and zoning department files in Landlord's possession or "
        "control relating to the Premises.")
    sec(doc, "2.10", "Memorandum of Lease; Recording", "Contemporaneously with the Lease Commencement Date, Landlord "
        "and Tenant shall execute, acknowledge and record in the Port Calloway Land Records a Memorandum of Ground "
        "Lease substantially in the form attached as **Exhibit G**, and each party shall execute and deliver such "
        "further recordable instruments (including any SNDA, New Lease, estoppel or subordination agreement) as the "
        "other party or any Leasehold Mortgagee may reasonably request. Tenant shall pay all recording fees; any "
        "Connecticut real estate conveyance tax payable upon the recording of this Lease shall be borne by Landlord "
        "except to the extent Applicable Law imposes it on Tenant. Neither party shall "
        "record this Lease itself without the written consent of the other party, except as required by Applicable "
        "Law or by any Leasehold Mortgagee.")

    # ================= ARTICLE 3 =================
    art(doc, "Article 3. Development, Milestones and Force Majeure")
    sec(doc, "3.1", "Tenant's Development Obligation", "Tenant shall use commercially reasonable efforts, consistent "
        "with prudent development practice and subject to receipt of the permits and approvals described in "
        "Section 2.3, to design, permit, construct and complete the Project substantially in accordance with the "
        "approved plans and specifications, applicable zoning and building requirements, the ELUR, and this Lease. "
        "Tenant shall have no obligation to commence or complete construction of any portion of the Project unless and "
        "until the conditions precedent in Section 2.3 have been satisfied or waived and the construction financing "
        "described in Recital E has closed.")
    sec(doc, "3.2", "Approval of Plans and Specifications", "Tenant shall submit to Landlord for informational "
        "purposes the site plan and exterior design of the Project as and when submitted to the City of Port Calloway "
        "for site plan review. Landlord's review of the site plan and exterior design shall be limited to "
        "confirmation of compliance with the requirements of Section 15.2 (Permitted Uses), Section 14.4 (Public Open Space) and "
        "Section 14.5 (Affordable Housing) of this Lease, and Landlord shall respond within ten (10) Business Days after "
        "receipt of any submission, failing which Landlord's approval shall be deemed given. Landlord shall have no "
        "right to review or approve interior layouts, unit mix (subject to Section 14.5), tenant improvements, "
        "construction means and methods, or any other matter except as expressly stated in this Section 3.2.")
    sec(doc, "3.3", "Development Milestones", "Tenant shall achieve each of the following Milestones by the "
        "corresponding Milestone Deadline (subject to extension as provided in Section 3.4):")
    table(doc,
          [["Milestone", "Requirement", "Months from Lease Commencement", "Milestone Deadline"],
           ["Milestone 1", "Commencement of Construction: the physical pouring of footings for at least one building "
            "within the Project, following issuance of all building permits necessary for such work",
            "18 months", "April 1, 2027"],
           ["Milestone 2", "Completion of Structural Frame of the Residential Tower (topping-out of structural steel "
            "and/or concrete frame)", "42 months", "April 1, 2029"],
           ["Milestone 3", "Substantial Completion of Phase 1 (Residential Tower and ground-floor retail)",
            "60 months", "October 1, 2030"],
           ["Milestone 4", "Substantial Completion of Phase 2 (Office Building)", "84 months", "October 1, 2032"]],
          [0.85, 2.95, 1.15, 1.55], size=8.5,
          caption="Table 3.3 — Development Milestones (also set forth on Exhibit C)")
    para(doc, "The dates in the final column assume a Lease Commencement Date of October 1, 2025. If the Lease "
              "Commencement Date differs, each deadline shall be recalculated by adding the corresponding number of "
              "months to the actual Lease Commencement Date, and the resulting dates shall be set forth on "
              "**Exhibit C**.")
    sec(doc, "3.4", "Extensions of Milestone Deadlines", "Each Milestone Deadline shall be extended as follows:")
    sub(doc, "(a)", "**Force Majeure.** Day for day for each day of delay caused by a Force Majeure Event, up to an "
        "aggregate maximum extension of twelve (12) months across all Milestones.")
    sub(doc, "(b)", "**Permitting Delays.** Day for day for each day of delay attributable to governmental permitting "
        "processes beyond Tenant's reasonable control (including delays in building, zoning, coastal, tidal wetlands, "
        "DEEP and ELUR-related approvals, and delays caused by appeals, third-party challenges or the absence of a "
        "quorum or meeting schedule of any governmental body), up to an aggregate maximum extension of six (6) "
        "months. The aggregate extension under Sections 3.4(a) and 3.4(b) shall not exceed eighteen (18) months.")
    sub(doc, "(c)", "**Landlord Delay.** Day for day for each day of Landlord Delay, without cap and in addition to "
        "the extensions under Sections 3.4(a) and 3.4(b).")
    sub(doc, "(d)", "**Tenant's Optional Paid Extensions.** [**Tenant position, to be negotiated:** Tenant may, by "
        "written notice delivered to Landlord not less than thirty (30) days prior to the applicable Milestone "
        "Deadline, extend Milestone 1 and/or Milestone 3 for up to two (2) successive periods of six (6) months each, "
        "upon payment to Landlord of an extension fee of $[●] for each such period, which fee shall be in lieu of, "
        "and not in addition to, any claim for damages arising from the delay. Any such extension shall be recorded "
        "by supplemental memorandum.]")
    para(doc, "Tenant shall give Landlord written notice of any Force Majeure Event or permitting delay within thirty "
              "(30) days after Tenant becomes aware of it, describing in reasonable detail its expected effect, but "
              "any failure to give timely notice shall not prejudice Tenant's right to an extension except to the "
              "extent, and only to the extent, that Landlord is actually prejudiced thereby.")
    sec(doc, "3.5", "Failure to Achieve Milestone 2 or Milestone 4", "Tenant's failure to achieve Milestone 2 or "
        "Milestone 4 by the applicable Milestone Deadline (as extended) shall not constitute an Event of Default, "
        "shall not give rise to any right of termination, reverter or forfeiture, and shall entitle Landlord only to "
        "written notice and consultation with Tenant regarding the reasons for the delay and Tenant's plan to achieve "
        "the Milestone. The parties acknowledge that Milestone 2 and Milestone 4 are schedule benchmarks and that the "
        "remedies in Article 10 are available only with respect to Milestone 1 and Milestone 3.")
    sec(doc, "3.6", "Phasing, Unit Mix and Changes", "Tenant may construct the Project in phases, may vary the "
        "sequence of construction, may change the unit mix, unit count, amenity program and retail configuration, and "
        "may make any other change to the design, plans or specifications, in each case without Landlord's consent, "
        "provided that (a) the Project continues to comply with Section 4 (Permitted Uses), Section 14.4 (Public Open "
        "Space), Section 14.5 (Affordable Housing), Article 15 (Compliance with Laws) and the ELUR, and (b) no such "
        "change materially and adversely affects the structural integrity of the bulkhead or the public's rights "
        "under the pedestrian access easement described on **Exhibit B**.")
    sec(doc, "3.7", "Landlord Cooperation", "Landlord shall cooperate in good faith with Tenant in connection with all "
        "permitting, approvals, utility applications, DEEP filings, coastal and floodplain approvals, and filings "
        "with the tax assessor, including by executing owner's authorizations, consents to the ELUR or Soil "
        "Management Plan, consents to subdivision or lot line adjustment if required, and any other instrument "
        "reasonably requested by a governmental authority, in each case within ten (10) Business Days after request "
        "and without charge.")
    sec(doc, "3.8", "No Landlord Funding Obligation", "Except as expressly provided in Article 7 (Remediation Credit) "
        "and Section 6.8 (Tax Abatement Backstop), Landlord shall have no obligation to fund any portion of the cost of "
        "the Project, the Environmental Remediation Work or the Public Open Space.")

    # ================= ARTICLE 4 =================
    art(doc, "Article 4. Base Rent, Escalations and Rent Resets")
    sec(doc, "4.1", "Covenant to Pay Rent", "From and after the Rent Commencement Date and throughout the balance of "
        "the Term, Tenant shall pay Base Rent and all other Rent to Landlord in lawful money of the United States, "
        "without demand, notice, deduction or setoff except as expressly provided in this Lease. All Rent shall be "
        "paid by wire transfer of immediately available funds to the account designated by Landlord in writing.")
    sec(doc, "4.2", "Initial Annual Base Rent", "The initial annual Base Rent shall be **Two Million Eight Hundred "
        "Fifty Thousand Dollars ($2,850,000)** (approximately $20.45 per square foot per annum based on 139,392 square "
        "feet), payable in equal monthly installments of **Two Hundred Thirty-Seven Thousand Five Hundred Dollars "
        "($237,500)**, commencing on the Rent Commencement Date and continuing through Lease Year 5. Base Rent shall "
        "be due on the first day of each calendar month, in advance.")
    sec(doc, "4.3", "Fixed Escalations (Lease Years 1 through 15)", "Base Rent shall escalate by two and one-half "
        "percent (2.5%) per annum, compounding annually, effective as of the first day of Lease Year 6 and the first "
        "day of Lease Year 11, in accordance with the following schedule (which schedule, together with Exhibit D, Part 1, "
        "controls in the event of any arithmetical inconsistency in the text of this Section 4.3):")
    table(doc,
          [["Lease Years", "Annual Base Rent", "Monthly Installment", "Computation"],
           ["1 through 5", "$2,850,000", "$237,500.00", "Initial annual Base Rent"],
           ["6 through 10", "$3,224,513", "$268,709.45", "$2,850,000 × (1.025)^5"],
           ["11 through 15", "$3,648,241", "$304,020.08", "$2,850,000 × (1.025)^10"]],
          [1.15, 1.3, 1.35, 2.2], size=9, align_right=[1, 2],
          caption="Table 4.3 — Base Rent, Lease Years 1 through 15 (see also Exhibit D, Part 1)")
    para(doc, "The amounts stated in the Term Sheet ($3,224,500 and $3,648,200, respectively) were rounded. The "
              "parties have recomputed the amounts specified in this Section 4.3 from the initial annual Base Rent and "
              "the stated 2.5% compounding rate, and the resulting amounts are $3,224,513 (a difference of $13 per "
              "annum) and $3,648,241 (a difference of $41 per annum). The parties agree that the schedule above "
              "reflects their intent that Base Rent escalate at exactly 2.5% per annum, compounded annually, from the "
              "initial annual Base Rent.")
    sec(doc, "4.4", "Rent Resets (Lease Year 16 and Thereafter)", "Effective as of the first day of each Rent Reset "
        "Date, Base Rent shall be reset to the greater of:")
    sub(doc, "(a)", "the amount that would result from the continued application of the two and one-half percent "
        "(2.5%) per annum compounding fixed escalation to the initial annual Base Rent of $2,850,000, calculated as of "
        "the applicable Rent Reset Date; and")
    sub(doc, "(b)", "the initial annual Base Rent of $2,850,000, adjusted by the cumulative percentage increase in the "
        "Consumer Price Index for All Urban Consumers, Northeast Region (CPI-U Northeast, Series ID CUUR0100SA0), as "
        "published by the United States Bureau of Labor Statistics, **from the Rent Commencement Date** through the "
        "Rent Reset Date.")
    para(doc, "The following provisions shall apply to each Rent Reset:")
    sub(doc, "(c)", "**Base month.** The base index month for each calculation shall be the third calendar month "
        "preceding the Rent Commencement Date, and the reset index month shall be the third calendar month preceding "
        "the applicable Rent Reset Date.")
    sub(doc, "(d)", "**No reduction; no compounding of reset amounts.** Base Rent shall not be reduced as a result of "
        "any Rent Reset, and the escalation under Section 4.4(a) shall be computed from the initial annual Base Rent "
        "and not from any previously reset amount.")
    sub(doc, "(e)", "**Successor index.** If the CPI-U Northeast ceases to be published, or if its methodology is "
        "materially revised, the parties shall use the most comparable successor index published by the Bureau of "
        "Labor Statistics, or if none, an index reasonably selected by Landlord and approved by Tenant (not to be "
        "unreasonably withheld).")
    sub(doc, "(f)", "**Dispute resolution.** If the parties disagree as to the amount of any reset, Tenant may pay Base "
        "Rent at the level determined by Tenant in good faith pending resolution, and any shortfall shall be paid "
        "within thirty (30) days after resolution, without interest or penalty.")
    sub(doc, "(g)", "**Landlord's records.** Landlord shall deliver to Tenant its calculation of each reset not less "
        "than sixty (60) days prior to the applicable Rent Reset Date.")
    note(doc, "[**Tenant position, to be negotiated:** Because Sections 4.4(a) and 4.4(b) each index from the "
              "initial annual Base Rent, Base Rent will be flat for each ten-year period and then increase by the full "
              "cumulative index in a single step on each Rent Reset Date (approximately 28% at 2.5% annual "
              "inflation). Tenant proposes, in the alternative, that Base Rent be adjusted annually on each "
              "anniversary of the Rent Commencement Date by the greater of (i) 2.0% and (ii) the increase in the CPI-U "
              "Northeast, subject to a collar of 0% floor and 4.0% ceiling, compounded annually. Tenant's alternative "
              "is economically equivalent over the Term at long-run average inflation but eliminates the reset cliffs "
              "and improves debt-service coverage stability for each Leasehold Mortgagee.]")

    sec(doc, "4.5", "Payment Mechanics; Partial Months", "If the Rent Commencement Date or any Rent Reset Date is not "
        "the first day of a calendar month, the Rent for the partial month shall be prorated on a per diem basis. "
        "Tenant's obligation to pay Rent is an independent covenant.")
    sec(doc, "4.6", "Setoff", "Notwithstanding Section 4.1, Tenant may set off against Base Rent next coming due "
        "(a) any amount due from Landlord under Section 6.8 (Tax Abatement Backstop), Section 7.5 (environmental "
        "indemnity) or Section 2.9(b) (bulkhead credit), in each case together with interest at the Default Interest "
        "Rate; (b) any amount reasonably and in good faith determined by Tenant to be owed by Landlord under this "
        "Lease that Landlord has failed to pay within thirty (30) days after written demand; and (c) any amount "
        "expended by Tenant to cure a Landlord default under Section 10.10. Tenant shall give simultaneous written "
        "notice of any setoff to each Leasehold Mortgagee, and no setoff shall exceed, in any single month, "
        "twenty-five percent (25%) of the monthly Base Rent then due unless Landlord has failed to pay a liquidated "
        "amount within sixty (60) days after written demand.")
    sec(doc, "4.7", "Late Payment; Interest", "Any installment of Rent not received within five (5) Business Days "
        "after its due date shall bear interest from the due date at a rate equal to the lesser of (a) the prime rate "
        "published in *The Wall Street Journal* plus four percent (4%) per annum and (b) the maximum rate permitted by "
        "Applicable Law (the \"**Default Interest Rate**\"). Interest shall accrue on a daily basis. No late charge "
        "shall be imposed except as provided in this Section 4.7. Landlord shall provide written notice of any "
        "delinquency and a period of five (5) Business Days to cure before any monetary default is deemed to exist.")
    sec(doc, "4.8", "Application of Payments", "Landlord shall apply all payments received first to costs and interest "
        "then due, then to the most recently accrued Rent. Landlord may not apply any payment to a disputed amount "
        "while a dispute is pending under Section 20.2.")
    sec(doc, "4.9", "Rent Absolutely Net", "Except as expressly provided in Article 6, Article 7, Section 10.10 and "
        "Article 13, this Lease is intended to be a \"triple-net\" lease, and Tenant shall pay all costs and expenses "
        "relating to the Premises and the Improvements, and Landlord shall receive the Rent free of any deduction, "
        "abatement, counterclaim or setoff.")

    # ================= ARTICLE 5 =================
    art(doc, "Article 5. Percentage Rent and Gross Revenues")
    sec(doc, "5.1", "Percentage Rent", "Commencing with Lease Year 6 and continuing for the balance of the Term, Tenant "
        "shall pay to Landlord, as additional Rent, percentage rent equal to **two percent (2.0%) of Gross Revenues "
        "in excess of the Breakpoint** for the applicable Lease Year (\"**Percentage Rent**\") (see Exhibit D, Parts 3 and 4). Percentage Rent shall "
        "be payable annually, within ninety (90) days after the end of each Lease Year, together with the statement "
        "required by Section 5.4. No Percentage Rent shall be payable for any period prior to Lease Year 6.")
    sec(doc, "5.2", "Gross Revenues", "\"**Gross Revenues**\" means the gross rents, fees, charges and other income "
        "actually collected by Tenant and its Affiliates from the operation of the Project, determined on a cash basis "
        "and at the Project level only (and excluding any income of Tenant or its Affiliates from any other property "
        "or business). Gross Revenues **include** only: residential rents; office rents; retail rents; percentage rent "
        "and overage rent paid by subtenants; parking revenues; amenity and service fees; and rent from cell tower, "
        "rooftop, signage and similar licenses. Gross Revenues **exclude**, without limitation:")
    excl = [
        "security deposits (unless and until applied to rent in accordance with the applicable sublease);",
        "reimbursements from subtenants for common area maintenance, real estate taxes, insurance, utilities, "
        "operating expenses, capital expenditures or other pass-throughs that are not true revenue to Tenant;",
        "utility reimbursements and recoveries of any kind;",
        "proceeds of insurance (including business interruption and rent loss insurance), condemnation awards, and "
        "proceeds of any warranty, guaranty, indemnity or litigation;",
        "interest and other income earned on reserves, escrows and deposits;",
        "loan proceeds, capital contributions, member loans and other financing or equity inflows;",
        "proceeds from the sale or other disposition of any asset, and any gain on sale;",
        "rent attributable to any period before the Rent Commencement Date, and any free rent, abated rent, "
        "concessions, tenant improvement allowances or similar inducements, valued at the amount actually collected;",
        "amounts billed but not collected, and any rent that Tenant determines in good faith to be uncollectible, "
        "provided that any subsequent collection shall be included in Gross Revenues for the Lease Year of "
        "collection;",
        "sales, use, excise and other taxes collected from subtenants and remitted to taxing authorities;",
        "the value of any real property tax abatement, exemption or incentive, including the Tax Abatement;",
        "charges for after-hours HVAC, overtime services and other services billed at cost;",
        "subtenant security forfeitures and late fees (except to the extent applied to rent);",
        "any amount received from Landlord, the City of Port Calloway or any other governmental authority; and",
        "any other item that is not true, recurring operating revenue of the Project from third parties.",
    ]
    for i, e in enumerate(excl):
        sub(doc, "(%s)" % chr(97 + i), e, level=2)
    para(doc, "No deduction shall be taken more than once, and Gross Revenues shall be determined without regard to "
              "any straight-lining, leveling or GAAP rent-adjustment convention.")
    sec(doc, "5.3", "Breakpoint Adjustment", "The Breakpoint shall be **$28,500,000** for Lease Year 6. Effective as "
        "of the first day of each Rent Reset Date thereafter, the Breakpoint shall be reset to an amount equal to "
        "$28,500,000 multiplied by a fraction, the numerator of which is the Base Rent payable for the Lease Year "
        "commencing on such Rent Reset Date and the denominator of which is $3,224,513 (being the Base Rent for Lease "
        "Year 6), such that the ratio of the Breakpoint to Base Rent in effect for Lease Year 6 is preserved for the "
        "balance of the Term.")
    note(doc, "[**Tenant position, to be negotiated.** The Term Sheet fixes the Breakpoint at $28,500,000 \"for the "
              "duration of the Lease Term.\" Because Base Rent escalates while the Breakpoint does not, a fixed "
              "Breakpoint erodes in real terms from approximately 8.8 times Base Rent in Lease Year 6 to less than "
              "1.0 times Base Rent by Lease Year 96 (see the model in the accompanying issues memorandum). At that "
              "point Percentage Rent operates as a tax on substantially all gross revenue rather than a sharing of "
              "upside. Tenant proposes the indexing mechanic above. Tenant's fallback positions, in order of "
              "preference, are: (i) index the Breakpoint to the CPI-U Northeast on the same schedule as the Rent "
              "Resets; (ii) step the Percentage Rent rate down over time (2.0% for Lease Years 6–25; 1.5% for Lease "
              "Years 26–50; 1.0% thereafter); or (iii) cap aggregate Percentage Rent in any Lease Year at an amount "
              "equal to twenty-five percent (25%) of Base Rent for such Lease Year.]")
    sec(doc, "5.4", "Statements", "Each payment of Percentage Rent shall be accompanied by a statement of Gross "
        "Revenues for the applicable Lease Year, certified as true and correct in all material respects by an "
        "authorized financial officer of Tenant, setting forth in reasonable detail the computation of Gross Revenues, "
        "each exclusion taken, and the resulting Percentage Rent. If no Percentage Rent is payable, Tenant shall "
        "deliver a statement so indicating. Tenant shall maintain complete and accurate books and records relating to "
        "Gross Revenues for not less than three (3) years after the end of each Lease Year.")
    sec(doc, "5.5", "Accounting Principles", "Gross Revenues shall be determined in accordance with sound and "
        "consistent accounting practices applied uniformly from year to year, on a cash basis, consistently with "
        "Tenant's audited project-level financial statements. Where this Lease and such practices conflict, this Lease "
        "controls.")
    sec(doc, "5.6", "Landlord's Audit Right", "Landlord may, not more than once in any twelve (12) month period and not "
        "more than once with respect to any Lease Year, and upon not less than thirty (30) days' prior written notice, "
        "cause an independent certified public accountant reasonably acceptable to Tenant to audit Tenant's books and "
        "records relating to Gross Revenues for any Lease Year ending not more than twenty-four (24) months before the "
        "date of the notice. Each audit shall be conducted during normal business hours at Tenant's principal place of "
        "business, shall be limited in scope to the determination of Gross Revenues, shall be conducted under a "
        "customary confidentiality undertaking, and shall be at Landlord's sole cost and expense unless the audit "
        "discloses an underpayment of Percentage Rent of five percent (5%) or more for the audited Lease Year, in "
        "which case Tenant shall reimburse Landlord's reasonable, documented out-of-pocket audit costs. No auditor "
        "shall be compensated on a contingency basis. Landlord shall have no right to audit Tenant's consolidated or "
        "affiliate-level records.")
    sec(doc, "5.7", "Overpayment; Underpayment", "If any statement or audit shows an overpayment, Tenant may credit "
        "the overpayment against the next installment(s) of Rent. If any statement or audit shows an underpayment, "
        "Tenant shall pay the shortfall within thirty (30) days after delivery of the audit, without interest unless "
        "the underpayment exceeds five percent (5%) of the Percentage Rent properly payable, in which case interest "
        "shall accrue at the Default Interest Rate from the original due date.")
    sec(doc, "5.8", "Confidentiality of Financial Statements", "Landlord shall treat all statements and audit results "
        "delivered under this Article 5 as confidential and shall not disclose them except (a) to its commissioners, "
        "officers, employees, attorneys, auditors and financial advisors who need to know, (b) as required by the "
        "Connecticut Freedom of Information Act or other Applicable Law, or (c) in connection with the enforcement of "
        "this Lease. Landlord shall, prior to any disclosure under clause (b), notify Tenant and cooperate with "
        "Tenant's reasonable efforts to obtain confidential treatment.")
