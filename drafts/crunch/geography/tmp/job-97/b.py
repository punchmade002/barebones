import json,re
P='/Users/gabrielwhelan/barebones/drafts/crunch/geography/'
def n(i,s,w,c): return {"id":i,"strength":s,"why":w,"confidence":c}
pk={
 't2g4':{},
 't2g5':{
  'geo-region-continental-s1.30.2':[n('geo-rivers-s4.2.2','helpful','delta built of deposited sediment','low')],
  'geo-region-continental-s1.33.0':[n('geo-rivers-s4.1.0','helpful','dam stores water, turbines make power','high')],
  'geo-region-continental-s1.53.0':[n('geo-rivers-s4.1.1','helpful','head: drop in height gives power','low')],
  'geo-region-continental-s1.54.2':[n('geo-economic-activities-s2.2.0','helpful','raw material and port location','high')],
  'geo-region-continental-s1.54.3':[n('geo-economic-activities-s2.2.0','helpful','siting near raw materials','high')],
  'geo-region-continental-s1.58.b':[n('geo-economic-activities-s2.2.0','helpful','raw materials as location factor','low')],
 },
 't2g6':{
  'geo-region-continental-s1.36.2':[n('geo-population-migration-s6.2.0','helpful','jobs in industry and services pull','low')],
  'geo-region-continental-s1.44.1':[n('geo-population-migration-s6.1.2','helpful','subdivided holdings','low')],
  'geo-region-continental-s1.54.1':[n('geo-urban-s7.23.1','helpful','Mumbai cotton mills','low')],
  'geo-region-continental-s1.54.2':[n('geo-urban-s7.16.2','helpful','Kolkata jute mills on Hooghly','low')],
 }}
for k,L in pk.items():
    txt=open(P+f'packs/geo-region-continental-s1.{k}.txt').read()
    tg=txt.split('\nCANDIDATES')[0]
    ids=re.findall(r'^\[([^\]]+)\]',tg,re.M)
    allids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
    out={i:{"needs":L.get(i,[])} for i in ids}
    assert set(L)<=set(ids)
    for v in out.values():
        for x in v['needs']: assert x['id'] in allids
    json.dump(out,open(P+f'point-links/geo-region-continental-s1.{k}.json','w'),indent=1)
    print(k,len(ids),sum(len(v['needs']) for v in out.values()),sum(x['confidence']=='low' for v in out.values() for x in v['needs']))
