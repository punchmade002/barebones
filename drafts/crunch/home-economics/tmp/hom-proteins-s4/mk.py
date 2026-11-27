import json,re
P='hom-proteins-s4.t1g1'
def L(i,s,w,c='high'): return {"id":i if i.startswith('hom-') else 'hom-proteins-s4.'+i,"strength":s,"why":w,"confidence":c}
d={
"0.b":(1,[]),"0.0":(1,[]),"0.1":(2,[]),"0.2":(1,[]),"0.3":(1,[]),
"1.b":(1,[L("hom-proteins-s3.3.2","helpful","globular protein")]),
"1.0":(1,[L("hom-proteins-s3.3.3","helpful","albumin as globular example","low")]),
"1.1":(1,[L("2.0","helpful","casein in milk")]),
"1.2":(1,[L("hom-proteins-s3.3.2","helpful","soluble globular protein")]),
"2.b":(1,[]),"2.0":(1,[]),"2.1":(1,[]),
"2.2":(2,[L("hom-proteins-s3.0.1","helpful","rennin acts on protein","low")]),
"3.b":(1,[L("6.1","helpful","collagen")]),
"3.0":(1,[L("6.1","helpful","collagen source")]),
"3.1":(1,[L("3.0","helpful","gelatine formation")]),
"3.2":(1,[L("3.0","helpful","gelatine from animals")]),
"4.b":(1,[]),"4.0":(1,[]),
"4.1":(1,[L("hom-proteins-s3.4.3","helpful","gliadin and glutenin form gluten")]),
"4.2":(2,[L("4.1","essential","gluten forms with water")]),
"4.3":(1,[L("4.0","helpful","wheat gluten")]),
"5.b":(1,[]),
"5.0":(1,[L("1.0","helpful","albumin")]),
"5.1":(1,[L("2.2","helpful","rennin coagulates casein")]),
"5.2":(1,[L("3.0","helpful","gelatine from collagen")]),
"5.3":(1,[L("4.2","helpful","gluten traps gas")]),
"6.b":(1,[]),"6.0":(1,[]),"6.1":(1,[]),
"6.2":(2,[L("6.1","essential","collagen"),L("3.0","helpful","gelatine formation")]),
"6.3":(1,[L("hom-proteins-s3.3.1","helpful","elastin as fibrous protein","low")]),
}
out={'hom-proteins-s4.'+k:{"cost":c,"needs":n} for k,(c,n) in d.items()}
txt=open('packs/'+P+'.txt').read()
tg=re.findall(r'^\[([^\]]+)\]',txt.split('CANDIDATES')[0],re.M)
allids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
assert list(out)==tg,(set(tg)^set(out))
for k,v in out.items():
  for n in v['needs']: assert n['id'] in allids and n['id']!=k,n
json.dump(out,open('point-links/'+P+'.json','w'),indent=1)
print(len(out),sum(len(v['needs']) for v in out.values()),sum(v['cost']==2 for v in out.values()),sum(n['confidence']=='low' for v in out.values() for n in v['needs']))
