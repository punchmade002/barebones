import json,re
P='/Users/gabrielwhelan/barebones/drafts/crunch/geography/'
S='geo-region-continental-s1.'
R='geo-rivers-s1.'
V='geo-volcanoes-earthquakes-s5.'
# id|cost|g1 links|g2 links|g3 links ; link = target:E/H:why:H/L ; '-' = explicit empty
spec='''0.b|1|-|-|-
0.0|1|-|-|-
0.1|1|-|-|-
0.2|1|-|-|-
0.3|1|-|-|-
0.4|1|-|-|-
0.5|1|-|-|-
1.b|1|-|-|-
1.0|1|-|-|-
1.1|1|17.2:H:Deccan Plateau:H|-|-
1.2|2|27.2:H:Ganges route and places:H|-|-
1.3|2|27.7:H:Kolkata on the Hooghly:H;27.3:H:Delhi on the Yamuna:H|-|-
1.4|1|42.1:H:Green Revolution:H|-|-
1.5|1|21.3:H:Chota Nagpur Plateau:H|-|-
2.b|1|-|-|-
2.0|2|-|-|-
2.1|1|-|-|-
2.2|1|-|-|-
2.3|1|2.0:H:monsoon wind reversal:H|-|-
2.4|1|2.0:H:monsoon wind reversal:H|-|-
2.5|1|2.3:H:wet season timing:L|-|-
3.b|1|-|-|-
3.0|2|2.0:H:monsoon wind reversal:H|-|-
3.1|2|3.0:H:low pressure draws air:L|-|-
3.2|2|3.1:H:ITCZ shift:H|-|-
3.3|1|3.2:E:south-west winds:H|-|-
3.4|2|3.3:H:monsoon arrival:L|-|-
3.5|1|3.4:E:jet stream position:H|-|-
4.b|1|-|-|-
4.0|1|-|-|-
4.1|1|2.3:H:wet monsoon season:H|-|-
4.2|1|22.0:H:Western Ghats:H|-|-
4.3|2|17.0:H:Himalayan barrier:L|-|-
5.b|1|-|-|-
5.0|2|22.0:H:Western Ghats:H;24.0:H:Konkan and Malabar coasts:H|-|-
5.1|2|5.0:E:relief rain:H;17.2:H:Deccan Plateau:H|-|-
5.2|1|5.0:E:relief rain:H;4.3:H:Bay of Bengal branch:H|-|-
5.3|1|4.3:H:Bay of Bengal branch:H|-|-
5.4|2|4.2:E:Arabian Sea branch:H;23.2:H:Aravalli Range:H;5.0:H:relief rain:H|-|-
6.b|1|-|-|-
6.0|1|2.4:H:cool dry season:H|-|-
6.1|1|17.0:H:Himalayas:L|-|-
6.2|1|6.0:H:winter monsoon winds:H;24.1:H:Coromandel coast:L|-|-
6.3|1|-|-|-
7.b|1|-|-|-
7.0|1|2.2:H:hot season:H|-|-
7.1|1|-|-|-
7.2|1|17.0:H:Himalayas:L|-|-
8.b|1|-|-|-
8.0|1|2.3:H:monsoon rain:H|-|-
8.1|1|2.3:H:monsoon rain:H|-|-
8.2|1|-|-|-
8.3|1|8.2:H:tropical cyclones:H|-|-
8.4|1|8.0:H:drought risk:H;8.1:H:flood risk:L|-|-
9.b|1|-|-|-
9.0|1|38.0:H:kharif and rabi crops:H|-|-
9.1|1|-|-|-
9.2|1|36.1:H:agriculture share of GDP:H|-|-
10.b|1|-|-|-
10.0|1|17.1:H:Indo-Gangetic Plain:H|-|-
10.1|2|10.0:E:alluvial soil:H|geo-rivers-s1.12.1:H:alluvium deposited by floods:L|-
10.2|1|23.3:H:Thar Desert:L|-|-
10.3|1|10.2:E:desert soils:H;41.0:H:Indira Gandhi Canal:H|-|-
11.b|1|-|-|-
11.0|2|21.4:E:Deccan Traps basalt:H|-|-
11.1|1|11.0:H:black soil:H|-|-
11.2|1|11.1:H:clay-rich soil:H|-|-
11.3|1|11.1:E:moisture-holding clay:H|-|-
12.b|1|-|-|-
12.0|1|21.0:H:Deccan crystalline rock:H|-|-
12.1|1|12.0:H:red soil:H|-|-
12.2|1|12.1:H:poor red soil:L|-|-
13.b|1|-|-|-
13.0|2|-|-|-
13.1|1|22.0:H:Western Ghats:H;13.0:H:laterite:H|-|-
13.2|1|13.0:E:leaching removes nutrients:H|-|-
13.3|1|13.0:H:laterite:H|-|-
14.b|1|-|-|-
14.0|1|17.0:H:Himalayas:L|-|-
14.1|1|14.0:H:Himalayan slopes:H|-|-
15.b|1|-|-|-
15.0|2|2.3:H:monsoon downpours:L|-|-
15.1|2|33.4:H:canal irrigation:H|-|-
15.2|1|42.1:H:Green Revolution:H|-|-
16.b|1|-|-|-
16.0|1|11.0:E:black soil from basalt:H;21.4:E:Deccan Traps:H|-|-
16.1|1|13.0:E:laterite formation:H|-|-
17.b|1|-|-|-
17.0|1|-|-|-
17.1|1|-|-|-
17.2|1|-|-|-
17.3|1|-|-|-
18.b|1|-|-|-
18.0|2|-|-|geo-volcanoes-earthquakes-s5.3.1:H:plates converge, rock compressed:H
18.1|1|18.0:H:Himalayan mountains:H|-|-
18.2|1|0.3:H:Nepal as neighbour:H|-|-
18.3|1|0.3:H:Nepal and China neighbours:L|-|-
19.b|1|-|-|-
19.0|1|-|-|-
19.1|1|5.0:H:relief rain:H|-|-
19.2|1|26.0:H:perennial Himalayan rivers:H|-|-
19.3|1|19.2:H:Himalayan rivers:H|-|-
19.4|1|18.0:H:fold mountain tectonics:L|-|-
19.5|1|7.2:H:cold at altitude:L|-|-
20.b|1|-|-|-
20.0|1|-|-|-
20.1|1|17.1:H:Northern Plains:H|geo-rivers-s1.12.1:H:alluvium deposition:H|-
20.2|1|20.0:H:Northern Plains:H|-|-
21.b|1|-|-|-
21.0|2|-|-|-
21.1|1|-|-|-
21.2|1|21.0:H:Deccan Plateau:H;30.0:H:east-flowing rivers:L|-|-
21.3|1|17.2:H:Deccan:H|-|-
21.4|2|-|-|-
22.b|1|-|-|-
22.0|1|-|-|-
22.1|1|22.0:H:Western Ghats:H|-|-
22.2|1|22.0:H:Western Ghats:H|-|-
22.3|1|21.2:H:plateau tilts east:H|-|-
23.b|1|-|-|-
23.0|1|17.1:H:Northern Plains:H;17.2:H:Deccan:H|-|-
23.1|1|23.0:H:Vindhya and Satpura:H|-|-
23.2|1|-|-|geo-volcanoes-earthquakes-s5.4.1:H:old fold mountains worn down:L
23.3|1|23.2:E:Aravalli Range:H;5.0:H:relief rain:H|-|-
24.b|1|-|-|-
24.0|1|17.3:H:coastal plains:H|-|-
24.1|1|21.2:H:rivers flow east:H|geo-rivers-s1.13.0:H:delta formation:H|-
25.b|1|-|-|-
25.0|1|20.2:H:Northern Plains:H|-|-
25.1|1|21.3:H:Chota Nagpur minerals:H|-|-
25.2|1|19.3:H:hydroelectric potential:H|-|-
26.b|1|-|-|-
26.0|1|19.2:H:perennial Himalayan rivers:H|-|-
26.1|1|21.2:H:plateau drainage:H|-|-
26.2|1|21.0:H:old hard Deccan rock:H|-|-
27.b|1|-|-|-
27.0|1|-|-|-
27.1|1|27.0:H:Bhagirathi:H|-|-
27.2|2|-|-|-
27.3|1|27.2:H:Ganges course:H|geo-rivers-s1.0.2:H:tributary:H|-
27.4|1|-|geo-rivers-s1.0.4:H:drainage basin:H|-
27.5|2|28.2:H:Brahmaputra joins Ganges:H|geo-rivers-s1.13.0:H:delta formation:H|-
27.6|1|27.5:H:Ganges delta:H|-|-
27.7|1|27.5:H:delta and distributaries:H|geo-rivers-s1.0.6:H:distributary:H|-
28.b|1|-|-|-
28.0|1|-|-|-
28.1|1|28.0:H:Brahmaputra course:H|-|-
28.2|1|-|-|-
28.3|1|-|geo-rivers-s1.15.2:H:braided channel:H|-
29.b|1|-|-|-
29.0|1|0.3:H:Pakistan as neighbour:H|-|-'''
rows=[l.split('|') for l in spec.split('\n')]
def L(s,pk):
    if s=='-':return []
    out=[]
    for x in s.split(';'):
        t,st,w,c=x.split(':')
        tid=t if t.startswith('geo-') else S+t
        out.append({"id":tid,"strength":"essential" if st=='E' else "helpful","why":w,"confidence":"high" if c=='H' else "low"})
    return out
