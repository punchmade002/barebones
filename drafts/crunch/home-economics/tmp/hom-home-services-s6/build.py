import json,re
D='/Users/gabrielwhelan/barebones/.claude/worktrees/crunch-chem-home/drafts/crunch/home-economics/'
P='hom-home-services-s6'
def N(i,s,w,c='high'): return {"id":i,"strength":s,"why":w,"confidence":c}
H,E='helpful','essential'
S=P+'.'
HS='hom-home-services-'
spec=[
('0.b',1,[]),
('0.0',2,[N(HS+'s5.0.0',H,'conduction'),N(HS+'s5.0.1',H,'convection'),N(HS+'s5.0.2',H,'radiation')]),
('0.1',2,[N(HS+'s5.0.0',H,'conduction through materials')]),
('0.2',1,[N(HS+'s5.0.1',H,'convection currents')]),
('0.3',1,[N(HS+'s5.0.2',H,'radiant heat')]),
('0.4',1,[N(HS+'s2.0.2',H,'air leakage through gaps')]),
('0.5',1,[]),
('1.b',1,[]),
('1.0',1,[]),
('1.1',1,[]),
('1.2',1,[]),
('1.3',1,[]),
('1.4',1,[]),
('1.5',2,[]),
('1.6',1,[]),
('2.b',1,[]),
('2.0',2,[]),
('2.1',2,[]),
('2.2',2,[]),
('2.3',1,[N(S+'2.1',H,'dry lining'),N(S+'2.2',H,'external insulation')]),
('2.4',1,[N(S+'2.0',H,'cavity wall structure')]),
('3.b',1,[]),
('3.0',2,[]),
('3.1',1,[N(S+'0.2',H,'trapped air cannot circulate')]),
('3.2',1,[N(S+'3.1',H,'double glazing')]),
('3.3',1,[N(S+'0.3',H,'low-E coatings reflect radiation')]),
('3.4',1,[]),
('3.5',1,[N(S+'0.4',H,'draught proofing')]),
('3.6',1,[]),
('3.7',1,[]),
('4.b',1,[]),
('4.0',1,[]),
('4.1',1,[]),
('4.2',1,[]),
('4.3',1,[]),
('4.4',1,[N(S+'3.7',H,'insulation reduces condensation')]),
('4.5',2,[N(HS+'s2.10.1',H,'BER scale A to G')]),
('4.6',1,[]),
('5.b',1,[]),
('5.0',1,[N(S+'1.5',H,'lagging tank and pipes')]),
('5.1',1,[N(S+'3.5',H,'draught proofing and glazing')]),
('5.2',1,[N(S+'2.3',H,'solid versus cavity walls'),N(S+'3.6',H,'cylinder lagging')]),
('5.3',1,[N(S+'4.4',H,'condensation and damp')]),
('5.4',2,[N(HS+'s2.5.4',H,'ranking improvements by cost')]),
('5.5',1,[N(S+'4.5',H,'BER'),N(S+'4.6',H,'SEAI grants')]),
]
txt=open(D+'packs/'+P+'.t1g1.txt').read()
allids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
tgt=re.findall(r'^\[([^\]]+)\]',txt.split('CANDIDATES')[0],re.M)
out={S+k:{"cost":c,"needs":n} for k,c,n in spec}
assert list(out)==tgt,(set(tgt)^set(out))
for k,v in out.items():
    for n in v['needs']: assert n['id'] in allids and n['id']!=k,(k,n)
json.dump(out,open(D+'point-links/'+P+'.t1g1.json','w'),indent=1)
print(len(out),sum(len(v['needs']) for v in out.values()),sum(v['cost']==2 for v in out.values()),sum(n['confidence']=='low' for v in out.values() for n in v['needs']))
