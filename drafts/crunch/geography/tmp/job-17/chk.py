import json,re,sys
# usage: chk.py spec pack out
spec,pack,out=sys.argv[1:4]
P='geo-economic-environment-'
txt=open(pack).read()
tgt=txt.split('CANDIDATES')[0]
tids=re.findall(r'^\[([^\]]+)\]',tgt,re.M)
allids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
res={}
for line in open(spec):
    line=line.strip()
    if not line: continue
    i,c,*n=line.split('|')
    needs=[]
    for x in (n[0].split(';') if n and n[0] else []):
        p=x.split(',')
        if len(p)==3: p.append('h')
        t,s,w,cf=p
        needs.append({"id":(t if t.startswith("geo-") else (P+t if t.startswith("s") else "geo-"+t)),"strength":"essential" if s=='e' else "helpful","why":w,"confidence":"high" if cf=='h' else "low"})
    res[P+i]={"cost":int(c),"needs":needs} if c!='-' else {"needs":needs}
assert list(res)==tids,(set(tids)^set(res))
for k,v in res.items():
    for n in v['needs']: assert n['id'] in allids and n['id']!=k,(k,n)
json.dump(res,open(out,'w'),indent=0)
print(len(res),sum(len(v['needs']) for v in res.values()),sum(v['cost']==2 for v in res.values()),sum(n['confidence']=='low' for v in res.values() for n in v['needs']))
