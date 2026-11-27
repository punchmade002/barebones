import json,re
B='/Users/gabrielwhelan/barebones/.claude/worktrees/crunch-chem-home/drafts/crunch/chemistry/'
def L(i,s,w,c='h'): return {"id":i,"strength":{'e':'essential','h':'helpful'}[s],"why":w,"confidence":'high' if c=='h' else 'low'}
M='chem8-s2.2.1'
D={}
for i in range(24): D[f'{i}.b']=[]
ex={
'1.1':[L('chem8-s2.2.0','h','concentration in mol per litre')],
'1.2':[L('chem8-s2.4.0','h','primary standard definition')],
'5.0':[L('chem8-s1.1.5','h','molar mass')],
'5.2':[L('chem8-s2.6.0','h','making a standard solution')],
'6.b':[L('chem8-s2.4.0','e','primary standard')],
'6.0':[L('chem8-s2.4.1','h','pure primary standard')],
'6.1':[L('chem8-s2.4.2','h','stable in air')],
'6.2':[L('chem8-s2.4.4','h','high molar mass reduces errors')],
'6.3':[L('chem8-s2.4.2','h','not stable in air')],
'7.0':[L('chem8-s2.8.3','h','pipette use')],
'7.4':[L('chem8-s2.8.4','h','pipette and filler diagram')],
'8.b':[L(M,'h','concentration and moles')],
'8.1':[L(M,'e','n = c x V')],
'8.3':[L(M,'e','c = n / V')],
'9.0':[L('chem8-s1.1.5','h','molar mass')],
'14.1':[L(M,'e','n = c x V')],
'14.4':[L(M,'e','c = n / V')],
'18.0':[L('chem8-s2.6.0','h','weighing accurately')],
'18.2':[L('chem8-s2.6.2','h','dissolve in beaker')],
'18.3':[L('chem8-s2.6.4','h','rinse into volumetric flask')],
'18.4':[L('chem8-s2.6.5','h','make up to mark')],
'18.6':[L('chem8-s2.7.1','h','volumetric flask diagram')],
'18.7':[L('chem8-s2.7.3','h','beaker and glass rod')],
'20.5':[L('chem8-s2.7.0','h','volumetric flask accuracy')],
'21.1':[L(M,'e','n = c x V')],
'21.4':[L('chem8-s1.2.1','e','mass from moles')],
'21.6':[L('chem8-s1.2.1','e','mass from moles'),L('chem8-s1.1.5','h','molar mass')],
}
EMPTY='0.0 0.1 0.2 0.3 0.4 1.0 1.3 1.4 2.0 2.1 2.2 2.3 3.0 3.1 3.2 3.3 3.4 4.0 4.1 4.2 4.3 4.4 5.1 5.3 7.1 7.2 7.3 7.5 7.6 8.0 8.2 9.1 9.2 9.3 9.4 10.0 10.1 10.2 10.3 10.4 11.0 11.1 11.2 11.3 11.4 12.0 12.1 12.2 13.0 13.1 13.2 13.3 13.4 14.0 14.2 14.3 15.0 15.1 15.2 15.3 16.0 16.1 16.2 17.0 17.1 17.2 17.3 17.4 17.5 18.1 18.5 19.0 19.1 19.2 19.3 19.4 19.5 20.0 20.1 20.2 20.3 20.4 20.6 21.0 21.2 21.3 21.5 21.7 22.0 22.1 23.0 23.1 23.2 23.3 23.4 23.5 23.6'.split()
for k in EMPTY: assert k not in ex; D[k]=[]
D.update(ex)
pk=open(B+'packs/chem15-s1.t1g2.txt').read()
tg=[];sec=None
for l in pk.split('\n'):
    if l.startswith('TARGET'): sec='T'
    elif l.startswith('CANDIDATES'): sec='C'
    m=re.match(r'\[([^\]]+)\]',l)
    if m and sec=='T': tg.append(m.group(1))
allids=set(re.findall(r'^\[([^\]]+)\]',pk,re.M))
P='chem15-s1.'
assert set(tg)==set(P+k for k in D),(set(tg)^set(P+k for k in D))
out={}
for t in tg:
    n=D[t[len(P):]]
    for x in n: assert x['id'] in allids
    out[t]={"needs":n}
json.dump(out,open(B+'point-links/chem15-s1.t1g2.json','w'),indent=1)
print(len(out),sum(len(v['needs']) for v in out.values()),sum(x['confidence']=='low' for v in out.values() for x in v['needs']))
