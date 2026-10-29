from memo_helpers import *

def blocks(doc):
    # ================= PART 7 =================
    h1(doc, "Part 7 — Legal research and verification items (not yet completed)", "7")
    body(doc, "These are the questions on which we have stated a principle but not verified the authority. Each must "
              "be closed before the position is relied on externally. We have graded them by consequence.")
    table(doc,
          [["#", "Question", "Why it matters", "Status"],
           ["7.1", "Connecticut authority on penalties and on relief from forfeiture in a lease, including whether a "
            "reverter in a ground lease is treated as an enforceable conditional limitation rather than a penalty, and "
            "the treatment of a leasehold mortgagee's intervening interest",
            "Underpins the entire reverter negotiation and any litigation position (Part 5.3)", "Open — high"],
           ["7.2", "Whether the City of Port Calloway has statutory authority for a fifteen-year, three-tier abatement "
            "at 25% / 50% / 75% of assessed value, and what hearing and approval steps are required",
            "If the structure is outside the city's authority the pro forma fails and the lease cannot fix it "
            "(Part 6.2)", "Open — critical"],
           ["7.3", "Whether a Connecticut redevelopment authority under Conn. Gen. Stat. § 8-125 et seq. may lease for "
            "99 years, and whether any appraisal, notice, hearing, RFP or best-value requirements apply to the "
            "disposition of the leasehold",
            "A defect in the Authority's authority would taint the lease, the title policy and the loan (Part 8)",
            "Open — high"],
           ["7.4", "Whether a mechanics' lien validly attaches to property held by a redevelopment authority for a "
            "public purpose, whether Conn. Gen. Stat. § 49-37 bonding is the correct route, and whether Tenant could be "
            "treated as an \"owner\" for lien purposes once the lease and memorandum are recorded",
            "Determines whether the lien must simply be paid or can be defeated (Part 6.6)", "Open — medium"],
           ["7.5", "Whether the Authority can be compelled by specific performance to execute a New Lease, and whether "
            "a future Board can be bound by this Board's covenant; whether the Authority may agree to binding "
            "arbitration; whether a jury trial waiver by a public body is effective; the scope of any governmental "
            "immunity",
            "The New Lease right is the single most important lender protection after the cure periods; if it is not "
            "specifically enforceable it is worth much less (Sections 9.6, 20.2, 20.16)", "Open — high"],
           ["7.6", "Whether the New Lease right survives rejection of the ground lease in bankruptcy as a property "
            "interest under 11 U.S.C. § 365(h)/(i), and how to document it to maximize that outcome",
            "Bayside § 5.7(d) requires it (Section 9.8)", "Open — medium"],
           ["7.7", "Whether the ELUR's ground-floor restriction, as drafted and as approved by DEEP, reaches "
            "non-habitable lobby, amenity and leasing space, and what a modification application requires",
            "Design, permitting and Milestone 1 risk (Part 6.3)", "Open — high"],
           ["7.8", "The coastal permit requirements for bulkhead rehabilitation (Structures, Dredging and Fill; tidal "
            "wetlands) and whether the pedestrian easement prohibits the work",
            "Schedule and cost risk for an unquantified item (Part 6.5)", "Open — medium"],
           ["7.9", "Whether the Authority's 2019 recorded declarations can be amended unilaterally or require the "
            "consent of any third party, and what Board action is required",
            "The ROFR amendment is a closing condition (Part 6.7)", "Open — medium"],
           ["7.10", "Connecticut and federal fair housing / affirmatively furthering fair housing requirements as they "
            "affect unit distribution and the 15% covenant, and any HUD or state monitoring obligations",
            "Affects the distribution provisions in Section 14.5", "Open — low"]],
          [0.42, 2.35, 2.1, 0.63], size=7)

    # ================= PART 8 =================
    h1(doc, "Part 8 — Missing documents and diligence requests", "8")
    body(doc, "Items marked ★ should be requested this week; each one has the potential to change a number in the "
              "draft.")
    table(doc,
          [["#", "Document", "From", "Why we need it"],
           ["1 ★", "ALTA/NSPS survey, plat Sheets 1 and 2 (CLS-2025-0417), certified to Bayside", "Calloway Land "
            "Surveyors / Ridgepoint", "To resolve the 480 ft / 320.47 ft bulkhead question, the 139,392 / 139,475 SF "
            "area question, and the 8,000 SF open-space geometry"],
           ["2 ★", "Survey CLS-2025-0321 by J. Michael Ferreira, P.L.S. (the survey cited in the title commitment), "
            "or confirmation that no such survey exists", "Ridgepoint", "The title commitment's Exhibit A cannot be "
            "reconciled without it"],
           ["3 ★", "Phase II ESA full report and Appendices A–J, especially Appendix I (cost estimate backup) and "
            "Appendix F (ELUR)", "Halcyon / Meridian", "The $2.4M estimate, the disposal quantity, and the ELUR text "
            "are all unverifiable without it"],
           ["4 ★", "The ELUR instrument (Vol. 412, Pg. 88) and the DEEP-approved Environmental Management Plan", "Land "
            "records / Authority", "Defines \"residential use,\" the cap specification, and the compliance "
            "obligations"],
           ["5 ★", "Declaration of Right of First Refusal (Sept. 8, 2019, Vol. 405, Pg. 55)", "Land records",
            "The amendment we must draft (Part 6.7)"],
           ["6 ★", "Declaration of Restrictive Covenants (Nov. 15, 2019, Vol. 408, Pg. 230)", "Land records",
            "The six gaps in the affordable covenant (Part 6.11)"],
           ["7 ★", "Independent structural engineering assessment of the bulkhead", "Authority (per our request)",
            "Quantifies the largest unallocated cost in the deal (Part 6.5)"],
           ["8 ★", "Executed Bayside term sheet (or confirmation of status), loan commitment letter and the lender's "
            "ground lease and SNDA checklists", "Meridian / Bayside", "Confirms the operative § 5 requirements and "
            "whether the June 27, 2025 expiration has passed"],
           ["9", "Bayside's written consent to disclose its confidential term sheet terms to the Authority and its "
            "counsel", "Bayside", "Bayside § 12 restricts disclosure to third parties; the Authority is a third party; "
            "yet the lease must implement § 5"],
           ["10", "Coventry preferred equity documentation (11% preferred return, 70/30 promote above a 15% IRR "
            "hurdle)", "Coventry", "Ensures the lease's transfer and ROFR provisions do not impede the equity "
            "structure"],
           ["11", "Site plan / zoning analysis for a 28-story tower in WRD-3 (FAR, height, setback, parking)", "Meridian "
            "/ architect", "Confirms the program is buildable as of right; not in the record"],
           ["12", "UST closure records and the DEEP LUST file status (\"closure pending/incomplete\")",
            "Authority / DEEP", "The northwest corner contamination is attributed to two USTs removed c. 1988 without "
            "documented closure"],
           ["13", "Authority's 2019/2022 waterfront revitalization plan (as amended and readopted)", "Authority",
            "Recited in Resolution No. 2025-047; relevant to the public purpose analysis"],
           ["14", "Certified copy of Resolution No. 2025-047 and the roll-call vote", "Authority", "Title Requirement "
            "No. 2 and Section 2.3(a)"],
           ["15", "Any DEEP correspondence regarding the ELUR, the 2016–2017 remediation or the site's residual "
            "contamination", "Authority", "Landlord's disclosure representation in Section 18.1(f)"]],
          [0.35, 2.3, 1.15, 1.7], size=7)

    # ================= PART 9 =================
    h1(doc, "Part 9 — Schedule of proposed deviations from the Term Sheet", "9")
    body(doc, "Resolution No. 2025-047 authorizes the Executive Director to execute a lease \"on terms and conditions "
              "substantially consistent with the Term Sheet\" (§ 1) and to approve changes he and Authority counsel "
              "consider immaterial, provided that any deviation either of them \"determines to be material shall be "
              "brought before the Board for further review and approval prior to execution\" (§ 4(d)). The following "
              "table is the list we recommend including in the transmittal to the Authority, both because it is "
              "required and because volunteering it builds credibility for the items that matter. Items marked "
              "**M** should be treated as material; **I** as immaterial.")
    table(doc,
          [["#", "Provision", "Term Sheet position", "Draft Lease position", "Class"],
           ["1", "Reverter — compensation", "Improvements revert \"without any payment, compensation, or "
            "reimbursement\"", "Improvement Payment = greater of appraised value or unreimbursed hard costs, net of "
            "recoveries and Documented Damages (§ 10.6)", "M"],
           ["2", "Reverter — mechanism", "\"Shall automatically terminate\" at expiry of 180-day cure",
            "Landlord election required within 30 days after all cure periods; deemed waiver; no automatic termination "
            "(§ 10.5)", "M"],
           ["3", "Deposit on reverter", "Landlord \"entitled to draw in full\"", "Draw limited to Documented Damages; "
            "excess returned (§ 10.9)", "M"],
           ["4", "Lender cure for milestone defaults", "None in the Term Sheet; 90 days non-monetary in Bayside § 5.4",
            "180 days from expiry of Tenant's cure period (§ 9.5(c))", "M"],
           ["5", "New Lease", "\"Substantially the same terms\"; cure within 60/90 days of termination",
            "Remainder of term; 60-day request window; 30-day execution; priority and sublease recognition; 180-day "
            "non-monetary tail (§ 9.6)", "M"],
           ["6", "Amendment restriction", "Not addressed", "No material amendment without each Leasehold Mortgagee's "
            "consent; void as against the mortgagee (§ 9.4)", "M"],
           ["7", "Bankruptcy", "Not addressed (filing is an Event of Default)", "Section 365 protections; no ipso "
            "facto termination; New Lease survives rejection (§ 9.8)", "M"],
           ["8", "Percentage rent", "Breakpoint fixed at $28,500,000 for the Term", "Breakpoint indexed at each Rent "
            "Reset to preserve the Year 6 ratio (§ 5.3)", "M"],
           ["9", "Tax abatement", "Period commences on the Lease Commencement Date", "Period commences on the later of "
            "Rent Commencement and the first assessment reflecting the completed Improvements; rent credit backstop "
            "(§§ 6.7–6.8)", "M"],
           ["10", "Remediation overruns", "Tenant bears all costs above $2,400,000", "Landlord bears overruns "
            "attributable to undisclosed or undelineated Pre-Existing Environmental Conditions; Landlord indemnity "
            "(§§ 7.4(c), 7.5)", "M"],
           ["11", "Bulkhead", "Not addressed", "Landlord funds the structural assessment; alternative repair "
            "allocation with rent credit (§§ 2.9(b), 14.3)", "M"],
           ["12", "Tenant extension option", "\"No renewal options are contemplated\"", "One 25-year extension at "
            "Tenant's option (§ 2.7, bracketed); note this exceeds the 99-year cap in Resolution § 4(b)", "M"],
           ["13", "Milestone extensions", "12 mo. FM + 6 mo. permitting; nothing for Landlord delay",
            "Adds uncapped Landlord Delay and optional paid extensions (§ 3.4)", "M"],
           ["14", "ROFR", "Applies to any non-Affiliate assignment in first 20 years", "Direct assignments for value "
            "only; broad Permitted Transfers; mortgagee carve-outs; lapse on failed closing; recorded Declaration to "
            "be amended (§§ 11.3, 11.5)", "M"],
           ["15", "Rent amounts", "$3,224,500 / $3,648,200", "$3,224,513 / $3,648,241 (recomputed from 2.5% "
            "compounding)", "I"],
           ["16", "CPI base month", "From the Lease Commencement Date", "From the Rent Commencement Date (§ 4.4(b))",
            "I"],
           ["17", "Rent reset mechanic", "Ten-year resets off the original Base Rent", "Unchanged, but a bracketed "
            "annual CPI alternative with a 0–4% collar is proposed (§ 4.4, note)", "M"],
           ["18", "Setoff", "\"Without setoff\" (§ 5) but Tenant may offset (§ 16)", "Express limited setoff rights "
            "with notice to mortgagees (§ 4.6)", "I"],
           ["19", "Flood insurance", "NFIP maximum", "NFIP maximum plus excess/DIC to full replacement cost "
            "(§ 12.1(f))", "I"],
           ["20", "LOC issuer", "A-/A3 bank (or, per Board recital, federally chartered bank)", "Either test (§ 8.3); "
            "cash deposit at Tenant's option (§ 8.2)", "I"],
           ["21", "Occupancy measurement", "\"Overall occupancy rate of 90%\"", "Defined RSF-based test with "
            "certification and deemed-approval mechanics (§ 8.4)", "I"],
           ["22", "Condominium conversion", "Rent only; \"no condominiums or cooperative units\"", "Conversion "
            "permitted if it does not alter Landlord's rights or reversion (§ 15.2)", "M"],
           ["23", "Remediation credit survival", "Silent", "Unapplied credit paid in cash on early termination "
            "(§ 7.2)", "I"],
           ["24", "Venue", "\"Judicial District of Port Calloway\"", "Judicial District of New Haven; mediation first "
            "(§ 20.2)", "I"],
           ["25", "Title and survey corrections", "Mechanics' lien listed as a Permitted Exception",
            "Lien discharged at Landlord's cost; legal description conformed to the survey; both conditions precedent "
            "(§§ 2.3, 2.9(a), 16.2)", "I — but gating"]],
          [0.3, 1.15, 1.75, 2.4, 0.4], size=6.5)
    body(doc, "Our recommendation is to transmit this schedule with the draft, with a cover note from us explaining "
              "that items 1–5, 8–11 and 14 are responsive to the requirements of the construction lender and that items "
              "1–3 are also responsive to the Authority's interest in an enforceable remedy. See Part 10.")

    # ================= PART 10 =================
    h1(doc, "Part 10 — Negotiation strategy", "10")
    h2(doc, "10.1  Must-haves (walk-away if refused)", "10.1")
    bullet(doc, "**Compensation for improvements on any reverter** (§ 10.6) — your stated non-negotiable, and the "
                "condition to the loan.")
    bullet(doc, "**Lender cure periods and New Lease** (§§ 9.5, 9.6) — without these the loan does not close, "
                "whatever the rest of the document says.")
    bullet(doc, "**A conformed legal description and a discharge of the mechanics' lien** (§§ 2.3, 16.2) — title "
                "cannot issue otherwise.")
    bullet(doc, "**An amendment of the recorded ROFR** to carve out mortgagee enforcement (§ 11.5) — a recorded "
                "instrument cannot be overridden by contract.")
    bullet(doc, "**A tax abatement backstop** (§ 6.8) — the Authority is not the taxing authority, so a covenant alone "
                "is not enough.")
    h2(doc, "10.2  Strong preferences (trade only against something real)", "10.2")
    bullet(doc, "Breakpoint indexation (§ 5.3) — trade against a higher Percentage Rent rate if pressed, or accept "
                "CPI-only indexation as a fallback.")
    bullet(doc, "Abatement commencement re-anchoring (§ 6.7) — this is the highest-value item that the Authority will "
                "frame as impossible; it may need City cooperation and therefore time.")
    bullet(doc, "Environmental overrun allocation and indemnity (§§ 7.4(c), 7.5) — a 50/50 sharing above $2.4 million "
                "is an acceptable landing zone.")
    bullet(doc, "Bulkhead allocation (§§ 2.9(b), 14.3) — get the assessment first; the number will do the arguing.")
    bullet(doc, "Extension option (§ 2.7) — valuable but not worth the transaction; drop it if the Board resists.")
    h2(doc, "10.3  Tradeables (give these if needed)", "10.3")
    body(doc, "The recomputed rent amounts (Part 2.1 items 3–4 — a $54 per annum point); the CPI base-month correction "
              "(item 16); the setoff mechanics; the flood insurance enhancement (we would not concede this, since it "
              "protects Bayside, but we can let it be framed as a lender requirement rather than a Tenant ask); the "
              "condominium conversion right; and the paid-extension mechanic, which is a concession to Tenant that "
              "costs the Authority nothing if Tenant never uses it and pays the Authority if it does.")
    h2(doc, "10.4  Sequencing", "10.4")
    body(doc, "Send the draft and this schedule to Mr. Koss with the loan-driven items identified as lender "
              "requirements, not Tenant preferences. That framing is accurate — Bayside § 5 requires most of them — and "
              "it moves the argument from \"the tenant wants more\" to \"the deal does not fund without this.\" Then "
              "schedule a joint call with Authority counsel and Bayside's counsel in the same week, so that the "
              "Authority hears the lender's requirements from the lender. We should not negotiate the reverter with "
              "Authority counsel alone and then have to re-open it when Bayside's redline arrives.")

    # ================= PART 11 =================
    h1(doc, "Part 11 — Timeline to October 1, 2025", "11")
    table(doc,
          [["Date", "Milestone", "Owner"],
           ["June 20, 2025", "Draft Lease and this memorandum delivered to you", "Hargrove & Linden"],
           ["June 23–27, 2025", "Your review and instructions on the bracketed items (Part 11 note below)",
            "Meridian"],
           ["June 27, 2025", "Confirm Bayside term sheet execution status (Bayside § 12 expiration)", "Meridian"],
           ["June 29, 2025", "Target delivery of the Draft Lease to Howard Koss with the deviation schedule",
            "Hargrove & Linden"],
           ["Week of June 30", "Joint call with Authority counsel and Bayside counsel on Article 9 and the reverter",
            "All"],
           ["July 7–18, 2025", "Request survey re-certification / update (90-day window expires July 19); request "
            "DEEP pre-application meeting on the ELUR ground-floor question", "Meridian / Halcyon"],
           ["July 2025", "First redline from Pryor Whitfield & Koss; Bayside checklist redline", "Authority / Bayside"],
           ["August 2025", "Negotiate Articles 6, 7 and 10 (tax abatement, environmental, reverter); confirm City "
            "authority for the abatement with municipal finance counsel", "All"],
           ["August 2025", "Obtain the bulkhead structural assessment and price the repair", "Authority"],
           ["Early September", "Circulate the execution version to the Authority Board package; request a special "
            "meeting date", "Authority / Hargrove & Linden"],
           ["Mid-September", "Board resolution approving the definitive lease (Term Sheet § 15(g)) and the recorded "
            "ROFR amendment", "Authority Board"],
           ["Late September", "Title: conformed commitment, lien discharged, policies marked to issue; SNDA executed "
            "and recorded", "Ridgepoint / all"],
           ["October 1, 2025", "Lease Commencement Date; Memorandum of Lease recorded; Letter of Credit delivered",
            "All"]],
          [1.1, 3.9, 1.5], size=7.5)
    flagbox(doc, "The critical path is not the drafting.",
             "It is the Authority Board calendar and the City's tax abatement approval. Resolution No. 2025-047 is an "
             "authorization to negotiate and execute a lease substantially consistent with the Term Sheet; Term Sheet "
             "§ 15(g) separately requires approval of the definitive lease by the Board at a properly noticed public "
             "meeting, and Resolution § 4(d) requires Board review of material deviations. You should assume **two** "
             "Board actions are required — one for the lease and one for the recorded ROFR amendment — and that the "
             "City must act separately on the abatement agreement. On a municipal calendar that is four to six weeks "
             "before October 1. Our recommendation is that we ask Mr. Koss this week to reserve a special meeting date "
             "in the second week of September.")
    body(doc, "**Five dollar amounts are left blank in the Draft Lease**, each marked \"$[\u25cf]\" and each "
              "requiring your instruction or a negotiated number: (i) the fee for Tenant's optional 6-month milestone "
              "extensions (\u00a7 3.4(d)); (ii) the cap on Tenant's environmental indemnity (\u00a7 7.6); (iii) the "
              "minimum capital and surplus of a federally chartered letter-of-credit issuer, if that alternative is "
              "used (\u00a7 8.3); (iv) the net-worth qualification for a foreclosure transferee (\u00a7 9.7); and "
              "(v) the threshold above which alterations in the final ten years of the Term require consent "
              "(\u00a7 14.6). We have not inserted numbers because each is a business judgment, and because the "
              "Authority will want to negotiate each of them.")
    body(doc, "**Items requiring your decision before we send the draft.** (i) Do you want us to keep the bracketed "
              "25-year extension option in Section 2.7, given that it exceeds the 99-year cap in Resolution § 4(b) and "
              "will itself require Board action? (ii) Do you accept the recomputed rent figures ($3,224,513 and "
              "$3,648,241) or should we adopt the Term Sheet's rounded amounts? (iii) Do you want us to press for a "
              "16–17 foot finished floor elevation now rather than 15 feet? (iv) Are you comfortable with the 24-month "
              "Base Rent cap on Documented Damages, or should we propose a lower number (e.g., 12 months) to make the "
              "proportionality argument even stronger at the cost of some negotiating room? (v) Do you want us to "
              "include the cash-security-deposit alternative (Bayside permits it; the Term Sheet does not)?")
