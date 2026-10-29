import re
src=open('memo.md').read()
specs=[
 ([0.75,5.75],'ll'),
 ([1.45,0.75,1.50,2.80],'llll'),
 ([0.50,1.75,1.60,2.05,0.60],'lllll'),
 ([1.90,4.60],'ll'),
 ([1.40,0.95,2.65,1.50],'llll'),
 ([0.45,4.20,1.85],'lll'),
 ([2.15,3.85,0.50],'lll'),
]
lines=src.split('\n')
sep=[i for i,l in enumerate(lines) if re.fullmatch(r'\|[ :\|-]*-[ :\|-]*\|\s*', l)]
print('tables:',len(sep))
assert len(sep)==len(specs), len(sep)
for idx,(w,al) in zip(sep,specs):
    cells=[('-'*max(6,int(round(x*20)))+(': ' if False else '')) for x in w]
    cells=[('-'*max(6,int(round(x*20)))) for x in w]
    lines[idx]='|'+'|'.join(':'+c for c in cells)+'|'
open('memo_fixed.md','w').write('\n'.join(lines))
print('ok')
