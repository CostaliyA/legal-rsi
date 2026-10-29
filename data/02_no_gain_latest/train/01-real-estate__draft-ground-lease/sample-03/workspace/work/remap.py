import subprocess, re, json, sys
def run():
    n=int(re.search(r'Pages:\s+(\d+)', subprocess.run(['pdfinfo','lease_final.pdf'],capture_output=True,text=True).stdout).group(1))
    pages={i: re.sub(r'\s+',' ',subprocess.run(['pdftotext','-f',str(i),'-l',str(i),'lease_final.pdf','-'],capture_output=True,text=True).stdout) for i in range(1,n+1)}
    body_start=min(i for i in pages if "THIS GROUND LEASE AGREEMENT (this" in pages[i])
    heads=[l[2:].strip() for l in open('lease.md') if l.startswith('# ')]
    m={}
    for h in heads:
        key=re.sub(r'\s+',' ',h)[:38]; hit=None
        for i in range(body_start,n+1):
            if key in pages[i]: hit=i;break
        m[h]=hit
    return n, body_start, m
if __name__=='__main__':
    n,bs,m=run()
    print("pages",n,"body_start",bs,"unmatched",[k for k,v in m.items() if v is None])
    with open('pagemap.txt','w') as f:
        for k,v in m.items(): f.write(f"{k}\t{v}\n")
