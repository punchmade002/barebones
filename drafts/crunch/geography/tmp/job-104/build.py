import json,re
P='/Users/gabrielwhelan/barebones/drafts/crunch/geography/'
S='geo-region-continental-s2.'
COST="""30.3 1
30.4 1
31.b 1
31.0 1
31.1 1
31.2 2
31.3 1
32.b 1
32.0 1
32.1 1
32.2 2
32.3 1
33.b 1
33.0 2
33.1 1
33.2 1
33.3 1
33.4 1
34.b 1
34.0 1
34.1 1
34.2 1
34.3 1
35.b 1
35.0 1
35.1 1
35.2 1
36.b 1
36.0 1
36.1 1
36.2 1
36.3 1
37.b 1
37.0 2
37.1 2
37.2 1
37.3 1
38.b 1
38.0 1
38.1 1
38.2 1
38.3 1
38.4 1
39.b 1
39.0 1
39.1 1
39.2 1
39.3 1
40.b 1
40.0 1
40.1 1
40.2 1
41.b 1
41.0 1
41.1 1
41.2 1
41.3 1
42.b 1
42.0 1
42.1 1
42.2 1
42.3 1
43.b 1
43.0 1
43.1 1
43.2 1
43.3 1
44.b 1
44.0 1
44.1 1
44.2 1
44.3 1
45.b 1
45.0 1
45.1 1
45.2 1
45.3 1
45.4 1
46.b 1
46.0 1
46.1 1
46.2 1
46.3 1
47.b 1
47.0 1
47.1 1
47.2 1
47.3 1
47.4 1
48.b 1
48.0 1
48.1 1
48.2 1
48.3 1
48.4 1
49.b 1
49.0 1
49.1 1
49.2 1
49.3 1
50.b 1
50.0 1
50.1 1
50.2 1
50.3 2
51.b 1
51.0 1
51.1 1
51.2 1
52.b 1
52.0 1
52.1 1
52.2 2
52.3 1
52.4 2
53.b 1
53.0 2
53.1 1
53.2 1
53.3 1
54.b 1
54.0 2
54.1 1
54.2 1
54.3 1
55.b 1
55.0 2
55.1 1
55.2 1
55.3 1
56.b 1
56.0 1
56.1 1
56.2 1
57.b 1
57.0 1
57.1 1
57.2 2
57.3 1
58.b 1
58.0 1
58.1 1
59.b 1
59.0 1
59.1 1
60.b 1
60.0 1
60.1 2
60.2 2
61.b 1
61.0 1
61.1 1
61.2 1
61.3 1
62.b 1
62.0 1
62.1 1"""
# pack|src|tgt|strength|conf|why ; tgt prefixes: R=geo-rivers-s1., R4=geo-rivers-s4., else s2
L="""1|31.0|31.2|helpful|high|white-water flooding defined
1|31.1|31.2|helpful|high|black-water defined
1|31.2|30.2|helpful|high|Rio Negro meets Solimões at Manaus
1|32.0|20.0|helpful|high|Brazilian Highlands
1|32.2|32.1|helpful|high|hydroelectric damming
1|32.3|24.2|helpful|high|Iguaçu Falls location
1|33.b|7.b|helpful|high|sertão dry Northeast
1|33.0|29.2|helpful|low|São Francisco basin
1|33.1|7.b|essential|high|sertão dry interior
1|33.4|33.0|helpful|low|São Francisco river course
1|34.0|32.2|helpful|high|Itaipu on the Paraná
1|34.3|34.2|essential|high|Belo Monte Dam
1|35.1|55.0|essential|high|Mariana disaster explained
1|36.3|11.1|helpful|high|2023 Rio Negro drought
1|37.3|37.2|helpful|low|farming versus agribusiness
1|38.2|26.0|helpful|low|Pantanal wetland
1|39.b|6.b|helpful|high|Cerrado wet-dry climate
1|39.0|6.0|helpful|high|rainy season timing
1|39.1|39.0|helpful|low|soya planting timing
1|39.2|39.1|helpful|high|soya harvest clears field
1|39.3|6.1|helpful|high|dry season timing
1|40.1|10.3|helpful|high|frost shaped coffee location
1|41.2|39.2|helpful|low|two crops a year
1|42.0|15.2|helpful|high|massapê soil
1|42.3|42.2|helpful|high|ethanol from cane
1|43.1|38.2|helpful|high|extensive ranching defined
1|43.3|19.3|helpful|high|Pampa grassland
1|44.b|33.b|helpful|high|São Francisco river
1|44.1|33.2|helpful|high|Sobradinho Dam
1|44.2|7.b|helpful|high|semi-arid sertão
1|44.3|17.3|helpful|high|salinisation
1|45.1|12.0|helpful|high|two or three crops a year
1|45.3|15.1|helpful|high|terra roxa on basalt
1|45.3|15.2|helpful|high|massapê soil
1|46.0|13.1|helpful|high|leached latosols
1|46.1|7.b|helpful|high|sertão rainfall
1|46.2|10.1|helpful|low|winter frost in south
1|46.3|17.1|helpful|high|erosion after clearance
1|47.1|47.0|helpful|low|landless versus large estates
1|48.2|14.2|helpful|high|EMBRAPA research
1|48.4|47.3|helpful|low|credit favours large farms
1|49.1|43.2|helpful|high|cattle clearance of forest
1|50.2|50.1|helpful|low|rubber from standing forest
1|50.3|50.2|essential|high|the rubber boom
1|51.0|50.1|helpful|low|rubber tapping
1|51.1|51.0|essential|high|Chico Mendes
1|51.2|51.0|helpful|high|Chico Mendes
1|53.0|0.2|helpful|low|7,400 km coastline
1|55.1|55.0|helpful|high|tailings dam
1|55.3|55.2|helpful|high|illegal mining Yanomami
1|56.0|12.2|helpful|high|rain feeds hydro rivers
1|56.1|56.0|helpful|low|hydro share of electricity
1|57.3|57.2|helpful|high|pre-salt fields
1|58.0|42.3|helpful|high|flex-fuel cars
1|59.1|40.0|helpful|high|coffee boom wealth
1|60.1|60.0|helpful|high|import substitution industry
1|61.1|32.2|helpful|low|Itaipu state project
1|61.1|54.0|helpful|low|Carajás state project
1|62.0|61.3|essential|high|hyperinflation
2|30.3|R:0.7|helpful|high|estuary defined
2|32.3|R:0.2|helpful|high|tributary defined
2|34.3|98.1|helpful|high|Kayapó people
2|35.0|98.1|helpful|high|Yanomami people
2|35.2|111.1|helpful|high|Tietê through São Paulo
2|36.2|R:1.0|helpful|low|gradient steepness
2|46.1|90.2|helpful|high|drought pushes people out
2|47.1|120.0|helpful|high|MST movement
2|47.4|82.1|helpful|low|transport costs for exports
2|55.2|98.1|helpful|high|Yanomami people
2|61.1|79.2|helpful|high|Trans-Amazonian Highway
3|32.1|R4:1.b|helpful|high|hydro-electric dams
3|33.2|R4:1.0|helpful|high|reservoir behind a dam
3|34.b|R4:1.b|helpful|high|hydro-electric dams
3|36.2|R4:1.1|helpful|high|head gives power
3|44.1|R4:1.0|helpful|low|reservoir behind a dam"""
def full(t):
    if t.startswith('R4:'): return 'geo-rivers-s4.'+t[3:]
    if t.startswith('R:'): return 'geo-rivers-s1.'+t[2:]
    return S+t
