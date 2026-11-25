import json,re
P='hist-eur3-s9.'
H,L='high','low'
E,HP='essential','helpful'
# id: (cost, [(target,strength,why,conf)])
d={
'0.b':(1,[]),
'0.0':(1,[]),
'0.1':(1,[]),
'0.2':(1,[('hist-eur3-s3.4.10',E,'uses the Nazi-Soviet Pact',H)]),
'0.3':(1,[(P+'0.4',HP,'uses the Phoney War',H)]),
'0.4':(1,[]),
'0.5':(2,[]),
'1.b':(1,[]),
'1.0':(1,[]),
'1.1':(1,[(P+'1.0',HP,'follows the May 1940 offensive',H)]),
'1.2':(1,[]),
'1.3':(2,[(P+'1.2',E,'defeated the attempt at air superiority',H),(P+'8.2',HP,'explains the Chain Home radar system',L)]),
'1.4':(1,[(P+'1.2',HP,'follows the Luftwaffe air campaign',H)]),
'1.5':(1,[(P+'1.3',HP,'invasion needed air superiority',L)]),
'2.b':(1,[]),
'2.0':(1,[]),
'2.1':(1,[(P+'2.0',E,'advance of Operation Barbarossa',H)]),
'2.2':(2,[]),
'2.3':(1,[]),
'2.4':(1,[(P+'2.2',HP,'Japan attacks following Pearl Harbor',H)]),
'2.5':(2,[]),
'2.6':(2,[(P+'2.2',HP,'Japanese offensive after Pearl Harbor',L)]),
'2.7':(1,[(P+'2.6',HP,'Japan advance being ended',H)]),
'2.8':(1,[(P+'2.7',HP,'counter-offensive after Midway',L)]),
'2.9':(2,[(P+'6.6',E,'uses the atomic bombs',H)]),
'3.b':(1,[]),
'3.0':(1,[('hist-eur3-s1.6.6',HP,'Pact of Steel signing, Italy non-belligerent',H)]),
'3.1':(1,[]),
'3.2':(1,[]),
'3.3':(2,[(P+'2.0',E,'uses Barbarossa',H),('hist-eur3-s1.6.7',HP,'Italy defeats in Greece and Africa',H)]),
'3.4':(1,[]),
'4.b':(1,[]),
'4.0':(1,[]),
'4.1':(1,[(P+'2.0',E,'Soviet Union joined after Barbarossa',H)]),
'4.2':(1,[(P+'4.1',HP,'second front demanded by Stalin',H)]),
'4.3':(2,[]),
'4.4':(2,[(P+'4.1',HP,'dispute over second front',H)]),
'5.b':(1,[]),
'5.0':(1,[]),
'5.1':(1,[]),
'5.2':(1,[('hist-eur3-s1.7.0',HP,'Sicily landing and Italian government',H)]),
'5.3':(1,[]),
'5.4':(1,[]),
'5.5':(1,[]),
'6.b':(1,[]),
'6.0':(2,[(P+'0.0',HP,'blitzkrieg armoured tactics',H)]),
'6.1':(2,[]),
'6.2':(1,[(P+'8.2',HP,'Chain Home development',H)]),
'6.3':(1,[(P+'8.4',HP,'early Enigma breaking',H)]),
'6.4':(1,[]),
'6.5':(2,[(P+'8.6',HP,'V-2 rocket research',H)]),
'6.6':(2,[]),
'7.b':(1,[]),
'7.0':(2,[]),
'7.1':(1,[(P+'7.0',HP,'earlier First Lord of the Admiralty role',L)]),
'7.2':(1,[(P+'1.2',HP,'uses the Battle of Britain',H)]),
'7.3':(1,[(P+'4.2',HP,'uses the Tehran Conference',H),(P+'4.3',HP,'uses the Yalta Conference',H)]),
'7.4':(1,[]),
'7.5':(2,[(P+'6.1',HP,'uses the bombing of Dresden',H)]),
'7.6':(1,[]),
'7.7':(1,[(P+'7.8',HP,'uses Dunkirk',H),(P+'1.4',HP,'uses the Blitz',H)]),
'7.8':(1,[(P+'1.1',HP,'British forces cut off at the coast',H)]),
'7.9':(1,[]),
'7.10':(1,[]),
'7.11':(1,[(P+'7.3',HP,'losing office in 1945',L)]),
'8.b':(1,[]),
'8.0':(2,[(P+'0.0',HP,'uses Panzer divisions and blitzkrieg',H)]),
'8.1':(2,[('hist-eur3-s3.4.11',HP,'uses the Condor Legion in Spain',H)]),
'8.2':(1,[]),
'8.3':(1,[(P+'1.3',HP,'uses Hurricane and Spitfire fighters',L)]),
'8.4':(1,[]),
'8.5':(1,[(P+'6.5',HP,'uses German jet fighter development',L)]),
'8.6':(1,[(P+'6.5',HP,'uses the V-2 rocket',H)]),
'9.b':(1,[]),
'9.0':(1,[(P+'1.2',HP,'uses refusal to negotiate in 1940',L)]),
'9.1':(1,[(P+'2.4',HP,'uses the fall of Singapore',H)]),
'9.2':(1,[]),
'9.3':(1,[(P+'4.4',E,'uses Eastern Europe divisions',H)]),
'9.4':(2,[(P+'7.7',HP,'uses Churchill as symbol of resistance',L)]),
'9.5':(2,[(P+'7.2',HP,'uses Churchill leadership in 1940',L)]),
}
out={}
for k,(c,n) in d.items():
    out[P+k]={"cost":c,"needs":[{"id":t,"strength":s,"why":w,"confidence":cf} for t,s,w,cf in n]}
txt=open('/Users/gabrielwhelan/barebones/drafts/crunch/history/packs/hist-eur3-s9.t1g1.txt').read()
lines=txt.split('\n')
ids=re.findall(r'^\[([^\]]+)\]',txt,re.M)
tgt=[]
for l in lines:
    if l.startswith('CANDIDATES'):break
    m=re.match(r'\[([^\]]+)\]',l)
    if m:tgt.append(m.group(1))
assert list(out)==tgt,(set(tgt)^set(out))
for v in out.values():
    for n in v['needs']:assert n['id'] in ids
json.dump(out,open('/Users/gabrielwhelan/barebones/drafts/crunch/history/point-links/hist-eur3-s9.t1g1.json','w'),indent=0)
print(len(out),sum(len(v['needs']) for v in out.values()),sum(v['cost']==2 for v in out.values()),sum(n['confidence']=='low' for v in out.values() for n in v['needs']))
