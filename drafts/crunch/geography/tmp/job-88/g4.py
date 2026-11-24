import json,re
P='/Users/gabrielwhelan/barebones/drafts/crunch/geography/'
p='geo-population-migration-s6.'
E=[]
L={ # explicit link decisions; all other targets explicitly empty
'11.0':[('geo-region-continental-s1.89.0','helpful','migrants from Bihar/UP to cities','high')],
'11.1':[('geo-region-continental-s1.113.0','helpful','small holdings, landlessness, debt','high')],
'11.3':[('geo-region-continental-s1.103.0','helpful','India urban share figures','high')],
'11.4':[('geo-region-continental-s1.103.1','helpful','urban agglomeration idea','low')],
'11.5':[('geo-region-continental-s1.88.1','helpful','Bihar density figure','high')],
'12.0':[('geo-region-continental-s1.111.0','helpful','slum population figure','high')],
'12.1':[('geo-region-continental-s1.106.0','helpful','Dharavi as Mumbai slum','high')],
'12.2':[('geo-region-continental-s1.111.2','helpful','inadequate water and sanitation','low')],
'12.3':[('geo-region-continental-s1.113.5','helpful','out-migration of young men','high')],
'12.5':[('geo-region-continental-s1.89.3','helpful','India largest remittance recipient','high')],
'12.6':[('geo-region-continental-s1.89.1','helpful','COVID lockdown migrant return','high')],
'13.0':[('geo-region-continental-s2.7.b','helpful','sertão drought-prone interior','high')],
'13.3':[('geo-region-continental-s2.28.3','helpful','favelas on steep hillsides','low')],
'13.5':[('geo-region-continental-s2.12.1','helpful','drought drives sertão out-migration','high')],
}
txt=open(P+'packs/geo-population-migration-s6.t1g4.txt').read()
tg=txt.split('CANDIDATES')[0]
ids=re.findall(r'^\[(geo-population-migration-s6\.[^\]]+)\]',tg,re.M)
allids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
out={};n=lo=0
for i in ids:
    k=i[len(p):]
    # k like '11.0' or '11.b'
    nl=[{'id':a,'strength':s,'why':w,'confidence':c} for a,s,w,c in L.get(k,[])]
    for x in nl: assert x['id'] in allids
    n+=len(nl);lo+=sum(x['confidence']=='low' for x in nl)
    out[i]={'needs':nl}
assert set(L)<= {i[len(p):] for i in ids}
json.dump(out,open(P+'point-links/geo-population-migration-s6.t1g4.json','w'),indent=1)
print(len(out),n,lo)
