import json,re,sys
n=sys.argv[1]
base='/Users/gabrielwhelan/barebones/.claude/worktrees/crunch-chem-home/drafts/crunch/home-economics/'
t=open(base+'packs/'+n+'.txt').read()
ids=re.findall(r'^\[([^\]]+)\]',t,re.M)
tgt=[]
sec=None
for l in t.split('\n'):
    if l.startswith('TARGET'): sec='T'
    elif l.startswith('CANDIDATES'): sec='C'
    m=re.match(r'\[([^\]]+)\]',l)
    if m and sec=='T': tgt.append(m.group(1))
o=json.load(open(base+'point-links/'+n+'.json'))
assert list(o)==tgt,(set(tgt)^set(o))
bad=[x['id'] for v in o.values() for x in v['needs'] if x['id'] not in ids]
assert not bad,bad
selfl=[k for k,v in o.items() if any(x['id']==k for x in v['needs'])]
assert not selfl
ln=sum(len(v['needs']) for v in o.values())
print(n,len(o),ln,sum(v.get('cost')==2 for v in o.values()),sum(x['confidence']=='low' for v in o.values() for x in v['needs']))
