import json,re,sys
pack,out=sys.argv[1:3]
txt=open(pack).read()
ids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
tg=[]
sec=None
for l in txt.split('\n'):
    if l.startswith('TARGET'): sec='t'
    elif l.startswith('CANDIDATES'): sec='c'
    m=re.match(r'\[([^\]]+)\]',l)
    if m and sec=='t': tg.append(m.group(1))
d=json.load(open(out))
assert list(d)==tg,(set(tg)^set(d))
n=0;c2=0;low=0
for k,v in d.items():
    assert v['cost'] in(1,2); c2+=v['cost']==2
    for x in v['needs']:
        assert x['id'] in ids and x['id']!=k,x; n+=1; low+=x['confidence']=='low'
        assert x['strength'] in('essential','helpful') and len(x['why'].split())<=8
print(len(tg),n,c2,low)
