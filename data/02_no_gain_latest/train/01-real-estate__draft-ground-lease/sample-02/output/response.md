# Ground Lease + Drafting Issues Memo — Meridian Gateway Holdings LLC (Tenant)

## Deliverables

| File | What it is | Length |
|---|---|---|
| `ground-lease-agreement.docx` | First-draft 99-year ground lease for 10–30 Pier Street, Port Calloway, CT — 20 Articles, 7 Exhibits, signature and notarial pages, Tenant-side but negotiable, with every departure from the Term Sheet flagged in-text | 69 pp. / ~32,200 words |
| `drafting-issues-memo.docx` | Privileged issues memorandum: source inventory, recomputation of every figure, cross-document conflict register, Bayside gap analysis, issue-by-issue analysis (reverter first), legal research register, missing-document list, deviation schedule, negotiation strategy, timeline, 4 appendices | 33 pp. / ~19,100 words |

Both are validated against the ECMA-376 XSDs (`skills/docx/scripts/validate.py`, exit 0) and render cleanly through LibreOffice.

## What was done

**Inventory and full read** of all seven sources (client instructions email, executed Term Sheet, Bayside loan term sheet, Title Commitment TC-2025-07821, Phase II ESA summary, ALTA/NSPS survey narrative, Board Resolution 2025-047), with a proposition-by-proposition source-to-issue log (memo Appendix 1) and figure register (Appendix 3).

**Independent recomputation** of every number rather than adopting the documents' arithmetic: rent, escalations, security deposit, remediation credit waterfall, tax tiers, capital stack, milestone dates, ROFR and expiration dates. Most figures check out; two rounding variances in the rent schedule ($13 and $41 p.a.) and two mislabelled "10%" contingencies in the Phase II cost tables (actually 5.71% and 4.76%) were found — the latter understates Tenant's remediation share by $102,500 if 10% is intended.

**Two traverses run on the competing legal descriptions.** The Title Commitment's Exhibit A miscloses by 1.10 ft and encloses ~279,535 SF (6.42 ac) against its own recited 3.2 ac — 2.01× the Premises, and it encroaches on the retained park parcel. The survey description closes exactly at 139,475 SF. The lease uses the survey description and makes a conformed title commitment a condition precedent.

**24-row cross-document conflict register** (memo Part 4.1), including: three different AMI geographies; three different start dates for the tax abatement/percentage rent; "automatic termination" (Term Sheet §9) versus "no termination until lender cure expires" (Bayside §5.4); the mechanics' lien treated as a Permitted Exception that the title company will not insure; and a recorded 2019 ROFR with no mortgagee carve-out.

**Bayside §5 gap analysis**: none of the seven required ground lease provisions is satisfied in full by the Term Sheet — four are not addressed at all (including all lender cure periods and bankruptcy protections), three only in part. The lease's Article 9 is drafted to meet or exceed each.

**The reverter** is handled as instructed: retained but converted into a sequenced, compensated remedy (notice → 180-day tenant cure → 180-day lender cure → 30-day election → deemed waiver), with an Improvement Payment equal to the greater of appraised value or unreimbursed hard costs, net of recoveries and capped Documented Damages, plus a first lien on the improvements until paid, and reverter subordination to the leasehold mortgage. The legal basis is stated carefully: the penalty/forfeiture principles are set out at the level of restated general doctrine, the client's "Stamford project" recollection could not be confirmed, and no Connecticut case is cited — the memo expressly says why an unenforceability argument is not a financing strategy.

**Percentage rent** is quantified: with the Breakpoint fixed at $28,500,000, it decays from 8.84× Base Rent in Year 6 to 0.96× by Year 96 ($2.73M in Year-1 dollars, below today's rent), and the ten-year resets produce 28% single-year steps. The lease indexes the Breakpoint to Base Rent and tightly defines Gross Revenues with 15 exclusions.

## Points requiring client attention

Five dollar amounts are intentionally left as `$[●]` (extension fee, environmental indemnity cap, LOC issuer capital, transferee net worth, alteration threshold) and are itemised in memo Part 11; 25 deviations from the Term Sheet are scheduled in Part 9 because each requires Board action under Resolution 2025-047 §4(d).
