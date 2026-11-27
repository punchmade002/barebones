import json,re,sys
def n(i,s,w,c='high'): return {"id":i,"strength":s,"why":w,"confidence":c}
E,H='essential','helpful'
L={
'1.0':[n('chem5-s1.2.1',H,'single covalent bond')],
'1.2':[n('chem5-s1.3.0',H,'non-polar bond meaning')],
'1.3':[n('chem10-s2.0.1',H,'molecular formula')],
'1.4':[n('chem5-s1.2.2',H,'double bond')],
'1.5':[n('chem5-s1.2.3',H,'triple bond')],
'1.6':[n('chem5-s1.13.0',H,'delocalised electrons')],
'2.2':[n('chem5-s1.2.2',H,'C=O double bond')],
'2.3':[n('chem5-s1.2.2',H,'C=O double bond')],
'2.4':[n('chem10-s2.0.1',H,'same molecular formula')],
'3.2':[n('chem10-s2.0.1',H,'same molecular formula')],
'15.0':[n('chem10-s2.0.1',E,'molecular formula')],
'16.0':[n('chem10-s2.0.0',E,'empirical formula')],
'16.1':[n('chem10-s2.0.2',H,'empirical versus molecular formula')],
'17.0':[n('chem5-s1.18.2',H,'tetrahedral shape 109.5 degrees')],
'17.2':[n('chem5-s1.18.1',H,'trigonal planar shape 120 degrees')],
'17.5':[n('chem5-s1.18.0',H,'linear shape 180 degrees')],
'17.7':[n('chem5-s1.16.2',E,'electron pairs repel, spread apart')],
'20.0':[n('chem10-s2.0.1',H,'molecular formula')],
'23.0':[n('chem10-s2.0.1',H,'molecular formula')],
'23.5':[n('chem5-s1.9.3',H,'carbon valency 4')],
}
P='chem24-s1.'
src=open(sys.argv[2]).read()
ids=re.findall(r'^\[(chem24-s1\.[^\]]+)\]',src.split('CANDIDATES')[0],re.M)
assert set(L)<={i[len(P):] for i in ids}
allids=set(re.findall(r'^\[([^\]]+)\]',src,re.M))
res={i:{"needs":L.get(i[len(P):],[])} for i in ids}
for v in res.values():
    for x in v['needs']: assert x['id'] in allids
json.dump(res,open(sys.argv[1],'w'),indent=0)
print(len(ids),sum(len(v['needs']) for v in res.values()),sum(x['confidence']=='low' for v in res.values() for x in v['needs']))
