from memo_helpers import *

def blocks(doc):
    # ================= PART 2 =================
    h1(doc, "Part 2 — Figures, dates and thresholds independently recomputed", "2")
    body(doc, "We recomputed every number that appears in the Term Sheet, the Phase II ESA and the Board Resolution "
              "rather than adopting the documents' own arithmetic. The full computation schedule is Appendix 3. "
              "Findings follow.")
    h2(doc, "2.1  Base Rent, escalation and the per-square-foot rate", "2.1")
    table(doc,
          [["#", "Item", "Record states", "Our recomputation", "Result"],
           ["1", "Rent per square foot", "$20.45/SF ($2,850,000 ÷ 139,392 SF)", "$20.4466", "Correct as rounded"],
           ["2", "Monthly Base Rent", "$237,500 ($2,850,000 ÷ 12)", "$237,500.00", "Correct"],
           ["3", "Years 6–10 annual Base Rent", "$3,224,500", "$3,224,513.41 ($2,850,000 × 1.025^5)",
            "Understated by $13.41"],
           ["4", "Years 11–15 annual Base Rent", "$3,648,200", "$3,648,240.95 ($2,850,000 × 1.025^10)",
            "Understated by $40.95"],
           ["5", "Years 6–10 monthly", "≈ $268,708", "$268,709.45", "Correct as rounded"],
           ["6", "Years 11–15 monthly", "≈ $304,017", "$304,020.08", "Correct as rounded"]],
          [0.28, 1.42, 1.45, 2.0, 1.35], size=7.5)
    body(doc, "Items 3 and 4 arise because the Term Sheet compounded the rounded Year 6 figure ($3,224,500 × 1.025^5 "
              "= $3,648,225.78) rather than the initial Base Rent. The aggregate difference is about $54 per annum — "
              "economically immaterial, but it would produce two different rent schedules depending on which sentence "
              "of the lease a reader applied. Section 4.3 of the Draft Lease states the schedule as controlling and "
              "reconciles the difference expressly, so that neither side can later argue that a scrivener's rounding "
              "was a negotiated term. If Mr. Koss prefers the Term Sheet figures, we should accept them and conform "
              "the schedule — the point is the internal consistency, not the $54.")
    h2(doc, "2.2  Security deposit and remediation credit", "2.2")
    table(doc,
          [["#", "Item", "Record states", "Our recomputation", "Result"],
           ["7", "Security deposit", "$5,700,000 = 24 × $237,500", "$5,700,000.00", "Correct"],
           ["8", "Step-down amount", "$2,850,000 = 12 × $237,500", "$2,850,000.00", "Correct"],
           ["9", "Remediation credit waterfall", "Months 1–7 at $0; month 8 credit $137,500, Tenant pays $100,000",
            "7 × $237,500 = $1,662,500; $1,800,000 − $1,662,500 = $137,500; $237,500 − $137,500 = $100,000",
            "Correct and internally consistent"],
           ["10", "Tenant remediation share", "$600,000", "$2,400,000 − $1,800,000 = $600,000", "Correct"]],
          [0.28, 1.42, 1.85, 2.15, 0.8], size=7.5)
    h2(doc, "2.3  Taxes and the tax abatement", "2.3")
    table(doc,
          [["#", "Item", "Record states", "Our recomputation", "Result"],
           ["11a", "Current taxes (land only)", "$145,950", "$4,200,000 × 0.03475 = $145,950.00", "Correct"],
           ["11b", "Full-build taxes", "$6,185,500", "$178,000,000 × 0.03475 = $6,185,500.00", "Correct"],
           ["11c", "Years 1–5 (25%)", "$1,546,375", "$178,000,000 × 0.25 × 0.03475 = $1,546,375.00", "Correct"],
           ["11d", "Years 6–10 (50%)", "$3,092,750", "$178,000,000 × 0.50 × 0.03475 = $3,092,750.00", "Correct"],
           ["11e", "Years 11–15 (75%)", "$4,639,125", "$178,000,000 × 0.75 × 0.03475 = $4,639,125.00", "Correct"],
           ["11f", "Aggregate value of the abatement", "not stated", "$46,391,250 over 15 years "
            "(5 × $4,639,125 + 5 × $3,092,750 + 5 × $1,546,375)", "New figure — useful for Board presentation"]],
          [0.3, 1.4, 1.15, 2.65, 1.0], size=7.5)
    body(doc, "The percentages and amounts are correct, but note the structural point in Part 6.2 below: the "
              "abatement is calculated as a percentage of the *post-development assessed value* that will not exist "
              "during construction. Because the Term Sheet starts the 15-year clock on the Lease Commencement Date, "
              "approximately three of the fifteen years (October 2025 – September 2028) fall before Rent Commencement, "
              "when the improvements are not yet on the grand list. The aggregate value of the abatement stated above "
              "is therefore only achievable if the clock is re-anchored.")
    h2(doc, "2.4  Capital stack and uses", "2.4")
    body(doc, "Sources ($285,000,000 loan + $95,000,000 Coventry preferred equity + $45,000,000 Meridian co-invest = "
              "$425,000,000) and uses ($352,000,000 hard + $38,500,000 soft + $34,500,000 contingency = $425,000,000) "
              "both reconcile. Loan-to-cost is 67.06% (the Term Sheet states 67.1%). Equity is 32.94%. Bayside's "
              "1.00% origination fee on $285,000,000 is $2,850,000, correct.")
    body(doc, "**Two items appear to be unbudgeted.** First, the environmental remediation: the Phase II estimate is "
              "$2,400,000, of which Tenant's net share is $600,000, but neither figure appears in the uses of funds. "
              "Second, the bulkhead: the Phase II expressly excludes bulkhead repair or replacement from its $2.4M "
              "estimate and recommends a separate structural assessment. We do not know the magnitude, but a 480-foot "
              "steel sheet pile and concrete cap rehabilitation on a coastal site is a seven-figure item, not a "
              "rounding error. Both should be added to the uses (or confirmed as within the hard-cost contingency) "
              "before the loan budget is finalized with Bayside, because Bayside's condition (g) requires an approved "
              "construction budget.")
    h2(doc, "2.5  Milestones and other date intervals", "2.5")
    table(doc,
          [["#", "Item", "Record states", "Our recomputation", "Result"],
           ["15", "Milestone 1 (18 months)", "April 1, 2027", "October 1, 2025 + 18 months = April 1, 2027", "Correct"],
           ["16", "Milestone 2 (42 months)", "April 1, 2029", "October 1, 2025 + 42 months = April 1, 2029", "Correct"],
           ["17", "Milestone 3 (60 months)", "October 1, 2030", "October 1, 2025 + 60 months = October 1, 2030",
            "Correct"],
           ["18", "Milestone 4 (84 months)", "October 1, 2032", "October 1, 2025 + 84 months = October 1, 2032",
            "Correct"],
           ["19", "Rent Commencement (36 months)", "October 1, 2028", "October 1, 2025 + 36 months = October 1, 2028",
            "Correct"],
           ["20", "Expiration", "September 30, 2124", "99 years from October 1, 2025 = September 30, 2124", "Correct"],
           ["21", "ROFR period (20 years)", "through September 30, 2045",
            "October 1, 2025 + 20 years = September 30, 2045", "Correct"],
           ["22", "Alteration restriction (final 10 years)", "from October 1, 2114", "October 1, 2124 − 10 years = "
            "October 1, 2114", "Correct"],
           ["23", "Force majeure cap", "12 months FM + 6 months permitting; aggregate 18", "12 + 6 = 18", "Correct"],
           ["24", "Title commitment expiration", "December 1, 2025", "June 1, 2025 + 6 months = December 1, 2025",
            "Correct — but see Part 6.14"],
           ["25", "Bayside term sheet expiration", "June 27, 2025", "May 28, 2025 + 30 days = June 27, 2025",
            "Correct — confirm execution"]],
          [0.3, 1.55, 1.2, 2.25, 1.2], size=7.5)
    h2(doc, "2.6  The Phase II cost estimate contains two arithmetic errors", "2.6")
    body(doc, "This is a small point with a real consequence, because the $2,400,000 total is the number the credit is "
              "built on. In each of Halcyon's two cost tables the line labelled \"Contingency (10%)\" is not 10%:")
    table(doc,
          [["Area", "Cost components (sum)", "Stated contingency", "Stated \"10%\" would be", "Stated total",
            "Total if 10% applied"],
           ["Area 1 — Northwest Corner", "$1,750,000", "$100,000 (5.71%)", "$175,000", "$1,850,000", "$1,925,000"],
           ["Area 2 — Former Dry Dock", "$525,000", "$25,000 (4.76%)", "$52,500", "$550,000", "$577,500"],
           ["Combined", "$2,275,000", "$125,000 (5.49%)", "$227,500", "$2,400,000", "$2,502,500"]],
          [1.35, 1.25, 1.15, 1.05, 0.85, 0.9], size=7.5, align_right=[1, 2, 3, 4, 5])
    body(doc, "The stated totals are arithmetically consistent with the stated contingency line items ($1,750,000 + "
              "$100,000 = $1,850,000; $525,000 + $25,000 = $550,000). The error is in the *label*, not the addition: "
              "the effective contingency is 5.5%, not 10%. The consequence is that if 10% is in fact the intended "
              "contingency, the total is $2,502,500, and Tenant's residual share (total less the $1,800,000 credit) is "
              "**$702,500, not $600,000** — a $102,500 gap in a figure that has already been described to the Authority, "
              "to Coventry and in the Board resolution. Our recommendation is not to litigate the label but to use it: "
              "we should confirm with Halcyon and with you which contingency is intended, and, if it is 10%, correct "
              "the figures now. An understated remediation estimate is the last thing we want in a lease where Tenant "
              "bears every dollar of overrun.")
    flagbox(doc, "Related quantity issue.", "Halcyon states that 933 cubic yards of contaminated soil require "
             "excavation in Area 1 but prices a \"material handling volume\" of approximately 3,100 cubic yards, and "
             "does not state the disposal quantity. At $520,000, the off-site transportation and disposal line implies "
             "either $557 per cubic yard on 933 CY (implausibly high) or $168 per cubic yard on 3,100 CY (plausible, "
             "but then all 3,100 CY is being treated as disposal rather than the clean backfill that a separate "
             "$290,000 line is procuring). The estimate cannot be verified without Appendix I (Remediation Cost "
             "Estimate Backup and Supporting Calculations), which is not in the record. **Request it.**")

    # ================= PART 3 =================
    h1(doc, "Part 3 — The Premises: a material legal description error", "3")
    body(doc, "This is the finding in the record that we regard as most urgent after the reverter, because it is "
              "silent, it is gating, and it will not be discovered by anyone who does not run the traverse.")

    h2(doc, "3.1  The title commitment's Exhibit A describes a parcel of approximately 6.42 acres", "3.1")
    body(doc, "The Title Commitment (Schedule A, Section 5 and Exhibit A) attaches a metes-and-bounds description and "
              "states that it is \"derived from\" an ALTA/NSPS survey. We ran that description:")
    table(doc,
          [["Course", "Bearing", "Distance"],
           ["North line (Pier Street)", "North 72° 15′ 30″ East", "580.00 ft"],
           ["Bulkhead (east), course 1", "South 18° 22′ 45″ East", "240.40 ft"],
           ["Bulkhead (east), course 2", "South 17° 48′ 10″ East", "239.60 ft"],
           ["South line (APN 127-003-0044)", "South 72° 08′ 15″ West", "582.50 ft"],
           ["West line (Harbor Avenue)", "North 17° 44′ 30″ West", "480.20 ft"]],
          [2.45, 2.65, 1.4], size=8, align_right=[2])
    body(doc, "Computed on those courses: the traverse **miscloses by approximately 1.10 feet**, and the enclosed area "
              "is **approximately 279,535 square feet, or 6.417 acres**. The same instrument recites \"Containing 3.2 "
              "acres (139,392 square feet), more or less.\" The discrepancy is not a rounding error: the computed area "
              "is **2.01 times** the recited area. The same description also recites a 480.00-foot bulkhead frontage "
              "(240.40 + 239.60), which is where the recurring \"approximately 480 linear feet of bulkhead\" figure "
              "comes from.")
    body(doc, "By contrast, the description in the delivered survey (Survey Job No. CLS-2025-0417) **closes exactly** "
              "(0.000 feet of misclosure) and encloses **139,475 square feet (3.202 acres)**, a variance of +83 square "
              "feet (+0.06%) from the recited 139,392 — which is simply the assessor's 3.2 acres × 43,560. The two "
              "descriptions also differ systematically:")
    table(doc,
          [["Element", "Title Commitment Exhibit A", "Delivered Survey (Section 4)", "Difference"],
           ["North line bearing", "N 72° 15′ 30″ E", "S 78° 15′ 30″ E", "Exactly 6° 00′ 00″"],
           ["West line bearing", "N 17° 44′ 30″ W", "N 11° 44′ 30″ E", "Exactly 6° 00′ 00″"],
           ["North / south line length", "580.00 ft / 582.50 ft", "435.22 ft / 435.22 ft", "≈ 145 ft"],
           ["East / west line length", "240.40 + 239.60 = 480.00 ft / 480.20 ft", "320.47 ft / 320.47 ft",
            "≈ 160 ft"],
           ["Closure", "1.10 ft misclosure", "0.000 ft", "—"],
           ["Enclosed area", "≈ 279,535 SF (6.417 ac)", "139,475 SF (3.202 ac)", "2.01×"]],
          [1.45, 1.95, 1.85, 1.25], size=7.5)
    body(doc, "**Conclusion.** The title commitment's Exhibit A cannot be used as the legal description of the "
              "Premises, and, taken literally, it would describe a parcel that encroaches on Assessor's Parcel No. "
              "127-003-0044 (retained by the Authority for park development) and beyond. It should not be signed by "
              "either party in its current form. We have drafted **Exhibit A** to the Draft Lease from the survey "
              "description and have inserted Section 16.2 and a drafting note requiring Landlord, at its cost, to "
              "correct the description and cause the title company to reissue before Lease Commencement. Section "
              "2.3(b) makes a conformed title commitment a condition precedent.")
    body(doc, "**Two further consequences** deserve your attention. First, the Base Rent is expressed as approximately "
              "$20.45 per square foot on 139,392 square feet. On the title commitment's (erroneous) 279,535 square "
              "feet, the same dollars would be $10.20 per square foot. If the parties ever litigate rent, the "
              "description and the area recital must be consistent, so this is a rent risk as well as a title risk. "
              "Second, the survey's own narrative repeats \"approximately 480 linear feet of bulkhead\" while its "
              "traverse gives a 320.47-foot eastern boundary and the pedestrian easement computation (15 ft × 480 ft = "
              "7,200 SF) is built on 480 feet. On 320.47 feet the easement area is 4,807 square feet. We have "
              "therefore treated the 480-foot figure as unverified in Sections 2.9(b) and 14.3 and flagged it for "
              "confirmation from the survey plat, because the bulkhead length drives both the repair cost allocation "
              "and the geometry of the 8,000 square foot public open space.")

    h2(doc, "3.2  The survey referenced by the title commitment is not the survey in the record", "3.2")
    table(doc,
          [["Data point", "Title Commitment (Exhibit A / Schedule A)", "Delivered survey"],
           ["Job / drawing number", "CLS-2025-0321", "CLS-2025-0417"],
           ["Surveyor", "J. Michael Ferreira, P.L.S.", "Thomas R. Pellegrino, P.L.S."],
           ["Connecticut license", "No. 12847", "No. PLS-008741"],
           ["Date", "April 20, 2025, \"last revised May 15, 2025\"", "Field April 20, 2025; plat April 28, 2025"]],
          [1.4, 2.75, 2.35], size=7.5)
    body(doc, "Either there are two surveys by the same firm (in which case we need CLS-2025-0321 and an explanation "
              "of why it differs), or the title company transcribed the description and the survey references from a "
              "different file. Either way, the survey referenced in the title commitment is not in the record, is not "
              "certified to Bayside, and cannot satisfy Bayside's condition (d), which requires a survey prepared by a "
              "licensed surveyor and certified to the Lender and the title company, dated within ninety days of "
              "closing. Ridgepoint and Calloway Land Surveyors must reconcile this before the description is used for "
              "the lease or the memorandum of lease.")

    h2(doc, "3.3  Two further record conflicts in the condemnation history", "3.3")
    body(doc, "The parties recite the Authority's 2012 taking inconsistently. The Term Sheet (§ 2) places the final "
              "judgment in the \"Connecticut Superior Court, Judicial District of Port Calloway\"; the Title Commitment "
              "(Schedule A, § 4 and Exception No. 10) places it in the \"Judicial District of New Haven\"; and the "
              "survey references the Final Order of Condemnation at **Volume 375, Page 44**, while the Title Commitment "
              "twice cites **Volume 367, Page 44**. We have drafted the Landlord representation in Section 18.1(g) to "
              "cover the substance (that no reverter, reversionary interest or former-owner claim survives) rather than "
              "reciting a volume and page that may be wrong, and we have flagged the discrepancy for correction in the "
              "title policy and in the recitals. Small in themselves; together with item 3.1 they suggest that the "
              "title work has not yet been reviewed by anyone at the level this transaction requires.")
