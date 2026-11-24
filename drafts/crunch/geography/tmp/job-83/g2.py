import json,re
P='geo-population-migration-s2.'
G='geo-graph-skills-s1.5.1'
# explicit decision per id: 0 = no links, D = density link
spec="""0.b 0|0.0 0|0.1 0|0.2 0|0.3 0|0.4 D|0.5 0|0.6 0|1.b 0|1.0 0|1.1 0|1.2 0|1.3 0|1.4 0|
2.b 0|2.0 0|2.1 0|2.2 0|2.3 0|3.b 0|3.0 0|3.1 0|3.2 0|3.3 0|3.4 0|3.5 0|
4.b 0|4.0 0|4.1 0|4.2 0|4.3 0|5.b 0|5.0 0|5.1 0|5.2 0|6.b 0|6.0 0|
7.b 0|7.0 0|7.1 0|7.2 0|7.3 0|7.4 0|8.b 0|8.0 0|8.1 0|8.2 0|8.3 0|
9.b 0|9.0 0|9.1 0|9.2 0|9.3 0|10.b 0|10.0 0|10.1 0|10.2 0|10.3 0|
11.b 0|11.0 0|11.1 0|11.2 0|11.3 0|12.b 0|12.0 0|12.1 0|12.2 0|12.3 D|
13.b 0|13.0 0|13.1 0|13.2 0|13.3 0|13.4 0|13.5 0|14.b 0|14.0 0|14.1 0|14.2 0|14.3 0|
15.b 0|15.0 0|15.1 0|15.2 0|16.b 0|16.0 0|16.1 0|16.2 0|16.3 0|16.4 0|16.5 0|16.6 0|
17.b 0|17.0 0|17.1 0|17.2 0|18.b 0|18.0 0|18.1 0|18.2 0|19.b 0|19.0 0|19.1 0|19.2 0|
20.b 0|20.0 0|20.1 0|20.2 0|20.3 0|21.b 0|21.0 0|21.1 0|21.2 0|22.b 0|22.0 0|22.1 0|22.2 0|22.3 0"""
d={}
for tok in re.split(r'[|\n]+',spec):
    if not tok.strip(): continue
    k,v=tok.split()
    d[P+k]={"needs":[] if v=='0' else [{"id":G,"strength":"helpful","why":"density = number per area","confidence":"low"}]}
json.dump(d,open('../../point-links/geo-population-migration-s2.t1g2.json','w'),indent=1)
t=open('../../packs/geo-population-migration-s2.t1g2.txt').read()
ids=re.findall(r'^\[([^\]]+)\]',t,re.M)
tg=[i for i in ids if i.startswith(P)]
assert sorted(tg)==sorted(d)
for v in d.values():
    for x in v['needs']: assert x['id'] in ids
print(len(d),sum(len(v['needs']) for v in d.values()),sum(x['confidence']=='low' for v in d.values() for x in v['needs']))
