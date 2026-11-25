import json,re
D='/Users/gabrielwhelan/barebones/drafts/crunch/biology/'
E,H='essential','helpful'
def n(i,s,w,c='high'):return {"id":i,"strength":s,"why":w,"confidence":c}
P='bio19-s6.'
spec={
'0.b':(1,[]),'0.0':(1,[]),'0.1':(1,[]),
'0.2':(1,[n(P+'0.1',H,'neurons signalling changed by chemicals')]),
'1.b':(1,[]),
'1.0':(1,[n(P+'0.b',H,'neurotransmitter definition')]),
'1.1':(1,[n(P+'1.0',E,'dopamine made from tyrosine')]),
'2.b':(1,[]),
'2.0':(1,[n(P+'1.0',H,'dopamine as neurotransmitter')]),
'2.1':(1,[n(P+'2.0',E,'dopamine released on reward')]),
'2.2':(1,[n(P+'2.1',H,'reward and reinforcement role')]),
'3.b':(1,[]),
'3.0':(1,[n(P+'1.0',H,'dopamine as neurotransmitter')]),
'3.1':(1,[n(P+'1.0',H,'dopamine as neurotransmitter')]),
'3.2':(1,[n('bio19-s5.7.2',H,'Parkinson\'s dopamine neuron loss'),n(P+'3.0',H,'dopamine controls movement')]),
'4.b':(1,[]),
'4.0':(2,[n('bio20-s1.1.b',H,'pituitary and hypothalamus location','low')]),
'4.1':(1,[n(P+'4.0',H,'endorphins as neurotransmitters')]),
'4.2':(2,[n(P+'4.0',E,'endorphins are peptide neurotransmitters')]),
'4.3':(1,[n(P+'4.0',H,'endorphins as neurotransmitters')]),
'5.b':(1,[n(P+'2.b',H,'reward pathway')]),
'5.0':(2,[n('bio19-s5.3.1',E,'reuptake by transporter proteins')]),
'5.1':(1,[n('bio19-s5.0.0',H,'neurotransmitter release','low')]),
'5.2':(1,[n(P+'5.0',E,'cocaine raises dopamine'),n(P+'5.1',E,'amphetamines raise dopamine'),n(P+'2.b',H,'reward pathway')]),
'6.b':(1,[]),
'6.0':(1,[n(P+'2.b',H,'reward pathway')]),
'6.1':(1,[n(P+'4.2',E,'endorphins bind opioid receptors')]),
'7.b':(1,[]),
'7.0':(2,[n('bio19-s5.4.3',H,'receptors on postsynaptic membrane','low')]),
'7.1':(1,[n(P+'7.0',E,'fewer receptors reduce effect')]),
'7.2':(1,[n(P+'7.0',E,'fewer dopamine receptors')]),
'7.3':(1,[n(P+'7.0',H,'brain adaptation to drug')]),
'7.4':(1,[n(P+'7.3',H,'dependence and withdrawal')]),
'8.b':(1,[n(P+'4.1',H,'when endorphins are released')]),
'8.0':(1,[n(P+'4.1',H,'endorphin release triggers')]),
'8.1':(2,[n(P+'8.0',E,'exercise raises endorphins and dopamine'),n(P+'4.2',H,'endorphins as painkillers')]),
'9.b':(1,[n(P+'1.b',H,'diet supplies dopamine raw material')]),
'9.0':(1,[n(P+'2.1',H,'reward reinforces behaviour')]),
'9.1':(1,[n(P+'1.0',E,'tyrosine as dopamine precursor')]),
'10.b':(1,[]),
'10.0':(1,[n(P+'8.0',H,'exercise raises neurotransmitters')]),
'10.1':(1,[n(P+'7.0',H,'brain adaptation causes dependence')]),
'10.2':(1,[]),
}
out={}
for k,(c,nd) in spec.items(): out[P+k]={"cost":c,"needs":nd}
json.dump(out,open(D+'point-links/bio19-s6.json','w'),indent=1)
# check
txt=open(D+'points/bio19-s6.txt').read()
ids=re.findall(r'^\[([^\]]+)\]',txt,re.M)
t=[i for i in ids if i.startswith(P)]
d=json.load(open(D+'point-links/bio19-s6.json'))
assert list(d)==t,(set(t)^set(d))
nl=[x for v in d.values() for x in v['needs']]
assert all(x['id'] in ids and True for x in nl)
assert all(x['id']!=k for k,v in d.items() for x in v['needs'])
print(len(d),len(nl),sum(v['cost']==2 for v in d.values()),sum(x['confidence']=='low' for x in nl))