cost={}
order=[]
for l in COST.split('\n'):
    a,b=l.split(); order.append(a); cost[a]=int(b)
links={1:{},2:{},3:{}}
for l in L.split('\n'):
    p,s,t,st,cf,w=l.split('|')
    links[int(p)].setdefault(s,[]).append({"id":full(t),"strength":st,"why":w,"confidence":cf})
names=['geo-region-continental-s2.t2g1','geo-region-continental-s2.t2g2','geo-region-continental-s2.t2g3']
for i,n in enumerate(names,1):
    txt=open(P+'packs/'+n+'.txt').read()
    head,_,rest=txt.partition('\nCANDIDATES')
    tids=re.findall(r'^\[([^\]]+)\]',head,re.M)
    ids_all=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
    assert tids==[S+o for o in order],(n)
    out={};nl=0;c2=0;low=0
    for o in order:
        d={}
        if i==1: d['cost']=cost[o]; c2+=cost[o]==2
        d['needs']=links[i].get(o,[])
        for x in d['needs']:
            assert x['id'] in ids_all and x['id']!=S+o,(o,x)
            nl+=1; low+=x['confidence']=='low'
        out[S+o]=d
    json.dump(out,open(P+'point-links/'+n+'.json','w'),ensure_ascii=False,indent=1)
    json.loads(open(P+'point-links/'+n+'.json').read())
    print(n,len(out),nl,c2 if i==1 else '-',low)
