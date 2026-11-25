import json,re
P='/Users/gabrielwhelan/barebones/drafts/crunch/biology/'
txt=open(P+'points/bio15-s5.txt').read()
allids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
tgt=[i for i in re.findall(r'^\[([^\]]+)\]',txt.split('CANDIDATES')[0],re.M)]
E,H='essential','helpful'
s='bio15-s5.'
D={ # id:(cost,[(id,strength,why,conf)])
'0.b':(1,[]),
'0.0':(1,[]),
'0.1':(2,[(s+'1.b',H,'electron transport chain','high')]),
'0.2':(1,[(s+'2.2',H,'protons moved into space','low')]),
'0.3':(1,[('bio15-s4.1.0',H,'citric acid cycle in matrix','high')]),
'0.4':(1,[('bio7-s3.6.1',H,'ribosome makes proteins','low')]),
'0.5':(2,[(s+'0.1',E,'cristae and ATP synthase placement','high')]),
'1.b':(1,[]),
'1.0':(1,[(s+'0.1',H,'inner membrane holds chains','high')]),
'1.1':(1,[(s+'1.0',E,'protein complexes of the chain','high')]),
'1.2':(1,[('bio9-s2.2.1',H,'NADH carries electrons to chain','high')]),
'1.3':(1,[('bio15-s4.2.3',H,'oxygen final electron acceptor','high')]),
'2.b':(1,[(s+'1.b',H,'electron transport chain','high')]),
'2.0':(2,[(s+'1.0',E,'protein complexes in membrane','high')]),
'2.1':(2,[(s+'2.0',E,'charge from arriving electrons','high')]),
'2.2':(2,[(s+'0.2',E,'intermembrane space location','high')]),
'2.3':(2,[(s+'2.2',E,'protons pumped into space','high')]),
'2.4':(2,[(s+'2.3',E,'proton gradient','high')]),
'2.5':(2,[(s+'2.4',E,'proton flow drives ATP synthase','high')]),
'2.6':(1,[(s+'1.3',E,'oxygen final acceptor','high')]),
'2.7':(2,[(s+'2.4',H,'steps shown in diagram','low')]),
'3.b':(1,[]),
'3.0':(1,[(s+'2.4',E,'proton gradient making ATP','high')]),
'3.1':(1,[(s+'3.0',H,'chemiosmosis idea','high')]),
'4.b':(1,[]),
'4.0':(1,[(s+'0.1',E,'cristae fold inner membrane','high')]),
'4.1':(1,[(s+'2.3',E,'gradient built in space','high')]),
'4.2':(1,[(s+'2.4',E,'protons return via ATP synthase','high')]),
'4.3':(1,[(s+'1.0',H,'complexes embedded in membrane','high')]),
'4.4':(1,[(s+'0.3',E,'matrix enzymes','high')]),
'4.5':(1,[(s+'0.2',H,'intermembrane space','high')]),
'4.6':(1,[(s+'0.4',E,'own DNA and ribosomes','high')]),
'5.b':(1,[('bio14-s5.0.1',H,'thylakoid membrane sacs','low')]),
'5.0':(1,[(s+'1.0',E,'protein complexes in membrane','high')]),
'5.1':(2,[(s+'2.3',E,'proton gradient','high'),('bio14-s5.2.2',H,'chloroplast ATP synthase flow','high')]),
'5.2':(1,[(s+'4.0',H,'cristae give large area','high'),('bio14-s5.3.0',H,'stacked thylakoid area','high')]),
'5.3':(1,[(s+'4.6',H,'own DNA and ribosomes','high')]),
'6.b':(1,[(s+'5.b',H,'shared mechanism','high')]),
'6.0':(1,[('bio9-s2.3.0',H,'light energises chlorophyll electrons','low')]),
'6.1':(1,[('bio9-s2.3.1',H,'water supplies electrons','low')]),
'6.2':(2,[('bio9-s2.4.3',H,'final acceptors compared','high')]),
'6.3':(1,[('bio9-s2.3.1',H,'photolysis of water','high')]),
'6.4':(1,[(s+'0.1',E,'inner membrane cristae','high'),('bio14-s5.0.1',E,'thylakoid membrane','high')]),
'6.5':(1,[(s+'0.2',E,'intermembrane space','high'),('bio14-s5.2.0',E,'thylakoid space protons','high')]),
'6.6':(1,[(s+'0.3',E,'matrix','high'),('bio14-s5.0.4',E,'stroma','high')]),
'6.7':(2,[(s+'6.4',H,'membranes compared','low')]),
}
out={}
for t in tgt:
    c,n=D[t[len(s):]]
    out[t]={'cost':c,'needs':[{'id':a,'strength':b,'why':w,'confidence':f} for a,b,w,f in n]}
json.dump(out,open(P+'point-links/bio15-s5.json','w'),indent=1)
o=json.load(open(P+'point-links/bio15-s5.json'))
assert list(o)==tgt and len(set(tgt))==len(tgt)
ns=[n for v in o.values() for n in v['needs']]
assert all(n['id'] in allids for n in ns)
assert all(n['id']!=k for k,v in o.items() for n in v['needs'])
print(len(o),len(ns),sum(v['cost']==2 for v in o.values()),sum(n['confidence']=='low' for n in ns))
