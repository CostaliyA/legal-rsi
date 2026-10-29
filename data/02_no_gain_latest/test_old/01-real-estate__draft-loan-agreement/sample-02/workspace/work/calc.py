from decimal import Decimal as D

def m(x): return f"{x:,.0f}"
def p(x): return f"{x*100:.2f}%"

loan=47_500_000; mezz=9_200_000; gmp=34_750_000
uses={'land':8_200_000,'hard':gmp,'soft':4_150_000,'intres':4_850_000,'orig':475_000,'devfee':2_835_000,'conting':1_440_000}
tot=sum(uses.values())
print("Total uses",m(tot), "sum of sources", m(loan+mezz))
print("LTC", p(loan/tot), "max loan at 80%", m(tot*0.80), "excess", m(loan-tot*0.80))
print("Combined leverage", p((loan+mezz)/tot))
ac=72_800_000; ast=76_200_000; asis=8_900_000
print("LTV ac",p(loan/ac),"max loan @65% ac",m(ac*0.65),"excess",m(loan-ac*0.65))
print("LTV as",p(loan/ast), "max loan @65% as", m(ast*0.65))
# NOI
res=212*2245*12; retail=18_400*30; other=198_000
gpi=res+retail+other
print("Residential 212*2245*12 =",m(res),"(stated 5,712,000 diff", m(5_712_000-res),")")
print("GPI computed",m(gpi),"stated 6,462,000")
vac=round(6_462_000*0.05); egi=6_462_000-vac; noi=egi-1_262_100
print("Vac",m(vac),"EGI",m(egi),"NOI",m(noi))
print("cap", p(4_876_800/ast))
ds=loan*0.0785
print("Annual interest @7.85%",m(ds),"DSCR",round(4_876_800/ds,4))
print("DSCR @ +200bp", round(4_876_800/(loan*0.0985),3))
ccr=287_500*0.12
print("CC&R assessment",m(ccr),"NOI adj",m(4_876_800-ccr),"DSCR adj",round((4_876_800-ccr)/ds,4))
print("OpEx ratio",p(1_262_100/egi))
# draw schedule
draws=[9_475_000,5_212_500,6_950_000,6_950_000,5_212_500,3_475_000,3_475_000,3_475_000,3_275_000]
print("draw total",m(sum(draws)))
hard=[0,5_212_500,6_950_000,6_950_000,5_212_500,3_475_000,3_475_000,3_475_000,3_475_000]
print("hard gross",m(sum(hard)))
ret=[0,521_250,695_000,695_000,521_250,347_500,347_500,347_500,-3_475_000]
print("retainage net col",m(sum(ret)))
net=[0,4_691_250,6_255_000,6_255_000,4_691_250,3_127_500,3_127_500,3_127_500,3_475_000]
print("net hard",m(sum(net)))
devf=[0,0,695_000,695_000,521_250,245_000,245_000,233_750,200_000]
cont=[0,521_250,102_500,102_500,113_750,600_000]
print("devfee col",m(sum(devf)),"contingency col",m(sum(cont)))
comp=sum(net)+4_150_000+4_850_000+475_000+sum(devf)+sum(cont)
print("sum of draw components",m(comp),"vs stated total 47,500,000; diff",m(comp-47_500_000))
print("10% of GMP",m(gmp*0.10),"Draw 9 label 3,275,000 diff",m(gmp*0.10-3_275_000))
print("Draw 9 components: 3,475,000 hard + 200,000 devfee + 600,000 conting =", m(3_475_000+200_000+600_000),"vs stated 3,275,000")
# interest reserve model
def model(sofr, spread=0.0325, months=30):
    draws_by_month={1:9_475_000,4:5_212_500,9:6_950_000,14:6_950_000,18:5_212_500,21:3_475_000,25:3_475_000,30:3_475_000}
    bal=0; cum=0; rate=sofr+spread
    for mo in range(1,months+1):
        bal+=draws_by_month.get(mo,0)
        cum+=bal*rate/12
    return cum
for s in (0.035,0.04,0.0435,0.0475,0.0525,0.0535):
    print(f"SOFR {s*100:.2f}% all-in {(s+0.0325)*100:.2f}% projected interest {m(model(s))} surplus/(short) {m(4_850_000-model(s))}")
# what SOFR makes reserve exactly adequate
lo,hi=0.0,0.30
for _ in range(200):
    mid=(lo+hi)/2
    if model(mid)>4_850_000: hi=mid
    else: lo=mid
print("breakeven SOFR for 4.85M reserve:", p(lo))
print("breakeven SOFR (mini-perm spread 3.50%):", p(lo), "approx")
# credit memo method
print("CM method: 28.5M*7.60%*2.5 =", m(28_500_000*0.076*2.5))
print("full draw 30 mo:", m(47_500_000*0.076*2.5))
# NFA: 14 units loss
lost=14*2245*12
print("14 units lost rev",m(lost),"NOI after",m(4_876_800-lost),"DSCR",round((4_876_800-lost)/ds,4))
# HVCRE
contrib=2_140_000+8_200_000
print("Contrib capital",m(contrib),"pct of as-completed",p(contrib/ac),"15% needed",m(ac*0.15))
print("If land funded by mezz (not contributed): contrib =", m(2_140_000), p(2_140_000/ac))
# site area checks
a1=305.41*298.62; a2=297.63*201.88
print("Parcel1 sf",m(a1),"acres",round(a1/43560,3),"Parcel2 sf",m(a2),"acres",round(a2/43560,3),"total",round((a1+a2)/43560,3))
print("Foster frontage per survey", 298.62+201.88)
print("3.47 acres sf", m(3.47*43560))
# land basis
print("Land 8.2 + demo/remediation 0.68 =", m(8_880_000), "vs as-is appraisal 8.9M; implied appreciation", m(8_900_000-8_880_000))
print("Total project cost incl 680k site costs:", m(56_700_000+680_000), "LTC", p(47_500_000/57_380_000))
print("Total project cost incl 680k + 3.4M payoff:", m(56_700_000+680_000+3_400_000), "LTC", p(47_500_000/60_780_000))
print("Payoff gap: uses without payoff = 56.7M; cash sources = 56.7M")
# equity
print("Land equity if 3.4M assumed debt:", m(8_200_000-3_400_000))
# DSCR test at mini-perm commencement with T-12
print("Trailing 12 at TCO ~ zero => DSCR fail")
# developer fee
print("Dev fee as % of costs excl fee:", p(2_835_000/(56_700_000-2_835_000)))
print("Contingency % hard:", p(1_440_000/gmp), " hard-only contingency 1.14M =", p(1_140_000/gmp))
print("soft contingency % soft:", p(300_000/4_150_000))
# soft costs total check
soft=[1_680_000,685_000,425_000,310_000,185_000,35_000,245_000,125_000,210_000,250_000]
print("soft items sum",m(sum(soft)))
hard_items=[3_180_000,2_950_000,6_420_000,4_275_000,5_850_000,5_940_000,920_000,3_590_000,1_625_000]
print("hard items sum",m(sum(hard_items)))
