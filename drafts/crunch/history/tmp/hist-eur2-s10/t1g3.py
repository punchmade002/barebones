import json,re
H='/Users/gabrielwhelan/barebones/.claude/worktrees/history-crunch/drafts/crunch/history/'
last=[3,6,3,4,3,5,4,2,5,7,5,5,6,3,4,6,2,5,6,3,3,6,4,5,5,5,5]
def L(i,s,w,c): return {"id":i,"strength":s,"why":w,"confidence":c}
links={
"hist-eur2-s10.2.1":[L("hist-eur2-s8.0.7","helpful","uses Russification policy","high")],
"hist-eur2-s10.23.b":[L("hist-eur2-s8.0.0","helpful","tsarist autocracy","low")],
"hist-eur2-s10.23.0":[L("hist-eur2-s8.0.0","helpful","autocracy and Orthodox state church","high")],
"hist-eur2-s10.23.1":[L("hist-eur2-s8.0.4","helpful","1897 census, multinational empire","low")],
"hist-eur2-s10.23.3":[L("hist-eur2-s8.0.6","helpful","Alexander II's assassination","high")],
"hist-eur2-s10.24.1":[L("hist-eur2-s8.0.7","helpful","Alexander III, Nicholas II, Russification","high")],
"hist-eur2-s10.24.4":[L("hist-eur2-s8.8.3","helpful","October Manifesto 1905","high")],
"hist-eur2-s10.25.4":[L("hist-eur2-s8.2.1","helpful","revolutionary parties","low")],
"hist-eur2-s10.25.5":[L("hist-eur2-s8.14.0","helpful","Provisional Government of 1917","high")],
}
out={}
for s,n in enumerate(last):
    for k in ['b']+list(range(n+1)):
        i=f"hist-eur2-s10.{s}.{k}"
        out[i]={"needs":links.get(i,[])}
txt=open(H+'packs/hist-eur2-s10.t1g3.txt').read()
ids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
tg=[i for i in ids if i.startswith('hist-eur2-s10.')]
assert set(tg)==set(out),(set(tg)^set(out))
for v in out.values():
    for n in v['needs']: assert n['id'] in ids
json.dump(out,open(H+'point-links/hist-eur2-s10.t1g3.json','w'),indent=0)
print(len(out),sum(len(v['needs']) for v in out.values()),sum(n['confidence']=='low' for v in out.values() for n in v['needs']))
