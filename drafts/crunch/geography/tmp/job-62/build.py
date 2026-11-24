import json,re
P='/Users/gabrielwhelan/barebones/drafts/crunch/geography/'
S='geo-option-geoecology-s4.'
def L(i,s,w,c): return {"id":i,"strength":s,"why":w,"confidence":c}
S1='geo-option-geoecology-s1.'; R6='geo-rocks-weathering-s6.'; G='geo-graph-skills-s1.'
A={
'5.1':[L(R6+'5.1','helpful','erg, reg, hamada landscapes','high')],
'5.3':[L(R6+'0.b','helpful','wind erosion processes','high')],
'6.1':[L(S1+'6.1','helpful','humus defined','high')],
'6.2':[L(S1+'9.1','helpful','capillary rise brings salts up','high')],
'6.3':[L(S1+'9.1','helpful','salts and lime left at surface','high')],
'6.4':[L(R6+'3.2','essential','desert pavement formation','high')],
'6.5':[L(S1+'19.2','helpful','alkaline soils in dry climates','high')],
'6.6':[L(S1+'0.3','helpful','alluvium as river deposit','high')],
'6.7':[L(S1+'18.0','helpful','organic content low in desert soils','low')],
'9.6':[L(S1+'9.1','helpful','salts rise to surface','low')],
'20.0':[L(S1+'18.1','helpful','latosols low in humus','high')],
'20.1':[L(S1+'6.1','helpful','litter and decomposers','high')],
'20.4':[L(S1+'20.2','helpful','leached soils infertile','low')],
}
B={
'15.b':[L(G+'13.b','helpful','climate graph construction','high')],
'15.0':[L(G+'13.3','essential','annual range calculation','high')],
'15.1':[L(G+'13.3','essential','total rainfall from bars','high')],
'15.2':[L(G+'13.2','essential','reading seasonal pattern','high')],
'30.b':[L(G+'13.b','helpful','climate graph construction','high')],
'30.0':[L(G+'13.3','essential','annual range calculation','high')],
'30.1':[L(G+'13.3','essential','total rainfall from bars','high')],
'30.2':[L(G+'13.2','essential','reading seasonal pattern','high')],
}
for name,links in (('geo-option-geoecology-s4.t1g4',A),('geo-option-geoecology-s4.t1g5',B)):
    txt=open(P+'packs/'+name+'.txt').read()
    tgt=txt.split('CANDIDATES')[0]
    ids=re.findall(r'^\[(geo-option-geoecology-s4\.[^\]]+)\]',tgt,re.M)
    allids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
    out={}
    for i in ids:
        k=i[len(S):]
        out[i]={"needs":links.get(k,[])}  # every id reviewed above; none-link items judged empty
    for k in links: assert S+k in out,k
    for v in out.values():
        for n in v['needs']: assert n['id'] in allids,n
    json.dump(out,open(P+'point-links/'+name+'.json','w'),indent=1)
    j=json.load(open(P+'point-links/'+name+'.json'))
    print(name,len(j),sum(len(v['needs']) for v in j.values()),sum(n['confidence']=='low' for v in j.values() for n in v['needs']))
