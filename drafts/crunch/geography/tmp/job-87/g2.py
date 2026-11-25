import json,re,sys
P='/Users/gabrielwhelan/barebones/drafts/crunch/geography/'
pk=sys.argv[1]
exec(open(P+'tmp/job-87/'+pk+'_links.py').read())
txt=open(P+'packs/geo-population-migration-s6.'+pk+'.txt').read()
tgt=re.findall(r'^\[(geo-population-migration-s6\.[^\]]+)\]',txt,re.M)
allids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
for k in links: assert k in tgt,k
out={}
for k in tgt:
  ns=[{"id":i,"strength":s,"why":w,"confidence":c} for i,s,w,c in links.get(k[len('geo-population-migration-s6.'):] and k,[])]
  for x in ns: assert x['id'] in allids and x['id']!=k
  out[k]={"needs":ns}
json.dump(out,open(P+'point-links/geo-population-migration-s6.'+pk+'.json','w'),indent=1)
print(len(out),sum(len(v['needs']) for v in out.values()),sum(x['confidence']=='low' for v in out.values() for x in v['needs']))
