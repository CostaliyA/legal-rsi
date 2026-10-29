from memo_helpers import *

def blocks(doc):
    # ---------- MEMO HEADER ----------
    runs(doc.add_paragraph(), "HARGROVE & LINDEN LLP", bold=True, size=13)
    p = doc.add_paragraph(); p.paragraph_format.space_after = Pt(2)
    runs(p, "1100 Constitution Avenue, Hartford, Connecticut 06103", size=8.5, italic=True)
    p = doc.add_paragraph(); p.paragraph_format.space_after = Pt(14)
    runs(p, "PRIVILEGED AND CONFIDENTIAL  •  ATTORNEY–CLIENT COMMUNICATION  •  ATTORNEY WORK PRODUCT  •  "
            "PREPARED IN ANTICIPATION OF LITIGATION", bold=True, size=8)
    pPr = p._p.get_or_add_pPr()
    pbdr = OxmlElement("w:pBdr")
    for side in ("top", "bottom"):
        e = OxmlElement("w:" + side)
        e.set(qn("w:val"), "single"); e.set(qn("w:sz"), "12"); e.set(qn("w:space"), "4"); e.set(qn("w:color"), "000000")
        pbdr.append(e)
    pPr.append(pbdr)

    rows = [
        ("TO:", "Marcus Ellison, Managing Member — Meridian Gateway Holdings LLC"),
        ("CC:", "Ansel Coventry III, Managing Partner — Coventry Capital Partners LP"),
        ("FROM:", "Rebecca Tsang, Lead Partner  •  Jordan Abernathy, Associate Counsel"),
        ("DATE:", "June 20, 2025"),
        ("RE:", "Drafting Issues Memorandum — Long-Term Ground Lease, 10–30 Pier Street, Port Calloway, CT "
                "(APN 127-003-0045); Issues, Conflicts and Gaps Across the Term Sheet, Title Commitment, Phase II "
                "Environmental Site Assessment, Construction Loan Term Sheet and Survey"),
    ]
    t = doc.add_table(rows=len(rows), cols=2)
    t.autofit = False
    tblPr = t._tbl.tblPr
    lay = OxmlElement("w:tblLayout"); lay.set(qn("w:type"), "fixed"); tblPr.append(lay)
    tw = OxmlElement("w:tblW"); tw.set(qn("w:type"), "dxa"); tw.set(qn("w:w"), str(int(6.5 * 1440))); tblPr.append(tw)
    t.columns[0].width = Inches(0.85); t.columns[1].width = Inches(5.65)
    for i, (a, b) in enumerate(rows):
        c0, c1 = t.cell(i, 0), t.cell(i, 1)
        c0.width = Inches(0.85); c1.width = Inches(5.65)
        c0.text = ""; c1.text = ""
        pa = c0.paragraphs[0]; pb = c1.paragraphs[0]
        for pp in (pa, pb):
            pp.paragraph_format.space_after = Pt(3)
        runs(pa, a, bold=True, size=9.5)
        runs(pb, b, size=9.5)
    doc.add_paragraph().paragraph_format.space_after = Pt(6)

    body(doc, "We have prepared the attached first draft of the Ground Lease Agreement (the \"**Draft Lease**\") for "
              "delivery to Howard Koss at Pryor Whitfield & Koss LLP. This memorandum accompanies that draft. It "
              "records every issue, conflict and gap we identified across the source documents, sets out our "
              "independent recomputation of every figure used in the Draft Lease, identifies the provisions of the "
              "Draft Lease that respond to each issue, and lists the open items that require your decision, a third "
              "party's action, or further legal research before we can deliver or finalize the draft.")

    # ---------- 1. PURPOSE / SCOPE ----------
    h1(doc, "Purpose, scope and sources reviewed", "1")
    body(doc, "1.1  **Purpose.** You asked for two things: a first draft of the ground lease, and a memorandum "
              "identifying \"any issues, conflicts, or gaps\" across the term sheet, the title commitment, the Phase II "
              "ESA and the Bayside loan term sheet. This memorandum is the second of those; the Draft Lease is the "
              "first. We have also responded to the specific instructions in your June 15 email (reverter and "
              "improvement forfeiture; percentage rent; tax abatement timing; remediation credit mechanics; security "
              "deposit step-down; affordable housing; milestones and force majeure; assignment/ROFR). Where your "
              "instructions required a change to the negotiated Term Sheet, the change is flagged in the Draft Lease "
              "and catalogued in Part 9 below, because each such change requires Landlord Board action under "
              "Resolution No. 2025-047, § 4(d).")
    body(doc, "1.2  **Sources reviewed.** We reviewed each of the following in full. Appendix 1 is a source-to-issue "
              "log recording where each material proposition, figure, date and obligation appears.")
    table(doc,
          [["#", "Document", "Date / Reference", "Used for"],
           ["1", "Client instructions email (M. Ellison to R. Tsang)", "June 15, 2025, 09:47", "Client priorities, "
            "business parameters, negotiation instructions"],
           ["2", "Executed binding term sheet (Term Sheet)", "June 10, 2025", "Deal terms; the baseline against which "
            "the Draft Lease is measured"],
           ["3", "Construction loan term sheet (Bayside)", "May 28, 2025", "Required ground lease provisions "
            "(§ 5.1–5.7); closing conditions (§ 6)"],
           ["4", "Title commitment TC-2025-07821 (Ridgepoint)", "Effective June 1, 2025", "Title, Schedule B-I "
            "requirements, Schedule B-II exceptions, recorded instruments"],
           ["5", "Phase II ESA executive summary (Halcyon HEC-2025-0412)", "May 2, 2025", "Environmental conditions, "
            "ELUR interpretation, remediation scope and cost"],
           ["6", "ALTA/NSPS survey narrative and legal description (CLS-2025-0417)", "Field April 20, 2025; plat "
            "April 28, 2025", "Premises description, easements, topography, legal description"],
           ["7", "Board Resolution No. 2025-047", "Adopted June 5, 2025", "Landlord's authority; limits on delegated "
            "authority"]],
          [0.3, 2.05, 1.55, 2.6], size=8)
    body(doc, "1.3  **What we did not have.** We did not have, and the Draft Lease assumes the existence of, the "
              "following. Their absence is itself a finding, and they are itemized in Part D: the Phase I ESA (only "
              "referenced); the full Phase II report and appendices (A–J, including boring logs, laboratory data and "
              "the ELUR text); the ELUR instrument itself; the 2019 Declaration of Right of First Refusal; the 2019 "
              "Declaration of Restrictive Covenants; the survey plat (Sheets 1 and 2) and the survey referenced in the "
              "title commitment (CLS-2025-0321); the Bayside loan documents and commitment letter; the Coventry "
              "preferred equity documentation; any zoning or site-plan determination; and any DEEP correspondence "
              "regarding the ELUR or the pending LUST file.")
    body(doc, "1.4  **Method and conventions.** We extracted every figure, date, period, threshold and cross-reference "
              "from the record and recomputed each one independently (Part 2 and Appendix 3). We recomputed the two "
              "competing legal descriptions by traverse and shoelace computation (Part 3.1). We read the Draft Lease "
              "against the Bayside requirements line by line (Part 4.2). We have separated: (a) facts extracted from "
              "the record; (b) our computations; (c) legal characterizations; (d) open questions; and (e) "
              "recommendations. Where we characterize law, we say so and we identify whether it has been verified. "
              "**Nothing in this memorandum is a substitute for the independent legal research identified in Part 7, "
              "which we have not completed.**")

    # ---------- 2. EXECUTIVE SUMMARY ----------
    h1(doc, "Executive summary and top-risk register", "2")
    body(doc, "2.1  **Bottom line.** The transaction is financeable in its current structure only if five things are "
              "fixed before the Draft Lease is negotiated: (i) the reverter/forfeiture provision; (ii) the lender "
              "protection package, which as drafted in the Term Sheet does not satisfy Bayside's § 5 conditions; "
              "(iii) the legal description, which as stated in the title commitment describes a parcel approximately "
              "twice the size of the Premises; (iv) the mechanics' lien, which the title company will not insure over "
              "and which the Term Sheet wrongly treats as a Permitted Exception; and (v) the recorded right of first "
              "refusal, which by its recorded terms contains no carve-out for leasehold mortgagee enforcement. Items "
              "(iii), (iv) and (v) are gating: without them, no leasehold title policy issues and the Bayside loan "
              "cannot close, whatever the business terms say.")
    body(doc, "2.2  **Top-risk register.** The table below is risk-prioritized. Severity reflects the risk to Meridian "
              "(economic exposure, closing risk, or financing risk), not the difficulty of the fix.")
    table(doc,
          [["#", "Risk", "Why it matters", "Sev.", "Draft Lease §"],
           ["1", "Reverter/forfeiture: on a missed milestone the Authority takes $200–300M of improvements and keeps "
            "the $5.7M deposit, with no compensation", "Exposure of $205.7M–$305.7M. Bayside will not lend against "
            "it. Likely unenforceable as a penalty, but that is not a financing strategy", "Critical",
            "§§ 10.5, 10.6, 10.7, 10.9; Art. 9"],
           ["2", "Term Sheet lender protections do not meet Bayside § 5.1–5.7", "Five of seven requirements are not "
            "addressed; none is fully satisfied. Each is a condition precedent to loan closing", "Critical",
            "Art. 9 (§§ 9.1–9.11); Ex. F"],
           ["3", "Legal description error in title commitment", "Stated courses enclose ~279,535 SF (6.42 ac) against "
            "a recited 3.2 ac; traverse miscloses 1.10 ft. Title cannot issue; $/SF rent basis is unsupported",
            "Critical", "§ 2.3(b); § 16.2; Ex. A; Ex. G"],
           ["4", "Mechanics' lien ($187,500, Calloway Marine Demolition)", "Title Requirement 7 bars any policy until "
            "discharged; Term Sheet § 13 wrongly lists it as a Permitted Exception; Bayside § 6(c) bars unapproved "
            "exceptions", "High", "§ 2.3(h); § 2.9(a); § 16.2; Ex. B, Part 6"],
           ["5", "Recorded ROFR (Vol. 405, Pg. 55) has no mortgagee carve-out", "A recorded instrument cannot be "
            "overridden by a lease term; blocks foreclosure, deed-in-lieu and New Lease transfers during the first 20 "
            "years", "High", "§ 11.5 and drafting flag; Ex. B, Part 4"],
           ["6", "Percentage rent: Breakpoint fixed at $28.5M for 99 years", "Erodes from 8.84x Base Rent in Year 6 to "
            "0.96x by Year 96 — becomes a gross-receipts tax, exactly the outcome you flagged", "High",
            "§ 5.3 and drafting flag; Ex. D"],
           ["7", "Tax abatement: delivered by the City, not the Authority; period starts on Lease Commencement Date",
            "3 construction years consumed before rent commences; no enforceable backstop; statutory authority "
            "unverified", "High", "§§ 6.6–6.9; § 2.3(f)"],
           ["8", "ELUR prohibits ground-floor residential use; project program includes ground-floor lobby, amenity "
            "and leasing space", "DEEP enforcement risk and a permitting risk that could delay Milestone 1; "
            "unresolved in the record", "High", "§ 7.8; § 14.5; § 15.2"],
           ["9", "Remediation overrun risk uncapped and estimate likely understated", "Tenant bears all costs above "
            "$2.4M; below-grade parking could generate 7,000–27,000 CY of additional excavation against a 1,533 CY "
            "contaminated-soil estimate", "High", "§ 7.4; § 7.5"],
           ["10", "Bulkhead in \"fair to poor\" condition, cost unquantified and unallocated", "Structural and cost "
            "risk sits with Tenant under a triple-net lease and again at surrender; survey notes 40 LF of cap already "
            "removed", "High", "§ 2.9(b); § 14.3"],
           ["11", "Survey is stale and title commitment expires before closing", "Bayside § 6(d) requires a survey "
            "dated within 90 days of closing (survey date + 90 days = July 19, 2025); commitment expires Dec. 1, 2025",
            "Med.", "§ 2.3(b), (c)"],
           ["12", "Security deposit step-down undefined; LOC issuer conflict between Term Sheet and Board Resolution",
            "\"90% occupancy\" is not defined for a mixed-use project; the Board recital requires a federally chartered "
            "bank", "Med.", "§§ 8.3–8.4"],
           ["13", "Material deviations from the Term Sheet require Board action", "Resolution No. 2025-047, § 4(d) "
            "requires Board review of any deviation deemed material; several of our changes are", "High",
            "Part 9 (deviation schedule)"],
           ["14", "Financing term mismatch", "Loan matures at 48 months (60 with extensions) but Milestone 3 is at 60 "
            "months and Milestone 4 at 84; Coventry's completion guaranty runs to the initial maturity", "Med.",
            "Part 6.13"],
           ["15", "Assignment/recapitalization constraints", "ROFR plus consent regime could impede Coventry's "
            "liquidity path and the 100% membership-interest pledge Bayside requires", "Med.",
            "§§ 11.1–11.7"]],
          [0.34, 1.72, 2.6, 0.55, 1.28], size=7.5)
    body(doc, "2.3  **What is not a problem.** Several items you flagged as concerns are, on our recomputation, "
              "internally consistent and should not consume negotiating capital: the initial Base Rent and per-square-"
              "foot rate (Part 2.1, item 1); the security deposit and step-down amounts (items 7–8); the remediation "
              "credit waterfall (item 9); the tax abatement percentages and dollar amounts (item 11); and the "
              "milestone dates (item 15). The dollar amounts in the Term Sheet are, with two immaterial exceptions, "
              "arithmetically correct.")
    body(doc, "2.4  **A note on tone.** Because this is a first draft to opposing counsel, the Draft Lease is drafted "
              "from Tenant's side but is intended to be negotiable rather than maximal: it retains the Authority's "
              "reverter concept (with compensation), retains the ROFR (narrowed), retains the affordable housing "
              "covenant and the public open space obligation, and does not seek to reduce Base Rent or the Percentage "
              "Rent rate. The provisions most likely to be characterized by Mr. Koss as \"not substantially consistent "
              "with the Term Sheet\" are catalogued in Part 9 with a suggested framing for each.")
