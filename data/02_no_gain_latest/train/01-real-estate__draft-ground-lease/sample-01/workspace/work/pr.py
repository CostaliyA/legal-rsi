base=2_850_000.0; BP=28_500_000.0; rev6=30_000_000.0; g=0.03
def base_rent(y):
    steps=((y-1)//5)*5
    return base*1.025**steps
def bp_indexed(y):
    steps=((y-1)//5)*5
    return BP*1.025**(steps-5) if steps>=5 else BP
rows=[]
for y in [6,10,15,20,30,45,60,80,99]:
    r=rev6*(1+g)**(y-6)
    bpi=bp_indexed(y)
    prf=0.02*max(0,r-BP); pri=0.02*max(0,r-bpi)
    rows.append((y,r,bpi,prf,pri,base_rent(y)))
    print(f"{y:>3} rev {r:>15,.0f} BPidx {bpi:>14,.0f} PRfixed {prf:>12,.0f} PRidx {pri:>11,.0f} baseRent {base_rent(y):>12,.0f} ratio BPidx/baseRent {bpi/base_rent(y):>5.2f}")
print()
for y in range(1,100):
    pass
tot_f=sum(0.02*max(0,rev6*(1+g)**(y-6)-BP) for y in range(6,100))
tot_i=sum(0.02*max(0,rev6*(1+g)**(y-6)-bp_indexed(y)) for y in range(6,100))
print("Total PR Years 6-99: fixed %.0f  indexed %.0f  difference %.0f" % (tot_f,tot_i,tot_f-tot_i))
print("base rent table:")
for s in range(0,100,5):
    y0=s+1
    if y0>99: break
    a=base*1.025**s
    print(f"| {y0} through {min(s+5,99)} | ${a:,.0f} | ${a/12:,.2f} |")
