
# 4. CREDIT CAPACITY, VALUATION AND LOAN SIZING

The four issues in this section are analytical rather than drafting points in the narrow sense, but they determine whether the covenant, reserve and cure architecture we have drafted can function. I have recomputed each figure from source components.

**4.1 Debt service capacity and the DSCR covenant — recomputation.**

**Source components.** Loan $14,750,000 (Term Sheet §3.1); interest rate Daily SOFR plus 285 basis points with a 3.00% SOFR floor, i.e. 5.85% at the floor (Term Sheet §3.6); interest-only for months 1–24, then 25-year amortization from May 15, 2027 (Term Sheet §3.9); DSCR covenant of 1.25x beginning after month 24 (Term Sheet §7.1); stabilized NOI of $622,772 on the borrower's best-case projection (Rent Roll, Vacancy Schedule rows 8–18, being $755,549 gross revenue less $37,777 vacancy/credit loss less $95,000 net landlord expense burden).

**Recomputation.**

| Metric | Amount | Basis |
|---|---|---|
| Annual interest during interest-only period | $862,875 | $14,750,000 × 5.85% (the rent roll shows $863,375 — a $500 rounding error in the file) |
| Monthly payment, 25-year amortization at 5.85% | $93,686.61 | Standard amortization formula, 300 periods |
| Annual debt service after the interest-only period | $1,124,239 | $93,686.61 × 12 (the rent roll shows $1,122,000 — understated by $2,239) |
| DSCR on amortizing debt service | **0.55x** | $622,772 ÷ $1,124,239 |
| DSCR on interest-only debt service | **0.72x** | $622,772 ÷ $862,875 |
| NOI required to meet 1.25x on amortizing debt service | **$1,405,299** | $1,124,239 × 1.25 |
| NOI required to meet 1.25x on interest-only debt service | **$1,078,594** | $862,875 × 1.25 |
| Shortfall against the amortizing requirement | $782,527 (125.6%) | $1,405,299 − $622,772 |
| Debt yield | **4.22%** | $622,772 ÷ $14,750,000 |
| Loan size supported at 1.25x DSCR (25-year amortization, 5.85%) | ≈ **$6,536,000** | $622,772 ÷ 1.25 ÷ 0.0762196 |
| Loan size supported at a 9.0% debt yield | ≈ **$6,920,000** | $622,772 ÷ 0.09 |

**Conclusion.** On the file's own numbers the Loan is approximately twice the size that the Property's income supports. The interest due during the interest-only period ($862,875) exceeds the Property's projected gross revenue at stabilized occupancy ($755,549). The Vacancy Schedule states the same conclusion in terms (row 25: "DOES NOT MEET 1.25x COVENANT"; row 39: "DSCR compliance at month 24 is at significant risk regardless of lease-up pace"). The Term Sheet's own requirement for an Interest Shortfall Guaranty covering the first fourteen months after closing (Term Sheet §5.5(c)) is consistent with — and corroborates — the proposition that the parties expect the Property not to cover debt service during the renovation and lease-up period.

**Options, for your discussion with Marcus Prideaux.** (i) Reduce the loan amount to a supportable level; (ii) lengthen the interest-only period to or beyond the first DSCR test date and reset the covenant (the Term Sheet already ends interest-only at month 24, one month before amortization begins in the same window in which the covenant is first tested); (iii) retain the loan amount but require a DSCR cure deposit, a cash-management sweep at a sub-1.10x trigger and an extension of the Interest Shortfall Guaranty through at least the first test date; (iv) treat the DSCR covenant as a placeholder and obtain a documented credit exception. What we should not do is paper the covenant as drafted and say nothing: a covenant that fails on the closing-date projections is either a default trigger from day one or evidence that the covenant was not intended to be enforced, and neither posture serves the Bank well in a workout. **Draft:** Article 12 implements the covenant precisely (Section 12.1), defines Net Operating Income and Annual Debt Service (Section 1.1), and adds a limited DSCR cure right (Section 12.6) — the Term Sheet's "without cure" language in §11.1(i) presupposes a cure mechanic that the Term Sheet never supplies. The cure mechanic is our construct and requires your approval (Section 10).

**4.2 The appraisal does not reconcile to its own income approach.**

