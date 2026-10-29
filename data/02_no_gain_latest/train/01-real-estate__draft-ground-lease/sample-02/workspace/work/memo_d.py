from memo_helpers import *

def blocks(doc):
    h1(doc, "Part 5 — The reverter and improvement forfeiture: \"the hill\"", "5")
    h2(doc, "5.1  What the record actually provides", "5.1")
    body(doc, "Term Sheet § 9 provides that if Tenant fails to achieve Milestone 1 or Milestone 3 (as extended), the "
              "Authority may deliver a notice specifying the failure; Tenant then has 180 days to cure; and \"the Lease "
              "shall automatically terminate upon the expiration of such period,\" whereupon (a) Tenant forfeits the "
              "$5,700,000 letter of credit, which the Authority \"shall be entitled to draw in full,\" and (b) \"[a]ll "
              "improvements, structures, and fixtures constructed, installed, or placed on the Premises by Tenant ... "
              "shall immediately revert to and become the sole property of the Landlord, free and clear of any claims "
              "by Tenant, without any payment, compensation, or reimbursement to Tenant.\"")
    body(doc, "Four features of that drafting deserve to be named, because each is a separate problem:")
    bullet(doc, "**It is automatic.** Termination occurs by operation of the expiry of the cure period, without any "
                "election, notice or grace. That is the feature that collides head-on with Bayside § 5.4 (conflict "
                "C11).")
    bullet(doc, "**It is not limited to milestones.** Term Sheet § 16 lists \"exercise the reverter rights\" as a "
                "general remedy for any uncured Event of Default, which would extend forfeiture to a monetary default, "
                "a bankruptcy filing or an insurance lapse (conflict C12).")
    bullet(doc, "**It double-counts.** The Authority takes both the deposit and the improvements. The deposit is "
                "already 24 months of Base Rent; the improvements may be worth fifty times that.")
    bullet(doc, "**It purports to extinguish the mortgage.** \"Free and clear of any claims by Tenant\" cannot, as a "
                "matter of recorded priority, extinguish a leasehold mortgagee's interest, and Bayside will not treat "
                "it as doing so. But it is exactly the language that makes the leasehold mortgage unmarketable, "
                "because the lender's only remedy — foreclosure into the leasehold — leads to the forfeiture it was "
                "lending against.")
    body(doc, "The Board has been told that the lease will contain \"reverter rights in favor of the Authority in the "
              "event of Tenant's failure to achieve such milestones\" (Resolution No. 2025-047, § 2(a)). The Draft "
              "Lease preserves a reverter. What it removes is the uncompensated forfeiture. That distinction is the "
              "single most important framing point in the negotiation, and it is accurate: the Authority still gets "
              "the land back, still gets the improvements, and still gets a defined remedy.")

    h2(doc, "5.2  Exposure, quantified", "5.2")
    table(doc,
          [["Component", "Amount", "Timing", "Source"],
           ["Security deposit forfeited", "$5,700,000", "On reverter termination", "TS § 9(b); TS § 8"],
           ["Improvements forfeited", "$200,000,000 – $300,000,000", "By Milestone 3 (October 1, 2030)",
            "Your June 15 email; consistent with $352,000,000 total hard costs and Phase 1 being the residential tower "
            "plus retail"],
           ["**Total forfeiture**", "**$205,700,000 – $305,700,000**", "Single milestone miss", "Computed"],
           ["Authority's actual damages on a 24-month slip of Milestone 3", "≈ $5,700,000 – $7,300,000",
            "24 months of Base Rent at the then-current rate", "Computed from TS § 5 schedule"],
           ["Ratio of forfeiture to damages", "≈ 28× to 54×", "—", "Computed"]],
          [2.25, 1.55, 1.3, 1.4], size=7.5)
    body(doc, "The final row is the heart of the matter. On a two-year slip in achieving Substantial Completion of "
              "Phase 1 — a slip that a DEEP approval, a coastal permitting appeal or a supply-chain failure could "
              "produce — the Authority's genuinely compensable loss is on the order of two years of ground rent, "
              "because Base Rent is the only thing it was going to receive in that period (and Percentage Rent does "
              "not begin until Lease Year 6). The provision delivers it between $206 million and $306 million. That is "
              "not a remedy proportioned to the harm; it is a transfer of the entire project.")

    h2(doc, "5.3  Is it enforceable? Our assessment, and its limits", "5.3")
    body(doc, "You asked us to research whether Connecticut law provides relief against a disproportionate forfeiture, "
              "and you recalled a \"Stamford project\" case. **We have not verified a Connecticut case on point, and we "
              "should not cite one until we have.** What follows is our assessment of the governing principles and of "
              "the risks on both sides; Part 7 identifies the research that must be completed before any of this is "
              "put in front of Mr. Koss or the Board.")
    h3(doc, "The argument for Tenant")
    body(doc, "The provision has two doctrinal vulnerabilities. **First, penalty.** A contractual term that fixes "
              "damages in an amount grossly disproportionate to the loss that the parties could reasonably have "
              "anticipated is an unenforceable penalty rather than a valid liquidated damages provision. The "
              "Restatement (Second) of Contracts states the rule at § 356(1), and Connecticut follows the general "
              "rule. On the numbers in Part 5.2 above, the disproportion is on the order of 28× to 54×, which is well "
              "outside any range a court is likely to accept as a forecast of harm.")
    body(doc, "**Second, forfeiture.** Equity relieves against forfeiture where the forfeiture would be "
              "disproportionate to the breach and the injured party can be adequately compensated (Restatement "
              "(Second) of Contracts §§ 208, 229; the Restatement (Third) of Property (Landlord and Tenant) treats "
              "forfeiture as a disfavoured remedy). A 99-year ground lease under which a tenant invests $425 million "
              "on land it does not own is the paradigm case for the application of that principle, and the Authority's "
              "own internal documents describe the public benefits it expects to receive from the completed project.")
    body(doc, "**Third, and practically most important:** the leasehold mortgagee's interest is a separate property "
              "interest. A provision that purports to wipe it out \"free and clear of any claims\" will be tested "
              "against a lender with $285 million at stake and its own counsel. Whatever the outcome, the Authority "
              "would be litigating against a secured creditor with priority, not merely against Meridian.")
    h3(doc, "The argument against Tenant — and why we must not rely on the defense")
    body(doc, "There are two credible counter-arguments, and you should hear them clearly. **(i) Forfeiture of a "
              "leasehold is different.** Courts have traditionally enforced conditional limitations and forfeiture "
              "clauses in leases more readily than they strike liquidated damages clauses in ordinary commercial "
              "contracts, on the theory that the landlord's reversion is a property right and the tenant takes subject "
              "to the condition. **(ii) Sophisticated parties, public landlord.** The Authority will argue that "
              "Meridian is a sophisticated developer that negotiated a public-benefit-laden ground lease with counsel, "
              "that the milestones are public obligations, and that a court should not rewrite the bargain that a "
              "public body obtained for public land.")
    body(doc, "**So the provision might well be enforced.** That is precisely why an unenforceability argument is not "
              "a strategy: Bayside will not lend $285 million against a litigable defense, and by the time the question "
              "is answered, the project will have failed. The provision must be fixed in the document. If the "
              "Authority's counsel argues that the provision is enforceable and therefore need not change, the answer "
              "is that the Authority is welcome to that view but that no institutional lender will accept it, and the "
              "transaction will not close.")
    flagbox(doc, "Research status — do not cite yet.",
             "The legal propositions in this section are stated at the level of restated general principle, not as "
             "verified Connecticut authority. The \"Stamford project\" case you recalled could not be identified from "
             "the record and we have not located it. Before any of this is used in a letter, at the Board table, or in "
             "a brief, we must (i) locate and Shepardize Connecticut appellate authority on penalties and on relief "
             "from forfeiture in leases, (ii) confirm whether a Connecticut court would treat the reverter as a "
             "conditional limitation enforceable according to its terms, and (iii) confirm the effect of the "
             "leasehold mortgagee's intervening interest. Item 7.1 of Part 7.")

    h2(doc, "5.4  What the Draft Lease does", "5.4")
    body(doc, "The reverter is a defined, sequenced, compensated remedy. Mechanically, the Draft Lease:")
    bullet(doc, "**Retains the reverter** for Milestone 1 and Milestone 3 only, and expressly confines it there: "
                "failure of Milestone 2 or Milestone 4 gives no remedy beyond notice and consultation (§ 3.5), and the "
                "Milestone remedy is Landlord's \"sole and exclusive remedy\" for a milestone default (§ 10.3).")
    bullet(doc, "**Removes automatic termination** (§ 10.5(f)), substituting a valid notice, a 180-day Tenant cure "
                "period, a 180-day lender cure period, and a 30-day election window — after which the Authority is "
                "deemed to have waived that milestone default (§ 10.5(e)). Waiver matters: it prevents an Authority "
                "from sitting on a stale default for years and then terminating.")
    bullet(doc, "**Requires the Improvement Payment** (§ 10.6(a)): the greater of the appraised fair market value of "
                "the Improvements or Tenant's unreimbursed hard costs, less insurance and condemnation recoveries not "
                "applied to restoration, less Landlord's Documented Damages. That is your option (a) and your option "
                "(b) from the June 15 email, in the alternative rather than the conjunctive, with the higher of the "
                "two governing.")
    bullet(doc, "**Caps the Authority's damages** (§ 10.7) at accrued rent, 24 months of Base Rent at the then-current "
                "rate, re-letting costs and enforcement costs, and excludes lost Percentage Rent, lost tax revenue, "
                "the value of the Improvements, and consequential and speculative amounts.")
    bullet(doc, "**Follows the compensation with real teeth** (§ 10.6(c)): the Improvement Payment is due within 60 "
                "days, may be secured by a first lien on the Improvements at Tenant's election, and the Authority may "
                "not take possession or lease the Improvements to a third party until it has paid or secured.")
    bullet(doc, "**Makes the reverter subordinate** to the leasehold mortgage and conditional on the lender's rights "
                "being exhausted (§ 10.5(g)), which is the Term Sheet change Sandra Milliken requires.")
    bullet(doc, "**Keeps the Authority whole on the public side** (§ 10.6(f)): on any reverter the Authority takes "
                "subject to the ELUR, the affordable housing covenant, all subleases and the open-space obligation — "
                "which is what the Authority actually wants, since it will be the owner of an operating building.")
    bullet(doc, "**Adds a paid escape valve** (§ 3.4(d), bracketed): Tenant may buy 6-month extensions of Milestone 1 "
                "or 3 rather than face forfeiture. For a landlord, an extension fee is a certain receipt; for a "
                "tenant, it is a way to survive a permitting overrun. It is often the provision that lets both sides "
                "sign.")
    body(doc, "Two further protections are worth flagging for your call: the appraisal mechanic (§ 10.8) uses two MAI "
              "appraisers and a third if they differ by more than 5%, with the valuation made disregarding the "
              "remaining term and the reversion — which prevents the Authority from arguing that a 99-year leasehold "
              "is worth little. And § 10.5(h) bars termination for a Milestone 3 miss if Substantial Completion has "
              "actually been achieved.")

    h2(doc, "5.5  How to sell it to the Authority", "5.5")
    body(doc, "The Authority's counsel will treat the reverter as a deal point it cannot give up, because the Board "
              "resolution recites it. The argument that has the best chance of moving them is not proportionality "
              "rhetoric; it is the following, in this order:")
    bullet(doc, "**An unenforceable remedy is worth nothing.** If a court strikes the forfeiture as a penalty, or "
                "relieves against the forfeiture, the Authority is left with a lease still in force, a tenant it "
                "wants to remove, and no remedy at all. A compensated reverter is a remedy a court will enforce.")
    bullet(doc, "**The lender is the reason.** The Authority's own recital records that the ground lease must contain "
                "provisions satisfactory to the construction lender (Resolution recital). Bayside has said in terms "
                "that the reverter as written would jeopardize the leasehold mortgage. The Authority cannot have both "
                "an uncompensated reverter and a $285 million construction loan.")
    bullet(doc, "**The Authority still gets the building.** On a reverter at 95% complete the Authority acquires a "
                "nearly finished residential tower and retail podium, subject to a defined payment that is largely "
                "funded by the value of the asset it is receiving. It is not paying $300 million; it is paying the "
                "appraised value out of the asset it keeps.")
    bullet(doc, "**The Authority's real leverage is elsewhere, and we will give it that leverage.** If the Authority "
                "wants enforcement teeth, we will trade: extension fees and delay charges payable to the Authority; a "
                "step-up in Base Rent during any period of milestone delay; Board reporting on construction progress; "
                "a right to approve a replacement developer; and the 180-day cure running from the Authority's notice "
                "rather than from any later event. Those are teeth that bite without destroying the collateral.")
    body(doc, "**Walk-away position.** If the Authority will not move on compensation, the minimum acceptable outcome "
              "is: (i) no forfeiture of the Improvements where Phase 1 is more than 50% complete; (ii) no forfeiture "
              "for delay caused by permitting, DEEP or coastal approvals, or by the Authority's own acts; (iii) no "
              "forfeiture while a lender is curing; (iv) the deposit applied to actual damages with the excess "
              "returned; and (v) the Improvement Payment limited to hard cost reimbursement net of recoveries and "
              "damages. If none of that is available, the transaction should not proceed, because the loan will not "
              "close.")
