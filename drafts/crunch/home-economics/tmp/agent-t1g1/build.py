import json,re,sys
B='/Users/gabrielwhelan/barebones/.claude/worktrees/crunch-chem-home/drafts/crunch/home-economics/'
H,E,L='helpful','essential','low'
def n(i,s,w,c='high'): return (i,s,w,c)

# each: pack name, own prefix, spec dict {suffix: (cost, [links])}; link ids may use short prefixes via PFX
PK={}
# ---- food preservation s4
P='hom-food-preservation-s4.'; S1='hom-food-preservation-s1.'
PK['hom-food-preservation-s4.t1g1']=(P,{
'0.b':(1,[]),
'0.0':(1,[n(S1+'2.6',H,'no water stops growth')]),
'0.1':(1,[]),'0.2':(1,[]),'0.3':(1,[]),
'0.4':(1,[n(S1+'2.6',H,'moisture needed for mould growth')]),
'0.5':(2,[n(S1+'1.0',E,'enzymes cause darkening'),n(S1+'5.0',H,'blanching inactivates enzymes by heat')]),
'1.b':(1,[]),'1.0':(2,[n(P+'0.5',H,'blanching vegetables before drying')]),
'1.1':(1,[]),'1.2':(1,[]),'1.3':(1,[]),'1.4':(1,[]),'1.5':(1,[]),
'2.b':(1,[]),'2.0':(1,[]),'2.1':(1,[]),'2.2':(1,[]),'2.3':(1,[]),
'3.b':(1,[]),'3.0':(1,[]),'3.1':(1,[]),'3.2':(1,[]),'3.3':(1,[]),
'3.4':(1,[n(S1+'5.2',H,'salt removes water','low')]),
'4.b':(1,[n(P+'4.3',H,'freeze drying process')]),
'4.0':(2,[]),'4.1':(1,[]),'4.2':(1,[]),
'4.3':(2,[]),
'4.4':(1,[n(P+'4.3',E,'continues AFD steps')]),
'4.5':(2,[n(P+'4.3',H,'AFD process')]),
'4.6':(2,[n(P+'4.3',H,'AFD freezing and sublimation')]),
'4.7':(1,[n(P+'4.3',H,'AFD equipment')]),
'4.8':(2,[n(P+'4.3',E,'AFD stages to draw')]),
'5.b':(1,[]),'5.0':(1,[]),
'5.1':(1,[n(S1+'1.3',H,'oxidation destroys vitamins')]),
'5.2':(2,[n(P+'0.5',H,'blanching and lemon juice stop browning')]),
'5.3':(1,[]),'5.4':(1,[]),'5.5':(1,[]),'5.6':(1,[]),
'5.7':(2,[]),'5.8':(2,[]),
})
# ---- home services s2
P='hom-home-services-s2.';A='hom-home-services-s1.';F='hom-home-services-s5.';I='hom-home-services-s6.'
x=lambda k:(1,[])
PK['hom-home-services-s2.t1g1']=(P,{
'0.b':(1,[n(F+'0.b',H,'conduction, convection, radiation')]),
'0.0':(1,[n(F+'0.0',H,'conduction through solids')]),
'0.1':(1,[n(F+'0.1',H,'convection currents')]),
'0.2':(1,[]),
'0.3':(1,[n(F+'0.1',H,'warm air rises','low')]),
'0.4':(1,[n(I+'3.1',H,'double glazing trapped gas')]),
'0.5':(1,[n(I+'2.2',H,'thermal bridges defined','low')]),
'0.6':(1,[n(I+'3.6',H,'lagging cylinder and pipes')]),
'0.7':(1,[n(F+'2.2',H,'timers, thermostats, radiator valves')]),
'1.b':(1,[]),
'1.0':(2,[n(F+'2.2',H,'timers, thermostats, radiator valves')]),
'1.1':(2,[]),'1.2':(2,[]),'1.3':(2,[]),'1.4':(1,[]),
'2.b':(1,[n(A+'0.0',H,'fuel combustion')]),
'2.0':(2,[n(A+'0.0',E,'combustion of a fuel')]),
'2.1':(1,[n(P+'2.0',E,'complete combustion contrasted')]),
'2.2':(2,[n(P+'2.1',E,'incomplete combustion makes CO')]),
'2.3':(1,[n(P+'2.2',H,'CO is odourless and poisonous')]),
'2.4':(1,[n(P+'2.0',H,'water vapour from combustion')]),
'2.5':(2,[n(P+'2.1',H,'incomplete combustion products'),n(P+'3.0',H,'effects of CO2'),n(P+'3.1',H,'effects of SO2')]),
'3.b':(1,[]),'3.0':(2,[]),'3.1':(2,[]),'3.2':(1,[]),
'3.3':(1,[n(P+'2.1',H,'incomplete combustion gives smoke')]),
'3.4':(2,[n(P+'3.0',H,'carbon dioxide emissions'),n(P+'3.3',H,'smoke emissions')]),
'3.5':(1,[n(A+'6.4',H,'wood as renewable biomass')]),
'4.b':(1,[]),
'4.0':(1,[n(P+'0.2',H,'draughts and air leakage')]),
'4.1':(1,[n(P+'0.2',H,'air leakage gaps')]),
'4.2':(1,[n(F+'2.2',H,'timers and thermostats')]),
'4.3':(1,[]),
'4.4':(1,[n(P+'1.1',H,'hot water wastes recorded')]),
'4.5':(1,[n(P+'1.3',H,'cooking energy wastes')]),
'4.6':(1,[]),
'4.7':(1,[n(A+'3.4',H,'gas odorant for leaks','low')]),
'5.b':(1,[n(P+'0.b',H,'routes of heat loss')]),
'5.0':(2,[n(I+'0.1',H,'insulating materials trap air')]),
'5.1':(2,[n(I+'3.1',H,'double glazing')]),
'5.2':(1,[n(I+'3.5',H,'draught excluders')]),
'5.3':(1,[n(I+'3.7',H,'airtight house needs ventilation')]),
'5.4':(2,[n(I+'6.5.4'.replace('6.5.4','5.4'),H,'ranking improvements by cost'),n(A+'10.6',H,'SEAI grants')]),
'6.b':(1,[]),
'6.0':(2,[n(F+'5.0',H,'programmer timer'),n(F+'4.4',H,'thermostatic radiator valve')]),
'6.1':(1,[n(F+'11.3',H,'condensing boiler'),n(P+'2.1',H,'complete combustion kept by servicing')]),
'6.2':(1,[n(F+'6.2',H,'background heating')]),
'6.3':(2,[n(I+'3.6',H,'lagging cylinder and pipes')]),
'6.4':(1,[]),
'6.5':(2,[n(F+'7.3',H,'heat pump'),n(A+'8.0',H,'solar thermal collectors')]),
'7.b':(1,[]),'7.0':(1,[]),'7.1':(1,[]),'7.2':(1,[]),'7.3':(1,[]),
'8.b':(1,[]),'8.0':(1,[]),
'8.1':(2,[n(P+'3.4',H,'fuels ranked by emissions')]),
'8.2':(1,[n(P+'2.3',H,'CO alarm and servicing')]),
'8.3':(1,[n(P+'3.3',H,'smoke and particles')]),
'8.4':(1,[n(A+'8.1',H,'PV panels'),n(F+'7.3',H,'heat pumps')]),
'9.b':(1,[]),'9.0':(1,[]),
'9.1':(1,[n(A+'8.3',H,'passive solar design')]),
'9.2':(2,[n(P+'5.3',H,'controlled ventilation')]),
'9.3':(1,[]),
'9.4':(1,[n(P+'6.0',H,'zoned heating controls')]),
'9.5':(1,[]),
'10.b':(1,[]),'10.0':(1,[]),'10.1':(2,[]),'10.2':(2,[]),'10.3':(1,[]),'10.4':(2,[]),
})
# ---- fruit veg s3
P='hom-fruit-vegetables-s3.';C1='hom-cooking-methods-s1.';V='hom-vitamins-minerals-s2.';C2='hom-cooking-methods-s2.';CH='hom-carbohydrates-s4.';FP='hom-food-preservation-s2.'
PK['hom-fruit-vegetables-s3.t1g1']=(P,{
'0.b':(1,[n(V+'0.0',H,'water-soluble vitamins')]),
'0.0':(2,[n(V+'0.0',H,'water-soluble vitamins dissolve')]),
'0.1':(1,[n(V+'5.2',H,'vitamin C instability')]),
'0.2':(1,[]),'0.3':(1,[]),
'0.4':(2,[n(C1+'5.1',H,'oxidation and heat destroy vitamin C')]),
'1.b':(1,[]),
'1.0':(1,[n(P+'0.1',H,'vitamin C is least stable')]),
'1.1':(1,[]),
'1.2':(1,[n(V+'5.3',H,'oxidase destroys vitamin C')]),
'1.3':(1,[n(V+'5.3',H,'oxidase destroys vitamin C')]),
'1.4':(1,[n(C1+'5.4',H,'small pieces expose surface')]),
'1.5':(1,[]),
'1.6':(1,[n(P+'0.0',H,'vitamins dissolve in water')]),
'1.7':(1,[]),
'2.b':(1,[n(P+'0.4',H,'three routes of nutrient loss')]),
'2.0':(1,[]),'2.1':(2,[]),
'2.2':(2,[n(C2+'5.2',H,'microwave cooking'),n(C2+'2.3.3'.replace('2.3.3','3.3'),H,'steaming transfers heat')]),
'2.3':(1,[n(P+'0.3',H,'carotene fat-soluble')]),
'2.4':(1,[n(P+'2.2',H,'microwaving as nutrient-saving method')]),
'2.5':(1,[n(V+'5.2',H,'alkalis destroy vitamin C')]),
'2.6':(1,[n(V+'5.4',H,'copper destroys vitamin C')]),
'2.7':(2,[n(FP+'4.2',H,'thawing and drip','low')]),
'3.b':(1,[]),'3.0':(1,[n(P+'0.0',H,'vitamins lost to heat and water')]),
'3.1':(1,[]),
'3.2':(1,[n(P+'0.3',H,'carotene stable to heat')]),
'3.3':(1,[]),
'3.4':(2,[n(CH+'1.0',H,'starch gelatinisation')]),
'3.5':(1,[n(C2+'0.5',H,'cooking destroys enzymes','low')]),
'4.b':(1,[]),
'4.0':(2,[n(C1+'0.5',H,'chlorophyll colour change')]),
'4.1':(1,[n(P+'2.5',H,'bicarbonate destroys vitamins')]),
'4.2':(1,[]),'4.3':(2,[]),
'5.b':(1,[]),
'5.0':(1,[n(C1+'0.6',H,'softening cellulose and pectin')]),
'5.1':(1,[]),'5.2':(1,[]),'5.3':(1,[]),
'5.4':(1,[n(CH+'5.0',H,'caramelisation of sugar')]),
'6.b':(1,[n(FP+'2.2.b'.replace('2.2.b','2.b'),H,'blanching before freezing')]),
'6.0':(1,[]),
'6.1':(1,[n(C1+'2.6',H,'heat inactivates the enzyme')]),
'6.2':(1,[]),'6.3':(1,[]),
'7.b':(1,[]),
'7.0':(1,[n(P+'0.1',H,'vitamin C is fragile')]),
'7.1':(1,[]),
'7.2':(1,[n(P+'1.3',H,'sharp knife limits oxidase')]),
'7.3':(1,[n(P+'2.1',H,'minimum water, lid, short time')]),
'7.4':(1,[n(P+'2.6',H,'copper destroys vitamin C')]),
'7.5':(2,[n(C1+'2.5',H,'acid slows enzymic browning')]),
})
for name,(P,spec) in PK.items():
    txt=open(B+'packs/'+name+'.txt').read()
    lines=txt.split('\n')
    # targets: items between TARGET and first blank line
    tl=[];ids=set()
    sec=None
    for l in lines:
        if l.startswith('TARGET'): sec='T'
        elif l.startswith('CANDIDATES'): sec='C'
        m=re.match(r'\[([^\]]+)\]',l)
        if m:
            ids.add(m.group(1))
            if sec=='T': tl.append(m.group(1))
    exp=[P+k for k in spec]
    assert sorted(exp)==sorted(tl) and len(set(exp))==len(exp),(name,set(tl)^set(exp))
    out={}
    for t in tl:
        c,ls=spec[t[len(P):]]
        for l in ls: assert l[0] in ids and l[0]!=t,(t,l)
        out[t]={'cost':c,'needs':[{'id':a,'strength':b,'why':w,'confidence':cf} for a,b,w,cf in ls]}
        out[t]={'cost':c,'needs':[{'id':a,'strength':(L and b),'why':w,'confidence':('low' if cf==L else cf)} for a,b,w,cf in ls]}
    json.dump(out,open(B+'point-links/'+name+'.json','w'),indent=1)
    j=json.load(open(B+'point-links/'+name+'.json'))
    nl=sum(len(v['needs']) for v in j.values())
    print(name,len(j),nl,sum(v['cost']==2 for v in j.values()),sum(l['confidence']=='low' for v in j.values() for l in v['needs']))
