import json,re
P='/Users/gabrielwhelan/barebones/.claude/worktrees/history-crunch/drafts/crunch/history/'
def L(i,s,w,c='high'): return {"id":i,"strength":s,"why":w,"confidence":c}
links={
"29.0":[L("hist-eur3-s3.10.4","helpful","German anti-Jewish measures, Nuremberg Laws","low")],
"29.2":[L("hist-eur3-s3.5.0","helpful","the SS under Himmler","low")],
"33.2":[L("hist-eur3-s3.5.2","helpful","the Gestapo secret police")],
"33.3":[L("hist-eur3-s3.5.0","helpful","the SS","low")],
"37.3":[L("hist-eur3-s3.12.3","helpful","Spanish Civil War, German intervention","low")],
}
txt=open(P+'packs/hist-eur3-s6.t2g3.txt').read()
ids=re.findall(r'^\[(hist-eur3-s6\.[^\]]+)\]',txt,re.M)
out={i:{"needs":links.get(i[len('hist-eur3-s6.'):],[])} for i in ids}
cand=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
assert len(set(ids))==len(ids)
for v in out.values():
  for n in v["needs"]: assert n["id"] in cand
used={k for k in links}; assert used<={i[13:] for i in ids},used-{i[13:] for i in ids}
json.dump(out,open(P+'point-links/hist-eur3-s6.t2g3.json','w'),ensure_ascii=False)
print(len(ids),sum(len(v["needs"]) for v in out.values()),sum(n["confidence"]=="low" for v in out.values() for n in v["needs"]))
