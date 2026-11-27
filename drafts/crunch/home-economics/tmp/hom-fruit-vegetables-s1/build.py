import json,re
P='/Users/gabrielwhelan/barebones/.claude/worktrees/crunch-chem-home/drafts/crunch/home-economics/'
C='hom-fruit-vegetables-s1.'
def L(i,s,w,c='high'): return {"id":i,"strength":s,"why":w,"confidence":c}
H,E='helpful','essential'
d={
'0.b':(1,[]),
'0.0':(2,[L('hom-vitamins-minerals-s1.2.1',H,'beta-carotene converts to vitamin A')]),
'0.1':(1,[]),'0.2':(1,[]),
'0.3':(2,[L('hom-vitamins-minerals-s2.10.b',H,'folate as a B vitamin','low')]),
'0.4':(1,[]),'0.5':(1,[]),'0.6':(1,[]),'0.7':(1,[]),'0.8':(1,[]),
'1.b':(1,[]),'1.0':(1,[]),'1.1':(1,[]),'1.2':(1,[]),'1.3':(1,[]),'1.4':(1,[]),'1.5':(2,[]),
'2.b':(1,[]),'2.0':(2,[]),'2.1':(1,[]),
'2.2':(1,[L('hom-carbohydrates-s3.3.b',H,'fibre as non-starch polysaccharide')]),
'2.3':(2,[L('hom-carbohydrates-s3.3.b',H,'what dietary fibre is')]),
'2.4':(1,[L('hom-vitamins-minerals-s1.2.1',H,'beta-carotene as provitamin A')]),
'2.5':(2,[]),'2.6':(2,[]),'2.7':(1,[]),
'3.b':(1,[]),'3.0':(1,[]),
'3.1':(1,[L('hom-carbohydrates-s3.2.b',H,'starch','low')]),
'3.2':(1,[L('hom-carbohydrates-s3.3.b',H,'cellulose and pectin as fibre')]),
'3.3':(1,[]),'3.4':(1,[]),
'3.5':(1,[L('hom-vitamins-minerals-s1.2.1',H,'beta-carotene converted to vitamin A')]),
'3.6':(1,[]),'3.7':(1,[]),
'4.b':(1,[]),
'4.0':(1,[L(C+'2.7',H,'high water content, low energy density')]),
'4.1':(1,[L(C+'2.1',H,'vegetables low in fat')]),
'4.2':(1,[L(C+'2.0',H,'pulses and soya protein')]),
'4.3':(2,[L('hom-vitamins-minerals-s2.2.4',H,'vitamin C as antioxidant')]),
'4.4':(1,[L('hom-vitamins-minerals-s2.6.0',H,'B12 only in animal foods')]),
'4.5':(1,[L(C+'1.4',H,'dried fruit concentrated in sugar')]),
'4.6':(1,[]),
'5.b':(1,[]),
'5.0':(2,[L('hom-energy-nutrition-s4.6.b',H,'Food Pyramid shelves')]),
'5.1':(1,[L(C+'5.0',H,'the 5 to 7 servings target')]),
'5.2':(1,[]),
'5.3':(1,[L('hom-energy-nutrition-s4.6.2',H,'top shelf of the Pyramid')]),
'5.4':(1,[L(C+'5.0',H,'recommended number of servings')]),
'5.5':(2,[L(C+'5.4',H,'survey results being commented on')]),
'6.b':(1,[]),'6.0':(1,[]),'6.1':(1,[]),'6.2':(1,[]),
'6.3':(1,[L('hom-carbohydrates-s3.2.b',H,'starchy carbohydrate foods','low')]),
'6.4':(1,[]),'6.5':(1,[]),'6.6':(1,[]),'6.7':(1,[]),
}
txt=open(P+'packs/hom-fruit-vegetables-s1.t1g1.txt').read()
tids=re.findall(r'^\[([^\]]+)\]',txt.split('CANDIDATES')[0],re.M)
allids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
assert [t[len(C):] for t in tids]==list(d.keys()),(len(tids),len(d))
out={C+k:{"cost":v[0],"needs":v[1]} for k,v in d.items()}
for k,v in out.items():
    for n in v['needs']: assert n['id'] in allids and n['id']!=k,n
json.dump(out,open(P+'point-links/hom-fruit-vegetables-s1.t1g1.json','w'),indent=1)
print(len(out),sum(len(v['needs']) for v in out.values()),sum(v['cost']==2 for v in out.values()),sum(n['confidence']=='low' for v in out.values() for n in v['needs']))
