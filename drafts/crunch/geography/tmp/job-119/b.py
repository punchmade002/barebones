import json,re
P='/Users/gabrielwhelan/barebones/drafts/crunch/geography/'
PFX={'s2':'geo-region-ireland-s2.','c4':'geo-region-concept-s4.','e2':'geo-economic-activities-s2.','c1':'geo-region-concept-s1.','c3':'geo-region-concept-s3.','m6':'geo-population-migration-s6.'}
def full(k):
    a,b=k.split('.',1); return PFX[a]+b
# pkg1: id|cost|links  (link = tid:E/H:why:h/l)
P1="""
0.b|1|c4.0.2:H:core-periphery idea:h
0.0|1|
0.1|1|
0.2|1|
1.b|1|c4.0.3:H:problems reinforce each other:l
1.0|1|
1.1|1|
1.2|1|s2.36.1:H:history of emigration:h
1.3|1|c4.0.1:H:primary activities:h
1.4|1|s2.33.2:H:growth centre Galway:l
2.b|1|
2.0|1|
2.1|1|s2.7.0:H:River Corrib route:h
2.2|1|s2.7.4:H:River Moy at Ballina:h
2.3|1|s2.0.1:H:Galway and Castlebar towns:h
2.4|1|s2.5.0:H:upland names:h
2.5|1|s2.5.4:E:limestone lowland location:h
2.6|1|s2.5.7:H:Aran Islands:h
3.b|1|
3.0|1|
3.1|1|
3.2|1|
3.3|2|s2.3.2:H:relief rainfall explains wet mountains:h
3.4|1|
3.5|1|
3.6|1|s2.3.1:H:Atlantic air from south-west:h
4.b|1|
4.0|1|s2.3.3:H:high rainfall waterlogging:h
4.1|1|s2.3.1:H:Atlantic gales:h
4.2|1|s2.3.1:H:gales and storms:h
4.3|1|
5.b|1|
5.0|2|
5.1|2|s2.5.0:E:the peaks named:h
5.2|2|s2.5.0:H:the uplands named:h
5.3|1|
5.4|1|
5.5|1|
5.6|2|
5.7|1|
6.b|1|
6.0|1|s2.3.3:H:high rainfall waterlogging:h
6.1|2|s2.5.0:H:upland location:h
6.2|1|s2.5.5:H:drumlins:h
6.3|1|s2.5.4:H:limestone lowland:h
6.4|1|s2.5.7:H:Aran limestone:h
7.b|1|
7.0|1|
7.1|1|
7.2|2|s2.5.4:H:limestone lowland:l
7.3|1|
7.4|1|
7.5|1|
7.6|1|s2.7.5:H:River Shannon:h
7.7|2|s2.7.4:H:the River Moy:h
8.b|1|
8.0|1|s2.3.3:H:high rainfall:h
8.1|1|s2.6.3:H:limestone brown earths:h
8.2|1|s2.6.3:H:brown earths on limestone:h
8.3|1|s2.6.0:H:blanket bog:h
9.b|1|
9.0|2|s2.37.0:H:rundale system:h
9.1|2|s2.9.0:E:fragmented plots consolidated:h
9.2|1|s2.9.0:E:fragmented holdings:h
9.3|1|
9.4|1|
9.5|1|s2.1.0:H:remote location:h
10.b|1|
10.0|2|s2.8.3:H:grazing-only land:h
10.1|1|
10.2|1|s2.8.1:H:tillage restricted:h
10.3|1|
10.4|1|
11.b|1|
11.0|1|s2.1.2:H:ageing, out-migration:h
11.1|2|s2.9.4:H:CAP payments:h;s2.10.1:H:sheep on commonage:h
11.2|1|s2.11.1:E:more sheep overgrazed:h
11.3|1|s2.11.2:E:damage from overgrazing:h
11.4|1|s2.10.1:H:hill commonage:h
11.5|1|s2.11.1:E:contrast with headage payments:h
11.6|1|
12.b|1|
12.0|1|s2.6.0:H:blanket bog:h
12.1|1|s2.12.0:H:conifer plantations:h
12.2|1|
12.3|1|
12.4|1|
13.b|1|
13.0|1|s2.12.0:H:conifer plantations:h
13.1|1|s2.12.0:H:single-species forest:h
13.2|2|s2.6.0:H:blanket bog peat:h
13.3|1|s2.13.2:E:the Derrybrien slide:h
14.b|1|
14.0|1|
14.1|1|
14.2|1|
14.3|1|
14.4|1|s2.7.4:H:River Moy at Ballina:h
14.5|1|
15.b|1|
15.0|1|s2.6.0:H:Bellacorick bog:h
15.1|1|s2.15.0:H:same place as peat station:h
15.2|1|s2.15.0:H:Bellacorick peat history:h
15.3|1|s2.3.1:H:Atlantic winds:h
15.4|1|s2.15.3:H:wave energy potential:h
16.b|1|
16.0|1|
16.1|1|s2.16.0:E:the Corrib gas field:h
16.2|1|s2.16.1:H:the gas project:h
16.3|1|
16.4|1|s2.5.2:H:hard rocks:l
16.5|1|s2.5.0:H:Croagh Patrick:h
17.b|1|
17.0|1|
17.1|1|
17.2|1|
18.b|1|
18.0|1|
18.1|1|s2.18.0:H:DEC skilled workforce:h
18.2|1|s2.18.1:E:the multinationals:h
18.3|1|s2.18.2:H:cluster growth:h
19.b|1|
19.0|1|
19.1|1|
19.2|1|s2.17.0:H:manufacturing in Galway:h
19.3|1|
20.b|1|
20.0|1|
20.1|1|
20.2|2|
20.3|1|
20.4|1|
21.b|1|
21.0|1|
"""
P2="""
0.b|c1.1.2:H:peripheral region defined:h
0.0|
0.1|
0.2|
1.b|
1.0|
1.1|
1.2|
1.3|
1.4|e2.1.7:H:infrastructure meaning:h
2.b|
2.0|
2.1|
2.2|
2.3|
2.4|
2.5|
2.6|
3.b|c1.4.b:H:causes of Irish climate:h
3.0|c1.3.b:H:cool temperate oceanic features:h
3.1|c1.4.3:H:prevailing south-westerly winds:h
3.2|c1.4.5:E:relief rainfall:h
3.3|c1.5.0:H:west wetter than east:h
3.4|c1.4.1:H:North Atlantic Drift:h
3.5|c1.4.2:H:maritime influence small range:h
3.6|c1.5.4:H:east sunnier than west:l
4.b|
4.0|c1.7.2:H:grass grows, pastoral farming:h
4.1|
4.2|
4.3|
5.b|
5.0|
5.1|
5.2|
5.3|
5.4|
5.5|
5.6|
5.7|c1.9.b:H:Burren limestone:h
6.b|
6.0|
6.1|
6.2|
6.3|
6.4|c1.9.1:H:limestone pavement:h
7.b|
7.0|
7.1|
7.2|c1.9.5:H:underground drainage on limestone:h
7.3|c1.9.2:H:turloughs:h
7.4|
7.5|
7.6|
7.7|
8.b|
8.0|
8.1|
8.2|
8.3|
9.b|
9.0|
9.1|
9.2|
9.3|
9.4|
9.5|
10.b|
10.0|
10.1|
10.2|
10.3|
10.4|
11.b|
11.0|
11.1|
11.2|
11.3|
11.4|
11.5|
11.6|
12.b|
12.0|
12.1|
12.2|
12.3|
12.4|
13.b|
13.0|
13.1|
13.2|
13.3|
14.b|
14.0|
14.1|
14.2|
14.3|
14.4|
14.5|
15.b|
15.0|
15.1|
15.2|
15.3|
15.4|
16.b|
16.0|
16.1|
16.2|
16.3|
16.4|
16.5|
17.b|
17.0|
17.1|
17.2|
18.b|
18.0|
18.1|
18.2|e2.6.0:H:agglomeration and clusters:h
18.3|
19.b|
19.0|
19.1|
19.2|
19.3|
20.b|e2.4.4:H:regional policy:h
20.0|e2.4.1:H:IDA Ireland grants:h
20.1|e2.4.3:H:Údarás na Gaeltachta:h
20.2|
20.3|
20.4|
21.b|e2.2.2:H:labour factor:h
21.0|e2.2.3:H:graduates for skilled firms:h
"""
P3_links={'9.0':'m6.1.2:H:small subdivided holdings:h','11.0':'m6.8.1:H:farms with no successor:h','1.4':'m6.9.0:H:growth centres gateways:l',
'20.1':'c3.2.1:H:Údarás na Gaeltachta:h','20.2':'m6.9.0:H:gateways and hubs:h','20.3':'m6.9.5:H:National Planning Framework:h','20.4':'m6.9.2:H:Western Development Commission:h'}
def parse_links(s):
    out=[]
    for l in filter(None,s.split(';')):
        t,st,why,c=l.split(':')
        out.append({'id':full(t),'strength':'essential' if st=='E' else 'helpful','why':why,'confidence':'high' if c=='h' else 'low'})
    return out
