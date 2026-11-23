import json,re
D='/Users/gabrielwhelan/barebones/drafts/crunch/biology/'
E,H='essential','helpful'
def n(i,s,w,c='high'): return {"id":i,"strength":s,"why":w,"confidence":c}
S={
'0.b':(1,[]),
'0.0':(1,[n('bio19-s4.3.2',H,'calcium triggers vesicle release')]),
'0.1':(1,[]),
'0.2':(1,[n('bio19-s4.3.2',H,'neurotransmitter release at knob','low')]),
'1.b':(1,[]),
'1.0':(1,[n('bio19-s4.1.4',H,'neurotransmitter definition')]),
'1.1':(2,[n('bio19-s5.1.0',E,'enzyme inactivates neurotransmitter')]),
'2.b':(1,[]),
'2.0':(1,[n('bio19-s4.3.4',E,'binding to postsynaptic receptors'),n('bio19-s5.1.0',H,'removal of neurotransmitter')]),
'2.1':(2,[n('bio19-s5.2.0',E,'continued binding keeps neuron firing')]),
'3.b':(1,[]),
'3.0':(1,[n('bio19-s5.1.1',H,'acetylcholine breakdown to choline')]),
'3.1':(2,[n('bio19-s5.1.0',H,'enzyme clearance contrast','low')]),
'4.b':(1,[]),
'4.0':(1,[n('bio19-s4.3.1',H,'calcium entry step')]),
'4.1':(1,[n('bio19-s4.3.2',H,'vesicle release step')]),
'4.2':(1,[n('bio19-s4.3.3',H,'diffusion step')]),
'4.3':(1,[n('bio19-s4.3.4',H,'receptor binding step')]),
'4.4':(1,[n('bio19-s4.3.5',H,'new postsynaptic impulse')]),
'4.5':(1,[n('bio19-s5.1.0',E,'enzyme breakdown'),n('bio19-s5.3.1',E,'reuptake')]),
'4.6':(1,[n('bio19-s5.3.0',E,'reabsorbing breakdown products')]),
'4.7':(2,[n('bio19-s4.2.0',H,'labelled synapse parts')]),
'5.b':(1,[]),
'5.0':(1,[n('bio19-s5.4.b',H,'synapse loop steps that can fail','low')]),
'5.1':(1,[]),
'6.b':(1,[]),
'6.0':(1,[n('bio19-s5.1.1',E,'acetylcholinesterase breaks down acetylcholine')]),
'6.1':(2,[n('bio19-s5.6.0',E,'enzyme inhibited so acetylcholine accumulates')]),
'6.2':(1,[n('bio19-s5.6.1',H,'paralysis of muscles')]),
'7.b':(1,[]),
'7.0':(1,[n('bio19-s4.1.5',H,'acetylcholine as neurotransmitter')]),
'7.1':(2,[n('bio19-s4.1.5',H,'serotonin and noradrenaline')]),
'7.2':(1,[n('bio19-s4.1.5',H,'dopamine as neurotransmitter')]),
'8.b':(1,[n('bio19-s5.1.0',E,'enzyme inactivates neurotransmitter')]),
'8.0':(2,[n('bio19-s5.1.1',E,'acetylcholinesterase breaks down acetylcholine'),n('bio19-s5.7.0',H,'Alzheimer acetylcholine neuron loss')]),
'8.1':(2,[n('bio19-s5.8.b',E,'inhibiting breakdown enzyme')]),
'9.b':(1,[n('bio19-s5.3.1',E,'reuptake by transporter proteins')]),
'9.0':(2,[n('bio19-s5.3.1',E,'serotonin reuptake'),n('bio19-s5.7.1',H,'depression and serotonin')]),
'9.1':(2,[n('bio19-s5.8.0',H,'enhancing remaining signalling')]),
'10.b':(1,[]),
'10.0':(1,[]),
'10.1':(1,[n('bio19-s5.3.1',E,'dopamine reuptake')]),
'10.2':(1,[n('bio19-s4.3.4',H,'receptor binding')]),
'10.3':(1,[n('bio19-s4.3.4',H,'receptor binding')]),
'10.4':(2,[n('bio19-s4.3.4',E,'receptor binding'),n('bio19-s5.6.1',H,'acetylcholine acts on muscles','low')]),
'11.b':(2,[n('bio19-s5.5.0',H,'types of disruption')]),
'11.0':(1,[n('bio19-s4.3.2',H,'release and receptors needed')]),
'11.1':(1,[n('bio19-s5.1.0',E,'breakdown removes neurotransmitter')]),
'11.2':(1,[n('bio19-s4.3.4',H,'receptor activation')]),
}
ids=re.findall(r'^\[(bio19-s5\.[\w.]+)\]',open(D+'points/bio19-s5.txt').read(),re.M)
out={}
for i in ids:
    c,nd=S[i[len('bio19-s5.'):]]; out[i]={"cost":c,"needs":nd}
json.dump(out,open(D+'point-links/bio19-s5.json','w'),indent=1)
txt=open(D+'points/bio19-s5.txt').read()
allid=set(re.findall(r'^\[([\w.\-]+)\]',txt,re.M))
d=json.load(open(D+'point-links/bio19-s5.json'))
assert list(d)==ids and len(set(S))==len(ids)
ls=[x for v in d.values() for x in v['needs']]
assert all(x['id'] in allid for x in ls)
assert all(x['id']!=k for k,v in d.items() for x in v['needs'])
print(len(d),len(ls),sum(v['cost']==2 for v in d.values()),sum(x['confidence']=='low' for x in ls))
