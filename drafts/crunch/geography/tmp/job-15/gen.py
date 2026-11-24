import json,re
P='/Users/gabrielwhelan/barebones/drafts/crunch/geography/'
S='geo-economic-environment-s3.'
cnt=[4,3,2,4,6,5,4,3,4,6,4,4,3,3,3,4,1,4,3,2,3,5,4,5,3]
ids=[]
for s,c in enumerate(cnt):
    ids.append(f'{S}{s}.b'); ids+= [f'{S}{s}.{i}' for i in range(c)]
cost2={'2.0','4.0','5.0','6.1','8.1','9.0','9.1','9.2','9.5','11.0','11.1','11.2','13.2','14.1','15.0','15.1','22.0'}
H,E='helpful','essential'
L1={ # id: (target, strength, why, conf)
'0.3':('s2:geo-economic-environment-s2.4.b',H,'acid rain as transboundary example','high'),
'2.1':(S+'2.0',E,'builds on natural greenhouse effect','high'),
'3.0':(S+'2.0',H,'uses term greenhouse gas','high'),
'3.1':(S+'2.0',H,'uses term greenhouse gas','high'),
'3.2':(S+'2.0',H,'uses term greenhouse gas','high'),
'4.0':(S+'2.1',H,'CO2 rise is enhanced greenhouse effect','low'),
'5.0':(S+'4.4',H,'sea level rise evidence','high'),
'5.2':(S+'4.5',H,'glacier retreat evidence','high'),
'7.0':(S+'3.1',H,'methane source from cattle','high'),
'7.2':(S+'7.0',H,'farming dominates emissions','low'),
'8.1':(S+'8.0',H,'builds on UNFCCC','low'),
'8.3':(S+'8.0',H,'COP meets under UNFCCC','high'),
'9.0':(S+'3.0',H,'CO2 emissions being priced','low'),
'9.3':(S+'9.2',H,'sectoral ceilings implement the Act','high'),
'10.1':(S+'3.0',H,'burning fossil fuels gives CO2','high'),
'10.2':(S+'3.1',H,'landfill gives methane','high'),
'10.3':(S+'3.0',H,'burning fossil fuels gives CO2','high'),
'11.0':(S+'1.1',H,'uses diffuse runoff from farms','low'),
'11.1':(S+'11.0',E,'nutrients from cause feed algae','high'),
'11.2':(S+'11.1',E,'algal bloom dying stage','high'),
'11.3':(S+'11.1',H,'algal bloom effects','high'),
'12.0':(S+'11.2',H,'fish kill','high'),
'12.1':(S+'11.0',H,'nitrates from fertiliser','low'),
'12.2':(S+'11.1',H,'algal growth from nutrients','high'),
'13.1':(S+'11.0',H,'fertiliser and slurry runoff','high'),
'13.2':(S+'11.0',H,'nitrogen pollution of water','low'),
'14.1':(S+'11.1',E,'eutrophication process','high'),
'15.0':(S+'11.0',H,'slurry washing into rivers','high'),
'15.1':(S+'15.0',H,'builds on Nitrates Action Programme','high'),
'18.2':(S+'17.3',H,'double-hulled tankers','low'),
'20.2':(S+'17.3',H,'double-hulled tankers','high'),
'21.2':(S+'21.1',H,'plastics persist as microplastics','low'),
'21.3':(S+'21.1',H,'plastic breakdown and persistence','low'),
'21.4':(S+'21.1',E,'uses term microplastics','high'),
'23.0':(S+'3.3',H,'CFCs also greenhouse gases','low'),
'23.1':(S+'23.0',H,'ozone destruction by CFCs','high'),
'23.2':(S+'23.0',H,'ozone absorbs ultraviolet radiation','high'),
'23.3':(S+'23.0',H,'phasing out CFCs','high'),
'23.4':(S+'23.3',H,'recovery follows CFC phase-out','high'),
'24.0':('s2:geo-economic-environment-s2.8.3',H,'smoky coal ban zones','low'),
'24.2':('s2:geo-economic-environment-s2.10.3',H,'wind farm visual impact','low'),
}
def mk(t,full):
    tid=t if t.startswith('geo-') else None
    return t
def conv(t):
    return t[3:] if t.startswith('s2:') else t
# fix 3.3 -> real item id
L1['23.0']=(S+'3.3',H,'CFCs also greenhouse gases','low')
L2={
'3.0':('geo-rocks-weathering-s2.7.1',H,'cement heating releases CO2','high'),
'21.4':(S+'3.1',H,'landfill gives methane','high'),
'24.1':('geo-rocks-weathering-s2.3.2',H,'Avoca acid mine drainage','high'),
'24.2':('geo-rocks-weathering-s2.9.1',H,'quarry noise and traffic','low'),
}
# 3.3 etc: refs written as S+'x.y' need full ids; patch ones lacking item index
fix={S+'2.1':S+'2.1',}
def resolve(t):
    t=conv(t)
    if t.count('.')==1 and t.startswith(S[:-1]): pass
    return t
def build(L,cost):
    out={}
    for i in ids:
        k=i[len(S):]
        d={}
        if cost: d['cost']=2 if k in cost2 else 1
        n=[]
        if k in L:
            t,s,w,c=L[k]; n.append({'id':conv(t),'strength':s,'why':w,'confidence':c})
        d['needs']=n; out[i]=d
    return out
for name,L,cost in (('t1g1',L1,True),('t1g2',L2,False)):
    o=build(L,cost)
    pack=open(P+f'packs/geo-economic-environment-s3.{name}.txt').read()
    pids=set(re.findall(r'^\[([^\]]+)\]',pack,re.M))
    tg=[l for l in pack.split('CANDIDATES')[0].splitlines() if l.startswith('[')]
    tids=[re.match(r'\[([^\]]+)\]',l).group(1) for l in tg]
    assert list(o)==tids,'ids'
    bad=[n['id'] for v in o.values() for n in v['needs'] if n['id'] not in pids]
    assert not bad,bad
    assert all(n['id']!=k for k,v in o.items() for n in v['needs'])
    json.dump(o,open(P+f'point-links/geo-economic-environment-s3.{name}.json','w'),indent=0)
    nl=sum(len(v['needs']) for v in o.values())
    lo=sum(n['confidence']=='low' for v in o.values() for n in v['needs'])
    print(name,len(o),nl,sum(v.get('cost')==2 for v in o.values()),lo)
