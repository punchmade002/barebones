import json,re
D='/Users/gabrielwhelan/barebones/.claude/worktrees/crunch-chem-home/drafts/crunch/chemistry/'
P='chem25-s4.'
E,H='essential','helpful'
# id: (cost, [(target, strength, why, conf)])
d={
'0.b':(1,[]),
'0.0':(1,[('chem5-s1.2.0',H,'covalent bond as shared pair','high')]),
'0.1':(1,[('chem25-s4.0.3',H,'free radical defined','high')]),
'0.2':(1,[('chem5-s1.2.0',H,'covalent bond as shared pair','low')]),
'0.3':(1,[]),
'0.4':(1,[('chem5-s1.10.2',H,'lone pairs','high')]),
'0.5':(1,[('chem25-s4.0.1',H,'homolytic fission','high')]),
'0.6':(1,[]),
'0.7':(1,[]),
'1.b':(1,[('chem25-s1.1.0',H,'substitution reaction','high')]),
'1.0':(1,[('chem25-s1.1.1',H,'same chlorination equation','high')]),
'1.1':(1,[('chem25-s4.0.1',E,'homolytic fission','high'),('chem25-s4.0.5',E,'fishhook arrows','high')]),
'1.2':(1,[('chem25-s4.0.3',E,'free radicals','high')]),
'1.3':(1,[('chem25-s4.1.2',E,'uses methyl radical formed','high')]),
'1.4':(1,[('chem25-s4.0.7',E,'chain reaction','high')]),
'1.5':(2,[('chem25-s4.0.3',E,'radicals combining','high')]),
'1.6':(1,[('chem25-s4.1.0',H,'monochlorination overall equation','high')]),
'2.b':(1,[('chem25-s4.1.b',E,'same three stages','high')]),
'2.0':(1,[('chem25-s4.1.0',H,'parallel with methane equation','high')]),
'2.1':(1,[('chem25-s4.1.1',H,'initiation as for methane','high')]),
'2.2':(2,[('chem25-s4.1.2',H,'propagation steps as for methane','high')]),
'2.3':(2,[('chem25-s4.1.5',E,'termination as for methane','high')]),
'3.b':(1,[('chem25-s4.1.b',H,'radical chain mechanism','high')]),
'3.0':(1,[('chem25-s4.1.1',E,'UV splits Cl2 in initiation','high')]),
'3.1':(1,[('chem25-s4.1.4',E,'propagation chain reaction','high')]),
'3.2':(1,[('chem25-s4.1.5',E,'termination steps','high')]),
'3.3':(1,[('chem25-s4.1.5',E,'termination','high')]),
'3.4':(1,[('chem25-s4.0.3',H,'free radicals','high')]),
'3.5':(1,[('chem25-s4.0.3',H,'free radicals','high')]),
'4.b':(1,[('chem25-s1.0.0',H,'addition reaction','high')]),
'4.0':(1,[('chem25-s1.0.3',H,'same ethene chlorine equation','high')]),
'4.1':(1,[('chem5-s1.12.2',E,'pi bond','high')]),
'4.2':(1,[('chem5-s1.3.3',E,'partial charges/dipole','high'),('chem25-s4.4.1',E,'pi electron density','high')]),
'4.3':(1,[('chem25-s4.0.2',E,'heterolytic fission','high'),('chem25-s4.0.4',E,'curved arrow','high')]),
'4.4':(2,[('chem25-s4.0.6',E,'carbocation','high'),('chem25-s4.0.4',E,'curved arrow','high')]),
'4.5':(1,[('chem25-s4.4.4',E,'attacks the carbocation','high')]),
'4.6':(1,[('chem25-s4.4.5',H,'ions adding one after other','high')]),
'5.b':(1,[('chem25-s4.4.b',E,'same ionic route','high')]),
'5.0':(1,[('chem25-s1.0.4',H,'same ethene HCl equation','high')]),
'5.1':(1,[('chem5-s1.3.3',E,'polar bond partial charges','high')]),
'5.2':(2,[('chem25-s4.0.4',E,'curved arrows','high'),('chem25-s4.4.4',H,'carbocation formation','high')]),
'5.3':(1,[('chem25-s4.4.5',H,'attack by negative ion','high')]),
'5.4':(1,[('chem25-s4.5.2',H,'H-X bond breaks','high')]),
'6.b':(1,[('chem25-s4.4.4',E,'carbocation intermediate','high')]),
'6.0':(1,[('chem25-s4.4.0',H,'normal dichloroethane product','high')]),
'6.1':(1,[('chem25-s4.4.4',E,'carbocation attacked','high')]),
'6.2':(1,[('chem25-s4.6.1',E,'water attack on carbocation','high')]),
'6.3':(1,[('chem25-s4.6.1',H,'nucleophile attacks carbocation','high')]),
'6.4':(1,[('chem25-s4.6.3',E,'bromine adds first','high')]),
'7.b':(1,[]),
'7.0':(1,[('chem25-s4.1.b',H,'radical substitution mechanism','high')]),
'7.1':(1,[('chem25-s4.4.b',H,'ionic addition mechanism','high')]),
'7.2':(2,[('chem25-s4.4.4',E,'four steps with carbocation','high')]),
}
txt=open(D+'packs/chem25-s4.t1g1.txt').read()
ids=re.findall(r'^\[(chem25-s4\.[^\]]+)\]',txt,re.M)
ids=[i for i in ids]
allids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
out={}
for i in ids:
    k=i[len(P):]
    c,n=d[k]
    out[i]={'cost':c,'needs':[{'id':t,'strength':s,'why':w,'confidence':f} for t,s,w,f in n]}
assert set(d)=={i[len(P):] for i in ids}, set(d)^{i[len(P):] for i in ids}
for i,v in out.items():
    for n in v['needs']: assert n['id'] in allids and n['id']!=i,(i,n)
json.dump(out,open(D+'point-links/chem25-s4.t1g1.json','w'),indent=1)
print(len(out),sum(len(v['needs']) for v in out.values()),sum(v['cost']==2 for v in out.values()),sum(n['confidence']=='low' for v in out.values() for n in v['needs']))
