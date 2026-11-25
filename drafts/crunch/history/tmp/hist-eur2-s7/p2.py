import json,re
P='/Users/gabrielwhelan/barebones/drafts/crunch/history/'
def L(i,s,w,c='high'): return {"id":i,"strength":s,"why":w,"confidence":c}
H,E='helpful','essential'
p='hist-eur2-s7.'
d={
p+"0.b":(1,[]),
p+"0.0":(1,[]),
p+"0.1":(1,[L("hist-eur2-s1.0.6",H,"Lorraine taken from France in 1871")]),
p+"0.2":(2,[]),
p+"0.3":(2,[]),
p+"0.4":(1,[]),
p+"0.5":(1,[]),
p+"0.6":(2,[L("hist-eur2-s1.0.6",H,"the French indemnity of 1871")]),
p+"0.7":(1,[]),
p+"0.8":(1,[]),
p+"0.9":(1,[]),
p+"0.10":(1,[]),
p+"1.b":(1,[]),
p+"1.0":(2,[L(p+"0.1",H,"Lorraine iron ore")]),
p+"1.1":(2,[]),
p+"1.2":(2,[]),
p+"1.3":(1,[]),
p+"1.4":(1,[]),
p+"1.5":(1,[]),
p+"1.6":(1,[]),
p+"2.b":(1,[]),
p+"2.0":(1,[]),
p+"2.1":(2,[]),
p+"2.2":(1,[L("hist-eur2-s1.0.0",H,"the Franco-Prussian War")]),
p+"2.3":(1,[]),
p+"2.4":(2,[]),
p+"2.5":(1,[L(p+"2.0",H,"Alfred Krupp's works")]),
p+"2.6":(1,[]),
p+"3.0":(1,[L(p+"2.5",E,"Friedrich Alfred Krupp, her father")]),
p+"3.1":(1,[L(p+"3.0",H,"Bertha Krupp inheriting the firm")]),
p+"3.2":(2,[L(p+"3.1",H,"Gustav's chairing the firm")]),
p+"3.3":(1,[]),
p+"3.4":(2,[]),
p+"3.5":(2,[L(p+"2.4",H,"Krupp paternalism")]),
p+"4.0":(1,[]),
p+"4.1":(1,[]),
p+"4.2":(1,[]),
p+"4.3":(2,[]),
p+"4.4":(1,[]),
p+"4.5":(1,[]),
p+"5.0":(1,[]),
p+"5.1":(1,[L(p+"5.0",H,"the SPD's formation")]),
p+"5.2":(2,[L(p+"5.1",H,"the Anti-Socialist Law lapsing")]),
p+"5.3":(1,[L("hist-eur2-s1.0.4",H,"the Bundesrat's role",'low')]),
p+"5.4":(1,[]),
p+"5.5":(1,[]),
p+"6.0":(1,[]),
p+"6.1":(2,[L("hist-eur2-s1.1.3",H,"the 1879 tariff"),L(p+"6.0",H,"the Junkers")]),
p+"6.2":(1,[L(p+"6.1",H,"the grain tariffs")]),
p+"6.3":(2,[]),
p+"6.4":(2,[L(p+"6.0",H,"Junker dominance")]),
p+"6.5":(2,[L(p+"6.4",E,"Wehler's thesis being answered")]),
p+"7.0":(1,[L(p+"5.0",H,"the SPD workers were weaned from")]),
p+"7.1":(1,[L("hist-eur2-s1.7.1",H,"Wilhelm II's dispute with Bismarck")]),
p+"7.2":(1,[L(p+"2.4",E,"Krupp's housing, schools and funds")]),
p+"7.3":(1,[L(p+"5.3",H,"the SPD's rising vote")]),
p+"7.4":(1,[L(p+"6.0",H,"the Prussian three-class vote")]),
p+"8.0":(1,[]),
p+"8.1":(1,[]),
p+"8.2":(1,[L(p+"7.0",H,"Bismarck's social insurance")]),
p+"8.3":(2,[L(p+"7.2",H,"company paternalist welfare")]),
p+"8.4":(1,[L(p+"2.2",H,"Krupp's arms production")]),
p+"8.5":(2,[]),
}
src=open(P+'packs/hist-eur2-s7.t1g1.txt').read()
ids=re.findall(r'^\[([^\]]+)\]',src.split('CANDIDATES')[0],re.M)
allids=set(re.findall(r'^\[([^\]]+)\]',src,re.M))
assert ids==list(d),(set(ids)^set(d))
out={k:{"cost":c,"needs":n} for k,(c,n) in d.items()}
for k,v in out.items():
  for n in v["needs"]: assert n["id"] in allids and n["id"]!=k,(k,n)
json.dump(out,open(P+'point-links/hist-eur2-s7.t1g1.json','w'),ensure_ascii=False,indent=1)
o=json.load(open(P+'point-links/hist-eur2-s7.t1g1.json'))
print(len(o),sum(len(v["needs"]) for v in o.values()),sum(v["cost"]==2 for v in o.values()),sum(n["confidence"]=="low" for v in o.values() for n in v["needs"]))
