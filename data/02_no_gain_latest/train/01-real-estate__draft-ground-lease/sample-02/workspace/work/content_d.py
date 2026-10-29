from helpers import *

def blocks(doc):
    art(doc, "Article 8. Security Deposit and Letter of Credit")
    sec(doc, "8.1", "Security Deposit", "On or before the Lease Commencement Date, Tenant shall deliver to Landlord a "
        "security deposit in the amount of **Five Million Seven Hundred Thousand Dollars ($5,700,000)**, equal to "
        "twenty-four (24) monthly installments of the initial Base Rent ($237,500 × 24), as security for the "
        "performance of Tenant's obligations under this Lease. The Security Deposit is not an advance payment of Rent, "
        "is not a measure or liquidation of Landlord's damages, and shall not be commingled with Landlord's other "
        "funds.")
    sec(doc, "8.2", "Form", "The Security Deposit shall be provided, at Tenant's election, in the form of (a) an "
        "irrevocable standby letter of credit substantially in the form attached as **Exhibit E**, naming Landlord as "
        "beneficiary, drawable in Connecticut or by facsimile or electronic presentation, and permitting partial draws "
        "and multiple draws and reinstatements (the \"**Letter of Credit**\"); or (b) cash deposited with an escrow "
        "agent reasonably acceptable to Landlord and each Leasehold Mortgagee. Tenant's election under this Section "
        "8.2 shall be made no later than thirty (30) days prior to the Lease Commencement Date.")
    sec(doc, "8.3", "Issuer Requirements", "Any Letter of Credit shall be issued by a commercial bank organized under "
        "the laws of the United States or any state thereof that (a) has a long-term issuer credit rating of not less "
        "than A- from Standard & Poor's Ratings Services or A3 from Moody's Investors Service, Inc. (or an equivalent "
        "rating from a nationally recognized rating agency), or (b) is a federally chartered banking institution with "
        "capital and surplus of not less than $[●]. If the rating of the issuing bank falls below the required level, "
        "Tenant shall deliver a replacement Letter of Credit from a qualifying issuer within sixty (60) days after "
        "written notice from Landlord, and such failure shall not constitute an Event of Default until the expiration "
        "of such sixty (60) day period.")
    sec(doc, "8.4", "Reduction of the Security Deposit", "The Security Deposit shall be reduced to **Two Million Eight "
        "Hundred Fifty Thousand Dollars ($2,850,000)** upon Tenant's demonstration, to Landlord's reasonable "
        "satisfaction, that the Project has achieved and maintained an Occupancy Rate of ninety percent (90%) or "
        "greater for twenty-four (24) consecutive full calendar months (the \"**Reduction Threshold**\"). The "
        "following procedures and definitions shall govern:")
    sub(doc, "(a)", "**Occupancy Rate** means, as of any date, the quotient (expressed as a percentage) obtained by "
        "dividing (i) the aggregate rentable square footage of all residential, office and retail space in the Project "
        "that is subject to a bona fide lease or occupancy agreement under which rent is being paid or a free-rent "
        "period is in effect, by (ii) the aggregate rentable square footage of all residential, office and retail "
        "space in the completed portions of the Project, in each case measured on a consistent basis. Residential "
        "square footage shall be the net rentable area of the dwelling units, exclusive of common areas and corridors. "
        "A Project that is not fully constructed shall be tested only with respect to completed buildings for which a "
        "Certificate of Occupancy has been issued.")
    sub(doc, "(b)", "**Demonstration.** Tenant shall deliver to Landlord (i) a certified rent roll as of the last day "
        "of the twentieth-fourth consecutive month, (ii) a certificate of an authorized financial officer of Tenant "
        "certifying the Occupancy Rate calculation, and (iii) such supporting documentation as Landlord may reasonably "
        "request. Landlord shall respond within thirty (30) days after receipt; failure to object in writing within "
        "such period shall constitute approval.")
    sub(doc, "(c)", "**Implementation.** Within ten (10) Business Days after Tenant's satisfaction of the Reduction "
        "Threshold, Landlord shall execute and deliver such instruments (including an amendment to the Letter of "
        "Credit) as are necessary to effect the reduction, and shall return any excess cash Security Deposit. Tenant "
        "may deliver a replacement Letter of Credit in the reduced amount in lieu of an amendment.")
    sub(doc, "(d)", "**No reinstatement.** The reduced Security Deposit shall not be increased by reason of any "
        "subsequent decline in occupancy, and the reduced amount shall remain the Security Deposit for the balance of "
        "the Term, subject only to Section 8.6 (replenishment following a draw).")
    sec(doc, "8.5", "Draws", "Landlord may draw upon the Letter of Credit (or apply the cash Security Deposit) only "
        "(a) after the occurrence of an Event of Default that remains uncured after the expiration of all applicable "
        "notice and cure periods (including the Lender Cure Periods under Section 9.5), and (b) only to the extent of "
        "amounts then due and payable and unpaid, or Documented Damages finally determined as provided in Section 10.7. "
        "Landlord may not draw on account of any amount that Tenant disputes in good faith while the dispute is "
        "pending under Section 20.2, and may not draw the entire Security Deposit as a consequence of any single "
        "Event of Default except to the extent of amounts finally determined. Landlord shall give simultaneous written "
        "notice of any draw to each Leasehold Mortgagee. Any amount drawn shall be applied to Tenant's obligations "
        "under this Lease and not to any other purpose.")
    sec(doc, "8.6", "Replenishment", "If Landlord lawfully draws upon the Security Deposit, Tenant shall, within thirty "
        "(30) days after written demand (accompanied by a written statement of the amount drawn and its application), "
        "restore the Security Deposit to the required amount. Tenant's failure to do so within such period, if "
        "continuing for ten (10) Business Days after a second written notice, shall constitute an Event of Default.")
    sec(doc, "8.7", "Transfer; Return", "Landlord may transfer the Security Deposit to any successor owner of "
        "Landlord's interest in the Premises, and upon such transfer and written notice to Tenant and each Leasehold "
        "Mortgagee, Landlord shall be released from further liability with respect thereto. Within thirty (30) days "
        "after the later of the Expiration Date (or earlier Termination Date) and the satisfaction of all of Tenant's "
        "obligations, Landlord shall return the Security Deposit to Tenant, together with any interest accrued on a "
        "cash deposit.")
    sec(doc, "8.8", "Renewal; Expiration", "If the Letter of Credit has a stated expiration date, Tenant shall deliver "
        "a renewal or replacement not later than thirty (30) days prior to its expiration, or shall cause the Letter "
        "of Credit to be an evergreen letter of credit that automatically renews for successive one-year periods "
        "unless the issuer gives not less than sixty (60) days' prior written notice of non-renewal. Failure to "
        "deliver a renewal or replacement shall constitute an Event of Default only if such failure continues for ten "
        "(10) Business Days after written notice from Landlord and any Leasehold Mortgagee.")
    sec(doc, "8.9", "No Landlord Lien; No Waiver", "Tenant's delivery of the Security Deposit shall not create any "
        "lien or security interest in favor of Landlord in any property of Tenant other than the Security Deposit, and "
        "Landlord hereby waives any statutory or contractual landlord's lien, distraint or right of levy against "
        "Tenant's personal property or the Improvements.")

    # ================= ARTICLE 9 =================
    art(doc, "Article 9. Leasehold Financing; Lender Protections; SNDA; New Lease")
    para(doc, "The provisions of this Article 9 are material inducements to Tenant's execution of this Lease and to "
              "the closing of the construction financing for the Project. The parties acknowledge that the "
              "requirements of this Article 9 equal or exceed the ground lease requirements of the Construction Lender "
              "and are intended to satisfy the requirements of any institutional lender that may hold a Leasehold "
              "Mortgage at any time during the Term. Each Leasehold Mortgagee is an express third-party beneficiary of "
              "this Article 9 and of Sections 10.5, 10.6 and 10.7, and may enforce those provisions directly.")
    sec(doc, "9.1", "Right to Encumber", "Tenant may, at any time and from time to time, without the consent, "
        "approval or joinder of Landlord and without the payment of any consent fee, administrative charge or other "
        "compensation to Landlord: (a) grant one or more Leasehold Mortgages encumbering all or any portion of "
        "Tenant's leasehold interest in the Premises and the Improvements; (b) collaterally assign this Lease, all "
        "subleases, leases, rents, revenues, permits, contracts and plans; (c) pledge the direct and indirect "
        "ownership interests in Tenant; and (d) grant such other security as any lender may require. No consent, "
        "approval or other condition of Landlord shall be required for the granting, recording, enforcement, "
        "refinancing or foreclosure of any Leasehold Mortgage. Each Leasehold Mortgage shall be permitted to encumber "
        "the entire leasehold estate created by this Lease, together with all Improvements, fixtures and "
        "appurtenances now or hereafter located on the Premises.")
    sec(doc, "9.2", "Designation of Leasehold Mortgagees", "Tenant may designate one or more Leasehold Mortgagees "
        "under this Lease. Each Leasehold Mortgagee shall deliver to Landlord a written notice specifying its name, "
        "address for notices, the amount of its loan and the collateral securing it, and may update such information "
        "from time to time. Landlord shall recognize each Leasehold Mortgagee so designated. There is no limit on the "
        "number of Leasehold Mortgagees, nor on the number of refinancings, restructurings or recapitalizations of "
        "the leasehold financing during the Term.")
    sec(doc, "9.3", "Notices to Leasehold Mortgagees", "Landlord shall deliver to each Leasehold Mortgagee, "
        "simultaneously with delivery to Tenant (and in any event no later than the delivery to Tenant), a copy of "
        "every notice of default, notice of termination, notice of Milestone Default, notice of intended termination "
        "or non-renewal, notice of casualty or condemnation, notice of any proceeding affecting the Premises, and every "
        "other notice, consent, approval, statement, estoppel or instrument delivered to Tenant under this Lease. "
        "Notices to each Leasehold Mortgagee shall be delivered to the address designated under Section 9.2 and to "
        "its counsel as designated. Any notice of default or termination not delivered to each Leasehold Mortgagee in "
        "accordance with this Section 9.3 shall be void and of no effect.")
    sec(doc, "9.4", "No Surrender, Amendment or Termination Without Mortgagee Consent", "For so long as any Leasehold "
        "Mortgage remains in effect, Landlord shall not accept a voluntary surrender or cancellation of this Lease, and "
        "Landlord and Tenant shall not amend, modify, supplement or terminate this Lease in any material respect, "
        "without the prior written consent of each Leasehold Mortgagee. Any purported surrender, amendment, "
        "modification, supplement or termination effected without such consent shall be void and of no force or effect "
        "as against each Leasehold Mortgagee, and this Lease shall continue in full force and effect as if such "
        "purported surrender, amendment, modification, supplement or termination had not occurred.")
    sec(doc, "9.5", "Lender Cure Periods", "No termination of this Lease and no exercise of any remedy by Landlord "
        "that would extinguish or impair any Leasehold Mortgage shall be effective unless and until Landlord has "
        "delivered the required notices to each Leasehold Mortgagee and the following cure periods (each, a "
        "\"**Lender Cure Period**\") have expired without cure:")
    sub(doc, "(a)", "**Monetary Defaults.** Sixty (60) days from the date of the Leasehold Mortgagee's receipt of "
        "notice of the monetary default to cure the default on behalf of Tenant.")
    sub(doc, "(b)", "**Non-Monetary Defaults.** Ninety (90) days from the date of the Leasehold Mortgagee's receipt of "
        "notice of the non-monetary default to cure the default, or, if such cure cannot reasonably be completed "
        "within ninety (90) days, to commence cure within such ninety (90) day period and thereafter diligently and "
        "continuously prosecute such cure to completion.")
    sub(doc, "(c)", "**Milestone Defaults.** One hundred eighty (180) days commencing upon the expiration of the "
        "Milestone Cure Period, during which the Leasehold Mortgagee may cure the Milestone Default, including by "
        "(i) causing the applicable Milestone to be achieved, (ii) advancing funds to Tenant or to a replacement "
        "developer to achieve the Milestone, (iii) installing a replacement developer, general contractor or property "
        "manager reasonably acceptable under Section 9.7, or (iv) causing Tenant's interest under this Lease to be "
        "transferred to the Leasehold Mortgagee or its designee in accordance with Section 9.7.")
    para(doc, "Each Lender Cure Period shall run in addition to, and not concurrently with, any cure period afforded to "
              "Tenant, and Landlord shall accept performance by a Leasehold Mortgagee with the same effect as "
              "performance by Tenant. A Leasehold Mortgagee may cure any default without curing all defaults and "
              "without being deemed to have assumed any of Tenant's obligations. Landlord shall give each Leasehold "
              "Mortgagee written notice of the commencement and expiration of each Lender Cure Period.")
    sec(doc, "9.6", "New Lease", "If this Lease is terminated for any reason whatsoever, including without limitation "
        "a Milestone Default, any other Event of Default by Tenant, surrender, rejection in bankruptcy, or operation of "
        "law (each, a \"**Termination Event**\"), then each Leasehold Mortgagee (or its designee) shall have the "
        "right, upon written request delivered to Landlord within sixty (60) days after such Leasehold Mortgagee's "
        "receipt of notice of the Termination Event, to enter into a new ground lease of the Premises with Landlord "
        "(a \"**New Lease**\") on the following terms:")
    sub(doc, "(a)", "**Term.** The New Lease shall be for the remainder of the Term of this Lease (as if this Lease had "
        "not been terminated), without reduction, together with any extension right then available under Section 2.7.")
    sub(doc, "(b)", "**Terms.** The New Lease shall be on the same terms and conditions as this Lease, modified only "
        "to the extent necessary to (i) reflect the identity of the new tenant, (ii) delete provisions that are "
        "inapplicable because the applicable default has been cured, (iii) state that the New Lease is effective as "
        "of the Termination Date, (iv) provide that the Leasehold Mortgagee (or its designee) assumes Tenant's "
        "obligations prospectively from the effective date of the New Lease and is not liable for any obligation, "
        "liability or default of Tenant arising before such date (other than the cure obligations described below), "
        "and (v) eliminate any improvement-forfeiture, reverter or security deposit forfeiture provisions.")
    sub(doc, "(c)", "**Cure.** The Leasehold Mortgagee (or its designee) shall cure all monetary defaults existing "
        "under this Lease within sixty (60) days after the effective date of the New Lease, and all non-monetary "
        "defaults reasonably susceptible of cure within ninety (90) days after the effective date of the New Lease, "
        "or, if any such non-monetary default cannot reasonably be cured within such period, shall commence cure "
        "within ninety (90) days and thereafter diligently and continuously pursue cure to completion, but in no "
        "event later than one hundred eighty (180) days after the effective date of the New Lease.")
    sub(doc, "(d)", "**Execution.** Landlord shall execute, acknowledge, deliver and record the New Lease within thirty "
        "(30) days after the Leasehold Mortgagee's written request, and the New Lease shall be effective as of the "
        "Termination Date. Landlord shall not require any consent, fee, payment, guaranty, credit support or other "
        "condition in connection with the New Lease, other than the cure obligations in Section 9.6(c).")
    sub(doc, "(e)", "**Priority and Subleases.** The New Lease shall have a priority in all respects equal to the "
        "priority of this Lease, and all subleases, licenses and occupancy agreements entered into by Tenant or any "
        "subtenant before the Termination Event shall be recognized by Landlord under the New Lease, and Landlord "
        "shall take the Premises subject thereto.")
    sub(doc, "(f)", "**No ROFR.** Neither Landlord's right of first refusal under Section 11.5 nor any consent, notice "
        "or other requirement of Article 11 shall apply to the New Lease or to any assignment by a Leasehold "
        "Mortgagee in connection with the exercise of its rights under this Article 9.")
    sub(doc, "(g)", "**Pre-Authorization; Enforceability.** Landlord covenants that it shall include in the resolution "
        "approving this Lease an express authorization of its obligation to execute and deliver a New Lease in "
        "accordance with this Section 9.6 and of its obligation to pay the Improvement Payment under Section 10.6, and "
        "that no further action of its Board of Commissioners shall be required to permit or give effect to either "
        "obligation. Landlord acknowledges that each Leasehold Mortgagee is relying on this Section 9.6 in making its "
        "loan, and that the Leasehold Mortgagee shall be entitled to specific performance of this Section 9.6 and to "
        "damages for its breach.")
    sub(doc, "(h)", "**Effect on Seniority of Landlord's Fee.** Nothing in this Section 9.6 shall subordinate "
        "Landlord's fee interest in the land, but Landlord's fee interest shall in all events remain subject to the "
        "New Lease.")
    sec(doc, "9.7", "Foreclosure and Assignment", "Each Leasehold Mortgagee shall have the unconditional right to "
        "foreclose on the leasehold interest (whether by judicial foreclosure, power of sale, strict foreclosure, or "
        "otherwise) or to accept a deed or assignment in lieu of foreclosure, and to assign this Lease to a qualified "
        "transferee at or following any foreclosure sale or deed-in-lieu transfer, without the prior consent of "
        "Landlord and without triggering the ROFR under Section 11.5 or any other right of Landlord. A transferee "
        "shall be deemed qualified if it (a) is a Person with not less than [**Tenant position:** $[●] of net worth] or "
        "assets under management, (b) has demonstrable experience in owning and operating comparable mixed-use "
        "properties or waterfront development, or (c) is a Leasehold Mortgagee or an affiliate or designee thereof or "
        "any institutional investor, pension fund, real estate investment trust, insurance company, bank or "
        "opportunity fund or an affiliate of any of them. Landlord shall not unreasonably withhold, condition or delay "
        "recognition of any such transferee as Tenant, shall execute and deliver any estoppel, recognition "
        "agreement, SNDA or other document reasonably requested by a Leasehold Mortgagee within ten (10) Business "
        "Days, and shall not charge any fee in connection therewith.")
    sec(doc, "9.8", "Bankruptcy Protections", "If Tenant becomes a debtor in any proceeding under Title 11 of the "
        "United States Code or any similar state insolvency law:")
    sub(doc, "(a)", "this Lease shall not terminate, and Landlord shall have no right to terminate this Lease or to "
        "exercise any remedy, solely by reason of the commencement of such proceeding (and any provision of this Lease "
        "purporting to terminate this Lease upon such a filing shall be void to the extent unenforceable under 11 "
        "U.S.C. § 365(e));")
    sub(doc, "(b)", "each Leasehold Mortgagee shall have the right to request that any trustee, debtor-in-possession "
        "or other party in interest assume or reject this Lease in a timely manner consistent with 11 U.S.C. § 365, "
        "and to cure any defaults and provide adequate assurance of future performance on behalf of Tenant to the "
        "extent necessary to prevent rejection;")
    sub(doc, "(c)", "Tenant and any trustee shall not reject this Lease without the prior written consent of each "
        "Leasehold Mortgagee, and Landlord shall not oppose any election by any Leasehold Mortgagee under 11 U.S.C. "
        "§ 365(h) or the counterpart provisions applicable to the leasehold mortgagee; and")
    sub(doc, "(d)", "the New Lease right under Section 9.6 shall survive any rejection of this Lease in bankruptcy to "
        "the fullest extent permitted by Applicable Law, and Landlord shall recognize each Leasehold Mortgagee's "
        "right to obtain a New Lease notwithstanding such rejection. The parties acknowledge that the New Lease right "
        "is intended to be a property interest of each Leasehold Mortgagee enforceable notwithstanding 11 U.S.C. "
        "§ 365(h) and § 365(i).")
    sec(doc, "9.9", "SNDA", "Landlord shall, simultaneously with or prior to the first advance of any loan secured by a "
        "Leasehold Mortgage, and at any later time upon the request of any Leasehold Mortgagee, execute, acknowledge, "
        "deliver and record an SNDA containing not less than the terms set forth on **Exhibit F**, including (a) "
        "Landlord's acknowledgment of the existence and priority of the Leasehold Mortgage; (b) Landlord's agreement "
        "not to disturb the Leasehold Mortgagee's security interest or the rights of any purchaser at foreclosure or "
        "transferee by deed in lieu of foreclosure; (c) Landlord's agreement to recognize the Leasehold Mortgagee or "
        "its designee or purchaser as Tenant under this Lease or the New Lease; and (d) provisions relating to "
        "casualty, condemnation, insurance and condemnation proceeds. Landlord shall have no obligation to subordinate "
        "its fee interest in the land, and nothing in any SNDA shall be construed to do so. Landlord's failure to "
        "deliver an SNDA within ten (10) Business Days after request shall constitute a Landlord Event of Default "
        "curable only by delivery, and Tenant may obtain specific performance.")
    sec(doc, "9.10", "Refinancing and Recapitalization Cooperation", "Landlord shall, without charge, within ten (10) "
        "Business Days after request, execute, acknowledge and deliver such estoppel certificates, consents, "
        "recognition agreements, SNDAs, subordination and non-disturbance agreements, financing statements, "
        "memoranda, and other instruments as Tenant or any Leasehold Mortgagee or prospective lender may reasonably "
        "request in connection with any financing, refinancing, securitization, syndication or recapitalization during "
        "the Term, in each case in form reasonably satisfactory to Landlord and consistent with this Lease. Landlord's "
        "obligations under this Section 9.10 shall not be limited in number of transactions.")
    sec(doc, "9.11", "Landlord's Fee Interest", "Landlord shall not mortgage, pledge, encumber, sell or otherwise "
        "transfer its fee interest in the land during the Term without (a) delivering to Tenant and each Leasehold "
        "Mortgagee a subordination, non-disturbance and attornment agreement from the transferee or lender, in form "
        "reasonably satisfactory to Tenant and each Leasehold Mortgagee, providing that this Lease and the New Lease "
        "right shall not be disturbed, and (b) giving Tenant not less than thirty (30) days' prior written notice. Any "
        "transfer of Landlord's fee interest shall be subject to this Lease in all respects.")

    # ================= ARTICLE 10 =================
    art(doc, "Article 10. Defaults, Remedies and Milestone Termination")
    sec(doc, "10.1", "Tenant Events of Default", "Each of the following shall constitute an Event of Default by "
        "Tenant, subject in each case to the notice and cure provisions of Article 9 and this Article 10:")
    t_ev = [
        "(a) Tenant's failure to pay any installment of Base Rent or Percentage Rent within ten (10) Business Days "
        "after written notice from Landlord that such amount is past due;",
        "(b) Tenant's failure to pay any other monetary obligation (other than Base Rent or Percentage Rent) within "
        "fifteen (15) days after written notice from Landlord;",
        "(c) Tenant's failure to perform or observe any material non-monetary obligation under this Lease within "
        "thirty (30) days after written notice specifying the failure, or, if the failure cannot reasonably be cured "
        "within thirty (30) days, Tenant's failure to commence cure within such period and thereafter diligently "
        "prosecute it to completion;",
        "(d) a Milestone Default, subject to Sections 10.5 and 10.6;",
        "(e) Tenant's failure to maintain the Security Deposit in accordance with Article 8;",
        "(f) Tenant's failure to maintain the insurance required by Article 12, which failure continues for ten (10) "
        "days after written notice;",
        "(g) an assignment, sublease or transfer in violation of Article 11;",
        "(h) the filing of a voluntary petition in bankruptcy by Tenant, the entry of an order for relief against "
        "Tenant in an involuntary proceeding that is not dismissed within sixty (60) days, or Tenant's making a "
        "general assignment for the benefit of creditors, in each case subject to and limited by Section 9.8; and",
        "(i) any material misrepresentation by Tenant in this Lease or in any certificate delivered under it, which "
        "misrepresentation remains uncured (to the extent curable) for thirty (30) days after written notice.",
    ]
    for t in t_ev: sub(doc, t.split(")")[0] + ")", t.split(")", 1)[1].strip())
    para(doc, "No Event of Default shall exist under Sections 10.1(a), (b) or (c) unless and until Landlord has given "
              "the applicable written notice and the applicable cure period has expired. Landlord shall deliver a "
              "copy of every such notice simultaneously to each Leasehold Mortgagee. Landlord may not declare an Event "
              "of Default under Section 10.1(a) or (b) more than twice in any period of twelve (12) consecutive months "
              "without giving a cure period of thirty (30) days.")
    sec(doc, "10.2", "Landlord Events of Default", "Each of the following shall constitute an Event of Default by "
        "Landlord if not cured within the applicable period after written notice from Tenant (with a copy to each "
        "Leasehold Mortgagee):")
    l_ev = [
        "(a) Landlord's failure to pay any amount due to Tenant under this Lease within ten (10) Business Days after "
        "written notice;",
        "(b) Landlord's failure to perform or observe any material obligation under this Lease within thirty (30) days "
        "after written notice, or, if the failure cannot reasonably be cured within thirty (30) days, Landlord's "
        "failure to commence cure within such period and thereafter diligently prosecute it to completion;",
        "(c) Landlord's failure to deliver any SNDA, estoppel certificate, consent, approval, New Lease or other "
        "instrument within the period specified in this Lease (or, if no period is specified, within ten (10) Business "
        "Days after written request), which failure shall be curable only by delivery;",
        "(d) Landlord's failure to cause the Tax Abatement Agreement to be executed and delivered in accordance with "
        "Section 6.8, or any breach of Section 6.8;",
        "(e) Landlord's failure to discharge the mechanics' lien described in Section 2.9(a);",
        "(f) any breach of Landlord's representations, warranties or covenants in Article 18 or Section 2.8 that is "
        "not cured within thirty (30) days after written notice; and",
        "(g) Landlord's breach of Article 9.",
    ]
    for t in l_ev: sub(doc, t.split(")")[0] + ")", t.split(")", 1)[1].strip())
    sec(doc, "10.3", "Landlord's Remedies", "Upon the occurrence and during the continuance of an Event of Default by "
        "Tenant, Landlord may, subject in all respects to Article 9 and Section 10.5:")
    sub(doc, "(a)", "terminate this Lease by written notice, but only after the expiration of all applicable notice and "
        "cure periods, including the Milestone Cure Period and each Lender Cure Period;")
    sub(doc, "(b)", "draw upon the Security Deposit only to the extent permitted by Section 8.5;")
    sub(doc, "(c)", "recover from Tenant, as damages (and not as a penalty), an amount equal to the Documented Damages "
        "determined under Section 10.7;")
    sub(doc, "(d)", "if the Event of Default is a Milestone Default, exercise the remedy set forth in Sections 10.5 and "
        "10.6, which shall be Landlord's sole and exclusive remedy for a Milestone Default; and")
    sub(doc, "(e)", "pursue specific performance of Tenant's obligations (other than an obligation to expend money) "
        "and any other remedy available at law or in equity consistent with this Lease.")
    para(doc, "Landlord shall have **no** right to declare the entire balance of future Rent immediately due and "
              "payable, and no right to forfeit the Improvements except as set forth in Sections 10.5 and 10.6. "
              "Landlord's remedies are cumulative except that, as to a Milestone Default, Sections 10.5 and 10.6 are "
              "the sole and exclusive remedy of Landlord.")
    sec(doc, "10.4", "Tenant's Remedies", "Upon the occurrence and during the continuance of an Event of Default by "
        "Landlord, Tenant may: (a) cure the default on Landlord's behalf and set off the reasonable cost thereof, "
        "together with interest at the Default Interest Rate, against Rent as provided in Section 4.6; (b) seek "
        "specific performance of Landlord's obligations, including the obligation to execute a New Lease, an SNDA or "
        "an estoppel, and the parties agree that the remedy of specific performance shall be available notwithstanding "
        "that damages may be an adequate remedy; (c) recover actual direct damages; (d) suspend performance of "
        "Tenant's obligations under this Lease to the extent caused by Landlord's default; and (e) terminate this "
        "Lease upon sixty (60) days' written notice if a Landlord Event of Default remains uncured and renders the "
        "Premises unusable for the Permitted Uses, in which case Tenant shall be entitled to the Improvement Payment "
        "determined under Section 10.6 as if the Termination Date were a termination under Section 10.5.")
    sec(doc, "10.5", "Milestone Default; Termination Procedure",
        "The following procedure shall apply to any Milestone Default, and shall supersede and control over any "
        "provision of this Lease or the Term Sheet that would cause this Lease to terminate automatically:")
    sub(doc, "(a)", "**Milestone Notice.** Landlord may deliver to Tenant (and simultaneously to each Leasehold "
        "Mortgagee) a written notice specifying the Milestone Default, the Milestone and Milestone Deadline "
        "asserted, the factual basis for the assertion, and Landlord's calculation of any extensions under Section "
        "3.4. A notice that does not satisfy these requirements shall be ineffective.")
    sub(doc, "(b)", "**Tenant Cure.** Tenant shall have one hundred eighty (180) calendar days following its receipt "
        "of a valid Milestone Notice to cure the Milestone Default by achieving the applicable Milestone (the "
        "\"**Milestone Cure Period**\").")
    sub(doc, "(c)", "**Extension of Cure Period.** The Milestone Cure Period shall be extended by any period during "
        "which Tenant is prevented from achieving the applicable Milestone by a Force Majeure Event, a permitting "
        "delay, Landlord Delay or the exercise by a Leasehold Mortgagee of its rights under Section 9.5.")
    sub(doc, "(d)", "**Lender Cure Period.** Following the expiration of the Milestone Cure Period, each Leasehold "
        "Mortgagee shall have the Lender Cure Period described in Section 9.5(c).")
    sub(doc, "(e)", "**Election.** If the Milestone Default remains uncured upon the expiration of all of the "
        "foregoing periods, Landlord may elect to terminate this Lease only by written notice delivered to Tenant and "
        "each Leasehold Mortgagee within thirty (30) days after the expiration of the last such period. If Landlord "
        "does not so elect within such thirty (30) day period, Landlord shall be deemed to have waived that Milestone "
        "Default, and Landlord may not thereafter terminate this Lease or exercise any other remedy on account of it.")
    sub(doc, "(f)", "**No Automatic Termination.** This Lease shall **not** terminate automatically upon the "
        "occurrence of a Milestone Default or the expiration of any cure period. Termination shall occur only upon "
        "Landlord's valid election under Section 10.5(e), and shall be effective as of the date specified in "
        "Landlord's notice, which shall be not earlier than the date of the notice.")
    sub(doc, "(g)", "**Conditions to Termination.** Notwithstanding any election by Landlord, no termination of this "
        "Lease on account of a Milestone Default shall be effective unless and until each of the following has been "
        "satisfied: (i) all notices required by Sections 9.3 and 10.5 have been delivered to each Leasehold "
        "Mortgagee; (ii) each Lender Cure Period has expired without cure; (iii) the period for a Leasehold Mortgagee "
        "to request a New Lease under Section 9.6 has expired without a request, or each Leasehold Mortgagee has "
        "waived its New Lease right in writing; (iv) the Improvement Payment has been paid in full or is secured in "
        "the manner provided in Section 10.6(c) or Section 10.6(d); and (v) Landlord is not then in default of any of its obligations "
        "under this Lease.")
    sub(doc, "(h)", "**No Termination After Substantial Completion.** Landlord shall have no right to terminate this "
        "Lease on account of a failure to achieve Milestone 3 if Substantial Completion of Phase 1 has been achieved "
        "before the effective date of any such termination, notwithstanding the existence of punch-list items or "
        "incomplete tenant fit-out, and any such termination shall be void.")
    sub(doc, "(i)", "**Wrongful Termination.** If Landlord purports to terminate this Lease on account of a Milestone "
        "Default other than in strict compliance with this Section 10.5, such termination shall be void, Tenant may "
        "obtain specific performance and injunctive relief, and Landlord shall indemnify Tenant and each Leasehold "
        "Mortgagee for all resulting losses, including financing costs, carry costs and lost profits.")
    sec(doc, "10.6", "Improvement Payment upon Termination for Milestone Default", "If this Lease is terminated on "
        "account of a Milestone Default in accordance with Section 10.5, then, as a condition to the effectiveness of "
        "such termination and in consideration of the transfer to Landlord of Tenant's Improvements and leasehold "
        "estate:")
    sub(doc, "(a)", "**Payment Obligation.** Landlord shall pay to Tenant (or, at Tenant's direction, to each "
        "Leasehold Mortgagee in accordance with its interest) an amount (the \"**Improvement Payment**\") equal to "
        "**the greater of** (i) the Appraised Value of the Improvements as of the Termination Date, determined in "
        "accordance with Section 10.8, and (ii) Tenant's Unreimbursed Hard Costs; less (iii) all insurance proceeds, "
        "condemnation awards and other recoveries theretofore received by or for the account of Tenant in respect of "
        "the Improvements and not applied to restoration; and less (iv) Landlord's Documented Damages determined in "
        "accordance with Section 10.7.")
    sub(doc, "(b)", "**Expression of Intent.** The parties agree that the Improvement Payment is intended to insure "
        "that Landlord does not acquire the Improvements, and the substantial value represented by them, without "
        "compensation, and that the Improvement Payment does not exceed a reasonable forecast of Landlord's "
        "compensable interest and is not a penalty. The parties further agree that Landlord's actual damages arising "
        "from a Milestone Default are limited to delay in the receipt of Rent and the other items described in "
        "Section 10.7, and that the uncompensated retention of Improvements having a value of $200,000,000 or more "
        "would bear no reasonable relationship to those damages.")
    sub(doc, "(c)", "**Security and Possession.** Landlord shall pay the Improvement Payment within sixty (60) days "
        "after the Termination Date. At Tenant's election, Landlord's obligation shall be secured by a first-priority "
        "lien and security interest on the Improvements and on Landlord's right to receive Rent under any replacement "
        "lease, evidenced by a deed of trust, mortgage or security agreement in form reasonably satisfactory to "
        "Tenant. Landlord shall not be entitled to take possession of the Improvements, to lease them to a third "
        "party, or to record any instrument asserting title to them, until the Improvement Payment has been paid in "
        "full or secured in accordance with this Section 10.6(c).")
    sub(doc, "(d)", "**Escrow Alternative.** At Tenant's election, Landlord shall deposit the Improvement Payment in "
        "escrow with a nationally recognized title company or escrow agent pending determination of the Appraised "
        "Value, whereupon Landlord may take possession subject to the escrow.")
    sub(doc, "(e)", "**New Lease Prevails.** If a Leasehold Mortgagee exercises its New Lease right under Section "
        "9.6, no Improvement Payment shall be due, and this Lease shall be deemed to have been continued in the form "
        "of the New Lease.")
    sub(doc, "(f)", "**Successors; Subleases; Continuing Obligations.** Upon any such termination, Landlord shall take "
        "the Premises and the Improvements subject to (i) the ELUR and all Environmental Laws, (ii) the affordable "
        "housing covenant described in Section 14.5 and the recorded Declaration of Restrictive Covenants described "
        "on **Exhibit B**, (iii) all subleases, occupancy agreements and residential tenancies then in effect, which "
        "Landlord shall recognize and honor, (iv) all utility, access and operating easements reasonably necessary for "
        "the operation of the Improvements, and (v) the public's rights under the pedestrian access easement and the "
        "Public Open Space obligations. Landlord shall assume the obligations of the landlord under such subleases "
        "prospectively and shall indemnify Tenant against any liability arising from Landlord's ownership or operation "
        "of the Improvements after the Termination Date.")
    sub(doc, "(g)", "**Survival; Enforcement.** Landlord's obligation to pay the Improvement Payment shall survive "
        "the termination of this Lease, shall not be subject to any setoff, counterclaim or defense, and may be "
        "enforced by Tenant and by each Leasehold Mortgagee as an express third-party beneficiary.")
    sec(doc, "10.7", "Documented Damages", "Landlord's \"**Documented Damages**\" for any Event of Default shall be "
        "limited to Landlord's actual, reasonable, documented out-of-pocket losses and costs proximately caused by the "
        "Event of Default, which, in the case of a Milestone Default, shall be limited to: (a) all Rent accrued and "
        "unpaid through the Termination Date; (b) an amount equal to twenty-four (24) monthly installments of Base Rent "
        "at the rate in effect on the Termination Date, representing Landlord's reasonable estimate of the ground rent "
        "lost during the period reasonably required to re-let the Premises on comparable terms; (c) Landlord's "
        "reasonable, documented costs of re-letting (including brokers' commissions, legal fees and tenant "
        "improvements, but excluding the cost of curing any condition for which Landlord is responsible); and (d) "
        "Landlord's reasonable, documented out-of-pocket enforcement costs and attorneys' fees. Documented Damages "
        "shall **exclude** any amount attributable to (i) the value of the Improvements, (ii) anticipated Percentage "
        "Rent, (iii) lost real property tax revenue or other governmental revenue, (iv) loss of the public benefits "
        "described in the Recitals, (v) any speculative or hypothetical development value, (vi) consequential, "
        "punitive or exemplary damages, and (vii) any amount that would constitute a penalty. In no event shall "
        "Documented Damages exceed the sum of clauses (a) through (d) above.")
    sec(doc, "10.8", "Appraisal Procedure", "The Appraised Value of the Improvements shall be determined as follows:")
    sub(doc, "(a)", "Within thirty (30) days after the Termination Date, Tenant and Landlord shall each appoint an "
        "independent appraiser who is a member of the Appraisal Institute (MAI) with not less than ten (10) years' "
        "experience in valuing mixed-use and waterfront properties in Connecticut, and shall instruct each appraiser "
        "to determine the fair market value of the Improvements, disregarding the remaining Term and the reversion "
        "and assuming the Improvements are fully leased and operating in the ordinary course.")
    sub(doc, "(b)", "If the two appraisals differ by five percent (5%) or less of the higher, their average shall be "
        "the Appraised Value. Otherwise, the two appraisers shall appoint a third MAI appraiser meeting the same "
        "criteria, whose appraisal shall be the Appraised Value (and who shall not be limited to the range established "
        "by the first two appraisals).")
    sub(doc, "(c)", "If either party fails to appoint an appraiser within such period, the appraiser appointed by the "
        "other party shall determine the Appraised Value.")
    sub(doc, "(d)", "Each party shall bear the cost of its own appraiser, and the parties shall share equally the cost "
        "of the third appraiser. The determination shall be final and binding absent manifest error.")
    sec(doc, "10.9", "Security Deposit Not Forfeited", "In no event shall Landlord be entitled to retain the Security "
        "Deposit as a forfeiture or penalty. Any draw upon the Security Deposit shall be applied only to Documented "
        "Damages or other amounts finally determined to be due, and any excess shall be returned to Tenant within "
        "thirty (30) days after final determination.")
    sec(doc, "10.10", "Tenant's Right to Cure", "If Landlord fails to perform any obligation under this Lease, Tenant "
        "may, after the expiration of the applicable cure period, perform it on Landlord's behalf, and Landlord shall "
        "reimburse Tenant within thirty (30) days after written demand, with interest at the Default Interest Rate. "
        "Tenant shall not be liable for any loss or damage to the Premises resulting from its performance in a "
        "reasonable and workmanlike manner.")
    sec(doc, "10.11", "Remedies Cumulative; No Waiver", "Except as expressly provided in Section 10.3, the rights and "
        "remedies of the parties are cumulative and not exclusive. No failure or delay in exercising any right, and no "
        "acceptance of Rent with knowledge of a default, shall constitute a waiver of that default or of any other "
        "default. Landlord shall not be entitled to recover more than once for the same loss.")
