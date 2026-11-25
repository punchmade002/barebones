import json,re
P='/Users/gabrielwhelan/barebones/.claude/worktrees/history-crunch/drafts/crunch/history/'
def L(i,s,w,c='high'): return {"id":i,"strength":s,"why":w,"confidence":c}
links={
"0.2":[L("hist-eur4-s4.0.1","helpful","satellite states of the bloc")],
"0.4":[L("hist-eur4-s4.0.3","helpful","order of Soviet leaders")],
"2.b":[L("hist-eur4-s4.0.1","helpful","satellite states under Moscow")],
"2.2":[L("hist-eur4-s4.1.5","helpful","Poland's private farms after 1956","low")],
"2.3":[L("hist-eur4-s4.0.2","helpful","Comecon as Soviet bloc alliance")],
"4.3":[L("hist-eur4-s4.0.7","helpful","arms race, SDI and Afghanistan","low")],
"5.3":[L("hist-eur4-s4.2.6","helpful","1968 invasion of Czechoslovakia")],
"6.0":[L("hist-eur4-s4.2.6","helpful","Warsaw Pact invasion of 1968"),L("hist-eur4-s4.2.2","helpful","Dubcek's market-based reform plans","low")],
"6.2":[L("hist-eur4-s4.0.4","helpful","Hungary 1956 brought Kadar to power","low")],
"6.4":[L("hist-eur4-s4.0.2","helpful","Comecon")],
"7.0":[L("hist-eur4-s4.2.6","helpful","1968 invasion of Czechoslovakia")],
"7.4":[L("hist-eur4-s4.0.7","helpful","Afghanistan invasion December 1979")],
"8.0":[L("hist-eur4-s4.1.3","helpful","who Gomulka was","low")],
"8.6":[L("hist-eur4-s4.6.6","helpful","Round Table talks of 1989")],
"9.0":[L("hist-eur4-s4.8.5","helpful","perestroika")],
"9.1":[L("hist-eur4-s4.8.5","helpful","Law on State Enterprise"),L("hist-eur4-s4.8.6","helpful","Law on Cooperatives")],
"10.2":[L("hist-eur4-s4.18.2","helpful","1990 monetary, economic and social union")],
"11.1":[L("hist-eur4-s4.2.2","helpful","Sik's market reform in 1968","low")],
"11.2":[L("hist-eur4-s4.1.1","helpful","emigration ended by Berlin Wall","low")],
"11.3":[L("hist-eur4-s4.13.6","helpful","Ceausescu's fall","low")],
}
ids=[]
txt=open(P+'packs/hist-eur4-s8.t1g3.txt').read().split('CANDIDATES')
tg=re.findall(r'^\[(hist-eur4-s8\.[^\]]+)\]',txt[0],re.M)
cand=set(re.findall(r'^\[([^\]]+)\]',txt[1],re.M))
out={}
for t in tg:
    k=t.split('s8.')[1]
    out[t]={"needs":links.get(k,[])}
assert all(('hist-eur4-s8.'+k) in out for k in links)
for v in out.values():
    for n in v["needs"]: assert n["id"] in cand
json.dump(out,open(P+'point-links/hist-eur4-s8.t1g3.json','w'),indent=0)
d=json.load(open(P+'point-links/hist-eur4-s8.t1g3.json'))
n=sum(len(v["needs"]) for v in d.values());lo=sum(1 for v in d.values() for x in v["needs"] if x["confidence"]=="low")
print(len(d),len(tg),n,lo)
