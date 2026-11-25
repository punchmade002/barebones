import json,re
P='hist-ire5-s4.'
E,H='essential','helpful'
# id: (cost, [(target, strength, why, conf)])  short ids for s4 targets prefixed with '.'
D={
'0.b':(1,[]),
'0.0':(1,[('hist-ire5-s1.1.5',H,'uses the RUC','high')]),
'0.1':(1,[('.0.0',E,'the clashes that began the battle','high'),('hist-ire5-s2.6.3',H,'Free Derry first declared','low')]),
'0.2':(1,[('.0.1',H,'follows the Battle of the Bogside','high')]),
'0.3':(1,[]),
'0.4':(1,[]),
'0.5':(1,[]),
'0.6':(2,[('hist-ire5-s1.1.5',H,'the RUC it recommends reforming','high')]),
'0.7':(1,[('.0.6',E,'the Hunt Report recommendation','high'),('hist-ire5-s1.1.4',E,'the B Specials','high')]),
'0.8':(1,[('hist-ire5-s1.1.4',E,'the B Specials it replaced','high')]),
'0.9':(2,[('hist-ire5-s1.0.2',H,'earlier consent guarantee','low')]),
'1.b':(1,[]),
'1.0':(1,[('hist-ire5-s2.6.7',H,'Chichester-Clark beat Faulkner narrowly','low')]),
'1.1':(1,[('.0.1',E,'the Battle of the Bogside','high'),('.0.7',E,'the B Specials disbanding','high'),('.0.6',H,'the Hunt Report','high')]),
'1.2':(2,[('hist-ire5-s2.5.6',H,'points system for housing','low')]),
'1.3':(1,[('.1.2',E,'the reforms hardliners opposed','high')]),
'1.4':(1,[('.1.0',H,'Chichester-Clark as Prime Minister','high')]),
'1.5':(1,[('.1.4',E,'his resignation created the vacancy','high')]),
'2.b':(1,[]),
'2.0':(2,[('hist-ire5-s1.7.0',H,'the IRA','low')]),
'2.1':(1,[('.2.0',E,'the Provisional IRA','high'),('.0.5',H,'violence of August 1969','low')]),
'2.2':(1,[('.2.0',E,'the new military wing','high')]),
'2.3':(1,[('.0.2',E,'the army deployed after 1969','high')]),
'2.4':(2,[('hist-ire5-s1.1.6',H,'the Nationalist Party it superseded','low')]),
'2.5':(1,[]),
'2.6':(1,[('.2.0',H,'the Official IRA','high')]),
'2.7':(1,[('.2.4',E,'the SDLP','high')]),
'3.b':(1,[]),
'3.0':(1,[('hist-ire5-s2.1.7',H,'UVF revival in 1966','high')]),
'3.1':(1,[('hist-ire5-s2.1.7',H,'the 1966 UVF murders','high')]),
'3.2':(1,[]),
'3.3':(2,[('.3.1',E,'the UVF','high')]),
'3.4':(1,[]),
'3.5':(1,[('hist-ire5-s2.1.2',H,'William Craig','high')]),
'3.6':(1,[]),
'4.b':(1,[]),
'4.0':(2,[('hist-ire5-s2.0.0',H,'O\'Neill as Prime Minister','low')]),
'4.1':(1,[('.1.0',E,'the vote that made Chichester-Clark leader','high'),('hist-ire5-s2.1.2',H,'William Craig','low')]),
'4.2':(1,[('.5.0',E,'internment','high')]),
'4.3':(1,[('.7.0',E,'the security dispute with Westminster','high')]),
'4.4':(1,[('.5.0',H,'internment','high')]),
'4.5':(2,[('.7.0',E,'Westminster taking over security','high'),('.7.1',H,'resignation and suspension','high')]),
'4.6':(1,[('.2.7',E,'the July 1971 Derry shootings','high'),('.2.4',H,'the SDLP','high')]),
'5.b':(1,[]),
'5.0':(1,[]),
'5.1':(1,[('.5.0',E,'internment sweep','high')]),
'5.2':(2,[('.5.0',E,'internment','high')]),
'5.3':(2,[('.5.2',E,'the five techniques','high')]),
'5.4':(2,[('.5.0',H,'army operations during internment','high')]),
'5.5':(1,[('.5.0',E,'internment','high'),('.2.0',H,'the Provisional IRA','high')]),
'6.b':(1,[]),
'6.0':(1,[('.5.0',E,'internment','high'),('hist-ire5-s2.4.0',E,'NICRA','high')]),
'6.1':(1,[('.6.0',E,'the 1972 march','high')]),
'6.2':(1,[('.6.1',E,'the shootings','high')]),
'6.3':(1,[('.6.1',E,'the killings investigated','high')]),
'6.4':(2,[('.6.1',E,'the killings investigated','high')]),
'6.5':(1,[('.6.1',E,'the killings','high'),('.2.0',H,'the Provisional IRA','high')]),
'7.b':(1,[]),
'7.0':(1,[('.4.3',H,'Faulkner on security powers','high')]),
'7.1':(1,[('.7.0',E,'the refusal of security powers','high')]),
'7.2':(1,[('.7.1',E,'the suspension of Stormont','high')]),
'7.3':(1,[('.7.2',E,'the Secretary of State under Direct Rule','high')]),
'7.4':(2,[('.7.2',E,'Direct Rule','high')]),
'7.5':(1,[('.7.1',H,'the suspension of Stormont','high')]),
'7.6':(2,[('.7.3',E,'Whitelaw as Secretary of State','high'),('.2.0',H,'the Provisional IRA','high')]),
'7.7':(2,[('.7.4',E,'Direct Rule lasting','high')]),
'8.b':(1,[]),
'8.0':(1,[('.2.0',H,'the Provisional IRA','high')]),
'8.1':(1,[('.8.0',E,'Bloody Friday','high')]),
'8.2':(1,[('.0.1',H,'the Bogside no-go area','high')]),
'8.3':(1,[('.8.2',E,'Operation Motorman','high')]),
'8.4':(1,[('.8.2',H,'Operation Motorman','high'),('.2.0',H,'the Provisional IRA','high')]),
'8.5':(1,[]),
'9.0':(1,[('hist-ire5-s2.3.1',H,'evidence of discrimination','low')]),
'9.1':(1,[('hist-ire5-s1.1.4',E,'the B Specials','high')]),
'9.2':(1,[('.2.0',E,'the Provisional IRA','high')]),
'9.3':(1,[('.3.2',H,'loyalist paramilitaries','low')]),
'9.4':(1,[('.5.0',E,'internment','high'),('.6.1',E,'Bloody Sunday','high')]),
'9.5':(1,[('hist-ire5-s1.0.4',H,'permanent unionist majority','low')]),
'9.6':(2,[('.7.0',H,'British takeover of security','high')]),
'10.0':(1,[('.7.5',E,'the abolition of Stormont','high')]),
'10.1':(1,[('.5.5',H,'internment alienating Catholics','high')]),
'10.2':(1,[('.7.1',E,'suspension of Stormont','high')]),
'10.3':(2,[('.7.1',H,'the 1972 suspension','high')]),
'10.4':(1,[('.7.2',E,'Direct Rule','high')]),
}
out={}
for k,(c,n) in D.items():
    out[P+k]={"cost":c,"needs":[{"id":(P[:-1]+t if t.startswith('.') else t),"strength":s,"why":w,"confidence":cf} for t,s,w,cf in n]}
base='/Users/gabrielwhelan/barebones/drafts/crunch/history/'
txt=open(base+'packs/hist-ire5-s4.t1g1.txt').read()
ids=re.findall(r'^\[([^\]]+)\]',txt,re.M)
tgt=[i for i in ids if i.startswith(P)]
assert list(out)==tgt,(set(tgt)^set(out),)
for v in out.values():
    for n in v['needs']: assert n['id'] in ids and n['id']!=None
json.dump(out,open(base+'point-links/hist-ire5-s4.t1g1.json','w'),indent=0)
d=json.load(open(base+'point-links/hist-ire5-s4.t1g1.json'))
for k,v in d.items():
    assert all(n['id']!=k for n in v['needs'])
print(len(d),sum(len(v['needs']) for v in d.values()),sum(v['cost']==2 for v in d.values()),sum(n['confidence']=='low' for v in d.values() for n in v['needs']))
