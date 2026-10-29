import math
def dms(d,m,s): return d+m/60+s/3600
def traverse(courses):
    x=y=0.0; pts=[(0.0,0.0)]
    for lbl,brg,dist,ns,ew in courses:
        r=math.radians(brg)
        y+=ns*dist*math.cos(r); x+=ew*dist*math.sin(r)
        pts.append((x,y))
    a=0.0
    for i in range(len(pts)-1):
        a+=pts[i][0]*pts[i+1][1]-pts[i+1][0]*pts[i][1]
    return x,y,abs(a)/2

print("=== TITLE COMMITMENT EXHIBIT A (Vol from Schedule A Sec.5 / Exhibit A) ===")
t=[("Pier St line N72-15-30E",dms(72,15,30),580.00, 1, 1),
   ("bulkhead S18-22-45E",    dms(18,22,45),240.40,-1, 1),
   ("bulkhead S17-48-10E",    dms(17,48,10),239.60,-1, 1),
   ("south line S72-08-15W",  dms(72, 8,15),582.50,-1,-1),
   ("Harbor Ave N17-44-30W",  dms(17,44,30),480.20, 1,-1)]
dx,dy,area=traverse(t)
print("  closure: dx=%.2f dy=%.2f  misclosure=%.2f ft" % (dx,dy,math.hypot(dx,dy)))
print("  sum of bulkhead courses: %.2f ft" % (240.40+239.60))
print("  shoelace area = %.0f SF = %.3f acres  |  recited 139,392 SF / 3.200 ac" % (area,area/43560))
print("  ratio computed/recited = %.2fx  (delta %+.0f SF)" % (area/139392, area-139392))
print("  rent/SF if title area used: $%.2f" % (2850000/area))

print()
print("=== SURVEY CLS-2025-0417 (narrative Section 4) ===")
s=[("Pier St S78-15-30E",  dms(78,15,30),435.22,-1, 1),
   ("east line S11-44-30W",dms(11,44,30),320.47,-1,-1),
   ("south N78-15-30W",    dms(78,15,30),435.22, 1,-1),
   ("Harbor N11-44-30E",   dms(11,44,30),320.47, 1, 1)]
dx,dy,area=traverse(s)
print("  closure: dx=%.3f dy=%.3f misclosure=%.3f ft" % (dx,dy,math.hypot(dx,dy)))
print("  shoelace area = %.0f SF = %.3f acres | recited 139,392 SF" % (area,area/43560))
print("  variance %+.0f SF (%+.3f%%)" % (area-139392,(area-139392)/139392*100))
print("  eastern boundary line length 320.47 ft vs '480 linear feet of bulkhead'")
print("  pedestrian easement 15ft x 480 = %.0f SF vs 15 x 320.47 = %.0f SF" % (15*480,15*320.47))
print("  bearing difference N-line: title 72-15-30 vs survey 78-15-30 = 6d00'00\"")
print("  bearing difference E-line: title 17-44-30 vs survey 11-44-30 = 6d00'00\"")

print()
print("=== PERCENTAGE RENT: BREAKPOINT EROSION (2.5% index) ===")
bp=28500000.0; init=2850000.0
print(f"{'LeaseYr':>7}{'BaseRent':>15}{'Breakpoint':>13}{'BP/Base':>10}{'BP in Yr1 $':>14}")
for ly in [6,16,26,36,46,56,66,76,86,96]:
    n=ly-1; br=init*1.025**n
    print(f"{ly:>7}{br:>15,.0f}{bp:>13,.0f}{bp/br:>9.2f}x{bp/1.025**n:>14,.0f}")
print("  10-yr reset step at 2.5%% CPI: %.1f%%" % ((1.025**10-1)*100))
print("  Yr16 rent @2.5%% CPI after 15 yrs: $%s" % format(init*1.025**15,",.0f"))
for cpi in [0.020,0.025,0.035,0.045]:
    r16=init*(1+cpi)**15; r15=init*1.025**10
    print("    CPI %.1f%% -> Yr16 $%-12s vs Yr15 $%-12s = %+.1f%%" %
          (cpi*100, format(r16,",.0f"), format(r15,",.0f"), (r16/r15-1)*100))
print()
print("=== % RENT ILLUSTRATION (breakpoint $28.5M, rate 2.0%) ===")
for gr in [30000000,40000000,60000000,90000000,150000000]:
    pr=max(0,(gr-bp))*0.02
    print("  GR $%-13s -> %% rent $%-11s = %.1f%% of Yr1 base rent" %
          (format(gr,",.0f"), format(pr,",.0f"), pr/init*100))
print()
print("=== REVERTER EXPOSURE ===")
print("  Security deposit forfeited: $5,700,000")
print("  Improvements at risk at M3 (Oct 2030), per client email: $200M-$300M")
print("  Total forfeiture exposure: $205.7M - $305.7M")
print("  Hard costs budgeted (whole project): $352,000,000")
