import json,re
P='/Users/gabrielwhelan/barebones/drafts/crunch/geography/'
S='geo-option-global-interdependence-s4.'
ids=[S+x for x in """20.4 20.5 21.b 21.0 21.1 21.2 21.3 21.4 22.b 22.0 22.1 22.2 22.3 22.4 22.5 22.6 22.7
23.b 23.0 23.1 23.2 23.3 23.4 24.b 24.0 24.1 24.2 24.3 24.4 24.5 24.6 24.7 25.b 25.0 26.b 26.0 26.1
27.b 27.0 27.1 27.2 28.b 28.0 28.1 28.2 28.3 28.4 29.b 29.0 29.1 30.b 30.0 30.1 30.2 30.3 30.4 30.5 30.6 30.7
31.b 31.0 31.1 31.2 31.3 32.b 32.0 32.1 32.2 32.3 32.4 32.5 33.b 33.0 33.1 34.b 34.0 34.1
35.b 35.0 35.1 35.2 35.3 35.4 35.5 35.6 35.7 35.8 36.b 36.0 37.b 37.0 37.1 37.2
38.b 38.0 38.1 38.2 38.3 38.4 39.b 39.0 40.b 40.0 40.1 40.2 40.3 41.b 41.0 41.1 41.2""".split()]
C='geo-region-continental-s2.'
def L(i,s,w,c='high'): return {"id":C+i,"strength":s,"why":w,"confidence":c}
g4={'28.0':[L('98.3','helpful','mining ranching dams threaten indigenous lands')],
 '28.2':[L('55.2','helpful','illegal gold mining mercury in Yanomami land')],
 '28.3':[L('98.3','helpful','Kayapó opposed Belo Monte dam')],
 '28.4':[L('98.2','helpful','demarcated indigenous lands cover Amazon forest')],
 '29.1':[L('51.2','helpful','extractive reserves harvest forest without clearing')]}
for name,links in (('t2g4',g4),('t2g5',{})):
    out={i:{"needs":links.get(i[len(S):],[])} for i in ids}
    path=P+'point-links/geo-option-global-interdependence-s4.%s.json'%name
    json.dump(out,open(path,'w'),indent=1,ensure_ascii=False)
    txt=open(P+'packs/geo-option-global-interdependence-s4.%s.txt'%name).read()
    tg=[m for m in re.findall(r'^\[(geo-option-global-interdependence-s4\.[^\]]+)\]',txt,re.M)]
    allids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
    d=json.load(open(path))
    assert sorted(d)==sorted(tg) and len(tg)==len(set(tg)),(set(tg)^set(d))
    assert all(n['id'] in allids for v in d.values() for n in v['needs'])
    print(name,len(d),sum(len(v['needs']) for v in d.values()),0)
