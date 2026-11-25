import json,re
P='/Users/gabrielwhelan/barebones/.claude/worktrees/history-crunch/drafts/crunch/history/'
def L(i,s,w,c='high'): return {"id":i,"strength":s,"why":w,"confidence":c}
cost2={"0.3","7.0"}
links={
"7.3":[L("hist-ire5-s4.0.2","helpful","civil rights campaign grievances")],
"8.0":[L("hist-ire5-s4.0.4","helpful","the RUC")],
"8.4":[L("hist-ire5-s4.2.2","helpful","British troops deployed August 1969","low")],
"10.2":[L("hist-ire5-s4.0.2","helpful","civil rights campaign")],
"11.0":[L("hist-ire5-s4.2.1","helpful","Battle of the Bogside")],
"11.1":[L("hist-ire5-s4.2.2","helpful","British army deployment 1969")],
}
txt=open(P+'packs/hist-ire5-s10.t1g1.txt').read().split('CANDIDATES')
tg=re.findall(r'^\[(hist-ire5-s10\.[^\]]+)\]',txt[0],re.M)
cand=set(re.findall(r'^\[([^\]]+)\]',txt[1],re.M))|set(tg)
out={}
for t in tg:
    k=t.split('s10.')[1]
    out[t]={"cost":2 if k in cost2 else 1,"needs":links.get(k,[])}
for v in out.values():
    for n in v["needs"]: assert n["id"] in cand
json.dump(out,open(P+'point-links/hist-ire5-s10.t1g1.json','w'),indent=0)
d=json.load(open(P+'point-links/hist-ire5-s10.t1g1.json'))
print(len(d),len(tg),sum(len(v["needs"]) for v in d.values()),sum(v["cost"]==2 for v in d.values()),sum(1 for v in d.values() for x in v["needs"] if x["confidence"]=="low"))
