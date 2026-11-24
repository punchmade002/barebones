import json,re
P='/Users/gabrielwhelan/barebones/drafts/crunch/geography/'
L=lambda i,s,w,c:{"id":i,"strength":s,"why":w,"confidence":c}
# every target judged; only these have links, all others judged as no links
links={
 'geo-option-global-interdependence-s3.t2g4':{
  'geo-option-global-interdependence-s3.34.0':[L('geo-region-continental-s2.10.2','helpful','locates Porto Alegre in Brazil','low')]},
 'geo-option-global-interdependence-s3.t2g5':{
  'geo-option-global-interdependence-s3.24.0':[L('geo-region-continental-s2.47.0','helpful','latifundia and minifundia in Brazil','high')]},
 'geo-option-global-interdependence-s3.t2g6':{
  'geo-option-global-interdependence-s3.24.1':[L('geo-region-continental-s2.120.0','helpful','MST land occupation campaign','high')],
  'geo-option-global-interdependence-s3.39.4':[L('geo-region-continental-s2.118.1','helpful','informal economy meaning','low')],
  'geo-option-global-interdependence-s3.44.2':[L('geo-region-continental-s2.118.1','helpful','informal jobs meaning','low')]},
}
for name,lk in links.items():
    txt=open(P+'packs/'+name.replace('geo-option-global-interdependence-s3.','geo-option-global-interdependence-s3.')+'.txt').read()
    tgt=txt.split('CANDIDATES')[0]
    ids=re.findall(r'^\[([^\]]+)\]',tgt,re.M)
    allids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
    out={i:{"needs":lk.get(i,[])} for i in ids}
    assert len(ids)==len(set(ids))
    for v in out.values():
        for n in v['needs']: assert n['id'] in allids
    json.dump(out,open(P+'point-links/'+name+'.json','w'),ensure_ascii=False)
    d=json.load(open(P+'point-links/'+name+'.json'))
    print(name,len(d),sum(len(v['needs']) for v in d.values()),sum(n['confidence']=='low' for v in d.values() for n in v['needs']))
