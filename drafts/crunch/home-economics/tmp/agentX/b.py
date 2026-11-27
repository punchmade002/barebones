import json,re
D='/Users/gabrielwhelan/barebones/.claude/worktrees/crunch-chem-home/drafts/crunch/home-economics/'
def L(i,s,w,c='high'): return (i,s,w,c)
H,E='helpful','essential'
# each: id -> (cost, [links])
P={}
P['hom-lipids-s5.t1g1']='''
0.b 1
0.0 1 hom-lipids-s5.4.0 H more energy per gram
0.1 1
0.2 1
0.3 1
0.4 1
1.b 1
1.0 2 hom-vitamins-minerals-s1.1.0 H fat-soluble vitamins absorbed with fat
1.1 1 hom-lipids-s1.3.0 H essential fatty acids
1.2 1 hom-lipids-s2.0.3 H phospholipids and sterols low
1.3 1
1.4 1 hom-lipids-s2.0.4 E lipase digests triglycerides
2.b 1
2.0 2 hom-lipids-s2.0.3 H cholesterol as a sterol low
2.1 1
2.2 1 hom-lipids-s1.5.3 H saturated fat raises LDL
2.3 2
2.4 1 hom-vitamins-minerals-s1.4.0 H vitamin D formed in skin
2.5 1 hom-lipids-s1.5.1 E LDL deposits narrow arteries
2.6 2 hom-lipids-s1.5.4 H unsaturated fat lowers LDL
2.7 1
3.b 1
3.0 1 hom-lipids-s5.0.1 E excess energy stored as adipose
3.1 1 hom-lipids-s1.5.1 E LDL narrows arteries
3.2 1
3.3 1 hom-lipids-s5.2.5 H cholesterol builds gallstones
3.4 1
3.5 2
3.6 2
3.7 2
4.b 1
4.0 1
4.1 2
4.2 1 hom-lipids-s5.4.0 E fat energy per gram
4.3 1 hom-lipids-s5.4.2 E energy calculation method
4.4 2
4.5 1 hom-lipids-s1.2.2 H trans fatty acids low
'''
P['hom-home-services-s3.t1g1']='''
0.b 1
0.0 1
0.1 1
0.2 1
0.3 1 hom-home-services-s3.0.0 E voltage|hom-home-services-s3.0.1 E current|hom-home-services-s3.0.2 E wattage
0.4 1 hom-home-services-s3.0.3 E W = V x A
0.5 1 hom-home-services-s3.0.2 H wattage as rate of energy use
0.6 1 hom-home-services-s3.0.0 H supply voltage 230 V
0.7 2 hom-home-services-s3.0.3 E current from wattage|hom-home-services-s3.1.2 H fuse in plug low
1.b 1
1.0 2
1.1 1 hom-home-services-s3.1.0 E live neutral earth wires
1.2 1 hom-home-services-s3.0.7 H fuse matched to wattage
1.3 1
2.b 1
2.0 1 hom-home-services-s1.1.0 H turbine drives generator
2.1 1 hom-home-services-s1.1.2 H high voltage low current
2.2 1 hom-home-services-s3.2.1 H voltage changes for transmission
2.3 1 hom-home-services-s3.0.0 H 230 V supply
2.4 1 hom-home-services-s1.1.4 H mains cable and meter
2.5 1 hom-home-services-s3.5.1 H MCB circuit breaker low
2.6 1 hom-home-services-s3.2.5 H consumer unit
2.7 2 hom-home-services-s3.2.1 H step-up transformer
3.b 1
3.0 1 hom-home-services-s3.0.2 E kilowatt as power unit
3.1 1 hom-home-services-s3.3.0 E kilowatt-hour
3.2 1 hom-home-services-s3.3.1 E energy in kWh
3.3 1 hom-home-services-s3.3.1 E kWh per appliance
3.4 1 hom-home-services-s3.3.0 H units are kWh
3.5 1
3.6 1 hom-home-services-s3.3.1 H units in kWh
3.7 1
4.b 1
4.0 1
4.1 1 hom-home-services-s3.4.0 H comparing with single rate
4.2 1 hom-home-services-s3.4.1 H time-of-use pricing
5.b 1
5.0 1 hom-home-services-s3.0.7 H fuse rating
5.1 1 hom-home-services-s3.5.0 H overcurrent protection
5.2 1 hom-home-services-s3.1.0 E live and neutral wires
5.3 2 hom-home-services-s3.5.2 E RCD operation
5.4 1 hom-home-services-s3.1.0 E earth wire
5.5 1 hom-home-services-s3.5.4 E earth fault path
5.6 1 hom-home-services-s3.5.4 H earth wire purpose
5.7 1 hom-home-services-s3.2.6 H separate circuits
6.b 1
6.0 2 hom-home-services-s3.2.5 H consumer unit
6.1 1 hom-home-services-s3.6.0 E ring loop
6.2 1 hom-home-services-s3.6.0 E ring circuit
6.3 1 hom-home-services-s3.6.0 H ring circuit
6.4 1 hom-home-services-s3.6.0 E ring circuit
6.5 1 hom-home-services-s3.6.0 H ring loop|hom-home-services-s3.5.1 H MCB
6.6 2 hom-home-services-s3.6.0 E ring layout
7.b 1
7.0 1
7.1 1
7.2 1
7.3 1
7.4 1
7.5 1 hom-home-services-s3.0.7 H correct fuse
7.6 1
7.7 1 hom-home-services-s3.5.3 H RCD protection
7.8 1
8.b 1
8.0 1 hom-home-services-s1.3.4 H odorant added to gas
8.1 1
8.2 1 hom-home-services-s1.0.0 H combustion needs oxygen
8.3 1 hom-home-services-s3.8.2 H carbon monoxide hazard
8.4 1 hom-home-services-s1.0.0 H combustion needs air
8.5 1
8.6 1
9.b 1
9.0 2
9.1 1
9.2 2 hom-home-services-s3.4.1 H night-rate tariff
9.3 1
9.4 1 hom-home-services-s3.6.0 H ring circuit sockets
9.5 1
'''
P['hom-meal-planning-s1.t1g1']='''
0.b 1
0.0 1
0.1 1
0.2 1
0.3 1
0.4 1 hom-meal-planning-s1.0.3 H eating patterns
0.5 1
0.6 1
1.b 1
1.0 1
1.1 2
1.2 1 hom-meal-planning-s1.1.1 H health status conditions
1.3 2
1.4 1 hom-consumer-rights-s1.0.0 H income sets spending limit
1.5 1 hom-meal-planning-s1.1.4 H finance and income
1.6 2 hom-consumer-rights-s1.3.6 H advertising to children low
2.b 1
2.0 1 hom-meal-planning-s1.0.3 H eating patterns
2.1 1
2.2 1 hom-meal-planning-s1.1.0 E nutritional awareness
2.3 1
3.b 1
3.0 1 hom-energy-nutrition-s5.1.1 H rice and pasta replacing potatoes
3.1 2 hom-energy-nutrition-s5.1.4 H convenience foods
3.2 1 hom-energy-nutrition-s5.1.6 H eating out increase
3.3 1 hom-energy-nutrition-s5.2.1 H main meal evening
3.4 1 hom-energy-nutrition-s5.1.6 H new dishes from abroad
3.5 1 hom-energy-nutrition-s5.1.4 H microwave convenience cooking
3.6 1 hom-energy-nutrition-s5.1.7 H health information
3.7 1
4.b 1
4.0 2
4.1 1
4.2 1
4.3 1 hom-meal-planning-s1.4.2 E food neophobia
5.b 1
5.0 1 hom-meal-planning-s1.1.6 H marketing and advertising
5.1 1 hom-meal-planning-s1.1.4 H finance
5.2 1
5.3 1 hom-meal-planning-s1.0.6 H early exposure and preferences
5.4 2
5.5 1 hom-meal-planning-s1.0.2 H religion restrictions|hom-meal-planning-s1.0.0 H culture
6.b 1
6.0 1
6.1 1
6.2 1 hom-meal-planning-s1.1.3 H availability
6.3 1 hom-meal-planning-s1.1.4 H finance
7.b 1
7.0 1
7.1 1
7.2 1
7.3 1 hom-energy-nutrition-s5.3.1 H fruit and vegetable guideline
7.4 1
8.b 1
8.0 1
8.1 1
'''
for name,txt in P.items():
    pk=open(D+'packs/'+name+'.txt').read()
    ids=set(re.findall(r'^\[([^\]]+)\]',pk,re.M))
    sub=re.search(r'TARGET (\S+):',pk).group(1)
    tg=re.findall(r'^\[('+re.escape(sub)+r'\.[^\]]+)\]',pk,re.M)
    out={}
    for ln in txt.strip().splitlines():
        p=ln.split(' ',2); k=sub+'.'+p[0]; cost=int(p[1]); needs=[]
        if len(p)>2:
            for part in p[2].split('|'):
                t=part.split(' ',2)
                m=t[2]; conf='high'
                if m.endswith(' low'): m=m[:-4]; conf='low'
                needs.append({'id':t[0],'strength':{'H':'helpful','E':'essential'}[t[1]],'why':m,'confidence':conf})
        assert k not in out; out[k]={'cost':cost,'needs':needs}
    assert list(out)==tg,(name,set(tg)^set(out))
    for v in out.values():
        for n in v['needs']: assert n['id'] in ids and n['id'] not in out or n['id'] in ids
    for k,v in out.items(): assert all(n['id']!=k for n in v['needs'])
    json.dump(out,open(D+'point-links/'+name+'.json','w'),indent=1)
    print(name,len(out),sum(len(v['needs']) for v in out.values()),sum(v['cost']==2 for v in out.values()),sum(n['confidence']=='low' for v in out.values() for n in v['needs']))
