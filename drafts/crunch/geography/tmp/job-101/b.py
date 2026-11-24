import json,re
P='/Users/gabrielwhelan/barebones/drafts/crunch/geography/'
def L(i,s,w,c='high'): return {"id":i,"strength":s,"why":w,"confidence":c}
E='geo-economic-activities-s2.';U='geo-urban-s7.';M='geo-population-migration-s6.'
links={
'g4':{},
'g5':{
'89.0':[L(U+'1.2','helpful','pull factors draw migrants to cities')],
'106.0':[L(U+'2.0','helpful','slums and informal settlements')],
'106.4':[L(U+'12.0','helpful','new towns relieve crowded core')],
'110.0':[L(U+'12.0','helpful','planned new towns','low')],
'110.2':[L(U+'13.0','helpful','metros as public transport')],
'111.0':[L(U+'2.0','helpful','slums defined')],
'111.1':[L(U+'4.b','helpful','informal sector work')],
'111.2':[L(U+'3.0','helpful','sanitation and water services lacking')],
'111.3':[L(U+'6.0','helpful','air pollution sources','low')],
'113.1':[L(U+'4.2','helpful','underemployment defined')],
'114.1':[L(U+'4.2','helpful','underemployment','low')],
'106.2':[L(U+'7.0','helpful','monsoon floods low-lying city','low')],
'117.1':[L(E+'2.0','helpful','raw materials pull industry','low')],
},
'g6':{
'89.0':[L(M+'2.b','helpful','pull factors of cities')],
'103.b':[L(M+'0.0','helpful','urbanisation defined')],
'103.0':[L(M+'0.0','helpful','urbanisation share','low')],
'113.0':[L(M+'1.2','helpful','small holdings push people','low')],
'113.5':[L(M+'12.3','helpful','donor impacts of out-migration','low')],
'106.0':[L(M+'12.1','helpful','Dharavi slum detail','low')],
'111.0':[L(M+'12.0','helpful','slum figures','low')],
},
}
txt=open(P+'packs/geo-region-continental-s1.t4g4.txt').read()
ids=re.findall(r'^\[(geo-region-continental-s1\.([\d.b]+))\]',txt.split('CANDIDATES')[0],re.M)
for k,n in (('g4','t4g4'),('g5','t4g5'),('g6','t4g6')):
    pk=open(P+f'packs/geo-region-continental-s1.{n}.txt').read()
    allids=set(re.findall(r'^\[([^\]]+)\]',pk,re.M))
    out={i:{"needs":links[k].get(s,[])} for i,s in ids}
    for v in out.values():
        for l in v['needs']: assert l['id'] in allids,l
    json.dump(out,open(P+f'point-links/geo-region-continental-s1.{n}.json','w'),indent=1)
    print(n,len(out),sum(len(v['needs']) for v in out.values()),sum(l['confidence']=='low' for v in out.values() for l in v['needs']))
