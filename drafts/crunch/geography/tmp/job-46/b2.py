import json,re
D='/Users/gabrielwhelan/barebones/drafts/crunch/geography/'
P='geo-option-atmosphere-ocean-s6.'
pre={'T':P,'A':'geo-option-atmosphere-ocean-s5.'}
def links(s,mp):
    r=[]
    for x in filter(None,s.split(';')):
        st,i,w,c=x.split(':',3) if False else (x.split(':')[0],x.split(':')[1],x.split(':')[2],x.split(':')[3])
        r.append({'id':mp(i),'strength':{'h':'helpful','e':'essential'}[st],'why':w,'confidence':{'H':'high','L':'low'}[c]})
    return r
def m1(i): return pre[i[0]]+i[1:]
def m2(i): return 'geo-option-atmosphere-ocean-s'+i
def m3(i): return 'geo-economic-development-s'+i
def read(f):
    return [l.rstrip('\n') for l in open(D+'tmp/job-46/'+f) if l.strip()]
g1={}
for l in read('g1.txt'):
    k,c,ln=l.split('|'); g1[P+k]={'cost':int(c),'needs':links(ln,m1)}
def sparse(f,mp):
    d={}
    for l in read(f):
        k,ln=l.split('|'); d[P+k]=links(ln,mp)
    return d
sets=[(g1,None),(sparse('g2.txt',m2),m2),(sparse('g3.txt',m3),m3)]
for n,(g,_) in enumerate(sets,1):
    pk=open(D+f'packs/{P}t1g{n}.txt').read()
    tg=re.findall(r'^\[([^\]]+)\]',pk.split('CANDIDATES')[0],re.M)
    pids=set(re.findall(r'^\[([^\]]+)\]',pk,re.M))
    if n==1: assert set(g)==set(tg) and len(g)==len(tg),(set(tg)-set(g),set(g)-set(tg))
    else: assert set(g)<=set(tg)
    out={i:(g[i] if n==1 else {'needs':g.get(i,[])}) for i in tg}
    for i,v in out.items():
        for x in v['needs']: assert x['id'] in pids and x['id']!=i,(n,i,x)
    old=json.load(open(D+f'tmp/job-46/old/{P}t1g{n}.json'))
    ch=sum(1 for i in tg if ({x['id'] for x in out[i]['needs']},out[i].get('cost'))!=({x['id'] for x in old[i]['needs']},old[i].get('cost')))
    json.dump(out,open(D+f'point-links/{P}t1g{n}.json','w'),indent=1)
    ls=[x for v in out.values() for x in v['needs']]
    print(n,len(out),len(ls),sum(v.get('cost')==2 for v in out.values()),sum(x['confidence']=='low' for x in ls),'changed',ch)
