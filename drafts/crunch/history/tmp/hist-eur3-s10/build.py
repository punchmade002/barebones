import json,re,sys
D='/Users/gabrielwhelan/barebones/.claude/worktrees/history-crunch/drafts/crunch/history/'
def run(spec,pack,out,cost):
    ptxt=open(D+'packs/'+pack).read()
    allids=set(re.findall(r'^\[(hist-[^\]]+)\]',ptxt,re.M))
    tgt=[];sec=None
    for l in ptxt.split('\n'):
        if l.startswith('TARGET'): sec='t'
        elif l.startswith('CANDIDATES'): sec='c'
        m=re.match(r'\[(hist-[^\]]+)\]',l)
        if m and sec=='t': tgt.append(m.group(1))
    res={};n=0;low=0;c2=0
    for l in open(spec).read().strip().split('\n'):
        p=l.split('|'); i='hist-eur3-s10.'+p[0]
        assert i not in res
        if cost: c=int(p[1]); links=p[2]
        else: links=p[1]
        needs=[]
        for x in filter(None,links.split(';')):
            a,s,w,cf=x.split(':'); a='hist-eur3-'+a
            assert a in allids and a!=i,a
            needs.append({"id":a,"strength":"essential" if s=='E' else "helpful","why":w,"confidence":"high" if cf=='H' else "low"})
        e={"cost":c,"needs":needs} if cost else {"needs":needs}
        if cost: c2+=c==2
        n+=len(needs);low+=sum(x['confidence']=='low' for x in needs)
        res[i]=e
    assert list(res)==tgt,(set(tgt)^set(res))
    json.dump(res,open(D+'point-links/'+out,'w'),indent=0)
    json.loads(open(D+'point-links/'+out).read())
    print(out,len(res),n,c2,low)
run('spec1.txt','hist-eur3-s10.t1g1.txt','hist-eur3-s10.t1g1.json',True)
run('spec2.txt','hist-eur3-s10.t1g2.txt','hist-eur3-s10.t1g2.json',False)
