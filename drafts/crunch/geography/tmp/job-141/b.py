import re,json,sys
P='/Users/gabrielwhelan/barebones/drafts/crunch/geography/'
def L(i,s,w,c='high'): return {"id":i,"strength":s,"why":w,"confidence":c}
links={
 't1g4':{'geo-urban-s7.17.2':[L('geo-region-continental-s1.99.0','helpful','uses 1947 Partition of British India')],
         'geo-urban-s7.19.0':[L('geo-region-continental-s1.99.0','helpful','uses Partition, East Pakistan')],
         'geo-urban-s7.20.1':[L('geo-region-continental-s1.39.1','helpful','uses monsoon as seasonal rain','low')]},
 't1g5':{'geo-urban-s7.31.0':[L('geo-region-continental-s2.23.1','helpful','São Paulo plateau, Santos port')],
         'geo-urban-s7.32.4':[L('geo-region-continental-s2.12.1','helpful','drought drives migration from the sertão','low')]},
 't1g6':{'geo-urban-s7.32.0':[L('geo-region-continental-s2.40.0','helpful','São Paulo coffee boom via Santos')],
         'geo-urban-s7.32.3':[L('geo-region-continental-s2.60.2','helpful','ABC region car makers, Volkswagen')]},
}
for k,d in links.items():
    txt=open(P+'packs/geo-urban-s7.%s.txt'%k).read()
    tgt=txt.split('CANDIDATES')[0]
    ids=re.findall(r'^\[(\S+?)\]',tgt,re.M)
    allids=set(re.findall(r'^\[(\S+?)\]',txt,re.M))
    out={i:{"needs":d.get(i,[])} for i in ids}
    assert all(n['id'] in allids for v in out.values() for n in v['needs'])
    json.dump(out,open(P+'point-links/geo-urban-s7.%s.json'%k,'w'),ensure_ascii=False)
    print(k,len(ids),sum(len(v['needs']) for v in out.values()),sum(n['confidence']=='low' for v in out.values() for n in v['needs']))
