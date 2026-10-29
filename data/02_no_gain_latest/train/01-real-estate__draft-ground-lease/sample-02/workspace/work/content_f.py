from helpers import *

def blocks(doc):
    art(doc, "Article 17. Surrender; End of Term; Removal; Holdover")
    sec(doc, "17.1", "Surrender", "Upon the Expiration Date or any earlier Termination Date, Tenant shall surrender the "
        "Premises to Landlord in good condition, order and repair, reasonable wear and tear and casualty excepted, free "
        "and clear of all liens, encumbrances and tenancies created by Tenant (other than subleases that Landlord is "
        "required to recognize under Section 9.6(e) or Section 10.6(f)), and in compliance with the ELUR and all "
        "Environmental Laws.")
    sec(doc, "17.2", "Improvements at End of Term", "Upon the Expiration Date (as distinguished from a termination "
        "under Section 10.5, which is governed by Section 10.6), the Improvements shall become the sole property of "
        "Landlord without payment, compensation or reimbursement to Tenant, and Tenant shall have no claim for "
        "compensation, unjust enrichment, betterment or otherwise in respect of the Improvements, the Environmental "
        "Remediation Work, the Public Open Space improvements or any other work performed by Tenant on the Premises.")
    note(doc, "[**Tenant position, to be negotiated.** Because the Tenant will have invested in excess of $425,000,000 "
              "in Improvements that pass to Landlord without compensation at the end of the Term, Tenant proposes one "
              "of the following: (a) the extension option in Section 2.7; (b) an option to purchase Landlord's fee "
              "interest at the then-appraised fair market value, exercisable during the final ten (10) years of the "
              "Term; or (c) a right to remove or to require Landlord to purchase Tenant's Trade Fixtures and the "
              "remediable value of the Environmental Remediation Work. Tenant also notes that the fair market value of "
              "the Improvements at the end of a 99-year term will be heavily depreciated, and that the value of the "
              "reversion to Landlord is already captured in the Base Rent structure.]")
    sec(doc, "17.3", "Removal of Trade Fixtures", "Tenant may remove its Trade Fixtures at any time during the Term and "
        "within sixty (60) days after the Expiration Date or Termination Date, provided that Tenant repairs any damage "
        "caused by removal. Tenant may abandon any Trade Fixtures it elects not to remove, and Landlord may dispose of "
        "them at Tenant's cost if Tenant fails to remove them within such period.")
    sec(doc, "17.4", "Holdover", "If Tenant remains in possession of the Premises after the Expiration Date with "
        "Landlord's written consent, the tenancy shall be month-to-month on the terms of this Lease except that Base "
        "Rent shall be one hundred twenty-five percent (125%) of the Base Rent in effect on the Expiration Date. If "
        "Tenant remains in possession without Landlord's consent, Base Rent shall be one hundred fifty percent (150%) "
        "of such Base Rent, and such amounts shall be Landlord's sole and exclusive remedy for the holdover for the "
        "first ninety (90) days. Nothing in this Section 17.4 shall limit Tenant's right to remain in possession under "
        "any extension right under Section 2.7 or to remain in possession pending resolution of a good-faith dispute "
        "as to the Expiration Date.")
    sec(doc, "17.5", "Continuing Environmental Obligations", "Tenant's obligations under Article 7 with respect to "
        "conditions created by Tenant, and Landlord's obligations under Section 7.5 with respect to Pre-Existing "
        "Environmental Conditions, shall survive the Expiration Date or any Termination Date.")

    # ================= ARTICLE 18 =================
    art(doc, "Article 18. Representations, Warranties and Covenants")
    sec(doc, "18.1", "Landlord's Representations, Warranties and Covenants", "Landlord represents, warrants and "
        "covenants to Tenant, as of the Effective Date and as of the Lease Commencement Date, that:")
    lr = [
        "Landlord is a public body corporate and politic duly organized, validly existing and in good standing under "
        "Connecticut General Statutes § 8-125 et seq., and has full power and authority to own, lease and convey the "
        "leasehold estate and to execute, deliver and perform this Lease;",
        "the execution, delivery and performance of this Lease have been duly authorized by Resolution No. 2025-047 "
        "and by all other necessary action of Landlord's Board of Commissioners, and no further authorization, consent "
        "or approval (including under Connecticut General Statutes § 8-125 et seq., the Authority's bylaws, the "
        "Connecticut Freedom of Information Act or any other Applicable Law) is required for Landlord to execute and "
        "deliver this Lease or to perform its obligations under Sections 9.6 and 10.6;",
        "this Lease constitutes the legal, valid and binding obligation of Landlord, enforceable against Landlord in "
        "accordance with its terms, subject only to applicable bankruptcy, insolvency, reorganization and similar laws "
        "and to general principles of equity;",
        "Landlord holds fee simple title to the Premises free and clear of all liens, encumbrances, leases, licenses "
        "and options other than the Permitted Exceptions, and there is no pending or, to Landlord's knowledge, "
        "threatened condemnation, reverter, escheat, tax sale or other proceeding affecting title to the Premises;",
        "to Landlord's actual knowledge, there is no litigation, arbitration, governmental investigation or "
        "enforcement proceeding pending or threatened against Landlord, the Premises or the Project that would "
        "materially and adversely affect the Premises, the leasehold estate or Landlord's ability to perform this "
        "Lease;",
        "Landlord has delivered to Tenant all environmental reports, studies, assessments, LUST files, underground "
        "storage tank records, DEEP correspondence, ELUR documents and notices of violation in Landlord's possession "
        "or control relating to the Premises, and, to Landlord's actual knowledge, there are no Hazardous Materials at "
        "the Premises other than as disclosed in the Phase I and Phase II Environmental Site Assessments and the ELUR, "
        "and no notice of violation, order or information request from DEEP or any other authority is outstanding;",
        "the Premises are not subject to any reverter, reversionary interest, residual claim, former owner claim or "
        "other interest arising out of the eminent domain proceedings by which Landlord acquired title that could "
        "impair Tenant's leasehold estate, and all statutory appeal periods under Connecticut General Statutes § 8-132 "
        "have expired;",
        "there are no service contracts, management agreements, equipment leases, union agreements or other "
        "commitments affecting the Premises that will be binding on Tenant after the Lease Commencement Date;",
        "Landlord is not in default under any agreement with the City of Port Calloway or any other governmental body "
        "that would affect the Premises, the Tax Abatement or this Lease; and",
        "Landlord has made no promise, representation or inducement to Tenant other than those expressly set forth in "
        "this Lease.",
    ]
    for i, t in enumerate(lr):
        sub(doc, "(%s)" % chr(97 + i), t)
    para(doc, "Landlord's representations and warranties in this Section 18.1 shall survive the Lease Commencement "
              "Date and shall not merge into any deed, lease, memorandum or other instrument.")
    sec(doc, "18.2", "Tenant's Representations and Warranties", "Tenant represents and warrants to Landlord that: "
        "(a) Tenant is a limited liability company duly organized, validly existing and in good standing under the laws "
        "of the State of Delaware and is duly qualified to transact business in the State of Connecticut; (b) Tenant "
        "has full power and authority to execute, deliver and perform this Lease, and such execution, delivery and "
        "performance have been duly authorized by all necessary action of Tenant and its members; (c) this Lease "
        "constitutes the legal, valid and binding obligation of Tenant, enforceable in accordance with its terms; "
        "(d) no bankruptcy, receivership or insolvency proceeding is pending or contemplated by or against Tenant; and "
        "(e) no litigation is pending or threatened against Tenant that would materially and adversely affect Tenant's "
        "ability to perform this Lease.")
    sec(doc, "18.3", "Landlord's Covenants", "Landlord further covenants that it shall (a) maintain its existence and "
        "good standing and all authorizations necessary to perform this Lease; (b) not voluntarily take any action to "
        "dissolve, wind up or divest itself of the Premises other than in compliance with Section 9.11; (c) not "
        "advocate or support the repeal or reduction of the Tax Abatement; and (d) at all times act in good faith and "
        "in a commercially reasonable manner in the exercise of any consent, approval or discretion under this Lease.")

    # ================= ARTICLE 19 =================
    art(doc, "Article 19. Notices")
    sec(doc, "19.1", "Addresses", "All notices, demands, consents and other communications under this Lease shall be in "
        "writing and shall be delivered to the following addresses (or such other address as a party may designate by "
        "not less than ten (10) days' prior written notice):")
    table(doc,
          [["Party", "Notice Address"],
           ["Landlord", "City of Port Calloway Redevelopment Authority\n75 Municipal Plaza, Port Calloway, CT 06801\n"
            "Attention: Executive Director\n\nwith a copy to: Pryor Whitfield & Koss LLP, 55 Courthouse Square, "
            "Port Calloway, CT 06801, Attention: Howard Koss, Esq."],
           ["Tenant", "Meridian Gateway Holdings LLC\n400 Harborview Drive, Suite 1200, Port Calloway, CT 06801\n"
            "Attention: Marcus Ellison, Managing Member\n\nwith a copy to: Hargrove & Linden LLP, 1100 Constitution "
            "Avenue, Hartford, CT 06103, Attention: Rebecca Tsang, Esq."],
           ["Leasehold Mortgagee", "As designated from time to time pursuant to Section 9.2.\n"
            "Bayside Federal Lending Corp., 200 Atlantic Boulevard, Stamford, CT 06902, Attention: Sandra Milliken, "
            "Senior Vice President, Commercial Real Estate Lending, with a copy to Lender's counsel at the address "
            "designated by Lender."]],
          [1.3, 5.2], size=8.5, header=True)
    sec(doc, "19.2", "Method of Delivery; Effectiveness", "Notices shall be deemed given (a) upon delivery, if "
        "delivered by hand (with written receipt), (b) one (1) Business Day after deposit with a nationally recognized "
        "overnight courier, (c) three (3) Business Days after deposit in the United States mail, certified or "
        "registered, return receipt requested, postage prepaid, or (d) upon confirmed transmission, if sent by "
        "electronic mail with a simultaneous copy sent by one of the methods in clauses (a) through (c). Notices of "
        "default, notices of termination and notices of Milestone Default must be given by a method described in "
        "clauses (a), (b) or (c) and may not be given solely by electronic mail.")
    sec(doc, "19.3", "Copies Not a Condition", "The failure to deliver a copy of any notice to a party's counsel or to "
        "a Leasehold Mortgagee's counsel shall not affect the effectiveness of the notice to the addressee, except "
        "that failure to deliver to a Leasehold Mortgagee shall render the notice ineffective as to that Leasehold "
        "Mortgagee and shall toll the commencement of its Lender Cure Period.")

    # ================= ARTICLE 20 =================
    art(doc, "Article 20. Miscellaneous")
    sec(doc, "20.1", "Governing Law", "This Lease shall be governed by and construed in accordance with the laws of the "
        "State of Connecticut, without regard to its conflict of laws principles. The parties acknowledge that the "
        "Premises are located in New Haven County, Connecticut.")
    sec(doc, "20.2", "Dispute Resolution", "Any dispute, claim or controversy arising out of or relating to this Lease "
        "(other than an application for injunctive relief or specific performance, or an action to collect a "
        "liquidated sum, which may be brought immediately) shall be submitted first to non-binding mediation before a "
        "single mediator acceptable to both parties, in New Haven, Connecticut, within sixty (60) days after written "
        "request by either party. Each party shall bear its own costs of the mediation and half of the mediator's "
        "fees. If the dispute is not resolved within ninety (90) days after the mediation request, either party may "
        "commence an action in the Superior Court of the State of Connecticut, Judicial District of New Haven "
        "(or, if such court lacks jurisdiction, in the United States District Court for the District of Connecticut). "
        "Each party consents to the personal jurisdiction and venue of such courts. Pending resolution, the parties "
        "shall continue to perform their obligations under this Lease, and Tenant shall continue to pay undisputed "
        "Rent.")
    note(doc, "[**Drafting flag:** The Term Sheet (§ 19) refers to the \"Connecticut Superior Court, Judicial District "
              "of Port Calloway,\" while the Title Commitment (Schedule A, § 4 and Exception No. 10) refers to the "
              "\"Superior Court of Connecticut, Judicial District of New Haven.\" There is no Judicial District of "
              "Port Calloway; the Premises are in New Haven County. The clause above uses the correct district. The "
              "parties have also elected mediation followed by litigation rather than binding arbitration because "
              "Connecticut law limits the ability of a public body to agree to binding arbitration absent express "
              "statutory authority; the arbitrability of disputes involving the Authority should be confirmed with "
              "Connecticut counsel before any arbitration provision is accepted.]")
    sec(doc, "20.3", "Attorneys' Fees", "In any action or proceeding between the parties arising out of this Lease, the "
        "prevailing party shall be entitled to recover its reasonable attorneys' fees, costs and disbursements from the "
        "non-prevailing party.")
    sec(doc, "20.4", "Freedom of Information", "The parties acknowledge that Landlord is a public agency subject to the "
        "Connecticut Freedom of Information Act, Connecticut General Statutes § 1-200 et seq., and that this Lease and "
        "the statements and other information delivered under this Lease may be subject to public disclosure. Landlord "
        "shall, to the extent permitted by Applicable Law, (a) treat Tenant's financial statements, pro forma "
        "information, rent rolls, construction budgets and financing terms as confidential commercial or financial "
        "information within the meaning of Connecticut General Statutes § 1-210(b)(5); (b) notify Tenant promptly of "
        "any request for disclosure and cooperate with Tenant's efforts to obtain confidential treatment; and (c) "
        "assert all available exemptions before disclosing any such information. Nothing in this Section 20.4 shall "
        "require Landlord to violate Applicable Law or to withhold this Lease itself, and Landlord shall not be liable "
        "to Tenant for any disclosure required by Applicable Law or ordered by a court of competent jurisdiction.")
    sec(doc, "20.5", "Confidentiality", "Tenant acknowledges that this Lease, and any memorandum of it, will be "
        "recorded and available to the public. Tenant shall not be required to keep the terms of this Lease "
        "confidential, and Landlord shall not disclose any Leasehold Mortgagee's financial information or loan terms "
        "without the consent of the applicable Leasehold Mortgagee, except as required by Applicable Law.")
    sec(doc, "20.6", "Broker", "The parties represent to each other that no broker, finder or other intermediary has "
        "been engaged in connection with this transaction and each shall indemnify the other against any claim for a "
        "commission or fee arising from its own acts.")
    sec(doc, "20.7", "Entire Agreement; Supersession of Term Sheet", "This Lease, together with its Exhibits, contains "
        "the entire agreement of the parties with respect to the Premises and supersedes all prior negotiations, term "
        "sheets, letters of intent and understandings, including the Term Sheet dated June 10, 2025 and the "
        "correspondence between the parties, all of which shall be of no further force or effect as of the Effective "
        "Date, except that the exclusivity obligations of the Term Sheet shall survive to the extent, and for so long "
        "as, expressly provided in the Term Sheet. In the event of any conflict between this Lease and the Term Sheet, "
        "this Lease controls.")
    sec(doc, "20.8", "Amendment; Waiver", "This Lease may not be amended, modified or supplemented except by a written "
        "instrument executed by both parties (and consented to by each Leasehold Mortgagee to the extent required by "
        "Section 9.4). No waiver of any provision shall be effective unless in writing and signed by the waiving "
        "party, and no waiver of any breach shall be deemed a waiver of any other or subsequent breach.")
    sec(doc, "20.9", "No Partnership; Third-Party Beneficiaries", "Nothing in this Lease shall create a partnership, "
        "joint venture, joint enterprise or principal-agent relationship between the parties. Except for each "
        "Leasehold Mortgagee and each Related Lender (which are express third-party beneficiaries of Article 9 and "
        "Sections 10.5, 10.6 and 10.7), this Lease confers no rights on any Person other than the parties and their "
        "permitted successors and assigns. No subtenant or other occupant shall be a third-party beneficiary of this "
        "Lease.")
    sec(doc, "20.10", "Severability", "If any provision of this Lease is held to be invalid, illegal or unenforceable, "
        "the remaining provisions shall continue in full force and effect, and the invalid, illegal or unenforceable "
        "provision shall be reformed to the minimum extent necessary to make it valid and enforceable while preserving "
        "the parties' economic intent.")
    sec(doc, "20.11", "Time of the Essence", "Time is of the essence with respect to each date and period set forth in "
        "this Lease, except that any period that ends on a day that is not a Business Day shall be extended to the next "
        "succeeding Business Day.")
    sec(doc, "20.12", "Further Assurances", "Each party shall execute, acknowledge and deliver such further "
        "instruments, and take such further actions, as the other party or any Leasehold Mortgagee may reasonably "
        "request to carry out the purposes of this Lease, without charge.")
    sec(doc, "20.13", "Counterparts; Electronic Signature", "This Lease may be executed in any number of counterparts, "
        "each of which shall be deemed an original and all of which together shall constitute one instrument. "
        "Electronic signatures and signatures transmitted by electronic mail in portable document format shall be "
        "deemed original signatures for all purposes.")
    sec(doc, "20.14", "Landlord Authority; Approval of this Lease", "Landlord represents that its Board of Commissioners "
        "has adopted, or will adopt prior to the Lease Commencement Date, a resolution approving this Lease in the form "
        "executed by the parties and authorizing the Executive Director to execute and deliver this Lease and the "
        "instruments contemplated by it, including the SNDA, the Memorandum of Lease and any New Lease. Landlord shall "
        "deliver a certified copy of such resolution to Tenant and each Leasehold Mortgagee, together with a "
        "certificate of the Secretary or Clerk of Landlord as to the incumbency of the officers executing this Lease.")
    sec(doc, "20.15", "No Personal Liability; Recourse", "No commissioner, officer, employee or agent of Landlord shall "
        "have any personal liability under this Lease, and no such Person shall be named as a party to any action "
        "arising out of this Lease. Tenant's recourse for any obligation of Landlord under this Lease shall be to "
        "Landlord's interest in the Premises and the Improvements, the Rent and Landlord's other assets (other than "
        "assets held in trust for bondholders or otherwise restricted by Applicable Law), and not to the City of Port "
        "Calloway or to any other governmental body, municipality or public treasury.")
    sec(doc, "20.16", "Waiver of Jury Trial", "[**To be negotiated:** TO THE EXTENT PERMITTED BY APPLICABLE LAW, THE "
        "PARTIES KNOWINGLY, VOLUNTARILY AND INTENTIONALLY WAIVE ANY RIGHT TO A TRIAL BY JURY IN ANY ACTION ARISING OUT "
        "OF OR RELATING TO THIS LEASE. Landlord's ability to waive a jury trial as a public body should be confirmed "
        "with Connecticut counsel.]")
    sec(doc, "20.17", "Survival", "The provisions of this Lease that by their nature are intended to survive, including "
        "Article 7, Article 9, Sections 10.6 through 10.8, Article 17 and this Article 20, shall survive the "
        "expiration or termination of this Lease.")
    sec(doc, "20.18", "Exhibits", "The following Exhibits are attached to and incorporated in this Lease: A (Legal "
        "Description); B (Permitted Exceptions); C (Development Milestones and Extension Schedule); D (Base Rent "
        "Schedule, Rent Reset and Percentage Rent Mechanics); E (Form of Letter of Credit); F (Required Terms of "
        "SNDA); and G (Form of Memorandum of Ground Lease).")

    # ================= SIGNATURES =================
    pagebreak(doc)
    para(doc, "**IN WITNESS WHEREOF**, the parties have executed this Ground Lease Agreement as of the Effective Date.")
    para(doc, "", space_after=10)
    para(doc, "**LANDLORD:**", space_after=4)
    para(doc, "**CITY OF PORT CALLOWAY REDEVELOPMENT AUTHORITY**,", space_after=0)
    para(doc, "a public body corporate and politic", space_after=20)
    para(doc, "By: ______________________________________", space_after=2)
    para(doc, "Name: Paul Castignetti", space_after=2)
    para(doc, "Title: Executive Director", space_after=2)
    para(doc, "Date: ____________________, 2025", space_after=14)
    para(doc, "Attest:", space_after=16)
    para(doc, "By: ______________________________________", space_after=2)
    para(doc, "Name: ___________________________________", space_after=2)
    para(doc, "Title: ___________________________________", space_after=4)
    para(doc, "Authorized by Resolution No. 2025-047, adopted June 5, 2025, and by Resolution "
              "No. ______________, adopted ______________, 2025", space_after=24)
    para(doc, "**TENANT:**", space_after=4)
    para(doc, "**MERIDIAN GATEWAY HOLDINGS LLC**,", space_after=0)
    para(doc, "a Delaware limited liability company", space_after=20)
    para(doc, "By: ______________________________________", space_after=2)
    para(doc, "Name: Marcus Ellison", space_after=2)
    para(doc, "Title: Managing Member", space_after=2)
    para(doc, "Date: ____________________, 2025", space_after=14)
    para(doc, "Attest:", space_after=16)
    para(doc, "By: ______________________________________", space_after=2)
    para(doc, "Name: ___________________________________", space_after=2)
    para(doc, "Title: ___________________________________", space_after=6)
    pagebreak(doc)
    para(doc, "**[SIGNATURE PAGE FOR LEASEHOLD MORTGAGEE CONSENT AND AGREEMENT]**", space_after=10)
    para(doc, "The undersigned Leasehold Mortgagee executes this Ground Lease Agreement solely for the purpose of "
              "acknowledging and consenting to the provisions of Article 9 and Sections 10.5 through 10.8, and agrees "
              "to be bound by the obligations applicable to a Leasehold Mortgagee under Article 9.")
    para(doc, "", space_after=14)
    para(doc, "**BAYSIDE FEDERAL LENDING CORP.**", space_after=20)
    para(doc, "By: ______________________________________", space_after=2)
    para(doc, "Name: Sandra Milliken", space_after=2)
    para(doc, "Title: Senior Vice President, Commercial Real Estate Lending", space_after=2)
    para(doc, "Date: ____________________, 2025", space_after=20)
    pagebreak(doc)
    para(doc, "**[NOTARIAL ACKNOWLEDGMENTS]**", space_after=12)
    para(doc, "**STATE OF CONNECTICUT**", space_after=0)
    para(doc, "**COUNTY OF NEW HAVEN**", space_after=12)
    para(doc, "On this ______ day of ________________, 2025, before me, the undersigned officer, personally appeared "
              "**Paul Castignetti**, who acknowledged himself to be the Executive Director of the **CITY OF PORT "
              "CALLOWAY REDEVELOPMENT AUTHORITY**, a public body corporate and politic, and that he, as such officer, "
              "being authorized to do so, executed the foregoing instrument for the purposes therein contained, by "
              "signing the name of the Authority by himself as such officer.", space_after=20)
    para(doc, "______________________________________", space_after=2)
    para(doc, "Notary Public", space_after=2)
    para(doc, "My commission expires: ________________", space_after=24)
    para(doc, "**STATE OF CONNECTICUT**", space_after=0)
    para(doc, "**COUNTY OF NEW HAVEN**", space_after=12)
    para(doc, "On this ______ day of ________________, 2025, before me, the undersigned officer, personally appeared "
              "**Marcus Ellison**, who acknowledged himself to be the Managing Member of **MERIDIAN GATEWAY HOLDINGS "
              "LLC**, a Delaware limited liability company, and that he, as such officer, being authorized to do so, "
              "executed the foregoing instrument for the purposes therein contained, by signing the name of the "
              "limited liability company by himself as such officer.", space_after=20)
    para(doc, "______________________________________", space_after=2)
    para(doc, "Notary Public", space_after=2)
    para(doc, "My commission expires: ________________", space_after=6)
