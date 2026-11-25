import json,re
P='/Users/gabrielwhelan/barebones/drafts/crunch/geography/'
IDS="0.b 0.0 0.1 0.2 0.3 0.4 0.5 1.b 1.0 1.1 1.2 1.3 1.4 1.5 1.6 2.b 2.0 2.1 2.2 2.3 2.4 2.5 2.6 2.7 3.b 3.0 3.1 3.2 3.3 3.4 3.5 4.b 4.0 4.1 4.2 4.3 4.4 4.5 5.b 5.0 5.1 5.2 6.b 6.0 6.1 6.2 6.3 7.b 7.0 7.1 7.2 8.b 8.0 8.1 8.2 9.b 9.0 9.1 9.2 9.3 10.b 10.0 10.1 10.2 10.3 11.b 11.0 11.1 11.2 11.3 12.b 12.0 12.1 12.2 12.3 13.b 13.0 13.1 13.2 13.3 13.4 13.5".split()
COST2={'2.6','2.7','3.2','10.0','12.1'}
def L(i,s,w,c='high'): return {"id":i,"strength":s,"why":w,"confidence":c}
S='geo-urban-s8.'
L1={
'2.5':[L('geo-urban-s5.4.2','helpful','charge to enter a zone','low')],
'2.6':[L('geo-urban-s5.4.4','helpful','homes close to jobs','low')],
'3.3':[L(S+'3.b','helpful','defines adaptation')],
'3.4':[L(S+'3.b','helpful','defines mitigation')],
'4.1':[L(S+'4.0','helpful','compact growth policy')],
'4.2':[L(S+'4.1','helpful','NPF defined here')],
'12.0':[L(S+'0.2','helpful','90% of urban increase in Asia, Africa')],
'13.2':[L(S+'2.1','helpful','MetroLink')],
'13.4':[L(S+'1.2','essential','Housing for All targets'),L(S+'3.2','essential','emissions targets')],
'13.5':[L(S+'11.1','essential','data centres electricity demand')],
}
L2={
'1.6':[L('geo-urban-s7.2.0','helpful','slums and informal settlements')],
'5.b':[L('geo-population-migration-s1.30.b','helpful','old-age dependency ratio')],
'5.0':[L('geo-population-migration-s1.30.4','helpful','housing and transport needs of older people','low')],
'5.2':[L('geo-population-migration-s1.30.2','helpful','smaller tax base')],
'11.2':[L('geo-urban-s7.36.1','helpful','Cantareira drought, rationing')],
'12.1':[L('geo-urban-s7.16.0','helpful','Kolkata low-lying delta site'),L('geo-urban-s7.25.2','helpful','Mumbai 2005 rainfall flood')],
'12.2':[L('geo-urban-s7.4.b','helpful','informal sector'),L('geo-urban-s7.3.b','helpful','sanitation and slum health')],
'12.3':[L('geo-urban-s7.14.0','helpful','Curitiba bus rapid transit')],
}
L3={
'2.5':[L('geo-economic-environment-s3.24.0','helpful','traffic air pollution')],
'3.b':[L('geo-economic-environment-s3.5.b','helpful','climate change effects on places')],
'3.0':[L('geo-economic-environment-s3.5.1','helpful','more intense heatwaves','low')],
'3.1':[L('geo-economic-environment-s3.5.0','helpful','sea-level rise threatens low land','low')],
}
def w(name,d,cost):
    out={}
    for i in IDS:
        e={}
        if cost: e['cost']=2 if i in COST2 else 1
        e['needs']=d.get(i,[])
        out[S+i]=e
    json.dump(out,open(P+'point-links/'+name+'.json','w'),indent=1)
w('geo-urban-s8.t1g1',L1,True);w('geo-urban-s8.t1g2',L2,False);w('geo-urban-s8.t1g3',L3,False)
for n in ['t1g1','t1g2','t1g3']:
    d=json.load(open(P+'point-links/geo-urban-s8.'+n+'.json'))
    pack=open(P+'packs/geo-urban-s8.'+n+'.txt').read()
    pk=set(re.findall(r'^\[([^\]]+)\]',pack,re.M))
    tgt=[x for x in re.findall(r'^\[(geo-urban-s8\.[^\]]+)\]',pack,re.M)]
    assert set(tgt)==set(d) and len(tgt)==len(set(tgt)), n
    nl=[x for v in d.values() for x in v['needs']]
    assert all(x['id'] in pk for x in nl)
    print(n,len(d),len(nl),sum(v.get('cost')==2 for v in d.values()),sum(x['confidence']=='low' for x in nl))
