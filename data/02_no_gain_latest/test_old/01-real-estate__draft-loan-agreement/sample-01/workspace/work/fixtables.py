import re
src=open('la.md').read()

# 1. avoid markdown ordered-list conversion
src=re.sub(r'(?m)^(\d+)\. ', r'(\1) ', src)

specs=[
 ([1.45,5.05], 'll'),
 ([3.25,3.25], 'll'),
 ([0.42,2.05,0.95,0.95,0.98,0.95], 'llrrrr'),
 ([0.45,1.90,0.60,0.95,0.95,0.90,0.75], 'llrrrrl'),
 ([1.85,0.85,3.60], 'lrl'),
 ([4.60,1.75], 'lr'),
 ([0.42,6.00], 'll'),
 ([1.45,2.90,2.05], 'lll'),
 ([1.75,1.55,0.95,1.10,0.95], 'llrrr'),
 ([2.75,1.30,1.40,0.90], 'llll'),
 ([2.05,1.70,1.35,1.25], 'llll'),
]
specs[2]=([0.42,2.05,0.95,0.95,0.98,0.95], 'llrrrr'); specs[8]=([1.75,1.55,0.95,1.10,0.95],'llrlr')

lines=src.split('\n')
sep_idx=[i for i,l in enumerate(lines) if re.fullmatch(r'\|[ \-\|:]+\|\s*', l)]
print('separator rows found:', len(sep_idx))
assert len(sep_idx)==len(specs), (len(sep_idx), len(specs))

for idx,(widths,al) in zip(sep_idx,specs):
    cells=[]
    for w,a in zip(widths,al):
        n=max(6,int(round(w*20)))
        dashes='-'*n
        if a=='r': cells.append(dashes+':')
        else: cells.append(':'+dashes)
    lines[idx]='|'+'|'.join(cells)+'|'
open('la_fixed.md','w').write('\n'.join(lines))
print('written')
