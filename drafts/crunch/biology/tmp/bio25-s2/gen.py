import json,re
P='bio25-s2.'
H,L='high','low'
E,Hp='essential','helpful'
# id suffix: (cost, [(target, strength, why, conf)])
d={
'0.b':(1,[('bio25-s1.2.0',Hp,'osmosis pulls water out',H)]),
'0.0':(1,[]),'0.1':(1,[]),
'0.2':(1,[('bio25-s1.3.0',E,'hypertonic solution outside cell',H)]),
'0.3':(1,[('bio25-s1.2.0',E,'osmosis direction of water',H)]),
'0.4':(2,[('bio25-s1.3.4',E,'plasmolysis of cells',H)]),
'0.5':(1,[]),
'0.6':(1,[('bio25-s1.2.0',Hp,'contrast with osmosis',L)]),
'1.b':(1,[('bio25-s1.2.0',Hp,'osmosis in preservation',H)]),
'1.0':(2,[('bio25-s2.0.3',Hp,'water drawn out by osmosis',H)]),
'1.1':(1,[]),
'1.2':(1,[('bio25-s2.0.3',Hp,'microbes lose water by osmosis',H)]),
'1.3':(1,[]),
'1.4':(2,[('bio25-s2.1.3',Hp,'acid pickling by low pH',H)]),
'2.b':(1,[]),'2.0':(1,[]),'2.1':(1,[]),
'2.2':(1,[('bio25-s2.0.3',Hp,'concentration difference drives osmosis',H)]),
'2.3':(1,[]),'2.4':(1,[]),'2.5':(1,[]),
'2.6':(1,[('bio25-s1.2.0',Hp,'osmosis draws water out',H)]),
'2.7':(1,[('bio25-s1.3.3',E,'turgid plant cells in water',H)]),
'3.b':(1,[('bio25-s1.3.3',Hp,'turgid cells from osmosis',H)]),
'3.0':(1,[('bio25-s1.3.3',E,'turgid cells, vacuole uptake',H)]),
'3.1':(1,[('bio25-s1.3.3',E,'turgor pressure on wall',H)]),
'3.2':(1,[('bio25-s2.3.0',Hp,'water entering vacuoles',L)]),
'3.3':(2,[('bio25-s1.3.3',E,'turgid cells',H),('bio25-s1.3.4',E,'flaccid cells',H),('bio30-s2.3.1',Hp,'guard cell opening mechanism',L)]),
'3.4':(2,[('bio25-s1.3.4',E,'flaccid cells lose water',H),('bio30-s2.2.0',Hp,'transpiration as water loss',H)]),
'3.5':(1,[('bio25-s2.3.4',E,'wilting defined',H)]),
'4.b':(1,[('bio25-s1.2.0',Hp,'direction of osmosis',H)]),
'4.0':(1,[('bio30-s2.0.2',Hp,'root hair osmosis',H)]),
'4.1':(2,[('bio25-s1.3.4',E,'plasmolysis',H),('bio25-s2.4.0',E,'normal root water uptake',H)]),
'4.2':(1,[('bio25-s2.4.1',Hp,'salty soil water harms roots',H)]),
'4.3':(1,[('bio25-s2.4.1',Hp,'concentrated soil water',H)]),
'4.4':(1,[('bio25-s2.4.1',E,'concentrated soil solution',H)]),
'4.5':(1,[('bio25-s2.4.4',E,'fertiliser burn',H)]),
'4.6':(2,[('bio25-s2.4.1',Hp,'salty soil draws water out',L)]),
'4.7':(1,[('bio25-s2.4.3',Hp,'salinisation from irrigation',H)]),
}
out={P+k:{"cost":c,"needs":[{"id":t,"strength":s,"why":w,"confidence":cf} for t,s,w,cf in n]} for k,(c,n) in d.items()}
txt=open('points/bio25-s2.txt').read()
tgt,cand=txt.split('CANDIDATES',1)
tids=re.findall(r'^\[([^\]]+)\]',tgt,re.M); allids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
assert list(out)==tids,(set(tids)^set(out))
for k,v in out.items():
    for n in v['needs']: assert n['id'] in allids and n['id']!=k,n
json.dump(out,open('point-links/bio25-s2.json','w'),indent=1)
print(len(out),sum(len(v['needs']) for v in out.values()),sum(v['cost']==2 for v in out.values()),sum(n['confidence']=='low' for v in out.values() for n in v['needs']))
