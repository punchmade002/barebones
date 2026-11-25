import json,re
P='/Users/gabrielwhelan/barebones/drafts/crunch/biology/'
txt=open(P+'points/bio15-s4.txt').read()
ids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
tgt=re.findall(r'^\[(bio15-s4\.[^\]]+)\]',txt,re.M)
H,L='high','low'
def n(i,s,w,c=H):return {"id":i,"strength":s,"why":w,"confidence":c}
E,Hp='essential','helpful'
d={
'0.b':(1,[n('bio15-s3.0.5',Hp,'pyruvate as glycolysis product')]),
'0.0':(1,[n('bio15-s3.0.5',E,'pyruvate made in glycolysis')]),
'0.1':(1,[n('bio9-s2.1.0',Hp,'NAD+ loading to NADH')]),
'0.2':(2,[n('bio15-s4.0.1',E,'acetyl group left after CO2 removal')]),
'0.3':(1,[n('bio15-s3.0.5',E,'two pyruvate per glucose')]),
'1.b':(1,[n('bio15-s4.0.2',Hp,'acetyl CoA from link step')]),
'1.0':(1,[n('bio15-s4.0.0',Hp,'mitochondrial matrix')]),
'1.1':(2,[n('bio15-s4.0.2',E,'acetyl CoA carries acetyl group')]),
'1.2':(1,[n('bio15-s4.1.1',E,'citric acid formation in cycle')]),
'1.3':(1,[n('bio15-s4.1.1',Hp,'acetyl group entering cycle')]),
'1.4':(2,[n('bio9-s2.1.0',Hp,'NAD+ loading to NADH')]),
'1.5':(2,[n('bio15-s4.0.3',E,'link step twice per glucose')]),
'1.6':(2,[n('bio15-s4.2.3',Hp,'water formed at chain end')]),
'1.7':(2,[n('bio15-s4.2.4',Hp,'no oxygen stops chain and cycle',L)]),
'2.b':(2,[n('bio15-s3.0.4',Hp,'net 2 ATP of glycolysis')]),
'2.0':(1,[n('bio15-s5.0.1',Hp,'inner membrane and cristae')]),
'2.1':(1,[n('bio15-s4.2.0',E,'electron transport chain structure')]),
'2.2':(2,[n('bio15-s4.2.1',E,'electrons arriving from NADH'),n('bio9-s1.3.0',Hp,'ATP made from ADP and Pi')]),
'2.3':(2,[n('bio15-s4.2.2',E,'electrons passed down chain')]),
'2.4':(2,[n('bio15-s4.2.3',E,'oxygen as final acceptor')]),
'2.5':(1,[n('bio15-s4.2.4',E,'chain stops without oxygen')]),
'2.6':(1,[n('bio9-s1.5.b',Hp,'ATP uses in cells')]),
'2.7':(2,[n('bio15-s5.2.b',Hp,'proton gradient drives ATP synthase')]),
'3.b':(1,[]),
'3.0':(1,[n('bio15-s3.0.6',E,'glycolysis summary products')]),
'3.1':(2,[n('bio15-s4.0.2',Hp,'acetyl CoA from pyruvate')]),
'3.2':(2,[n('bio15-s4.2.3',Hp,'electrons passed to oxygen')]),
'3.3':(2,[n('bio9-s2.2.0',Hp,'NAD+ collects electrons')]),
'3.4':(1,[n('bio9-s1.4.0',Hp,'ATP/ADP cycle')]),
'3.5':(2,[n('bio15-s4.2.3',E,'water formed with oxygen')]),
'3.6':(2,[n('bio9-s2.3.2',E,'NADPH and ATP build glucose')]),
'3.7':(2,[n('bio15-s4.3.2',Hp,'chain, oxygen and ATP summary',L)]),
}
out={}
for t in tgt:
    c,nd=d[t.split('s4.')[1]]; out[t]={"cost":c,"needs":nd}
json.dump(out,open(P+'point-links/bio15-s4.json','w'),indent=1,ensure_ascii=False)
o=json.load(open(P+'point-links/bio15-s4.json'))
assert list(o)==tgt and len(d)==len(tgt)
for k,v in o.items():
    for x in v['needs']: assert x['id'] in ids and x['id']!=k,(k,x)
print(len(o),sum(len(v['needs']) for v in o.values()),sum(v['cost']==2 for v in o.values()),sum(x['confidence']=='low' for v in o.values() for x in v['needs']))
