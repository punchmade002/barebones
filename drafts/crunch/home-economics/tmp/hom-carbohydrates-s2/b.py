import json,re
P='hom-carbohydrates-s2.'
def L(i,s,w,c='high'): return {"id":P+i,"strength":s,"why":w,"confidence":c}
D={
"0.b":(1,[]),
"0.0":(1,[]),
"0.1":(1,[L("0.0","helpful","carbon, hydrogen, oxygen elements")]),
"0.2":(1,[L("0.1","essential","2:1 hydrogen to oxygen ratio")]),
"1.b":(1,[]),
"1.0":(2,[]),
"1.1":(2,[]),
"1.2":(2,[]),
"1.3":(1,[L("1.2","helpful","uses starch, glycogen, cellulose polysaccharides")]),
"1.4":(1,[L("1.0","helpful","uses monosaccharide formula"),L("1.1","helpful","uses disaccharide formula")]),
"1.5":(1,[L("1.b","helpful","sugar unit classification")]),
"1.6":(1,[L("1.b","helpful","uses chemical grouping")]),
"1.7":(2,[L("1.0","helpful","monosaccharide row"),L("1.1","helpful","disaccharide row"),L("1.2","helpful","polysaccharide row")]),
"2.b":(1,[]),
"2.0":(1,[]),
"2.1":(1,[L("1.0","helpful","glucose as monosaccharide")]),
"2.2":(2,[L("2.1","helpful","glucose formula C6H12O6")]),
"2.3":(1,[L("2.2","helpful","hydroxyl groups on glucose ring")]),
"2.4":(1,[L("2.1","essential","uses glucose formula")]),
"2.5":(2,[L("2.2","essential","ring structure being drawn")]),
"2.6":(2,[L("2.5","helpful","numbered ring diagram")]),
"2.7":(1,[L("2.5","helpful","ring diagram of glucose")]),
"3.b":(1,[]),
"3.0":(2,[L("1.0","helpful","monosaccharide formula"),L("1.1","helpful","disaccharide formula")]),
"3.1":(1,[L("3.0","essential","condensation reaction joining units")]),
"3.2":(2,[L("3.0","helpful","condensation joining monosaccharides")]),
"3.3":(2,[L("3.0","essential","condensation repeated at each link")]),
"3.4":(1,[L("3.3","helpful","chains straight or branched")]),
"3.5":(1,[L("3.3","helpful","branched glucose polymer")]),
"3.6":(1,[L("3.3","helpful","straight glucose chains")]),
"3.7":(2,[L("3.1","helpful","glycosidic link labelled")]),
}
txt=open('packs/hom-carbohydrates-s2.t1g1.txt').read()
ids=re.findall(r'^\[(hom-[^\]]+)\]',txt,re.M)
assert [P+k for k in D]==ids,(len(ids),len(D))
out={P+k:{"cost":c,"needs":n} for k,(c,n) in D.items()}
json.dump(out,open('point-links/hom-carbohydrates-s2.t1g1.json','w'),indent=1)
print(len(out),sum(len(v['needs']) for v in out.values()),sum(v['cost']==2 for v in out.values()),sum(l['confidence']=='low' for v in out.values() for l in v['needs']))
