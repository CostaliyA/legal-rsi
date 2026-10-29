import math

print("=== 1. AREA / GEOMETRY CHECKS ===")
print("3.2 ac in SF:", 3.2*43560)
# Survey (CLS-2025-0417) rectangle
a,b = 435.22, 320.47
print("Survey courses area (rect):", round(a*b,1), "ac:", round(a*b/43560,4))
print("Stated survey area 139,392 vs computed", round(a*b,1), "delta:", round(a*b-139392,1))

# Title commitment Exhibit A polygon (DMS -> coords)
def dms(d,m,s): return d+m/60+s/3600
courses = [
 ("N72-15-30E", 580.00, dms(72,15,30)),
 ("S18-22-45E", 240.40, dms(18,22,45)),
 ("S17-48-10E", 239.60, dms(17,48,10)),
 ("S72-08-15W", 582.50, dms(72,8,15)),
 ("N17-44-30W", 480.20, dms(17,44,30)),
]
x=y=0.0; pts=[(0,0)]
for name,dist,brg in courses:
    if name.startswith("N"):
        dy = dist*math.cos(math.radians(brg)); sx = 1
    else:
        dy = -dist*math.cos(math.radians(brg)); sx = 1
    if name.endswith("E"): dx = dist*math.sin(math.radians(brg))
    else: dx = -dist*math.sin(math.radians(brg))
    x+=dx; y+=dy
    pts.append((x,y))
    print(f"  {name} {dist}: dE={dx:8.2f} dN={dy:8.2f} -> ({x:8.2f},{y:8.2f})")
area=0
for i in range(len(pts)-1):
    area += pts[i][0]*pts[i+1][1]-pts[i+1][0]*pts[i][1]
area=abs(area)/2
print("Title Exhibit A computed area:", round(area,0), "SF =", round(area/43560,3), "acres")
print("Closure error:", round(pts[-1][0],2), round(pts[-1][1],2))
print("Easement areas: utility 20x435.22 =", 20*435.22, " pedestrian 15x480 =", 15*480, " 15x320.47 =", round(15*320.47,1))

print()
print("=== 2. RENT SCHEDULE (2.5% compounding, 5-yr steps from $2,850,000) ===")
base=2850000
for yr10 in range(0,100,5):
    y0=yr10+1
    if y0>99: break
    amt = base*(1.025)**yr10
    print(f"  Lease Yr {y0:>2}-{min(yr10+5,99):>2}: ${amt:,.2f}/yr  ${amt/12:,.2f}/mo  (step factor 1.025^{yr10})")
print(" TS stated Yr6-10: 3,224,500 / mo 268,708 ; computed monthly:", round(base*1.025**5/12,2))
print(" TS stated Yr11-15: 3,648,200 / mo 304,017 ; computed 3,648,308 /", round(base*1.025**10/12,2))
print(" per SF:", round(2850000/139392,4))

print()
print("=== 3. CPI 'greater of' reset at Yr16 (option a continued 2.5%) ===")
print(" Yr16 option (a):", round(base*1.025**15,2), " monthly:", round(base*1.025**15/12,2))
print(" Yr 96 option (a):", round(base*1.025**95,2))

print()
print("=== 4. PERCENTAGE RENT: fixed vs indexed breakpoint ===")
BP=28500000
rev6=30_000_000  # illustrative
g=0.03
def rev(year):  # year = lease/rent year index 6..99
    return rev6*(1+g)**(year-6)
print(f" {'Yr':>4} {'Gross Rev':>14} {'PR fixed BP':>13} {'BP indexed 3%':>14} {'PR indexed':>12} {'BaseRent':>13} {'PR%ofBase':>9}")
for yr in [6,10,15,20,30,45,60,80,99]:
    r=rev(yr); bp_i=BP*(1+g)**(yr-6)
    pr_f=0.02*max(0,r-BP); pr_i=0.02*max(0,r-bp_i)
    # base rent in that year: 2.5% steps each 5 yrs from rent year1
    steps=(yr-1)//5*5
    br=base*(1.025)**steps
    print(f" {yr:>4} {r:>14,.0f} {pr_f:>13,.0f} {pr_i:>14,.0f} {pr_i:>12,.0f} {br:>13,.0f} {pr_f/br*100:>8.1f}%")

