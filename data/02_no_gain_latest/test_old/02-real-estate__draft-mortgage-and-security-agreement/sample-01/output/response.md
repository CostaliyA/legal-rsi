# Deliverables

| File | Description |
|---|---|
| `mortgage-and-security-agreement.docx` | 70-page first draft of the South Carolina Mortgage and Security Agreement (with absolute assignment of leases, rents, issues and profits) from Palmetto Gateway Partners LLC to Calverley Heritage Bank, Loan No. 2025-CHS-0047, for 520–534 King Street, Charleston, SC. |
| `drafting-issues-memorandum.docx` | 31-page privileged issues memorandum from the drafting associate to the supervising partner, responding to the March 18 markup notes and cataloguing every cross-document inconsistency, recomputed figure and open item. |

## What the mortgage contains

Drafted to the executed Term Sheet of April 1, 2025 and the Title Commitment, organised as Articles 1–18 plus Exhibits A–E:

- **Granting clause** covering all three tax parcels and the vacated Anson Lane strip, with the full collateral schedule (fixtures, FF&E, accounts, proceeds, permits, contracts including the GC contract, leases and rents).
- **Article 5 — absolute and present assignment of rents** restyled from a collateral assignment, with a revocable licence to collect, enforcement on written notice to tenants, and the Lowcountry Provisions remediation covenant.
- **Article 7.4 — full single-purpose entity and separateness covenants**, including the independent-manager bankruptcy consent, and **7.5** direct *and* indirect/upstream transfer restrictions.
- **Article 7.6 + Exhibit E — specific SCDHEC land use restriction covenants** (no residential use of the Bay 1 ground floor; vapour barrier maintenance; no penetration without SCDHEC approval; annual certification) with a dedicated, uncurable Event of Default.
- **Article 10 — renovation holdback** of $2,250,000 against a $3,150,000 budget: draw conditions, AIA certifications, lien waivers, title date-downs, 10% retainage, equity-funding ratio test, June 15, 2026 substantial completion deadline.
- **Article 16 — prepayment** with an absolute 24-month lockout, a self-contained yield maintenance formula (greater of 1% or the present value of the interest differential, Treasury Rate defined and interpolated), and open prepayment in months 49–60.
- **Articles 12–13 — defaults and remedies**, stated expressly as judicial foreclosure only with no power of sale, plus receivership as of right.
- **Exhibits** — A legal description, B permitted exceptions, C budget and draw schedule, D rent roll and lease provisions, E land use restriction compliance protocol.

## Principal findings in the memorandum

The review recomputed 39 figures and identified 16 cross-document conflicts. The largest:

1. **The DSCR covenant cannot be met.** On the borrower's own stabilised projections, NOI of $622,772 supports 0.72x on interest-only debt service and 0.55x on amortising debt service against a 1.25x covenant tested from month 24 — the same month amortisation starts. A 1.25x test would support roughly a $6.5m loan.
2. **Occupancy is 56.13%, not 68%.** The Term Sheet and appraisal both use 21,400 occupied SF where the rent roll supports 17,400; the Term Sheet's own two occupancy statements contradict each other.
3. **Sources and uses do not balance** — loan plus equity equals project cost exactly, leaving at least $352,075 of closing costs and the $150,000 TI/LC reserve unfunded.
4. **The proposed yield maintenance formula produces a zero premium** for a partially amortising loan (no scheduled balloon at month 48), and dropping the 1% floor would conflict with the binding Term Sheet; placement of the 50 bps changes the premium by ~$212,000.
5. **The operating agreement does not support the SPE structure** — no independent manager, no separateness covenants, and bankruptcy is not a "Major Decision", so the 72% managing member could file the borrower unilaterally.
6. **Anson Lane derives from a quitclaim deed** with the Title Insurer expressly disclaiming that its chain matches Parcel One; affirmative coverage must be confirmed and endorsed.
7. **A ten-month guaranty gap** — the interest-shortfall guaranty ends at month 14, DSCR testing begins at month 24.

Every memorandum risk is tied to a numbered body issue (A-1 to H-6), and each to the specific mortgage provision that addresses it, with 19 open information requests, 20 recorded drafting decisions, and an arithmetic verification log.

## Verification performed

Figures were recomputed independently in Python (debt service, DSCR, LTV/LTC, occupancy, holdback allocations, draw schedule totals, mortgage recording tax, capital reserve, security deposits, balloon balance, prepayment illustrations). Internal cross-references were machine-checked across both documents. Both .docx files pass ECMA-376 schema validation, render without text overflow at the margins, and were proof-checked from a PDF render.
