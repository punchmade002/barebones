import json,re,sys
pack,out=sys.argv[1],sys.argv[2]
txt=open(pack).read()
tg=[];allids=set()
sec=None
for l in txt.split('\n'):
    if l.startswith('TARGET'): sec='T'
    elif l.startswith('CANDIDATES'): sec='C'
    m=re.match(r'\[([^\]]+)\]',l)
    if m:
        allids.add(m.group(1))
        if sec=='T': tg.append(m.group(1))
d=json.load(open(out))
assert list(d)==tg,(set(tg)-set(d),set(d)-set(tg))
n=c2=low=0
for k,v in d.items():
    for x in v['needs']:
        assert x['id'] in allids and x['id']!=k,(k,x)
        assert len(x['why'].split())<=8
        n+=1; low+=x['confidence']=='low'
    c2+=v.get('cost')==2
print(len(tg),n,c2,low)
