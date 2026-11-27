import json,re
P='hom-unemployment-poverty-s1.'
def L(i,s,w,c='high'): return {"id":P+i,"strength":s,"why":w,"confidence":c}
E,H='essential','helpful'
D={
"0.b":(1,[]),
"0.0":(2,[]),
"0.1":(1,[L("0.0",H,"paid employment condition")]),
"0.2":(1,[L("0.0",E,"available-for-work condition")]),
"0.3":(2,[L("0.0",E,"actively-seeking-work condition")]),
"0.4":(1,[L("0.0",E,"availability and seeking conditions")]),
"0.5":(1,[L("0.0",H,"paid employment condition")]),
"1.b":(1,[]),
"1.0":(1,[L("0.0",H,"who counts as employed or unemployed")]),
"1.1":(1,[L("1.0",E,"labour force definition"),L("0.0",H,"unemployed people definition")]),
"1.2":(1,[L("1.1",H,"unemployment rate")]),
"1.3":(2,[L("1.1",H,"unemployment rate")]),
"1.4":(2,[L("1.3",H,"official measure it is contrasted with")]),
"2.b":(1,[]),
"2.0":(1,[]),
"2.1":(1,[L("2.0",H,"short-term unemployment")]),
"2.2":(1,[L("2.0",H,"contrast with short-term")]),
"2.3":(1,[L("2.2",E,"long-term unemployment")]),
"2.4":(1,[]),
"3.b":(1,[]),
"3.0":(2,[L("1.3",H,"Labour Force Survey and standardised rate"),L("1.4",H,"Live Register","low")]),
"3.1":(1,[]),
"3.2":(1,[L("3.1",H,"downturn job losses")]),
"3.3":(2,[L("1.1",H,"unemployment rate")]),
"3.4":(2,[L("1.0",E,"labour force definition")]),
"3.5":(1,[]),
"3.6":(1,[L("2.2",H,"long-term unemployment")]),
"3.7":(1,[]),
}
txt=open('packs/hom-unemployment-poverty-s1.t1g1.txt').read()
ids=re.findall(r'^\[(hom-[^\]]+)\]',txt,re.M)
assert [P+k for k in D]==ids,(len(ids),len(D))
out={P+k:{"cost":c,"needs":n} for k,(c,n) in D.items()}
assert all(l['id'] in ids and l['id']!=k for k,v in out.items() for l in v['needs'])
json.dump(out,open('point-links/hom-unemployment-poverty-s1.t1g1.json','w'),indent=1)
print(len(out),sum(len(v['needs']) for v in out.values()),sum(v['cost']==2 for v in out.values()),sum(l['confidence']=='low' for v in out.values() for l in v['needs']))
