import json,re,sys
D='/Users/gabrielwhelan/barebones/.claude/worktrees/crunch-chem-home/drafts/crunch/home-economics/'
def L(i,s,w,c='high'): return {"id":i,"strength":s,"why":w,"confidence":c}
H,E='helpful','essential'
def run(name,P,spec):
    txt=open(D+'packs/'+name+'.txt').read()
    tgt=txt.split('CANDIDATES')[0]
    tids=re.findall(r'^\[([^\]]+)\]',tgt,re.M)
    allids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
    out={}
    for t in tids:
        k=t[len(P):]
        cost,needs=spec[k]   # KeyError if any target unjudged
        out[t]={"cost":cost,"needs":needs}
    assert set(spec)=={t[len(P):] for t in tids},(set(spec)^{t[len(P):] for t in tids})
    for t,v in out.items():
        for n in v['needs']: assert n['id'] in allids and n['id']!=t,(t,n)
    json.dump(out,open(D+'point-links/'+name+'.json','w'),indent=1)
    nl=sum(len(v['needs']) for v in out.values())
    print(name,len(out),nl,sum(v['cost']==2 for v in out.values()),sum(n['confidence']=='low' for v in out.values() for n in v['needs']))
F='hom-family-caring-s4.'
f4=lambda k:F+k
fam={
'0.b':(1,[]),'0.0':(1,[]),'0.1':(2,[]),'0.2':(1,[]),'0.3':(1,[]),
'0.4':(1,[L('hom-family-caring-s1.0.4',H,'later life stage care','low')]),'0.5':(1,[]),
'1.b':(1,[]),'1.0':(1,[]),'1.1':(2,[]),'1.2':(2,[]),'1.3':(1,[]),
'1.4':(1,[L(f4('4.4'),H,'State assistance and allowances')]),
'1.5':(1,[]),'1.6':(1,[]),'1.7':(1,[]),
'2.b':(1,[]),'2.0':(1,[]),'2.1':(1,[]),'2.2':(1,[]),'2.3':(1,[]),'2.4':(1,[]),
'3.b':(1,[]),
'3.0':(1,[L(f4('4.4'),H,'State financial support payments')]),
'3.1':(1,[L(f4('4.0'),H,'HSE therapy and assessment services')]),
'3.2':(1,[]),
'3.3':(1,[L(f4('1.6'),H,'siblings need attention')]),
'3.4':(1,[]),
'4.b':(1,[]),'4.0':(2,[]),'4.1':(2,[]),'4.2':(1,[]),
'4.3':(2,[L(f4('4.2'),E,'coordinates education services')]),
'4.4':(2,[]),
'4.5':(1,[L(f4('4.4'),H,'Carer\'s Allowance, carer payments')]),
'4.6':(1,[L(f4('1.1'),H,'adapting the home ramps')]),
'5.b':(1,[]),
'5.0':(1,[L(f4('4.0'),H,'statutory services gaps')]),
'5.1':(2,[]),
'5.2':(1,[L(f4('5.1'),E,'Rehab Group training arm')]),
'5.3':(1,[L(f4('5.1'),E,'Rehab Group work funded')]),
'5.4':(2,[]),'5.5':(2,[]),
'5.6':(1,[L(f4('5.0'),H,'voluntary services roles')]),
'6.b':(1,[]),
'6.0':(1,[L(f4('0.0'),H,'physical needs described')]),
'6.1':(2,[L(f4('1.b'),H,'family responses listed')]),
'6.2':(1,[L(f4('4.0'),H,'HSE services')]),
'6.3':(1,[L(f4('5.0'),H,'voluntary services offered')]),
'6.4':(1,[L(f4('2.b'),H,'family difficulties')]),
}
run('hom-family-caring-s4.t1g1',F,fam)
S='hom-sociological-concepts-s5.'
s5=lambda k:S+k
soc={
'0.b':(1,[]),'0.0':(1,[]),'0.1':(1,[]),'0.2':(1,[]),
'0.3':(1,[L('hom-sociological-concepts-s4.0.0',H,'uses institutions, norms, values')]),
'1.b':(1,[]),
'1.0':(2,[L('hom-sociological-concepts-s1.4.5',H,'values change over time')]),
'1.1':(1,[]),'1.2':(1,[]),'1.3':(1,[]),
'1.4':(1,[L('hom-sociological-concepts-s4.2.4',H,'social mobility through education')]),
'1.5':(2,[]),
'1.6':(2,[L('hom-sociological-concepts-s1.1.0',H,'uses culture')]),
'1.7':(2,[]),
'2.b':(1,[]),'2.0':(2,[]),'2.1':(1,[]),
'2.2':(1,[L(s5('2.1'),H,'same-sex marriage replaced civil partnership')]),
'2.3':(1,[]),
'3.b':(1,[]),'3.0':(1,[]),
'3.1':(1,[L('hom-sociological-concepts-s4.5.4',H,'economy shapes family','low')]),
'3.2':(1,[]),
'3.3':(1,[L('hom-sociological-concepts-s4.6.6',H,'State supports family economically')]),
'4.b':(1,[L(s5('0.3'),E,'cultural lag')]),
'4.0':(1,[]),'4.1':(1,[]),'4.2':(1,[]),'4.3':(1,[]),'4.4':(1,[]),
'5.b':(1,[]),
'5.0':(1,[L(s5('1.1'),H,'greater equality for women')]),
'5.1':(1,[L(s5('1.5'),H,'demographic change')]),
'5.2':(1,[L(s5('1.0'),H,'changing attitudes and values')]),
'5.3':(1,[L(s5('1.5'),H,'ageing population demographics')]),
'5.4':(1,[L('hom-sociological-concepts-s1.4.1',H,'values behind norms','low')]),
'5.5':(2,[]),
'5.6':(1,[L('hom-sociological-concepts-s4.4.5',H,'Church influence declining','low')]),
'5.7':(1,[]),
'6.b':(1,[]),'6.0':(1,[]),
'6.1':(1,[L('hom-sociological-concepts-s4.4.1',H,'religion and moral codes','low')]),
'6.2':(1,[]),'6.3':(1,[]),
'7.b':(1,[]),
'7.0':(1,[L(s5('2.0'),H,'divorce referendum and Act')]),
'7.1':(1,[L(s5('1.1'),H,'marriage bar, equality for women')]),
'7.2':(1,[L(s5('1.6'),H,'migration')]),
'7.3':(1,[L(s5('3.2'),H,'emigration and recession')]),
'7.4':(1,[L(s5('1.2'),H,'urbanisation')]),
'8.b':(1,[]),
'8.0':(2,[L(s5('1.b'),H,'social causes','low')]),
'8.1':(1,[L(s5('1.2'),H,'urbanisation weakening extended family')]),
}
run('hom-sociological-concepts-s5.t1g1',S,soc)
C='hom-cereals-grains-s5.'
c5=lambda k:C+k
cer={
'0.b':(1,[]),
'0.0':(2,[L('hom-cereals-grains-s3.3.2',H,'rubbing in limits gluten')]),
'0.1':(2,[L('hom-cereals-grains-s4.3.1',H,'steam raising')]),
'0.2':(1,[L('hom-cereals-grains-s4.3.1',H,'steam raising')]),
'0.3':(1,[]),
'0.4':(1,[L('hom-cereals-grains-s3.2.1',H,'self-raising flour')]),
'0.5':(2,[L(c5('0.0'),H,'pastry groups matched to dishes')]),
'0.6':(1,[L(c5('1.b'),H,'shortcrust method compared','low')]),
'1.b':(1,[L('hom-cereals-grains-s3.3.2',H,'limits gluten')]),
'1.0':(2,[]),'1.1':(1,[]),
'1.2':(1,[L('hom-cereals-grains-s3.3.2',H,'fat limits gluten')]),
'1.3':(1,[]),
'1.4':(1,[L('hom-cereals-grains-s3.3.2',H,'gluten relaxes, handling develops gluten')]),
'1.5':(1,[]),
'1.6':(2,[L('hom-cereals-grains-s4.0.1',H,'browning of crust','low')]),
'1.7':(2,[]),
'2.b':(1,[L(c5('0.1'),H,'rough puff is laminated pastry')]),
'2.0':(1,[]),'2.1':(1,[]),'2.2':(1,[]),'2.3':(1,[]),'2.4':(1,[]),'2.5':(1,[]),
'2.6':(2,[L('hom-cereals-grains-s4.3.1',H,'steam as raising agent')]),
'2.7':(1,[]),
'3.b':(1,[]),
'3.0':(1,[L('hom-lipids-s4.0.0',H,'fat melting point','low')]),
'3.1':(1,[]),'3.2':(1,[]),'3.3':(1,[]),
'3.4':(1,[L('hom-cereals-grains-s3.3.2',H,'gluten development')]),
'3.5':(1,[L('hom-cereals-grains-s3.3.2',H,'gluten relaxes')]),
'3.6':(1,[]),
'3.7':(1,[L(c5('1.6'),H,'blind baking')]),
}
run('hom-cereals-grains-s5.t1g1',C,cer)
