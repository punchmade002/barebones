import json,re
H,E='helpful','essential'
def n(i,s,w,c='high'): return {"id":i,"strength":s,"why":w,"confidence":c}
ids="0.b 0.0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 1.b 1.0 1.1 1.2 1.3 1.4 2.b 2.0 2.1 2.2 2.3 2.4 2.5 3.b 3.0 3.1 3.2 3.3 4.b 4.0 4.1 4.2 4.3 4.4 4.5 4.6 4.7 5.b 5.0 5.1 5.2 5.3 5.4 5.5 5.6 6.b 6.0 6.1 6.2 6.3 6.4 7.b 7.0 7.1 7.2 8.b 8.0 8.1".split()
d={k:[] for k in ids}
d["0.b"]=[n('chem14-s1.0.0',H,'oxidation as gaining oxygen')]
d["0.0"]=[n('chem24-s2.12.2',H,'recrystallising benzoic acid from water','low')]
d["0.1"]=[n('chem24-s2.16.0',H,'carboxylate ion from carboxylic acid')]
d["0.4"]=[n('chem14-s1.1.0',E,'reduction is gain of electrons')]
d["1.b"]=[n('chem14-s1.3.0',H,'oxidising agent')]
d["1.2"]=[n('chem11-s1.1.1',H,'bases and basic solution','low')]
d["2.1"]=[n('chem14-s1.3.1',H,'sulfite acting as reducing agent','low')]
d["2.3"]=[n('chem24-s2.12.2',H,'benzoic acid less soluble when cold')]
d["3.0"]=[n('chem24-s2.12.4',E,'benzoate salt is soluble in water'),n('chem24-s2.12.2',H,'benzoic acid slightly soluble when cold')]
d["3.1"]=[n('chem11-s1.8.b',H,'acid reacts with carbonate')]
d["3.2"]=[n('chem14-s1.3.1',E,'reducing agent reduces MnO2'),n('chem14-s1.16.3',H,'oxidation numbers of manganese','low')]
d["4.1"]=[n('chem24-s2.12.2',E,'benzoic acid solubility hot versus cold')]
d["8.1"]=[n('chem14-s1.3.0',H,'oxidising agent','low')]
out={'chem25-s3.'+k:{"needs":v} for k,v in d.items()}
base='/Users/gabrielwhelan/barebones/.claude/worktrees/crunch-chem-home/drafts/crunch/chemistry/'
json.dump(out,open(base+'point-links/chem25-s3.t1g2.json','w'),ensure_ascii=False)
txt=open(base+'packs/chem25-s3.t1g2.txt').read()
allids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M)); tg=[];sec=0
for l in txt.split('\n'):
    if l.startswith('TARGET'): sec=1
    elif l.startswith('CANDIDATES'): sec=0
    m=re.match(r'\[([^\]]+)\]',l)
    if m and sec: tg.append(m.group(1))
assert sorted(tg)==sorted(out) and len(tg)==len(out)
for k,v in out.items():
    for x in v['needs']: assert x['id'] in allids and not x['id'].startswith('chem25-s3')
print(len(out),sum(len(v['needs']) for v in out.values()),sum(x['confidence']=='low' for v in out.values() for x in v['needs']))
