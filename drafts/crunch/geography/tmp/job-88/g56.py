import json,re,sys
P='/Users/gabrielwhelan/barebones/drafts/crunch/geography/'
p='geo-population-migration-s6.'
S={
't1g5':{
'13.b':[('geo-region-continental-s2.109.b','helpful','Brazil rural to urban shift','high')],
'13.0':[('geo-region-continental-s2.94.0','helpful','nordestinos moving to São Paulo, Rio','high')],
'13.1':[('geo-region-continental-s2.109.0','helpful','urban share 36% to 87%','high')],
'13.2':[('geo-region-continental-s2.110.0','helpful','São Paulo and Rio as megacities','high')],
'13.3':[('geo-region-continental-s2.113.0','helpful','favela spread in São Paulo','high')],
'13.4':[('geo-region-continental-s2.118.1','helpful','informal economy in cities','high')],
'13.5':[('geo-region-continental-s2.94.b','helpful','Northeast to Southeast internal migration','high')],
},
't1g6':{
'1.3':[('geo-region-continental-s2.119.3','helpful','poor rural services make young leave','high')],
'13.0':[('geo-region-continental-s2.124.0','helpful','drought-hit sertão migrants to São Paulo','high')],
}}
for t,L in S.items():
    txt=open(P+f'packs/geo-population-migration-s6.{t}.txt').read()
    ids=re.findall(r'^\[(geo-population-migration-s6\.[^\]]+)\]',txt.split('CANDIDATES')[0],re.M)
    allids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
    assert set(L)<={i[len(p):] for i in ids}
    out={};n=lo=0
    for i in ids:
        nl=[{'id':a,'strength':s,'why':w,'confidence':c} for a,s,w,c in L.get(i[len(p):],[])]
        for x in nl: assert x['id'] in allids
        n+=len(nl);lo+=sum(x['confidence']=='low' for x in nl);out[i]={'needs':nl}
    json.dump(out,open(P+f'point-links/geo-population-migration-s6.{t}.json','w'),indent=1)
    json.load(open(P+f'point-links/geo-population-migration-s6.{t}.json'))
    print(t,len(out),n,lo)
