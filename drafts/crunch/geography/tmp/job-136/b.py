import json,re
P='/Users/gabrielwhelan/barebones/drafts/crunch/geography/'
PRE={'S3':'geo-urban-s3.','u1':'geo-urban-s1.','r5':'geo-region-concept-s5.'}
def tok(t):
    ref,s,why,c=t.split(':')
    p,rest=ref.split('.',1)
    return {"id":PRE[p]+rest,"strength":{'h':'helpful','e':'essential'}[s],"why":why.replace('_',' '),"confidence":{'H':'high','L':'low'}[c]}
def parse(txt,cost=True):
    out={}
    for ln in txt.strip().splitlines():
        p=ln.split()
        k='geo-urban-s3.'+p[0]
        if cost: c=int(p[1]); l=p[2:]
        else: l=p[1:]
        d={"needs":[tok(t) for t in l]}
        if cost: d={"cost":c,**d}
        out[k]=d
    return out
A='''0.b 1
0.0 1
0.1 1
0.2 1
0.3 1
0.4 1
0.5 1
0.6 1
1.b 1 u1.0.2:h:situation_defined_there:H
1.0 1
1.1 1
1.2 1
2.b 1 u1.0.3:h:function_defined_there:H
2.0 1
2.1 1
2.2 1
2.3 1
2.4 1
3.b 1
3.0 1
3.1 1
3.2 1
4.b 1 S3.3.0:h:hierarchy_ranking:H
4.0 1
4.1 2
4.2 2
4.3 1
5.b 1
5.0 1 S3.5.b:h:primate_city_defined:H
5.1 2
5.2 2
5.3 1
6.b 1
6.0 1
6.1 1 S3.6.0:h:contrasts_low-order_goods:H
7.b 1
7.0 1
8.b 1 S3.7.b:h:hinterland_defined:H
8.0 1
8.1 1
8.2 1
8.3 1
8.4 1
8.5 1
9.b 1
9.0 1 S3.7.b:h:hinterland_idea:H
9.1 1
9.2 1
9.3 1 S3.7.b:h:hinterland_idea:H
10.b 1
10.0 1
10.1 1
10.2 1
10.3 2 S3.10.1:e:threshold:H S3.10.2:e:range:H
11.b 1 S3.10.b:h:central_place_theory:H
11.0 1
11.1 1
11.2 1
11.3 1
11.4 1
12.b 1 S3.11.b:h:ideal_plain_assumptions:H
12.0 1
12.1 1 S3.6.0:h:low-order_and_high-order_goods:H
12.2 1 S3.12.1:h:hierarchy_of_centres:H
12.3 2 S3.12.0:h:hexagonal_market_areas:L
13.b 1
13.0 1
13.1 2
13.2 1 S3.12.1:h:two-level_hierarchy:L
14.b 1
14.0 1 S3.11.0:h:uniform_plain_assumption:H
14.1 1 S3.11.2:h:equal_transport_assumption:H
14.2 1 S3.11.3:h:nearest_centre_assumption:H
14.3 1 S3.10.1:h:threshold:H S3.10.2:h:range:H
14.4 1 u1.7.b:h:Viking_towns:L
14.5 1 S3.5.0:h:Dublin_primacy:H
14.6 1 S3.2.1:h:town_function_types:L
15.b 1 S3.10.b:h:central_place_theory:H
15.0 1 S3.3.0:h:hierarchy_ranking:H
15.1 1 S3.5.0:h:Dublin_primacy:H
16.b 1 S3.2.b:h:functions_defined:H
16.0 1
16.1 1
16.2 1
16.3 1
16.4 1 S3.2.3:h:commuter_towns:H
16.5 1
17.b 1
17.0 1
17.1 2
17.2 1
17.3 1
17.4 1
18.b 1
18.0 1
18.1 1
18.2 1
18.3 2 S3.5.3:h:NSS_and_NPF_plans:H
18.4 1
18.5 1
18.6 1
19.b 1 S3.0.2:h:island_site:H
19.0 1
19.1 1 S3.0.2:h:island_site:H
19.2 1
19.3 1 u1.13.6:h:Newtown_Pery:L
20.b 1
20.0 1
20.1 1 u1.15.0:h:Shannon_Free_Zone:H
20.2 2
20.3 2
20.4 1
20.5 1
20.6 1
21.b 1
21.0 1 u1.7.2:h:Dublin_Viking_longphort:L
21.1 1
21.2 1 u1.13.5:h:Wide_Streets_Commissioners:H
21.3 1
21.4 2
22.b 1 S3.2.3:h:commuter_towns:H
22.0 1
22.1 1 S3.2.3:h:commuter_towns:H
22.2 2 S3.2.3:h:commuter_towns:H
23.b 1
23.0 1 S3.0.b:h:site_types:H
23.1 1 S3.0.1:h:route_focus:H
23.2 1
23.3 1
23.4 1
23.5 1
23.6 1 S3.5.3:h:NSS_and_NPF:H
23.7 1'''
B={'2.3':'r5.0.4:h:commuter_belt:H','5.0':'r5.4.b:h:primate_city_Dublin:H','5.3':'r5.6.0:h:NPF_aim:H','9.3':'r5.5.2:h:Galway_hinterland:H','14.5':'r5.4.b:h:Dublin_primacy:L','16.4':'r5.0.4:h:commuter_belt:L','18.3':'r5.6.0:h:NPF:H','22.1':'r5.0.4:h:commuter_belt:H','23.6':'r5.6.0:h:NPF:H'}
a=parse(A)
b=parse('\n'.join(k+(' '+B[k] if k in B else '') for k in [l.split()[0] for l in A.splitlines()]),False)
for name,d,pk in(('t1g1',a,'geo-urban-s3.t1g1'),('t1g2',b,'geo-urban-s3.t1g2')):
    txt=open(P+'packs/'+pk+'.txt').read()
    ids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
    tg=re.findall(r'^\[(geo-urban-s3\.[^\]]+)\]',txt.split('CANDIDATES')[0],re.M)
    assert list(d)==tg,(set(tg)^set(d))
    for v in d.values():
        for n in v['needs']: assert n['id'] in ids,n
    json.dump(d,open(P+'point-links/geo-urban-s3.'+name+'.json','w'),indent=1)
    print(name,len(d),sum(len(v['needs']) for v in d.values()),sum(v.get('cost')==2 for v in d.values()),sum(n['confidence']=='low' for v in d.values() for n in v['needs']))
