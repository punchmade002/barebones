import json,re
P='/Users/gabrielwhelan/barebones/.claude/worktrees/crunch-chem-home/drafts/crunch/home-economics/'
C='hom-cooking-methods-s1.'
def L(i,s,w,c='high'): return {"id":i,"strength":s,"why":w,"confidence":c}
H,E='helpful','essential'
d={
'0.b':(1,[]),
'0.0':(2,[L('hom-proteins-s5.0.0',H,'uses denaturation of protein')]),
'0.1':(1,[]),'0.2':(1,[]),'0.3':(1,[]),'0.4':(1,[]),'0.5':(2,[]),'0.6':(1,[]),'0.7':(1,[]),
'0.8':(1,[L(C+'5.0',H,'water-soluble vitamins dissolve in water')]),
'1.b':(1,[]),'1.0':(1,[]),
'1.1':(1,[L(C+'1.0',H,'bicarbonate reacting with acid')]),
'1.2':(1,[]),
'1.3':(1,[L('hom-proteins-s5.7.1',H,'acid marinade denatures meat protein')]),
'1.4':(2,[L(C+'4.b',H,'the three browning processes')]),
'2.b':(1,[L(C+'1.b',H,'definition of chemical change')]),
'2.0':(1,[]),
'2.1':(1,[L(C+'2.0',E,'the enzyme polyphenol oxidase')]),
'2.2':(1,[]),'2.3':(1,[]),
'2.4':(2,[L(C+'2.1',H,'oxygen needed for browning')]),
'2.5':(2,[L(C+'2.0',H,'polyphenol oxidase enzyme action')]),
'2.6':(1,[L(C+'2.0',H,'enzyme inactivated by heat')]),
'2.7':(1,[L(C+'2.0',H,'enzyme activity slowed','low')]),
'3.b':(1,[]),
'3.0':(1,[L(C+'2.b',H,'enzymic browning')]),
'3.1':(1,[L(C+'2.5',E,'acid slows the enzyme')]),
'3.2':(1,[]),'3.3':(1,[]),'3.4':(2,[]),
'3.5':(2,[L(C+'3.2',H,'treatments applied to slices')]),
'3.6':(1,[]),
'3.7':(1,[L(C+'3.1',H,'the hypothesis being supported')]),
'3.8':(2,[L(C+'3.3',H,'rating browning by eye')]),
'4.b':(2,[L(C+'2.b',H,'contrast with enzymic browning')]),
'4.0':(1,[]),
'4.1':(1,[L(C+'4.0',H,'Maillard reaction')]),
'4.2':(1,[L(C+'4.0',H,'Maillard reaction')]),
'4.3':(1,[L(C+'4.0',H,'Maillard reaction needs dry heat','low')]),
'4.4':(1,[]),
'4.5':(1,[L(C+'4.4',H,'caramelisation')]),
'4.6':(1,[]),
'4.7':(1,[L(C+'4.6',H,'dextrinisation')]),
'5.b':(1,[]),
'5.0':(1,[L('hom-vitamins-minerals-s2.0.0',H,'water-soluble vitamins dissolve in water')]),
'5.1':(1,[]),'5.2':(1,[]),'5.3':(1,[]),
'5.4':(1,[L(C+'5.0',H,'nutrients dissolving in cooking water')]),
'6.b':(1,[]),'6.0':(1,[]),
'6.1':(1,[L(C+'5.1',H,'vitamin C destroyed by heat')]),
'6.2':(1,[L('hom-vitamins-minerals-s2.5.2',H,'alkalis destroy vitamin C')]),
'6.3':(2,[L(C+'5.4',H,'loss from water and long cooking')]),
'6.4':(1,[L(C+'5.0',H,'nutrients dissolve into cooking water')]),
}
txt=open(P+'packs/hom-cooking-methods-s1.t1g1.txt').read()
lines=txt.split('CANDIDATES')[0].split('\n')
tids=re.findall(r'^\[([^\]]+)\]',txt.split('CANDIDATES')[0],re.M)
allids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
assert [t[len(C):] for t in tids]==list(d.keys()),(len(tids),len(d))
out={C+k:{"cost":v[0],"needs":v[1]} for k,v in d.items()}
for k,v in out.items():
    for n in v['needs']: assert n['id'] in allids and n['id']!=k,n
json.dump(out,open(P+'point-links/hom-cooking-methods-s1.t1g1.json','w'),indent=1)
print(len(out),sum(len(v['needs']) for v in out.values()),sum(v['cost']==2 for v in out.values()),sum(n['confidence']=='low' for v in out.values() for n in v['needs']))
