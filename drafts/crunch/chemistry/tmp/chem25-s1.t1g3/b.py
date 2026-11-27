import json,re
D='/Users/gabrielwhelan/barebones/.claude/worktrees/crunch-chem-home/drafts/crunch/chemistry/'
counts=[8,8,7,6,6,4,6,6,7,6,7,6,7,6,3,5]
ids=[]
for s,n in enumerate(counts):
    ids.append(f'chem25-s1.{s}.b'); ids+= [f'chem25-s1.{s}.{i}' for i in range(n)]
def L(i,st,w,c='high'): return {"id":'chem5-s1.'+i,"strength":st,"why":w,"confidence":c}
N={
'chem25-s1.0.b':[L('12.4','helpful','double bond opens (pi bond)','low')],
'chem25-s1.0.1':[L('2.2','helpful','double and triple bonds')],
'chem25-s1.6.b':[L('12.4','essential','pi bond added to sigma bond')],
'chem25-s1.6.0':[L('12.4','essential','double bond is sigma plus pi')],
'chem25-s1.6.1':[L('12.2','essential','pi bond of C=C')],
'chem25-s1.6.2':[L('12.2','essential','C=O pi bond')],
'chem25-s1.7.0':[L('2.0','helpful','covalent bonds joining units','low')],
'chem25-s1.8.1':[L('12.2','essential','pi bond breaking in C=C')],
'chem25-s1.10.b':[L('3.2','helpful','polar covalent bond')],
'chem25-s1.10.2':[L('3.2','essential','polar C-Cl bond, partial charges')],
'chem25-s1.11.b':[L('13.1','helpful','benzene ring','low')],
'chem25-s1.11.0':[L('13.1','helpful','benzene ring','low')],
'chem25-s1.13.2':[L('3.0','helpful','non-polar covalent C-C bonds')],
'chem25-s1.13.3':[L('12.2','helpful','pi bonds absent','low'),L('3.2','helpful','polar group to attack','low')],
}
out={i:{"needs":N.get(i,[])} for i in ids}
t=open(D+'packs/chem25-s1.t1g3.txt').read()
tg=re.findall(r'^\[(chem25-s1\.[^\]]+)\]',t.split('CANDIDATES')[0],re.M)
cand=set(re.findall(r'^\[(chem5-s1\.[^\]]+)\]',t,re.M))
assert tg==ids, (set(tg)^set(ids))
assert all(n['id'] in cand for v in out.values() for n in v['needs'])
json.dump(out,open(D+'point-links/chem25-s1.t1g3.json','w'),indent=1)
print(len(out),sum(len(v['needs']) for v in out.values()),sum(n['confidence']=='low' for v in out.values() for n in v['needs']))
