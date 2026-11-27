import json,re,sys
D='/Users/gabrielwhelan/barebones/.claude/worktrees/crunch-chem-home/drafts/crunch/home-economics'
def L(i,s,w,c='high'): return {"id":i,"strength":{'e':'essential','h':'helpful'}[s],"why":w,"confidence":c}
def run(name,pre,items):
    out={}
    for k,(cost,links) in items.items():
        assert k not in out; out[pre+k]={"cost":cost,"needs":[ {**l,"id":l["id"] if l["id"].startswith("hom-") else pre+l["id"]} for l in links]}
    txt=open(f'{D}/packs/{name}.txt').read()
    tgt=[];sec=None
    for line in txt.split('\n'):
        if line.startswith('TARGET'): sec='T'
        elif line.startswith('CANDIDATES'): sec='C'
        m=re.match(r'\[([^\]]+)\]',line)
        if m and sec=='T': tgt.append(m.group(1))
    allids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
    assert list(out)==tgt,(set(tgt)^set(out))
    for k,v in out.items():
        for n in v['needs']: assert n['id'] in allids and n['id']!=k,(k,n)
        assert all(len(n['why'].split())<=8 for n in v['needs'])
    json.dump(out,open(f'{D}/point-links/{name}.json','w'),indent=1)
    nl=sum(len(v['needs']) for v in out.values()); c2=sum(v['cost']==2 for v in out.values())
    lo=sum(n['confidence']=='low' for v in out.values() for n in v['needs'])
    print(name,len(out),nl,c2,lo)

