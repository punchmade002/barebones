import json,re
base='/Users/gabrielwhelan/barebones/.claude/worktrees/crunch-chem-home/drafts/crunch/chemistry/'
def L(i,s,w,c='high'): return {"id":i,"strength":s,"why":w,"confidence":c}
N={}
ids=re.findall(r'^\[(chem21-s5\.[^\]]+)\]',open(base+'packs/chem21-s5.t1g3.txt').read().split('CANDIDATES')[0],re.M)
links={
"chem21-s5.0.1":[L("chem24-s1.2.1","helpful","alcohols family","low")],
"chem21-s5.1.3":[L("chem24-s1.2.1","helpful","alcohol contains one O in OH")],
"chem21-s5.2.b":[L("chem24-s1.7.0","essential","primary alcohol definition"),L("chem24-s1.0.0","helpful","hydrocarbons and double/triple bonds","low")],
"chem21-s5.2.0":[L("chem24-s1.1.0","helpful","alkane general formula")],
"chem21-s5.2.1":[L("chem24-s1.1.4","helpful","alkene general formula")],
"chem21-s5.2.2":[L("chem24-s1.1.5","helpful","alkyne general formula")],
"chem21-s5.2.3":[L("chem24-s1.2.1","helpful","alcohol general formula")],
"chem21-s5.4.b":[L("chem24-s1.2.1","helpful","OH group in alcohols")],
"chem21-s5.4.0":[L("chem24-s1.2.1","helpful","methanol formula","low")],
"chem21-s5.4.2":[L("chem24-s1.6.0","helpful","propan-1-ol formula","low")],
"chem21-s5.4.3":[L("chem24-s1.6.0","helpful","butan-1-ol formula","low")],
"chem21-s5.4.4":[L("chem24-s1.6.2","helpful","pentan-1-ol formula","low")],
"chem21-s5.4.5":[L("chem24-s1.6.2","helpful","hexan-1-ol formula","low")],
"chem21-s5.5.1":[L("chem24-s1.7.0","helpful","primary alcohols")],
"chem21-s5.5.2":[L("chem24-s1.1.4","helpful","ethene and ethyne families","low")],
"chem21-s5.6.b":[L("chem24-s1.0.4","essential","homologous series")],
"chem21-s5.6.0":[L("chem24-s1.0.5","essential","series differ by CH2")],
"chem21-s5.6.1":[L("chem24-s1.1.0","helpful","alkane series")],
"chem21-s5.6.2":[L("chem24-s1.7.0","helpful","primary alcohol series")],
"chem21-s5.6.3":[L("chem24-s1.0.5","essential","each member adds CH2")],
"chem21-s5.6.5":[L("chem24-s1.0.5","helpful","same CH2 added each time")],
"chem21-s5.7.0":[L("chem24-s1.0.5","helpful","per CH2 increment")],
"chem21-s5.8.0":[L("chem24-s1.7.0","helpful","primary alcohols"),L("chem24-s1.1.0","helpful","alkanes","low")],
"chem21-s5.8.1":[L("chem24-s1.2.1","essential","alcohol has C–O–H group")],
"chem21-s5.9.1":[L("chem24-s1.1.4","helpful","alkene and alkyne formulae")],
"chem21-s5.10.0":[L("chem24-s1.7.0","helpful","primary alcohols")],
"chem21-s5.10.5":[L("chem24-s1.0.5","helpful","extra CH2 per member")],
}
out={i:{"needs":links.get(i,[])} for i in ids}
assert set(links)<=set(ids)
json.dump(out,open(base+'point-links/chem21-s5.t1g3.json','w'),ensure_ascii=False)
cand=set(re.findall(r'^\[(chem24-s1\.[^\]]+)\]',open(base+'packs/chem21-s5.t1g3.txt').read(),re.M))
assert all(l['id'] in cand for v in links.values() for l in v)
print(len(ids),sum(len(v) for v in links.values()),sum(l['confidence']=='low' for v in links.values() for l in v))
