from helpers import *

def blocks(doc):
    # ================= COVER =================
    for _ in range(3): cover_line(doc, "", size=10, space_after=0)
    cover_line(doc, "DRAFT OF JUNE 20, 2025", size=11, bold=True, space_after=4)
    cover_line(doc, "PRIVILEGED AND CONFIDENTIAL  •  ATTORNEY WORK PRODUCT  •  FOR DISCUSSION PURPOSES ONLY",
               size=8, bold=True, space_after=2)
    cover_line(doc, "NOT FOR EXECUTION — SUBJECT TO CONTINUING REVIEW, COMMENT AND LANDLORD BOARD APPROVAL",
               size=8, italic=True, space_after=30)
    cover_line(doc, "GROUND LEASE AGREEMENT", size=22, bold=True, space_after=6)
    cover_line(doc, "(Long-Term Ground Lease — Ninety-Nine (99) Year Term)", size=11, italic=True, space_after=30)
    cover_line(doc, "by and between", size=10, italic=True, space_after=14)
    cover_line(doc, "**CITY OF PORT CALLOWAY REDEVELOPMENT AUTHORITY**", size=12, space_after=2)
    cover_line(doc, "a public body corporate and politic organized under", size=9, space_after=0)
    cover_line(doc, "Connecticut General Statutes § 8-125 et seq.", size=9, italic=True, space_after=2)
    cover_line(doc, "as Landlord", size=10, italic=True, space_after=14)
    cover_line(doc, "and", size=10, italic=True, space_after=14)
    cover_line(doc, "**MERIDIAN GATEWAY HOLDINGS LLC**", size=12, space_after=2)
    cover_line(doc, "a Delaware limited liability company", size=9, space_after=2)
    cover_line(doc, "as Tenant", size=10, italic=True, space_after=36)
    cover_line(doc, "Premises:  10–30 Pier Street, Port Calloway, Connecticut 06801", size=10, bold=True, space_after=2)
    cover_line(doc, "Assessor's Parcel No. 127-003-0045  •  Approximately 3.2 acres (139,392 square feet)", size=9, space_after=30)
    cover_line(doc, "Prepared by Hargrove & Linden LLP, Tenant's Counsel", size=9, italic=True, space_after=2)
    cover_line(doc, "1100 Constitution Avenue, Hartford, Connecticut 06103", size=9, italic=True, space_after=2)
    cover_line(doc, "Rebecca Tsang, Lead Partner  •  Jordan Abernathy, Associate Counsel", size=9, italic=True, space_after=2)
    pagebreak(doc)

    # ================= TABLE OF CONTENTS =================
    cover_line(doc, "TABLE OF CONTENTS", size=13, bold=True, space_after=12)
    toc = [
        ("ARTICLE 1", "DEFINITIONS AND INTERPRETATION"),
        ("ARTICLE 2", "PREMISES; TERM; CONDITIONS PRECEDENT; DELIVERY"),
        ("ARTICLE 3", "DEVELOPMENT, MILESTONES AND FORCE MAJEURE"),
        ("ARTICLE 4", "BASE RENT, ESCALATIONS AND RENT RESETS"),
        ("ARTICLE 5", "PERCENTAGE RENT AND GROSS REVENUES"),
        ("ARTICLE 6", "IMPOSITIONS AND THE TAX ABATEMENT"),
        ("ARTICLE 7", "ENVIRONMENTAL MATTERS AND THE REMEDIATION CREDIT"),
        ("ARTICLE 8", "SECURITY DEPOSIT AND LETTER OF CREDIT"),
        ("ARTICLE 9", "LEASEHOLD FINANCING; LENDER PROTECTIONS; SNDA; NEW LEASE"),
        ("ARTICLE 10", "DEFAULTS, REMEDIES AND MILESTONE TERMINATION"),
        ("ARTICLE 11", "ASSIGNMENT, SUBLETTING, PERMITTED TRANSFERS AND RIGHT OF FIRST REFUSAL"),
        ("ARTICLE 12", "INSURANCE"),
        ("ARTICLE 13", "CASUALTY AND CONDEMNATION"),
        ("ARTICLE 14", "OPERATION, MAINTENANCE, OPEN SPACE, BULKHEAD AND ALTERATIONS"),
        ("ARTICLE 15", "COMPLIANCE WITH LAWS; FLOOD RESILIENCE; ELUR"),
        ("ARTICLE 16", "TITLE, PERMITTED EXCEPTIONS, QUIET ENJOYMENT AND ESTOPPELS"),
        ("ARTICLE 17", "SURRENDER; END OF TERM; REMOVAL; HOLDOVER"),
        ("ARTICLE 18", "REPRESENTATIONS, WARRANTIES AND COVENANTS"),
        ("ARTICLE 19", "NOTICES"),
        ("ARTICLE 20", "MISCELLANEOUS"),
        ("", "SIGNATURE PAGES AND ACKNOWLEDGMENTS"),
        ("", "EXHIBITS A THROUGH G"),
    ]
    for n, t in toc:
        p = doc.add_paragraph()
        p.paragraph_format.space_after = Pt(5)
        p.paragraph_format.left_indent = Inches(0.15)
        runs(p, (n + "   " if n else "") + t, size=9.5, bold=bool(t))
    p = doc.add_paragraph(); p.paragraph_format.space_before = Pt(18)
    runs(p, "Exhibits", size=10, bold=True)
    ex = [
        ("EXHIBIT A", "Legal Description of the Premises"),
        ("EXHIBIT B", "Permitted Exceptions"),
        ("EXHIBIT C", "Development Milestones and Extension Schedule"),
        ("EXHIBIT D", "Base Rent Schedule, Rent Reset and Percentage Rent Mechanics"),
        ("EXHIBIT E", "Form of Letter of Credit"),
        ("EXHIBIT F", "Required Terms of SNDA"),
        ("EXHIBIT G", "Form of Memorandum of Ground Lease"),
    ]
    for n, t in ex:
        p = doc.add_paragraph(); p.paragraph_format.space_after = Pt(4)
        p.paragraph_format.left_indent = Inches(0.15)
        runs(p, n + "   " + t, size=9.5)
    pagebreak(doc)

    # ================= PREAMBLE / RECITALS =================
    cover_line(doc, "GROUND LEASE AGREEMENT", size=13, bold=True, space_after=12)
    para(doc, "This **GROUND LEASE AGREEMENT** (this \"**Lease**\") is made and entered into as of "
              "__________________, 2025 (the \"**Effective Date**\"), by and between **CITY OF PORT CALLOWAY "
              "REDEVELOPMENT AUTHORITY**, a public body corporate and politic organized and existing under the "
              "provisions of Connecticut General Statutes § 8-125 *et seq.*, having its principal offices at "
              "75 Municipal Plaza, Port Calloway, Connecticut 06801 (the \"**Landlord**\" or the \"**Authority**\"), "
              "and **MERIDIAN GATEWAY HOLDINGS LLC**, a Delaware limited liability company duly formed on "
              "August 14, 2019, registered to do business in the State of Connecticut, having its principal place "
              "of business at 400 Harborview Drive, Suite 1200, Port Calloway, Connecticut 06801 (the \"**Tenant**\").")
    art(doc, "Recitals")
    rec = [
        ("A.", "Landlord holds fee simple title to that certain parcel of land located at 10–30 Pier Street, "
               "Port Calloway, Connecticut 06801, identified as Assessor's Parcel No. 127-003-0045, containing "
               "approximately 3.2 acres (139,392 square feet), as more particularly described on **Exhibit A** "
               "attached hereto (the \"**Premises**\"), which Premises Landlord acquired through eminent domain "
               "proceedings concluded in 2012."),
        ("B.", "The Premises are located within the Port Calloway Waterfront Revitalization District and are zoned "
               "WRD-3 (Mixed-Use High Density) under the Port Calloway Zoning Regulations, and are subject to that "
               "certain Environmental Land Use Restriction recorded March 22, 2018, at Volume 412, Page 88 of the "
               "Port Calloway Land Records (the \"**ELUR**\") and to the other matters described on **Exhibit B**."),
        ("C.", "Tenant intends to develop on the Premises a mixed-use project consisting of a twenty-eight (28) story "
               "residential rental tower, a six (6) story Class A office building, ground-floor retail space, "
               "accessory structured and/or below-grade parking, and not less than eight thousand (8,000) square feet "
               "of publicly accessible waterfront open space, together with related amenities and improvements "
               "(collectively, the \"**Project**\"), at an estimated total project cost of Four Hundred Twenty-Five "
               "Million Dollars ($425,000,000)."),
        ("D.", "Landlord and Tenant are parties to that certain binding term sheet dated June 10, 2025 (the "
               "\"**Term Sheet**\") setting forth the principal business terms of this Lease, and Landlord's Board of "
               "Commissioners adopted Resolution No. 2025-047 on June 5, 2025, authorizing the Executive Director to "
               "negotiate, execute and deliver this Lease."),
        ("E.", "Tenant has obtained a construction loan commitment from Bayside Federal Lending Corp. in the "
               "principal amount of Two Hundred Eighty-Five Million Dollars ($285,000,000), and equity commitments "
               "from Coventry Capital Partners LP in the amount of Ninety-Five Million Dollars ($95,000,000) and from "
               "Tenant's members in the amount of Forty-Five Million Dollars ($45,000,000), each of which is "
               "conditioned upon this Lease being in form and substance satisfactory to the construction lender and "
               "containing the leasehold mortgage protections set forth in Article 9."),
        ("F.", "The environmental condition of the Premises has been evaluated in the Phase I Environmental Site "
               "Assessment dated March 15, 2025 and the Phase II Environmental Site Assessment dated May 2, 2025, "
               "each prepared by Halcyon Environmental Consultants Inc., and the parties have agreed upon the "
               "allocation of remediation responsibility and the Remediation Credit set forth in Article 7."),
        ("G.", "The redevelopment of the Premises serves a valid public purpose and is consistent with Landlord's "
               "waterfront revitalization plan, and the parties intend that this Lease confer upon Tenant a "
               "financeable, institutional-quality leasehold estate for the full ninety-nine (99) year Term."),
    ]
    for lbl, txt in rec:
        p = doc.add_paragraph()
        pf = p.paragraph_format
        pf.left_indent = Inches(0.4); pf.first_line_indent = Inches(-0.4)
        pf.space_after = Pt(6); pf.tab_stops.add_tab_stop(Inches(0.4))
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        runs(p, lbl + "\t" + txt)
    para(doc, "**NOW, THEREFORE**, in consideration of the mutual covenants contained herein, the Remediation "
              "Credit, the Security Deposit, and other good and valuable consideration, the receipt and sufficiency "
              "of which are hereby acknowledged, Landlord and Tenant agree as follows:")
    pagebreak(doc)

    # ================= ARTICLE 1 =================
    art(doc, "Article 1. Definitions and Interpretation")
    sec(doc, "1.1", "Defined Terms", "Capitalized terms used in this Lease have the meanings set forth in this "
        "Article 1. Terms defined elsewhere in this Lease have the meanings given to them in the provision in "
        "which they are defined.")
    defs = [
        ("Affiliate", "means, with respect to any Person, any other Person that directly or indirectly controls, is "
         "controlled by, or is under common control with such Person; any entity in which Marcus Ellison holds a "
         "direct or indirect controlling interest; Coventry Capital Partners LP, any fund, vehicle, account or "
         "separate account managed or advised by Coventry Capital Partners LP or its affiliates, and any of their "
         "respective affiliates, subsidiaries, general partners, managers and related funds; and any entity "
         "resulting from an internal reorganization or restructuring of Tenant's ownership. For purposes of this "
         "definition, \"control\" means the direct or indirect power to direct or cause the direction of the "
         "management and policies of a Person, whether through the ownership of voting securities, by contract or "
         "otherwise."),
        ("Applicable Law", "means all present and future federal, state and local statutes, ordinances, codes, "
         "rules, regulations, orders, permits, judgments and administrative determinations applicable to the "
         "Premises, the Improvements or the use or operation thereof, including the Connecticut General Statutes, "
         "the Port Calloway Zoning Regulations, the Connecticut Remediation Standard Regulations, the ELUR, the "
         "Connecticut State Building Code, the Port Calloway Flood Damage Prevention Ordinance, the federal Fair "
         "Housing Act and all applicable coastal, tidal wetlands and floodplain management requirements."),
        ("Appraised Value", "means, with respect to the Improvements as of any date, the fair market value of the "
         "Improvements (exclusive of the value of Landlord's fee interest in the land, and disregarding any "
         "depreciation attributable to the remaining Term or to the reversion), determined in accordance with "
         "Section 10.8."),
        ("Base Rent", "means the annual rent payable under Article 4, as escalated and reset from time to time, "
         "together with all interest and charges thereon."),
        ("Breakpoint", "means Twenty-Eight Million Five Hundred Thousand Dollars ($28,500,000) for Lease Year 6, as "
         "adjusted and reset in accordance with Section 5.3."),
        ("Business Day", "means any day other than a Saturday, Sunday or day on which commercial banks in the State "
         "of Connecticut are authorized or required by law to be closed."),
        ("Certificate of Occupancy", "means a temporary or permanent certificate of occupancy (or equivalent "
         "certificate of completion or use) issued by the Port Calloway Building Official for any portion of the "
         "Project."),
        ("Documented Damages", "means, with respect to Landlord and any Milestone Default or other Event of Default, "
         "Landlord's actual, reasonable and documented out-of-pocket losses and costs proximately caused by such "
         "default, determined and limited as provided in Section 10.7, and expressly excluding any amount "
         "attributable to the value of the Improvements, anticipated Percentage Rent, lost tax revenue, lost "
         "development opportunity, or any consequential, punitive or speculative damages."),
        ("ELUR", "has the meaning given in Recital B, together with any modification, amendment, renewal or "
         "replacement thereof approved by the Connecticut Department of Energy and Environmental Protection "
         "(\"**DEEP**\")."),
        ("Environmental Laws", "means all Applicable Laws relating to pollution, contamination, protection of the "
         "environment, natural resources, human health or Hazardous Materials, including the Connecticut Remediation "
         "Standard Regulations, Conn. Agencies Regs. § 22a-133k-1 *et seq.*, Connecticut General Statutes § 22a-133o "
         "and § 22a-134 *et seq.*, the federal Comprehensive Environmental Response, Compensation, and Liability Act, "
         "and the federal Resource Conservation and Recovery Act."),
        ("Event of Default", "means an event described in Section 10.1 or Section 10.2."),
        ("Force Majeure Event", "means any of the following events or conditions, to the extent beyond Tenant's "
         "reasonable control and not caused by Tenant's fault or negligence: acts of God; fire; flood; storm surge; "
         "hurricane, tropical storm or nor'easter; unusually severe weather; sea level rise or tidal flooding "
         "affecting the Premises; earthquake; war; terrorism; civil unrest; epidemic or pandemic; strikes, lockouts "
         "or other labor disputes; shortages or disruption in the supply of labor, materials, equipment or "
         "utilities; governmental orders, moratoria, shutdowns or delays (including delays in the issuance of "
         "building, zoning, coastal, tidal wetlands, DEEP, ELUR-related, floodplain or other permits or approvals "
         "and delays caused by appeals or third-party challenges); delay in the issuance of a Certificate of "
         "Occupancy; discovery of previously unknown or undocumented subsurface conditions, contamination or "
         "archeological or historic resources; failure of utilities or transportation infrastructure; and any act, "
         "omission or delay of Landlord, the City of Port Calloway or any other governmental authority."),
        ("Gross Revenues", "has the meaning given in Section 5.2."),
        ("Hazardous Materials", "means petroleum and petroleum products (including total petroleum hydrocarbons, "
         "gasoline-range and diesel-range organics), volatile and semi-volatile organic compounds, polychlorinated "
         "biphenyls, heavy metals, asbestos, polychlorinated dibenzodioxins and dibenzofurans, per- and "
         "polyfluoroalkyl substances, and any other substance, material or waste that is regulated as hazardous, "
         "toxic or a pollutant under any Environmental Law."),
        ("Improvements", "means all buildings, structures, fixtures, site work, utilities, landscaping, bulkhead "
         "repairs and replacements, and other improvements of every kind now or hereafter constructed, installed or "
         "placed on the Premises by or for Tenant, including the Project, but excluding Tenant's Trade Fixtures."),
        ("Improvement Payment", "has the meaning given in Section 10.6."),
        ("Impositions", "has the meaning given in Section 6.2."),
        ("Landlord Delay", "means any delay in the performance of Tenant's obligations under this Lease (including "
         "the achievement of any Milestone) to the extent caused by (a) any failure by Landlord to perform any "
         "obligation under this Lease within the time required, including any failure to deliver a consent, "
         "approval, estoppel, SNDA or other instrument within the applicable period; (b) any failure by Landlord or "
         "the City of Port Calloway to obtain, maintain or cooperate in obtaining any governmental approval within "
         "the control of Landlord or the City of Port Calloway; (c) any act, omission, negligence or interference by "
         "Landlord, its agents, contractors or invitees; or (d) any failure of the Premises to be delivered in the "
         "condition required by Section 2.9."),
        ("Lease Year", "means each successive period of twelve (12) full calendar months during the Term, the first "
         "such period commencing on the Rent Commencement Date and each subsequent period commencing on the "
         "anniversary of the Rent Commencement Date; provided that if the Rent Commencement Date is not the first "
         "day of a calendar month, Lease Year 1 shall commence on the Rent Commencement Date and shall end on the "
         "last day of the calendar month in which the first anniversary of the Rent Commencement Date occurs."),
        ("Leasehold Mortgage", "means any mortgage, deed of trust, deed to secure debt or other security instrument "
         "(including any amendment, restatement, renewal, extension, consolidation, replacement or refinancing "
         "thereof, and any assignment of leases and rents, security agreement or other ancillary instrument executed "
         "in connection therewith) encumbering Tenant's leasehold interest in the Premises and the Improvements, "
         "whether granted to the Construction Lender or to any other institutional lender, together with all "
         "collateral therefor."),
        ("Leasehold Mortgagee", "means the holder of any Leasehold Mortgage from time to time, including the "
         "Construction Lender, and each of their respective successors and assigns, designees and nominees, and any "
         "purchaser at a foreclosure sale or transferee pursuant to a deed in lieu of foreclosure, in each case that "
         "has delivered to Landlord a written notice designating an address for notices under Section 19.1."),
        ("Construction Lender", "means Bayside Federal Lending Corp., a Connecticut-chartered commercial bank, and "
         "its successors and assigns."),
        ("Lender Cure Period", "has the meaning given in Section 9.5."),
        ("Letter of Credit", "has the meaning given in Section 8.2."),
        ("Milestone", "means each of Milestone 1, Milestone 2, Milestone 3 and Milestone 4 described in Section 3.3 "
         "and **Exhibit C**."),
        ("Milestone Cure Period", "means, with respect to a Milestone Default, the period of one hundred eighty (180) "
         "calendar days following Tenant's receipt of a Milestone Notice, as extended pursuant to Section 10.5(c)."),
        ("Milestone Default", "means Tenant's failure to achieve Milestone 1 or Milestone 3 by the applicable "
         "Milestone Deadline, as such deadline is extended pursuant to Article 3."),
        ("Milestone Deadline", "means, with respect to each Milestone, the corresponding deadline set forth in "
         "Section 3.3 and Exhibit C, as extended pursuant to Section 3.4."),
        ("Memorandum of Lease", "means the Memorandum of Ground Lease substantially in the form attached as "
         "Exhibit G, to be recorded in the Port Calloway Land Records pursuant to Section 2.10."),
        ("Permitted Uses", "means the uses of the Premises permitted under Section 15.2."),
        ("Milestone Notice", "has the meaning given in Section 10.5(a)."),
        ("New Lease", "has the meaning given in Section 9.6."),
        ("Permitted Exceptions", "means the matters described on **Exhibit B** and such other exceptions as are "
         "approved in writing by Tenant and each Leasehold Mortgagee."),
        ("Permitted Transfers", "has the meaning given in Section 11.3."),
        ("Person", "means any individual, corporation, limited liability company, partnership, joint venture, trust, "
         "estate, governmental authority or other entity."),
        ("Pre-Existing Environmental Condition", "means any condition of the Premises arising from acts, omissions or "
         "operations occurring before the Lease Commencement Date, including the presence of Hazardous Materials in "
         "soil, soil gas, groundwater, sediment or fill; any condition identified in the Phase I Environmental Site "
         "Assessment dated March 15, 2025 or the Phase II Environmental Site Assessment dated May 2, 2025; any "
         "condition attributable to the former ship repair and dry dock operations conducted on the Premises from "
         "approximately 1942 through 1987, to the former underground storage tanks formerly located in the northwest "
         "corner of the Premises, to the filled former dry dock basin, or to the demolition, grading or remedial "
         "activities conducted by or for Landlord; and any condition subject to or arising under the ELUR."),
        ("Public Open Space", "means the not less than eight thousand (8,000) square feet of publicly accessible open "
         "space to be provided on the waterfront (eastern) side of the Premises in accordance with Section 14.4."),
        ("Related Lender", "means any Leasehold Mortgagee and any participant, co-lender, assignee or affiliate of a "
         "Leasehold Mortgagee, and any trustee, receiver or servicer acting for any of them."),
        ("Remediation Credit", "has the meaning given in Section 7.2."),
        ("Rent", "means, collectively, Base Rent, Percentage Rent and all other sums payable by Tenant to Landlord "
         "under this Lease, whether or not denominated as rent."),
        ("Rent Commencement Date", "means the earlier of (a) the date that is thirty-six (36) months after the Lease "
         "Commencement Date (being October 1, 2028 if the Lease Commencement Date is October 1, 2025), and (b) the "
         "Rent Trigger Date, if any, determined in accordance with Section 2.5."),
        ("Rent Reset Date", "means each of Lease Years 16, 26, 36, 46, 56, 66, 76, 86 and 96."),
        ("ROFR", "has the meaning given in Section 11.5."),
        ("Security Deposit", "means the security deposit described in Article 8, whether held in the form of a Letter "
         "of Credit or as a cash deposit."),
        ("SNDA", "means a subordination, non-disturbance and attornment agreement between Landlord, Tenant and a "
         "Leasehold Mortgagee, containing not less than the terms set forth on **Exhibit F**."),
        ("Substantial Completion", "means, with respect to Phase 1, the issuance of a Certificate of Occupancy for "
         "the Residential Tower and the ground-floor retail space such that the Residential Tower is ready for "
         "residential occupancy and the retail space is available for tenant fit-out, and with respect to Phase 2, "
         "the issuance of a Certificate of Occupancy for the Office Building, in each case notwithstanding the "
         "completion of punch-list items, minor incomplete work, and outstanding tenant fit-out work."),
        ("Tax Abatement", "means the fifteen (15) year phased abatement of real property taxes applicable to the "
         "Project described in Section 6.6."),
        ("Tax Abatement Agreement", "means the agreement between Tenant and the City of Port Calloway, approved by "
         "all requisite action of the City of Port Calloway, implementing the Tax Abatement."),
        ("Term", "means the term of this Lease described in Section 2.2."),
        ("Termination Date", "means the effective date of any termination of this Lease."),
        ("Trade Fixtures", "means Tenant's movable furniture, trade fixtures, equipment, appliances, signage, "
         "inventory and personal property that are not incorporated into the Improvements and that can be removed "
         "without material structural damage."),
        ("Unreimbursed Hard Costs", "means, as of any date, the aggregate hard construction costs actually incurred "
         "and paid by Tenant or its Affiliates in connection with the design, permitting, construction, restoration "
         "and equipping of the Improvements (including the cost of the Environmental Remediation Work to the extent "
         "borne by Tenant and not offset by the Remediation Credit), net of (a) all insurance proceeds, condemnation "
         "awards and other recoveries theretofore received by or for the account of Tenant in respect of the "
         "Improvements and not applied to restoration, and (b) any amount funded by Landlord or the City of Port "
         "Calloway, all as substantiated by Tenant's construction records, draw schedules, invoices and paid "
         "contractor applications."),
    ]
    for term, text in defs:
        defn(doc, term, text)

    sec(doc, "1.2", "Interpretation", "In this Lease, unless the context otherwise requires: (a) the words "
        "\"include,\" \"includes\" and \"including\" are deemed to be followed by \"without limitation\"; (b) "
        "\"hereof,\" \"herein\" and \"hereunder\" refer to this Lease as a whole; (c) references to Articles, "
        "Sections and Exhibits are to this Lease; (d) headings and the table of contents are for convenience only "
        "and do not affect interpretation; (e) references to any statute or regulation include any successor "
        "provision and the rules and regulations promulgated thereunder; (f) references to \"days\" are to calendar "
        "days unless Business Days are specified; (g) \"$\" and \"Dollars\" mean United States dollars; (h) the "
        "singular includes the plural and vice versa; and (i) this Lease has been negotiated between sophisticated "
        "parties with the assistance of counsel and shall not be construed against either party as the drafter.")
    sec(doc, "1.3", "No Strict Construction Against Either Party",
        "Landlord has been represented by Pryor Whitfield & Koss LLP and Tenant has been represented by Hargrove & "
        "Linden LLP in the negotiation of this Lease, and no rule of construction resolving ambiguities against the "
        "drafting party shall be applied.")
