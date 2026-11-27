import json,re,sys
D='/Users/gabrielwhelan/barebones/.claude/worktrees/crunch-chem-home/drafts/crunch/chemistry/'
# pack1 table: id cost | links (e/h strength, H/L confidence); '-' prefix omitted = chem20-s1.
T1='''
0.b 1
0.0 2
0.1 2
0.2 2
0.3 1
0.4 2 | chem11-s2.8.2:h:equilibrium arrow reversible reaction:L
0.5 1
1.b 1
1.0 1 | chem21-s5.0.0:h:combustion of fuels:H
1.1 1
1.2 1 | 1.1:e:fossil fuels as long-term stores:H ; 1.0:e:combustion releases CO2:H
1.3 2 | 0.1:h:photosynthesis arrow:H ; 0.2:h:respiration arrow:H ; 0.3:h:decay arrow:H ; 0.4:h:ocean dissolving arrow:H ; 0.5:h:shells and limestone arrow:H ; 1.0:h:combustion arrow:H ; 1.1:h:fossil fuel formation arrow:H
2.b 1
2.0 1 | 1.0:h:combustion as a CO2 source:H
2.1 1 | 0.1:h:photosynthesis in growing forests:H
2.2 1 | 0.3:e:decay of dead plant material:H
2.3 1 | 2.0:e:carbon sources:H ; 2.1:e:carbon sinks:H
2.4 1 | 1.2:e:burning moves stored carbon to air:H ; 2.1:e:sinks absorbing carbon:H
2.5 1 | 2.4:e:fossil fuel burning outpaces sinks:H
2.6 1 | 3.3:e:greenhouse gases trap heat:H ; 2.5:h:rising CO2 level:H
2.7 1 | 2.1:h:sinks absorbing emissions:H
3.b 1
3.0 1
3.1 1 | 3.0:h:incoming solar radiation:H
3.2 1 | 3.1:e:absorbed energy warms the Earth:H
3.3 1 | 3.2:e:infrared radiation emitted:H
3.4 1 | 3.3:e:greenhouse gases absorb and re-emit IR:H
3.5 1 | 3.4:h:natural greenhouse effect gases:H
3.6 1 | 3.3:h:heat kept in by gases:H
3.7 2 | 3.0:h:incoming visible radiation:H ; 3.1:h:reflected radiation:H ; 3.2:h:IR emitted from surface:H ; 3.3:h:absorption and re-emission:H
4.b 1
4.0 1 | 3.3:e:what makes a gas a greenhouse gas:H
4.1 2 | 3.2:e:infrared radiation:H ; chem5-s1.2.0:h:covalent bonds in molecules:L
4.2 1 | 4.1:e:IR absorption needs charge change:H ; chem5-s1.3.2:h:polar bonds share electrons unequally:H
4.3 1 | 3.5:h:water vapour as natural greenhouse gas:H
4.4 1
5.b 1
5.0 1 | 3.4:e:natural greenhouse effect:H
5.1 1 | 5.0:e:temperature without greenhouse effect:H
5.2 1 | 3.4:e:natural greenhouse effect:H
5.3 1 | 3.4:h:natural greenhouse effect:H
5.4 2 | 4.0:h:which gases absorb IR:H
5.5 1 | 5.4:e:Tyndall experiments:H
6.b 1
6.0 1 | 3.4:e:natural greenhouse effect:H
6.1 1 | 6.0:e:enhanced greenhouse effect causes:H
6.2 1 | 6.0:h:extra warming from enhanced effect:H
7.b 1
7.0 1 | 4.1:h:IR absorption by molecules:L
7.1 2 | 7.0:h:gases differ in warming:H
7.2 1 | 7.1:e:global warming potential:H
7.3 1 | 7.2:e:GWP values from AR5:H
7.4 1 | 7.3:e:GWP values differ between reports:H
7.5 1 | 7.1:e:GWP meaning:H ; 8.2:h:CO2 stays for centuries:H
7.6 1 | 7.1:e:GWP of a gas:H
7.7 1 | 7.6:e:CO2 equivalent method:H ; 7.2:e:GWP of methane 28:H
8.b 1
8.0 1 | 2.0:h:cement-making releases CO2:H
8.1 1 | 2.5:h:CO2 rise to 420 ppm:H
8.2 1 | 8.1:h:extra CO2 in air:H
8.3 1 | 6.1:h:livestock and landfill activities:L
8.4 1 | 8.1:h:ppm and pre-industrial comparison:H
9.b 1
9.0 1 | 8.1:h:ppm and increase:H
9.1 1 | 9.0:e:N2O source and level:H ; 7.0:h:atmospheric lifetime:H
9.2 1 | 8.3:h:methane from cattle:H ; 9.0:h:N2O from fertilisers:H
9.3 1 | 8.0:h:CO2 from burning fuels:H
10.b 1
10.0 1
10.1 1 | 10.0:e:NO formation:H
10.2 1 | 10.0:e:NOx definition:H ; 3.5:h:ozone as greenhouse gas:H
10.3 1 | 10.0:e:NO2 as NOx:H
10.4 1 | 10.0:e:NOx:H ; 9.0:e:N2O from fertilisers:H
10.5 1
10.6 1 | 10.5:e:sulfur oxides:H ; 3.1:h:sunlight reflected:H
10.7 1 | 10.5:e:sulfur oxides:H ; 10.3:h:acid rain:H
11.b 1
11.0 1 | 4.4:h:water vapour set by temperature:H
11.1 1 | 11.0:e:short stay of water vapour:H ; 7.1:e:GWP:H
11.2 2 | 11.0:e:water vapour concentration:H ; 3.3:h:trapping heat:H
11.3 1 | 11.2:h:water vapour feedback:H
12.b 1
12.0 1 | 8.1:h:CO2 level in ppm:H
12.1 1 | 2.3:h:pre-industrial CO2 level:H
12.2 1 | 12.1:e:ice core CO2 range:H
12.3 1 | 6.2:h:global warming:H
12.4 1 | 6.2:h:effects of warming:H
12.5 1 | 12.4:h:melting ice:H
12.6 1 | 12.3:e:observed warming:H ; 6.0:h:human emissions:H
12.7 1 | 12.6:h:model evidence for human cause:H
13.b 1
13.0 1 | 6.2:e:global warming:H ; 12.5:h:sea level rise:H
13.1 1 | 11.3:e:warmer air holds more water vapour:H
13.2 1 | 13.1:h:more rainfall:H
13.3 1 | 13.0:h:effects of warming:H
14.b 1
14.0 1 | 0.4:h:oceans as a carbon store:H
14.1 2 | 0.4:e:CO2 dissolving in water:H ; chem11-s2.11.0:h:pH and H+ concentration:H
14.2 1 | 14.1:e:pH falls as CO2 dissolves:H ; chem11-s2.11.0:h:pH scale:H
14.3 1 | 14.2:e:pH fall of oceans:H
14.4 1 | 14.1:e:extra H+ in ocean:H ; chem11-s2.3.1:e:carbonate accepts a proton:H ; 0.5:h:shell building with carbonate:H
14.5 1 | 14.1:e:dissolved CO2 and H2CO3:H ; 0.5:h:calcium carbonate shells:H
15.b 1
15.0 1 | 6.1:h:fossil fuel burning:H
15.1 1 | 6.1:h:transport emissions:H
15.2 1 | 9.0:h:N2O from fertilisers:H
15.3 1 | 8.3:h:methane from livestock:H
15.4 1 | 2.1:e:carbon sinks:H ; 2.2:h:waterlogged peatlands store carbon:H
16.b 1
16.0 1 | 8.3:h:methane from landfill:H ; 7.2:h:methane GWP higher than CO2:H
16.1 2
16.2 1 | 10.3:e:NOx acid rain:H ; 10.7:e:sulfur oxides acid rain:H
16.3 1 | 6.2:h:rise in global temperature:H
16.4 1 | 16.3:h:emission targets:H
16.5 1 | 7.6:e:CO2 equivalent:H
'''
T2='''
0.b
0.0
0.1
0.2
0.3 | chem23-s1.2.0:h:anaerobic decomposition makes methane:H
0.4
0.5
1.b
1.0
1.1 | chem23-s1.1.0:h:fossil fuel formation:L
1.2
1.3
2.b
2.0
2.1
2.2
2.3
2.4
2.5
2.6
2.7
3.b
3.0
3.1
3.2
3.3
3.4
3.5
3.6
3.7
4.b
4.0
4.1
4.2
4.3
4.4
5.b
5.0
5.1
5.2
5.3
5.4
5.5
6.b
6.0
6.1
6.2
7.b
7.0
7.1
7.2
7.3
7.4
7.5
7.6
7.7
8.b
8.0
8.1
8.2
8.3 | chem23-s1.2.1:h:methane sources landfill slurry cattle:H
8.4
9.b
9.0
9.1
9.2
9.3
10.b
10.0
10.1
10.2
10.3
10.4
10.5
10.6
10.7
11.b
11.0
11.1
11.2
11.3
12.b
12.0
12.1
12.2
12.3
12.4
12.5
12.6
12.7
13.b
13.0
13.1
13.2
13.3
14.b
14.0
14.1
14.2
14.3
14.4
14.5
15.b
15.0
15.1
15.2
15.3 | chem23-s1.2.2:h:biogas from anaerobic digestion:H
15.4
16.b
16.0
16.1
16.2 | chem23-s1.12.2:h:catalytic converters:L
16.3
16.4
16.5
'''
def full(i): return i if i.startswith('chem') else 'chem20-s'+i if False else ('chem20-s1.'+i if re.match(r'^\d+\.',i) else i)
def links(s,pk):
    out=[]
    for l in s.split(';'):
        l=l.strip()
        if not l: continue
        i,st,why,c=l.split(':')
        out.append({"id":full(i),"strength":"essential" if st=='e' else "helpful","why":why,"confidence":"high" if c=='H' else "low"})
    return out
for name,T,pk in (('t1g1',T1,1),('t1g2',T2,2)):
    pack=open(D+'packs/chem20-s1.%s.txt'%name).read()
    allids=set(re.findall(r'^\[([^\]]+)\]',pack,re.M))
    tgt=re.findall(r'^\[(chem20-s1\.[^\]]+)\]',pack,re.M)
    res={};
    for line in T.strip().split('\n'):
        head,_,rest=line.partition('|')
        p=head.split(); i='chem20-s1.'+p[0]
        assert i not in res,i
        d={}
        if pk==1: d['cost']=int(p[1])
        d['needs']=links(rest,pk)
        res[i]=d
    assert list(res)==tgt,(set(tgt)^set(res))
    n=0;lo=0;c2=0
    for i,d in res.items():
        for x in d['needs']:
            assert x['id'] in allids and x['id']!=i,(i,x['id']); n+=1; lo+=x['confidence']=='low'
        c2+=d.get('cost')==2
    json.dump(res,open(D+'point-links/chem20-s1.%s.json'%name,'w'),ensure_ascii=False,indent=1)
    json.load(open(D+'point-links/chem20-s1.%s.json'%name))
    print(name,len(res),n,c2 if pk==1 else '-',lo)
