# The Piedmont at Brightleaf — Loan No. CRE-2025-0342

Two deliverables were produced from the seven source documents in `documents/`:

| File | Description | Length |
|---|---|---|
| `loan-agreement-draft.docx` | Full construction-to-mini-permanent Loan Agreement (22 articles, 8 schedules, 4 exhibits) drafted to the executed Term Sheet and conformed where the record required | 78 pages |
| `cover-memorandum.docx` | Cover memorandum from Lender's counsel to the SVP / Senior Loan Committee: 47 numbered issues with sources, recomputation, impact and recommended resolution, plus recomputation schedule, closing checklist and source-to-issue log | 37 pages |

Both were validated with `skills/docx/scripts/validate.py` (schema-clean, no dangling relationships) and rendered to PDF to confirm 0 words extend past the right margin.

## Loan agreement

Drafted as a complete instrument, not an outline: definitions (120+), interest and SOFR mechanics with ARRC benchmark replacement, 26 closing conditions, 16 conditions to each advance, disbursement/retainage/interest-reserve machinery, representations, affirmative and negative covenants, financial covenants with testing mechanics, environmental covenants keyed to the NCDEQ NFA Letter, single-purpose-entity covenants, insurance, collateral and title, guaranties and recourse carve-outs, events of default, remedies (North Carolina power of sale), indemnities, intercreditor provisions, notices, boilerplate and a fully specified extension option. Schedules include a **restated draw schedule** that withholds the 10% retainage correctly, and a **conformed Permitted Exceptions schedule**. 31 flagged Drafting Notes cross-reference the memorandum. Brackets are used only where a Senior Loan Committee decision or a missing document is required.

## The findings that drive the draft

1. **The loan cannot satisfy its own credit tests.** $47.5M ÷ $56.7M = 83.77% LTC (cap 80%) and $47.5M ÷ $72.8M = 65.25% LTV (cap 65%). The credit memo records both figures but passes the LTV by measuring it against a 70% maximum found nowhere in the term sheet. The memo's proposed $2,140,000 equity escrow *does not cure either ratio* — an escrow is neither a reduction of the loan nor an increase in cost. The only arithmetic cure is a commitment reduction to $45,360,000 (or costs of $59,375,000), which the draft implements as an automatic Closing Date reduction.
2. **There is no equity, and the land is not equity.** The Borrower's own detailed budget funds the $8,200,000 land cost and $1,000,000 of developer fee with mezzanine proceeds, so senior plus mezzanine debt equals 100% of project cost. This contradicts the term sheet and the credit memo, which count the land as an $8.2M equity contribution.
3. **The $12M Borrower net worth covenant cannot be met after closing** (book equity ≈ 0 once $56.7M of debt funds $56.7M of cost), and the stated $14.2M net worth cannot be reconciled to the $8.2M of documented contributions.
4. **Environmental:** the NFA Letter restricts 0.38 acres to non-residential use while the plans place 14 units above it (DSCR 1.31x falls to 1.21x), and the deed notice due November 29, 2024 does not appear on the December 5, 2024 title commitment — although the appraisal asserts it is recorded.
5. **Title:** an unreleased 2018 Triangle Commercial Bank deed of trust ($3.4M original, balance unknown) has no budget line and no cash to pay it; August/September 2024 demolition and remediation work may prime the Bank's deed of trust under N.C.G.S. § 44A-10; the appraisal says the historic-district ARC approved the design, the title officer says there is no evidence of it.
6. **Control:** both loans claim a first-priority 100% membership pledge (intercreditor unexecuted), and the operating agreement's 75% supermajority gives the mezzanine lender's affiliate a veto over bankruptcy because 62% + 10% = 72%.
7. **The draw schedule over-advances $3,475,000** (each hard-cost draw funded at 100% with no retainage withheld, then a second "release"), contains four footing errors, and hides the developer fee and contingency inside the retainage line — the term sheet's Draw 9 of $3,275,000 is exactly $1,835,000 + $1,440,000.
8. **Timing and coverage:** construction maturity (Aug. 28, 2027) precedes projected substantial completion (Aug. 31, 2027); the DSCR test as written cannot be performed at mini-perm commencement; builder's risk of $34.75M against a $56.7M–$72.8M replacement cost is underinsurance; the interest reserve is short $366,000–$565,000 at current SOFR (the Borrower's "adequate" conclusion assumes a rate 85 bp below the memo's).

Every figure in both documents was recomputed from source inputs rather than adopted from the summaries. The memorandum's Tables 3 and Appendix A record each computation and each proposition-to-source citation, and Section 5 assigns every recommendation an owner and a deadline.
