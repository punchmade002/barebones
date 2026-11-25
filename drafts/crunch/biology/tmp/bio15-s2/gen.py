import json,re
P='bio15-s2.'
def n(i,s='helpful',w='',c='high'): return {"id":i,"strength":s,"why":w,"confidence":c}
L={
'0.0':(1,[n('bio15-s1.2.0',w='anaerobic respiration')]),
'0.1':(1,[n(P+'0.0','essential','yeast fermentation products'),n(P+'5.5',w='iodoform test result',c='low')]),
'0.2':(1,[n('bio15-s1.0.7',w='respiratory substrate')]),
'0.3':(1,[n('bio15-s1.0.0',w='enzyme-catalysed respiration',c='low')]),
'0.4':(2,[n('bio15-s1.1.0','essential','aerobic respiration products'),n('bio15-s1.2.2',w='yeast ethanol equation')]),
'0.5':(2,[n(P+'0.3','essential','enzymes carry out fermentation'),n('bio33-s2.8.3',w='denaturation of enzymes')]),
'0.6':(1,[n('bio15-s1.2.6',w='facultative anaerobe')]),
'1.b':(1,[n('bio2-s2.2.0',w='fair test')]),
'1.1':(1,[n(P+'0.0',w='yeast fermentation products')]),
'1.2':(1,[n('bio2-s2.2.0',w='fair test design')]),
'1.3':(1,[n('bio2-s2.0.1','essential','independent variable')]),
'1.4':(1,[n('bio2-s2.0.2','essential','dependent variable')]),
'1.5':(1,[n('bio2-s2.0.3','essential','controlled variables')]),
'1.6':(1,[n('bio2-s2.2.1','essential','control experiment')]),
'2.1':(1,[n(P+'3.2',w='oil layer excludes air')]),
'2.2':(1,[n(P+'5.b',w='iodoform ethanol test')]),
'2.3':(1,[n('bio2-s2.6.2',w='measuring gas volume')]),
'3.0':(1,[n(P+'0.4',w='removing oxygen')]),
'3.2':(1,[n(P+'0.4',w='anaerobic condition')]),
'3.3':(1,[n(P+'2.0',w='limewater and fermentation lock',c='low')]),
'3.5':(2,[n(P+'0.1',w='CO2 as evidence')]),
'3.6':(1,[n(P+'2.3',w='gas collection apparatus')]),
'3.7':(1,[n(P+'5.b',w='ethanol test')]),
'4.0':(1,[n(P+'0.2','essential','sugar needed')]),
'4.1':(1,[n(P+'1.6',w='boiled yeast control')]),
'4.2':(1,[n(P+'0.4','essential','oxygen prevents fermentation')]),
'4.3':(2,[n(P+'0.4','essential','aerobic vs anaerobic products')]),
'4.5':(2,[n(P+'0.5','essential','enzymes and temperature')]),
'4.6':(1,[n(P+'0.5','essential','denaturation at high temperature')]),
'5.4':(1,[n('bio2-s2.2.3',w='negative control'),n('bio2-s2.2.4',w='positive control')]),
'6.0':(1,[n('bio15-s1.2.3',w='lactic acid fermentation')]),
'6.2':(2,[n('bio33-s2.9.b',w='pH meaning',c='low')]),
'6.3':(1,[n(P+'0.1',w='limewater detects CO2')]),
'7.0':(1,[n('bio2-s2.7.3',w='corrosive reagent precautions')]),
'7.4':(1,[n('bio2-s2.7.5',w='microorganism safety',c='low')]),
'8.2':(2,[n(P+'4.3',w='aerated flask result',c='low')]),
'8.3':(1,[n(P+'4.5',w='temperature series result')]),
'8.4':(1,[n(P+'0.0',w='fermentation products')]),
'8.5':(1,[n(P+'3.3',w='set-up with lock')]),
'9.0':(2,[n('bio2-s2.5.0',w='reliability and repeats')]),
'9.1':(2,[n(P+'0.4',w='anaerobic conditions for ethanol')]),
'10.0':(1,[n(P+'3.2',w='oil layer excludes oxygen')]),
'10.1':(2,[n(P+'0.4',w='facultative aerobic/anaerobic')]),
'10.2':(1,[n(P+'3.6',w='gas collection method',c='low')]),
'10.3':(2,[n(P+'0.1',w='limewater test for CO2')]),
'10.5':(1,[n('bio2-s2.5.2',w='repeats and means')]),
}
ids=re.findall(r'^\[(bio15-s2\.[\w.]+)\]',open('points/bio15-s2.txt').read(),re.M)
out={}
for i in ids:
    k=i[len(P):]
    c,nd=L.get(k,(1,[]))
    out[i]={"cost":c,"needs":nd}
json.dump(out,open('point-links/bio15-s2.json','w'),indent=1)
# check
pk=open('points/bio15-s2.txt').read()
allids=set(re.findall(r'^\[([^\]]+)\]',pk,re.M))
d=json.load(open('point-links/bio15-s2.json'))
assert list(d)==ids
bad=[x['id'] for v in d.values() for x in v['needs'] if x['id'] not in allids]
selfl=[k for k,v in d.items() for x in v['needs'] if x['id']==k]
print(len(d),sum(len(v['needs']) for v in d.values()),sum(v['cost']==2 for v in d.values()),sum(x['confidence']=='low' for v in d.values() for x in v['needs']),bad,selfl)
