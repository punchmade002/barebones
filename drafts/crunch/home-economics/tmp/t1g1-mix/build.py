import json,re,os
B='/Users/gabrielwhelan/barebones/.claude/worktrees/crunch-chem-home/drafts/crunch/home-economics/'
H,E='helpful','essential'
def L(i,s,w,c='high'): return {"id":i,"strength":s,"why":w,"confidence":c}
# each: id -> (cost, [links])
fs={
'0.b':(1,[]),'0.0':(2,[]),'0.1':(1,[]),'0.2':(1,[]),'0.3':(1,[]),
'1.b':(1,[]),'1.0':(1,[L('hom-food-safety-s9.4.0',H,'FSAI Act 1998 framework')]),'1.1':(1,[]),
'1.2':(1,[L('hom-food-safety-s8.3.0',H,'uses official agencies')]),'1.3':(1,[]),
'1.4':(1,[L('hom-food-safety-s7.0.0',H,'uses HACCP system')]),
'1.5':(1,[L('hom-food-safety-s8.3.0',H,'acts through official agencies')]),
'2.b':(1,[]),'2.0':(1,[]),'2.1':(1,[]),'2.2':(1,[]),
'2.3':(2,[L('hom-food-safety-s8.7.2',H,'withdrawals and recalls'),L('hom-food-safety-s8.7.1',H,'traceability')]),
'2.4':(1,[]),
'3.b':(1,[]),'3.0':(2,[]),'3.1':(1,[]),'3.2':(1,[]),'3.3':(1,[]),
'4.b':(1,[]),'4.0':(1,[]),'4.1':(1,[]),'4.2':(1,[]),'4.3':(2,[]),'4.4':(1,[]),
'4.5':(2,[L('hom-food-safety-s9.2.b',H,'labelling legislation','low')]),
'4.6':(1,[L('hom-food-safety-s8.7.3',H,'rapid alerts and recalls')]),'4.7':(1,[]),
'5.b':(1,[]),'5.0':(1,[]),'5.1':(1,[]),'5.2':(2,[]),'5.3':(1,[]),'5.4':(1,[]),
'6.b':(1,[]),'6.0':(1,[]),'6.1':(1,[]),'6.2':(1,[]),
'6.3':(1,[L('hom-food-safety-s8.7.1',H,'traceability')]),'6.4':(1,[]),
'7.b':(1,[]),'7.0':(1,[]),'7.1':(1,[]),'7.2':(1,[]),'7.3':(1,[]),
}
cs={
'0.b':(1,[L('hom-clothing-selection-s4.0.b',H,'elements of design')]),
'0.0':(1,[L('hom-clothing-selection-s4.0.2',H,'colour scheme terms')]),
'0.1':(1,[L('hom-clothing-selection-s4.0.1',H,'shape and silhouette')]),
'0.2':(1,[L('hom-clothing-selection-s4.1.b',H,'effects of line direction')]),
'0.3':(1,[L('hom-clothing-selection-s4.4.0',H,'proportion')]),
'0.4':(1,[L('hom-clothing-selection-s4.0.5',H,'pattern')]),
'0.5':(1,[L('hom-clothing-selection-s4.0.4',H,'texture')]),
'0.6':(1,[L('hom-clothing-selection-s3.4.b',H,'accessories')]),
'0.7':(2,[]),
'1.b':(1,[]),'1.0':(1,[]),'1.1':(1,[]),'1.2':(1,[]),
'1.3':(1,[L('hom-clothing-selection-s2.2.3',H,'fashion houses and designers')]),
'1.4':(2,[L('hom-clothing-selection-s3.3.2',H,'sustainability and fast fashion')]),
'1.5':(1,[]),'1.6':(1,[L('hom-clothing-selection-s3.3.5',H,'retro revival')]),
'2.b':(1,[]),'2.0':(1,[]),'2.1':(1,[]),'2.2':(2,[]),'2.3':(1,[]),'2.4':(1,[]),'2.5':(1,[]),'2.6':(1,[]),
'3.b':(1,[]),'3.0':(1,[]),'3.1':(1,[]),'3.2':(1,[L('hom-clothing-selection-s3.1.4',H,'fast fashion and sustainability')]),
'3.3':(2,[]),'3.4':(1,[L('hom-clothing-selection-s3.3.0',H,'vintage clothing')]),
'3.5':(1,[L('hom-clothing-selection-s3.0.4',H,'retro patterns','low')]),
'3.6':(1,[]),'3.7':(2,[L('hom-clothing-selection-s3.3.6',H,'upcycling')]),
'4.b':(1,[]),'4.0':(1,[]),
'4.1':(1,[L('hom-clothing-selection-s4.4.2',H,'focal point is emphasis')]),
'4.2':(1,[]),'4.3':(1,[]),'4.4':(1,[]),'4.5':(1,[]),'4.6':(1,[]),
'5.b':(1,[]),'5.0':(1,[]),
'5.1':(1,[L('hom-clothing-selection-s3.1.4',H,'fast fashion')]),
'5.2':(1,[]),'5.3':(1,[]),'5.4':(1,[]),'5.5':(1,[]),
'6.b':(1,[]),
'6.0':(2,[L('hom-clothing-selection-s4.4.5',H,'labelling elements and principles')]),
'6.1':(2,[]),
'6.2':(1,[L('hom-clothing-selection-s4.7.2',H,'aesthetic appeal')]),
}
P='hom-energy-nutrition-s2.'
es={
'0.b':(1,[]),'0.0':(2,[L('hom-energy-nutrition-s1.1.0',H,'BMR definition')]),
'0.1':(1,[L(P+'0.0',E,'energy input and output')]),
'0.2':(1,[L(P+'0.0',E,'energy input and output'),L('hom-energy-nutrition-s1.0.3',H,'fat stored as adipose tissue')]),
'0.3':(1,[L(P+'0.0',E,'energy input and output'),L('hom-energy-nutrition-s1.0.3',H,'glycogen and fat stores')]),
'0.4':(1,[L(P+'0.3',H,'negative energy balance')]),
'0.5':(1,[L(P+'0.1',H,'energy balance')]),
'1.b':(1,[]),'1.0':(1,[]),'1.1':(1,[]),
'1.2':(1,[L('hom-energy-nutrition-s1.4.b',H,'physical activity energy use')]),
'1.3':(1,[L('hom-energy-nutrition-s1.4.3',H,'sedentary lifestyle')]),
'1.4':(1,[]),'1.5':(1,[L(P+'0.1',H,'returning to energy balance')]),
'2.b':(1,[]),
'2.0':(1,[L('hom-energy-nutrition-s1.5.b',H,'factors affecting energy requirement')]),
'2.1':(1,[L('hom-energy-nutrition-s3.7.0','helpful','energy-dense foods','low')]),
'2.2':(1,[L(P+'0.2',E,'positive energy balance'),L(P+'0.3',E,'negative energy balance')]),
'2.3':(1,[L(P+'1.0',H,'reducing energy intake')]),
'2.4':(1,[L(P+'1.2',H,'increasing energy output')]),
'2.5':(2,[L('hom-energy-nutrition-s3.7.2',H,'healthy eating guidelines')]),
'2.6':(2,[]),'2.7':(1,[]),
'3.b':(1,[]),'3.0':(1,[]),'3.1':(1,[]),'3.2':(1,[L(P+'3.0',H,'empty kilocalories')]),
'4.b':(1,[]),'4.0':(1,[L(P+'0.2',E,'positive energy balance')]),
'4.1':(1,[L('hom-energy-nutrition-s1.4.3',H,'sedentary lifestyle lowers output')]),
'4.2':(1,[L('hom-energy-nutrition-s1.4.2',H,'leisure activity')]),
'4.3':(1,[]),
'4.4':(1,[L('hom-energy-nutrition-s1.2.4',H,'thyroid controls BMR')]),
'4.5':(1,[]),'4.6':(1,[L('hom-energy-nutrition-s3.7.0',H,'energy-dense foods')]),
'4.7':(2,[]),
'5.b':(1,[]),'5.0':(1,[]),'5.1':(1,[]),'5.2':(1,[]),'5.3':(1,[]),'5.4':(1,[]),
'5.5':(2,[]),'5.6':(2,[]),
'5.7':(1,[L(P+'0.1',H,'return to energy balance')]),
'6.b':(1,[]),'6.0':(1,[]),
'6.1':(1,[L(P+'6.0',H,'BMI calculation')]),'6.2':(1,[L(P+'6.0',H,'BMI calculation')]),
'6.3':(1,[L(P+'6.0',H,'BMI calculation')]),'6.4':(1,[L(P+'6.0',H,'BMI calculation')]),
'6.5':(1,[]),'6.6':(1,[L(P+'6.b',H,'BMI as screening measure')]),'6.7':(1,[]),
'7.b':(1,[]),'7.0':(1,[L(P+'6.0',E,'BMI formula uses metres')]),
'7.1':(1,[L(P+'6.0',H,'BMI formula')]),'7.2':(1,[L(P+'6.0',E,'BMI formula')]),
'7.3':(1,[L(P+'6.2',H,'BMI categories','low')]),'7.4':(1,[L(P+'6.3',H,'overweight and obese categories')]),
}
for sub,d in [('hom-food-safety-s8',fs),('hom-clothing-selection-s3',cs),('hom-energy-nutrition-s2',es)]:
    txt=open(B+'packs/%s.t1g1.txt'%sub).read()
    allids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
    tgt=[i for i in re.findall(r'^\[([^\]]+)\]',txt.split('CANDIDATES')[0],re.M)]
    keys=[sub+'.'+k for k in d]
    assert keys==tgt,(sub,set(tgt)^set(keys))
    out={}
    for k,(c,l) in d.items():
        i=sub+'.'+k
        for x in l: assert x['id'] in allids and x['id']!=i,(i,x)
        out[i]={"cost":c,"needs":l}
    json.dump(out,open(B+'point-links/%s.t1g1.json'%sub,'w'),indent=1)
    n=sum(len(v['needs']) for v in out.values())
    print(sub,len(out),n,sum(v['cost']==2 for v in out.values()),sum(x['confidence']=='low' for v in out.values() for x in v['needs']))
