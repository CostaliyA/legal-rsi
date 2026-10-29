# Deliverables

| File | Description | Length |
|---|---|---|
| `mortgage-and-security-agreement.docx` | Recordable South Carolina Mortgage and Security Agreement, with absolute assignment of rents, Article 9 security agreement, fixture filing, 13 Articles / 98 Sections, 6 Exhibits, witness and notarial execution blocks, guarantor limited joinder | ~24,200 words, 63 pp. |
| `drafting-issues-memorandum.docx` | Risk-prioritised issues memorandum: top-risk register, 30-issue log, independent recomputation worksheet, open items, closing-condition matrix, term-sheet traceability, drafting decisions, limitations | ~14,300 words, 30 pp. |

Both files pass `validate.py` (ZIP integrity, XML well-formedness, content-type and relationship consistency) and render correctly through LibreOffice to PDF.

# Approach

I inventoried and read all eight sources in full — executed term sheet, title commitment, appraisal, Phase I ESA, rent roll and lease abstracts (three worksheets), renovation budget and draw schedule (two worksheets), the redacted operating agreement summary, and prior counsel's markup notes — then built a source-to-issue log before drafting, and recomputed every amount, ratio, date interval and cross-reference rather than carrying any figure forward.

The instrument is drafted to the term sheet's commercial terms and incorporates the three structural instructions in the markup notes: the assignment of rents is **absolute** (not collateral) and brought inside the mortgage body, the SPE package is enforceable rather than merely recited, and the yield maintenance formula is self-contained and mathematically determinable. It also responds to the title commitment's *instructions to closer*, which materially extend the environmental covenants.

# The findings that drove the draft

Four matters go beyond ordinary customisation and are flagged as critical:

1. **The loan cannot satisfy its own financial covenant.** On the borrower's own rent roll projections, best-case stabilised DSCR is 0.554x and the realistic figure at the first test date is 0.280x, against a required 1.25x. A 1.25x DSCR needs NOI of $1,405,299 — 2.26× the best-case projection. The covenant is effectively a scheduled default.
2. **The appraisal's income approach does not support its own values.** Stated NOI of $332k–$345k at 6.25% yields $5.3–5.5m, not $18.2m (implied cap 1.82%); stabilised NOI of $582k–$592k at 5.85% yields $9.9–10.1m, not $23.5m (implied cap 2.48%). The 81.04% as-is LTV rests on sales comparison alone.
3. **Occupancy is 56.13%, not 68%.** The term sheet is internally contradictory (it states 43.9% vacancy three lines later); the appraisal's "21,400 SF occupied + 13,600 SF vacant" totals 35,000 SF in a 31,000 SF building, and its $19.40 average rent inherits that error. The draft represents the correct figure on the face of the instrument.
4. **The operating agreement cannot support a non-recourse loan** — no independent manager, no separateness covenants, no single-purpose restriction, no lender consent to dissolution or amendment, and a 75% Major Decisions threshold that a 72% managing member cannot meet alone.

Eleven issues are rated high, including the Anson Lane quitclaim parcel (rear access and parking the leases depend on), the SCDHEC land use restriction (where prior counsel's instruction that "standard provisions should suffice" conflicts with Title Requirement 6, which requires specific covenants *and* a dedicated Event of Default), the yield maintenance formula (the markup's substitute omits the term sheet's 1% floor), and a 14-month interest shortfall guaranty that expires four months before the DSCR test it protects.

The recomputation worksheet also catches arithmetic defects in the borrower's materials — the draw schedule over-draws equity by $5,000 ($3,155,000 against a $3,150,000 budget), misallocates $50,000 between the HVAC and elevator lines, and ignores the 10% retainage the term sheet requires.

# Deliberate drafting positions

Where sources conflicted, the draft follows the binding term sheet and the conflict is recorded rather than smoothed over — the yield maintenance 1% floor is preserved; the net worth covenant is drafted on the Borrower as §7.2 allocates it, with the conflicting reading flagged for instruction; LUR breaches carry a cure period (30 days extendable to 180 where SCDHEC action is needed) because an uncurable default invites a foreclosure defence, while conversion to residential use remains an immediate default.

Six items could not be resolved from the record and are expressly flagged rather than invented: the metes and bounds description (record description plus survey reference used), the full unredacted operating agreement, the construction contract, the leases themselves (only abstracts available), the Guarantor's financial statement, and the Harborline ownership chain.
