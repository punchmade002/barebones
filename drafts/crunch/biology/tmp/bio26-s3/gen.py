import json,re
P='bio26-s3.'
def n(i,s,w,c='high'):return {"id":i,"strength":s,"why":w,"confidence":c}
E,H='essential','helpful'
d={
'0.b':(1,[]),
'0.0':(1,[n('bio26-s2.0.5',H,'collecting duct location')]),
'0.1':(1,[]),
'0.2':(1,[]),
'1.b':(1,[]),
'1.0':(1,[n('bio20-s1.2.3',H,'pituitary releases ADH')]),
'1.1':(1,[n('bio26-s2.0.5',E,'collecting duct structure')]),
'1.2':(2,[n('bio25-s1.0.3',E,'aquaporins water channels'),n('bio20-s1.0.0',H,'hormone receptors on target cells','low')]),
'1.3':(2,[n('bio25-s1.2.0',E,'osmosis definition'),n('bio26-s2.4.0',E,'salty medulla')]),
'1.4':(1,[n(P+'1.2',E,'ADH makes duct permeable')]),
'1.5':(1,[n(P+'1.2',E,'water channels and permeability')]),
'1.6':(1,[]),
'2.b':(1,[]),
'2.0':(1,[n('bio21-s2.1.0',H,'stimulus in homeostasis','low')]),
'2.1':(1,[n('bio21-s2.1.1',H,'receptor role')]),
'2.2':(1,[n(P+'1.0',E,'ADH from pituitary')]),
'2.3':(1,[n(P+'2.2',H,'ADH release')]),
'2.4':(1,[n(P+'1.2',E,'ADH raises permeability')]),
'2.5':(1,[n(P+'1.4',E,'more ADH gives concentrated urine')]),
'2.6':(2,[n('bio21-s2.2.0',E,'negative feedback')]),
'2.7':(1,[]),
'3.b':(1,[]),
'3.0':(1,[]),
'3.1':(1,[]),
'3.2':(1,[n(P+'1.0',H,'ADH release','low')]),
'3.3':(1,[n(P+'1.5',E,'less ADH, fewer channels')]),
'3.4':(1,[n(P+'1.5',H,'less water reabsorbed')]),
'3.5':(1,[n(P+'3.4',H,'less reabsorption gives dilute urine','low')]),
'3.6':(1,[n('bio21-s2.2.0',H,'negative feedback')]),
'4.b':(1,[]),
'4.0':(1,[n(P+'2.4',E,'more ADH raises permeability')]),
'4.1':(1,[n(P+'2.5',E,'more ADH gives small urine')]),
'4.2':(2,[n(P+'3.3',E,'less ADH, less permeable ducts')]),
'5.b':(1,[]),
'5.0':(2,[n(P+'2.6',E,'high-concentration branch'),n(P+'3.6',H,'low-concentration branch')]),
}
out={P+k:{"cost":c,"needs":nd} for k,(c,nd) in d.items()}
json.dump(out,open('../../point-links/bio26-s3.json','w'),indent=1)
# check
txt=open('../../points/bio26-s3.txt').read()
ids=re.findall(r'^\[([^\]]+)\]',txt,re.M)
tg=[i for i in ids if i.startswith(P)]
j=json.load(open('../../point-links/bio26-s3.json'))
assert list(j)==tg,(set(tg)^set(j))
assert all(x['id'] in ids and x['id']!=k for k,v in j.items() for x in v['needs'])
L=[x for v in j.values() for x in v['needs']]
print(len(j),len(L),sum(v['cost']==2 for v in j.values()),sum(x['confidence']=='low' for x in L))
