import json,re,sys
pk,out=sys.argv[1],sys.argv[2]
t=open(pk).read()
tg=t.split('CANDIDATES')[0]
ids=re.findall(r'^\[([^\]]+)\]',tg,re.M)
allids=set(re.findall(r'^\[([^\]]+)\]',t,re.M))
d=json.load(open(out))
assert list(d)==ids,(set(ids)^set(d))
n=sum(len(v['needs']) for v in d.values())
for k,v in d.items():
    for x in v['needs']: assert x['id'] in allids and x['id']!=k,(k,x)
print(len(ids),n,sum(v['cost']==2 for v in d.values()),sum(x['confidence']=='low' for v in d.values() for x in v['needs']))
