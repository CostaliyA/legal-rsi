# SOURCE-TO-ISSUE LOG (drafting notes)
## Documents in record
1. client-instructions-memo.eml — Ellison to Tsang, Sun 15 Jun 2025 09:47 (tenant instructions; deadline first draft ~29 Jun 2025)
2. term-sheet.docx — Executed binding term sheet, 10 Jun 2025 (20 sections + Exhibit A placeholder)
3. construction-loan-term-sheet.docx — Bayside Federal Lending Corp., 28 May 2025 (13 sections)
4. title-commitment.docx — Ridgepoint TC-2025-07821, eff. 1 Jun 2025 (Sched A, B-I 1-8, B-II 1-10, Sched C, Exh A)
5. phase-ii-esa-summary.docx — Halcyon HEC-2025-0412, 2 May 2025 exec summary
6. survey-description.docx — Calloway Land Surveyors CLS-2025-0417, field 20 Apr 2025 / plat 28 Apr 2025
7. board-resolution.docx — Resolution 2025-047, adopted 5 Jun 2025

## Arithmetic verified independently (calc3.py)
- 2,850,000/139,392 = $20.45/SF OK; /12 = 237,500 OK
- 2.5% compounding: exact $3,224,513.41 (TS says 3,224,500; -$13.41) and $3,648,240.95 (TS says 3,648,200; -$40.95)
- 24 x 237,500 = 5,700,000 OK; 12 x 237,500 = 2,850,000 OK
- Remediation credit: 7 x 237,500 = 1,662,500; +137,500 = 1,800,000 OK; month-8 payment 100,000 OK
- Area1 1,850,000 + Area2 550,000 = 2,400,000 OK; 2,400,000-1,800,000 = 600,000 OK
- Area1 components sum 1,750,000; stated "Contingency (10%) $100,000" = 5.71%, not 10% (true 10% = 175,000)  **ERROR**
- Area2 components sum 525,000; stated "Contingency (10%) $25,000" = 4.76%, not 10% (true 10% = 52,500)  **ERROR**
- Area1 volume 4,200x6/27 = 933 CY OK
- Taxes: 4,200,000x.03475=145,950 OK; 178,000,000x.03475=6,185,500 OK; 25/50/75% = 1,546,375 / 3,092,750 / 4,639,125 OK
- Capital stack 285+95+45=425 OK; 352+38.5+34.5=425 OK; LTC 67.06% (doc 67.1%) OK
- Milestone dates from 1 Oct 2025: 18mo=1 Apr 2027; 42mo=1 Apr 2029; 60mo=1 Oct 2030; 84mo=1 Oct 2032; 36mo=1 Oct 2028; expiry 30 Sep 2124 OK
- ROFR 20 yrs = through 30 Sep 2045 OK

## LEGAL DESCRIPTION — MAJOR ERROR FOUND
Survey traverse (CLS-2025-0417) closes exactly (0.000 ft), encloses 139,475 SF (3.202 ac) vs recited 139,392 (delta +83 SF, +0.06%).
Title Commitment Exhibit A traverse closes at 1.10 ft misclosure and encloses 279,535 SF = 6.417 acres
  => 2.01x the recited 139,392 SF. Bearings differ by exactly 6 deg (72-15-30 vs 78-15-30; 17-44-30 vs 11-44-30);
  distances 580.00/582.50/480.20 vs 435.22/435.22/320.47. Title's bulkhead calls sum to exactly 480.00 ft
  (= the "480 linear feet of bulkhead" figure repeated in TS, TC and Survey narrative), while the survey's
  eastern line is 320.47 ft. Title also cites a survey "CLS-2025-0321" by "J. Michael Ferreira, PLS 12847"
  revised 15 May 2025; delivered survey is "CLS-2025-0417" by Thomas R. Pellegrino, PLS-008741, 28 Apr 2025.

## Cross-document conflicts (see memo table)
- AMI geography: 3 different (TS "Port Calloway MSA" / TC "New Haven-Milford MSA" / Survey "Bridgeport-Stamford-Norwalk HUD FMR area")
- Condemnation: judicial district Port Calloway (TS) vs New Haven (TC); vol 367 p 44 (TC) vs vol 375 p 44 (Survey)
- Percentage rent start: TS "Lease Year 6" (Lease Yr 1 = Rent Commencement) vs Board Res. "Year 6 of the Ground Lease term"
- Tax abatement start: TS "commence on the Lease Commencement Date" vs client instruction to run during income years
- LOC issuer: A-/A3 rated bank (TS) vs "federally chartered banking institution" (Board Res.); cash alternative (Bayside SS4)
- Setoff: TS SS5 no setoff vs TS SS16 tenant offset right
- Reverter: TS SS9 "automatically terminate" vs Bayside SS5.4 "no termination effective unless ... lender cure periods expired"
- Bayside SS5.1-5.7 vs TS SS9 lender provisions: 5.1, 5.4, 5.5, 5.7 not met; 5.3 materially narrower; 5.2/5.6 partial
- Bayside dated 28 May 2025 references a ground lease term sheet "dated June 10, 2025" (later document)
- Coventry completion guaranty to Initial Maturity Date (48 mo = Oct 2029) vs Milestone 3 at 60 mo (Oct 2030)
- Loan max term 60 mo vs Milestone 4 at 84 mo (Phase 2 unfinanced)
- Mechanism lien: TS SS13 treats as Permitted Exception; TC Req. 7 says no policy until discharged
- ROFR recorded 2019 Declaration (Vol 405 Pg 55) has no mortgagee/foreclosure carve-out per TC Ex. 4
- ELUR ground-floor residential prohibition vs TS ground-floor lobby/amenity program
- Flood insurance: TS "not less than NFIP maximum" vs Bayside SS6(h) "amounts satisfactory to Lender"
- Freeboard: 3 ft (TS/TC/survey) vs Phase II recommendation 4-5 ft for 99-yr coastal term