def run(n,name,data):
    txt=open(P+'packs/'+name+'.txt').read()
    tgt=txt.split('CANDIDATES')[0]
    ids=re.findall(r'^\[(\S+?)\]',tgt,re.M)
    allids=set(re.findall(r'^\[(\S+?)\]',txt,re.M))
    out={}
    for i in ids:
        k=i.replace('geo-region-ireland-s2.','')
        out[i]=data[k]
    assert len(out)==len(ids)==len(data),(len(out),len(ids),len(data))
    nl=nlow=c2=0
    for v in out.values():
        c2+=v.get('cost')==2
        for l in v['needs']:
            assert l['id'] in allids and l['id']!=None; nl+=1; nlow+=l['confidence']=='low'
    json.dump(out,open(P+'point-links/'+name+'.json','w'),ensure_ascii=False,indent=1)
    print(name,len(out),nl,c2,nlow)
d1={}
for line in P1.strip().splitlines():
    k,c,l=line.split('|'); d1[k]={'cost':int(c),'needs':parse_links(l)}
d2={};d3={}
for line in P2.strip().splitlines():
    k,l=line.split('|'); d2[k]={'needs':parse_links(l)}; d3[k]={'needs':parse_links(P3_links.get(k,''))}
for k in d1: assert k in d2
run(1,'geo-region-ireland-s2.t1g1',d1)
run(2,'geo-region-ireland-s2.t1g2',d2)
run(3,'geo-region-ireland-s2.t1g3',d3)