print()
print("=== 5. TAX ABATEMENT ===")
AV=178_000_000; mill=0.03475
tiers={0.25:"Yr1-5",0.50:"Yr6-10",0.75:"Yr11-15",1.00:"Yr16+"}
for pct,lab in tiers.items():
    print(f"  {lab}: {pct:.0%} x 178M x 34.75mills = ${AV*pct*mill:,.0f}")
full=AV*mill
print("  Full:", round(full,0))
vals=[0.25]*5+[0.5]*5+[0.75]*5
print("  Nominal taxes paid over 15 yrs:", round(sum(AV*p*mill for p in vals),0))
print("  Nominal abatement value (vs full):", round(15*full - sum(AV*p*mill for p in vals),0))
print("  Value of waived 75% tier per yr:", round(full-AV*0.75*mill,0))
print("  Value of waived 50% tier per yr:", round(full-AV*0.50*mill,0))
print("  Value of waived 25% tier per yr:", round(full-AV*0.25*mill,0))
print("  3-yr deferral benefit (3 extra yrs at 75% instead of 100%):", round(3*(full-AV*0.75*mill),0))
print("  Land-only current: 4.2M x .03475 =", round(4_200_000*mill,0))
print("  25% of land-only:", round(4_200_000*0.25*mill,0))
print("  Abatement as % of full: 25/50/75 tiers")
print("  ground rent / land assessed value:", round(2_850_000/4_200_000,3))
print("  implied land value at 5%/6%/7%/8% ground yield:", [round(2_850_000/r,0) for r in (0.05,0.06,0.07,0.08)])

print()
print("=== 6. REMEDIATION CREDIT ===")
rent=237_500; credit=1_800_000
print("  7 months:", 7*rent, " remaining:", credit-7*rent, " month8 credit:", credit-7*rent, " tenant pays:", rent-(credit-7*rent))
print("  total check:", 7*rent+(credit-7*rent), "==", credit)
print("  2.4M - 1.8M =", 2_400_000-1_800_000)
print("  Area1 breakdown sum:", 680000+520000+85000+290000+175000+100000)
print("  Area2 breakdown sum:", 210000+145000+40000+85000+45000+25000)
print("  Contingency % check area1:", round(100000/(1850000-100000)*100,2), " area2:", round(25000/(550000-25000)*100,2))
print("  Excavation volume check Area1: 4200*6/27 =", round(4200*6/27,1), "CY")
print("  Area 4200+1600 =", 4200+1600)

print()
print("=== 7. CAPITAL STACK / LOC / DATES ===")
print(" sources:", 285_000_000+95_000_000+45_000_000)
print(" uses:", 352_000_000+38_500_000+34_500_000)
print(" LTC:", round(285/425*100,2), " equity pct:", round(140/425*100,2))
print(" LOC 24 mo:", 24*rent, " stepdown 12 mo:", 12*rent)
print(" 90-day/60-day checks n/a")
print(" LTV 75% implies min appraisal:", 285_000_000/0.75)
print(" appraised vs cost gap:", 425_000_000-285_000_000/0.75)
print(" origination fee 1%:", 0.01*285_000_000)
print(" default rate:", 2.75+4.00)
import datetime
def addm(d,m):
    y=d.year+(d.month-1+m)//12; mo=(d.month-1+m)%12+1
    return datetime.date(y,mo,d.day)
c=datetime.date(2025,10,1)
for m,lab in [(18,"M1"),(42,"M2"),(60,"M3"),(84,"M4"),(36,"RentComm"),(48,"Loan initial maturity"),(60,"Loan ext maturity")]:
    print(f"  {lab}: +{m} mo = {addm(c,m)}")
print("  Term end:", datetime.date(2124,9,30))
print("  Title commitment expiration: 6 mo from 2025-06-01 =", "2025-12-01")
print("  Bayside TS expiration: 30 days from 2025-05-28 = 2025-06-27")
print("  Exclusivity (ground lease TS) to 2025-12-31; target commencement 2025-10-01")
print("  Draft due approx 2025-06-29")
