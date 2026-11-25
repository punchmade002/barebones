import json,re,sys
D='/Users/gabrielwhelan/barebones/drafts/crunch/history'
def run(pack,spec,out,pre,mode):
    txt=open(pack).read()
    tgt=[];allids=set();sec=None
    for l in txt.splitlines():
        if l.startswith('TARGET'):sec='t'
        elif l.startswith('CANDIDATES'):sec='c'
        m=re.match(r'\[([^\]]+)\]',l)
        if m:
            allids.add(m.group(1))
            if sec=='t':tgt.append(m.group(1))
    res={}
    for l in open(spec).read().splitlines():
        p=l.split('|');i=pre+p[0]
        assert i in tgt and i not in res,i
        needs=[]
        for n in [x for x in p[2].split(';') if x]:
            a,s,w,c=n.split(',')
            if not a.startswith('hist-'):a='hist-eur4-'+a if pre.startswith('hist-eur4') else a
            assert a in allids and a!=i,(i,a)
            needs.append({"id":a,"strength":"essential" if s=='E' else "helpful","why":w,"confidence":"high" if c=='h' else "low"})
        res[i]={"cost":int(p[1]),"needs":needs}
    assert list(res)==tgt,set(tgt)-set(res)
    json.dump(res,open(out,'w'),indent=1)
    v=list(res.values())
    print(len(res),sum(len(x['needs']) for x in v),sum(x['cost']==2 for x in v),sum(n['confidence']=='low' for x in v for n in x['needs']))
if __name__=='__main__':
    run(*sys.argv[1:5],None)
