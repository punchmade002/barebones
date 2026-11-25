import re,json,sys
B='/Users/gabrielwhelan/barebones/drafts/crunch/geography/'
P='geo-economic-activities-s1.'
PFX={'':P,'d:':'geo-economic-development-s1.','s2:':'geo-economic-activities-s2.','g:':'geo-economic-globalisation-s1.'}
def rid(r):
    for k in ('d:','s2:','g:'):
        if r.startswith(k): return PFX[k]+r[len(k):]
    return P+r
def need(s):
    r,st,c,w=s.split(',',3)
    return {'id':rid(r),'strength':'essential' if st=='e' else 'helpful','why':w,'confidence':'high' if c=='h' else 'low'}
def run(pack,spec,out,cost):
    txt=open(B+'packs/'+pack).read()
    tgt=[];allids=set()
    sec=None
    for l in txt.splitlines():
        if l.startswith('TARGET'): sec='t'
        elif l.startswith('CANDIDATES'): sec='c'
        m=re.match(r'\[(\S+)\]',l)
        if m:
            allids.add(m[1])
            if sec=='t': tgt.append(m[1])
    d={}
    for l in open(spec):
        l=l.rstrip('\n')
        if not l: continue
        p=l.split('|')
        if cost: i,c,n=p[0],int(p[1]),p[2]
        else: i,n=p[0],p[1]; c=None
        d[P+i]=(c,[need(x) for x in n.split(';') if x])
    res={}
    for t in tgt:
        c,n=d.get(t,(1 if cost else None,[]))
        if cost and t not in d: sys.exit('missing '+t)
        res[t]={'cost':c,'needs':n} if cost else {'needs':n}
    for k in d: assert k in res,k
    for t,v in res.items():
        for n in v['needs']: assert n['id'] in allids and n['id']!=t,(t,n['id'])
    json.dump(res,open(B+'point-links/'+out,'w'),indent=1)
    json.loads(open(B+'point-links/'+out).read())
    links=sum(len(v['needs']) for v in res.values())
    low=sum(n['confidence']=='low' for v in res.values() for n in v['needs'])
    c2=sum(v.get('cost')==2 for v in res.values())
    print(out,len(res),links,c2,low)
run('geo-economic-activities-s1.t1g1.txt','p1.txt','geo-economic-activities-s1.t1g1.json',True)
run('geo-economic-activities-s1.t1g2.txt','p2.txt','geo-economic-activities-s1.t1g2.json',False)
run('geo-economic-activities-s1.t1g3.txt','p3.txt','geo-economic-activities-s1.t1g3.json',False)
