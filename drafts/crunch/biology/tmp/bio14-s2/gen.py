import json,re
P='bio14-s2.'
txt=open('points/bio14-s2.txt').read()
ids=re.findall(r'^\[([^\]]+)\]',txt,re.M)
tgt=[i for i in ids if i.startswith('bio14-s2.')]
# id:(cost,[(need,strength,why,conf)])
E,H='essential','helpful'
S={
'0.1':(1,[('bio14-s1.5.3',E,'photolysis releases oxygen','high')]),
'0.2':(1,[('bio14-s1.5.5',E,'light energy trapped as ATP, hydrogen','high')]),
'0.3':(1,[('bio14-s1.5.7',E,'CO2 used in light-independent stage','high')]),
'0.4':(2,[('bio14-s1.6.2',E,'stage 2 reactions enzyme-controlled','high')]),
'0.5':(1,[(P+'0.4',H,'enzymes and optimum temperature','high')]),
'0.7':(1,[(P+'0.6',E,'limiting factor definition','high')]),
'1.0':(2,[('bio15-s1.1.0',E,'respiration uses oxygen','high'),(P+'0.1',H,'oxygen as product measured','low')]),
'1.1':(2,[(P+'1.0',E,'net rate equals photosynthesis minus respiration','high')]),
'1.2':(1,[('bio15-s1.1.0',H,'respiration takes in oxygen','high')]),
'2.0':(1,[('bio2-s2.2.0',E,'fair test, one variable changed','high')]),
'2.1':(1,[(P+'0.2',E,'light intensity effect on rate','high')]),
'2.2':(1,[(P+'0.3',E,'CO2 effect on rate','high')]),
'2.3':(1,[(P+'0.4',E,'temperature effect via enzymes','high'),(P+'0.5',H,'denaturation above optimum','high')]),
'2.4':(1,[(P+'0.1',H,'oxygen bubbles as measurable product','low')]),
'3.0':(1,[('bio2-s2.0.1',E,'independent variable','high'),(P+'0.2',H,'light intensity as factor','low')]),
'3.1':(1,[('bio2-s2.0.2',E,'dependent variable','high')]),
'3.2':(2,[('bio2-s2.0.3',E,'controlled variables','high')]),
'3.3':(1,[(P+'3.0',E,'independent variable structure','high')]),
'3.4':(1,[('bio2-s2.2.1',E,'control experiment','high')]),
'3.5':(2,[]),
'3.6':(1,[('bio14-s1.2.1',H,'hydrogencarbonate as CO2 source','low')]),
'4.0':(1,[(P+'3.6',H,'NaHCO3 supplies CO2','high')]),
'4.3':(1,[(P+'3.2',H,'temperature as controlled variable','high')]),
'4.5':(2,[('bio2-s2.5.2',H,'repeats and means','low')]),
'4.6':(2,[(P+'3.7',H,'funnel, graduated tube apparatus','low')]),
'4.7':(1,[(P+'4.6',E,'collecting gas volume method','high')]),
'5.0':(1,[(P+'4.b',E,'basic set-up','high')]),
'5.1':(1,[(P+'3.0',H,'lamp distance sets light intensity','high')]),
'5.2':(1,[(P+'4.5',E,'counting method','high')]),
'5.3':(1,[(P+'5.2',E,'repeat counting procedure','high')]),
'5.4':(1,[(P+'5.5',H,'lamp heating the water','high')]),
'5.5':(2,[('bio2-s2.3.1',E,'invalid if two variables change','high')]),
'5.6':(2,[]),
'5.7':(1,[(P+'5.6',E,'inverse square law','high')]),
'6.0':(2,[(P+'3.6',H,'NaHCO3 supplies CO2','high')]),
'6.1':(1,[(P+'3.2',H,'controlling other variables','high')]),
'6.2':(1,[(P+'4.5',H,'counting bubbles method','high')]),
'7.0':(1,[(P+'4.b',H,'basic set-up','high')]),
'7.3':(1,[(P+'0.5',H,'denaturation at high temperature','low')]),
'7.4':(1,[(P+'3.4',E,'darkness control','high')]),
'9.0':(1,[('bio2-s2.5.2',H,'repeats and means','low')]),
'9.1':(1,[(P+'9.0',H,'results table data','high')]),
'9.2':(2,[(P+'0.2',E,'light intensity effect on rate','high'),(P+'0.6',H,'limiting factor','high')]),
'9.3':(2,[(P+'0.3',E,'CO2 effect on rate','high'),(P+'0.6',H,'limiting factor','high')]),
'9.4':(2,[(P+'0.5',E,'denaturation above optimum','high')]),
'9.5':(1,[(P+'0.6',E,'limiting factor','high')]),
'10.0':(2,[(P+'3.5',H,'equipment list','high')]),
'10.1':(2,[(P+'9.2',H,'light graph shape','high'),(P+'9.4',H,'temperature graph shape','high')]),
'11.0':(1,[('bio2-s2.5.4',H,'larger sample, reliability','low')]),
'11.1':(2,[(P+'0.6',E,'limiting factor','high')]),
'11.2':(1,[(P+'11.1',E,'reading overlapping curves','high')]),
'11.3':(1,[(P+'0.7',E,'raising limiting factors','high')]),
'11.4':(1,[(P+'11.3',E,'glasshouse factor control','high')]),
'12.0':(1,[(P+'4.7',H,'volume more accurate than counting','high')]),
'12.1':(1,[(P+'4.4',H,'darkened room set-up','high')]),
'12.2':(1,[(P+'5.5',H,'bulb heating the plant','high')]),
'12.3':(1,[(P+'1.0',E,'net rate after respiration','high')]),
'12.4':(1,[(P+'6.0',H,'NaHCO3 supplies CO2','high')]),
'12.5':(1,[(P+'4.5',H,'adjustment time before counting','high')]),
'12.6':(1,[('bio2-s2.5.2',H,'repeats and means','high')]),
}
out={}
for t in tgt:
    k=t[len(P):]
    c,n=S.get(k,(1,[]))
    out[t]={"cost":c,"needs":[{"id":a,"strength":s,"why":w,"confidence":f} for a,s,w,f in n]}
json.dump(out,open('point-links/bio14-s2.json','w'),indent=1)
o=json.load(open('point-links/bio14-s2.json'))
assert list(o)==tgt
for v in o.values():
    for n in v['needs']:
        assert n['id'] in ids,n['id']
print(len(o),sum(len(v['needs']) for v in o.values()),sum(v['cost']==2 for v in o.values()),sum(n['confidence']=='low' for v in o.values() for n in v['needs']))
