def m(x): return f"{x:,.0f}"
# Rebuilt draw schedule that actually withholds 10% retainage
gross=[5_212_500,6_950_000,6_950_000,5_212_500,3_475_000,3_475_000,3_475_000]
ret=[round(g*0.10,2) for g in gross]
net=[g-r for g,r in zip(gross,ret)]
print("gross total",m(sum(gross)),"ret",m(sum(ret)),"net",m(sum(net)))
cont=[0,0,440_000,0,400_000,0,600_000]           # contingency 1,440,000
devf=[0,0,458_750,0,458_750,0,458_750]           # senior-funded dev fee 1,835,000
print("cont",m(sum(cont)),"devf+tail",m(sum(devf)+458_750))
draws=[9_475_000]
for g,n,c,d in zip(gross,net,cont,devf):
    draws.append(round(n+c+d,2))
draws.append(round(3_475_000+458_750,2))
print("draws",[m(d) for d in draws],"total",m(sum(draws)))
cum=0
for i,d in enumerate(draws,1):
    cum+=d
    print(i, m(d), m(cum))
print("mezz-funded dev fee", m(2_835_000-1_835_000))
print("senior loan check:", m(sum(net)+3_475_000+4_150_000+4_850_000+475_000+1_440_000+1_835_000))
# Corrected total project cost / equity
print("Corrected uses 56.7 + 3.4 payoff + 0.68 site =", m(60_780_000))
print("Equity needed:", m(60_780_000-47_500_000-9_200_000))
print("LTC on corrected:", f"{47_500_000/60_780_000*100:.2f}%")
print("LTC excl site costs:", f"{47_500_000/60_100_000*100:.2f}%")
# mezz PIK accrual
for mo in (30,42):
    print(f"PIK accrual {mo} mo:", m(9_200_000*0.125*mo/12))
print("Total debt at mini-perm maturity:", m(47_500_000+9_200_000+9_200_000*0.125*3.5))
print("Combined LTV at stab:", f"{(47_500_000+9_200_000+4_025_000)/76_200_000*100:.1f}%")
print("Combined debt service at stab:", m(47_500_000*0.0785+9_200_000*0.125), "coverage:", round(4_876_800/(47_500_000*0.0785+9_200_000*0.125),3))
# implied tax assessment
print("implied assessed value for 412,000 taxes:", m(412_000/(49_065/7_250_000)))
print("2024 land taxes:", m(29_847.12+19_218.44), "eff rate", f"{(29_847.12+19_218.44)/7_250_000*100:.3f}%")
# NC excise tax
print("NC DOT excise tax on 47.5M:", m(47_500_000/500))
# EGI per SF etc
print("opex/EGI", f"{1_262_100/6_138_900*100:.2f}%")
print("Reserves per unit", m(53_000/212))
print("value per unit ac", m(72_800_000/212), "as-stab", m(76_200_000/212))
print("profit on cost:", m(72_800_000-56_700_000), f"{(72_800_000-56_700_000)/56_700_000*100:.1f}% of cost, {(72_800_000-56_700_000)/72_800_000*100:.1f}% of value")
print("rent per SF 1BR:", round(2175/725,2))
