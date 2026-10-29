from helpers import *

def blocks(doc):
    art(doc, "Article 11. Assignment, Subletting, Permitted Transfers and Right of First Refusal")
    sec(doc, "11.1", "Assignment", "Tenant may not assign this Lease or any interest in it to a Person that is not an "
        "Affiliate of Tenant without Landlord's prior written consent, which consent shall not be unreasonably "
        "withheld, conditioned or delayed, and subject to the ROFR set forth in Section 11.5. Any purported assignment "
        "in violation of this Article 11 shall be void.")
    sec(doc, "11.2", "Subletting and Occupancy", "Tenant may sublease or license individual dwelling units, office "
        "suites and retail spaces, and may grant occupancy rights, concessions, licenses (including parking licenses, "
        "cell tower and rooftop licenses, signage licenses and amenity memberships), and easements for utilities, "
        "access and services within the Premises, in the ordinary course of the operation of the Project, without "
        "Landlord's consent. A sublease of the entire Premises, or of substantially all of the Premises, to a single "
        "subtenant for a term extending beyond the Term shall require Landlord's consent, not to be unreasonably "
        "withheld, conditioned or delayed.")
    sec(doc, "11.3", "Permitted Transfers", "Notwithstanding Sections 11.1 and 11.5, the following transfers "
        "(collectively, \"**Permitted Transfers**\") shall be permitted without Landlord's consent, without notice "
        "(except as provided in Section 11.3(j)) and without triggering the ROFR:")
    pts = [
        "any transfer, assignment or conveyance to an Affiliate of Tenant;",
        "any transfer of direct or indirect ownership interests in Tenant, including any sale, issuance, redemption, "
        "transfer, pledge, hypothecation or encumbrance of membership interests, and any change in the control, "
        "composition or identity of Tenant's members, managers or general partners;",
        "the pledge of one hundred percent (100%) of the membership interests in Tenant to any Leasehold Mortgagee, "
        "and any foreclosure, transfer in lieu of foreclosure, or exercise of remedies with respect to such pledged "
        "interests, and any resulting change in the ownership or control of Tenant;",
        "any assignment or transfer to a Leasehold Mortgagee, its designee, or any purchaser at foreclosure or "
        "transferee by deed in lieu of foreclosure, in accordance with Section 9.7;",
        "any grant of a Leasehold Mortgage, collateral assignment of leases and rents, or other financing "
        "encumbrance;",
        "any transfer resulting from the exercise of a buy-sell, put, call, drag-along, tag-along, right of first "
        "offer, right of first refusal or other right under any joint venture, operating, partnership or shareholder "
        "agreement of Tenant or its members;",
        "any transfer to Coventry Capital Partners LP, any fund, vehicle, account or separate account managed or "
        "advised by Coventry Capital Partners LP or its affiliates, or any of their respective affiliates, "
        "subsidiaries, general partners or related funds;",
        "any recapitalization, refinancing, joint venture, syndication, securitization, conversion, merger, "
        "consolidation or internal reorganization of Tenant or its Affiliates, provided that Tenant's leasehold "
        "interest is not transferred to a third party that is unrelated to Marcus Ellison or Coventry Capital "
        "Partners LP in a transaction that would otherwise constitute an assignment for value;",
        "any transfer to a Person acquiring the leasehold interest in connection with a judicial or non-judicial "
        "foreclosure, a federal or state receivership, or a bankruptcy sale; and",
        "any transfer of the leasehold interest to an entity in which Marcus Ellison or Coventry Capital Partners LP "
        "(or their respective affiliates) holds a direct or indirect interest of not less than twenty percent (20%).",
    ]
    for i, t in enumerate(pts):
        sub(doc, "(%s)" % chr(97 + i), t)
    para(doc, "Tenant shall give Landlord written notice of any Permitted Transfer described in clause (a) above within "
              "thirty (30) days after its occurrence, and shall give Landlord written notice of any other Permitted "
              "Transfer within thirty (30) days after its occurrence for informational purposes only. No Permitted "
              "Transfer shall require the payment of any fee, the delivery of any guaranty, or any increase in the "
              "Security Deposit.")
    sec(doc, "11.4", "Consent Standard; Deemed Consent", "Landlord's consent to an assignment (other than a Permitted "
        "Transfer) shall be requested in writing and accompanied by the identity of the proposed assignee, its "
        "financial statements and operating experience, and the material terms of the proposed assignment. Landlord "
        "shall respond within ten (10) Business Days after receipt of a complete request, failing which Landlord's "
        "consent shall be deemed given. Landlord may withhold consent only if the proposed assignee (a) does not have "
        "the financial capacity to perform Tenant's obligations, (b) lacks experience in owning or operating "
        "comparable properties, or (c) is a governmental entity or a Person that would, if the assignee became Tenant, "
        "adversely affect the Project's ability to obtain insurance or comply with Applicable Law. Landlord may not "
        "condition consent on any payment, fee, guaranty or increase in the Security Deposit.")
    sec(doc, "11.5", "Right of First Refusal", "During the period from the Lease Commencement Date through September "
        "30, 2045, if Tenant proposes to assign this Lease to a non-Affiliate for value (an \"**Assignment for "
        "Value**\"), Landlord shall have a right of first refusal (the \"**ROFR**\") to acquire the leasehold interest "
        "on the same terms and conditions as the proposed Assignment for Value, subject to the following:")
    sub(doc, "(a)", "The ROFR shall apply **only** to a direct assignment of this Lease to a third party for a "
        "purchase price payable in cash or its equivalent. The ROFR shall **not** apply to any Permitted Transfer, to "
        "any transfer of direct or indirect ownership interests in Tenant, to any Leasehold Mortgage, foreclosure or "
        "deed-in-lieu, to any merger or consolidation, to any transfer in connection with a recapitalization or "
        "refinancing, or to any New Lease.")
    sub(doc, "(b)", "Tenant shall deliver a written notice (a \"**ROFR Notice**\") setting forth the identity of the "
        "proposed assignee, the proposed purchase price and the other material terms, together with a copy of the "
        "executed letter of intent or purchase agreement. Landlord shall have sixty (60) days after receipt of the "
        "ROFR Notice to elect to acquire the leasehold interest by irrevocable written notice, and shall close the "
        "acquisition within sixty (60) days after its election (or concurrently with the proposed assignment, if "
        "later).")
    sub(doc, "(c)", "Any acquisition by Landlord under the ROFR shall be subject to, and shall not impair, each "
        "Leasehold Mortgage, and shall be consummated only with the prior written consent of each Leasehold Mortgagee "
        "or upon payment in full of the indebtedness secured by each Leasehold Mortgage and release thereof. Landlord "
        "shall assume all of Tenant's obligations under this Lease prospectively.")
    sub(doc, "(d)", "If Landlord does not elect within the sixty (60) day period, or elects but fails to close within "
        "the period specified in Section 11.5(b), the ROFR shall lapse as to that proposed Assignment for Value and "
        "Tenant may complete it on terms not materially more favorable to the assignee than those in the ROFR Notice. "
        "If Tenant does not complete the assignment within one hundred eighty (180) days after the ROFR lapses, the "
        "ROFR shall be reinstated.")
    sub(doc, "(e)", "Landlord shall not be entitled to any fee, deposit or reimbursement in connection with the ROFR.")
    note(doc, "[**Drafting flag:** The ROFR is also evidenced by a recorded Declaration of Right of First Refusal "
              "dated September 8, 2019, recorded at Volume 405, Page 55 of the Port Calloway Land Records, which, as "
              "noted in Exception No. 4 of Title Commitment TC-2025-07821, contains no carve-out for mortgagee "
              "foreclosure, deed-in-lieu transfers, or assignments by a Leasehold Mortgagee or its designee. The "
              "terms of this Section 11.5 cannot, as a matter of record notice, override the recorded instrument. "
              "Landlord shall, as a condition to the Lease Commencement Date, execute and record an amendment to the "
              "Declaration of Right of First Refusal conforming it to this Section 11.5, including the carve-outs in "
              "Sections 11.3 and 11.5(a) and (c).]")
    sec(doc, "11.6", "No Release", "No assignment or sublease shall release Tenant from its obligations under this "
        "Lease accruing before the effective date of the assignment, and any assignee shall assume all obligations "
        "accruing after such date. Failing delivery of an assumption agreement by an assignee other than a Permitted "
        "Transferee assignee, Tenant shall remain liable for all obligations under this Lease.")
    sec(doc, "11.7", "Charge of Control Not an Assignment", "For the avoidance of doubt, no change in the direct or "
        "indirect ownership, composition or control of Tenant or any of its members shall constitute an assignment of "
        "this Lease or an interest in it, and neither Landlord's consent nor the ROFR shall apply to any such change.")

    # ================= ARTICLE 12 =================
    art(doc, "Article 12. Insurance")
    sec(doc, "12.1", "Tenant's Insurance Obligations", "Throughout the Term, Tenant shall procure and maintain, at its "
        "sole cost and expense, with insurers licensed or authorized to do business in Connecticut and having a "
        "financial strength rating of not less than A-VIII from A.M. Best Company (or an equivalent rating from a "
        "nationally recognized rating agency), the following coverages:")
    ins = [
        "**Commercial General Liability** on an occurrence basis, with limits of not less than $10,000,000 per "
        "occurrence and $20,000,000 in the annual aggregate, covering bodily injury, property damage, personal and "
        "advertising injury, products-completed operations and contractual liability (including the indemnities in this "
        "Lease), and including a waiver of the insured-versus-insured exclusion as respects Landlord and each "
        "Leasehold Mortgagee;",
        "**All-Risk (Special Form) Property Insurance** on a replacement cost basis, without deduction for "
        "depreciation, covering the Improvements, including fire, windstorm, flood (as provided in Section 12.1(f)), "
        "earthquake, vandalism and malicious mischief, with an agreed amount endorsement, ordinance or law coverage, "
        "and a waiver of subrogation in favor of Landlord and each Leasehold Mortgagee;",
        "**Builder's Risk Insurance** on a completed value basis during construction of any phase of the Project, "
        "covering the full value of construction work in progress, materials and supplies stored on or off the "
        "Premises, with a soft-cost endorsement and, if available on commercially reasonable terms, a delay-in-opening "
        "endorsement;",
        "**Business Interruption and Rent Loss Insurance** covering not less than twelve (12) months of Base Rent and "
        "customary fixed operating expenses, with the proceeds payable to Tenant (and, to the extent of any assignment "
        "of rents, to each Leasehold Mortgagee as its interest may appear);",
        "**Environmental Liability / Pollution Legal Liability Insurance** with limits of not less than $5,000,000 per "
        "occurrence and $10,000,000 in the annual aggregate, covering claims arising from pollution conditions at, on, "
        "under or migrating from the Premises, including remediation costs, third-party bodily injury and property "
        "damage, and, to the extent available on commercially reasonable terms, covering Pre-Existing Environmental "
        "Conditions for a term consistent with the Term of this Lease;",
        "**Flood Insurance** as provided in Section 12.1(f); and",
        "**Workers' Compensation Insurance** as required by Connecticut law, and Employer's Liability Insurance with "
        "limits of not less than $1,000,000.",
    ]
    for i, t in enumerate(ins):
        sub(doc, "(%s)" % chr(97 + i), t)
    sub(doc, "(f)", "**Flood Insurance.** Because the Premises lie entirely within FEMA Flood Zone AE (Base Flood "
        "Elevation 12 feet NAVD88), Tenant shall maintain flood insurance consisting of (i) the maximum coverage "
        "available under the National Flood Insurance Program (or any successor program), plus (ii) excess flood "
        "insurance or difference-in-conditions coverage, on a replacement cost basis, in an amount sufficient to "
        "insure the full replacement cost of the Improvements or such lesser amount as each Leasehold Mortgagee may "
        "require, obtained from the commercial market and, if available on commercially reasonable terms, on a "
        "multi-year prepaid basis. The parties acknowledge that the National Flood Insurance Program maximum "
        "available coverage is materially less than the replacement cost of the Project and that coverage under this "
        "Section 12.1(f) is intended to satisfy the requirements of each Leasehold Mortgagee.", level=2)
    sec(doc, "12.2", "Additional Insureds and Loss Payees", "Landlord shall be named as an additional insured on the "
        "Commercial General Liability policy, and each Leasehold Mortgagee shall be named as an additional insured on "
        "the Commercial General Liability policy and as mortgagee/loss payee on the property, builder's risk, flood "
        "and business interruption policies, as its interest may appear. Landlord shall not be named as a loss payee "
        "or additional insured on the property policies except to the extent of its insurable interest as fee owner, "
        "which the parties acknowledge is limited and does not include the value of Tenant's Improvements.")
    sec(doc, "12.3", "Certificates; Notice of Cancellation", "Tenant shall deliver certificates of insurance (and, upon "
        "request, copies of policies and endorsements) to Landlord and each Leasehold Mortgagee prior to the Lease "
        "Commencement Date and thereafter annually, and shall give not less than thirty (30) days' prior written "
        "notice of cancellation, non-renewal or material modification of any required coverage (ten (10) days for "
        "non-payment of premium). Tenant shall use commercially reasonable efforts to cause each insurer to provide "
        "such notice directly.")
    sec(doc, "12.4", "Waiver of Subrogation", "Landlord and Tenant each waive, and shall cause their respective "
        "insurers to waive, all rights of subrogation against the other and against each Leasehold Mortgagee for loss "
        "or damage covered by insurance required under this Lease, to the extent permitted by the applicable policies.")
    sec(doc, "12.5", "Landlord's Insurance", "Landlord shall maintain commercially reasonable liability and property "
        "insurance with respect to its fee interest in the land and its activities as a public body, at its own cost. "
        "Nothing in this Article 12 shall relieve Landlord of its own insurance obligations or require Tenant to "
        "insure Landlord's fee interest or Landlord's own liability.")
    sec(doc, "12.6", "No Limitation of Liability", "The insurance requirements of this Article 12 are minimum "
        "requirements and shall not limit or discharge Tenant's obligations, indemnities or liabilities under this "
        "Lease.")

    # ================= ARTICLE 13 =================
    art(doc, "Article 13. Casualty and Condemnation")
    sec(doc, "13.1", "Casualty; Restoration", "If the Improvements are damaged or destroyed by fire or other casualty, "
        "Tenant shall promptly notify Landlord and each Leasehold Mortgagee, and shall restore the Improvements "
        "substantially to their condition before the casualty (subject to Applicable Law then in effect, including "
        "any floodplain or freeboard requirement then applicable), using available insurance proceeds, provided that "
        "Tenant shall not be required to restore if (a) this Lease is terminated in accordance with Section 13.3 or "
        "(b) the Leasehold Mortgagee directs that proceeds be applied to the indebtedness secured by its Leasehold "
        "Mortgage.")
    sec(doc, "13.2", "Rent Abatement", "During the period of restoration following a casualty, Base Rent and "
        "Percentage Rent shall abate in proportion to the portion of the rentable area of the Improvements rendered "
        "unusable and not actually used by Tenant, measured on a rentable square footage basis, from the date of the "
        "casualty until the earlier of the date restoration is substantially complete and the date Tenant reoccupies "
        "the affected space. Insurance proceeds received by Tenant under the rent loss coverage shall be applied first "
        "to the abated Rent; any excess shall be retained by Tenant.")
    sec(doc, "13.3", "Termination Rights on Casualty", "If (a) restoration would require expenditures exceeding fifty "
        "percent (50%) of the then-replacement cost of the Improvements, (b) the casualty occurs during the final ten "
        "(10) years of the Term, (c) the Improvements cannot be restored to a condition suitable for the Permitted "
        "Uses within twenty-four (24) months, or (d) applicable law would prohibit restoration as a practical matter, "
        "then either party may terminate this Lease by written notice delivered within ninety (90) days after the "
        "casualty. Upon any such termination, all insurance proceeds (other than those payable under the rent loss "
        "coverage) shall be paid to Tenant or, to the extent of its interest, to each Leasehold Mortgagee, and Landlord "
        "shall have no claim to them. Tenant shall have no obligation to rebuild in the event of a termination under "
        "this Section 13.3.")
    sec(doc, "13.4", "Condemnation", "If all or any part of the Premises or the Improvements is taken by eminent "
        "domain, or conveyed in lieu of condemnation under threat of condemnation, then:")
    sub(doc, "(a)", "the entire award, including any award for the fee interest, the leasehold interest, the "
        "Improvements, relocation costs, business interruption and loss of goodwill, shall be allocated between the "
        "parties as follows: Landlord shall receive the portion of the award attributable to the value of the land as "
        "unimproved and unencumbered by this Lease, determined as of the date of valuation, and Tenant shall receive "
        "all remaining portions of the award, including the portion attributable to the value of the leasehold "
        "interest, the Improvements, the Environmental Remediation Work, relocation costs and business interruption;")
    sub(doc, "(b)", "if the taking is of the whole Premises, or of such portion that the balance is not reasonably "
        "susceptible of use for the Permitted Uses, either party may terminate this Lease effective as of the date of "
        "the taking; and")
    sub(doc, "(c)", "if the taking is partial and the Premises remain reasonably susceptible of use for the Permitted "
        "Uses, this Lease shall continue as to the remainder, Tenant shall restore the remaining Improvements to the "
        "extent practicable, and Base Rent and the Breakpoint shall be equitably adjusted in proportion to the "
        "reduction in the reasonably usable area of the Premises.")
    para(doc, "Landlord and Tenant shall each cooperate in presenting claims to the condemning authority, and each "
              "shall retain its own counsel at its own expense. Nothing in this Section 13.4 shall be construed to "
              "require Landlord to subordinate its fee interest to any third party.")
    sec(doc, "13.5", "Temporary Taking", "A temporary taking of all or part of the Premises shall not terminate this "
        "Lease. Base Rent shall abate in proportion to the area and duration of the taking, and Tenant shall be "
        "entitled to any award allocable to the period of the temporary taking and to the loss of use of the "
        "Premises.")

    # ================= ARTICLE 14 =================
    art(doc, "Article 14. Operation, Maintenance, Open Space, Bulkhead and Alterations")
    sec(doc, "14.1", "Tenant's Maintenance Obligations", "Tenant shall, at its sole cost and expense, maintain, repair, "
        "replace and keep the Premises and the Improvements in good order, condition and repair, in a manner "
        "consistent with comparable first-class mixed-use properties in the region, and in compliance with Applicable "
        "Law (including the ELUR and all floodplain requirements). Tenant shall not permit any waste, nuisance or "
        "unlawful use of the Premises.")
    sec(doc, "14.2", "Landlord's Obligations", "Landlord shall have no obligation to maintain, repair, alter or insure "
        "the Premises or the Improvements, except as expressly provided in Section 2.9 and Article 12. Landlord shall "
        "maintain its fee interest free of liens and encumbrances (other than the Permitted Exceptions) and shall "
        "continue to perform any obligation imposed on the fee owner by the ELUR or by Applicable Law that cannot "
        "lawfully be performed by Tenant.")
    sec(doc, "14.3", "Bulkhead", "The approximately 480 linear feet of bulkhead along the eastern boundary of the "
        "Premises, together with the backfill behind it, is a material element of the Premises and was in fair to poor "
        "condition as of the Phase II Environmental Site Assessment, exhibiting lateral displacement, cracking, "
        "deteriorated and missing timber lagging, erosion of backfill, spalling of the concrete cap and corrosion of "
        "the sheet piling, and including approximately forty (40) linear feet from which the concrete cap has been "
        "removed. The parties agree that:")
    sub(doc, "(a)", "Landlord shall deliver the independent structural engineering assessment described in Section "
        "2.9(b) prior to the Lease Commencement Date, at Landlord's cost;")
    sub(doc, "(b)", "[**Tenant position, to be negotiated:** Landlord shall be responsible, at its sole cost, for "
        "rehabilitating the bulkhead and backfill to a sound and watertight condition as of the Lease Commencement "
        "Date, or, at Tenant's election, Tenant shall perform such work and receive a dollar-for-dollar credit against "
        "Base Rent in addition to the Remediation Credit, together with interest at the Default Interest Rate on any "
        "unreimbursed amount;]")
    sub(doc, "(c)", "thereafter, Tenant shall maintain and repair the bulkhead in accordance with Section 14.1, and "
        "shall not be responsible for any pre-existing structural deficiency documented in the assessment; and")
    sub(doc, "(d)", "the parties acknowledge that the bulkhead lies within or adjacent to the fifteen (15) foot public "
        "pedestrian access easement described on **Exhibit B**, that maintenance and repair of the bulkhead is "
        "consistent with the easement and does not constitute a prohibited permanent structure, and that Landlord and "
        "the City of Port Calloway shall cooperate in any permitting required for bulkhead work, including any "
        "Structures, Dredging and Fill permit or tidal wetlands approval.")
    sec(doc, "14.4", "Public Open Space", "Tenant shall design, construct, maintain and operate, at its sole cost and "
        "expense, not less than eight thousand (8,000) square feet of Public Open Space on the waterfront (eastern) "
        "side of the Premises, connected to the existing public pedestrian promenade, and shall not enclose, gate or "
        "restrict public access to it. The design and programming of the Public Open Space shall be subject to "
        "Landlord's reasonable approval in connection with site plan review, which approval shall be given or withheld "
        "within ten (10) Business Days after submission. The Public Open Space may be located within the pedestrian "
        "access easement area to the extent consistent with the terms of that easement. Tenant's maintenance "
        "obligation shall be performed in a manner consistent with the engineered barrier and Soil Management Plan "
        "requirements of the ELUR, and the parties acknowledge that landscaping depths and planting specifications must "
        "be coordinated with the twenty-four (24) inch clean fill cap.")
    sec(doc, "14.5", "Affordable Housing", "Not less than **fifteen percent (15%)** of the residential dwelling units "
        "in the Project shall be designated as affordable housing units, available to households earning at or below "
        "**eighty percent (80%) of Area Median Income**, for the duration of the Term, and this covenant shall run "
        "with the leasehold interest and bind Tenant's successors and assigns. The following shall govern:")
    ah = [
        "**AMI.** \"Area Median Income\" means the median family income for the New Haven-Milford, Connecticut HUD "
        "Metro Fair Market Rent Area (or such other HUD-defined geographic area as is then applicable to the City of "
        "Port Calloway), as determined annually by the U.S. Department of Housing and Urban Development.",
        "**Unit count and recalculation.** The 15% requirement shall be calculated by reference to the total number of "
        "residential dwelling units in the Project as finally constructed and, if the total unit count changes by more "
        "than five percent (5%) through renovation, reconfiguration, partial demolition or redevelopment, shall be "
        "recalculated and the number of designated affordable units adjusted accordingly, rounding to the nearest "
        "whole unit.",
        "**Location.** Affordable units shall be located only on floors two (2) and above (consistent with the ELUR) "
        "and shall be distributed throughout the Residential Tower rather than concentrated on a single floor or in a "
        "single stack, and shall be comparable in size, finish and access to amenities to market-rate units of the "
        "same bedroom count.",
        "**Compliance and verification.** Tenant shall administer income qualification and recertification in "
        "accordance with HUD guidance and any applicable regulatory agreement, shall maintain records, and shall "
        "deliver an annual compliance certificate to Landlord and the City of Port Calloway within ninety (90) days "
        "after the end of each Lease Year.",
        "**Enforcement.** Landlord's sole remedies for a breach of this Section 14.5 shall be specific performance and "
        "injunctive relief; no such breach shall constitute an Event of Default, give rise to any right of "
        "termination, reverter or forfeiture, or permit any draw on the Security Deposit. Tenant shall have ninety "
        "(90) days after written notice to cure any non-compliance.",
        "**Recorded covenant.** The parties acknowledge the Declaration of Restrictive Covenants dated November 15, "
        "2019, recorded at Volume 408, Page 230 of the Port Calloway Land Records, and agree that Tenant's compliance "
        "with that recorded covenant, as supplemented by this Section 14.5, shall constitute compliance with this "
        "Section 14.5.",
    ]
    for i, t in enumerate(ah):
        sub(doc, "(a)" if i == 0 else "(%s)" % chr(97 + i), t)
    note(doc, "[**Drafting flag — AMI geography:** The record states three different AMI geographies: \"the Port "
              "Calloway Metropolitan Statistical Area\" (Term Sheet § 4), \"the New Haven-Milford, Connecticut "
              "Metropolitan Statistical Area\" (Title Commitment Exception No. 5, describing the recorded 2019 "
              "covenant), and \"the Bridgeport-Stamford-Norwalk, CT HUD Metro Fair Market Rent Area\" (Survey § 3(d)). "
              "The Premises are in New Haven County. This Section 14.5 adopts the geography used in the recorded "
              "covenant, which is the operative instrument; the other two formulations should be conformed.]")
    sec(doc, "14.6", "Alterations and Redevelopment", "Tenant may make alterations, renovations, expansions, "
        "demolitions and replacements of the Improvements, and may redevelop the Premises, from time to time without "
        "Landlord's consent, provided that (a) the work complies with Applicable Law, the ELUR and Article 15, (b) the "
        "Project continues to comply with Sections 14.4 and 14.5, and (c) Tenant gives Landlord not less than thirty "
        "(30) days' prior written notice of any demolition of more than twenty-five percent (25%) of the rentable area "
        "of the Improvements. During the final ten (10) years of the Term (from and after October 1, 2114), Tenant "
        "shall not undertake alterations or capital improvements exceeding $[●] in any twelve-month period that would "
        "materially impair the reversionary value of the Premises without Landlord's consent, which consent shall not "
        "be unreasonably withheld, conditioned or delayed; provided that no consent shall be required for (i) work "
        "required by Applicable Law, including any flood, coastal resilience, energy or accessibility requirement, (ii) "
        "repairs and replacements in the ordinary course, or (iii) work required to comply with the ELUR.")
    sec(doc, "14.7", "Signage, Rooftop and Antenna Rights", "Tenant may install signage, rooftop equipment, solar "
        "panels, telecommunications antennas and similar installations on the Improvements, subject to Applicable Law "
        "and the Port Calloway Zoning Regulations, without Landlord's consent, and may license such rights to third "
        "parties.")
    sec(doc, "14.8", "Utilities", "Tenant shall be responsible for obtaining and paying for all utility services to the "
        "Premises. Landlord shall cooperate in obtaining utility connections and shall execute any utility easement or "
        "consent reasonably required, without charge, provided that no such easement materially impairs the "
        "Improvements.")
    sec(doc, "14.9", "Landlord's Access", "Landlord and its designees may enter the Premises upon not less than "
        "twenty-four (24) hours' prior written notice (except in an emergency, in which case notice shall be given as "
        "soon as practicable) for the purpose of inspecting, exercising any right or remedy under this Lease, "
        "performing any obligation of Landlord, or complying with Applicable Law or the ELUR, provided that Landlord "
        "shall not unreasonably interfere with Tenant's operations or any subtenant's occupancy and shall comply with "
        "Tenant's reasonable construction, safety and security requirements.")

    # ================= ARTICLE 15 =================
    art(doc, "Article 15. Compliance with Laws; Flood Resilience; ELUR")
    sec(doc, "15.1", "General Compliance", "Tenant shall comply, and shall cause the Project and all subtenants to "
        "comply, with all Applicable Law relating to the Premises, the Improvements and their use, including the "
        "Connecticut State Building Code, the Port Calloway Zoning Regulations, the WRD-3 zoning district "
        "requirements, coastal area management and tidal wetlands requirements, floodplain management regulations, "
        "fair housing and accessibility requirements, and the ELUR.")
    sec(doc, "15.2", "Permitted Uses", "The Premises may be used for the following purposes and no other: residential "
        "apartments (for rent only; no condominiums or cooperative units, provided that Tenant may convert the "
        "leasehold structure to a condominium form of ownership without Landlord's consent if such conversion does not "
        "alter Landlord's rights, obligations or reversionary interest); Class A office; ground-floor retail "
        "(excluding adult entertainment establishments, firearms sales, pawnshops and gasoline service stations); "
        "restaurants, including those with liquor service licensed by the Connecticut Department of Consumer "
        "Protection; accessory parking; residential lobby and amenity spaces (including a fitness center, package room, "
        "resident lounge and leasing office) at the ground-floor level, subject to Section 7.8; and uses accessory to "
        "the foregoing. No industrial, manufacturing or warehousing uses shall be permitted other than as accessory "
        "to the operation of the Improvements.")
    sec(doc, "15.3", "Flood Resilience and Freeboard", "The Premises lie entirely within FEMA Flood Zone AE, FIRM "
        "Panel No. 09009C0301G, effective January 15, 2020, with a Base Flood Elevation of twelve (12) feet NAVD88. "
        "Tenant shall design and construct the Improvements with a finished floor elevation of not less than fifteen "
        "(15) feet NAVD88 (three (3) feet of freeboard), and with all mechanical, electrical, telecommunications and "
        "life-safety equipment located above such elevation or otherwise protected against inundation. Tenant may, at "
        "its election, construct to a higher finished floor elevation. If any Applicable Law, permit condition, insurer "
        "requirement or Leasehold Mortgagee requirement imposes a higher finished floor elevation or additional "
        "freeboard, Tenant shall comply, and the incremental cost shall be borne by Tenant; any resulting delay shall "
        "constitute a Force Majeure Event and a permitting delay under Section 3.4.")
    sec(doc, "15.4", "Climate Adaptation and Code Changes", "The parties acknowledge that over a Term of ninety-nine "
        "(99) years the Base Flood Elevation, flood maps, coastal resilience standards, energy codes and building codes "
        "are likely to change materially, and that Connecticut Public Act 23-167 (2023) and evolving municipal "
        "standards may require additional freeboard, floodproofing or adaptation measures. Tenant shall be responsible "
        "for compliance with any such change as and when required by Applicable Law, and no such change shall "
        "constitute a default by Tenant or entitle Landlord to any increase in Rent; provided that Tenant shall be "
        "entitled to the benefit of any applicable amortization, hardship or phased-compliance provision of "
        "Applicable Law. Landlord shall cooperate with Tenant in seeking any variance, extension of time or "
        "alternative compliance method, at Tenant's cost, and the time required to obtain such relief shall be a "
        "Force Majeure Event and a permitting delay under Section 3.4.")
    sec(doc, "15.5", "ELUR", "Tenant shall comply with the ELUR in accordance with Section 7.7. Nothing in this Lease "
        "shall be construed to require Tenant to perform any remediation or to accept any obligation in excess of "
        "those allocated to Tenant in Article 7.")
    sec(doc, "15.6", "Notice of Violations", "Each party shall deliver to the other, within five (5) Business Days after "
        "receipt, a copy of any notice of violation, citation, order, compliance notice or enforcement action received "
        "from any governmental authority relating to the Premises, the Improvements or the ELUR, and each Leasehold "
        "Mortgagee shall receive a copy simultaneously.")

    # ================= ARTICLE 16 =================
    art(doc, "Article 16. Title, Permitted Exceptions, Quiet Enjoyment and Estoppels")
    sec(doc, "16.1", "Title Representations", "Landlord shall convey the leasehold estate to Tenant subject only to the "
        "Permitted Exceptions. Landlord represents and warrants that, as of the Lease Commencement Date, the leasehold "
        "estate created by this Lease will be insurable as a good and indefeasible leasehold estate, subject only to "
        "the Permitted Exceptions, and that the fee simple title to the Premises is vested in Landlord free and clear "
        "of all liens and encumbrances other than the Permitted Exceptions.")
    sec(doc, "16.2", "Permitted Exceptions", "The Permitted Exceptions are those described on **Exhibit B**. Tenant's "
        "approval of the Permitted Exceptions is limited to those matters expressly described on **Exhibit B**, and "
        "any additional exception, or any change in the recorded terms of any listed exception, shall require Tenant's "
        "written approval and the approval of each Leasehold Mortgagee. Landlord shall, at its sole cost, cause the "
        "mechanics' lien described on **Exhibit B**, Part 6, to be discharged or bonded, cure any title defect within "
        "its control, and correct the legal description of the Premises so that it conforms to the ALTA/NSPS survey "
        "delivered under Section 2.3(c).")
    note(doc, "[**Drafting flag — legal description:** The metes and bounds description attached as Exhibit A to Title "
              "Commitment TC-2025-07821 does not close and, on the courses stated, encloses approximately 279,535 "
              "square feet (6.42 acres) rather than the 139,392 square feet (3.20 acres) recited in the same instrument. "
              "The description in the ALTA/NSPS survey (Survey Job No. CLS-2025-0417) closes exactly and encloses "
              "139,475 square feet. **Exhibit A** to this Lease is derived from the survey. The title company must "
              "reissue its commitment with a conformed legal description, and the description in Exhibit A must be "
              "confirmed by each Leasehold Mortgagee's title insurer before the Lease Commencement Date.]")
    sec(doc, "16.3", "Quiet Enjoyment", "Landlord covenants that, so long as no Event of Default by Tenant is "
        "continuing, Tenant shall peaceably and quietly have, hold and enjoy the Premises for the Term without "
        "hindrance or interruption by Landlord or any Person claiming by, through or under Landlord, subject to the "
        "Permitted Exceptions and Applicable Law. Landlord shall defend Tenant's possession at Landlord's cost against "
        "any claim asserted by any Person claiming by, through or under Landlord.")
    sec(doc, "16.4", "Estoppel Certificates", "Within ten (10) Business Days after request by Tenant or any Leasehold "
        "Mortgagee (but not more than twice in any calendar year except in connection with a financing or a proposed "
        "transfer), Landlord shall execute and deliver a written estoppel certificate certifying, as applicable, the "
        "Lease Commencement Date, the Rent Commencement Date, the then-current Base Rent, the status of any default, "
        "the amounts of any prepaid Rent or Security Deposit, and such other factual matters as may reasonably be "
        "requested. Landlord's failure to deliver an estoppel within such period shall be a Landlord Event of Default "
        "curable only by delivery, and Tenant and each Leasehold Mortgagee may rely upon such failure as confirmation "
        "of the matters stated in the request.")
    sec(doc, "16.5", "Subordination and Non-Disturbance", "This Lease is and shall remain superior to any mortgage or "
        "deed of trust hereafter placed on Landlord's fee interest. Landlord shall cause any present or future holder "
        "of a mortgage or deed of trust encumbering the fee interest to execute a subordination, non-disturbance and "
        "attornment agreement in favor of Tenant and each Leasehold Mortgagee, in form reasonably satisfactory to "
        "Tenant and each Leasehold Mortgagee, providing that this Lease (and any New Lease) shall not be disturbed by "
        "reason of the foreclosure of such fee mortgage.")
    sec(doc, "16.6", "No Merger", "No merger of the leasehold estate created by this Lease with the fee interest in the "
        "Premises shall occur by reason of (a) the acquisition of the fee interest by Tenant or any Affiliate of "
        "Tenant, (b) the acquisition of the leasehold interest by Landlord or any Affiliate of Landlord, or (c) the "
        "transfer of either interest to the same Person, unless such Person delivers written notice to each Leasehold "
        "Mortgagee expressly electing to effect such merger.")
    sec(doc, "16.7", "Leasehold Title Insurance", "Tenant shall obtain, at its cost, an ALTA Leasehold Owner's Policy "
        "of title insurance in the amount of the total project cost and shall cause each Leasehold Mortgagee to obtain "
        "an ALTA Leasehold Loan Policy in the amount of its loan, in each case subject only to the Permitted Exceptions "
        "and with the ALTA 13-06 and 13.1-06 leasehold endorsements and the environmental protection lien endorsement. "
        "Landlord shall execute such affidavits, no-lien affidavits, owner's certificates, gap undertakings and "
        "indemnities as the title company reasonably requires, without charge.")
