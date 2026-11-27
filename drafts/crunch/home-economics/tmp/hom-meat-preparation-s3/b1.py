import json,re
P='/Users/gabrielwhelan/barebones/.claude/worktrees/crunch-chem-home/drafts/crunch/home-economics/'
E,H='essential','helpful'
def L(i,s,w,c='high'): return {"id":i,"strength":s,"why":w,"confidence":c}
p='hom-meat-preparation-s3.'
d={
'0.b':(1,[]),
'0.0':(1,[L('hom-meat-preparation-s1.4.3',H,'connective tissue and collagen')]),
'0.1':(1,[L('hom-meat-preparation-s1.4.3',H,'connective tissue content of muscle')]),
'0.2':(1,[]),
'0.3':(2,[]),
'0.4':(1,[L('hom-proteins-s5.0.3',E,'coagulation of protein')]),
'0.5':(1,[L('hom-meat-preparation-s1.5.3',E,'collagen converts in moist cooking')]),
'0.6':(1,[L('hom-meat-preparation-s1.4.4',H,'marbling fat in muscle')]),
'1.b':(2,[]),
'1.0':(2,[L('hom-meat-preparation-s3.0.3',H,'rigor mortis after slaughter')]),
'1.1':(1,[]),
'1.2':(1,[]),
'1.3':(2,[L('hom-proteins-s5.8.1',H,'proteolytic enzymes such as papain')]),
'1.4':(1,[L('hom-proteins-s5.7.1',H,'acid marinade denatures surface protein')]),
'1.5':(1,[L('hom-proteins-s5.7.3',H,'salt acts on protein','low')]),
'1.6':(2,[L('hom-meat-preparation-s1.5.3',E,'collagen converts to gelatine'),L('hom-meat-preparation-s1.5.4',H,'elastin not softened by cooking')]),
'1.7':(1,[L('hom-meat-preparation-s3.1.6',H,'collagen to gelatine in moist cooking')]),
'2.b':(1,[]),
'2.0':(1,[L('hom-proteins-s5.0.0',E,'denaturation of protein')]),
'2.1':(1,[]),
'2.2':(1,[]),
'2.3':(1,[L('hom-meat-preparation-s1.5.3',H,'collagen and gelatine')]),
'2.4':(1,[L('hom-meat-preparation-s1.5.2',E,'myoglobin pigment')]),
'2.5':(1,[]),
'2.6':(2,[L('hom-proteins-s5.4.0',E,'Maillard reaction'),L('hom-meat-preparation-s1.2.7',H,'extractives flavour compounds')]),
'2.7':(2,[]),
'3.b':(1,[]),
'3.0':(1,[]),
'3.1':(1,[]),
'3.2':(1,[]),
'3.3':(1,[]),
'3.4':(1,[L('hom-cooking-methods-s2.2.b',H,'conduction through the pot','low'),L('hom-cooking-methods-s2.3.b',H,'convection in the liquid','low')]),
'4.b':(1,[L('hom-meat-preparation-s1.4.3',H,'connective tissue and collagen')]),
'4.0':(2,[]),
'4.1':(2,[L('hom-meat-preparation-s3.1.6',H,'slow moist cooking','low')]),
'4.2':(1,[L('hom-meat-preparation-s1.5.3',H,'collagen to gelatine')]),
'4.3':(2,[]),
'4.4':(1,[]),
'4.5':(1,[]),
'4.6':(1,[]),
'5.b':(1,[]),
'5.0':(2,[]),
'5.1':(2,[L('hom-cooking-methods-s3.1.2',H,'stewing method')]),
'5.2':(1,[]),
'5.3':(1,[]),
'5.4':(1,[L('hom-cooking-methods-s2.4.b',H,'radiant heat')]),
'5.5':(1,[]),
'5.6':(1,[L('hom-cooking-methods-s2.5.2',H,'microwave heating')]),
'5.7':(1,[]),
'6.b':(1,[]),
'6.0':(2,[]),
'6.1':(1,[]),
'6.2':(1,[]),
'6.3':(1,[]),
'6.4':(1,[L('hom-meat-preparation-s1.2.0',H,'haem iron')]),
'6.5':(1,[L('hom-meat-preparation-s1.2.7',H,'extractives')]),
'6.6':(1,[]),
'6.7':(2,[]),
}
out={p+k:{"cost":c,"needs":n} for k,(c,n) in d.items()}
f=P+'packs/hom-meat-preparation-s3.t1g1.txt'
t=open(f).read()
tgt=[]
ids=set(re.findall(r'^\[([^\]]+)\]',t,re.M))
sec=t.split('CANDIDATES')[0]
tgt=re.findall(r'^\[([^\]]+)\]',sec,re.M)
assert sorted(tgt)==sorted(out),(set(tgt)^set(out))
assert [x for x in tgt]==list(out)
for v in out.values():
  for n in v['needs']: assert n['id'] in ids,n
json.dump(out,open(P+'point-links/hom-meat-preparation-s3.t1g1.json','w'),indent=1)
print(len(out),sum(len(v['needs']) for v in out.values()),sum(v['cost']==2 for v in out.values()),sum(n['confidence']=='low' for v in out.values() for n in v['needs']))
