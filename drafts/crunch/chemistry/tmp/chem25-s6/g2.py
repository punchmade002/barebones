import json,re
H,E='helpful','essential'
L={
'1.0':[('chem6-s2.5.1',H,'polar molecules have charged ends','high')],
'1.1':[('chem6-s2.1.2',H,'non-polar substances dissolve in non-polar','high')],
'1.2':[],
'1.3':[('chem6-s2.1.0',H,'like dissolves like','high')],
'2.1':[('chem6-s2.1.0',H,'like dissolves like','high')],
'7.0':[('chem20-s2.10.3',H,'not biodegradable meaning','low')],
'7.1':[('chem20-s2.6.b',H,'eutrophication from nutrients','high')],
'8.0':[('chem26-s3.0.0',H,'limiting reagent','high')],
'9.1':[('chem6-s2.1.0',H,'solvent dissolves both','low')],
'9.6':[('chem26-s3.0.0',H,'limiting versus excess','high')],
'11.1':[('chem6-s2.1.2',H,'oil and water do not mix','low')],
'13.b':[('chem26-s3.0.0',H,'limiting reagent definition','high')],
'13.0':[('chem26-s3.0.2',H,'product set by limiting reagent','high')],
'13.2':[('chem26-s3.0.1',H,'reagent in excess','high')],
'13.5':[('chem26-s3.0.1',H,'reagent in excess','high')],
'15.1':[('chem26-s3.1.1',H,'convert mass to moles','high')],
'15.2':[('chem26-s3.1.2',E,'compare moles needed to find limiting','high')],
'15.3':[('chem26-s3.1.3',E,'less reactant than ratio needs','high')],
'15.4':[('chem26-s3.1.6',E,'moles of excess left','high')],
}
t=open('packs/chem25-s6.t1g2.txt').read()
ids=set(re.findall(r'^\[([^\]]+)\]',t,re.M))
tg=re.findall(r'^\[([^\]]+)\]',t.split('CANDIDATES')[0],re.M)
out={}
for x in tg:
    k=x.split('chem25-s6.')[1]
    out[x]={'needs':[{'id':i,'strength':s,'why':w,'confidence':c} for i,s,w,c in L.get(k,[])]}
for v in out.values():
    for n in v['needs']: assert n['id'] in ids and not n['id'].startswith('chem25-s6'),n
assert set(L)<={x.split('chem25-s6.')[1] for x in tg}
json.dump(out,open('point-links/chem25-s6.t1g2.json','w'))
print(len(out),sum(len(v['needs']) for v in out.values()),sum(n['confidence']=='low' for v in out.values() for n in v['needs']))
