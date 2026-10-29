from memo_helpers import *

def blocks(doc):
    h1(doc, "Part 4 — Cross-document conflict register and the Bayside gap analysis", "4")
    h2(doc, "4.1  Conflict register", "4.1")
    body(doc, "The following conflicts appear across the five transaction documents. \"Conflict\" here means that two "
              "records cannot both be right, or that one record attributes to another a term it does not contain.")
    rows = [
        ["C1", "Parcel area and legal description",
         "TC Ex. A: courses enclosing ~279,535 SF, recited \"3.2 acres (139,392 SF)\"; TS § 2 adopts 139,392 SF and "
         "$20.45/SF",
         "Survey: 139,475 SF on a description that closes exactly",
         "Title description is wrong; use survey description; conform area recital (Part 3.1)",
         "Crit."],
        ["C2", "Identity of the governing survey",
         "TC: \"CLS-2025-0321,\" Ferreira, PLS 12847, rev. May 15, 2025",
         "Survey: \"CLS-2025-0417,\" Pellegrino, PLS-008741, April 28, 2025",
         "Different job, surveyor, license and date; the referenced survey is not in the record",
         "High"],
        ["C3", "Bulkhead frontage",
         "TS § 2, TC Ex. A and Survey narrative: \"approximately 480 linear feet\"",
         "Survey traverse: eastern boundary line 320.47 ft; easement area 15 × 320.47 = 4,807 SF, not 7,200 SF",
         "480 ft appears to trace to the erroneous title description; confirm from plat. Drives bulkhead cost and "
         "open-space geometry",
         "High"],
        ["C4", "Condemnation record",
         "TC: Vol. 367, Pg. 44; Judicial District of New Haven",
         "Survey: Vol. 375, Pg. 44. TS § 2: Judicial District of Port Calloway",
         "Discrepancy in volume/page and in court; recited consistently nowhere",
         "Low"],
        ["C5", "AMI geography for the affordable covenant",
         "TS § 4: \"Port Calloway Metropolitan Statistical Area\"",
         "TC Ex. 5: \"New Haven-Milford, CT MSA\". Survey § 3(d): \"Bridgeport-Stamford-Norwalk HUD Metro FMR Area\"",
         "Three geographies. The recorded 2019 covenant (New Haven-Milford) controls. Premises are in New Haven County",
         "Med."],
        ["C6", "Commencement of Percentage Rent",
         "TS § 6: \"Lease Year 6\" (and TS § 5 makes Lease Year 1 = Rent Commencement Date)",
         "Board Res. recital (b): \"Year 6 of the Ground Lease term\"",
         "A three-year difference (Oct 2031 vs Oct 2033) in when Percentage Rent begins",
         "High"],
        ["C7", "Commencement of the tax abatement",
         "TS § 10: period \"shall commence on the Lease Commencement Date\"",
         "Client instruction; Board Res. recital (income years); Coventry underwriting",
         "Three construction years consumed before rent commences; abatement value lost (Part 6.2)",
         "High"],
        ["C8", "LOC issuer criteria",
         "TS § 8: rating of A- (S&P) / A3 (Moody's)",
         "Board Res. recital (c): \"issued by a federally chartered banking institution\"",
         "Different tests; a federally chartered bank need not be A-/A3 rated, and vice versa",
         "Med."],
        ["C9", "Form of security deposit",
         "TS § 8 and § 15(d): irrevocable standby LOC only",
         "Bayside § 4: LOC \"or, at Borrower's option, a cash security deposit\"",
         "Tenant-favourable option exists under the loan but is unavailable under the Term Sheet",
         "Low"],
        ["C10", "Setoff",
         "TS § 5: Base Rent payable \"without demand, setoff, or deduction except as expressly provided\"",
         "TS § 16 (Tenant remedies): Tenant may \"offset amounts due against Base Rent\"",
         "Internal conflict in the same instrument; must be reconciled expressly (Draft § 4.6)",
         "Med."],
        ["C11", "Whether reverter termination is automatic",
         "TS § 9: Lease \"shall automatically terminate upon the expiration of such period\"",
         "Bayside § 5.4: \"No termination ... shall be effective unless and until Lender has received such notice and "
         "the applicable Lender cure periods ... have expired without cure\"",
         "Direct conflict. A self-executing termination would defeat the lender cure rights that are a condition of the "
         "loan",
         "Crit."],
        ["C12", "Scope of the reverter",
         "TS § 9: reverter only for Milestone 1 and Milestone 3",
         "TS § 16 (Landlord remedies): \"exercise the reverter rights described in Section 9\" upon any uncured Event "
         "of Default",
         "Would extend forfeiture to bankruptcy, monetary defaults and everything else",
         "Crit."],
        ["C13", "Treatment of the mechanics' lien",
         "TS § 13: listed as Permitted Exception No. 6",
         "TC Req. 7: \"The Company will not issue either policy ... until this requirement has been satisfied\". "
         "Bayside § 6(c): no exceptions other than those approved by Lender",
         "The lien cannot be a Permitted Exception if the policy will not issue over it. It must be discharged",
         "High"],
        ["C14", "ROFR carve-outs",
         "TS § 11 and Draft § 11.5: no ROFR for mortgagee transfers, affiliates or change of control",
         "Recorded Declaration (Sept. 8, 2019, Vol. 405, Pg. 55), per TC Ex. 4: \"does not by its terms contain any "
         "exception or carve-out for transfers resulting from foreclosure, deed-in-lieu ... or assignments by a "
         "leasehold mortgagee\"",
         "A recorded instrument binds regardless of the lease. Must be amended of record before closing",
         "High"],
        ["C15", "Ground-floor residential use",
         "TS § 4: Project includes \"ground-floor residential lobby and amenity spaces (fitness center, package room, "
         "resident lounge, and leasing office)\" and permits \"residential apartments\"",
         "ELUR and Phase II § 2.3(a): prohibition on residential use on the ground floor; Phase II expressly flags that "
         "the ELUR \"does not define or specifically address\" lobby/amenity space",
         "Live enforcement and permitting risk; unresolved in the record",
         "High"],
        ["C16", "Affordable housing unit count",
         "TS § 4(a): tower contains \"a number of residential dwelling units to be determined and specified in the "
         "Definitive Lease\"",
         "15% covenant applies to \"all residential dwelling units\" (TS § 4; recorded 2019 covenant)",
         "The 15% obligation cannot be quantified, scheduled or monitored until the unit count is fixed",
         "Med."],
        ["C17", "Affordable covenant enforcement gaps",
         "TS § 4 and Board Res. § 2(b) assume a complete covenant",
         "TC Ex. 5 notes the recorded covenant omits (i) a recalculation method, (ii) income verification, (iii) a "
         "monitoring entity, (iv) enforcement remedies, (v) distribution requirements, (vi) floor/location rules",
         "Six gaps; the lease must fill them (Draft § 14.5)",
         "Med."],
        ["C18", "Flood insurance standard",
         "TS § 12(d): \"in no event less than the maximum coverage available under the National Flood Insurance "
         "Program\"",
         "Bayside § 6(h): flood insurance \"in amounts satisfactory to Lender\"",
         "NFIP maximum (residential $250,000 building / $100,000 contents; commercial $500,000 / $500,000) is a "
         "fraction of replacement cost. The two standards are incompatible",
         "Med."],
        ["C19", "Freeboard",
         "TS § 2; TC Ex. 9; Survey: FFE 15 ft NAVD88 (3 ft freeboard)",
         "Phase II §§ 5, 7.5: recommends 4–5 ft freeboard (FFE 16–17 ft), citing PA 23-167, CIRCA projections and "
         "municipal practice",
         "For a 99-year coastal term, 3 ft is likely inadequate; design, insurance and code-change exposure",
         "Med."],
        ["C20", "Distortion in document dating",
         "Bayside term sheet dated May 28, 2025",
         "Bayside § 5 refers to the Ground Lease \"the term sheet for which is dated June 10, 2025\"",
         "A May document cites a June document. Suggests Bayside updated its requirements form after circulation; "
         "confirm the operative version",
         "Low"],
        ["C21", "Loan term against development program",
         "Bayside § 2: 48 months, plus two 6-month extensions (maximum 60 months). Coventry completion guaranty: "
         "lien-free completion \"on or before the Initial Maturity Date\"",
         "TS § 9: Milestone 3 at 60 months; Milestone 4 at 84 months",
         "Phase 1 completion coincides with maximum loan maturity; Phase 2 has no construction financing at all; "
         "Coventry's guaranty matures a year before the Phase 1 milestone",
         "High"],
        ["C22", "Renewal/extension",
         "TS § 3: \"No renewal options are contemplated\"",
         "Bayside § 5.3: New Lease for \"the remainder of the original term (including any extension periods)\"",
         "No extension periods exist. Immaterial as drafted, but relevant to any extension option we negotiate",
         "Low"],
        ["C23", "Status of the 2019 recorded declarations",
         "TS § 13 lists the ROFR and affordable covenant as Permitted Exceptions \"as described in Section 11\" / "
         "\"Section 4\" as though created by the Term Sheet",
         "Both are pre-existing recorded instruments (Vol. 405, Pg. 55; Vol. 408, Pg. 230, both 2019)",
         "The lease cannot create or amend them; they must be incorporated, conformed or amended of record",
         "Med."],
        ["C24", "Diligence windows against the closing schedule",
         "Survey field date April 20, 2025 / plat April 28, 2025; TC effective June 1, 2025, expiring December 1, 2025",
         "Bayside § 6(d): survey dated within 90 days of closing; § 6(a)–(c): current commitment and policies",
         "For any closing after July 19, 2025 the survey is stale. The commitment expires before a December closing",
         "Med."],
    ]
    table(doc, [["#", "Subject", "One record says", "Another record says", "Analysis", "Sev."]] + rows,
          [0.38, 1.0, 1.5, 1.5, 1.6, 0.52], size=6.5)
    body(doc, "Three of these conflicts (C11, C12, C13) would each by itself prevent the loan from closing. Two more "
              "(C1, C14) sit in the title chain and will surface at the title company's desk regardless of what the "
              "lease says. We have resolved each in the Draft Lease as described in the last column of the table and "
              "in Part 6; where the resolution requires a recorded amendment or a third party's action, the Draft "
              "Lease makes it a condition precedent rather than a covenant to be performed later.")

    h2(doc, "4.2  Bayside § 5 gap analysis: the Term Sheet does not satisfy the loan conditions", "4.2")
    body(doc, "Bayside's § 5 lists seven required ground lease provisions and states that \"every one of which shall "
              "constitute a condition precedent to the closing of the Loan.\" We compared each against Term Sheet § 9 "
              "and the rest of the record. **None is satisfied in full.** Four are not addressed at all; three are "
              "addressed only in part.")
    table(doc,
          [["Bayside requirement", "What the Term Sheet says", "Gap", "Status", "Draft Lease §"],
           ["§ 5.1 Leasehold mortgage without consent, approval, joinder or fee",
            "TS § 9: Tenant \"shall have the right to encumber ... subject to the terms and conditions of the "
            "Definitive Lease\"",
            "No express no-consent / no-fee / no-condition language; \"subject to\" invites a later consent right",
            "Not met", "§ 9.1"],
           ["§ 5.2 SNDA containing items (a)–(d), delivered before first advance",
            "TS § 9: SNDA \"on customary terms,\" form attached as exhibit",
            "\"Customary\" is not a standard a lender's counsel will accept; items (a)–(d) not specified; recording "
            "not required", "Partial", "§ 9.9; Ex. F"],
           ["§ 5.3 New Lease: request within 60 days of notice of termination; remainder of original term; Landlord to "
            "execute within 30 days; effective as of termination; priority equal to terminated lease; subleases "
            "recognized; non-monetary cure up to 180 days",
            "TS § 9: mortgagee may obtain a New Lease on \"substantially the same terms\"; cure monetary within 60 days "
            "and non-monetary within 90 days \"following the date of termination\"",
            "No request window; no statement that the term is the **remainder** of the original term; no 30-day "
            "execution obligation; no effective-date, priority or sublease-recognition provision; no 180-day "
            "non-monetary cure tail", "Not met", "§ 9.6"],
           ["§ 5.4 Notices simultaneous; lender cure 60 days (monetary) / 90 days (non-monetary); \"in addition to, and "
            "not concurrent with\" Tenant's cure periods; Landlord to accept lender cure",
            "TS § 9 (Default Notices): copies delivered simultaneously with Tenant",
            "Simultaneous notice only. **No lender cure periods at all**, and no non-concurrency clause — the "
            "essential protection", "Not met", "§§ 9.3, 9.5"],
           ["§ 5.5 No voluntary surrender **and no material amendment** without lender consent; void as against Lender",
            "TS § 9: \"No Voluntary Surrender\" bullet only",
            "Amendment/modification/supplement restriction and the voidness remedy are absent", "Partial", "§ 9.4"],
           ["§ 5.6 Foreclose and assign without consent; qualified transferee; Landlord to execute documents "
            "reasonably requested",
            "TS § 9: foreclosure and assignment permitted \"provided that any such transferee meets reasonable "
            "financial and experience qualifications to be established in the Definitive Lease\"",
            "Qualification criteria left open (a lender wants objective tests); no duty to execute documents; no "
            "recognition deadline", "Partial", "§ 9.7"],
           ["§ 5.7 Bankruptcy protections: request to assume/reject under 11 U.S.C. § 365; lender right to cure and "
            "provide adequate assurance; New Lease survives rejection",
            "Term Sheet: **silent**. § 16(d) treats a bankruptcy filing as an Event of Default",
            "Absent entirely. As drafted, a Tenant bankruptcy is a default with no lender protection", "Not met",
            "§ 9.8"]],
          [1.68, 1.62, 1.62, 0.62, 0.96], size=6.5)
    body(doc, "**Implication.** Bayside will not close on the Term Sheet's language. Sandra Milliken's team will "
              "redline the Draft Lease to its checklist in any event; the point of getting it right now is that the "
              "redline will not then arrive at the same time as the title objection and the Board approval cycle. The "
              "Draft Lease's Article 9 is deliberately drafted to meet or exceed each of § 5.1–5.7, and to be equally "
              "acceptable to a future refinancing lender (no fee, no consent, unlimited mortgagees, no cap on "
              "refinancings, protections running to \"each Leasehold Mortgagee\"), which is what Ansel needs for "
              "institutional-quality status.")
    body(doc, "**Your specific asks** in this area were four: reverter subordination to the leasehold mortgage; "
              "180 days' independent lender cure for milestone defaults; New Lease surviving reverter termination; and "
              "no reverter before the lender's cure period is exhausted. All four are in the Draft Lease "
              "(§§ 9.5(c), 9.6, 10.5(g), 10.6(e)). Note that neither the Term Sheet nor Bayside's own § 5.4 provides a "
              "lender cure period calibrated to milestone defaults — Bayside's 90-day non-monetary period assumes a "
              "curable default, and a missed completion milestone is not curable by writing a check. The 180-day "
              "period in Draft § 9.5(c), running from the expiry of Tenant's own 180-day cure period (i.e., a "
              "theoretical 360 days from the Authority's notice), is a provision we are adding for both parties' "
              "benefit: without it, a lender facing a milestone default could only foreclose into a forfeiture, which "
              "no lender will do.")
