import json,re
P='/Users/gabrielwhelan/barebones/drafts/crunch/geography/'
mx=[4,3,4,5,5,2,3,4,3,2,3,4,3,3,3,3,2,3,4,3,4,2,2,3,2,3,3,2,3,3,2]
ids=[]
for g,m in enumerate(mx):
    ids+= [f'geo-region-continental-s2.{g}.b']+[f'geo-region-continental-s2.{g}.{i}' for i in range(m+1)]
def L(i,s,w,c='high'): return {"id":i,"strength":s,"why":w,"confidence":c}
p='geo-region-continental-s2.'
a={p+'23.1':[L('geo-economic-activities-s2.3.1','helpful','port as transport link','low')]}
b={p+'12.1':[L('geo-population-migration-s6.13.0','helpful','sertão drought migration to cities')],
   p+'28.3':[L('geo-urban-s7.2.0','helpful','favelas as informal settlements')],
   p+'23.1':[L('geo-urban-s7.31.0','helpful','São Paulo inland from Santos','low')],
   p+'2.1':[L('geo-population-migration-s6.13.0','helpful','sertão term','low')]}
for name,d in (('t1g4',a),('t1g5',b)):
    out={i:{"needs":d.get(i,[])} for i in ids}
    json.dump(out,open(P+f'point-links/geo-region-continental-s2.{name}.json','w'),ensure_ascii=False)
    pk=open(P+f'packs/geo-region-continental-s2.{name}.txt').read()
    tg=re.findall(r'^\[(geo-region-continental-s2\.[^\]]+)\]',pk,re.M)
    assert tg==ids,(len(tg),len(ids))
    cand=set(re.findall(r'^\[([^\]]+)\]',pk,re.M))
    n=[x for v in out.values() for x in v['needs']]
    assert all(x['id'] in cand for x in n)
    print(name,len(ids),len(n),sum(x['confidence']=='low' for x in n))
