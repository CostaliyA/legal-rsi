# Pinnacle Savings Bank / Harborview Capital Partners — CRE-2025-0342

## Deliverables

| File | What it is |
|---|---|
| `loan-agreement-draft.docx` | First draft, Construction-to-Mini-Permanent Loan Agreement (76 pp.) — 18 Articles, 10 Exhibits, 35 bracketed drafting notes keyed to the cover memo |
| `cover-memorandum.docx` | Cover memorandum to the partner (58 pp.) — document inventory, executive summary, 44-item severity-ranked issue register with recommendations, 8 reconciliation schedules, open-items closing checklist |

## How the work was done

1. **Inventory and full read.** All seven source documents were read in full (term sheet, credit memorandum, appraisal, title commitment, Phase I ESA, org chart, draw/detail schedule). Nothing was relied on as a summary except where the record itself furnishes only excerpts (Phase I ESA, appraisal, org chart, operating agreement) — those limits are flagged in memo § 1.3 and Issue 44.
2. **Independent recomputation.** Every material computation was re-performed from source components rather than accepted: sources and uses; LTC (83.7743%); as-completed and as-stabilized LTV (65.2473% / 62.3360%); DSCR at 7.85% (1.3079x) and the +200 bp stress (1.0423x); the interest reserve accrual month by month ($4,628,675 at 6.75%; implied average balance $27,429,185); the draw schedule footings (found a $1,000,000 gap in Draw 9); the detailed budget column totals (found a $725,000 overstatement); retainage (10% = $3,475,000 vs. $3,275,000 released); guaranty percentages; acreage and frontage from the metes and bounds; HVCRE contributed capital; combined senior + mezzanine coverage (0.93x); and each date interval.
3. **Drafting from the verified issue log,** with defined terms used consistently and each open point bracketed and cross-referred to its issue number.

## Principal findings (all in memo § 3 and § 5)

- **No borrower equity.** The sources and uses allocates 100% of the $56.7M to the two loans with $0 equity, and the detailed budget shows the $8.2M land cost funded by *mezzanine proceeds* — irreconcilable with the term sheet (member capital calls) and the org chart (Vasquez-Torres personal funds). The credit memo credits the same $8.2M as "land equity" in its equity and HVCRE analyses, counting it twice (Issue 5).
- **Two leverage breaches, and the prescribed cure does not work.** LTC 83.77% > 80%; as-completed LTV 65.25% > the term sheet's 65% (the credit memo measures against a 70% policy limit and reports a pass). A $2.14M equity escrow alone leaves the loan at $47.5M and creates a $2.14M surplus of sources over uses — it must be paired with a reduction to $45,360,000 (Issues 1–3).
- **Interest reserve inadequacy, measured three different ways** in the record (+$221,325 / −$365,830 / −$565,000). Correct figure on the draw schedule's own pattern at 4.35% SOFR: ≈$361,500 short. The credit memo's average-balance method overstates by ≈$199,500 (Issues 9–10).
- **Environmental record defective:** the NFA deed notice (due 29 Nov 2024) is not shown on the title commitment but is said by the appraisal to be recorded; the scope of the residential use restriction is expressly *unverified* in the Phase I (the "14 units" appears to be the three-bedroom count); Phase II report, NFA letter and Phase II reliance letter are absent (Issues 21–27).
- **Completion is guaranteed three days before it is projected** (28 Aug vs 31 Aug 2027), with Draw 9 falling after maturity and no schedule float (Issue 28).
- **Borrower's $14.2M net worth cannot be reconciled** to the only balance sheet in the record (≈$4.8M), and the $12M covenant would fail at closing (Issue 31).
- **Governance:** the operating agreement's 75% supermajority (62% + 10% = 72%) gives the mezzanine lender's affiliate a veto over the loan, the membership pledge, the SPE amendment and any take-out (Issues 37–39).

## Validation

Both files passed `validate.py` (ZIP integrity, XML well-formedness, ECMA-376 schema, content-type registration, relationship consistency) and were rendered to PDF and reviewed page by page for table fitting, page breaks, orphaned headings and cross-references. Every internal section reference and every "Cover Memorandum, Issue N" reference in the loan agreement resolves to an existing provision or issue, and each of the six "critical" conditions in the credit memo has an operative provision (not merely a recital).
