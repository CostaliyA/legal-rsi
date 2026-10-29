from memo_helpers import *

def blocks(doc):
    h1(doc, "Part 6 — Other substantive issues, analyzed", "6")

    # 6.1 PERCENTAGE RENT
    h2(doc, "6.1  Percentage rent: the Breakpoint is a fixed number in a 99-year lease", "6.1")
    body(doc, "Term Sheet § 6 fixes the Breakpoint at $28,500,000 and states that it \"is a fixed dollar amount and "
              "shall remain unchanged for the duration of the Lease Term.\" Base Rent, meanwhile, escalates at 2.5% "
              "compounded for 15 years and then resets on a CPI floor at each tenth anniversary. The consequence is "
              "arithmetic, not argument:")
    table(doc,
          [["Lease Year", "Base Rent (2.5% floor)", "Fixed Breakpoint", "Breakpoint ÷ Base Rent",
            "Breakpoint in Year-1 dollars"],
           ["6", "$3,224,513", "$28,500,000", "8.84×", "$25,189,847"],
           ["16", "$4,127,650", "$28,500,000", "6.90×", "$19,678,268"],
           ["26", "$5,283,741", "$28,500,000", "5.39×", "$15,372,632"],
           ["36", "$6,763,635", "$28,500,000", "4.21×", "$12,009,075"],
           ["46", "$8,658,024", "$28,500,000", "3.29×", "$9,381,471"],
           ["56", "$11,083,003", "$28,500,000", "2.57×", "$7,328,790"],
           ["66", "$14,187,181", "$28,500,000", "2.01×", "$5,725,239"],
           ["76", "$18,160,791", "$28,500,000", "1.57×", "$4,472,547"],
           ["86", "$23,247,348", "$28,500,000", "1.23×", "$3,493,947"],
           ["96", "$29,758,571", "$28,500,000", "0.96×", "$2,729,466"]],
          [0.85, 1.45, 1.35, 1.35, 1.5], size=7.5, align_right=[1, 2, 3, 4],
          caption="Model: Base Rent escalated at the 2.5% floor; Breakpoint held at $28,500,000; deflated at the same "
                  "2.5%.")
    body(doc, "Read the last two columns together. By **Lease Year 96 the fixed Breakpoint is smaller than Base Rent** — "
              "so Percentage Rent is payable on essentially every dollar of gross revenue above the rent roll's own "
              "fixed charge, i.e. it becomes a 2% tax on gross receipts. And in real terms the Breakpoint has decayed "
              "to **$2.73 million**, which is below today's Base Rent of $2.85 million. In other words, the mechanism "
              "the parties agreed to as a share of upside becomes, within one lifetime, a charge larger in real terms "
              "than the ground rent that existed when the deal was struck. That is your worry, and it is well founded.")
    body(doc, "There is a second, separate problem. Because both limbs of the reset formula are computed from the "
              "*initial* Base Rent rather than from the then-current rent, Base Rent is flat within each ten-year band "
              "and then jumps by the whole cumulative index in one step. At 2.5% inflation, each reset after Year 16 is "
              "a **28.0% single-year increase**; at 3.5% inflation the Year 16 step is +30.9%, and at 4.5% it is "
              "+51.2% (Appendix 2). Step increases of that size do not merely look arbitrary; they will trip debt "
              "service coverage tests at each refinancing, which is an institutional-quality problem for Ansel as well "
              "as for us.")
    body(doc, "**What the Draft Lease does.** Section 5.3 resets the Breakpoint at each Rent Reset Date so as to "
              "preserve the Lease Year 6 ratio of Breakpoint to Base Rent (8.84×). That is the single change that "
              "keeps the mechanism doing what both sides intended in Year 60 as in Year 6, and it is easy to explain: "
              "*the percentage rent shares revenue growth above the rent growth the landlord is already capturing.* We "
              "have also flagged, in a bracketed note in Section 4.4, an alternative rent mechanic — annual CPI "
              "adjustment with a 0% floor and a 4% ceiling — which removes the reset cliffs without changing the "
              "long-run economics. Both are Tenant positions; expect the Authority to resist the Breakpoint indexation "
              "first and the collar second. Our fallbacks are set out in the note to Section 5.3 (CPI-only indexation; "
              "a declining rate; or a cap on Percentage Rent at 25% of Base Rent).")
    body(doc, "**Gross Revenues.** Your instruction was to define this tightly, and the Draft Lease does. Section 5.2 "
              "is drafted as an exhaustive inclusion list plus fifteen exclusions, and it omits the Term Sheet's "
              "open-ended \"all rents, fees, charges, and other income of every kind\" formulation. The exclusions "
              "cover everything you listed — security deposits, utility reimbursements, insurance proceeds, "
              "condemnation awards, CAM and other pass-throughs, interest on reserves, loan proceeds, capital "
              "contributions, free rent and concessions, amounts billed but not collected, sales taxes collected and "
              "remitted, the value of the tax abatement, and at-cost service charges. We also changed three mechanics "
              "that would otherwise create disputes: cash basis rather than \"GAAP consistently applied\" (GAAP "
              "straight-lining would manufacture revenue that has not been collected), **project-level only** (so "
              "consolidated affiliate income is out of scope), and a 24-month audit look-back with a 12-month audit "
              "window, a confidentiality undertaking, and no contingency-fee auditors.")

    # 6.2 TAX ABATEMENT
    h2(doc, "6.2  Tax abatement: three separate problems, one of which is not curable by the lease", "6.2")
    body(doc, "You asked us to make sure the abatement applies during the income-producing years. There are three "
              "distinct issues, in ascending order of seriousness.")
    body(doc, "**(a) Measurement base.** The percentages (25% / 50% / 75%) are applied to \"the full post-development "
              "assessed value,\" and the Term Sheet then illustrates the result using $178,000,000. We have drafted "
              "the clause to apply to the assessed value the Assessor *actually* determines (Section 6.6), with the "
              "$178,000,000 figures expressly illustrative. You do not want to be locked to a $178,000,000 base if the "
              "Assessor comes in at $200,000,000, nor does the Authority want to be locked to it if the Assessor comes "
              "in lower; the percentage mechanic is the deal, not the dollar projection.")
    body(doc, "**(b) Starting date — this is the timing point you raised.** Term Sheet § 10 provides that the 15-year "
              "period \"shall commence on the Lease Commencement Date,\" i.e. October 1, 2025. But the improvements "
              "will not be on the grand list until they are substantially complete, around October 2030. On that "
              "structure, **five of the fifteen years are consumed before the asset exists**, and the 25% band — the "
              "most valuable band — covers a period in which the property is assessed as vacant land. On our "
              "computation the nominal value of the abatement is $46,391,250 over fifteen years; on the Term Sheet's "
              "structure a significant part of that is simply unattainable. Section 6.7 re-anchors the period to the "
              "later of the Rent Commencement Date and the first fiscal year in which the completed Improvements are "
              "reflected in the assessment. Expect this to be the hardest of the three to obtain, because the City may "
              "have its own fiscal-year constraints; it is nevertheless the single highest-value, lowest-visibility "
              "change in the document, and Coventry's model depends on it.")
    body(doc, "**(c) The obligor is not a party to the lease.** The abatement is granted and administered by the City "
              "of Port Calloway, not by the Authority; the Board resolution itself contemplates \"a separate tax "
              "abatement agreement between Meridian and the City of Port Calloway.\" The Authority therefore cannot "
              "grant the abatement, and a covenant by the Authority to provide it is worth only what the Authority's "
              "influence with the City is worth. Section 6.9 obliges the Authority to use diligent efforts and to join "
              "in all applications and hearings, and Section 2.3(f) makes execution of the Tax Abatement Agreement a "
              "condition precedent to Lease Commencement. But the protection you actually need is a financial "
              "backstop, so Section 6.8 provides one: if the abatement is not implemented, is reduced or is repealed "
              "for any reason not attributable to Tenant, Tenant receives a dollar-for-dollar credit against Base Rent "
              "for the excess taxes. That converts a political risk into a rent adjustment, which is a risk the "
              "Authority controls and can therefore price.")
    flagbox(doc, "Not curable in the lease.",
             "We have not verified the City's statutory authority to grant a fifteen-year, three-tier abatement. "
             "Connecticut's tax-abatement statutes impose term limits and procedural requirements (public hearing, "
             "legislative-body approval), and different provisions apply in different contexts, including urban "
             "renewal and redevelopment areas. If the fifteen-year structure is outside the City's authority, or if "
             "the required hearing is not held, the pro forma does not work and no amount of lease drafting fixes it. "
             "**This should be confirmed with Connecticut municipal finance counsel before the Board votes**, not "
             "after. Item 7.2 of Part 7.")

    # 6.3 ELUR
    h2(doc, "6.3  ELUR: the ground-floor residential prohibition against a ground-floor residential program", "6.3")
    body(doc, "The ELUR prohibits residential use on the ground floor of any structure on the Premises because "
              "near-surface soils exceed the Residential Direct Exposure Criteria. The Term Sheet describes the "
              "Project as including \"ground-floor residential lobby and amenity spaces (fitness center, package room, "
              "resident lounge, and leasing office)\" and permits \"residential apartments\" without a floor "
              "restriction. Halcyon addressed the tension directly and did not resolve it: the ELUR defines "
              "residential use as \"habitable space at or below finished grade elevation intended for residential "
              "dwelling, sleeping, cooking, or eating purposes\" and \"does not define or specifically address "
              "non-habitable spaces such as building lobbies, mail rooms, fitness centers, package rooms, leasing "
              "offices, or common amenity areas.\" Halcyon's recommendation is a formal DEEP interpretation or variance "
              "before the design is finalized.")
    body(doc, "This matters in three ways that are easy to miss. **First, permitting.** DEEP approval is on the "
              "critical path to Milestone 1, and an ELUR enforcement question can stop a building permit. **Second, "
              "the milestone clock.** If DEEP's interpretation requires a redesign of the ground floor, the delay will "
              "count against Milestone 1 (18 months) unless it is expressly treated as a force majeure event or a "
              "permitting delay — which is why Section 7.8(b) and Section 3.4 say so. **Third, cost allocation.** An "
              "ELUR modification application is expensive, and it is expensive because of a pre-existing condition the "
              "Authority created and disclosed in 2018, not because of anything Tenant did. Section 7.8(a) puts that "
              "cost on the Authority.")
    body(doc, "There is a helpful physical fact in the record that the parties should not lose: the project's ground "
              "floor will be at **finished floor elevation 15 feet NAVD88**, while existing site grades run from "
              "approximately 10.2 to 14.8 feet NAVD88 and the BFE is 12 feet. On the ELUR's own definition (space \"at "
              "or below finished grade elevation\"), a slab at 15.0 feet is above grade across essentially the whole "
              "site. That is a strong argument that the ground floor is not within the restricted zone at all — but it "
              "is an argument, not a determination, and DEEP has not been asked. Section 7.8(c) records the point for "
              "use in the application.")
    body(doc, "Two related ELUR obligations that appear nowhere in the Term Sheet and are now in the Draft Lease: the "
              "ELUR's prohibition on potable water supply wells (Section 7.7(e)), and the annual ELUR compliance "
              "certification to DEEP (Section 7.7(f)). The latter raises an allocation question the Term Sheet does not "
              "answer: the certification is required of the \"owner, operator, or designee,\" and the fee owner is the "
              "Authority. Section 7.7 obliges the Authority to join in any filing requiring the fee owner's signature "
              "within ten business days. Finally, note the interaction between the 24-inch engineered barrier and the "
              "8,000 square feet of public open space: landscaping and tree planting over a capped area is constrained "
              "by both the barrier specification and the prohibition on ground disturbance below two feet without a "
              "DEEP-approved Soil Management Plan (Section 14.4, final sentence).")

    # 6.4 REMEDIATION
    h2(doc, "6.4  Remediation: the $2.4 million estimate is not a cap, and Tenant bears every dollar above it", "6.4")
    body(doc, "Term Sheet § 7 provides a fixed $1,800,000 credit and makes Tenant responsible for the $600,000 balance "
              "**and for \"any actual remediation costs in excess of the $2,400,000 estimate.\"** Because the credit is "
              "fixed, Tenant keeps the benefit if costs come in lower and absorbs the whole of any overrun. Three "
              "observations.")
    body(doc, "**First, the estimate has arithmetic problems** (Part 2.6): the contingency lines labelled \"10%\" are "
              "5.71% and 4.76%. If 10% is intended, the total is $2,502,500 and Tenant's residual is $702,500 rather "
              "than $600,000.")
    body(doc, "**Second, and much more seriously, the estimate almost certainly does not cover the excavation the "
              "project actually requires.** Halcyon's estimate assumes excavation of the two delineated areas: 933 "
              "cubic yards in Area 1 and approximately 600 in Area 2 — about 1,533 cubic yards of contaminated soil, "
              "priced on a material handling volume of about 3,700 cubic yards. But the Term Sheet's project "
              "description includes \"structured and/or below-grade parking,\" and a below-grade parking structure "
              "across any meaningful part of a 139,392 square foot site generates a different order of magnitude:")
    table(doc,
          [["Excavation footprint", "Depth", "Soil volume", "Multiple of the 1,533 CY of delineated contamination"],
           ["20,000 SF", "12 ft", "8,889 CY", "5.8×"],
           ["40,000 SF", "12 ft", "17,778 CY", "11.6×"],
           ["60,000 SF", "12 ft", "26,667 CY", "17.4×"]],
          [1.7, 0.9, 1.5, 2.4], size=8, align_right=[1, 2, 3])
    body(doc, "Every cubic yard excavated below the cap must be handled under a DEEP-approved Soil Management Plan, and "
              "much of it will require characterization, stockpiling, testing and — where it is or may be impacted — "
              "licensed disposal. The estimate does not address this, and the ELUR separately prohibits excavation "
              "below the engineered barrier without DEEP's written approval, which is itself a schedule item for "
              "Milestone 1. On the record before us, the probability that Tenant's remediation cost exceeds $2.4 "
              "million is high, and the excess is 100% Tenant's under the Term Sheet.")
    body(doc, "**Third, the contamination is the Authority's legacy.** The Premises were a ship repair and dry dock "
              "facility from 1942 to 1987; the Authority acquired the land by condemnation in 2012, performed a "
              "partial remediation in 2016–2017, and recorded the ELUR in 2018. Tenant did none of it. Section 7.4(c) "
              "therefore draws the line where it belongs: Tenant bears the cost of remediating the two areas the Phase "
              "II delineated, and Landlord bears the cost of a Pre-Existing Environmental Condition that was *not* "
              "identified, delineated or quantified — undiscovered contamination, contamination beyond the delineated "
              "depths, off-site migration, groundwater and sediment impacts, and any DEEP-imposed requirement not "
              "contemplated by the Phase II. Section 7.5 adds a full Landlord indemnity for Pre-Existing Environmental "
              "Conditions, running to Tenant, its members, its agents and each Leasehold Mortgagee. Section 7.6 caps "
              "Tenant's reciprocal indemnity. Together these are the most important economic protections in Article 7 "
              "after the credit itself, and they are the provisions most likely to be resisted; expect the Authority "
              "to offer a smaller version of § 7.4(c), such as a shared overrun above a threshold. A 50/50 sharing "
              "above $2.4 million would be an acceptable landing zone.")
    body(doc, "One further point on the credit mechanics, which you asked us to make unambiguous. Section 7.2 states "
              "the waterfall as a table (months 1–7 at zero, month 8 credit $137,500 with $100,000 payable, month 9 "
              "onward full rent), confirms that the credit is not reduced by any other credit or abatement, allows "
              "unabsorbed credit to be applied against other Rent or paid in cash, and — the provision that was "
              "missing — requires Landlord to **pay any unapplied balance in cash if the lease ends before the credit "
              "is exhausted**. Without that last sentence, an early termination (say in month 3) would forfeit roughly "
              "$962,500 of credit that Tenant had effectively paid for through its remediation work.")

    # 6.5 BULKHEAD
    h2(doc, "6.5  Bulkhead: an unquantified structural liability inside a triple-net lease", "6.5")
    body(doc, "Halcyon inspected approximately 480 linear feet of bulkhead and found it in \"fair to poor condition,\" "
              "with lateral displacement, longitudinal and transverse cracking, deteriorated and missing timber "
              "lagging, and erosion of backfill. The survey adds spalling of the concrete cap, corrosion of the sheet "
              "piling, and \"evidence of partial demolition activity ... consistent with work reportedly performed by "
              "Calloway Marine Demolition Inc.,\" including removal of approximately 40 linear feet of concrete cap. "
              "Halcyon recommends an independent structural engineering assessment and expressly excludes bulkhead "
              "repair or replacement from its $2.4 million cost estimate. The Term Sheet says nothing about the "
              "bulkhead at all.")
    body(doc, "Under a triple-net ground lease, and again under the surrender obligation in Term Sheet § 18 (\"good "
              "condition, reasonable wear and tear excepted\"), that liability lands on Tenant — for an asset that was "
              "already deteriorated when the Authority delivered it and that the Authority's own contractor partially "
              "demolished in 2025. Section 2.9(b) requires the Authority to commission and pay for the structural "
              "assessment before Lease Commencement, and Section 14.3 offers the alternative allocation (Authority "
              "repairs, or Tenant repairs with a dollar-for-dollar rent credit), with an express carve-out from "
              "Tenant's maintenance obligation for any pre-existing structural deficiency documented in the "
              "assessment. We recommend obtaining the assessment **now**, before the lease is negotiated, because the "
              "size of the number will determine which allocation is realistic. Note also that bulkhead work will "
              "require coastal permits (Structures, Dredging and Fill; tidal wetlands) and City cooperation, and that "
              "the bulkhead sits at or near the pedestrian access easement, whose terms prohibit permanent structures "
              "— Section 14.3(d) addresses both.")

    # 6.6 MECHANICS LIEN
    h2(doc, "6.6  The mechanics' lien: the Term Sheet cannot make it a Permitted Exception", "6.6")
    body(doc, "A $187,500 mechanics' lien was filed on April 3, 2025 by Calloway Marine Demolition Inc. against the "
              "Authority's fee interest (Vol. 418, Pg. 302) for bulkhead demolition work. Term Sheet § 13 lists it as "
              "Permitted Exception No. 6 — that is, the lease would insure subject to it. The title commitment says "
              "the opposite in terms: \"The Company will not issue either policy described in Schedule A until this "
              "requirement has been satisfied,\" and until then \"Exception No. 6 shall remain as an exception to "
              "coverage.\" Requirement No. 7 offers three routes — discharge, a bond under Conn. Gen. Stat. § 49-37, "
              "or an indemnity from the fee owner. Bayside § 6(c) separately requires that all exceptions be reviewed "
              "and approved by the Lender.")
    body(doc, "The lien arises from work performed for the Authority, on the Authority's fee, before Tenant had any "
              "interest. Tenant should not pay it, insure over it, or accept it. Section 2.9(a) puts the obligation on "
              "Landlord at its sole cost, and Section 2.3(h) makes discharge or bonding a condition precedent. There "
              "is also an unresolved question worth asking: the demolition work that generated the lien is the same "
              "work that removed 40 feet of bulkhead cap. The Authority should be asked whether it has a claim against "
              "the contractor, and whether the lien is being defended rather than simply paid — because if the "
              "contractor's work is the cause of the bulkhead damage described in Part 6.5, that is a cost the "
              "Authority should bear twice over.")

    # 6.7 ROFR
    h2(doc, "6.7  The recorded right of first refusal will bind regardless of what the lease says", "6.7")
    body(doc, "Term Sheet § 11 creates a ROFR for the first twenty years, with no carve-out for Leasehold Mortgagee "
              "enforcement. But there is also a **recorded** Declaration of Right of First Refusal dated September 8, "
              "2019 (Vol. 405, Pg. 55), and the title commitment tells us exactly what it does not contain: it \"does "
              "not by its terms contain any exception or carve-out for transfers resulting from foreclosure, "
              "deed-in-lieu of foreclosure, the exercise of remedies by a leasehold mortgagee, or assignments by a "
              "leasehold mortgagee or its designee following a foreclosure or acceptance of a deed-in-lieu,\" and it "
              "\"is binding upon the Tenant and all successors and assigns.\"")
    body(doc, "That is a direct collision with Bayside § 5.6 (unconditional right to foreclose and assign without "
              "Landlord's consent) and with the 100% membership-interest pledge Bayside requires under § 4. A lease "
              "provision cannot cure it; only a recorded amendment can. Section 11.5 of the Draft Lease narrows the "
              "ROFR in four ways (direct assignments for value only; no ROFR for Permitted Transfers, mortgagee "
              "transfers, recapitalizations or New Leases; acquisition subject to the leasehold mortgage and requiring "
              "the mortgagee's consent or payoff; lapse if the Authority elects but fails to close) and the drafting "
              "note records that the recorded Declaration \"must be amended of record\" before Lease Commencement. "
              "Exhibit B, Part 4 describes the permitted exception as the Declaration *as so amended*.")
    body(doc, "There is a secondary point in your instruction that the ROFR should not \"interfere with the financing "
              "or any future recapitalization.\" Term Sheet § 11's Affiliate definition is reasonably broad, but it "
              "captures control, not economic interest, so a Coventry-led recapitalization in which Coventry's fund "
              "brings in a new institutional partner and Meridian's sponsorship interest is diluted could be argued to "
              "be a non-Affiliate transfer. Section 11.3 addresses this with a ten-item Permitted Transfers list "
              "including transfers of direct or indirect ownership interests, pledges and foreclosures of membership "
              "interests, buy-sell and drag-along exercises, transfers to Coventry vehicles, and a 20% look-through "
              "test. Section 11.7 then states expressly that no change of control is an assignment. We recommend "
              "confirming that list with Ansel, because it is his exit path that is being protected.")

    # 6.8 SECURITY DEPOSIT
    h2(doc, "6.8  Security deposit: two ambiguity traps and a conflict", "6.8")
    body(doc, "The amounts are right (24 × $237,500 = $5,700,000; 12 × $237,500 = $2,850,000), and the step-down "
              "concept is standard. Three problems remain. **(a) \"Overall occupancy rate of 90%\" is undefined in a "
              "three-product-type project** — 90% of units, of rentable square feet, of each component, or blended? A "
              "project that is 95% leased residentially and 70% leased in the office building is not 90% occupied by "
              "any measure the parties will agree on after the fact. Section 8.4(a) defines an Occupancy Rate as "
              "rentable square footage leased over rentable square footage completed, tested only against completed "
              "buildings, with residential measured on unit net rentable area. **(b) Documentation and timing were "
              "missing**; Section 8.4(b)–(c) requires a certified rent roll and officer's certificate, gives the "
              "Authority 30 days to object (deemed approved), and requires the amendment or replacement letter of "
              "credit within 10 business days. **(c) The \"twelve months of the initial Base Rent\" characterisation "
              "is already stale** — if 90% occupancy is first achieved in, say, Lease Year 8, Base Rent is $268,709 a "
              "month and $2,850,000 is less than eleven months' rent. We have drafted the reduction as a fixed "
              "$2,850,000 with no reinstatement (Section 8.4(d)), which is the Tenant-favourable reading; the Authority "
              "may ask for twelve months of *then-current* rent, which we would resist.")
    body(doc, "The conflict is the issuer test: Term Sheet § 8 requires an A-/A3 bank; the Board resolution recital "
              "describes a \"federally chartered banking institution.\" Section 8.3 accepts either, and Section 8.2 "
              "preserves Bayside's own option (§ 4) of a cash deposit. Two further Tenant protections are worth "
              "noting: draws are limited to amounts finally determined to be due (Section 8.5), and a failure to renew "
              "the letter of credit is not a default until ten business days after notice (Section 8.8). The Term "
              "Sheet made non-renewal an immediate Event of Default.")

    # 6.9 INSURANCE
    h2(doc, "6.9  Insurance: the NFIP \"maximum\" standard cannot work on this site", "6.9")
    body(doc, "Term Sheet § 12(d) requires flood insurance \"in no event less than the maximum coverage available "
              "under the National Flood Insurance Program or equivalent private market policy.\" The NFIP maximum for "
              "a commercial building is $500,000 ($250,000 for a residential building) plus contents — against a "
              "project with a $425 million cost basis sitting entirely within Zone AE. Bayside § 6(h) requires flood "
              "insurance \"in amounts satisfactory to Lender,\" which will mean full replacement cost. Section 12.1(f) "
              "reconciles the two by requiring NFIP maximum *plus* excess flood or difference-in-conditions coverage "
              "to full replacement cost. That is more coverage and more premium than the Term Sheet contemplated; it "
              "is also the only version that survives a lender's insurance review, so we recommend raising it with Mr. "
              "Koss as a correction rather than a concession.")
    body(doc, "Two smaller points. Term Sheet § 12 names the Authority as an additional insured on the **all-risk "
              "property** policy; an additional-insured endorsement is the wrong instrument for a fee owner's interest "
              "(a mortgagee/loss-payee endorsement or a waiver of subrogation is the right one), and Section 12.2 "
              "confines the Authority to additional insured on the liability policy. And Phase II recommends a "
              "pollution legal liability policy with a term reflecting the length of the ground lease; Section 12.1(e) "
              "requires, to the extent available on commercially reasonable terms, multi-year coverage for "
              "Pre-Existing Environmental Conditions, with Section 7.9 directing proceeds to the remediation cost.")

    # 6.10 ASSIGNMENT
    h2(doc, "6.10  Assignment, subletting and the interaction with the loan documents", "6.10")
    body(doc, "Three documents impose three regimes: Term Sheet § 11 (consent plus ROFR for non-Affiliate "
              "assignments, free subletting), Bayside § 5.6 (foreclosure and assignment without consent) and Bayside "
              "§ 4 (first-priority pledge of 100% of the membership interests in Meridian). The pledgor's problem is "
              "that a foreclosure of the pledged membership interests is a change of control, which a naively drafted "
              "assignment clause could read as a prohibited transfer. Section 11.3 resolves it expressly, and Section "
              "11.7 states that no change in ownership or control is an assignment. Section 11.2 preserves subletting "
              "freedom, which matters more than it looks: with a 28-story residential tower, a leasing office that "
              "cannot sign residential leases without consent is not a leasing office.")

    # 6.11 AFFORDABLE
    h2(doc, "6.11  Affordable housing: the covenant is agreed, but it is not yet a workable instrument", "6.11")
    body(doc, "You are right that this should not be contentious. But the title commitment's own note identifies six "
              "things the recorded 2019 Declaration of Restrictive Covenants does not specify: how the 15% is "
              "recalculated if the unit count changes, income verification procedures, a monitoring or enforcement "
              "entity, the consequences of non-compliance, whether units must be distributed through the project, and "
              "any floor or location rules. Section 14.5 fills all six — with the important overlay that the ELUR's "
              "ground-floor restriction means affordable units must be on upper floors (Halcyon says so expressly), "
              "which also means the covenant and the ELUR should be read together. Two drafting choices are yours to "
              "confirm: the AMI geography (we adopted New Haven-Milford, the geography in the recorded covenant, "
              "because the Premises are in New Haven County; the Term Sheet says \"Port Calloway MSA\" and the survey "
              "says \"Bridgeport-Stamford-Norwalk,\" and at least one of those is wrong), and the remedy (we have "
              "limited the Authority to specific performance and injunctive relief, with no default, no reverter and "
              "no draw on the deposit — a breach of a 15% covenant should never forfeit a $425 million project).")

    # 6.12 FLOOD
    h2(doc, "6.12  Flood resilience: three feet of freeboard for a 99-year coastal lease", "6.12")
    body(doc, "All three of the term sheet, title commitment and survey settle on a finished floor elevation of 15 feet "
              "NAVD88 — three feet above the BFE of 12 feet. Halcyon recommends 16 to 17 feet (four to five feet of "
              "freeboard), citing Connecticut Public Act 23-167 (2023), CIRCA's projections (20 inches by 2050 and up "
              "to 80 inches by 2100 under high-emission scenarios), the emergence of four-to-five-foot municipal "
              "standards in coastal Connecticut, the fact that roughly 60% of the parcel lies at or below the BFE, and "
              "a November 2024 nor'easter that put water at approximately 10.5 feet NAVD88 at this bulkhead. The FIRM "
              "panel is dated January 15, 2020 and will be revised during the Term.")
    body(doc, "Section 15.3 holds 15 feet as the contractual minimum (as negotiated) but permits Tenant to build "
              "higher, and Section 15.4 allocates code change over the Term to Tenant with the benefit of any "
              "phased-compliance or hardship relief, no rent increase, and a force-majeure/permitting extension for "
              "the time needed to obtain relief. Our commercial recommendation is that you evaluate now, not in 2040, "
              "whether to build to 16–17 feet: the incremental structural cost on a 28-story tower is small relative "
              "to the cost of a later retrofit or of uninsurable ground-floor retail, and it will be far easier to "
              "persuade the Authority and Bayside to accept a higher elevation at design stage than to explain a "
              "flood claim later.")

    # 6.13 FINANCING MISMATCH
    h2(doc, "6.13  The financing does not cover the development program", "6.13")
    body(doc, "Two mismatches in the loan documents should be raised with Sandra Milliken before the loan documents are "
              "negotiated. **First**, the construction loan has a 48-month term with two 6-month extensions — a "
              "maximum of 60 months — while Milestone 3 (Phase 1 substantial completion) is set at 60 months and "
              "Milestone 4 (the office building) at 84 months. Phase 2 is therefore unfinanced, and Phase 1 completion "
              "coincides with final maturity rather than preceding it. **Second**, Coventry's completion guaranty under "
              "Bayside § 4 guarantees lien-free completion \"on or before the Initial Maturity Date,\" i.e. 48 months "
              "from closing; but the ground lease allows 60 months for Phase 1. Coventry could be in default of its "
              "guaranty a full year before the ground lease milestone is missed. These are loan-document issues rather "
              "than lease issues, but they will surface in the same negotiation and they affect how much enforcement "
              "pressure the Authority can apply through us.")

    # 6.14 CLOSING MECHANICS
    h2(doc, "6.14  Closing mechanics: three dates that will not line up", "6.14")
    bullet(doc, "**The survey goes stale on July 19, 2025** for purposes of Bayside § 6(d), which requires a survey "
                "\"dated within ninety (90) days of the closing date.\" The field survey is April 20, 2025. Any closing "
                "after July 19 requires a re-certification or update. Section 2.3(c) requires a survey dated within 90 "
                "days of Lease Commencement.")
    bullet(doc, "**The title commitment expires on December 1, 2025** — six months after its effective date. That is "
                "tight but workable for an October 1 commencement, and not workable at all if the lease slips into "
                "December. An extension should be requested now rather than in November.")
    bullet(doc, "**Bayside's term sheet expired on June 27, 2025** if not executed and returned by then (Bayside "
                "§ 12). We do not have an executed copy in the record. Please confirm the status, because the "
                "sixty-day exclusivity and the § 5 ground lease conditions both run from execution, and there is a "
                "further oddity: a term sheet dated May 28 refers to a ground lease term sheet \"dated June 10, "
                "2025,\" so the version in the record may post-date its own cover date.")

    # 6.15 END OF TERM
    h2(doc, "6.15  End of term: 99 years, then nothing", "6.15")
    body(doc, "Term Sheet § 18 provides that at expiration all improvements become the Authority's property \"without "
              "any payment, compensation, or reimbursement,\" and § 3 confirms there are no renewal options. That is "
              "market for a ground lease and we have not disturbed it in Section 17.2. But it should be seen clearly "
              "for what it is: Meridian invests $425 million in buildings on land it will never own, and, absent an "
              "extension or purchase right, receives nothing at the end. We have bracketed three alternatives in "
              "Section 17.2 — a 25-year extension option, a purchase option at appraised value in the final ten years, "
              "or a right of removal or purchase for trade fixtures — and note that an extension option conflicts with "
              "Resolution No. 2025-047, § 4(b), which caps the lease term at ninety-nine years. Any of the three "
              "requires Board action. Our view is that the extension option is worth pursuing now, while the "
              "Authority needs the transaction, rather than in year 90.")
