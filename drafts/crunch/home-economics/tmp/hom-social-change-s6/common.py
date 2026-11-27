import json,re
D='/Users/gabrielwhelan/barebones/.claude/worktrees/crunch-chem-home/drafts/crunch/home-economics/'
def run(name,pref,T):
    txt=open(D+'packs/'+name+'.txt').read()
    tg=[];ids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
    sec=txt.split('CANDIDATES')[0]
    tg=re.findall(r'^\[([^\]]+)\]',sec,re.M)
    out={}
    for t in tg:
        k=t[len(pref):]
        c,nd=T[k]
        out[t]={"cost":c,"needs":nd}
    assert set(T)==set(k[len(pref):] for k in tg),(set(T)^set(k[len(pref):] for k in tg))
    links=low=c2=0
    for t,v in out.items():
        for x in v['needs']:
            assert x['id'] in ids and x['id']!=t,x['id'];links+=1;low+=x['confidence']=='low'
        c2+=v['cost']==2
    json.dump(out,open(D+'point-links/'+name+'.json','w'),indent=1)
    print(name,len(out),links,c2,low)
