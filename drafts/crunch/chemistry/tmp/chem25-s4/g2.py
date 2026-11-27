import json,re
D='/Users/gabrielwhelan/barebones/.claude/worktrees/crunch-chem-home/drafts/crunch/chemistry/'
P='chem25-s4.'
E,H='essential','helpful'
d={k:[] for k in ['0.b','0.0','0.1','0.2','0.3','0.4','0.5','0.6','0.7','1.b','1.0','1.1','1.2','1.3','1.4','1.5','1.6','2.b','2.0','2.1','2.2','2.3','3.b','3.0','3.1','3.2','3.3','3.4','3.5','4.b','4.0','4.1','4.2','4.3','4.4','4.5','4.6','5.b','5.0','5.1','5.2','5.3','5.4','6.b','6.0','6.1','6.2','6.3','6.4','7.b','7.0','7.1','7.2']}
d['0.4']=[('chem6-s1.11.1',H,'lone pair defined','high')]
d['4.b']=[('chem23-s4.10.4',H,'pi electrons in ethene C=C','high')]
d['4.1']=[('chem23-s4.10.4',H,'pi bond in ethene','high')]
d['4.2']=[('chem6-s1.9.2',E,'induced dipole','high'),('chem6-s1.2.7',H,'delta charges on polar bond','high')]
d['4.4']=[('chem23-s4.10.4',H,'pi bond electrons used','low')]
d['4.5']=[('chem6-s1.11.1',H,'lone pair on chloride','high')]
d['5.1']=[('chem6-s1.0.0',E,'electronegativity makes bond polar','high')]
d['5.3']=[('chem6-s1.11.1',H,'lone pair on chloride','high')]
d['6.1']=[('chem6-s1.11.1',H,'lone pair on oxygen','high')]
txt=open(D+'packs/chem25-s4.t1g2.txt').read()
ids=re.findall(r'^\[(chem25-s4\.[^\]]+)\]',txt,re.M)
allids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
assert set(d)=={i[len(P):] for i in ids}
out={i:{'needs':[{'id':t,'strength':s,'why':w,'confidence':f} for t,s,w,f in d[i[len(P):]]]} for i in ids}
for i,v in out.items():
    for n in v['needs']: assert n['id'] in allids and n['id']!=i
json.dump(out,open(D+'point-links/chem25-s4.t1g2.json','w'),indent=1)
print(len(out),sum(len(v['needs']) for v in out.values()),sum(n['confidence']=='low' for v in out.values() for n in v['needs']))
