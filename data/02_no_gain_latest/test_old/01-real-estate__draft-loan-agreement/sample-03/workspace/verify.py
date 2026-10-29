def f(x): return f"${x:,.0f}"

out=[]
def chk(label, calc, stated, tol=1.0):
    ok = abs(calc-stated)<=tol
    out.append((label, calc, stated, "OK" if ok else "*** MISMATCH ***"))

# ---- Sources & uses
uses = dict(land=8_200_000, hard=34_750_000, soft=4_150_000, ir=4_850_000,
            orig=475_000, dev=2_835_000, cont=1_440_000)
tp = sum(uses.values())
chk("Total Project Costs", tp, 56_700_000)
chk("Sources (47.5+9.2+0)", 47_500_000+9_200_000+0, 56_700_000)
chk("Developer fee = 5% of TPC", tp*0.05, 2_835_000)
chk("Origination = 1% of loan", 47_500_000*0.01, 475_000)
chk("Hard contingency 1.14M as % GMP", 1_140_000/34_750_000*100, 3.28, 0.01)
chk("Total contingency as % GMP (memo says 4.1%)", 1_440_000/34_750_000*100, 4.14, 0.01)

# ---- LTC / LTV
ltc = 47_500_000/tp
print("LTC  %.4f%%  -> %.2f%%" % (ltc*100, ltc*100))
chk("Max loan at 80% LTC", tp*0.80, 45_360_000)
chk("LTC shortfall $", 47_500_000-tp*0.80, 2_140_000)
ltv_c = 47_500_000/72_800_000; ltv_s = 47_500_000/76_200_000
print("LTV as-completed %.4f%% ; as-stab %.4f%%" % (ltv_c*100, ltv_s*100))
print("Term sheet cap 65%% -> as-completed %s" % ("BREACH (65.25>65)" if ltv_c>0.65 else "ok"))

# ---- NOI
res, ret, oth = 5_712_000, 552_000, 198_000
gpi = res+ret+oth; chk("GPI", gpi, 6_462_000)
vac = gpi*0.05; chk("Vacancy 5%", vac, 323_100)
egi = gpi-vac; chk("EGI", egi, 6_138_900)
opex = 1_262_100; noi = egi-opex; chk("NOI", noi, 4_876_800)
chk("Opex ratio %", opex/egi*100, 20.56, 0.01)
chk("Residential 212 x 2,245 x 12", 212*2_245*12, 5_712_000, 1000)
chk("Retail 18,400 x 30", 18_400*30, 552_000)
chk("Cap rate", noi/76_200_000*100, 6.40, 0.01)
chk("76.2M x 6.4%", 76_200_000*0.064, 4_876_800, 10)
chk("As-completed = 76.2 - 3.4", 76_200_000-3_400_000, 72_800_000)
chk("Lease-up deductions 2.45+.68+.27", 2_450_000+680_000+270_000, 3_400_000)

# ---- DSCR
for rate,label in ((0.0785,"7.85%"),(0.0985,"9.85%"),(0.0795+0.0,"8.00%")):
    ds = 47_500_000*rate
    print("  rate %s annual interest %s DSCR %.4f" % (label, f(ds), noi/ds))
chk("Annual int @7.85%", 47_500_000*0.0785, 3_728_750)
chk("Annual int @9.85%", 47_500_000*0.0985, 4_678_750)

# ---- 14 units lost
loss = 14*2_245*12
chk("Revenue loss 14 units", loss, 377_160)
noi2 = noi-loss; print("  NOI w/o 14 units", f(noi2), "DSCR %.4f"%(noi2/3_728_750))
print("  implied value @6.4%% %s ; LTV %.2f%%" % (f(noi2/0.064), 47_500_000/(noi2/0.064)*100))

# ---- CC&R assessment omitted from opex
assess = 287_500*0.12
print("  CC&R assessment 0.12 x 287,500 GBA =", f(assess))
noi3 = noi-assess; print("  NOI less assessment", f(noi3), "DSCR %.4f"%(noi3/3_728_750), "value", f(noi3/0.064), "LTV %.2f%%"%(47_500_000/(noi3/0.064)*100))
noi4 = noi-loss-assess
print("  NOI less both", f(noi4), "DSCR %.4f"%(noi4/3_728_750), "value", f(noi4/0.064), "LTV %.2f%%"%(47_500_000/(noi4/0.064)*100))

# ---- Guarantors
print("Guarantors: VT", f(6_100_000+19_400_000+4_300_000), "Osei", f(3_200_000+6_800_000+1_500_000),
      "combined", f(29_800_000+11_500_000), "liq", f(6_100_000+3_200_000))
chk("Partial guaranty 25%", 47_500_000*0.25, 11_875_000)
print("  as %% of VT NW %.1f%% ; of Osei NW %.1f%%" % (11_875_000/29_800_000*100, 11_875_000/11_500_000*100))
print("  as multiple of VT liquidity %.2fx ; Osei liquidity %.2fx ; combined %.2fx" %
      (11_875_000/6_100_000, 11_875_000/3_200_000, 11_875_000/9_300_000))
chk("Liquidity coverage 9.3/5.0", 9_300_000/5_000_000, 1.86, 0.01)

# ---- Draw schedule as stated
draws = [9_475_000,5_212_500,6_950_000,6_950_000,5_212_500,3_475_000,3_475_000,3_475_000,3_275_000]
chk("Sum of 9 draws", sum(draws), 47_500_000)
chk("Draw 1 components", 4_150_000+4_850_000+475_000, 9_475_000)
chk("10% retainage of GMP", 0.10*34_750_000, 3_475_000)
print("  Draw 9 vs retainage: %s vs %s -> diff %s ; effective rate %.4f%%" %
      (f(3_275_000), f(3_475_000), f(3_275_000-3_475_000), 3_275_000/34_750_000*100))
