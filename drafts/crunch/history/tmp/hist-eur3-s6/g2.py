import json,re
P='/Users/gabrielwhelan/barebones/.claude/worktrees/history-crunch/drafts/crunch/history/'
def L(i,s,w,c='high'): return {"id":i,"strength":s,"why":w,"confidence":c}
links={
"18.2":[L("hist-eur3-s9.3.6","helpful","the armistice of 22 June")],
"18.3":[L("hist-eur3-s9.3.6","helpful","the 22 June armistice")],
"19.b":[L("hist-eur3-s9.3.b","helpful","the six-week defeat of 1940")],
"19.0":[L("hist-eur3-s9.3.0","helpful","Ardennes thrust of May 1940")],
"19.1":[L("hist-eur3-s9.1.0","helpful","concentrated Panzer divisions")],
"19.2":[L("hist-eur3-s9.3.1","essential","Maginot Line bypassed through Ardennes")],
"19.6":[L("hist-eur3-s9.3.b","helpful","military defeat of May 1940")],
"20.2":[L("hist-eur3-s9.3.6","helpful","the armistice of June 1940")],
"21.0":[L("hist-eur3-s9.17.0","helpful","armoured warfare theory")],
"27.4":[L("hist-eur3-s9.10.1","essential","Operation Torch landings")],
"28.3":[L("hist-eur3-s9.7.b","helpful","German invasion of the USSR")],
"31.1":[L("hist-eur3-s9.23.0","helpful","Churchill becoming Prime Minister")],
"31.3":[L("hist-eur3-s9.24.0","helpful","Churchill and Roosevelt relations","low")],
"32.2":[L("hist-eur3-s9.7.0","essential","Germany invading USSR, Operation Barbarossa")],
"33.1":[L("hist-eur3-s9.11.0","essential","the Normandy landings")],
"34.b":[L("hist-eur3-s9.11.b","helpful","Normandy landings and advance")],
"34.0":[L("hist-eur3-s9.11.0","essential","D-Day landings")],
"34.1":[L("hist-eur3-s9.11.2","helpful","liberation of Paris 25 August")],
"37.1":[L("hist-eur3-s9.3.b","helpful","German attack of 1940")],
"37.4":[L("hist-eur3-s9.3.6","helpful","the armistice")],
"37.7":[L("hist-eur3-s9.3.b","helpful","defeat of 1940","low")],
}
txt=open(P+'packs/hist-eur3-s6.t2g2.txt').read()
ids=re.findall(r'^\[(hist-eur3-s6\.[^\]]+)\]',txt,re.M)
out={i:{"needs":links.get(i[len('hist-eur3-s6.'):],[])} for i in ids}
cand=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
assert len(set(ids))==len(ids)
for v in out.values():
  for n in v["needs"]: assert n["id"] in cand
used={k for k in links}; assert used<={i[13:] for i in ids},used-{i[13:] for i in ids}
json.dump(out,open(P+'point-links/hist-eur3-s6.t2g2.json','w'),ensure_ascii=False)
print(len(ids),sum(len(v["needs"]) for v in out.values()),sum(n["confidence"]=="low" for v in out.values() for n in v["needs"]))