| Appraisal input | Figure | Source |
|---|---|---|
| Concluded as-is value | $18,200,000 | Appraisal §1, §6.2, §7 |
| Concluded as-stabilized value | $23,500,000 | Appraisal §1, §6.3, §7 |
| Selected going-in capitalization rate (as-is) | 6.25% | Appraisal §6.2 |
| Selected capitalization rate (as-stabilized) | 5.85% | Appraisal §6.3 |
| Stated as-is NOI | $332,000–$345,000 | Appraisal §6.2 |
| Stated stabilized NOI | $582,000–$592,000 | Appraisal §6.3 |

**Recomputation.** A 6.25% capitalization rate applied to NOI of $332,000–$345,000 indicates a value of **$5,312,000–$5,520,000**, not $18,200,000. A 5.85% rate applied to stabilized NOI of $582,000–$592,000 indicates a value of **$9,948,718–$10,119,658**, not $23,500,000. Put the other way, the concluded values imply NOI of **$1,137,500** (as-is) and **$1,374,750** (as-stabilized) — between 2.3 and 3.4 times the NOI the appraiser reports. The implied capitalization rates on the reported NOI are **1.86%** (as-is) and **2.52%** (as-stabilized), both far outside the 5.75%–6.50% range the appraiser says is market (Appraisal §4).

**Consequence.** The as-is loan-to-value ratio of 81.04% (Term Sheet §3.5; Appraisal §7) — and the Bank's reliance on it — rests on a value conclusion that its own income approach does not support. Either the NOI figures or the value conclusions are wrong; the discrepancy is not a rounding matter. Term Sheet §12.1(d) makes receipt of a satisfactory appraisal "supporting the as-is and as-stabilized values set forth in Section 2.4" a condition precedent to closing, and the appraisal must conform to USPAP and FIRREA. **Recommendation:** return the report to Pinnacle Valuation Services for correction or a written reconciliation of the income approach to the concluded values, and obtain an independent review appraisal under the Bank's appraisal policy before closing. This is also the answer to the question you raised with Marcus about whether the as-is LTV "runs a little hot": at 81.04% it is well above customary CRE leverage, and 82.87% of the purchase price ($14,750,000 ÷ $17,800,000), and on the appraiser's own income figures the ratio would exceed 100%.

**4.3 Occupancy and in-place rent — three conflicting sets of figures.**

| Item | Term Sheet §2.3 | Appraisal §§1, 3.1 | Rent Roll (Summary tab) | Recomputation |
|---|---|---|---|---|
| Occupied area | 21,400 SF | 21,400 SF | 17,400 SF | 3,800 + 3,800 + 9,800 = **17,400 SF** |
| Occupancy rate | 68% | 68% | 56.13% | 17,400 ÷ 31,000 = **56.13%** (21,400 ÷ 31,000 = 69.03%, so 21,400 and 68% are also inconsistent with each other) |
| Vacant area | 13,600 SF (43.9%) | 32% | 13,600 SF (43.87%) | 13,600 ÷ 31,000 = **43.87%** — note 68% plus 43.9% equals 111.9% |
| Total in-place annual rent | $415,100 | $415,100 | $415,100 | Sum of the three leases at stated rents = **$415,100** |
| Weighted average rent | not stated | $19.40/SF | $23.86/SF | $415,100 ÷ 17,400 = **$23.86/SF** ($415,100 ÷ 21,400 = $19.40/SF, which confirms the appraisal used the erroneous 21,400 SF) |

The Term Sheet's §2.3 contradictory within itself: it states occupancy of "approximately sixty-eight percent (68%)" and, three sentences later, that vacant space totals 13,600 square feet "or approximately 43.9% of total building area." Both statements cannot be true. The correct figures are 17,400 SF occupied, 56.13%.

