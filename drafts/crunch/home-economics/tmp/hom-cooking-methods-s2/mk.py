import json,re
P='hom-cooking-methods-s2.t1g1'
S='hom-cooking-methods-s2.'
def L(i,s,w,c='high'): return {"id":S+i,"strength":s,"why":w,"confidence":c}
d={
"0.b":(1,[]),"0.0":(1,[]),"0.1":(1,[]),"0.2":(1,[]),"0.3":(1,[]),"0.4":(1,[]),"0.5":(1,[L("0.0","helpful","micro-organisms destroyed by heat","low")]),
"1.b":(1,[]),"1.0":(1,[]),
"1.1":(1,[L("2.6","helpful","heat travels inwards through food","low")]),
"1.2":(1,[]),"1.3":(1,[]),"1.4":(1,[L("0.0","helpful","bacteria in food","low")]),
"2.b":(1,[]),"2.0":(1,[L("2.b","helpful","conduction through molecules")]),
"2.1":(2,[L("2.b","helpful","conduction")]),
"2.2":(1,[L("2.b","helpful","conduction"),L("2.1","helpful","metal pan base conducts")]),
"2.3":(1,[L("2.2","essential","pan-based conduction")]),
"2.4":(1,[L("2.b","helpful","conduction into meat")]),
"2.5":(1,[L("2.1","helpful","metal tins conduct")]),
"2.6":(1,[L("2.0","helpful","molecule by molecule conduction")]),
"2.7":(1,[L("2.b","helpful","conduction")]),
"3.b":(1,[]),"3.0":(1,[L("3.b","helpful","rising and sinking currents")]),
"3.1":(1,[L("3.0","helpful","natural convection in oven")]),
"3.2":(1,[L("3.b","helpful","convection currents")]),
"3.3":(2,[L("3.b","helpful","convection by steam")]),
"3.4":(1,[L("3.b","helpful","convection")]),
"3.5":(1,[L("3.b","helpful","convection currents")]),
"4.b":(1,[]),
"4.0":(1,[L("2.b","helpful","inside cooks by conduction")]),
"4.1":(1,[L("4.b","helpful","radiant heat")]),
"4.2":(1,[L("4.b","helpful","radiant heat")]),
"4.3":(2,[L("4.b","helpful","radiant heat")]),
"4.4":(1,[L("4.b","helpful","radiant heat")]),
"4.5":(1,[L("4.b","helpful","radiation")]),
"5.b":(1,[]),
"5.0":(2,[L("2.b","helpful","conduction"),L("3.b","helpful","convection"),L("4.b","helpful","radiation")]),
"5.1":(1,[L("2.2","helpful","pan base conduction"),L("3.b","helpful","convection in water")]),
"5.2":(2,[]),
"5.3":(1,[L("2.b","helpful","conduction"),L("5.2","essential","heat made in outer layer")]),
"6.b":(1,[]),
"6.0":(2,[L("1.3","helpful","food type governs method")]),
"6.1":(1,[L("1.3","helpful","delicate foods gentle heat")]),
"6.2":(1,[L("0.1","helpful","protein denatures and sets")]),
"6.3":(1,[]),
"6.4":(1,[L("0.2","helpful","starch gelatinises")]),
"6.5":(1,[]),"6.6":(1,[]),"6.7":(2,[]),
}
out={S+k:{"cost":c,"needs":n} for k,(c,n) in d.items()}
txt=open('packs/'+P+'.txt').read()
tg=re.findall(r'^\[([^\]]+)\]',txt,re.M)
assert list(out)==tg,(set(tg)^set(out))
for k,v in out.items():
  for n in v['needs']: assert n['id'] in tg and n['id']!=k
json.dump(out,open('point-links/'+P+'.json','w'),indent=1)
print(len(out),sum(len(v['needs']) for v in out.values()),sum(v['cost']==2 for v in out.values()),sum(n['confidence']=='low' for v in out.values() for n in v['needs']))
