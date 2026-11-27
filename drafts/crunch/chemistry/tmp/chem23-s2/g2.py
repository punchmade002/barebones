import json,re
D='/Users/gabrielwhelan/barebones/.claude/worktrees/crunch-chem-home/drafts/crunch/chemistry/'
def L(i,s,w,c='high'): return {"id":i,"strength":s,"why":w,"confidence":c}
R={"6.b":[L("chem26-s2.0.3","helpful","percentage yield definition")],
"6.2":[L("chem26-s2.0.1","essential","theoretical yield from the equation")],
"6.4":[L("chem26-s2.0.3","essential","percentage yield formula")],
"6.5":[L("chem26-s2.6.b","helpful","causes of low actual yield")]}
pk=open(D+'packs/chem23-s2.t1g2.txt').read()
tg=[];sec=None
for ln in pk.split('\n'):
    if ln.startswith('TARGET'): sec='T'
    elif ln.startswith('CANDIDATES'): sec='C'
    m=re.match(r'\[(\S+?)\]',ln)
    if m and sec=='T': tg.append(m.group(1))
ids=set(re.findall(r'^\[(\S+?)\]',pk,re.M))
out={t:{"needs":R.get(t.split('chem23-s2.')[1],[])} for t in tg}
for v in out.values():
    for n in v['needs']: assert n['id'] in ids
json.dump(out,open(D+'point-links/chem23-s2.t1g2.json','w'),indent=0)
print(len(out),sum(len(v['needs']) for v in out.values()),sum(n['confidence']=='low' for v in out.values() for n in v['needs']))
