import json,re
P='geo-option-atmosphere-ocean-s6'
cnt=[3,7,7,4,2,5,4,4,3,6,6,2,5,4,5,4,6,6,4,6,4,4,3,7,2,4,5,4,4,4]
ids=[]
for n,c in enumerate(cnt):
    ids.append(f'{P}.{n}.b'); ids+= [f'{P}.{n}.{k}' for k in range(c)]
def L(i,s,w,c): return {"id":i,"strength":s,"why":w,"confidence":c}
C='geo-region-continental-s1.'
links={
 'g4':{
  '5.0':[L(C+'2.0','helpful','monsoon as seasonal wind reversal','high')],
  '5.1':[L(C+'38.3','helpful','kharif and rabi crops','high'),L(C+'6.3','helpful','western disturbances give winter rain','high')],
  '5.2':[L(C+'8.0','helpful','late or weak monsoon causes drought','high')],
  '5.3':[L(C+'15.1','helpful','salinisation and waterlogging from canals','high')],
  '5.4':[L(C+'10.3','helpful','Indira Gandhi Canal waters the Thar','high')],
  '6.2':[L(C+'33.0','helpful','multipurpose dams: irrigation, hydroelectricity','low')],
  '9.3':[L(C+'9.1','helpful','monsoon refills reservoirs and groundwater','low')],
  '13.3':[L(C+'3.1','helpful','ITCZ shifting north over India','high')],
 },
 'g5':{
  '5.2':[L(C+'40.0','helpful','monsoon unreliable: drought and floods','high')],
  '5.3':[L(C+'41.2','helpful','irrigation essential to Green Revolution','high'),L(C+'42.4','helpful','Green Revolution core areas','high')],
  '5.4':[L(C+'41.0','helpful','Indira Gandhi Canal brings river water','high')],
 },
 'g6':{
  '14.2':[L(C+'89.b','helpful','migration defined','low')],
  '19.3':[L(C+'89.b','helpful','migration defined','low')],
 }}
for g,suf in (('g4','t1g4'),('g5','t1g5'),('g6','t1g6')):
    pk=open(f'packs/{P}.{suf}.txt').read()
    t=pk.split('CANDIDATES')[0]
    cands=set(re.findall(r'^\[([^\]]+)\]',pk,re.M))
    assert [x for x in re.findall(r'^\[([^\]]+)\]',t,re.M)]==ids
    out={}
    for i in ids:
        k=i[len(P)+1:]
        out[i]={"needs":links[g].get(k,[])}
        for l in out[i]["needs"]: assert l['id'] in cands,(g,l['id'])
    json.dump(out,open(f'point-links/{P}.{suf}.json','w'),indent=1)
    n=[l for v in out.values() for l in v['needs']]
    print(g,len(out),len(n),sum(l['confidence']=='low' for l in n))
