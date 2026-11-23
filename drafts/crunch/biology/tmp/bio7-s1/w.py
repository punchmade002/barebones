import json,re
P='bio7-s1.'
def n(i,s,w,c='high'): return {"id":i,"strength":s,"why":w,"confidence":c}
d={
"0.b":(1,[]),
"0.0":(1,[]),
"0.1":(1,[n(P+"0.0","helpful","membrane-bound organelles defined")]),
"0.2":(1,[]),
"1.b":(1,[]),
"1.0":(1,[n(P+"0.0","helpful","cytoplasm defined")]),
"1.1":(1,[n("bio5-s1.1.4","helpful","shared cell features","low")]),
"1.2":(1,[n("bio5-s1.3.0","helpful","respiration releases energy as ATP")]),
"1.3":(2,[n(P+"1.1","helpful","shared features across cells","low")]),
"2.b":(1,[]),
"2.0":(2,[n(P+"0.0","helpful","prokaryotes lack nucleus")]),
"2.1":(1,[]),
"2.2":(1,[n(P+"2.1","helpful","chromosome shape","low")]),
"2.3":(2,[n(P+"2.1","helpful","circular main chromosome")]),
"2.4":(1,[n(P+"2.3","essential","what plasmids are")]),
"3.b":(1,[]),
"3.0":(1,[n(P+"0.1","helpful","membrane-bound organelles in eukaryotes")]),
"3.1":(2,[n("bio5-s1.3.0","helpful","respiration releases energy")]),
"3.2":(1,[n(P+"3.3","essential","70S ribosome size")]),
"3.3":(1,[n(P+"1.1","helpful","ribosomes in both cell types")]),
"3.4":(2,[n(P+"3.3","essential","70S versus 80S ribosomes")]),
"4.b":(1,[]),
"4.0":(1,[n(P+"0.2","helpful","micrometre unit")]),
"4.1":(2,[]),
"4.2":(1,[]),
"4.3":(2,[n("bio5-s1.7.4","helpful","binary fission as asexual reproduction")]),
"4.4":(1,[]),
"5.b":(1,[]),
"5.0":(1,[n(P+"4.0","helpful","bacterial size 1-10 µm")]),
"5.1":(1,[n(P+"4.1","helpful","plant cell wall","low")]),
"5.2":(2,[n(P+"2.0","helpful","nucleoid")]),
"5.3":(2,[n(P+"2.0","essential","nuclear envelope and pores")]),
"5.4":(2,[n(P+"2.0","helpful","nucleoid and nuclear envelope","low")]),
"6.b":(1,[]),
"6.0":(1,[n(P+"0.1","essential","eukaryotes enclose DNA in nucleus")]),
"6.1":(1,[n(P+"4.0","essential","cell size ranges")]),
"6.2":(1,[n(P+"3.0","essential","only eukaryotes have organelles")]),
"6.3":(2,[n(P+"4.1","essential","cell wall differences")]),
}
out={P+k:{"cost":c,"needs":x} for k,(c,x) in d.items()}
t=open('points/bio7-s1.txt').read()
tgt=re.findall(r'^\[(bio7-s1\.[^\]]+)\]',t.split('CANDIDATES')[0],re.M)
allids=set(re.findall(r'^\[([^\]]+)\]',t,re.M))
assert list(out)==tgt,(set(tgt)^set(out))
for v in out.values():
  for x in v['needs']: assert x['id'] in allids
json.dump(out,open('point-links/bio7-s1.json','w'),indent=1)
L=sum(len(v['needs']) for v in out.values())
print(len(out),L,sum(v['cost']==2 for v in out.values()),sum(x['confidence']=='low' for v in out.values() for x in v['needs']))
