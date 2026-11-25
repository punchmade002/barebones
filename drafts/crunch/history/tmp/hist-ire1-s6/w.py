import json,re,sys
H='/Users/gabrielwhelan/barebones/.claude/worktrees/history-crunch/drafts/crunch/history/'
E,Hp='essential','helpful'
def run(pk,pre,rows):
    txt=open(H+'packs/'+pk+'.txt').read()
    allids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
    tsec=txt.split('\nCANDIDATES')[0]
    tids=re.findall(r'^\[([^\]]+)\]',tsec,re.M)
    out={}
    for r in rows:
        i,c,n=r[0],r[1],r[2:]
        i=pre+i
        assert i not in out
        out[i]={"cost":c,"needs":[{"id":(x[0] if x[0].startswith('hist-') else pre+x[0]),"strength":x[1],"why":x[2],"confidence":x[3]} for x in n]}
    assert list(out)==tids,(set(tids)-set(out),set(out)-set(tids))
    nl=0;lo=0
    for k,v in out.items():
        for x in v['needs']:
            assert x['id'] in allids and x['id']!=k,(k,x)
            assert len(x['why'].split())<=8
            nl+=1;lo+=x['confidence']=='low'
    json.dump(out,open(H+'point-links/'+pk+'.json','w'),indent=1)
    print(pk,len(out),nl,sum(v['cost']==2 for v in out.values()),lo)
