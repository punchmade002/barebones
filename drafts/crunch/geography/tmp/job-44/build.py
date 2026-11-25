import json,re
P='/Users/gabrielwhelan/barebones/drafts/crunch/geography/'
S5='geo-option-atmosphere-ocean-s5.'
def L(i,s,w,c='high'): return {"id":i,"strength":s,"why":w,"confidence":c}
# explicit cost for every target (suffix -> cost)
cost={}
for k in "18.2 18.3 18.4 18.5 19.b 19.1 19.2 19.4 19.5 20.b 20.0 21.b 21.1 21.2 21.3 21.4 21.5 22.b 22.0 22.1 22.2 22.3 22.4 23.b 23.1 23.2 23.3 23.4 23.5 24.b 24.2 24.4 24.5 24.6 25.b 25.0 25.1 25.2 25.3 25.4 25.5 25.6 26.b 26.0 26.1 26.2 26.3 26.4 26.5 26.6 27.b 27.1 27.2 27.3 27.4 27.5 28.b 28.0 28.1 28.2 28.3 28.4 28.5 29.b 29.0 29.1 29.2 30.b 30.2 30.3 31.b 31.0 31.2 31.3 31.4 32.b 32.0 32.1 32.2 32.3 32.4 32.5 32.6 33.b 33.0 33.1 33.2 33.3 34.b 34.0 34.1 34.2 35.b 35.0 35.1 35.2".split(): cost[k]=1
for k in "19.0 19.3 19.6 21.0 23.0 24.0 24.1 24.3 27.0 30.0 30.1 31.1".split(): cost[k]=2
ids=re.findall(r'^\[(geo-option-atmosphere-ocean-s5\.[\w.]+)\]',open(P+'packs/geo-option-atmosphere-ocean-s5.t2g1.txt').read().split('CANDIDATES')[0],re.M)
assert set(i[len(S5):] for i in ids)==set(cost),(set(i[len(S5):] for i in ids)^set(cost))
s2='geo-option-atmosphere-ocean-s2.';s4='geo-option-atmosphere-ocean-s4.';s3='geo-option-atmosphere-ocean-s3.';g='geo-glaciation-s1.'
l1={ "18.2":[L(s2+"13.1","helpful","cold currents cool coasts"),L(s2+"13.0","helpful","North Atlantic Drift warms")],
"18.3":[L(s2+"14.0","helpful","temperature falls with height")],
"18.4":[L(S5+"6.1","helpful","Deccan rain shadow")],
"18.5":[L(S5+"1.4","helpful","ITCZ movement")],
"19.1":[L(S5+"24.0","helpful","Milankovitch cycles explained there")],
"19.4":[L(s2+"19.0","helpful","oceans redistribute heat")],
"19.5":[L(s2+"19.0","helpful","currents carry heat")],
"19.6":[L(s2+"3.0","essential","albedo")],
"20.0":[L(s2+"5.0","helpful","greenhouse effect")],
"21.4":[L(S5+"23.1","helpful","glacial landforms listed")],
"22.1":[L(S5+"22.0","helpful","glacial and interglacial")],
"22.2":[L(S5+"22.0","helpful","glacial period")],
"22.4":[L(S5+"0.2","helpful","climate belts by latitude","low")],
"23.4":[L(S5+"23.3","helpful","loess and dry climates")],
"24.0":[L(s2+"9.0","helpful","earth's tilt and seasons","low")],
"24.1":[L(S5+"24.0","essential","Milankovitch cycles")],
"24.2":[L(S5+"24.0","helpful","orbital change effect")],
"24.3":[L(s2+"3.0","essential","albedo")],
"24.4":[L(S5+"21.0","helpful","ice core records")],
"24.5":[L(s2+"19.0","helpful","ocean heat transport")],
"25.6":[L(S5+"19.3","helpful","volcanic cooling")],
"27.0":[L(s2+"5.0","essential","greenhouse effect")],
"27.1":[L(S5+"27.0","helpful","extra heat trapped")],
"27.2":[L(s2+"3.1","essential","albedo of ice and ocean")],
"27.3":[L(S5+"27.0","helpful","greenhouse gas warming")],
"27.4":[L(S5+"19.6","helpful","permafrost feedback")],
"28.2":[L(S5+"0.2","helpful","climate belts","low")],
"28.3":[L(s2+"24.0","helpful","thermohaline circulation")],
"28.4":[L(s2+"22.1","helpful","tropical cyclones draw heat")],
"28.5":[L(S5+"27.1","helpful","warming sea expands")],
"30.1":[L(S5+"30.0","essential","warm pool and trade winds")],
"31.0":[L(S5+"30.0","essential","normal trade winds")],
"31.1":[L(S5+"30.1","essential","normal Walker circulation")],
"32.0":[L(S5+"31.1","essential","rain zone shifts east")],
"32.1":[L(S5+"30.2","essential","upwelling and anchoveta")],
"32.2":[L(S5+"31.1","helpful","rain zone shifts east")],
"32.3":[L(S5+"5.0","helpful","Indian monsoon","low")],
"34.1":[L(S5+"32.0","helpful","El Nino effects reversed","low")],
"34.0":[L(S5+"30.0","helpful","normal trade winds")],
"34.b":[L(S5+"31.b","helpful","El Nino reversed")],
}
l2={"18.2":[L(s4+"13.1","helpful","cold eastern-boundary currents")],
"18.5":[L(s4+"6.3","helpful","ITCZ shift and Sahel")],
"19.5":[L(s4+"15.b","helpful","ocean circulation","low")],
"24.5":[L(s4+"15.4","helpful","AMOC carries heat north")],
"28.2":[L(s4+"3.1","helpful","subtropical highs and dry zones","low")],
"28.3":[L(s4+"16.0","helpful","why AMOC may weaken")],
"28.4":[L(s4+"38.0","helpful","cyclones need warm sea")],
"30.0":[L(s4+"2.0","helpful","wind drag moves surface water")],
"30.1":[L(s4+"5.b","helpful","circulation cells","low")],
"30.2":[L(s4+"14.0","essential","upwelling of cold water")],
"31.0":[L(s4+"4.0","helpful","trade winds")],
"31.1":[L(s4+"14.0","helpful","upwelling")],
"32.1":[L(s4+"14.2","essential","Peruvian anchoveta fishery")],
"32.3":[L(s4+"6.3","helpful","monsoon seasonal shift","low")],
"32.4":[L(s4+"38.b","helpful","cyclone formation","low")],
"33.0":[L(s4+"14.2","helpful","anchoveta fishery")],
"34.0":[L(s4+"14.0","helpful","upwelling")],
}
l3={"18.2":[L(s3+"32.3","helpful","ocean currents and rainfall","low")],
"18.4":[L(s3+"28.b","helpful","relief rain and rain shadow")],
"18.5":[L(s3+"35.0","helpful","Sahel rainfall")],
"21.4":[L(g+"0.b","helpful","glacial landforms","low")],
"23.0":[L(g+"0.0","helpful","Munsterian and Midlandian")],
"23.1":[L(g+"17.b","helpful","drumlins"),L(g+"20.b","helpful","eskers"),L(g+"7.b","helpful","corries"),L(g+"9.b","helpful","U-shaped valleys")],
"23.4":[L(g+"21.b","helpful","outwash plains")],
"25.2":[L(g+"4.0","helpful","glacier advance","low")],
"26.5":[L(g+"4.1","helpful","glacier retreat")],
"27.3":[L(s3+"6.2","helpful","warm air holds more vapour")],
"28.0":[L(s3+"0.b","helpful","hydrological cycle")],
"30.1":[L(s3+"27.b","helpful","convectional rain","low")],
}
def out(fn,mode,links):
    d={}
    for i in ids:
        k=i[len(S5):]; n=[x for x in links.get(k,[])]
        d[i]={"cost":cost[k],"needs":n} if mode else {"needs":n}
    pk=open(P+'packs/'+fn+'.txt').read()
    for v in d.values():
        for n in v["needs"]:
            assert '['+n["id"]+']' in pk,n["id"]
            assert n["id"]!=i
    json.dump(d,open(P+'point-links/'+fn+'.json','w'),indent=1)
    d=json.load(open(P+'point-links/'+fn+'.json'))
    assert list(d)==ids
    nl=sum(len(v["needs"]) for v in d.values())
    lo=sum(n["confidence"]=="low" for v in d.values() for n in v["needs"])
    print(fn,len(d),nl,sum(v.get("cost")==2 for v in d.values()),lo)
out('geo-option-atmosphere-ocean-s5.t2g1',1,l1)
out('geo-option-atmosphere-ocean-s5.t2g2',0,l2)
out('geo-option-atmosphere-ocean-s5.t2g3',0,l3)
