import json,re
P='bio18-s1.'
def L(i,s,w,c='high'):
    return {"id":i if i.startswith('bio21') else P+i,"strength":s,"why":w,"confidence":c}
E,H='essential','helpful'
d={
'0.b':(1,[]),
'0.0':(1,[]),
'0.1':(1,[L('0.0',H,'bones')]),
'0.2':(1,[L('0.0',E,'bones and joints')]),
'0.3':(1,[]),
'0.4':(1,[]),
'0.5':(2,[L('0.4',E,'axial group of skeleton')]),
'0.6':(2,[L('0.4',E,'appendicular group of skeleton')]),
'1.b':(1,[]),
'1.0':(1,[]),
'1.1':(1,[L('1.0',H,'bone as tissue')]),
'1.2':(1,[L('1.1',H,'bone matrix')]),
'1.3':(1,[]),
'2.b':(1,[]),
'2.0':(1,[]),
'2.1':(2,[]),
'2.2':(1,[L('0.2',H,'bones as levers')]),
'2.3':(2,[]),
'2.4':(2,[L('2.3','essential','red marrow')]),
'2.5':(1,[L('2.4',H,'long bones')]),
'2.6':(1,[L('1.1',H,'calcium phosphate in bone')]),
'2.7':(2,[L('2.6',E,'bone stores calcium'),L('5.3',H,'calcium needed for muscle'),L('bio21-s2.0.b',H,'keeping factors constant','low')]),
'3.b':(1,[]),
'3.0':(1,[L('0.1',H,'tendons attach muscle')]),
'3.1':(1,[L('3.0',H,'skeletal muscle')]),
'3.2':(1,[]),
'3.3':(1,[L('3.2',E,'smooth muscle')]),
'3.4':(1,[]),
'4.b':(1,[L('bio21-s2.1.3',E,'effector definition')]),
'4.0':(1,[L('3.0',H,'skeletal muscle')]),
'4.1':(1,[L('4.0',E,'muscle fibres')]),
'4.2':(1,[L('4.0',E,'muscle fibres')]),
'4.3':(1,[L('4.2',E,'actin and myosin filaments')]),
'5.b':(1,[]),
'5.0':(1,[L('3.0',H,'voluntary control of skeletal muscle')]),
'5.1':(1,[L('5.0',E,'motor neuron stimulates muscle')]),
'5.2':(2,[L('5.1',E,'neuromuscular junction')]),
'5.3':(1,[L('5.2',E,'impulse in the fibre')]),
'5.4':(2,[L('5.3',E,'calcium release'),L('4.2',E,'actin and myosin')]),
'5.5':(1,[L('4.1',H,'mitochondria in fibres')]),
'6.b':(1,[]),
'6.0':(1,[L('5.3',E,'calcium released in contraction')]),
'6.1':(1,[L('6.0',H,'relaxation of muscle')]),
'6.2':(1,[]),
'6.3':(1,[L('0.2',E,'muscle pulls bone at joint')]),
'6.4':(1,[L('5.0',H,'motor neuron stimulation'),L('4.0',E,'muscle fibres')]),
'6.5':(1,[L('5.4',H,'partial contraction','low')]),
'6.6':(2,[L('5.0',H,'voluntary response pathway'),L('4.2',H,'actin and myosin filaments')]),
'7.b':(1,[]),
'7.0':(1,[]),
'7.1':(1,[]),
'7.2':(1,[L('6.5',H,'muscle tone')]),
'7.3':(1,[L('0.5',H,'ribs','low')]),
'7.4':(1,[]),
'7.5':(1,[L('bio21-s2.4.4',H,'shivering releases heat')]),
'8.b':(1,[]),
'8.0':(1,[L('5.0',E,'motor neuron stimulates muscle')]),
'8.1':(1,[]),
'8.2':(2,[L('5.5',H,'respiration supplies ATP')]),
'8.3':(2,[L('8.2',H,'oxygen supply to muscle'),L('5.5',H,'ATP from respiration')]),
'8.4':(1,[L('8.3',E,'lactic acid produced')]),
'8.5':(1,[]),
'8.6':(1,[L('1.3',H,'bone adapts to forces')]),
'8.7':(1,[L('1.1',H,'calcium in bone matrix')]),
}
out={P+k:{"cost":c,"needs":n} for k,(c,n) in d.items()}
json.dump(out,open('point-links/bio18-s1.json','w'),indent=1)
pk=open('points/bio18-s1.txt').read()
ids=re.findall(r'^\[([^\]]+)\]',pk,re.M)
t=re.split(r'CANDIDATES',pk)[0]
tid=re.findall(r'^\[([^\]]+)\]',t,re.M)
assert list(out)==tid,(set(tid)^set(out))
assert all(n['id'] in ids and n['id']!=k for k,v in out.items() for n in v['needs'])
print(len(out),sum(len(v['needs']) for v in out.values()),sum(v['cost']==2 for v in out.values()),sum(n['confidence']=='low' for v in out.values() for n in v['needs']))
