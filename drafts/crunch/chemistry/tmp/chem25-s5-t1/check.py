import json,re,sys
pack,out=sys.argv[1],sys.argv[2]
txt=open(pack).read().split('\n')
mode=txt[0]
tg=[];allids=set();cur=None
for l in txt:
    if l.startswith('TARGET'):cur='T'
    elif l.startswith('CANDIDATES'):cur='C'
    m=re.match(r'\[([^\]]+)\]',l)
    if m:
        allids.add(m.group(1))
        if cur=='T':tg.append(m.group(1))
d=json.load(open(out))
assert list(d)==tg,(set(tg)-set(d),set(d)-set(tg))
n=c2=low=0
for k,v in d.items():
    for x in v['needs']:
        assert x['id'] in allids and x['id']!=k,(k,x)
        assert x['strength'] in('essential','helpful') and x['confidence'] in('high','low')
        n+=1;low+=x['confidence']=='low'
    if 'cost' in v: assert v['cost'] in(1,2);c2+=v['cost']==2
print(len(tg),n,c2,low,mode)
