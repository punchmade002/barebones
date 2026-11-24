import json,re,sys
def build(pack,out,spec,mode_cost=True):
    pre='geo-option-atmosphere-ocean-'
    txt=open(pack).read()
    tgt=txt.split('CANDIDATES')[0]
    tids=re.findall(r'^\[([^\]]+)\]',tgt,re.M)
    allids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
    res={}
    for sid,cost,needs in spec:
        k=pre+'s4.'+sid
        d={'cost':cost} if mode_cost else {}
        d['needs']=[{'id':(pre+n[0]) if not n[0].startswith('geo-') else n[0],'strength':{'e':'essential','h':'helpful'}[n[1]],'why':n[2],'confidence':{'h':'high','l':'low'}[n[3]]} for n in needs]
        assert k not in res,k
        res[k]=d
    assert list(res)==tids,(set(tids)-set(res),set(res)-set(tids))
    for k,v in res.items():
        for n in v['needs']:
            assert n['id'] in allids and n['id']!=k,n
            assert len(n['why'].split())<=8
    json.dump(res,open(out,'w'),indent=0)
    links=sum(len(v['needs']) for v in res.values())
    print(len(res),links,sum(v.get('cost')==2 for v in res.values()),sum(n['confidence']=='low' for v in res.values() for n in v['needs']))
