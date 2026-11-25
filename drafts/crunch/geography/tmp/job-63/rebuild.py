import json,re
P='/Users/gabrielwhelan/barebones/drafts/crunch/geography/'
S="""0.b|1|-
0.0|1|-
0.1|1|-
0.2|1|0.1:H:effects spread through linked system:H
1.b|1|-
1.0|2|-
1.1|1|1.0:H:forest cover after colonisation:H;4.0.3:H:temperate deciduous biome belt:L
2.b|1|-
2.0|1|-
2.1|2|2.0:H:contrast with hunter-gatherers:H;1.1:H:forest that was cleared:H
2.2|2|2.1:E:clearance by farmers:H;1.0:H:elm among native trees:L
3.b|1|2.1:H:clearance for farming:L
3.0|1|2.1:E:Neolithic farming in Ireland:H
3.1|2|3.0:E:fields later covered by bog:H;2.1:H:forest clearance by farmers:H
3.2|1|3.1:H:walls buried under bog:H
4.b|1|-
4.0|1|2.1:H:earlier clearance continues:H
4.1|2|4.0:H:clearance before the great clearance:L
4.2|1|4.1:E:conquest and plantation context:H
4.3|1|4.1:H:result of great clearance:H
4.4|1|4.3:H:recovery from 1% forest:H
5.b|1|-
5.0|1|1.1:H:native deciduous forest:H
5.1|1|5.0:H:habitat lost by replacement:H
5.2|2|3.1:H:blanket bog spread and leaching:H
6.b|1|4.4:H:new forest is plantation:L
6.0|1|4.4:H:conifer plantations:H
6.1|1|6.0:E:Sitka plantations:H
6.2|2|5.0:H:remnants of native forest:L
7.b|1|-
7.0|2|-
7.1|1|7.0:E:cleared slopes:H
7.2|1|-
7.3|1|-
8.b|1|4.17.1:H:Amazon Basin location:H
8.0|1|-
8.1|2|8.0:E:PRODES satellite figures:H
8.2|1|8.1:H:scale of clearance:L
9.b|1|-
9.0|1|-
9.1|1|9.0:H:contrast with cattle ranching:L
9.2|1|-
9.3|1|9.0:H:causes of clearance:L
10.b|1|-
10.0|2|9.3:H:government policy drives clearance:L
10.1|2|10.0:E:roads open forest to settlers:H;8.0:H:satellite images:H
10.2|1|-
10.3|1|10.2:E:Carajas mining:H
10.4|1|12.0:H:Yanomami and gold miners:H
10.5|2|-
10.6|1|10.5:E:Belo Monte dam:H;12.0:H:indigenous peoples harmed:L
11.b|1|-
11.0|1|4.24.b:H:high rainforest species diversity:H
11.1|1|11.0:H:habitat loss:L
11.2|2|4.20.3:E:closed rapid nutrient cycle:H;9.0:H:pasture after ranching:L
11.3|2|11.2:H:exposed soil after clearance:H;4.20.0:H:laterised latosol soils:H
11.4|2|4.19.6:H:forest recycles rain by evapotranspiration:H
11.5|1|-
11.6|2|8.2:H:share of forest cleared:H;11.4:H:water cycle loss:L
12.b|1|-
12.0|1|10.4:H:gold mining on Yanomami land:H
12.1|1|9.0:H:ranchers behind conflict:L
12.2|1|10.4:E:illegal gold mining:H;12.0:H:Yanomami harmed:H
13.b|1|-
13.0|1|-
13.1|1|9.1:E:soya farming in Amazon:H
13.2|1|-
13.3|2|8.0:E:PRODES satellite data:H
13.4|2|12.1:E:Chico Mendes:H
13.5|1|8.1:E:falls and rises in clearance:H
14.b|1|4.17.3:H:South-East Asia rainforest:H
14.0|1|14.b:H:palm oil:H
14.1|1|14.b:H:oil palm clearance in Borneo:H
14.2|1|14.1:E:drained peat forest:H
14.3|1|4.25.3:H:orangutan lives in Borneo:L
15.b|1|-
15.0|1|9.1:H:soya exported to Europe:H;14.0:H:palm oil demand:L
15.1|2|15.0:H:European demand being regulated:H
16.b|1|-
16.0|1|-
16.1|1|16.0:H:intensive farming:H
17.b|1|16.0:H:intensive farming:H
17.0|1|17.b:H:dairying intensifies:L
17.1|2|16.1:H:fewer simpler habitats:H
17.2|1|17.1:H:meadows reseeded:L
17.3|1|17.2:E:corncrake:H
17.4|1|17.1:H:hedgerows and meadows lost:H
18.b|1|-
18.0|1|16.0:H:fertiliser use:L
18.1|1|18.0:E:nutrients from fertiliser:H
18.2|1|-
18.3|2|18.0:H:problem being responded to:H
19.b|1|-
19.0|2|16.1:H:hedgerow and wetland loss:H;17.1:H:same Irish changes:L
19.1|1|19.0:E:guaranteed prices:H
19.2|1|19.0:H:reform of CAP:H;18.3:H:agri-environment payments:L
20.b|1|-
20.0|1|-
20.1|1|20.0:H:ploughed grassland:H
20.2|1|9.0:E:cattle ranching impacts:H;9.1:H:soya farming:H
21.b|1|-
21.0|1|21.b:H:Aral Sea case study:L
21.1|2|21.0:H:the sea being starved:H
21.2|1|21.1:E:less water reached sea:H
21.3|1|21.2:E:sea shrank:H
21.4|1|21.2:E:exposed seabed:H
21.5|1|21.1:H:irrigation:H
21.6|1|21.2:H:shrunken sea:H
22.b|1|-
22.0|1|-
22.1|2|22.0:E:acids carried downwind:H
22.2|1|22.0:E:acid pollution:H
22.3|1|22.0:E:acid pollution:H
22.4|2|22.0:H:acid gases:H
22.5|1|22.4:E:Black Triangle emissions:H;22.2:H:forest damage:H
23.b|1|22.1:H:acid rain crosses borders:H
23.0|2|22.0:H:SO2 and NOx emissions:H
23.1|1|23.0:E:responses reducing SO2:H
23.2|1|-
23.3|1|23.2:E:Moneypoint:H;23.0:H:flue-gas desulphurisation:H
24.b|1|-
24.0|1|24.b:E:raised bogs:H
24.1|2|24.0:E:Bord na Mona peat harvesting:H
24.2|2|24.1:H:end of peat harvesting:H
24.3|1|24.b:E:raised bog:H
24.4|1|-
25.b|1|-
25.0|2|4.0.3:H:boreal forest biome:L
25.1|1|25.0:E:oil sands mining:H
25.2|1|25.0:E:mined land:H
26.b|1|-
26.0|1|-
26.1|1|26.0:E:oil production spills:H
26.2|1|26.1:E:pollution from spills:H
27.b|1|-
27.0|1|-
27.1|1|27.0:E:Chernobyl explosion:H
27.2|2|27.0:E:Chernobyl evacuation:H
28.b|1|-
28.0|2|-
28.1|1|-
29.b|1|-
29.0|2|24.2:H:rewetting of bogs:L;18.3:H:agri-environment schemes:H
29.1|1|29.0:H:benefits versus losses:H"""
name='geo-option-geoecology-s5.t1g1'
pk=set(re.findall(r'^\[([^\]]+)\]',open(P+'packs/'+name+'.txt').read(),re.M))
tg=[i for i in re.findall(r'^\[([^\]]+)\]',open(P+'packs/'+name+'.txt').read().split('CANDIDATES')[0],re.M)]
d={}
for ln in S.split('\n'):
    k,c,ls=ln.split('|');i=f"geo-option-geoecology-s5.{k}";needs=[]
    if ls!='-':
        for l in ls.split(';'):
            t,s,w,cf=l.split(':');t=t if t.startswith('4.') or t.startswith('s4') else t
            tid='geo-option-geoecology-s'+(t if t.count('.')==2 else '5.'+t)
            assert tid in pk and tid!=i,(i,tid)
            needs.append({"id":tid,"strength":{'E':'essential','H':'helpful'}[s],"why":w,"confidence":{'H':'high','L':'low'}[cf]})
    d[i]={"cost":int(c),"needs":needs}
assert list(d)==tg,(set(tg)-set(d),set(d)-set(tg))
json.dump(d,open(P+'point-links/'+name+'.json','w'),ensure_ascii=False)
o=json.load(open(P+'tmp/job-63/old_t1g1.json'))
ch=sum(o[i]!=d[i] for i in d);cc=sum(o[i]['cost']!=d[i]['cost'] for i in d)
print(len(d),sum(len(v['needs']) for v in d.values()),sum(v['cost']==2 for v in d.values()),sum(n['confidence']=='low' for v in d.values() for n in v['needs']),'changed',ch,'costchanged',cc)
