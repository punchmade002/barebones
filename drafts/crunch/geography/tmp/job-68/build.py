import json,re
P='/Users/gabrielwhelan/barebones/drafts/crunch/geography/'
S='geo-option-global-interdependence-s2.'
def L(i,s,w,c='high'): return {"id":i,"strength":s,"why":w,"confidence":c}
E,H='essential','helpful'
# costs: explicit for every target id
cost={}
def c(k,v):
    for x in k.split(): cost[S+x]=v
c("22.3 22.4 23.b 23.1 23.3 24.b 24.0 24.1 24.3 24.4 25.b 25.0 25.1 25.2 25.3 25.4 25.6 26.b 26.0 26.1 26.2 27.b 27.0 27.3 27.6 28.b 28.0 28.2 28.3 28.4 28.5 29.b 29.0 29.1 29.2 30.b 30.0 30.4 30.7 31.b 31.0 31.1 31.2 31.4 31.6 32.b 32.0 32.3 32.4 33.b 33.1 33.3 33.4 33.5 34.b 34.0 34.1 34.3 35.b 35.0 35.2 35.4 35.5 36.b 36.1 36.5 37.b 37.0 37.1 37.2 38.b 38.0 38.1 38.2 38.3 39.b 39.1 39.3 39.5 39.6 40.b 40.1 40.2 40.3 40.4 41.b 41.1 41.2 41.3 42.b 42.0 42.1 22.2",1)
c("22.5 23.0 23.2 24.2 25.5 26.3 27.1 27.2 27.4 27.5 28.1 28.6 30.1 30.2 30.3 30.5 30.6 31.3 31.5 32.1 32.2 33.0 33.2 34.2 35.1 35.3 35.6 36.0 36.2 36.3 36.4 37.3 39.0 39.2 39.4 40.0 41.0",2)
g1={
"22.2":[L(S+"22.1",E,"sea shrank from river diversion")],
"22.3":[L(S+"22.1",H,"sea shrank, exposing seabed")],
"22.4":[L(S+"22.1",E,"rivers diverted to irrigate cotton")],
"22.5":[L(S+"22.1",H,"sea split and shrank")],
"23.b":[L(S+"20.0",H,"dryland damage definition")],
"23.0":[L(S+"20.0",H,"drylands and land degradation")],
"23.1":[L(S+"23.0",E,"greenhouses in dry Almeria")],
"23.2":[L(S+"20.0",H,"dryland degradation and dust","low")],
"23.3":[L(S+"23.2",E,"the tree-planting scheme")],
"24.0":[L(S+"24.b",E,"greenhouse gases cause warming")],
"24.2":[L(S+"24.b",H,"global warming meaning")],
"24.4":[L(S+"24.0",H,"emissions causing warming")],
"25.0":[L(S+"24.b",H,"warming causes sea-level rise")],
"25.1":[L(S+"25.2",H,"sea-level rise explained")],
"25.2":[L(S+"24.b",E,"warming melts ice")],
"25.3":[L(S+"24.b",H,"air warming")],
"25.4":[L(S+"24.b",H,"warm water from warming","low")],
"25.5":[L(S+"24.b",H,"greenhouse gas emissions")],
"25.6":[L(S+"21.b",H,"Sahel location and climate")],
"26.0":[L(S+"24.0",H,"sources of greenhouse gases")],
"26.2":[L(S+"24.b",H,"extreme weather from warming","low")],
"27.b":[L(S+"24.b",E,"warming problem being solved")],
"27.0":[L(S+"24.b",H,"warming needing co-operation")],
"27.1":[L(S+"27.0",H,"framework for later agreements")],
"27.4":[L(S+"25.0",H,"poor countries emitted least")],
"27.5":[L(S+"27.2",H,"carbon pricing in EU","low")],
"27.6":[L(S+"27.1",H,"1.5 degree goal")],
"28.2":[L(S+"28.1",E,"refugee status definition")],
"28.3":[L(S+"28.1",E,"unlike a refugee")],
"28.6":[L(S+"28.1",E,"political refugee persecution"),L(S+"28.0",E,"economic migrant motive")],
"29.0":[L(S+"28.1",H,"refugees"),L(S+"28.3",H,"internally displaced people")],
"29.1":[L(S+"28.1",H,"refugee definition")],
"29.2":[L(S+"28.1",H,"refugee population","low")],
"30.b":[L(S+"28.6",H,"political refugees","low")],
"30.1":[L(S+"28.3",E,"displaced inside Syria"),L(S+"28.1",H,"refugees abroad")],
"30.2":[L(S+"29.1",H,"refugees stay in neighbours")],
"30.4":[L(S+"28.2",E,"asylum applications")],
"30.5":[L(S+"30.4",H,"asylum numbers in 2015")],
"30.6":[L(S+"30.2",H,"Turkey hosting refugees")],
"30.7":[L(S+"30.0",H,"Assad government and war")],
"31.b":[L(S+"28.4",E,"stateless people")],
"31.1":[L(S+"28.4",E,"stateless definition")],
"31.2":[L(S+"31.0",H,"who the Rohingya are")],
"31.3":[L(S+"31.2",H,"refugees in Bangladesh")],
"31.4":[L(S+"31.3",H,"camps around Cox's Bazar")],
"31.5":[L(S+"31.2",H,"killings of Rohingya","low")],
"31.6":[L(S+"31.2",H,"safe return of refugees")],
"32.1":[L(S+"28.2",E,"asylum decision wait")],
"32.2":[L(S+"32.1",E,"temporary protection directive")],
"32.3":[L(S+"28.1",H,"refugee definition","low")],
"32.4":[L(S+"32.1",H,"Ukrainians' immediate rights"),L(S+"28.2",H,"asylum seekers","low")],
"33.0":[L(S+"28.2",H,"asylum seekers")],
"33.1":[L(S+"28.2",H,"asylum seekers")],
"33.2":[L(S+"33.0",E,"direct provision")],
"33.3":[L(S+"33.0",H,"accommodation for asylum seekers")],
"33.4":[L(S+"33.3",H,"accommodation pressure")],
"33.5":[L(S+"30.b",H,"Syrian crisis","low")],
"34.0":[L(S+"28.0",H,"economic migrants","low")],
"35.0":[L(S+"34.3",E,"EU enlargement 2004")],
"35.1":[L(S+"28.0",H,"economic migrant workers")],
"35.2":[L(S+"35.1",E,"migrant workers in Gulf")],
"35.3":[L(S+"35.2",H,"kafala and worker rights")],
"35.4":[L(S+"34.2",H,"West Africa-Europe corridor")],
"35.5":[L(S+"35.4",H,"Atlantic route migration")],
"35.6":[L(S+"34.2",H,"North Africa-Europe corridor")],
"36.0":[L(S+"1.1".replace("1.1","0.0"),H,"foreign direct investment") if False else L("geo-economic-globalisation-s1.1.b",H,"meaning of FDI")],
"36.1":[L(S+"36.0",E,"remittances")],
"36.5":[L(S+"28.2",H,"asylum system","low")],
"38.0":[L(S+"28.1",H,"persecution and refugees")],
"38.1":[L(S+"28.1",H,"refugee definition")],
"39.0":[L(S+"39.b",H,"supply chain and brands")],
"39.1":[L(S+"39.0",E,"Rana Plaza disaster")],
"39.2":[L(S+"39.b",H,"forced labour in supply chains","low")],
"39.3":[L(S+"39.2",E,"forced labour in Xinjiang")],
"39.4":[L(S+"39.2",E,"Xinjiang forced labour")],
"39.6":[L(S+"3.6",E,"child labour in cobalt mines"),L(S+"35.3",E,"Qatar migrant workers")],
"40.1":[L(S+"40.0",E,"Dunnes strike protest")],
"40.2":[L(S+"40.0",H,"apartheid and strike")],
"40.3":[L(S+"40.0",H,"apartheid","low")],
"40.4":[L(S+"39.b",E,"supply chains")],
"41.0":[L(S+"35.6",E,"Lampedusa shipwreck")],
"41.1":[L(S+"33.0",E,"direct provision")],
"41.3":[L(S+"28.4",E,"stateless people"),L(S+"31.1",H,"Rohingya statelessness")],
"42.0":[L(S+"30.b",H,"Syria case"),L(S+"31.b",H,"Rohingya case"),L(S+"32.b",H,"Ukraine case")],
"42.1":[L(S+"28.5",H,"UNHCR"),L(S+"28.1",H,"UN Refugee Convention")],
}
E3="geo-economic-environment-s3."; T3="geo-economic-globalisation-s3."
g2={
"24.b":[L(E3+"2.1",H,"enhanced greenhouse effect")],
"24.0":[L(E3+"3.0",H,"CO2 sources")],
"24.1":[L(E3+"4.0",H,"CO2 ppm evidence")],
"24.2":[L(E3+"4.1",H,"temperature rise evidence")],
"25.0":[L(E3+"5.0",H,"sea-level rise and deltas")],
"25.1":[L(E3+"5.0",H,"low-lying states threatened")],
"25.2":[L(E3+"4.4",H,"sea level rise figure")],
"25.3":[L(E3+"4.3",H,"Arctic sea ice")],
"25.4":[L(E3+"5.3",H,"coral bleaching")],
"25.5":[L(E3+"5.1","helpful","floods and extreme weather","low")],
"25.6":[L(E3+"5.4",H,"climate refugees","low")],
"26.0":[L(E3+"7.0",H,"Irish emissions shares")],
"26.1":[L(E3+"6.0",H,"Irish temperature rise")],
"26.2":[L(E3+"6.3",H,"Storm Eowyn")],
"26.3":[L(E3+"9.2",H,"Climate Act targets")],
"27.0":[L(E3+"8.0",H,"UNFCCC Rio 1992")],
"27.1":[L(E3+"8.1",H,"Kyoto Protocol"),L(E3+"8.2",H,"Paris Agreement")],
"27.2":[L(E3+"9.0",H,"EU Emissions Trading System"),L(E3+"9.1",H,"European Green Deal")],
"27.3":[L(E3+"8.3",H,"COP meetings")],
"27.5":[L(T3+"4.1",H,"tariffs as trade barriers","low"),L(E3+"9.0",H,"carbon pricing","low")],
"39.b":[L(T3+"6.0",H,"supply chains","low")],
"39.4":[L(T3+"4.1",H,"import bans as trade barriers","low")],
"40.1":[L(T3+"4.1",H,"import bans as trade barriers","low")],
"40.3":[L(T3+"4.1",H,"restricting trade","low")],
}
M="geo-population-migration-s3."; G="geo-option-geoecology-s3."
g3={
"22.3":[L(G+"6.3",H,"salinisation from irrigation","low")],
"22.4":[L(G+"5.3",H,"poorly managed irrigation","low")],
"23.b":[L(G+"5.0",H,"desertification definition","low")],
"23.2":[L(G+"15.3",H,"shelter belts of trees")],
"25.6":[L(G+"8.3",H,"Sahel droughts","low")],
"28.0":[L(M+"0.4",H,"economic migrants")],
"28.1":[L(M+"0.4",H,"refugees flee persecution")],
"28.2":[L(M+"0.4",H,"asylum seekers")],
"28.3":[L(M+"0.2",H,"internal migration")],
"28.6":[L(M+"0.3",H,"voluntary and forced migration")],
"32.2":[L(M+"11.1",H,"Ukrainians in Ireland","low")],
"34.1":[L(M+"0.2",H,"international migration")],
"34.3":[L(M+"9.1",H,"EU enlargement 2004")],
"35.0":[L(M+"9.2",H,"open labour markets 2004")],
"36.0":[L(M+"16.0",H,"remittances")],
"36.2":[L(M+"15.0",H,"brain drain")],
"36.3":[L(M+"17.1",H,"young workers offset ageing")],
"36.4":[L(M+"18.0",H,"pressure on housing and services")],
"37.0":[L(M+"5.0",H,"Famine emigration")],
"37.1":[L(M+"6.4",H,"net emigration")],
"37.2":[L(M+"10.2",H,"2013 emigration peak")],
"37.3":[L(M+"13.0",H,"non-Irish nationals"),L(M+"0.1",H,"net immigration")],
}
ids=[l.split(']')[0][1:] for l in open(P+'packs/geo-option-global-interdependence-s2.t2g1.txt') if l.startswith('['+S)]
tids=[]
for l in open(P+'packs/geo-option-global-interdependence-s2.t2g1.txt'):
    if l.startswith('CANDIDATES'): break
    if l.startswith('['): tids.append(l[1:l.index(']')])
short=lambda i:i[len(S):]
assert set(tids)==set(cost) and len(tids)==len(set(tids)), (set(tids)^set(cost))
for n,g,mode in (("g1",g1,1),("g2",g2,0),("g3",g3,0)):
    pk=open(P+f'packs/geo-option-global-interdependence-s2.t2{n}.txt').read()
    pids=set(re.findall(r'^\[([^\]]+)\]',pk,re.M))
    out={}
    for t in tids:
        nd=g.get(short(t),[])
        for x in nd: assert x["id"] in pids and x["id"]!=t,(t,x["id"])
        out[t]={"cost":cost[t],"needs":nd} if mode else {"needs":nd}
    json.dump(out,open(P+f'point-links/geo-option-global-interdependence-s2.t2{n[1:]}'.replace('t2g','t2g')+'.json' if False else P+f'point-links/geo-option-global-interdependence-s2.t2{n}.json','w'),ensure_ascii=False)
    nl=sum(len(v["needs"]) for v in out.values()); lo=sum(x["confidence"]=="low" for v in out.values() for x in v["needs"])
    print(n,len(out),nl,sum(v.get("cost")==2 for v in out.values()),lo)
for k in g1:
    assert S+k in tids
