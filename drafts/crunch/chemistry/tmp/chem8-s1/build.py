import json,re,sys
# usage: build.py data pack out ; data lines: id|cost|link;link ; link=target,E|H,h|l,why ; ids starting "s." expand to PFX
pfx,data,pack,out=sys.argv[1:5]
ex=lambda x:(pfx+x) if re.match(r's\d*\.',x) and not x.startswith(('chem')) else x
res={}
for ln in open(data):
    ln=ln.rstrip('\n')
    if not ln.strip(): continue
    i,c,l=ln.split('|')
    needs=[]
    for k in filter(None,l.split(';')):
        t,s,cf,w=k.split(',',3)
        needs.append({"id":ex(t),"strength":{'E':'essential','H':'helpful'}[s],"why":w,"confidence":{'h':'high','l':'low'}[cf]})
    key=ex(i)
    assert key not in res,key
    res[key]=({"cost":int(c)} if c!='-' else {})|{"needs":needs}
txt=open(pack).read()
tgt=re.search(r'TARGET.*?\n(.*?)\n\nCANDIDATES',txt,re.S).group(1)
tids=re.findall(r'^\[([^\]]+)\]',tgt,re.M)
allids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
assert list(res)==tids,(set(tids)^set(res),)
n=0
for k,v in res.items():
    for x in v['needs']:
        assert x['id'] in allids and x['id']!=k,(k,x); n+=1
json.dump(res,open(out,'w'),indent=1)
print(len(res),n,sum(v.get('cost')==2 for v in res.values()),sum(x['confidence']=='low' for v in res.values() for x in v['needs']))
