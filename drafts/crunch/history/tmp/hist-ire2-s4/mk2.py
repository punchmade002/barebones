import json,re,sys
H='/Users/gabrielwhelan/barebones/drafts/crunch/history/'
def run(pack,out,pre,ext,data):
    ids=[];cands=set()
    mode=None
    for l in open(H+'packs/'+pack):
        if l.startswith('TARGET'):mode='t'
        elif l.startswith('CANDIDATES'):mode='c'
        m=re.match(r'\[(\S+?)\]',l)
        if m:
            (ids if mode=='t' else []).append(m.group(1)); cands.add(m.group(1))
    res={}
    keys=[k for k,_,_ in data]
    assert len(set(keys))==len(keys)
    full=[pre+'.'+k for k in keys]
    assert full==ids,(set(ids)-set(full),set(full)-set(ids))
    nl=n2=nlow=0
    for k,c,links in data:
        needs=[]
        for t,s,w,cf in links:
            i=t if t.startswith('hist-') else (ext+t[1:] if t[0]=='s' else pre+'.'+t)
            if t[0]=='s' and not t.startswith('hist-'): i='hist-'+ext+t[1:] if False else None
            needs.append((t,s,w,cf))
        res[pre+'.'+k]=(c,needs)
    return ids,cands,res