gross_hard = sum(draws[1:])
chk("Sum hard-cost draws 2-9 vs GMP", gross_hard, 34_750_000)
hard_gross_col = [5_212_500,6_950_000,6_950_000,5_212_500,3_475_000,3_475_000,3_475_000,3_475_000]
chk("XLSX 'Hard Costs (gross)' column total", sum(hard_gross_col), 38_225_000)
print("  excess over GMP = %s (= retainage double-count)" % f(sum(hard_gross_col)-34_750_000))
dev_cont = [245_000+102_500, 245_000+102_500, 233_750+113_750, 200_000+600_000]
chk("XLSX dev fee+contingency columns total", sum(dev_cont), 3_275_000)
print("   required dev fee+contingency = %s ; shortfall %s" % (f(1_835_000+1_440_000), f(1_835_000+1_440_000-sum(dev_cont))))
chk("Check identity 9.475+34.75+3.275", 9_475_000+34_750_000+3_275_000, 47_500_000)

# ---- Interest reserve
tot_int_35 = 4_628_675
print("IR model @3.50%% SOFR (6.75%%) total int %s surplus %s" % (f(tot_int_35), f(4_850_000-tot_int_35)))
print("IR model @4.35%% (7.60%%) stated %s -> shortfall %s (ratio-scaled %.0f -> shortfall %.0f)" %
      (f(5_215_830), f(4_850_000-5_215_830), tot_int_35*7.60/6.75, 4_850_000-tot_int_35*7.60/6.75))
print("Credit memo avg-balance: 28.5M*7.60%%*2.5 = %s shortfall %s" % (f(28_500_000*0.076*2.5), f(4_850_000-28_500_000*0.076*2.5)))
print("Day-count: model uses /12; actual/360 on 365 days => uplift %.4f%% -> +%s on 4.6287M" %
      ((365/360-1)*100, f(4_628_675*(365/360-1))))

# independent monthly model, actual/360, 4.35% SOFR
bal=0.0; total=0.0
draw_at={1:9_475_000,4:5_212_500,9:6_950_000,14:6_950_000,18:5_212_500,21:3_475_000,25:3_475_000,30:3_475_000}
rate=0.0435+0.0325
import datetime
d=datetime.date(2025,2,28)
for m in range(1,31):
    bal += draw_at.get(m,0)
    # days in month
    nd = (datetime.date(d.year+(d.month==12), (d.month%12)+1, 1)-d)
    days = nd.days
    total += bal*rate*days/360
    d = nd
print("Independent monthly model, actual/360, SOFR 4.35%%: total interest %s ; reserve 4,850,000 -> shortfall %s" % (f(total), f(4_850_000-total)))
bal=0.0; total2=0.0
d=datetime.date(2025,2,28); rate=0.035+0.0325
for m in range(1,31):
    bal += draw_at.get(m,0)
    nd = (datetime.date(d.year+(d.month==12), (d.month%12)+1, 1)-d); days=nd.days
    total2 += bal*rate*days/360; d=nd
print("   same model at SOFR 3.50%%: %s ; surplus %s" % (f(total2), f(4_850_000-total2)))

# ---- Mezz PIK
print("Mezz PIK 30 months on 9.2M @12.5%% = %s ; balance at constr maturity %s" % (f(9_200_000*0.125*2.5), f(9_200_000*1.3125)))
comb = 47_500_000+9_200_000*1.3125
print("   combined debt %s / 72.8M = %.2f%% ; / 56.7M = %.2f%%" % (f(comb), comb/72_800_000*100, comb/56_700_000*100))

# ---- HVCRE
cc=2_140_000+8_200_000
print("HVCRE contributed %s / 72.8M = %.2f%% ; need 15%% = %s ; short %s" % (f(cc), cc/72_800_000*100, f(72_800_000*0.15), f(72_800_000*0.15-cc)))
print("   if land at appraised 8.9M: %s -> %.2f%%" % (f(2_140_000+8_900_000), (2_140_000+8_900_000)/72_800_000*100))
print("   if land excluded (encumbered/debt-funded): %s -> %.2f%%" % (f(2_140_000), 2_140_000/72_800_000*100))

# ---- Equity %
print("Equity incl escrow %s / 56.7M = %.2f%%" % (f(10_340_000), 10_340_000/56_700_000*100))

# ---- Land / title
print("Parcel1 298.62x305.41 = %.0f sf = %.3f ac" % (298.62*305.41, 298.62*305.41/43560))
print("Parcel2 201.88x297.63 = %.0f sf = %.3f ac" % (201.88*297.63, 201.88*297.63/43560))
print("Combined frontage along Foster = %.2f ft (appraisal says ~420)" % (298.62+201.88))
print("3.47 ac = %.0f sf ; 3.47 x 2,565,000 = %s" % (3.47*43560, f(3.47*2_565_000)))
print("0.38 ac = %.0f sf ; 100ft x 165ft = %s sf ; 125x130 = %s sf" % (0.38*43560, f(100*165), f(125*130)))
print("0.22 ac = %.0f sf" % (0.22*43560))
print("276/212 = %.2f spaces/unit" % (276/212))
print("residential sf 102,950+58,800+18,900 = %s ; +retail 18,400 = %s ; GBA 287,500 -> parking/other %s sf = %.0f sf/space" %
      (f(180_650), f(199_050), f(287_500-199_050), (287_500-199_050)/276))

print()
for r in out:
    print("%-52s calc=%-14s stated=%-14s %s" % (r[0], f(r[1]) if isinstance(r[1],(int,float)) and abs(r[1])>100 else f"{r[1]:.4f}", r[2], r[3]))
