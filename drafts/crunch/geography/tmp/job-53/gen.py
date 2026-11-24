import json,re
P='geo-option-culture-identity-'
O='/Users/gabrielwhelan/barebones/drafts/crunch/geography/point-links/'
K='/Users/gabrielwhelan/barebones/drafts/crunch/geography/packs/'
def full(x): return P+x if x.startswith('s') and x[1].isdigit() and x[2]=='.' and x[1]!='5' or x.startswith('s4') or x.startswith('s3') or x.startswith('s2') else P+'s5.'+x
def fid(x):
    if re.match(r'^s[234]\.',x): return P+x if x[1]!='4' else 'geo-region-european-'+x
    return P+'s5.'+x
def parse(l):
    out=[]
    for p in filter(None,l.split(';')):
        i,s,w,c=p.split(':')
        out.append({"id":fid(i),"strength":"essential" if s=='E' else "helpful","why":w,"confidence":"high" if c=='h' else "low"})
    return out
p1={};ids=[]
for ln in open('p1.txt'):
    a,c,l=ln.rstrip('\n').split('|')
    ids.append(a);p1[fid(a)]={"cost":int(c),"needs":parse(l)}
def links(f):
    d={}
    for ln in open(f):
        a,l=ln.rstrip('\n').split('|');d[fid(a)]=parse(l)
    return d
def out(n,res):
    txt=open(K+'geo-option-culture-identity-s5.t1g%d.txt'%n).read()
    pack=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
    tg=re.findall(r'^\[([^\]]+)\]',txt.split('CANDIDATES')[0],re.M)
    assert list(res)==tg,(set(tg)^set(res))
    for k,v in res.items():
        for x in v['needs']:
            assert x['id'] in pack and x['id']!=k,x
    json.dump(res,open(O+'geo-option-culture-identity-s5.t1g%d.json'%n,'w'),indent=1,ensure_ascii=False)
    nl=sum(len(v['needs']) for v in res.values());lo=sum(x['confidence']=='low' for v in res.values() for x in v['needs'])
    print(n,len(res),nl,sum(v.get('cost')==2 for v in res.values()),lo)
out(1,p1)
for n,f in((2,'p2.txt'),(3,'p3.txt')):
    d=links(f)
    out(n,{k:{"needs":d.get(k,[])} for k in p1})
