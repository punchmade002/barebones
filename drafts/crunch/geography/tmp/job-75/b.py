import re,json
P='/Users/gabrielwhelan/barebones/drafts/crunch/geography/'
# every target judged: only link is s4.15.1 in package 1; all others explicitly empty
links={('geo-option-global-interdependence-s4.t1g4','geo-option-global-interdependence-s4.15.1'):[{"id":"geo-region-continental-s2.43.2","strength":"helpful","why":"cattle ranching as cause of Amazon clearance","confidence":"low"}]}
for n in ('t1g4','t1g5'):
    txt=open(P+'packs/geo-option-global-interdependence-s4.%s.txt'%n).read()
    tg,cand=txt.split('CANDIDATES',1)
    tids=re.findall(r'^\[(\S+?)\]',tg,re.M); cids=set(re.findall(r'^\[(\S+?)\]',cand,re.M))
    out={}
    for t in tids:
        out[t]={"needs":links.get(('geo-option-global-interdependence-s4.t1g4',t),[]) if n=='t1g4' else []}
    for v in out.values():
        for l in v['needs']: assert l['id'] in cids|set(tids)
    json.dump(out,open(P+'point-links/geo-option-global-interdependence-s4.%s.json'%n,'w'),ensure_ascii=False)
    print(n,len(out),sum(len(v['needs']) for v in out.values()))
