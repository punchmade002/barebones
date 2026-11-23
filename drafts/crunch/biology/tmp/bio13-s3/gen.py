import json,re
P='/Users/gabrielwhelan/barebones/drafts/crunch/biology/'
pk=open(P+'points/bio13-s3.txt').read()
pre={'a':'bio13-s1.','b':'bio2-s2.','c':'bio2-s4.','t':'bio13-s3.'}
# item: (cost, [(ref,strength,why,conf)])  E=essential H=helpful h/l
D="""
0.b|1
0.0|1|a.4.0 E substrate and product defined h
0.1|1|t.0.0 E rate definition h
0.2|1|a.4.1 H catalase hydrogen peroxide reaction h
0.3|1|a.6.0 H amylase splits starch l
0.4|1|t.0.0 E rate as amount per time h
0.5|2|t.0.3 E end-point starch disappearing h;c.4.4 H rate as 1/time h
0.6|1|t.0.5 E rate = 1/time h
0.7|1|t.0.0 E rate concept h
1.b|1
1.0|1|b.0.1 E independent variable h
1.1|1|c.5.0 H axes convention h
2.b|1
2.0|1|a.4.1 H catalase hydrogen peroxide l
2.1|1|t.2.0 E catalase sources h;b.0.3 H controlled variable l
2.2|1|t.0.3 H amylase digests starch h
2.3|1|b.1.1 H measuring volumes equipment l
2.4|1
2.5|1|b.1.0 H water bath controls temperature h
2.6|1|t.3.0 H buffer defined l
3.b|1
3.0|1
3.1|1|t.3.0 E buffer keeps pH constant h;b.0.3 H controlled variable h
3.2|1|t.0.2 E oxygen released by catalase h
3.3|1|b.1.0 H water bath holds temperature l
3.4|1|b.2.2 E boiled enzyme control h
3.5|1|t.3.4 E boiled enzyme control h
4.b|1
4.0|1
4.1|1|t.3.0 H buffer defined l
4.2|1
4.3|1
4.4|1
5.b|1|a.4.0 E substrate defined h
5.0|1|b.0.1 E independent variable h
5.1|2|a.5.1 E collisions with active sites h;a.4.2 E active site h
5.2|1|b.0.1 E independent variable h
5.3|1|b.0.2 E dependent variable h
5.4|1|b.0.3 E controlled variables h
5.5|1|t.3.4 E boiled enzyme control h
6.b|1|t.0.2 H oxygen measured as volume l
6.0|1
6.1|1|t.3.3 E equilibration in water bath h
6.2|1|t.6.0 E upturned cylinder set-up h
6.3|1|t.6.2 H delivery tube position l
6.4|1|t.5.3 H oxygen volume measured l
6.5|1|b.5.2 E repeats allow a mean h
6.6|1|t.3.2 E foam method h
6.7|2|t.0.5 E rate = 1/time h
6.8|1|t.6.1 E set-up contents h
7.b|1
7.0|1|c.6.1 H plateau feature l
7.1|2|a.5.1 E collisions increase rate h;a.5.0 E enzyme-substrate complex h
7.2|2|a.4.2 E active site occupied h;t.7.1 H contrast with collision rise l
7.3|2|t.7.2 E saturation at plateau h
7.4|1|t.7.2 H plateau from saturation l
7.5|1|c.10.0 E conclusion states relationship h
7.6|1|t.7.2 E plateau saturation h
8.b|1
8.0|1|a.6.0 H amylase digests starch l
8.1|2|a.4.2 E active sites bind substrate h
8.2|1|b.0.1 E independent variable h
8.3|1|t.0.5 E rate = 1/time h
8.4|1|b.0.3 E controlled variables h
8.5|1|t.3.4 E boiled enzyme control h
9.b|1|t.8.b H iodine colour change h
9.0|1|t.8.b E iodine tests for starch h
9.1|1|t.3.3 E equilibration in water bath h
9.2|1|t.9.1 E tubes prepared in step 2 h
9.3|1|t.9.0 E iodine wells ready h
9.4|1|t.8.b E iodine colour end-point h
9.5|1|b.5.2 E repeats allow a mean h
9.6|1|t.3.2 H foam measures oxygen l
9.7|1|t.9.0 H spotting tile with iodine l
10.b|1
10.0|1|t.9.4 E end-point of starch digestion h
10.1|1|c.6.3 E directly proportional line h
10.2|2|a.4.2 E active sites bind substrate h
10.3|2|t.7.3 H limiting factor l
10.4|1|t.10.1 E straight-line graph h
11.b|1|t.3.0 H buffers set pH h
11.0|1
11.1|2|a.4.2 E active site shape h
11.2|1|b.0.1 E independent variable h;t.3.0 E buffer holds pH h
11.3|1|b.0.2 E dependent variable h
11.4|1|b.0.3 E controlled variables h
11.5|1|t.3.4 E boiled enzyme control h
12.b|1|t.3.2 H foam traps oxygen h
12.0|1|t.3.2 E washing-up liquid forms foam h
12.1|1|t.3.3 E equilibration time h
12.2|1
12.3|1
12.4|1
12.5|1|b.5.2 H repeats and mean h
12.6|1|t.12.0 H foam set-up contents l
13.b|1|a.4.2 H active site shape h
13.0|1|c.6.1 H optimum peak l
13.1|2|a.4.3 E active site complementary to substrate h
13.2|2|a.7.5 E shape change stops fit h;a.5.0 H enzyme-substrate complexes l
13.3|2|a.1.3 E denaturation h
13.4|2|t.13.1 E optimum pH defined h
13.5|1|t.13.1 E optimum pH h
14.b|1|a.7.5 H heat denatures enzyme h
14.0|1
14.1|2|a.1.3 E denatured by heat h;a.5.1 E collisions raise rate h
14.2|1|b.0.1 E independent variable h
14.3|1|b.0.2 E dependent variable h
14.4|1|b.0.3 E controlled variables h
14.5|1|t.3.4 E boiled enzyme control h
15.b|1|t.12.b H foam method h
15.0|1|t.12.0 E pH investigation method h
15.1|1|b.5.2 H repeats and mean h
15.2|1|t.9.4 E amylase end-point timing h
15.3|1|t.12.6 E pH set-up diagram h
16.b|1
16.0|1|c.6.1 H optimum peak l
16.1|1|t.16.0 H curve shape l
16.2|2|a.5.1 E collisions raise rate h;a.5.0 H enzyme-substrate complexes l
16.3|1|t.16.2 H rise with temperature l
16.4|2|a.4.2 E active site shape h;a.1.3 E denaturation h
16.5|1|t.16.4 E denaturation explanation h
16.6|2|t.16.4 E denatured versus inactive h
16.7|1|t.16.0 E curve shape h
17.b|1|a.7.5 H denaturation h
17.0|1
17.1|1|a.4.2 E active site h
17.2|1|t.17.1 E denaturation h
17.3|1|b.0.1 E independent variable h
17.4|1|b.0.3 E controlled variables h
17.5|1|b.2.1 E control definition h
18.b|1|b.2.0 H fair test h
18.0|1
18.1|1
18.2|1|t.3.3 E equilibration h
18.3|1|t.3.2 E foam method h
18.4|1|t.12.4 H reading foam l
18.5|1|t.17.1 H denaturation h
18.6|2|t.17.1 E denaturation permanent h
18.7|2|t.16.6 E inactive not denatured h
18.8|1|t.9.4 E iodine end-point h
19.b|1|c.0.6 E primary and secondary data h
19.0|1|c.0.6 E secondary data h
19.1|1|t.13.4 H published optima l
19.2|1|b.5.0 H reproducibility l
19.3|2|a.7.5 E denaturation by heat h
19.4|1|t.19.0 E secondary data h
20.b|1
20.0|1|t.3.2 E foam method h
20.1|1|t.6.3 H bung timing l
20.2|1|t.2.5 H water baths h
20.3|1|t.3.3 E equilibration h
21.b|1
21.0|1|t.2.1 H catalase extract batch h
21.1|1
21.2|1|t.9.3 E sampling every 30 seconds h
21.3|1|b.6.0 H equipment resolution l
21.4|1|c.9.0 E anomalous result h
21.5|1|b.1.3 H at least five values h
"""
def rid(r):
    k,rest=r.split('.',1); return pre[k]+rest
out={}
for ln in D.strip().split('\n'):
    f=ln.split('|'); iid='bio13-s3.'+f[0]; needs=[]
    if len(f)>2:
        for n in f[2].split(';'):
            w=n.split(); needs.append({"id":rid(w[0]),"strength":"essential" if w[1]=='E' else "helpful","why":' '.join(w[2:-1]),"confidence":"high" if w[-1]=='h' else "low"})
    out[iid]={"cost":int(f[1]),"needs":needs}
ids=re.findall(r'^\[([^\]]+)\]',pk,re.M)
tgt=[i for i in ids if i.startswith('bio13-s3.')]
assert list(out)==tgt,(set(tgt)^set(out))
for v in out.values():
    for n in v['needs']: assert n['id'] in ids and n['id']!=None,n
for k,v in out.items():
    assert all(n['id']!=k for n in v['needs'])
json.dump(out,open(P+'point-links/bio13-s3.json','w'),indent=0)
L=[n for v in out.values() for n in v['needs']]
print(len(out),len(L),sum(v['cost']==2 for v in out.values()),sum(n['confidence']=='low' for n in L))
