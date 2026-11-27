import json,re
D='/Users/gabrielwhelan/barebones/.claude/worktrees/crunch-chem-home/drafts/crunch/chemistry/'
def L(i,s,w,c='h'): return {"id":i,"strength":{'E':'essential','H':'helpful'}[s],"why":w,"confidence":c and {'h':'high','l':'low'}[c]}
links={
'chem23-s4.3.4':[L('chem6-s1.9.0','H','London forces between molecules')],
'chem23-s4.19.1':[L('chem6-s1.9.0','E','London dispersion forces')],
'chem23-s4.20.1':[L('chem6-s1.10.1','E','dipole–dipole attractions')],
'chem23-s4.20.2':[L('chem6-s1.9.0','H','non-polar molecules, London forces only')],
}
ids="""0.b 0.0 0.1 0.2 0.3 0.4 0.5 1.b 1.0 1.1 1.2 1.3 1.4 1.5 1.6 1.7 1.8 2.b 2.0 3.b 3.0 3.1 3.2 3.3 3.4
4.b 4.0 4.1 4.2 4.3 4.4 4.5 5.b 5.0 5.1 5.2 5.3 5.4 5.5 6.b 6.0 6.1 6.2 6.3 7.b 7.0 7.1 7.2 7.3 8.b 8.0 8.1 8.2
9.b 9.0 9.1 9.2 9.3 10.b 10.0 10.1 10.2 10.3 10.4 10.5 10.6 10.7 11.b 11.0 11.1 11.2 12.b 12.0 12.1 12.2 12.3
13.b 13.0 13.1 13.2 13.3 14.b 14.0 14.1 14.2 14.3 15.b 15.0 15.1 15.2 15.3 15.4 16.b 16.0 16.1 16.2 16.3
17.b 17.0 17.1 17.2 17.3 17.4 17.5 17.6 18.b 18.0 18.1 18.2 19.b 19.0 19.1 20.b 20.0 20.1 20.2 20.3 21.b 21.0 21.1""".split()
txt=open(D+'packs/chem23-s4.t1g2.txt').read()
tgt=re.findall(r'^\[(chem23-s4\.[^\]]+)\]',txt.split('CANDIDATES')[0],re.M)
mine=['chem23-s4.'+i for i in ids]
assert mine==tgt,(set(mine)^set(tgt))
allids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
out={i:{"needs":links.get(i,[])} for i in mine}
for v in out.values():
  for n in v['needs']: assert n['id'] in allids
json.dump(out,open(D+'point-links/chem23-s4.t1g2.json','w'),ensure_ascii=False,indent=0)
print(len(out),sum(len(v['needs']) for v in out.values()),0)
