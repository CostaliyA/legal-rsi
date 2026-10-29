import math
from datetime import date

print("=== LEGAL DESCRIPTION CHECK: TITLE COMMITMENT EXHIBIT A ===")
def course(bearing_deg, dist, quad):  # bearing measured clockwise from N
    r=math.radians(bearing_deg)
    dx=dist*math.sin(r); dy=dist*math.cos(r)
    return dx,dy
def dms(d,m,s): return d+m/60+s/3600

# Title Commitment Exhibit A courses
c=[]
b1=dms(72,15,30);   c.append(("N72-15-30 E",580.00, 1,1))
b2=dms(18,22,45);   c.append(("S18-22-45 E",240.40,-1,1))
b3=dms(17,48,10);   c.append(("S17-48-10 E",239.60,-1,1))
b4=dms(72,8,15);    c.append(("S72-08-15 W",582.50,-1,-1))
b5=dms(17,44,30);   c.append(("N17-44-30 W",480.20, 1,-1))
x=y=0.0; pts=[(0,0)]
for lbl,d,ns,ew in c:
    r=math.radians(d)
    y+=ns*d*math.cos(r); x+=ew*d*math.sin(r)
    pts.append((x,y))
print("  computed closure error (ft): dx=%.2f dy=%.2f dist=%.2f" % (x,y,math.hypot(x,y)))
area=0
for i in range(len(pts)-1):
    area+=pts[i][0]*pts[i+1][1]-pts[i+1][0]*pts[i][1]
area=abs(area)/2
print("  shoelace area = %.0f SF = %.3f acres" % (area, area/43560))
print("  recited area  = 139,392 SF = 3.200 acres")
print("  RATIO computed/recited = %.2fx" % (area/139392))
print("  implied rent/SF using title area: $%.2f" % (2850000/area))

print()
print("=== LEGAL DESCRIPTION CHECK: SURVEY (CLS-2025-0417) ===")
w=435.22; h=320.47
print("  rectangle %.2f x %.2f = %.0f SF = %.4f acres" % (w,h,w*h,w*h/43560))
print("  recited = 139,392 SF ; variance = %+.0f SF (%+.3f%%)" % (w*h-139392,(w*h-139392)/139392*100))
print("  distance required for exactly 139,392 at width 435.22 = %.2f ft" % (139392/435.22))
print("  'eastern boundary line' = 320.47 ft, but narrative claims 480 LF of bulkhead")
print("  pedestrian easement: 15 x 480 = %.0f SF ; 15 x 320.47 = %.0f SF" % (15*480, 15*320.47))
print()
print("=== PERCENTAGE RENT / BREAKPOINT EROSION (2.5% index) ===")
bp=28500000.0; init=2850000.0
rows=[]
for ly in [6,16,26,36,46,56,66,76,86,96]:
    n=ly-1
    br=init*1.025**n
    rows.append((ly,br,bp,bp/br,bp/1.025**(n)))
print(f"{'LeaseYr':>7}{'BaseRent':>16}{'Breakpoint':>14}{'BP/BaseRent':>13}{'BP in 2025$':>15}")
for ly,br,b,bpr,real in rows:
    print(f"{ly:>7}{br:>16,.0f}{b:>14,.0f}{bpr:>13,.2f}x{real:>15,.0f}")
print()
print("  Reset step at each 10-yr reset (2.5% CPI): %.2f%%" % ((1.025**10-1)*100))
print("  Yr16 rent with 15 yrs CPI at 2.5%%: %,.0f" % (init*1.025**15))
for cpi in [0.020,0.025,0.035,0.045]:
    print("   CPI %.1f%% -> Yr16 rent $%s ; jump from Yr15 $%s = +%.1f%%" %
          (cpi*100, format(init*(1+cpi)**15,",.0f"), format(init*1.025**10,",.0f"),
           (init*(1+cpi)**15/(init*1.025**10)-1)*100))
print()
print("=== PERCENTAGE RENT ILLUSTRATION ===")
for gr in [30000000,40000000,60000000,90000000,150000000]:
    pr=max(0,(gr-bp))*0.02
    print("  Gross Revenues $%-14s -> %rent $%-12s  (= %.1f%% of Yr-1 base rent)" %
          (format(gr,",.0f"), format(pr,",.0f"), pr/init*100))
