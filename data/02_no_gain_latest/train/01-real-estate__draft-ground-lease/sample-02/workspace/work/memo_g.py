from memo_helpers import *

def blocks(doc):
    pagebreak(doc)
    cover_line(doc, "APPENDIX 1", size=12, bold=True, space_after=4)
    cover_line(doc, "SOURCE-TO-ISSUE LOG", size=11, bold=True, space_after=10)
    body(doc, "Each material proposition, figure, date and obligation relied on in this memorandum and in the Draft "
              "Lease, with the document and location from which it was taken. \"TS\" = Term Sheet (June 10, 2025); "
              "\"BL\" = Bayside construction loan term sheet (May 28, 2025); \"TC\" = Title Commitment TC-2025-07821; "
              "\"P2\" = Phase II ESA executive summary (May 2, 2025); \"SV\" = survey narrative CLS-2025-0417; "
              "\"BR\" = Board Resolution No. 2025-047; \"CI\" = client instructions (June 15, 2025).", size=9)
    rows = [
        ["Parties, addresses, EIN, formation date", "TS § 1; BL § 1; TC Sched. A § 4"],
        ["Authority's enabling statute (CGS § 8-125)", "TS § 1; BR preamble; TC Sched. A § 4"],
        ["Premises: 10–30 Pier Street; APN 127-003-0045; ~3.2 ac / 139,392 SF", "TS § 2; P2 § 2.1; SV § 1; BR recitals"],
        ["Waterfront location; 480 LF of bulkhead", "TS § 2; P2 § 2.1; SV §§ 1, 3(b)"],
        ["FEMA Zone AE; BFE 12 ft NAVD88; FFE 15 ft NAVD88", "TS § 2; P2 § 5; TC Ex. 9; SV § 2; BL § 6(l)"],
        ["Lease term 99 years; expiration Sept. 30, 2124", "TS § 3; TC Sched. A § 3; BR § 1"],
        ["Rent Commencement = earlier of 36 months or first CO", "TS § 3"],
        ["No renewal options", "TS § 3"],
        ["Project program: 28-story tower, 6-story office, retail, parking", "TS § 4; P2 § 2.3 (Client note); BL § 1"],
        ["Ground-floor residential lobby and amenity spaces", "TS § 4(a)"],
        ["8,000 SF public open space", "TS § 4; BR § 2(e); BL § 1"],
        ["15% affordable at 80% AMI for the term", "TS § 4; BR § 2(b); TC Ex. 5; BL § 1, § 7(f)"],
        ["ELUR recorded Mar. 22, 2018, Vol. 412, Pg. 88", "TS § 4, § 7; TC Ex. 1; P2 § 2.3; SV § 3(c); BL § 6(e)"],
        ["Initial Base Rent $2,850,000; $237,500/month; $20.45/SF", "TS § 5"],
        ["2.5% escalation; $3,224,500 / $3,648,200", "TS § 5"],
        ["CPI resets at Lease Years 16–96; greater of formula", "TS § 5"],
        ["Percentage Rent 2.0%; Breakpoint $28,500,000; from Lease Year 6", "TS § 6; BR recital (b)"],
        ["Gross Revenues definition and exclusion placeholder", "TS § 6"],
        ["Audit right; 5% threshold; 3-year retention", "TS § 6"],
        ["Phase II: Area 1 4,200 SF, max TPH 3,800 mg/kg; Area 2 1,600 SF, max 1,200 mg/kg; RDEC 500 mg/kg",
         "TS § 7; P2 §§ 4.1–4.2, 7"],
        ["Remediation estimate $2,400,000 ($1,850,000 / $550,000)", "TS § 7; P2 § 6"],
        ["Remediation credit $1,800,000; Tenant bears $600,000 and all overruns", "TS § 7; P2 § 6 (Allocation Note)"],
        ["Contingency lines stated as 10% ($100,000 / $25,000)", "P2 § 6 (cost tables)"],
        ["ELUR ambiguity re non-habitable ground-floor space; recommend DEEP clarification", "P2 § 2.3 (Important "
         "Note), § 7 rec. 2"],
        ["ELUR: no potable wells; annual compliance certification; 30-day breach notice; 90-day repair",
         "P2 § 2.3(b)–(d); TC Ex. 1"],
        ["Bulkhead fair-to-poor; 40 LF of cap removed; repair excluded from estimate", "P2 § 5; SV § 3(d)(iii)"],
        ["Freeboard recommendation 4–5 ft; PA 23-167; CIRCA projections; Nov. 2024 flooding at 10.5 ft",
         "P2 § 5, § 7 rec. 5; SV § 2 (surveyor's note)"],
        ["Security deposit $5,700,000; step-down to $2,850,000 at 90% occupancy for 24 months", "TS § 8; BR recital "
         "(c); BL § 4"],
        ["Milestones 1–4 and dates", "TS § 9; BR § 2(a)"],
        ["Force majeure 12 months; permitting 6 months; aggregate 18 months", "TS § 9"],
        ["Reverter: automatic termination; deposit forfeiture; improvements without compensation", "TS § 9"],
        ["Term Sheet lender protections (mortgage, SNDA, New Lease, notices, no surrender, foreclosure)",
         "TS § 9; BL § 5.1–5.7"],
        ["Bayside cure periods 60/90 days; non-concurrent; simultaneous notices", "BL § 5.4"],
        ["Bayside bankruptcy protections", "BL § 5.7"],
        ["Triple net; current assessment $4,200,000; mill rate 34.75; $145,950", "TS § 10; TC Ex. 7"],
        ["Projected assessment $178,000,000; $6,185,500 at full", "TS § 10; BR recital"],
        ["Abatement 25/50/75% for 15 years, commencing Lease Commencement Date", "TS § 10; BR recital"],
        ["Abatement implemented by separate agreement with the City", "BR § 3(d)"],
        ["Assignment consent; subletting; ROFR first 20 years; Affiliate definition", "TS § 11; TC Ex. 4"],
        ["Recorded ROFR Declaration Sept. 8, 2019, Vol. 405, Pg. 55, without mortgagee carve-outs", "TC Ex. 4"],
        ["Recorded affordable covenant Nov. 15, 2019, Vol. 408, Pg. 230, with six gaps", "TC Ex. 5"],
        ["Insurance: CGL $10M/$20M; all-risk; builder's risk; NFIP flood; environmental $5M/$10M; WC", "TS § 12; BL "
         "§ 6(h)"],
        ["Permitted Exceptions list (10 items)", "TS § 13; TC Sched. B-II"],
        ["Mechanics' lien $187,500, Apr. 3, 2025, Vol. 418, Pg. 302", "TS § 13; TC Ex. 6 and Req. 7; SV § 3(d)(iii)"],
        ["Loan $285M; SOFR + 275; 48 months + two 6-month extensions", "TS § 14; BL § 2"],
        ["Equity: Coventry $95M; Meridian $45M; total $425M", "TS § 14; BL § 3"],
        ["Cost allocation: hard $352M; soft $38.5M; contingency $34.5M", "TS § 14; BL § 3"],
        ["Coventry completion guaranty to Initial Maturity Date", "BL § 4"],
        ["Conditions precedent to lease commencement", "TS § 15"],
        ["Default and remedies summary; reverter available on any Event of Default", "TS § 16"],
        ["Casualty/condemnation summary; award allocation", "TS § 17"],
        ["End of term: improvements to Landlord without compensation; last-10-year alteration restriction", "TS § 18"],
        ["Governing law; mediation; Judicial District of Port Calloway; FOIA; exclusivity to Dec. 31, 2025",
         "TS § 19"],
        ["Resolution authority; rent floor; 99-year cap; affordable floor; material deviation rule",
         "BR §§ 1, 2, 4"],
        ["Title commitment expiration Dec. 1, 2025; requirements 1–8", "TC Conditions, Sched. B-I"],
        ["Survey: CLS-2025-0417; Pellegrino PLS-008741; Table A items; certification to four parties", "SV cover, § 5"],
        ["Survey referenced in title: CLS-2025-0321; Ferreira PLS 12847; rev. May 15, 2025", "TC Sched. A § 5; Ex. A"],
        ["Condemnation: 2012; Vol. 367 Pg. 44 (TC) / Vol. 375 Pg. 44 (SV); New Haven (TC) / Port Calloway (TS)",
         "TS § 2; TC Sched. A § 4, Ex. 10; SV § 4"],
        ["Client priorities: reverter, financeability, abatement, percentage rent, remediation, deposit, affordable, "
         "milestones, assignment", "CI §§ 1–5"],
        ["Total project cost $425M; client's improvement value estimate $200–300M at Milestone 3", "CI § 1, § 2"],
    ]
    table(doc, [["Proposition / figure", "Source"]] + rows, [4.3, 2.2], size=6.5)

    pagebreak(doc)
    cover_line(doc, "APPENDIX 2", size=12, bold=True, space_after=4)
    cover_line(doc, "PERCENTAGE RENT AND RENT RESET MODELS", size=11, bold=True, space_after=10)
    body(doc, "**A2.1  Breakpoint erosion.** Base Rent escalated at the 2.5% floor; Breakpoint fixed at $28,500,000; "
              "\"Year-1 dollars\" deflate nominal amounts at the same 2.5% for comparability.", size=9.5)
    table(doc,
          [["Lease Yr", "Base Rent (2.5% floor)", "Breakpoint", "Breakpoint ÷ Base Rent", "Breakpoint (Yr-1 $)",
            "Base Rent (Yr-1 $)"],
           ["6", "3,224,513", "28,500,000", "8.84×", "25,189,847", "2,850,000"],
           ["16", "4,127,650", "28,500,000", "6.90×", "19,678,268", "2,850,000"],
           ["26", "5,283,741", "28,500,000", "5.39×", "15,372,632", "2,850,000"],
           ["36", "6,763,635", "28,500,000", "4.21×", "12,009,075", "2,850,000"],
           ["46", "8,658,024", "28,500,000", "3.29×", "9,381,471", "2,850,000"],
           ["56", "11,083,003", "28,500,000", "2.57×", "7,328,790", "2,850,000"],
           ["66", "14,187,181", "28,500,000", "2.01×", "5,725,239", "2,850,000"],
           ["76", "18,160,791", "28,500,000", "1.57×", "4,472,547", "2,850,000"],
           ["86", "23,247,348", "28,500,000", "1.23×", "3,493,947", "2,850,000"],
           ["96", "29,758,571", "28,500,000", "0.96×", "2,729,466", "2,850,000"]],
          [0.7, 1.25, 1.05, 1.1, 1.2, 1.2], size=7.5, align_right=[1, 2, 3, 4, 5])
    body(doc, "Observation: the real value of the Breakpoint falls below the Year-1 Base Rent in nominal terms by "
              "Lease Year 86 and in real terms far earlier. A fixed breakpoint in a 99-year lease is a transfer of "
              "value, not a sharing of upside.", size=9.5)
    body(doc, "**A2.2  Reset step sensitivity.** Base Rent under Section 4.4 is flat within each ten-year band and "
              "steps to the full cumulative index at each Rent Reset Date. The step at Lease Year 16, for a range of "
              "long-run CPI assumptions:", size=9.5)
    table(doc,
          [["Long-run CPI", "Lease Yr 15 Base Rent", "Lease Yr 16 Base Rent", "Step"],
           ["2.0%", "3,648,241", "3,835,725", "+5.1%"],
           ["2.5%", "3,648,241", "4,127,650", "+13.1%"],
           ["3.0%", "3,648,241", "4,440,128", "+21.7%"],
           ["3.5%", "3,648,241", "4,774,744", "+30.9%"],
           ["4.5%", "3,648,241", "5,515,555", "+51.2%"]],
          [1.1, 1.6, 1.6, 0.9], size=8, align_right=[1, 2, 3])
    body(doc, "After Lease Year 16, each subsequent reset produces a further step equal to ten years of index growth "
              "(28.0% at 2.5% CPI), because the formula recomputes from the original Base Rent rather than "
              "compounding the then-current rent.", size=9.5)
    body(doc, "**A2.3  Percentage Rent illustrations** (Breakpoint $28,500,000; rate 2.0%)", size=9.5)
    table(doc,
          [["Lease Yr", "Gross Revenues", "Breakpoint", "Excess", "Percentage Rent", "% of Base Rent"],
           ["6", "30,000,000", "28,500,000", "1,500,000", "30,000", "0.9%"],
           ["6", "40,000,000", "28,500,000", "11,500,000", "230,000", "7.1%"],
           ["6", "60,000,000", "28,500,000", "31,500,000", "630,000", "19.5%"],
           ["6", "90,000,000", "28,500,000", "61,500,000", "1,230,000", "38.1%"],
           ["96 (fixed BP)", "60,000,000", "28,500,000", "31,500,000", "630,000", "2.1%"],
           ["96 (indexed BP)", "60,000,000", "262,986,000", "nil", "nil", "nil"]],
          [0.8, 1.2, 1.2, 1.15, 1.1, 1.05], size=7.5, align_right=[1, 2, 3, 4, 5])

    pagebreak(doc)
    cover_line(doc, "APPENDIX 3", size=12, bold=True, space_after=4)
    cover_line(doc, "RECOMPUTATION SCHEDULES", size=11, bold=True, space_after=10)
    body(doc, "**A3.1  Base Rent and monthly installments**", size=9.5)
    table(doc,
          [["Lease Years", "Formula", "Annual", "Monthly"],
           ["1–5", "$2,850,000", "$2,850,000.00", "$237,500.00"],
           ["6–10", "$2,850,000 × 1.025^5", "$3,224,513.41", "$268,709.45"],
           ["11–15", "$2,850,000 × 1.025^10", "$3,648,240.95", "$304,020.08"]],
          [1.0, 2.0, 1.6, 1.4], size=8, align_right=[2, 3])
    body(doc, "**A3.2  Tax schedule** (mill rate 34.75; projected assessed value $178,000,000)", size=9.5)
    table(doc,
          [["Phase", "Percentage of assessed value", "Assessed value subject to tax", "Annual tax",
            "Annual saving vs full"],
           ["Years 1–5", "25%", "$44,500,000", "$1,546,375", "$4,639,125"],
           ["Years 6–10", "50%", "$89,000,000", "$3,092,750", "$3,092,750"],
           ["Years 11–15", "75%", "$133,500,000", "$4,639,125", "$1,546,375"],
           ["Year 16+", "100%", "$178,000,000", "$6,185,500", "nil"],
           ["**15-year total**", "—", "—", "**$46,391,250 in savings**", "—"]],
          [0.95, 1.3, 1.5, 1.2, 1.15], size=8, align_right=[2, 3, 4])
    body(doc, "**A3.3  Remediation cost — stated vs. recomputed**", size=9.5)
    table(doc,
          [["Item", "Area 1", "Area 2", "Combined"],
           ["Excavation and soil management", "$680,000", "$210,000", "$890,000"],
           ["Transportation and disposal", "$520,000", "$145,000", "$665,000"],
           ["Confirmation sampling and laboratory", "$85,000", "$40,000", "$125,000"],
           ["Clean backfill procurement and placement", "$290,000", "$85,000", "$375,000"],
           ["Environmental oversight and reporting", "$175,000", "$45,000", "$220,000"],
           ["Subtotal", "$1,750,000", "$525,000", "$2,275,000"],
           ["Stated contingency (labelled \"10%\")", "$100,000", "$25,000", "$125,000"],
           ["Stated total", "$1,850,000", "$550,000", "$2,400,000"],
           ["Effective contingency rate", "5.71%", "4.76%", "5.49%"],
           ["Total if 10% is applied", "$1,925,000", "$577,500", "$2,502,500"],
           ["Tenant residual at stated total", "—", "—", "$600,000"],
           ["Tenant residual if 10% applied", "—", "—", "$702,500"]],
          [2.35, 1.15, 1.15, 1.35], size=8, align_right=[1, 2, 3])
    body(doc, "**A3.4  Capital stack and uses**", size=9.5)
    table(doc,
          [["Sources", "Amount", "Uses", "Amount"],
           ["Construction loan (Bayside)", "$285,000,000", "Hard costs", "$352,000,000"],
           ["Preferred equity (Coventry)", "$95,000,000", "Soft costs", "$38,500,000"],
           ["Co-invest (Meridian)", "$45,000,000", "Contingency", "$34,500,000"],
           ["**Total sources**", "**$425,000,000**", "**Total uses**", "**$425,000,000**"],
           ["Loan-to-cost", "67.06%", "Origination fee (1.00%)", "$2,850,000"],
           ["", "", "Remediation (not budgeted)", "$2,400,000"],
           ["", "", "Bulkhead (not budgeted, unquantified)", "TBD"]],
          [1.9, 1.2, 2.0, 1.3], size=8, align_right=[1, 3])

    pagebreak(doc)
    cover_line(doc, "APPENDIX 4", size=12, bold=True, space_after=4)
    cover_line(doc, "OPEN ITEMS CHECKLIST", size=11, bold=True, space_after=10)
    table(doc,
          [["#", "Item", "Type", "Owner", "Target"],
           ["1", "Confirm bracketed policy items in Part 11 (extension option; rent figures; freeboard; damages cap; "
            "cash deposit)", "Instruction", "M. Ellison", "June 24"],
           ["2", "Confirm Bayside term sheet executed; obtain lender's ground lease and SNDA checklists",
            "Diligence", "M. Ellison / S. Milliken", "June 27"],
           ["3", "Request survey plat and re-certification; obtain CLS-2025-0321 if it exists", "Diligence",
            "J. Abernathy", "June 27"],
           ["4", "Request Phase II full report, Appendices A–J, ELUR instrument and EMP", "Diligence",
            "J. Abernathy", "June 27"],
           ["5", "Request recorded 2019 declarations (ROFR and affordable covenant)", "Diligence", "J. Abernathy",
            "June 27"],
           ["6", "Commission the bulkhead structural assessment", "Action", "Authority / Meridian", "June 30"],
           ["7", "Obtain Bayside consent to disclose its term sheet terms to the Authority and its counsel", "Action",
            "R. Tsang", "July 3"],
           ["8", "DEEP pre-application meeting on the ELUR ground-floor interpretation", "Action",
            "Halcyon / Meridian", "July 15"],
           ["9", "Verify City's statutory authority for the 15-year abatement; confirm hearing requirements",
            "Legal research", "R. Tsang", "July 18"],
           ["10", "Complete Connecticut research on penalty/forfeiture, New Lease enforceability, municipal "
            "arbitration, and mechanics' liens on public property", "Legal research", "R. Tsang / J. Abernathy",
            "July 25"],
           ["11", "Draft the amendment to the recorded ROFR for Authority counsel", "Drafting", "R. Tsang", "July 25"],
           ["12", "Obtain zoning/site-plan analysis confirming the 28-story program is buildable as of right",
            "Diligence", "Meridian / architect", "July 31"],
           ["13", "Confirm remediation contingency (5.5% or 10%) with Halcyon and correct the figures if needed",
            "Instruction", "Meridian", "July 11"],
           ["14", "Confirm AMI geography with HUD and conform the Term Sheet, title exception and survey", "Diligence",
            "J. Abernathy", "July 11"],
           ["15", "Request special Authority Board meeting date for the second week of September", "Action",
            "R. Tsang to H. Koss", "June 27"],
           ["16", "Confirm that a separate ROFR-amendment resolution is required and calendared", "Action",
            "Authority counsel", "July 18"],
           ["17", "Obtain City counsel's confirmation on the tax abatement agreement timeline and fiscal-year "
            "constraints", "Action", "Authority / City", "August 8"],
           ["18", "Reconcile the 480 ft / 320.47 ft bulkhead length and conform Sections 2.9 and 14.3", "Drafting",
            "J. Abernathy", "After survey plat"]],
          [0.35, 3.05, 0.85, 1.3, 0.85], size=7.5)
    body(doc, "**Legend.** *Instruction* — requires a decision from the client. *Diligence* — requires a third "
              "party's document. *Action* — requires a third party's cooperation or performance. *Legal research* — "
              "requires completion before the position is used externally. *Drafting* — within our control.", size=8.5)
    para(doc, "", space_after=10)
    body(doc, "*This memorandum is a privileged and confidential attorney–client communication prepared in "
              "anticipation of litigation and for the purpose of rendering legal advice. It is based solely on the "
              "documents identified in Part 1 and Appendix 1, which we have assumed to be genuine, complete and "
              "accurate. We have not independently investigated the Premises, the title, the environmental "
              "conditions, the financial projections or the parties' authority except as expressly stated. Nothing "
              "in this memorandum constitutes an opinion of Connecticut law on the questions identified in Part 7, "
              "which remain subject to confirmation.*", size=8.5)
