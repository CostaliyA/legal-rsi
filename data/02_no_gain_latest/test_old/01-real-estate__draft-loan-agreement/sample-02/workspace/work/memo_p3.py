# -*- coding: utf-8 -*-
import sys; sys.path.insert(0,'/workspace/work')
from dh import *
from memo_p2 import issue
from docx.enum.text import WD_ALIGN_PARAGRAPH as AL

def build_p3(doc):
    sub_h(doc, "C.  Credit metrics, reserve and coverage")
    issue(doc, "12", "The interest reserve adequacy conclusion differs across three documents, and the reserve is adequate only below a 3.82% SOFR", "H",
      "Borrower Draw Schedule, \u201cInterest Reserve Adequacy Analysis\u201d tab (month-by-month model at an assumed SOFR of 3.50%; "
      "projected interest of $4,628,675 against $4,850,000 \u2192 surplus $221,325; conclusion \u201cAPPEARS ADEQUATE\u201d; the "
      "schedule's own sensitivity table shows a shortfall of $365,830 at a 4.35% SOFR). Credit Memorandum \u00a7 6.2 (SOFR of 4.35%; "
      "average outstanding balance estimated at approximately $28,500,000; projected interest of $5,415,000; shortfall approximately "
      "$565,000; \u00a7 9.2 \u201capproximately $565,000\u201d shortfall). Term Sheet \u00a7 10 (reserve of $4,850,000; Borrower to "
      "fund shortfalls within five business days).",
      "We rebuilt Borrower's month-by-month model independently (draw dates as scheduled, interest on the daily balance at "
      "SOFR + 3.25%, accrued monthly at one-twelfth of the annual all-in rate) and reproduced its result at 3.50% ($4,628,672 against the "
      "$4,628,675 shown), which confirms that the model is internally correct but rate-sensitive. Running the same model across "
      "rates: 3.50% \u2192 $4,628,672 (surplus $221,328); 4.00% \u2192 $4,971,536 (shortfall $121,536); 4.35% \u2192 $5,211,542 "
      "(shortfall $361,542); 4.75% \u2192 $5,485,833 (shortfall $635,833); 5.25% \u2192 $5,828,698 (shortfall $978,698); 5.35% \u2192 "
      "$5,897,271 (shortfall $1,047,271). Solving for the breakeven, the $4,850,000 reserve covers construction-period interest only "
      "if SOFR averages 3.82% or less (all-in 7.07%). The Credit Memorandum's own market assumption is 4.35%. The Credit Memorandum's "
      "$565,000 figure and Borrower's $365,830 figure also differ from each other because they use different methods (average "
      "balance versus month-by-month draw modelling); the month-by-month figure is the more reliable of the two and is approximately "
      "$361,000 at 4.35%. The loan accrues interest on an actual/360 basis, so an actual day-count would increase every projection "
      "by approximately 1.4% (approximately $72,000 at a 4.35% SOFR), widening each shortfall; the conclusions are unaffected.",
      "On the Bank's own rate assumption the reserve is exhausted before construction is complete, and Borrower \u2014 which is "
      "contributing no verified cash equity (Issue 1) \u2014 must fund the shortfall or the Loan goes into payment default during "
      "construction. The credit file contains two contradictory conclusions (\u201cAPPEARS ADEQUATE\u201d in Borrower's schedule; a "
      "$565,000 shortfall in the Credit Memorandum) that cannot both stand in a file presented to examiners.",
      "Either increase the reserve to reflect current rates with a cushion (approximately $5,800,000 at 4.35% plus 100 basis points) or "
      "retain $4,850,000 and rely on a combination of (a) the mandatory replenishment obligation (section 5.3), (b) the "
      "adequacy test at each draw (section 5.4), (c) the Carry Guaranty (section 11.2), and (d) an explicit Committee "
      "acknowledgement, recorded in the credit file, that a call on the Guarantors is probable rather than theoretical. Correct "
      "Borrower's schedule so that it does not state a conclusion the sensitivity analysis contradicts.",
      "Sections 5.3\u20135.6 (replenishment, adequacy testing, monthly reconciliation, and Borrower's acknowledgement of the "
      "shortfall); section 11.2 (Carry Guaranty); Schedule 6, Part A.")

    issue(doc, "13", "Stabilized coverage is thin on a combined basis, and the DSCR testing dates and periods are internally inconsistent", "H",
      "Term Sheet \u00a7 6.3 (minimum projected stabilized DSCR of 1.25x \u201cbased on interest-only debt service during the Mini-Perm "
      "Period\u201d; \u201ctested at the commencement of the Mini-Perm Period and annually thereafter based on actual trailing "
      "twelve-month net operating income\u201d) and \u00a7 4 (DSCR of 1.31x at a 7.85% all-in rate). Credit Memorandum \u00a7 6.1 "
      "(1.31x; stress test 1.04x at +200 basis points) and \u00a7 11(d) (extension test: trailing three-month annualized in-place NOI "
      "at 1.15x). Appraisal \u00a7 6.3 (stabilization not projected until approximately May 2028). Term Sheet \u00a7 2 and section "
      "3.1 of the Credit Memorandum (projected substantial completion August 31, 2027).",
      "The 1.31x figure is arithmetic: $4,876,800 \u00f7 ($47,500,000 \u00d7 7.85% = $3,728,750) = 1.308. But it is senior-only, "
      "interest-only and excludes the mezzanine. Adding the Mezzanine Loan at its stated fixed 12.50% ($9,200,000 \u00d7 12.50% = "
      "$1,150,000) produces combined debt service of $4,878,750 against NOI of $4,876,800 \u2014 coverage of 1.00x. Because the "
      "mezzanine is stated to accrue interest and be paid in kind during construction (Credit Memorandum \u00a7 4.4), the accrued "
      "balance grows by approximately $2,875,000 over the 30-month construction period and approximately $4,025,000 by the mini-perm "
      "maturity date, at which point total debt is approximately $60,725,000 (79.7% of the as-stabilized value) and cash coverage, if "
      "the mezzanine converts to cash pay as contemplated, falls below 1.00x ($4,876,800 \u00f7 ($3,728,750 + $1,650,000) = 0.91x). "
      "Separately, the test mechanics do not work: a trailing twelve-month actual NOI test at the commencement of the Mini-Perm "
      "Period cannot be satisfied when Substantial Completion is projected for August 31, 2027 \u2014 three days after the "
      "Construction Maturity Date of August 28, 2027 \u2014 and stabilization is not projected until approximately May 2028. The "
      "covenant would fail arithmetically on the day it is first tested, and the cure (curtailment or cash collateral under Term "
      "Sheet \u00a7 6.3) requires cash that the structure does not have. The extension test uses a different metric and a different "
      "threshold (three-month annualized at 1.15x) from the covenant (twelve-month at 1.25x).",
      "On any realistic stress the Project cannot service its aggregate debt from operations, so repayment depends on a refinancing "
      "or a sale. A covenant that fails at first test is not a control; it is a forbearance negotiation in waiting.",
      "Conform the testing mechanics: test at mini-perm commencement on annualized in-place NOI (or on the Appraiser's projected NOI "
      "until twelve months of operating history exists), then move to trailing twelve months once available; align the extension "
      "test with the covenant or state expressly why it differs. Add a combined-debt-service coverage measure as a covenant or, at "
      "minimum, as a reporting metric. Require an interest rate cap at conversion to the Mini-Perm Period (not only at extension) "
      "given that a 200 basis point move takes senior coverage to 1.04x. Require evidence of a take-out strategy (section 17.4 of the "
      "draft).",
      "Section 9.3(a)\u2013(c); section 2.14(e)\u2013(g) (extension conditions, including the cap); section 17.4 (take-out "
      "reporting); Schedule 6, Part A.")

    sub_h(doc, "D.  Guarantors, structure and parties")
    issue(doc, "14", "Borrower net worth and guarantor liquidity are unsupported by the Record, and the net worth covenant is likely to fail at closing", "M",
      "Term Sheet \u00a7 6.4 and \u00a7 6.5 (Borrower net worth of $12,000,000 tested annually; combined guarantor liquidity of "
      "$5,000,000 tested quarterly); \u00a7 15 (Events of Default: \u201cAny Guarantor's net worth falls below the minimum threshold "
      "set forth in Section 6.4\u201d). Credit Memorandum \u00a7 2.1 and \u00a7 2.3 (Borrower net worth approximately $14,200,000; "
      "guarantor liquidity $6,100,000 and $3,200,000 from personal financial statements dated December 15 and 18, 2024; \u00a7 2.3.3 "
      "notes that Mr. Osei's $11,875,000 guaranty exposure equals approximately 103.3% of his net worth). Organizational Materials "
      "\u00a7 1.1 and \u00a7 1.3 (net worth approximately $14,200,000 \u201cbased on the book value of its assets and liabilities\u201d; "
      "member capital contributions to date of $8,200,000, consisting solely of the land contribution).",
      "No financial statement for Borrower or either Guarantor is in the Record, so every net worth and liquidity figure is a "
      "summary assertion. More importantly, the $14,200,000 Borrower net worth is difficult to reconcile with a single-purpose "
      "entity that owns only the Property: land at a cost basis of $8,200,000, subject to the $3,400,000 Triangle deed of trust, "
      "plus capitalized site costs of approximately $680,000, produces net assets of approximately $5,480,000; if the mezzanine loan "
      "has been drawn to pay for the land (Issue 1), the entity holds cash of $9,200,000 against debt of $12,600,000 and net worth is "
      "approximately $4,800,000. Either way the figure is closer to $5,000,000 than to $14,200,000, and a $12,000,000 covenant "
      "tested at closing would fail. Note also the cross-reference defect in Term Sheet \u00a7 15, which treats section 6.4 (a "
      "Borrower covenant) as a Guarantor test \u2014 the Term Sheet contains no guarantor net worth covenant at all.",
      "A covenant that is breached at closing is a waiver request on day one, and the credit committee's stated cushion "
      "($2,200,000 above the minimum, per Credit Memorandum \u00a7 2.1) may not exist. Guarantor support may likewise be overstated if "
      "the liquid asset figures cannot be verified, and the personal financial statements will be approximately two and a half "
      "months old at closing, before any equity contribution of approximately $4,080,000 (Issue 3).",
      "Obtain Borrower's interim balance sheet as of a date within 30 days of closing, with a schedule reconciling to the $14,200,000 "
      "representation, and a written net worth computation applying the definition in section 9.4(c) of the draft. If the computed "
      "figure is below $12,000,000, either reset the covenant to the computed level with a step-up at stabilization, or require an "
      "additional capital contribution. Obtain bring-down personal financial statements dated within 30 days of closing and "
      "verification of each liquid account. If a guarantor net worth covenant is intended, add it (the draft leaves the point open).",
      "Section 9.4(a)\u2013(c) (net worth, including a GAAP definition that excludes capitalized interest and unrealized "
      "appreciation, and a closing test); section 9.5 (liquidity); section 3.16 (financial information conditions); section "
      "13.13 (Guarantor default).")

    issue(doc, "15", "Borrower is not yet a compliant single-purpose entity, the 28% member holds an effective veto, and its affiliate is the mezzanine lender", "M",
      "Organizational Materials \u00a7 1.1 (\u201cthe Amended and Restated Operating Agreement \u2026 does not currently include "
      "provisions for an independent director or independent manager, nor does it contain separateness covenants\u201d); \u00a7 2.2 "
      "(Operating Agreement \u00a7\u00a7 3.1\u20133.2: major decisions, including any financing over $1,000,000, require 75% approval, "
      "which Ms. Vasquez-Torres (62%) and Mr. Osei (10%) cannot reach at 72%, giving Brightleaf Investors Group LLC an effective "
      "veto; \u00a7 9.1: a pledge of a membership interest requires the Managing Member's written consent); \u00a7 1.2 (Thomas R. Chen "
      "is the managing member of both Brightleaf Investors Group LLC (28% member) and Brightleaf Mezzanine Capital LLC (mezzanine "
      "lender)). Credit Memorandum \u00a7 9.3 and \u00a7 10.1(4) (SPE covenants, independent manager and non-consolidation opinion as "
      "conditions). Term Sheet \u00a7 20 (SPE requirements, including the potential appointment of an independent manager).",
      "The three structural protections the Credit Memorandum relies on \u2014 separateness covenants, an independent manager and a "
      "non-consolidation opinion \u2014 do not exist today and have to be created by amendment before closing. The governance "
      "arithmetic matters practically as well as theoretically: because the loan and the pledges require 75% member approval, "
      "Brightleaf Investors Group LLC's written consent is a closing deliverable, and the same entity is affiliated with the lender "
      "whose pledge must be subordinated (Issue 17). That gives an affiliated party two points of leverage over the closing. The "
      "independent manager requirement is also the single most effective protection against a voluntary bankruptcy filing, which is "
      "a recourse trigger under section 11.4.",
      "Without the amendments, the Bank has no separateness protection, and the Borrower cannot deliver the consents it has "
      "promised; with the amendments but without the affiliated member's consent, the pledges are ineffective under \u00a7 9.1 of "
      "the Operating Agreement.",
      "Require, as conditions precedent: (a) a member-approved amendment adding the SPE covenants and an independent manager with a "
      "bankruptcy-consent right; (b) the Managing Member's written consent to each pledge under \u00a7 9.1; (c) the 75% member consent "
      "to the financing and the security interests; (d) a non-consolidation opinion from Borrower's counsel; and (e) an annual "
      "independent-manager certificate. Confirm that the independent manager is unaffiliated with Mr. Chen. Consider also requiring "
      "the independent manager's consent right to be documented in a side letter for the Bank's benefit.",
      "Section 3.9 (amendments, consents and non-consolidation opinion); Article XV (SPE covenants, including the independent "
      "manager); section 13.9 (SPE breach as an Event of Default); section 11.4 (SPE breach as a recourse trigger).")

    issue(doc, "16", "The partial repayment guaranty is described inconsistently, and the environmental indemnity parties differ between documents", "M",
      "Term Sheet \u00a7 7.3 (\u201ca partial repayment guaranty \u2026 in the amount of 25% of the Loan Amount (25% \u00d7 "
      "$47,500,000 = $11,875,000) \u2026 joint and several, meaning that each Guarantor shall be individually liable for the full "
      "guaranteed amount\u201d) and \u00a7 7.4 (Environmental Indemnity to be executed by \u201ceach Guarantor\u201d). Credit Memorandum "
      "\u00a7 4.3 (\u201ceach guarantor will provide a 25% partial repayment guaranty \u2014 $11,875,000 per guarantor \u2026 a payment "
      "guaranty obligating each guarantor to pay \u2026 up to $11,875,000 in the event of a payment default or other event of "
      "default\u201d) and \u00a7 8.2 (environmental indemnity from \u201cboth the Borrower and the Guarantors\u201d).",
      "The two descriptions produce materially different liabilities. Under the Term Sheet, $11,875,000 is the aggregate cap on a "
      "guaranty that is joint and several, so the Bank's total recovery from both Guarantors is $11,875,000. The Credit Memorandum's "
      "\u201cper guarantor\u201d formulation implies $23,750,000 in the aggregate and, separately, describes a payment guaranty "
      "triggered by any default rather than a limited 25% recourse obligation with bad-boy carve-outs to full recourse. Those are "
      "different products with different pricing. On the environmental indemnity, the Term Sheet names only the Guarantors while the "
      "Credit Memorandum names Borrower and Guarantors \u2014 the latter is correct for a construction loan where the Borrower is the "
      "owner and operator.",
      "An ambiguity in a guaranty invites litigation precisely when the Bank needs it most, and a guaranty that overstates the "
      "obtainable recovery (two times the intended amount) distorts the credit analysis in the file used to approve the loan.",
      "Fix the aggregate cap at $11,875,000 with express language that collections reduce the aggregate dollar for dollar, and "
      "specify whether the obligation is a 25% recourse guaranty with bad-boy conversion or a full payment guaranty in that amount; we "
      "recommend the former, consistent with the Term Sheet. Confirm the environmental indemnity runs from Borrower and each "
      "Guarantor and is unlimited and survives foreclosure. Update the credit file to conform to whichever structure is approved.",
      "Section 11.3(a)\u2013(c) (aggregate cap of $11,875,000, credit for recoveries, and the fair-value adjustment); section 11.4 "
      "(recourse carve-outs); section 11.5 (Borrower and Guarantors).")

    issue(doc, "17", "Mezzanine terms are incomplete: pay-in-kind interest is undisclosed in the Term Sheet, the pledge priority is contested, and the mezzanine lender is an affiliate of a 28% member", "M",
      "Term Sheet \u00a7 1.4 (mezzanine loan of $9,200,000 at 12.50% fixed, secured by a pledge of 100% of the membership interests, "
      "maturity coterminous with the senior loan \u201cincluding any extension period\u201d; intercreditor agreement \u201ccurrently under "
      "negotiation and must be executed prior to or simultaneously with the closing\u201d) and \u00a7 8 (senior collateral includes "
      "\u201cPledge of 100% of membership interests in the Borrower by all members\u201d). Credit Memorandum \u00a7 4.2 and \u00a7 9.4 "
      "(both loans secured by a pledge of 100% of the membership interests; \u201cmutually exclusive as first-priority security "
      "interests\u201d) and \u00a7 4.4 (mezzanine payments: \u201cInterest accrues and is paid-in-kind during construction; cash pay "
      "during mini-perm\u201d). Organizational Materials \u00a7 2.5 (Operating Agreement contains no mechanism to resolve competing "
      "pledges) and \u00a7 1.2 (common control by Thomas R. Chen).",
      "Two problems. First, the Term Sheet and the Credit Memorandum each promise the senior lender a first-priority pledge of 100% "
      "of the membership interests while acknowledging that the mezzanine lender holds a pledge of the same 100%; the only resolution "
      "is subordination in an intercreditor agreement that has not been executed and, so far as the Record shows, has not been "
      "drafted. Second, and less visibly, the Credit Memorandum discloses that mezzanine interest is paid in kind during construction, "
      "but the Term Sheet does not, and nothing in the Record caps the accrual, requires reporting of it, or includes it in any "
      "leverage calculation. On the stated terms, $9,200,000 at 12.50% accrues approximately $2,875,000 of interest over the "
      "30-month construction period and approximately $4,025,000 by the mini-perm maturity date, taking aggregate debt to "
      "approximately $60,725,000, or 79.7% of the as-stabilized value, with combined coverage below 1.00x if cash pay begins.",
      "Without the intercreditor agreement the Bank's collateral position is undefined, which the Credit Memorandum itself treats as "
      "a closing failure; and leverage grows during construction in a way that the approval documents do not reflect, eroding the "
      "only cushion (the land) that the file relies on.",
      "Obtain the mezzanine term sheet or loan agreement and the draft intercreditor agreement now. Require the intercreditor "
      "agreement to address: senior first-priority pledge; a standstill of at least 90 days; notice and cure rights; a purchase "
      "option at par plus the Exit Fee; prohibition on modification, on prepayment and on any payment while a senior default exists; "
      "PIK accrual reporting and a cap; coterminous extension mechanics; and an express acknowledgement of the common control. Add "
      "the accrued mezzanine balance to the leverage reported to the Committee and to the loan-to-value covenant calculation.",
      "Section 3.8 (intercreditor conditions, including the PIK and payment-block provisions); sections 8.13 and 13.10 (mezzanine "
      "modifications and cross-default); section 10.6 (pledges); section 9.3(c) (combined coverage disclosure).")

    sub_h(doc, "E.  Insurance, documentation and legal points")
    issue(doc, "18", "The insurance program covers construction only, and the flood zone data conflict", "M",
      "Term Sheet \u00a7 19 and Credit Memorandum \u00a7 8.1 (builder's risk of not less than $34,750,000; commercial general liability "
      "$5,000,000/$10,000,000; umbrella $10,000,000; workers' compensation; flood insurance \u201cif the Property is determined to be "
      "located in a FEMA-designated Special Flood Hazard Area\u201d). Borrower Draw Schedule line 3.09 (builder's risk $210,000). "
      "Appraisal \u00a7 2 (Zone X on FIRM panel 3710406400J, effective May 2, 2019). Phase I ESA \u00a7 2.3 (Zone X on FIRM panel "
      "3720098700J, effective March 2, 2009). Credit Memorandum \u00a7 8.1 (architect's professional liability of $2,000,000).",
      "Every insurance requirement in the Record addresses the Construction Period. None specifies property insurance at full "
      "replacement value for the twelve-month Mini-Perm Period (during which the completed building \u2014 approximately "
      "$72,800,000 of as-completed value \u2014 will be occupied and income-producing), rent loss or business income coverage, "
      "equipment breakdown, or the professional liability coverage the Credit Memorandum requires of the architect. Builder's risk at "
      "$34,750,000 is appropriate for construction but is roughly half the replacement value of the finished asset. The two flood "
      "determinations also cite different FIRM panels and effective dates, so a current determination from a recognized service is "
      "needed before closing.",
      "A casualty during the Mini-Perm Period would leave the Bank with collateral worth substantially more than the insurance "
      "proceeds, and no rent loss coverage with which to pay debt service while the building is restored.",
      "Amend the insurance schedule to require, from Substantial Completion: special-form property insurance at full replacement cost "
      "with an agreed-amount endorsement; rent loss of at least twelve months including debt service; equipment breakdown; flood "
      "coverage if applicable under a current determination; and architect's professional liability of $2,000,000. Obtain a current "
      "flood zone determination before closing and reconcile the two FIRM references in the Record.",
      "Section 16.1 and 16.2 (construction and mini-perm coverage); section 16.5 (flood determination); Schedule 5.")

    issue(doc, "19", "Document-level inconsistencies and drafting points carried forward from the Term Sheet", "L",
      "Term Sheet \u00a7 3.1 (\u201cstructured as a single advance facility, with loan proceeds to be disbursed in accordance with the "
      "approved draw schedule\u201d) against \u00a7 9.2 (nine draws); \u00a7 15, final bullet (Guarantor net worth keyed to \u00a7 6.4, "
      "which is a Borrower covenant); \u00a7 3.2 (extension \u201csubject to satisfaction of customary conditions to be determined "
      "and set forth in the definitive Loan Agreement\u201d, with no conditions stated) against Credit Memorandum \u00a7 11 (ten "
      "specific conditions); \u00a7 3.4 (unused line fee on the \u201caverage daily undrawn commitment amount\u201d) against a fully "
      "committed construction facility for which the undrawn portion is already reserved for identified uses; \u00a7 22 (expense "
      "deposit of $75,000 applied to the Lender's costs) against Borrower Draw Schedule line 3.04 ($310,000 of Lender's counsel and "
      "title costs funded from loan proceeds); \u00a7 18 (four Permitted Exceptions) against Title Commitment Schedule B\u2013Part II "
      "(thirteen exceptions, including ad valorem taxes, the zoning exception, the possession exception and the CC&R First "
      "Amendment recorded in Book 7102, Page 388).",
      "These are drafting points rather than credit points, but each could produce a dispute: a \u201csingle advance\u201d description "
      "invites an argument that the Bank must fund once; an Events of Default clause that points to the wrong covenant is "
      "unenforceable as written; an extension option with no stated conditions could be read as unconditional; an unused line fee on "
      "reserved amounts charges the Borrower for money it cannot draw; the expense deposit and the loan-funded lender-expense line "
      "may fund the same costs twice; and an incomplete permitted-exception list gives the Bank a title policy that is broader than "
      "what it approved.",
      "Ambiguity in a construction loan agreement is most expensive at the point of a draw, an extension or a default \u2014 exactly "
      "when the Bank needs the documents to be self-executing.",
      "Correct each point in the definitive documents: describe the facility as a single commitment with multiple milestone "
      "disbursements; state the extension conditions expressly; define the unused line fee base to exclude the interest reserve and "
      "contingency; require invoices and a settlement statement showing that no cost is funded twice from the expense deposit and loan "
      "proceeds; and list the permitted exceptions completely, including the First Amendment to the CC&Rs and the environmental deed "
      "notice.",
      "Section 2.1 (single commitment, multiple disbursements); section 2.10(c) (unused line fee base) and 2.10(e) (expense deposit); "
      "section 2.14 (extension conditions); section 13 (Events of Default, with the cross-reference corrected); Schedule 3 (permitted "
      "exceptions).")

    issue(doc, "20", "The Term Sheet's permitted exceptions omit matters that appear in the Title Commitment", "L-M",
      "Term Sheet \u00a7 18 (Permitted Exceptions: \u201cstandard printed exceptions, to be removed or modified as required by the "
      "Lender\u201d; the Duke Energy easement; the City of Durham stormwater easement; and the CC&Rs recorded in Book 6984, Page 1155) "
      "against Title Commitment, Schedule B\u2013Part II \u00b6\u00b6 1\u201313 (adds ad valorem taxes for 2025 and subsequent years; "
      "the Unified Development Ordinance and MU-D zoning restrictions; facts ascertainable by inspection or asserted by persons in "
      "possession; and the First Amendment to the CC&Rs recorded in Book 7102, Page 388, dated June 19, 2017).",
      "The Term Sheet's list is incomplete rather than wrong. The tax, zoning and possession exceptions are customary and, in the case "
      "of the possession exception, removable with a survey and an owner's affidavit. The First Amendment to the CC&Rs is a "
      "substantive omission because the operative architectural review and assessment provisions may be in the amendment. The "
      "environmental deed notice (Issue 8) is missing altogether from both lists.",
      "If the Title Policy is issued with exceptions beyond the approved list, the Bank's insured position is narrower than the credit "
      "approval assumed, and the difference may not be discovered until a claim.",
      "Approve a conformed permitted-exception schedule (Schedule 3 to the draft) that lists every exception, identifies which are to be "
      "removed and which accepted, and adds the recorded environmental deed notice in the form approved by counsel. Confirm with the "
      "Title Company that the standard exceptions will be deleted on delivery of the survey and affidavit.",
      "Schedule 3 (permitted exceptions); section 3.3 (title conditions).")

    issue(doc, "21", "North Carolina legal characterizations and two unbudgeted closing costs should be confirmed", "L",
      "Credit Memorandum \u00a7 4.3 (\u201cNorth Carolina is a judicial foreclosure state and \u2026 deficiency judgments following "
      "foreclosure are subject to the fair price confirmation hearing requirements of N.C.G.S. \u00a7 45-21.36\u201d). Term Sheet "
      "\u00a7 3.3 (default rate of the contract rate plus 5.00%) and section 2.15 of the draft (late charge of 5.00%). Title "
      "Commitment, Schedule A \u00b6 3(b) (owner's policy proposed at $8,900,000 in addition to the $47,500,000 loan policy) against "
      "Borrower Draw Schedule line 3.07 (\u201cTitle Insurance & Recording \u2014 Lender's title policy, endorsements, recording fees\u201d "
      "$245,000).",
      "Deeds of trust in North Carolina are foreclosed by the trustee's exercise of a power of sale in a special proceeding before the "
      "Clerk of Superior Court under Article 2A of Chapter 45 of the General Statutes, with deficiency determinations subject to the "
      "fair-value provisions of N.C.G.S. \u00a7 45-21.36 \u2014 a characterization materially different from \u201cjudicial "
      "foreclosure,\u201d and one that affects how the remedies article, the receiver provisions and the guaranty analysis should be "
      "drafted. Counsel should also confirm that the default rate and the late charge are within the maximum lawful rate for a "
      "commercial loan of this size (N.C.G.S. \u00a7\u00a7 24-1.1, 24-8), and that the savings clause in section 2.16 is sufficient. "
      "On costs, the documentary excise tax payable on the Deed of Trust in North Carolina (approximately $1.00 per $500 of secured "
      "indebtedness, or approximately $95,000 on $47,500,000) and the owner's policy premium are not separately identified in the "
      "budget; they may be captured in line 3.07, but that should be confirmed rather than assumed.",
      "A mischaracterization of North Carolina foreclosure law in the credit file is a examiner and audit finding waiting to happen, "
      "and an unbudgeted $95,000 closing cost is a small but avoidable addition to the funding gap in Issue 3.",
      "Conform the credit file and any borrower-facing description to North Carolina practice; confirm the rate and charge analysis "
      "in a short opinion or memorandum; and obtain a fee quote from the Title Company allocating the loan policy premium, the "
      "owner's policy premium, the excise tax and the recording fees, so that line 3.07 can be reconciled to actual invoices.",
      "Section 11.8 (North Carolina foreclosure and fair value); section 14.1(d) (power of sale under Chapter 45); section 2.16 "
      "(maximum rate); section 18.2 (expenses and excise tax).")

    issue(doc, "22", "A number of documents necessary to close are not in the Record", "M",
      "The Record contains no GMP construction contract, architect's agreement, Phase II report, NFA letter, recorded deed notice, "
      "ALTA survey, payoff letter, complete Operating Agreement, Borrower or Guarantor financial statements and tax returns, draft "
      "intercreditor agreement, zoning compliance letter, building permits, insurance certificates, Architectural Review Committee "
      "approval, flood determination, non-consolidation opinion, or contractor bonding evidence \u2014 each of which is a condition of "
      "closing under Term Sheet \u00a7 11 and Credit Memorandum \u00a7 10.1.",
      "We have drafted the closing conditions to require each item (Article III of the draft) and have not assumed the content of any "
      "of them. Where a fact depends on a missing document (the payoff amount, the number and identity of units above the affected "
      "area, the actual source of the land purchase funds, the GMP scope exclusions), the draft uses a bracketed placeholder rather "
      "than an assumed figure.",
      "Several of the issues above (notably 1, 3, 5 and 11) cannot be closed out on the current Record, and the Bank cannot issue the "
      "closing certificate or fund the initial advance on the basis of an unverified file.",
      "Circulate the diligence request list in Section VIII below to Borrower and its counsel immediately, with a return date that "
      "permits review before the February 28, 2025 target closing; if the items cannot be delivered in time, move the closing rather "
      "than fund against an incomplete file. Note also that the Phase I ESA's All Appropriate Inquiries shelf life runs to April 26, "
      "2025 and the Title Commitment expires June 5, 2025, so a closing delay past April 26, 2025 requires an updated Phase I.",
      "Article III (conditions precedent, in 20 sections); section 3.2 (updated Phase I if closing after April 26, 2025).")
