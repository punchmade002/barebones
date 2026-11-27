import json,re
D='/Users/gabrielwhelan/barebones/.claude/worktrees/crunch-chem-home/drafts/crunch/home-economics/'
P='hom-fruit-vegetables-s4'
def N(i,s,w,c='high'): return {"id":i,"strength":s,"why":w,"confidence":c}
H,E='helpful','essential'
S=P+'.'
FP='hom-food-preservation-'
FA='hom-food-additives-'
spec=[
('0.b',1,[]),
('0.0',1,[]),
('0.1',1,[]),
('0.2',2,[N(FP+'s2.2.3',H,'blanching inactivates enzymes')]),
('0.3',1,[]),
('0.4',1,[]),
('1.b',1,[]),
('1.0',2,[N(S+'1.2',H,'blanching before freezing')]),
('1.1',2,[N(FP+'s2.0.0',H,'low temperature and enzymes')]),
('1.2',1,[N(FP+'s2.2.3',H,'blanching inactivates enzymes')]),
('1.3',1,[N(FP+'s2.1.1',H,'quick freezing small crystals')]),
('1.4',1,[N(FP+'s2.1.4',H,'slow freezing large crystals')]),
('1.5',1,[N(FP+'s2.5.0',H,'air blast freezing')]),
('1.6',1,[N(FP+'s2.5.1',H,'plate freezing')]),
('1.7',1,[N(FP+'s2.5.2',H,'flow freezing')]),
('1.8',1,[N(FP+'s2.5.3',H,'cryogenic freezing')]),
('2.b',1,[]),
('2.0',1,[N(FP+'s2.2.5',H,'blanching vitamin losses')]),
('2.1',1,[N(FP+'s2.0.5',H,'freezing keeps nutritive value')]),
('2.2',1,[N(FP+'s2.3.8',H,'foods that freeze poorly')]),
('2.3',1,[]),
('3.b',1,[]),
('3.0',2,[N(FP+'s3.2.0',H,'commercial canning stages')]),
('3.1',1,[N(FP+'s3.0.0',H,'heat destroys microbes and enzymes')]),
('3.2',1,[N(FP+'s3.3.0',H,'vitamin C lost in canning')]),
('3.3',1,[]),
('3.4',1,[N(FP+'s3.3.3',H,'canned vegetables gain sodium')]),
('3.5',1,[N(FP+'s3.3.4',H,'syrup adds sugar')]),
('3.6',1,[]),
('3.7',2,[]),
('3.8',1,[]),
('4.b',1,[]),
('4.0',2,[N(FP+'s4.0.5',H,'blanching or fruit treatment before drying')]),
('4.1',1,[N(FP+'s4.0.0',H,'water needed by microbes and enzymes')]),
('4.2',1,[N(FP+'s4.5.0',H,'vitamin loss in drying')]),
('4.3',1,[N(FA+'s4.3.2',H,'sulphur dioxide preservative')]),
('4.4',1,[N(FP+'s4.5.3',H,'dried fruit concentrated sugar')]),
('4.5',1,[N(FP+'s4.5.6',H,'rehydrating dried food','low')]),
('4.6',1,[]),
('5.b',1,[]),
('5.0',2,[N(FA+'s4.0.0',H,'additive classes and functions')]),
('5.1',1,[N(FA+'s4.0.3',H,'E numbers and labels')]),
('5.2',1,[N(FA+'s4.1.0',H,'colourings restore colour')]),
('5.3',1,[N(FA+'s4.3.0',H,'preservatives inhibit microbes')]),
('5.4',1,[N(FA+'s4.6.0',H,'antioxidants')]),
('5.5',2,[]),
('5.6',1,[N(FA+'s4.7.1',H,'fortification')]),
('6.b',1,[]),
('6.0',2,[]),
('6.1',2,[]),
('6.2',2,[]),
('6.3',1,[]),
('6.4',1,[]),
('6.5',1,[]),
('6.6',1,[N(S+'6.5',H,'fruit juice lacks fibre')]),
('6.7',2,[N(FA+'s4.0.3',H,'additives identified by E number')]),
('6.8',1,[N(S+'0.4',H,'labelling regulation')]),
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
