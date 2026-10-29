from helpers import *

def blocks(doc):
    # ---------- EXHIBIT A ----------
    pagebreak(doc)
    cover_line(doc, "EXHIBIT A", size=12, bold=True, space_after=4)
    cover_line(doc, "LEGAL DESCRIPTION OF THE PREMISES", size=11, bold=True, space_after=16)
    para(doc, "All that certain piece or parcel of land situated in the City of Port Calloway, County of New Haven, "
              "State of Connecticut, bounded and described as follows:")
    para(doc, "**BEGINNING** at a point at the intersection of the southerly line of Pier Street (a 60-foot public "
              "right-of-way) and the easterly line of Harbor Avenue (a 50-foot public right-of-way), said point being "
              "the northwest corner of the herein-described parcel, marked by a found 5/8-inch iron rebar;")
    para(doc, "**THENCE** running South 78 degrees 15 minutes 30 seconds East along the southerly line of Pier Street, "
              "a distance of Four Hundred Thirty-Five and 22/100 feet (435.22') to a point at the northeast corner of "
              "the herein-described parcel, said point being on the westerly line of the 15-foot public pedestrian "
              "access easement recorded at Volume 395, Page 112 of the Port Calloway Land Records, marked by a found "
              "5/8-inch iron rebar;")
    para(doc, "**THENCE** running South 11 degrees 44 minutes 30 seconds West along the westerly line of said "
              "pedestrian access easement and along the bulkhead line, a distance of Three Hundred Twenty and 47/100 "
              "feet (320.47') to a point at the southeast corner of the herein-described parcel, said point being on "
              "the northerly boundary of Assessor's Parcel No. 127-003-0044 (City of Port Calloway Redevelopment "
              "Authority, reserved for future park development), marked by a set 5/8-inch iron rebar with aluminum cap "
              "stamped \"PLS 008741\";")
    para(doc, "**THENCE** running North 78 degrees 15 minutes 30 seconds West along the northerly line of said "
              "Assessor's Parcel No. 127-003-0044, a distance of Four Hundred Thirty-Five and 22/100 feet (435.22') to "
              "a point at the southwest corner of the herein-described parcel, said point being on the easterly line "
              "of Harbor Avenue, marked by a set 5/8-inch iron rebar with aluminum cap stamped \"PLS 008741\";")
    para(doc, "**THENCE** running North 11 degrees 44 minutes 30 seconds East along the easterly line of Harbor Avenue, "
              "a distance of Three Hundred Twenty and 47/100 feet (320.47') to the POINT OF BEGINNING.")
    para(doc, "Containing 139,392 square feet, or 3.200 acres, more or less.")
    para(doc, "**Basis of Bearings:** Connecticut State Plane Coordinate System, NAD83 (2011), South Zone. "
              "**Vertical Datum:** NAVD88.")
    para(doc, "Being a portion of the land conveyed to the City of Port Calloway Redevelopment Authority by Final "
              "Order of Condemnation recorded in the Port Calloway Land Records, dated June 15, 2012.")
    para(doc, "Said parcel is subject to the easements, encumbrances and other matters set forth on **Exhibit B**.")
    note(doc, "[**Drafting note — source and reconciliation.** This description is taken from the narrative legal "
              "description in the ALTA/NSPS Land Title Survey prepared by Calloway Land Surveyors LLC, Thomas R. "
              "Pellegrino, PLS (Connecticut License No. PLS-008741), Survey Job No. CLS-2025-0417, field survey "
              "April 20, 2025, plat dated April 28, 2025. (1) The traverse closes exactly and encloses 139,475 square "
              "feet, not the 139,392 square feet recited above; the recital of 139,392 square feet is the assessor's "
              "figure (3.2 acres x 43,560), and the parties should confirm which figure controls, particularly because "
              "the per-square-foot Base Rent ($20.45) in the Term Sheet is derived from 139,392. (2) The description "
              "**attached as Exhibit A to Title Commitment TC-2025-07821** is materially different: it uses bearings "
              "of North 72 degrees 15 minutes 30 seconds East (rather than South 78 degrees 15 minutes 30 seconds "
              "East), distances of 580.00 feet and 582.50 feet along the north and south lines, a Harbor Avenue line "
              "of 480.20 feet, and two bulkhead courses of 240.40 feet and 239.60 feet. On those courses the parcel "
              "encloses approximately 279,535 square feet (6.42 acres) and the traverse miscloses by approximately "
              "1.10 feet. That description cannot be used. (3) The Title Commitment states that its description was "
              "derived from a survey identified as Drawing No. CLS-2025-0321 by J. Michael Ferreira, P.L.S. "
              "(Connecticut License No. 12847), last revised May 15, 2025 — a survey that is not in the record and "
              "that differs in job number, surveyor, license number and date from the survey actually delivered. "
              "Landlord and the title company must reconcile and reissue before the Lease Commencement Date. "
              "(4) The \"approximately 480 linear feet of bulkhead\" figure used in the Term Sheet, the Title "
              "Commitment and the survey narrative is not consistent with the 320.47-foot eastern boundary line in "
              "the survey traverse; the 480-foot figure appears to derive from the erroneous title description. The "
              "parties should confirm the actual bulkhead length from the survey plat and conform Sections 2.9 and "
              "14.3 accordingly.]")

    # ---------- EXHIBIT B ----------
    pagebreak(doc)
    cover_line(doc, "EXHIBIT B", size=12, bold=True, space_after=4)
    cover_line(doc, "PERMITTED EXCEPTIONS", size=11, bold=True, space_after=16)
    para(doc, "The leasehold estate created by this Lease is subject only to the following Permitted Exceptions, as "
              "disclosed in Title Commitment No. TC-2025-07821 issued by Ridgepoint Title & Escrow Co. (effective "
              "June 1, 2025), as the same may be updated to reflect conditions at the Lease Commencement Date:")
    ex = [
        ("Part 1 — Environmental Land Use Restriction.", "Environmental Land Use Restriction recorded March 22, 2018, "
         "at Volume 412, Page 88 of the Port Calloway Land Records, executed by the City of Port Calloway Redevelopment "
         "Authority and approved by DEEP pursuant to Connecticut General Statutes § 22a-133o and the Connecticut "
         "Remediation Standard Regulations, imposing (a) a prohibition on residential use on the ground floor of any "
         "structure on the Premises, (b) a requirement to install and maintain an engineered barrier of not less than "
         "two (2) feet of clean fill or an equivalent impervious surface cover over any area of ground disturbance, "
         "(c) monitoring, inspection and annual compliance certification obligations, and (d) restrictions on "
         "excavation below the engineered barrier without DEEP approval. Subject to Section 7.8."),
        ("Part 2 — Public Utility Easement.", "Easement for public utilities (underground electric and sewer) in favor "
         "of the City of Port Calloway, twenty (20) feet in width, along the northern boundary of the Premises (Pier "
         "Street frontage), recorded at Volume 388, Page 201 of the Port Calloway Land Records, together with rights of "
         "ingress and egress."),
        ("Part 3 — Public Pedestrian Access Easement.", "Easement for public pedestrian access, fifteen (15) feet in "
         "width, along the eastern (waterfront) boundary of the Premises, recorded at Volume 395, Page 112 of the Port "
         "Calloway Land Records, prohibiting permanent structures within the easement area but permitting landscaping, "
         "paving, benches, lighting and similar public amenities. Tenant's obligations with respect to the Public Open "
         "Space are set forth in Section 14.4."),
        ("Part 4 — Right of First Refusal.", "Right of first refusal in favor of the City of Port Calloway "
         "Redevelopment Authority set forth in the Declaration of Right of First Refusal dated September 8, 2019, "
         "recorded at Volume 405, Page 55 of the Port Calloway Land Records, as amended prior to the Lease Commencement "
         "Date to conform to Section 11.5 of this Lease (including the carve-outs for Permitted Transfers, Leasehold "
         "Mortgages, foreclosure, deed-in-lieu transfers and New Leases)."),
        ("Part 5 — Affordable Housing Restrictive Covenant.", "Declaration of Restrictive Covenants dated November 15, "
         "2019, recorded at Volume 408, Page 230 of the Port Calloway Land Records, requiring that not less than fifteen "
         "percent (15%) of residential dwelling units be designated as affordable housing available to households "
         "earning at or below eighty percent (80%) of Area Median Income for the duration of the ground lease, as "
         "supplemented by Section 14.5 of this Lease."),
        ("Part 6 — Mechanics' Lien (to be discharged).", "Mechanics' lien filed by Calloway Marine Demolition Inc. on "
         "April 3, 2025 in the amount of $187,500.00, recorded at Volume 418, Page 302 of the Port Calloway Land "
         "Records, arising from bulkhead demolition work performed for Landlord. **This exception is not a Permitted "
         "Exception for purposes of this Lease.** Landlord shall discharge, release or bond off the lien at its sole "
         "cost prior to the Lease Commencement Date pursuant to Section 2.9(a), and the leasehold title policy shall "
         "not contain an exception for it."),
        ("Part 7 — Taxes and Assessments.", "Real property taxes and assessments for the fiscal year commencing July 1, "
         "2025 and thereafter, not yet due and payable, subject to Article 6 (including the Tax Abatement) and to "
         "Tenant's right to contest under Section 6.4."),
        ("Part 8 — Zoning and Land Use Regulations.", "All zoning ordinances, land use regulations, building codes, "
         "coastal management and wetlands regulations and other governmental regulations applicable to the Premises, "
         "including the WRD-3 zoning district regulations, subject to Tenant's rights under Article 15."),
        ("Part 9 — Flood Zone Designation.", "Location of the Premises within FEMA Flood Zone AE, FIRM Panel No. "
         "09009C0301G, effective January 15, 2020, Base Flood Elevation 12 feet NAVD88, subject to Section 15.3."),
        ("Part 10 — Eminent Domain History.", "Rights reserved by or to the public or any governmental entity in "
         "connection with the eminent domain proceedings by which Landlord acquired fee simple title, subject to "
         "Landlord's representation in Section 18.1(g) that no reverter, reversionary interest, residual claim or "
         "former owner claim exists that could impair Tenant's leasehold estate."),
    ]
    for t, txt in ex:
        p = doc.add_paragraph(); p.paragraph_format.space_after = Pt(2)
        p.paragraph_format.keep_with_next = True
        runs(p, "**" + t + "**", size=9.5)
        para(doc, txt, indent=0.35, space_after=8, size=None)

    # ---------- EXHIBIT C ----------
    pagebreak(doc)
    cover_line(doc, "EXHIBIT C", size=12, bold=True, space_after=4)
    cover_line(doc, "DEVELOPMENT MILESTONES AND EXTENSION SCHEDULE", size=11, bold=True, space_after=16)
    table(doc,
          [["Milestone", "Description", "Period from Lease Commencement Date", "Deadline (assuming 10/1/2025)",
            "Maximum Extension"],
           ["1", "Commencement of Construction — physical pouring of footings for at least one building following "
            "issuance of all necessary building permits", "18 months", "April 1, 2027",
            "12 mo. Force Majeure + 6 mo. permitting + uncapped Landlord Delay + optional paid extensions"],
           ["2", "Completion of Structural Frame — topping out of structural steel and concrete frame of the "
            "Residential Tower", "42 months", "April 1, 2029", "As above (no reverter)"],
           ["3", "Substantial Completion of Phase 1 — Residential Tower and ground-floor retail", "60 months",
            "October 1, 2030", "As above (reverter right subject to Article 10 procedure)"],
           ["4", "Substantial Completion of Phase 2 — Office Building", "84 months", "October 1, 2032",
            "As above (no reverter)"]],
          [0.5, 2.3, 1.05, 1.15, 1.5], size=8)
    para(doc, "**Extension mechanics.** (a) Force Majeure Events: day for day, maximum 12 months in the aggregate. "
              "(b) Permitting delays: day for day, maximum 6 months in the aggregate. (c) The aggregate of (a) and (b) "
              "shall not exceed 18 months. (d) Landlord Delay: day for day, uncapped. (e) Tenant's optional paid "
              "extensions under Section 3.4(d), if agreed. Tenant shall give notice of any Force Majeure Event or "
              "permitting delay within thirty (30) days after becoming aware of it.")
    para(doc, "**Reversion of rights.** Only Milestone 1 and Milestone 3 are enforceable by termination, and only "
              "after the Milestone Notice, the 180-day Milestone Cure Period, the 180-day Lender Cure Period, the "
              "30-day Landlord election window and the conditions in Section 10.5(g), and only upon payment or "
              "securing of the Improvement Payment under Section 10.6. Failure to achieve Milestone 2 or Milestone 4 "
              "gives Landlord no remedy other than notice and consultation (Section 3.5).")

    # ---------- EXHIBIT D ----------
    pagebreak(doc)
    cover_line(doc, "EXHIBIT D", size=12, bold=True, space_after=4)
    cover_line(doc, "BASE RENT SCHEDULE, RENT RESET AND PERCENTAGE RENT MECHANICS", size=11, bold=True, space_after=14)
    para(doc, "**Part 1 — Base Rent, Lease Years 1 through 15**", space_after=6)
    table(doc,
          [["Lease Year", "Annual Base Rent", "Monthly Installment", "Computation"],
           ["1", "$2,850,000", "$237,500.00", "Initial annual Base Rent"],
           ["2", "$2,850,000", "$237,500.00", "No escalation"],
           ["3", "$2,850,000", "$237,500.00", "No escalation"],
           ["4", "$2,850,000", "$237,500.00", "No escalation"],
           ["5", "$2,850,000", "$237,500.00", "No escalation"],
           ["6", "$3,224,513", "$268,709.45", "$2,850,000 x (1.025)^5"],
           ["7", "$3,224,513", "$268,709.45", "No escalation"],
           ["8", "$3,224,513", "$268,709.45", "No escalation"],
           ["9", "$3,224,513", "$268,709.45", "No escalation"],
           ["10", "$3,224,513", "$268,709.45", "No escalation"],
           ["11", "$3,648,241", "$304,020.08", "$2,850,000 x (1.025)^10"],
           ["12", "$3,648,241", "$304,020.08", "No escalation"],
           ["13", "$3,648,241", "$304,020.08", "No escalation"],
           ["14", "$3,648,241", "$304,020.08", "No escalation"],
           ["15", "$3,648,241", "$304,020.08", "No escalation"]],
          [0.9, 1.5, 1.5, 2.1], size=8.5, align_right=[1, 2])
    para(doc, "**Part 2 — Rent Resets (Lease Years 16, 26, 36, 46, 56, 66, 76, 86 and 96)**", space_after=6)
    para(doc, "Base Rent shall be reset on each Rent Reset Date to the greater of (a) $2,850,000 x (1.025)^(Lease Year "
              "- 1) and (b) $2,850,000 x the cumulative percentage increase in the CPI-U Northeast from the base index "
              "month (the third calendar month preceding the Rent Commencement Date) to the reset index month (the "
              "third calendar month preceding the Rent Reset Date). Base Rent shall not be reduced on any Rent Reset, "
              "and each calculation shall be made from the initial annual Base Rent rather than from any previously "
              "reset amount.")
    para(doc, "**Part 3 — Percentage Rent**", space_after=6)
    table(doc,
          [["Lease Year", "Base Rent (2.5% floor)", "Breakpoint (as proposed in Section 5.3)", "Ratio of Breakpoint to Base Rent"],
           ["6", "$3,224,513", "$28,500,000", "8.84x"],
           ["16", "$4,127,650", "$36,486,000", "8.84x"],
           ["26", "$5,283,741", "$46,697,000", "8.84x"],
           ["36", "$6,763,635", "$59,776,000", "8.84x"],
           ["46", "$8,658,024", "$76,516,000", "8.84x"],
           ["56", "$11,083,003", "$97,956,000", "8.84x"],
           ["66", "$14,187,181", "$125,380,000", "8.84x"],
           ["76", "$18,160,791", "$160,481,000", "8.84x"],
           ["86", "$23,247,348", "$205,453,000", "8.84x"],
           ["96", "$29,758,571", "$262,986,000", "8.84x"]],
          [1.0, 1.75, 2.2, 1.55], size=8.5, align_right=[1, 2, 3])
    para(doc, "The Base Rent figures in the second column assume the 2.5% floor governs at every Rent Reset. The "
              "Breakpoint figures in the third column are illustrative only and apply the mechanic proposed in Section "
              "5.3 (preserving the Lease Year 6 ratio of 8.84x); they are rounded to the nearest $1,000. If the "
              "Breakpoint is not indexed, it remains $28,500,000 for the entire Term.")
    para(doc, "**Part 4 — Worked Examples**", space_after=6)
    table(doc,
          [["Lease Year", "Gross Revenues", "Breakpoint", "Excess", "Percentage Rent (2.0%)"],
           ["6", "$30,000,000", "$28,500,000", "$1,500,000", "$30,000"],
           ["6", "$40,000,000", "$28,500,000", "$11,500,000", "$230,000"],
           ["16 (indexed)", "$40,000,000", "$36,486,000", "$3,514,000", "$70,280"],
           ["26 (indexed)", "$60,000,000", "$46,697,000", "$13,303,000", "$266,060"]],
          [1.05, 1.4, 1.4, 1.35, 1.35], size=8.5, align_right=[1, 2, 3, 4])

    # ---------- EXHIBIT E ----------
    pagebreak(doc)
    cover_line(doc, "EXHIBIT E", size=12, bold=True, space_after=4)
    cover_line(doc, "FORM OF LETTER OF CREDIT — REQUIRED TERMS", size=11, bold=True, space_after=14)
    para(doc, "The Letter of Credit required by Article 8 shall be an irrevocable standby letter of credit containing "
              "not less than the following terms:")
    lc = [
        "**Applicant:** Meridian Gateway Holdings LLC.",
        "**Beneficiary:** City of Port Calloway Redevelopment Authority, and its successors and assigns as owner of "
        "the landlord's interest under the Lease.",
        "**Amount:** $5,700,000, reduced to $2,850,000 in accordance with Section 8.4 (with an amendment mechanism "
        "requiring the issuer to amend within five (5) Business Days after receipt of a beneficiary-signed reduction "
        "notice and Tenant's request).",
        "**Issuer:** A bank meeting the rating or charter requirements of Section 8.3.",
        "**Term:** One (1) year, automatically renewable for successive one-year periods unless the issuer gives not "
        "less than sixty (60) days' prior written notice of non-renewal to the beneficiary; or, at Tenant's election, "
        "a term co-extensive with the Lease with annual renewal.",
        "**Drawing:** Available by presentation of a sight draft and a beneficiary's certificate stating that an "
        "Event of Default has occurred and remains uncured after the expiration of all applicable notice, cure and "
        "Lender Cure Periods and that the amount drawn does not exceed the amounts then due and unpaid or the "
        "Documented Damages finally determined under Section 10.7.",
        "**Partial Draws:** Permitted, with automatic reinstatement of the available amount to the extent of any "
        "amounts subsequently paid by or on behalf of Tenant or restored by Tenant under Section 8.6.",
        "**Presentation:** In Connecticut, by hand, overnight courier, facsimile or electronic presentation complying "
        "with applicable law (including the Uniform Commercial Code as adopted in Connecticut).",
        "**Governing Rules:** International Standby Practices (ISP98) or Uniform Customs and Practice for Documentary "
        "Credits (UCP 600), as designated by the issuer.",
        "**Transfer:** Transferable at the request of the beneficiary to any successor owner of the landlord's "
        "interest, without fee.",
        "**Expiry:** Returned to the issuer for cancellation promptly upon delivery of a replacement or upon the "
        "return of the Security Deposit under Section 8.7.",
    ]
    for i, t in enumerate(lc):
        sub(doc, "(%s)" % chr(97 + i), t)

    # ---------- EXHIBIT F ----------
    pagebreak(doc)
    cover_line(doc, "EXHIBIT F", size=12, bold=True, space_after=4)
    cover_line(doc, "REQUIRED TERMS OF SUBORDINATION, NON-DISTURBANCE AND ATTORNMENT AGREEMENT", size=11, bold=True,
               space_after=14)
    para(doc, "The SNDA required by Section 9.9 shall, at a minimum, provide as follows:")
    snd = [
        "Landlord acknowledges the existence, validity and first-priority lien of the Leasehold Mortgage, the "
        "assignment of leases and rents and the other collateral, and agrees that the Leasehold Mortgagee's interest "
        "is not subject to any offset, defense or claim of Landlord.",
        "Landlord agrees that, so long as no Event of Default by Tenant remains uncured after the expiration of all "
        "notice, cure and Lender Cure Periods, Landlord will not disturb the Leasehold Mortgagee's security interest, "
        "the leasehold estate, or the rights of any purchaser at a foreclosure sale or transferee by deed in lieu of "
        "foreclosure.",
        "Landlord agrees to recognize and accept the Leasehold Mortgagee, its designee, or any purchaser at "
        "foreclosure or transferee by deed in lieu of foreclosure as Tenant under the Lease (or under a New Lease), "
        "upon the same terms and conditions as the Lease, without requiring any further consent, fee or condition "
        "other than those in Article 9.",
        "Landlord agrees to deliver to the Leasehold Mortgagee a copy of every notice, together with the simultaneous "
        "delivery and cure provisions of Sections 9.3 and 9.5, and acknowledges the New Lease right in Section 9.6.",
        "All insurance proceeds and condemnation awards payable to Landlord's benefit as fee owner shall be applied as "
        "provided in Article 13, and the Leasehold Mortgagee's interest in such proceeds and awards shall be "
        "recognized.",
        "The Leasehold Mortgagee may exercise the New Lease right without Landlord's consent and without triggering "
        "the ROFR.",
        "The SNDA shall be binding on and inure to the benefit of the parties' successors and assigns, shall be "
        "recorded in the Port Calloway Land Records, and shall survive any transfer of Landlord's fee interest.",
        "Nothing in the SNDA shall subordinate Landlord's fee interest in the land to the Leasehold Mortgage or "
        "constitute an agreement by Landlord to subordinate its fee interest; the Leasehold Mortgagee's lien shall "
        "attach only to the leasehold estate and the Improvements.",
    ]
    for i, t in enumerate(snd):
        sub(doc, "(%s)" % chr(97 + i), t)

    # ---------- EXHIBIT G ----------
    pagebreak(doc)
    cover_line(doc, "EXHIBIT G", size=12, bold=True, space_after=4)
    cover_line(doc, "FORM OF MEMORANDUM OF GROUND LEASE", size=11, bold=True, space_after=14)
    para(doc, "**This Memorandum is prepared for the purpose of record notice only. It does not modify, amend or "
              "supersede the Ground Lease, and in the event of any conflict between this Memorandum and the Ground "
              "Lease, the Ground Lease controls.**", size=None)
    para(doc, "**1. Parties.** Landlord: City of Port Calloway Redevelopment Authority, a public body corporate and "
              "politic organized under Connecticut General Statutes § 8-125 et seq., 75 Municipal Plaza, Port "
              "Calloway, Connecticut 06801. Tenant: Meridian Gateway Holdings LLC, a Delaware limited liability "
              "company, 400 Harborview Drive, Suite 1200, Port Calloway, Connecticut 06801.")
    para(doc, "**2. Premises.** The land located at 10–30 Pier Street, Port Calloway, Connecticut 06801, Assessor's "
              "Parcel No. 127-003-0045, containing approximately 3.2 acres (139,392 square feet), as more particularly "
              "described on Schedule 1 to this Memorandum (being Exhibit A to the Ground Lease).")
    para(doc, "**3. Term.** Ninety-nine (99) years, commencing on the Lease Commencement Date (targeted October 1, "
              "2025) and expiring September 30, 2124, unless sooner terminated or extended in accordance with the "
              "Ground Lease.")
    para(doc, "**4. Permitted Uses.** Residential rental apartments, Class A office, ground-floor retail, "
              "restaurants, accessory parking, residential lobby and amenity space and accessory uses, in each case "
              "as more particularly set forth in Article 15 of the Ground Lease.")
    para(doc, "**5. Rent.** Initial annual Base Rent of $2,850,000, escalating at 2.5% per annum through Lease Year "
              "15, with Rent Resets thereafter as provided in Article 4, plus Percentage Rent as provided in "
              "Article 5, in each case as more particularly set forth in the Ground Lease.")
    para(doc, "**6. Notice of Restrictions and Rights.** The Premises are subject to (a) the Environmental Land Use "
              "Restriction recorded at Volume 412, Page 88 of the Port Calloway Land Records; (b) the Right of First "
              "Refusal described in Article 11 of the Ground Lease; (c) the affordable housing covenant described in "
              "Section 14.5 of the Ground Lease and in the Declaration of Restrictive Covenants recorded at Volume "
              "408, Page 230 of the Port Calloway Land Records; (d) the public utility easement recorded at Volume "
              "388, Page 201; and (e) the public pedestrian access easement recorded at Volume 395, Page 112.")
    para(doc, "**7. Leasehold Mortgage and New Lease.** Tenant may grant one or more Leasehold Mortgages without "
              "Landlord's consent. Each Leasehold Mortgagee has the rights set forth in Article 9 of the Ground Lease, "
              "including independent cure periods, the right to a New Lease for the remainder of the Term upon any "
              "termination of the Ground Lease, and the right to foreclose and assign. The Ground Lease may not be "
              "surrendered, amended or terminated in any material respect without the consent of each Leasehold "
              "Mortgagee.")
    para(doc, "**8. Improvement Payment.** If the Ground Lease is terminated on account of a failure to achieve "
              "Milestone 1 or Milestone 3, Landlord is obligated to pay the Improvement Payment described in "
              "Section 10.6 of the Ground Lease as a condition to the effectiveness of the termination, and the "
              "Improvements do not otherwise pass to Landlord without compensation.")
    para(doc, "**9. No Option or Renewal.** Except as expressly set forth in the Ground Lease, Tenant has no renewal, "
              "extension or purchase option.")
    para(doc, "**10. Reference to Ground Lease.** Reference is made to the Ground Lease for the full terms and "
              "conditions, all of which are incorporated in this Memorandum by reference.")
    para(doc, "", space_after=12)
    para(doc, "**LANDLORD:** CITY OF PORT CALLOWAY REDEVELOPMENT AUTHORITY", space_after=16)
    para(doc, "By: ____________________________________    Date: ______________", space_after=2)
    para(doc, "Name: Paul Castignetti    Title: Executive Director", space_after=16)
    para(doc, "**TENANT:** MERIDIAN GATEWAY HOLDINGS LLC", space_after=16)
    para(doc, "By: ____________________________________    Date: ______________", space_after=2)
    para(doc, "Name: Marcus Ellison    Title: Managing Member", space_after=14)
    para(doc, "**STATE OF CONNECTICUT**", space_after=0)
    para(doc, "**COUNTY OF NEW HAVEN**", space_after=8)
    para(doc, "On this ____ day of ____________, 2025, personally appeared Paul Castignetti, Executive Director of the "
              "City of Port Calloway Redevelopment Authority, and Marcus Ellison, Managing Member of Meridian Gateway "
              "Holdings LLC, before me and acknowledged that they executed the foregoing instrument for the purposes "
              "therein contained.", space_after=14)
    para(doc, "____________________________________    Notary Public    My commission expires: ____________")
    pagebreak(doc)
    para(doc, "**SCHEDULE 1 TO MEMORANDUM OF GROUND LEASE**", space_after=2)
    para(doc, "LEGAL DESCRIPTION OF THE PREMISES", space_after=10)
    para(doc, "[Attach the legal description set forth on Exhibit A to the Ground Lease.]", italic=True)
