import json,re
d='/Users/gabrielwhelan/barebones/drafts/crunch/biology/exam-tags/'
for q in open(d+'batches/batch-34.txt').read().split():
    t=open(d+'packages/%s.txt'%q).read()
    ids=set(re.findall(r'^\[([^\]]+)\]',t,re.M))
    parts=re.findall(r'^PART (\S+)',t,re.M)
    j=json.load(open(d+'out/%s.json'%q))
    n=0;e=0
    for p,v in j.items():
        if not v:e+=1
        for m in v:
            n+=1
            assert 1<=m['k']<=len(m['of']),(q,p)
            assert all(i in ids for i in m['of']),(q,p)
    print(q,len(parts),n,e,list(j)==parts)
