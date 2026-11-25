import json,re
D='/Users/gabrielwhelan/barebones/.claude/worktrees/history-crunch/drafts/crunch/history/'
H='helpful'
def n(i,w,c='high'): return {"id":"hist-eur3-s"+i,"strength":H,"why":w,"confidence":c}
links={
"11.1.1":[n("2.7.1","Mein Kampf written in prison"),n("2.2.2","the Versailles settlement")],
"11.1.2":[n("2.1.5","the stab in the back myth"),n("2.4.2","the 1923 hyperinflation")],
"11.1.3":[n("2.7.1","Lebensraum as set out in Mein Kampf","low")],
"11.1.4":[n("2.14.1","Hitler appointed Chancellor 30 January 1933")],
"11.5.1":[n("2.11.2","Goebbels as propaganda chief","low")],
}
P=D+'packs/hist-eur3-s11.t1g3.txt'
txt=open(P).read()
tgt=re.findall(r'^\[(hist-eur3-s11\.[^\]]+)\]',txt.split('CANDIDATES')[0],re.M)
allids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
cand=set(re.findall(r'^\[(hist-eur3-s2\.[^\]]+)\]',txt,re.M))
assert all("hist-eur3-s"+k in tgt for k in links)
out={t:{"needs":links.get(t[len("hist-eur3-s"):],[])} for t in tgt}
for v in out.values():
    for x in v["needs"]: assert x["id"] in cand
json.dump(out,open(D+'point-links/hist-eur3-s11.t1g3.json','w'),indent=0)
chk=json.load(open(D+'point-links/hist-eur3-s11.t1g3.json'))
assert list(chk)==tgt
print(len(out),sum(len(v["needs"]) for v in out.values()),sum(x["confidence"]=="low" for v in out.values() for x in v["needs"]))
