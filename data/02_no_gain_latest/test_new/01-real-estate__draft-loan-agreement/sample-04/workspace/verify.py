from decimal import Decimal as D
def p(label, val): print(f"{label:60s} {val}")

# Core
loan = D('47500000'); mezz = D('9200000')
uses = {
 'Land': D('8200000'), 'Hard GMP': D('34750000'), 'Soft': D('4150000'),
 'InterestReserve': D('4850000'), 'OrigFee': D('475000'), 'DevFee': D('2835000'), 'Contingency': D('1440000')}
tp = sum(uses.values()); p("Total Project Costs", tp)
p("LTC senior", f"{(loan/tp*100):.2f}%")
p("Max loan @80%", tp*D('0.80')); p("Shortfall vs 47.5M", loan - tp*D('0.80'))
p("Combined leverage (senior+mezz)/TPC", f"{((loan+mezz)/tp*100):.2f}%")
p("LTV as-completed", f"{(loan/D('72800000')*100):.2f}%")
p("LTV as-stab", f"{(loan/D('76200000')*100):.2f}%")

# NOI
res = D('5712000'); retail = D('552000'); other = D('198000')
gpi = res+retail+other; p("GPI", gpi)
vac = gpi*D('0.05'); p("Vacancy 5%", vac)
egi = gpi-vac; p("EGI", egi)
opex = [D(x) for x in ['214862','412000','148500','96200','127500','142000','38000','53000','30038']]
p("OpEx sum", sum(opex))
noi = egi-sum(opex); p("NOI", noi)
p("Cap 6.40% -> value", noi/D('0.064'))
p("212 x 2245 x 12", 212*2245*12, )
p("OpEx ratio", f"{(sum(opex)/egi*100):.2f}%")
# debt service
ds = loan*D('0.0785'); p("Annual DS @7.85%", ds)
p("DSCR", f"{noi/ds:.3f}")
ds_stress = loan*D('0.0985'); p("Stressed DS @9.85%", ds_stress); p("Stressed DSCR", f"{noi/ds_stress:.3f}")
# 200bps sensitivity: SOFR 6.35 + 3.50 = 9.85
# 14 units lost
loss = 14*2245*12; p("14-unit revenue loss", loss)
p("NOI less loss", noi-loss); p("DSCR w/o 14 units", f"{(noi-loss)/ds:.3f}")
# CC&R assessment
p("CC&R assessment 0.12/sf on 287,500 sf", D('287500')*D('0.12'))
noi2 = noi - D('287500')*D('0.12'); p("NOI less CC&R", noi2)
p("DSCR after CC&R", f"{noi2/ds:.3f}"); p("Value after CC&R", noi2/D('0.064'))
# retainage
p("10% retainage of GMP", D('34750000')*D('0.10'))
p("Draw 9 release per TS", D('3275000'))
p("Retainage never released", D('34750000')*D('0.10') - D('3275000'))
# draw schedule vs budget
draws = [D(x) for x in ['9475000','5212500','6950000','6950000','5212500','3475000','3475000','3475000','3275000']]
p("Sum of draws (TS)", sum(draws))
p("Draw1 components", D('4150000')+D('4850000')+D('475000'))
p("Hard cost draws 2-8", sum(draws[1:8]))
p("DevFee+Contingency not in TS draws", D('2835000')+D('1440000'))
p("Hard-cost $ allocated by TS draws (2-8 gross + D9)", sum(draws[1:8])+D('3275000'))
# xlsx draw components total
comp = D('34750000')+D('4150000')+D('4850000')+D('475000')+D('2835000')+D('1440000')
p("xlsx component total", comp); p("vs stated total draws", D('47500000')); p("xlsx overstatement", comp-D('47500000'))
# Detailed budget check
sen = D('34750000')+D('4150000')+D('4850000')+D('475000')+D('1835000')+D('1440000')
p("Detailed budget senior-funded total", sen)
mez = D('8200000')+D('1000000'); p("Detailed budget mezz-funded", mez)
p("Hard cost contingency pct", f"{(D('1140000')/D('34750000')*100):.2f}%")
p("Total contingency pct of TPC", f"{(D('1440000')/tp*100):.2f}%")
# Interest reserve math
pay = D('47500000')
for sofr in ['0.0350','0.0435','0.0525','0.0635']:
    r = D(sofr)+D('0.0325'); print(f"  SOFR {sofr} all-in {r*100:.2f}% : full-draw 30mo interest = {pay*r*D(2.5):,.0f}")
# land equity
p("Land value less $3.4M DOT", D('8900000')-D('3400000'))
# Project cost including DOT payoff
p("TPC incl 3.4M payoff", tp+D('3400000'))
p("LTC if payoff added & equity funded", f"{(loan/(tp+D('3400000'))*100):.2f}%")
p("LTC if payoff added & loan funded", f"{((loan+D('3400000'))/(tp+D('3400000'))*100):.2f}%")
# HVCRE
cc = D('10340000'); p("HVCRE contributed capital pct", f"{(cc/D('72800000')*100):.2f}%")
p("15% of as-completed", D('72800000')*D('0.15'))
p("HVCRE if only 2.14M cash counts", f"{(D('2140000')/D('72800000')*100):.2f}%")
# partial guaranty
p("25% of loan", loan*D('0.25'))
p("Osei guaranty / NW", f"{(loan*D('0.25')/D('11500000')*100):.2f}%")
p("Vasquez guaranty / NW", f"{(loan*D('0.25')/D('29800000')*100):.2f}%")
# frontage / acreage
import math
p("Parcel1 SF", D('298.62')*D('305.41')); p("Parcel1 acres", f"{(D('298.62')*D('305.41')/D('43560')):.3f}")
p("Parcel2 SF", D('201.88')*D('297.63')); p("Parcel2 acres", f"{(D('201.88')*D('297.63')/D('43560')):.3f}")
p("Foster frontage (N-S sum)", D('298.62')+D('201.88'))
p("3.47 acres in SF", D('3.47')*D('43560'))
p("Affected 0.38 ac as % of parcel2 (1.38)", f"{(D('0.38')/D('1.38')*100):.1f}%")
p("Affected 0.38 ac as % of parcel2 (1.58 per ESA)", f"{(D('0.38')/D('1.58')*100):.1f}%")
p("xlsx says affected 100ft x 165ft =", f"{(D('100')*D('165')/D('43560')):.2f} acres")
p("ESA fig3 says 125 x 130 =", f"{(D('125')*D('130')/D('43560')):.2f} acres")
# Unused line fee
p("Unused fee 0.25% on avg undrawn", "n/a")
# Bank asset ratio
p("loan / 18.6B", f"{(loan/D('18600000000')*100):.3f}%")
# land sale comps
for s,pr,ac in [('1',D('7447000'),D('2.81')),('2',D('5460000'),D('1.95')),('3',D('9888000'),D('4.12')),('4',D('7168000'),D('3.05'))]:
    print(f"  land sale {s}: {pr/ac:,.0f}/acre")
p("3.47 x 2,565,000", D('3.47')*D('2565000'))
p("per unit as-completed", D('72800000')/212); p("per unit as-stab", D('76200000')/212)
p("psf as-completed", f"{D('72800000')/D('287500'):.2f}"); p("psf as-stab", f"{D('76200000')/D('287500'):.2f}")
