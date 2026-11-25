import json,re
P='bio29-s3.'
H,E,h,l='high','essential','helpful','low'
def n(i,s,w,c=H): return {"id":i,"strength":s,"why":w,"confidence":c}
d={
'0.b':(1,[]),
'0.0':(1,[n('bio29-s1.0.3',h,'ventricles as lower chambers')]),
'0.1':(1,[]),
'0.2':(1,[n('bio29-s1.3.3',h,'myogenic cardiac muscle')]),
'0.3':(1,[n('bio29-s1.0.2',h,'atria as upper chambers'),n('bio29-s1.1.1',h,'superior vena cava entry')]),
'0.4':(1,[n(P+'0.3',E,'SA node as pacemaker')]),
'1.b':(1,[n(P+'0.4',h,'SA node impulse')]),
'1.0':(1,[n(P+'0.4',E,'SA node impulse starts beat')]),
'1.1':(1,[n(P+'1.0',h,'impulse spreading across atria')]),
'1.2':(1,[n(P+'1.1',h,'impulse blocked from ventricles'),n('bio29-s1.0.5',h,'septum as dividing wall',l)]),
'1.3':(2,[n(P+'1.2',E,'AV node passes impulse on'),n('bio29-s1.0.5',h,'septum',l)]),
'1.4':(1,[n(P+'1.3',h,'conducting fibres reach ventricles'),n('bio29-s1.1.4',h,'aorta leaves heart',l)]),
'1.5':(2,[n(P+'1.3',h,'conduction route to label')]),
'2.b':(1,[n(P+'0.4',h,'SA node sets rate')]),
'2.0':(1,[]),
'2.1':(2,[n(P+'0.3',E,'SA node receives impulses'),n('bio21-s2.1.2',h,'control centre in brain',l)]),
'2.2':(1,[n(P+'2.1',E,'medulla cardiac centre'),n('bio21-s2.1.1',h,'receptors detect changes')]),
'2.3':(1,[n(P+'0.3',h,'SA node target')]),
'2.4':(1,[]),
'2.5':(2,[n(P+'0.3',E,'SA node failure'),n(P+'1.1',h,'impulse blocked from ventricles',l)]),
'2.6':(1,[n(P+'2.5',E,'pacemaker device and its purpose')]),
'3.b':(1,[n(P+'0.0',h,'ventricle contraction')]),
'3.0':(1,[n('bio29-s1.1.3',h,'arteries carry blood from heart',l)]),
'3.1':(1,[n(P+'3.0',h,'pulse as artery wall wave')]),
'3.2':(1,[n(P+'3.0',E,'pulse as pressure wave')]),
'3.3':(1,[]),
'3.4':(1,[n(P+'3.1',h,'radial artery site')]),
'3.5':(1,[]),
'3.6':(1,[]),
'3.7':(1,[n(P+'3.0',E,'pulse as artery wall wave')]),
'4.b':(1,[n(P+'2.0',h,'rate rises with exercise')]),
'4.0':(2,[n(P+'3.3',h,'pulse measuring method')]),
'4.1':(1,[n(P+'4.0',h,'investigation results')]),
'4.2':(1,[n(P+'4.1',h,'fitness and pulse',l)]),
'4.3':(1,[]),
'4.4':(1,[n(P+'4.3',h,'variable definitions')]),
'5.b':(1,[n(P+'0.0',h,'ventricles pushing blood')]),
'5.0':(1,[n('bio29-s1.0.3',h,'ventricles pump blood')]),
'5.1':(1,[n(P+'5.0',E,'blood pressure definition')]),
'5.2':(1,[n(P+'5.0',h,'blood pressure definition')]),
'5.3':(2,[n(P+'5.2',h,'pressure measurement units')]),
'5.4':(1,[n(P+'5.3',E,'normal 120/80 values')]),
'5.5':(1,[n(P+'5.4',E,'hypertension defined')]),
'5.6':(2,[n(P+'5.4',h,'hypertension')]),
'5.7':(1,[n(P+'5.6',h,'factors raising pressure')]),
'6.b':(1,[]),
'6.0':(2,[n('bio29-s1.0.b',h,'heart chambers',l)]),
'6.1':(2,[n('bio29-s1.1.4',E,'aorta'),n(P+'6.0',h,'coronary circulation'),n('bio29-s1.2.3',h,'aortic semilunar valve')]),
'6.2':(1,[n(P+'6.1',h,'coronary arteries branch into muscle')]),
'6.3':(1,[n(P+'6.2',h,'capillaries in heart muscle',l),n('bio29-s1.0.2',h,'right atrium')]),
'6.4':(2,[n(P+'6.1',E,'coronary arteries to label')]),
'7.b':(1,[n(P+'6.1',h,'coronary arteries')]),
'7.0':(2,[n(P+'6.1',E,'coronary arteries')]),
'7.1':(1,[n(P+'7.0',E,'plaque in coronary arteries')]),
'7.2':(1,[n(P+'7.1',E,'clot causing heart attack')]),
'7.3':(2,[n(P+'5.4',h,'high blood pressure risk',l)]),
'7.4':(1,[n(P+'7.3',E,'risk factors removed')]),
'7.5':(2,[n(P+'7.0',E,'narrowed coronary artery')]),
'7.6':(1,[n(P+'7.0',E,'blocked coronary artery')]),
}
out={P+k:{"cost":c,"needs":x} for k,(c,x) in d.items()}
json.dump(out,open('/Users/gabrielwhelan/barebones/drafts/crunch/biology/point-links/bio29-s3.json','w'),indent=1)
pk=open('/Users/gabrielwhelan/barebones/drafts/crunch/biology/points/bio29-s3.txt').read()
ids=re.findall(r'^\[([^\]]+)\]',pk,re.M)
tg=[i for i in ids if i.startswith(P)]
o=json.load(open('/Users/gabrielwhelan/barebones/drafts/crunch/biology/point-links/bio29-s3.json'))
assert list(o)==tg,(set(tg)^set(o))
assert all(x['id'] in ids and x['id']!=k for k,v in o.items() for x in v['needs'])
print(len(o),sum(len(v['needs']) for v in o.values()),sum(v['cost']==2 for v in o.values()),sum(x['confidence']=='low' for v in o.values() for x in v['needs']))
