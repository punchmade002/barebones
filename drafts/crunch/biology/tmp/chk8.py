import json,re,sys
q=sys.argv[1]
base="/Users/gabrielwhelan/barebones/drafts/crunch/biology/exam-tags/"
pk=open(base+"packages/%s.txt"%q).read()
parts=re.findall(r"^PART (\S+) ",pk,re.M)
ids=set(re.findall(r"^\[([^\]]+)\]",pk,re.M))
d=json.load(open(base+"out/%s.json"%q))
assert list(d)==parts,(list(d),parts)
mp=0;emp=0
for p,l in d.items():
    if not l: emp+=1
    for e in l:
        assert 1<=e["k"]<=len(e["of"]),p
        assert all(i in ids for i in e["of"]),(p,e)
        mp+=1
print(q,len(parts),mp,emp)
