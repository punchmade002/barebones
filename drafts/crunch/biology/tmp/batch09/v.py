import json,re
base='/Users/gabrielwhelan/barebones/drafts/crunch/biology/exam-tags/'
for q in open(base+'batches/batch-09.txt').read().split():
    d=json.load(open(base+'out/'+q+'.json'))
    t=open(base+'packages/'+q+'.txt').read()
    ids=set(re.findall(r'^\[([^\]]+)\]',t,re.M))
    parts=re.findall(r'^PART (.+?) \(\d+ marks?\)',t,re.M)
    bad=[i for v in d.values() for m in v for i in m['of'] if i not in ids]
    badk=[m for v in d.values() for m in v if not 1<=m['k']<=len(m['of'])]
    print(q,list(d)==parts,bad,badk,len(d),sum(len(v) for v in d.values()),[k for k,v in d.items() if not v])