names=['t1g1','t1g2','t1g3']
for k,n in enumerate(names):
    out={}
    for r in rows:
        assert len(r)==5,r
        e={"needs":L(r[2+k],k)}
        out[S+r[0]]={"cost":int(r[1]),**e} if k==0 else e
    ids=[l[1:l.index(']')] for l in open(P+'packs/geo-region-continental-s1.%s.txt'%n) if l.startswith('[geo-region-continental-s1.')]
    # targets = first segment before first CANDIDATES
    txt=open(P+'packs/geo-region-continental-s1.%s.txt'%n).read()
    tgt=re.findall(r'^\[([^\]]+)\]',txt.split('\nCANDIDATES')[0],re.M)
    allids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
    assert list(out)==tgt,(n,set(out)^set(tgt))
    for v in out.values():
        for nd in v['needs']: assert nd['id'] in allids and (k==0 or nd['id'] not in tgt),(n,nd)
    json.dump(out,open(P+'point-links/geo-region-continental-s1.%s.json'%n,'w'),indent=1)
    json.load(open(P+'point-links/geo-region-continental-s1.%s.json'%n))
    nl=sum(len(v['needs']) for v in out.values());lo=sum(nd['confidence']=='low' for v in out.values() for nd in v['needs'])
    print(n,len(out),nl,sum(v.get('cost')==2 for v in out.values()),lo)
