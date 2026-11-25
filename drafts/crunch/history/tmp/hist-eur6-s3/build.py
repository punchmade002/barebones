import json,re,sys
P='/Users/gabrielwhelan/barebones/.claude/worktrees/history-crunch/drafts/crunch/history/'
def build(spec,pre,pack,out):
    ids=[l.split(']')[0][1:] for l in open(P+'packs/'+pack) if l.startswith('[')]
    d={}
    for line in open(spec):
        line=line.rstrip('\n')
        if not line: continue
        i,c,n=line.split('|')
        full=pre+i
        needs=[]
        if n:
            for x in n.split(';'):
                t,s,w,cf=x.split(':')
                t=t if t.startswith('hist-') else pre+t
                needs.append({"id":t,"strength":s,"why":w,"confidence":cf})
        d[full]={"cost":int(c),"needs":needs}
    tg=[i for i in ids if i.startswith(pre)]
    assert list(d)==tg,(set(tg)^set(d))
    for v in d.values():
        for n in v['needs']: assert n['id'] in ids and n['id']!=full
        assert all(len(n['why'].split())<=8 for n in v['needs'])
    for k,v in d.items():
        assert all(n['id']!=k for n in v['needs'])
    json.dump(d,open(P+'point-links/'+out,'w'),indent=0)
    print(len(d),sum(len(v['needs']) for v in d.values()),sum(v['cost']==2 for v in d.values()),sum(n['confidence']=='low' for v in d.values() for n in v['needs']))
T='/Users/gabrielwhelan/barebones/.claude/worktrees/history-crunch/drafts/crunch/history/tmp/hist-eur6-s3/'
build(T+'spec1.txt','hist-eur6-s3.','hist-eur6-s3.t1g1.txt','hist-eur6-s3.t1g1.json')
build(T+'spec2.txt','hist-ire3-s1.','hist-ire3-s1.t1g1.txt','hist-ire3-s1.t1g1.json')
