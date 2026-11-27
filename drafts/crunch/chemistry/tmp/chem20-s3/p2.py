import json,re
D='/Users/gabrielwhelan/barebones/.claude/worktrees/crunch-chem-home/drafts/crunch/chemistry/'
E,H='essential','helpful'
def L(i,s,w,c='high'): return {"id":i,"strength":s,"why":w,"confidence":c}
R={
"chem20-s3.0.b":(1,[]),
"chem20-s3.0.0":(1,[]),
"chem20-s3.0.1":(1,[]),
"chem20-s3.0.2":(2,[]),
"chem20-s3.0.3":(1,[]),
"chem20-s3.0.4":(1,[]),
"chem20-s3.0.5":(2,[L("chem20-s3.0.2",H,"order of treatment steps")]),
"chem20-s3.1.b":(1,[]),
"chem20-s3.1.0":(1,[]),
"chem20-s3.1.1":(1,[]),
"chem20-s3.2.b":(1,[]),
"chem20-s3.2.0":(1,[]),
"chem20-s3.2.1":(1,[]),
"chem20-s3.2.2":(1,[L("chem20-s3.2.1",E,"aluminium sulfate as flocculant"),L("chem20-s3.2.0",E,"charges keep particles apart")]),
"chem20-s3.2.3":(2,[L("chem20-s3.2.1",E,"aluminium sulfate as flocculant")]),
"chem20-s3.2.4":(1,[L("chem20-s3.2.2",H,"particles clump together")]),
"chem20-s3.3.b":(1,[]),
"chem20-s3.3.0":(1,[L("chem20-s3.2.4",E,"flocs formed in flocculation")]),
"chem20-s3.3.1":(1,[L("chem20-s3.3.0",H,"settling tanks")]),
"chem20-s3.4.b":(1,[]),
"chem20-s3.4.0":(1,[]),
"chem20-s3.4.1":(1,[L("chem20-s3.4.0",E,"sand filter beds")]),
"chem20-s3.4.2":(1,[]),
"chem20-s3.4.3":(1,[L("chem20-s3.4.2",E,"microfiltration pore size")]),
"chem20-s3.5.b":(1,[]),
"chem20-s3.5.0":(1,[L("chem14-s1.5.0",H,"oxidising disinfectants kill microorganisms","low")]),
"chem20-s3.5.1":(2,[L("chem19-s1.0.2",H,"double arrow means equilibrium","low")]),
"chem20-s3.5.2":(1,[L("chem20-s3.5.1",H,"chlorine disinfectant added")]),
"chem20-s3.5.3":(1,[]),
"chem20-s3.5.4":(1,[]),
"chem20-s3.5.5":(1,[L("chem20-s3.5.1",H,"chlorine added to water")]),
"chem20-s3.5.6":(1,[L("chem20-s3.5.5",E,"chlorine reacts with organic matter")]),
"chem20-s3.6.b":(1,[]),
"chem20-s3.6.0":(1,[]),
"chem20-s3.6.1":(1,[L("chem20-s3.5.3",H,"Cryptosporidium resists chlorine")]),
"chem20-s3.6.2":(1,[]),
"chem20-s3.6.3":(1,[L("chem20-s3.5.2",E,"chlorine residual protects pipes")]),
"chem20-s3.6.4":(1,[L("chem20-s3.0.4","helpful","suspended particles removed first")]),
"chem20-s3.6.5":(1,[L("chem20-s3.6.1",H,"UV effective against Cryptosporidium")]),
"chem20-s3.7.b":(1,[]),
"chem20-s3.7.0":(1,[]),
"chem20-s3.7.1":(2,[]),
"chem20-s3.7.2":(1,[L("chem20-s3.7.1",E,"fluorapatite formed in enamel")]),
"chem20-s3.7.3":(1,[]),
"chem20-s3.7.4":(1,[]),
"chem20-s3.7.5":(1,[L("chem20-s3.7.4",H,"fluoride level limit")]),
"chem20-s3.7.6":(1,[]),
"chem20-s3.8.b":(1,[L("chem19-s1.5.2",H,"pH scale acidic neutral basic")]),
"chem20-s3.8.0":(1,[L("chem19-s1.5.2",H,"pH scale acidic neutral basic")]),
"chem20-s3.8.1":(1,[L("chem19-s1.5.2",H,"acidic water has low pH")]),
"chem20-s3.8.2":(1,[L("chem20-s3.8.1",H,"lime added raises pH")]),
"chem20-s3.8.3":(1,[L("chem14-s1.6.0",H,"corrosion of metals")]),
"chem20-s3.8.4":(1,[]),
"chem20-s3.8.5":(1,[L("chem20-s3.2.1",H,"flocculation","low")]),
"chem20-s3.9.b":(1,[]),
"chem20-s3.9.0":(1,[]),
"chem20-s3.9.1":(1,[]),
"chem20-s3.9.2":(1,[]),
"chem20-s3.9.3":(1,[]),
"chem20-s3.9.4":(1,[]),
"chem20-s3.9.5":(1,[]),
"chem20-s3.9.6":(1,[L("chem20-s2.1.1",H,"environmental cost of treatment")]),
}
out={k:{"cost":c,"needs":n} for k,(c,n) in R.items()}
txt=open(D+'packs/chem20-s3.t1g1.txt').read()
ids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
tg=re.findall(r'^\[(chem20-s3\.[^\]]+)\]',txt,re.M)
assert list(out)==tg,(set(tg)^set(out))
for k,v in out.items():
    for n in v['needs']: assert n['id'] in ids and n['id']!=k,(k,n)
json.dump(out,open(D+'point-links/chem20-s3.t1g1.json','w'),ensure_ascii=False,indent=1)
json.load(open(D+'point-links/chem20-s3.t1g1.json'))
print(len(out),sum(len(v['needs']) for v in out.values()),sum(v['cost']==2 for v in out.values()),sum(n['confidence']=='low' for v in out.values() for n in v['needs']))
