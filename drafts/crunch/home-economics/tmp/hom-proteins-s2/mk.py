import json,re,sys
P='hom-proteins-s2.t1g1'
def L(i,s,w,c='high'): return {"id":i,"strength":s,"why":w,"confidence":c}
d={
"hom-proteins-s2.0.b":(1,[L("hom-proteins-s1.0.2","helpful","amino acids as units")]),
"hom-proteins-s2.0.0":(1,[L("hom-proteins-s1.0.2","helpful","amino acids")]),
"hom-proteins-s2.0.1":(1,[L("hom-proteins-s1.3.0","helpful","peptide bond formation")]),
"hom-proteins-s2.0.2":(1,[]),
"hom-proteins-s2.0.3":(1,[L("hom-proteins-s2.1.0","helpful","folding into shape","low")]),
"hom-proteins-s2.0.4":(1,[]),
"hom-proteins-s2.0.5":(1,[L("hom-proteins-s2.0.1","helpful","peptide bonds link blocks")]),
"hom-proteins-s2.1.b":(1,[]),
"hom-proteins-s2.1.0":(1,[L("hom-proteins-s2.0.0","helpful","polypeptide chain from primary structure")]),
"hom-proteins-s2.1.1":(1,[L("hom-proteins-s2.1.0","helpful","bonds folding the chain")]),
"hom-proteins-s2.1.2":(1,[L("hom-proteins-s2.1.1","essential","hydrogen bond")]),
"hom-proteins-s2.1.3":(1,[L("hom-proteins-s2.1.1","helpful","hydrogen bonds")]),
"hom-proteins-s2.1.4":(1,[L("hom-proteins-s2.2.0","helpful","disulphide links explained there"),L("hom-proteins-s2.2.1","helpful","salt bonds explained there")]),
"hom-proteins-s2.2.b":(1,[]),
"hom-proteins-s2.2.0":(2,[]),
"hom-proteins-s2.2.1":(1,[L("hom-proteins-s1.1.3","helpful","side group R")]),
"hom-proteins-s2.2.2":(1,[L("hom-proteins-s2.1.1","helpful","hydrogen bond")]),
"hom-proteins-s2.2.3":(2,[]),
"hom-proteins-s2.2.4":(2,[L("hom-proteins-s2.1.2","helpful","many weak hydrogen bonds"),L("hom-proteins-s2.0.1","helpful","peptide bonds stay intact")]),
"hom-proteins-s2.2.5":(2,[L("hom-proteins-s2.2.0","helpful","disulphide links"),L("hom-proteins-s2.2.1","helpful","salt bonds")]),
"hom-proteins-s2.3.b":(1,[]),
"hom-proteins-s2.3.0":(1,[L("hom-proteins-s2.0.0","helpful","primary structure")]),
"hom-proteins-s2.3.1":(1,[L("hom-proteins-s2.1.0","helpful","coiling by hydrogen bonds")]),
"hom-proteins-s2.3.2":(2,[L("hom-proteins-s2.2.0","helpful","disulphide links")]),
}
out={k:{"cost":c,"needs":n} for k,(c,n) in d.items()}
txt=open('packs/'+P+'.txt').read()
tg=re.findall(r'^\[([^\]]+)\]',txt.split('CANDIDATES')[0],re.M)
allids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
assert list(out)==tg,(set(tg)^set(out))
for k,v in out.items():
  for n in v['needs']: assert n['id'] in allids and n['id']!=k
json.dump(out,open('point-links/'+P.replace('.txt','')+'.json','w'),indent=1)
print(len(out),sum(len(v['needs']) for v in out.values()),sum(v['cost']==2 for v in out.values()),sum(n['confidence']=='low' for v in out.values() for n in v['needs']))
