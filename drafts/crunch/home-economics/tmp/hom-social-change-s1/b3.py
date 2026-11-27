import json,re
P='hom-social-change-s1.'
def T(i,s,w,c='high'): return {"id":P+i,"strength":s,"why":w,"confidence":c}
def X(i,s,w,c='high'): return {"id":i,"strength":s,"why":w,"confidence":c}
d={
"0.b":(1,[]),
"0.0":(1,[]),
"0.1":(1,[T("0.0","essential","urban and rural meanings")]),
"0.2":(1,[T("0.0","helpful","rural area meaning")]),
"0.3":(1,[T("0.2","essential","rural depopulation meaning")]),
"0.4":(1,[T("0.2","helpful","people leaving rural areas")]),
"0.5":(1,[T("0.2","essential","rural population loss")]),
"0.6":(1,[T("0.2","helpful","remote areas losing people")]),
"1.b":(1,[]),
"1.0":(1,[T("0.0","helpful","towns and cities concentrate jobs","low")]),
"1.1":(1,[]),
"1.2":(1,[]),
"1.3":(1,[]),
"1.4":(1,[]),
"1.5":(1,[T("0.4","helpful","young adults leaving countryside")]),
"2.b":(1,[]),
"2.0":(1,[T("0.0","helpful","urban areas and services","low")]),
"2.1":(1,[]),
"2.2":(1,[]),
"2.3":(2,[]),
"2.4":(1,[]),
"2.5":(1,[X("hom-family-society-s3.2.b","helpful","extended family meaning")]),
"2.6":(1,[]),
"3.b":(1,[]),
"3.0":(1,[T("0.4","helpful","younger people moving away")]),
"3.1":(1,[T("0.2","helpful","depopulated areas")]),
"3.2":(1,[]),
"3.3":(1,[T("0.2","helpful","rural decline and emigration")]),
"3.4":(2,[T("0.5","helpful","loss of rural services")]),
"3.5":(1,[T("0.4","helpful","young people leaving")]),
"3.6":(2,[]),
"4.b":(1,[]),
"4.0":(1,[T("0.6","helpful","commuter belts","low")]),
"4.1":(1,[T("2.3","helpful","high urban rents")]),
"4.2":(1,[]),
"4.3":(1,[]),
"4.4":(1,[]),
"4.5":(1,[T("5.1","helpful","rural resettlement schemes","low")]),
"5.b":(1,[]),
"5.0":(1,[]),
"5.1":(1,[T("0.2","helpful","rural communities losing people")]),
"5.2":(1,[]),
"5.3":(1,[]),
"5.4":(1,[]),
"5.5":(1,[]),
"5.6":(1,[]),
"5.7":(2,[T("4.4","helpful","broadband and working from home")]),
"5.8":(1,[]),
"6.b":(1,[]),
"6.0":(1,[]),
"6.1":(1,[T("0.2","helpful","people leaving the area","low")]),
}
out={}
for k,(c,n) in d.items():
    out[P+k]={"cost":c,"needs":n}
json.dump(out,open('point-links/hom-social-change-s1.t1g1.json','w'),indent=1)
txt=open('packs/hom-social-change-s1.t1g1.txt').read()
ids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
tg=re.findall(r'^\[([^\]]+)\]',txt.split('CANDIDATES')[0],re.M)
assert sorted(tg)==sorted(out) and len(tg)==len(out)
assert all(n['id'] in ids and n['id']!=k for k,v in out.items() for n in v['needs'])
print(len(out),sum(len(v['needs']) for v in out.values()),sum(v['cost']==2 for v in out.values()),sum(n['confidence']=='low' for v in out.values() for n in v['needs']))
