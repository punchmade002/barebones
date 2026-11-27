import json,re
P='hom-energy-nutrition-s3.'
def L(i,s,w,c='high'):
    if '-s' not in i.split('.')[0][-4:] and not i.startswith('hom-'): i=P+i
    if not i.startswith('hom-'): i=P+i
    return {"id":i,"strength":s,"why":w,"confidence":c}
def T(i,s,w,c='high'): return {"id":P+i,"strength":s,"why":w,"confidence":c}
def X(i,s,w,c='high'): return {"id":i,"strength":s,"why":w,"confidence":c}
d={
"0.b":(1,[]),
"0.0":(2,[]),
"0.1":(1,[T("0.0","essential","energy values per gram")]),
"0.2":(1,[]),
"0.3":(1,[]),
"0.4":(1,[X("hom-carbohydrates-s6.0.2","helpful","fibre not digested, little energy")]),
"0.5":(1,[T("0.0","helpful","kJ and kcal values being converted")]),
"1.b":(1,[]),
"1.0":(1,[]),
"1.1":(1,[T("0.0","essential","energy value per gram")]),
"1.2":(1,[T("1.1","essential","results of multiplying")]),
"1.3":(1,[T("0.5","helpful","kJ to kcal conversion")]),
"1.4":(1,[T("1.0","helpful","values per 100 g from tables")]),
"1.5":(1,[T("1.4","essential","scaling to portion")]),
"2.b":(1,[]),
"2.0":(1,[T("1.1","essential","multiply grams by energy value")]),
"2.1":(1,[T("2.0","essential","kJ results being added"),T("0.5","helpful","kJ to kcal conversion","low")]),
"2.2":(1,[T("1.1","essential","multiply grams by energy value")]),
"2.3":(1,[T("2.2","essential","kJ results being added")]),
"2.4":(1,[T("2.1","essential","total energy of sample food")]),
"3.b":(1,[]),
"3.0":(1,[T("1.1","essential","method for calculating kJ")]),
"3.1":(1,[]),
"3.2":(1,[T("0.1","helpful","fat has most energy per gram")]),
"3.3":(1,[]),
"3.4":(1,[T("3.0","helpful","calculate and rank energy values")]),
"4.b":(1,[]),
"4.0":(1,[]),
"4.1":(1,[]),
"4.2":(1,[T("0.3","helpful","empty kilocalories meaning")]),
"4.3":(1,[]),
"5.b":(1,[]),
"5.0":(1,[]),
"5.1":(1,[T("0.1","helpful","fat energy per gram comparison","low")]),
"5.2":(1,[X("hom-lipids-s5.0.1","helpful","adipose tissue as energy store")]),
"5.3":(2,[]),
"5.4":(1,[]),
"6.b":(1,[]),
"6.0":(1,[]),
"6.1":(1,[X("hom-proteins-s8.3.0","helpful","surplus amino acids not stored","low")]),
"6.2":(1,[X("hom-proteins-s8.0.3","helpful","protein used for energy when short")]),
"6.3":(2,[]),
"6.4":(1,[T("0.0","essential","protein and carbohydrate values per gram")]),
"7.b":(1,[]),
"7.0":(1,[T("0.1","helpful","fat energy-dense")]),
"7.1":(1,[T("7.0","helpful","energy density meaning")]),
"7.2":(2,[T("4.3","helpful","starchy food guideline","low")]),
"7.3":(1,[T("7.2","helpful","guidelines being compared")]),
"7.4":(2,[T("1.1","essential","multiply grams by energy value"),T("2.4","helpful","percentage contribution method")]),
}
out={P+k:{"cost":c,"needs":n} for k,(c,n) in d.items()}
json.dump(out,open('point-links/hom-energy-nutrition-s3.t1g1.json','w'),indent=1)
txt=open('packs/hom-energy-nutrition-s3.t1g1.txt').read()
ids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
tg=re.findall(r'^\[([^\]]+)\]',txt.split('CANDIDATES')[0],re.M)
assert sorted(tg)==sorted(out) and len(tg)==len(out)
assert all(n['id'] in ids and n['id']!=k for k,v in out.items() for n in v['needs'])
print(len(out),sum(len(v['needs']) for v in out.values()),sum(v['cost']==2 for v in out.values()),sum(n['confidence']=='low' for v in out.values() for n in v['needs']))