**Separate but related: the rents.** The Rent Roll's Summary and Lease Abstracts tabs state the "current" base rents as $28.50/SF (Bay 1), $24.00/SF (Bay 3) and $22.00/SF (Suite A), totaling $415,100. The same tabs' escalation schedules show Bay 1 escalating 3% annually "beginning January 1, 2025" (i.e. $29.355/SF, $111,549 per annum) and Bay 3 escalating 2.5% annually "beginning July 1, 2023" (i.e. $25.215/SF, $95,817–$95,836 per annum depending on rounding). The Vacancy Schedule in fact uses $111,549 for Bay 1. The rent actually payable as of an April 15, 2025 closing, applying the contractual escalations, is therefore approximately **$422,985**, not $415,100 — a difference of $7,885 per annum that flows directly into the DSCR calculation. **Draft:** Exhibit B to the Draft Mortgage reports the lease-stated rents of $415,100 (as the record's certified rent roll) and Note 10 to Exhibit B discloses the escalation conflict, states the escalated total of $422,985, and requires Borrower to certify the conformed rent roll on or before closing. The Section 5.4 representation must not be made against a rent roll that the borrower's own document contradicts.

**4.4 Sources and uses — the closing costs are unfunded.**

| Use of funds | Amount | Source |
|---|---|---|
| Purchase price | $17,800,000 | Term Sheet §§3.2, 3.4 |
| Renovation Budget | $3,150,000 | Term Sheet §3.4; Renovation Budget |
| **Total Project Cost (as defined)** | **$20,950,000** | Term Sheet §3.4 |

| Source of funds | Amount | Source |
|---|---|---|
| Loan (Initial Advance $12,500,000 + Renovation Holdback $2,250,000) | $14,750,000 | Term Sheet §3.3 |
| Borrower Equity Contribution | $6,200,000 | Term Sheet §3.4 |
| **Total** | **$20,950,000** | |

The sources equal the uses exactly — which is the problem. The Total Project Cost as defined excludes (i) closing costs that Term Sheet §13.2 requires Borrower to pay, including the origination fee of $147,500 (Term Sheet §13.1), South Carolina mortgage recording tax of $54,575 (0.37% of $14,750,000, as you computed), title premiums, survey, appraisal, environmental and legal fees, and UCC filing and search fees; (ii) the $150,000 TI/LC Reserve required to be deposited at closing (Term Sheet §6.3); and (iii) any initial deposit into the tax and insurance escrow (Term Sheet §6.1). At closing, the Initial Advance of $12,500,000 plus the $6,200,000 equity contribution produces $18,700,000 against a purchase price of $17,800,000, leaving exactly $900,000 — which is precisely the Renovation Equity that the Draw Schedule deploys over fourteen months (Renovation Budget, Budget Detail row 9; Draw Schedule column S). On these numbers there is no source for closing costs and no source for the TI/LC Reserve. The gap is approximately **$450,000–$600,000** depending on title premium and escrow deposits (my estimate, to be confirmed from the closing/settlement statement). **Recommendation:** require an updated sources-and-uses statement and evidence of additional Borrower equity before closing; add the TI/LC Reserve funding to the closing conditions; and confirm with Prestige Title the recording fee and mortgage tax computation (Term Sheet §13.2(f)).

**4.5 Underwriting ratios — recomputed.**

| Ratio | Stated | Recomputed | Comment |
|---|---|---|---|
| Loan-to-value, as-is | 81% (Term Sheet §3.5); 81.04% (Appraisal §7) | 81.04% | Arithmetically correct; the denominator is the problem (§4.2) |
| Loan-to-value, as-stabilized | 62.77% | 62.77% | Correct arithmetic; depends on a hypothetical condition (§4.2) |
| Loan-to-cost | 70.41% | 70.41% | Correct; but the cost base omits closing costs (§4.4) |
| Loan-to-purchase-price | not stated | **82.87%** | $14,750,000 ÷ $17,800,000 |
| Borrower equity as % of Total Project Cost | 29.6% | 29.59% | Correct as against the defined total; overstated against a total that includes closing costs |
| Debt yield | not stated | **4.22%** | $622,772 ÷ $14,750,000 |
| DSCR (amortizing / interest-only) | not stated | **0.55x / 0.72x** | §4.1 |

# 5. TITLE, SURVEY AND COLLATERAL ISSUES

**5.1 The Anson Lane strip — quitclaim vesting (your item 2).** You asked three questions. Answering them on the face of the commitment:

> **(1) Is the strip insured without a carve-out?** Yes, on the face of the commitment. Schedule A, Section 4 describes Parcel Two as part of the land and Section 3 confirms fee simple vesting in Hampstead Village Holdings LLC as to both parcels; Schedule B, Part II contains no exception that excepts the strip, reduces the estate to less than fee simple, or qualifies the strip's coverage. The general exceptions (a)–(e) are the printed standard exceptions, which are committed to be removed upon delivery of the survey, affidavits, gap indemnity and lien waivers (Schedule B, Part II, Exception 1; Requirements 9, 10 and 12).
>
> **(2) Is the vesting chain complete?** On the title company's examination, yes: Quitclaim Deed from the City of Charleston dated February 28, 2019, recorded March 22, 2019, in Deed Book 1128 at Page 443, pursuant to Ordinance No. 2019-084. But the title officer expressly qualifies this: "This parcel was conveyed by Quitclaim Deed only … no warranties of title were provided … The Company's willingness to insure title to this parcel … should not be construed as a representation that the chain of title for this parcel is equivalent to that of Parcel One" (Vesting Chain Notes, item 2).
>
> **(3) Should we request an endorsement?** Yes, but note two points. First, the endorsement the title officer recommends is an ALTA 34 (Identified Exception) or other affirmative coverage specific to the parcel (Closer's Note 3), not the ALTA 9 you mentioned in your notes; ALTA 9 covers restrictions, encroachments and mineral rights and does not address quitclaim vesting. Second, the title officer reserves the right to require an additional premium for extended coverage and/or to limit coverage by endorsement on this parcel (Closer's Note 3). We should obtain written confirmation, before closing, of the precise form of affirmative coverage, the premium, and that no endorsement will limit the amount of insurance as to the strip.

**Why it matters.** The strip runs along the rear (northwest) boundary of Lots 7, 8 and 9 and provides rear access and loading for the building (Phase I ESA §2, "Physical Description of Lots"; Appraisal §2.1). Loss of, or a dispute over, the strip would impair vehicular and pedestrian access and the approved site plan — the concern you flagged. **Draft:** Section 5.3 of the Draft Mortgage contains a specific representation addressed to the quitclaim conveyance and to Borrower's title to the strip; Section 3.1(a) describes Parcel Two in the granting clause with both the ordinance and the deed references; Exhibit A carries both parcels and the Cartwright plat reference. The post-closing covenant to defend title (Section 6.15) applies to the whole Property, including the strip.

**5.2 The SCDHEC land use restriction and the controlled recognized environmental condition.**

**Facts.** Historical dry-cleaning operations at the adjoining 518 King Street (1968–2005) released perchloroethylene and petroleum solvents that migrated to the southwest corner of Lot 7. Remediation was completed under SCDHEC oversight; SCDHEC issued a No Further Action letter dated August 12, 2021 for Site ID SC-29403-0772, subject to institutional controls. The land use restriction recorded in Deed Book 1203 at Page 89 (i) prohibits residential use of the ground floor of Lot 7 (Bay 1, 520 King Street) and (ii) requires maintenance and periodic inspection of the vapor barrier beneath the Bay 1 slab, with SCDHEC approval required before any penetration (Phase I ESA §§5.1–5.3; Title Exception 4). The appraiser applied no value reduction (Appraisal §5).

**Issues.** (a) The restriction runs with the land and cannot be removed without SCDHEC approval (Title Closer's Note 1). (b) The No Further Action status is contingent on continued compliance; a breach can result in the site being reopened at the owner's expense (Phase I ESA §5.2). (c) The renovation program is directly implicated: HVAC replacement, elevator modernization and façade restoration are all in the budget, and any work affecting the Bay 1 slab requires prior written notice to SCDHEC, a vapor barrier protection plan, and post-work inspection and repair (Phase I ESA §5.3; §6(c)–(d)). The budget contains no line item for vapor barrier protection or SCDHEC coordination, and the Draw Schedule assumes HVAC work in months 2–9 without any environmental gate.

**Draft treatment.** Article 11 contains the bespoke covenant package: compliance with the LUR and all Environmental Laws (§11.1), the specific obligations not to use the Lot 7 ground floor for residential purposes, to maintain the vapor barrier, not to penetrate it without SCDHEC approval and Lender consent, to conduct annual (or more frequent) inspections, to deliver an annual compliance certificate in the form of **Exhibit F**, and not to modify, terminate or seek the release of the LUR (§11.2); notice before any work affecting the Bay 1 slab (§11.3); full recourse under the Environmental Indemnity Agreement (§11.4); Lender's right to cure (§11.5); and an Event of Default for any breach or any modification, termination or violation of the LUR (§14.1(l)), with a limited cure period (§14.2(e)). Article 8 adds a draw condition requiring SCDHEC notice, a vapor barrier protection plan and professional certification before any disbursement for work within ten feet of the Bay 1 slab (§8.5(h)), and the coordination covenant at §8.13. This implements Title Closer's Note 1 (which asks for a specific default trigger), Phase I ESA §6(d) (which asks for a continuing compliance covenant and consequences of breach), and Requirement 6 of the commitment (which requires the Environmental Indemnity Agreement to address the vapor barrier and SCDHEC compliance specifically). **Action:** confirm that the Environmental Indemnity Agreement, as issued by the Bank, contains the Requirement 6 language; the draft Mortgage assumes that it does (§11.4). Also confirm the inspection interval the Bank wants (the LUR is described only as requiring "periodic inspection"; the draft uses annual).

**5.3 Balcony encroachment over the King Street right-of-way.**

**Facts.** A decorative iron balcony projects approximately 2.5 feet over the King Street right-of-way (Title Exception 5; Appraisal §2.1). The title company makes no representation as to any permit, license or encroachment agreement, recommends an ALTA 28.1 (or equivalent) endorsement if coverage is wanted, and advises that evidence of a valid encroachment permit be obtained and reviewed before closing (Title Exception 5; Closer's Note 2). The appraiser treats it as minor but notes that any City-mandated removal could affect the historic façade and require work beyond the current budget (Appraisal §§2.1, 2.2). The façade restoration line item of $625,000 expressly includes "decorative ironwork repair (including King Street balcony)" (Renovation Budget, Budget Detail line 3) and is subject to Board of Architectural Review oversight.

**Issues.** (i) The encroachment remains a title exception unless affirmative coverage is obtained; (ii) there is no encroachment license in the record, so the City's position is unknown; (iii) the renovation scope touches the balcony, which may require the City to confirm or condition the license, and removal (if required) is an unbudgeted cost; (iv) a municipal removal order would not be a taking and would not produce condemnation proceeds. **Draft:** Section 5.14 (representation disclosing the encroachment), Section 6.5 (compliance with permits and obligation to maintain the encroachment license), Section 8.7 (BAR approvals), and the Permitted Exceptions schedule (Exhibit C, item 4). **Action:** request evidence of the encroachment license now and make delivery of the license (or a written statement from the City that no license is required for the existing balcony) a closing condition. Consider also making the ALTA 28.1 endorsement a closing condition, since the Term Sheet §5.6 already requires "such endorsements as Lender may reasonably require."

**5.4 Leases, estoppels, SNDAs and the Bay 2 right of first refusal.**

**Facts.** Three leases are in place (Exhibit B to the Draft Mortgage; Rent Roll, Lease Abstracts):

> • **Lowcountry Provisions Inc.** (Bay 1; 3,800 SF; NNN; expires December 31, 2027). The lease contains **no assignment or subletting provision**, **no estoppel certificate obligation** and **no subordination or SNDA provision**. The tenant holds an exclusive right to use as a specialty grocery within the Property. The abstract notes "Assignment/Subletting: No provision."
>
> • **Harmon & Wren Design Studio LLC** (Bay 3; 3,800 SF; modified gross; expires June 30, 2026). Assignment requires consent not unreasonably withheld; estoppel within 15 business days of request; lease is subordinate to any mortgage **provided the mortgagee delivers a commercially reasonable non-disturbance agreement**. The tenant holds a **right of first refusal on Bay 2** (15 business day acceptance period) which survives renewal. A three-year renewal option requires notice by December 31, 2025. The lease's early termination right (effective June 30, 2025) required notice by December 31, 2024, which has passed, so the right has lapsed.
>
> • **Tidemark Consulting Group LLC** (Suite A; 9,800 SF; NNN; expires March 31, 2029). Assignment requires consent which may be withheld in the landlord's sole discretion; estoppel within 10 business days; tenant agrees to execute an SNDA upon request.

**Issues.**

> **(a) Closing conditions depend on third parties.** Term Sheet §§2.3 and 12.1(j)–(k) require estoppel certificates and SNDAs from all three tenants as conditions precedent. Two of the three leases obligate the tenant to deliver an estoppel on request (and Harmon & Wren's lease conditions its subordination on receipt of a commercially reasonable non-disturbance agreement), but the Lowcountry lease obligates the tenant to do neither. The condition can therefore only be satisfied with that tenant's voluntary cooperation. You are right that the Lowcountry estoppel should not be waived; the Draft Mortgage accordingly makes delivery of the estoppels a condition to the Initial Advance (Section 6.7(c)) and, because the tenant cannot be compelled, couples it with a commercially reasonable efforts covenant rather than an absolute obligation that Borrower would breach at closing. Note also that Requirement 11 of the title commitment requires delivery of tenant estoppel certificates from all tenants in occupancy as a condition to the **issuance of the policy**, so the same third-party dependency burdens the title condition as well as the loan conditions. **Action:** Marcus should be told that the Lowcountry estoppel and SNDA are outside Borrower's control and that the Bank's options are to waive or to delay closing.
>
> **(b) The Bank must decide whether it will give non-disturbance.** Because the pre-existing leases are prior in time to the Mortgage, foreclosure will not extinguish them unless they are subordinated. Harmon & Wren's and Tidemark's leases subordinate only in exchange for a commercially reasonable non-disturbance agreement. The Lowcountry lease is silent, so its position on foreclosure is unresolved. The Draft Mortgage therefore (i) subordinates the leases to the Mortgage (§4.5), (ii) requires Borrower to use commercially reasonable efforts to deliver SNDAs (§4.4), and (iii) preserves Lender's discretion whether to deliver a non-disturbance agreement (§4.5).
>
> **(c) The Bay 2 right of first refusal affects the collateral and any foreclosure purchaser.** The ROFR constrains lease-up of Bay 2 (the appraiser adds 60–90 days to the absorption timeline, Appraisal §§3.2, 6.3; the Vacancy Schedule notes the marketing constraint) and, if not subordinated, would bind a purchaser at foreclosure. Section 4.5 of the Draft Mortgage provides that any SNDA delivered by Lender may provide that purchase rights of this kind are not binding on Lender or a foreclosure purchaser. **Action:** obtain that provision in the Harmon & Wren SNDA; also confirm that the $550,000 TI allowance line covers the Bay 2 build-out notwithstanding the ROFR process.
>
> **(d) The assignment of rents and the Lowcountry lease.** You are correct that, under the South Carolina Uniform Assignment of Rents Act, the assignment is enforceable against a tenant upon notification irrespective of the lease's silence on assignment. The Draft Mortgage implements this as an absolute and present assignment (Article 4), with the statutory basis identified, a revocable license to collect until default (§4.2), enforcement on default without court order or receiver (§4.3), tenant direction letters and estoppels (§4.4), and an express representation that Borrower has full right and authority to assign all rents, naming the Lowcountry lease (§5.4). **Verification required:** the citation you used (§ 29-3-100 et seq.) should be verified against the current Code before the instrument is recorded; the Draft Mortgage refers to the Act by name and to Title 29, Chapter 3 rather than to a specific section range, and we should confirm the statutory requirements (effectiveness on execution and recording, perfection by recording, enforcement upon default) in the research file.

**5.5 Survey, legal description and Permitted Exceptions.**

> **(a) No metes and bounds in the record.** The Term Sheet's Exhibit A is a summary description by plat reference; the commitment's Schedule A describes Parcel One by plat reference and Parcel Two by ordinance, deed and the Cartwright plat (Plat Book 64, Page 91). The ALTA/NSPS survey itself is not in the file and is a closing requirement (Requirement 9; Term Sheet §12.1(e)). Exhibit A to the Draft Mortgage therefore carries the commitment description and the plat references, with a clearly bracketed instruction for the metes and bounds to be inserted from the certified survey. **This is the only substantive blank in the instrument** (Section 12). Do not record until it is conformed.
>
> **(b) Survey recertification timing.** Requirement 9 requires a survey "dated or re-certified to a date not more than ninety (90) days prior to the date of closing." The survey is dated January 15, 2025. Ninety days later is April 15, 2025 — the anticipated closing date exactly. Any slippage in closing requires recertification, and the Term Sheet permits closing as late as May 15, 2025 (Term Sheet §14.5). Request recertification now.
>
> **(c) Permitted Exceptions require Lender's written approval.** Neither the Term Sheet nor the commitment defines which Schedule B, Part II exceptions the Bank accepts. The Draft Mortgage defines "Permitted Exceptions" by reference to Lender's written approval and attaches **Exhibit C**, which lists the six specific exceptions and reserves item 7 for such further matters as Lender may approve. **Action:** obtain Marcus's written approval of Exhibit C before closing, and confirm that the standard exceptions (a)–(e) are deleted by endorsement as the commitment contemplates.
>
> **(d) Future advances and mechanics' lien priority.** The Renovation Holdback is a future advance under a recorded mortgage. Section 3.4 of the Draft Mortgage contains the future-advance clause and a maximum principal amount of $14,750,000; the Term Sheet requires a future advance endorsement (Term Sheet §5.6). During construction, the Bank's priority over subsequently recorded mechanics' liens depends on the future-advance endorsement and on the draw mechanics (date-down endorsements, lien waivers, retainage) — see Section 8.5 below.
>
> **(e) Tax parcels and the escrow.** Three tax map numbers are identified, but the vacated Anson Lane strip has no separate tax map number in the record; it may be assessed within Lot 7 or separately. Term Sheet §6.1 requires the escrow to cover "all three tax parcels." **Action:** confirm from the tax certificates (Requirement 10) how the strip is assessed, and conform the escrow provision and Exhibit A accordingly.
