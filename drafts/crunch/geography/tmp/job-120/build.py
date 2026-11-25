import json,re,sys
P='/Users/gabrielwhelan/barebones/drafts/crunch/geography/'
PRE={'':'geo-region-ireland-s2.','c4:':'geo-region-concept-s4.','e2:':'geo-economic-activities-s2.','c3:':'geo-region-concept-s3.','m6:':'geo-population-migration-s6.','c1:':'geo-region-concept-s1.'}
def full(s):
    for k in ('c4:','e2:','c3:','m6:','c1:'):
        if s.startswith(k): return PRE[k]+s[len(k):]
    return PRE['']+s
def L(s,st,why,conf='high'):
    return {"id":full(s),"strength":"essential" if st=='E' else "helpful","why":why,"confidence":conf}
H='H'
def pack(name,entries,cost):
    txt=open(P+'packs/'+name+'.txt').read()
    tgt=[]
    for line in txt.split('\n\n')[0].split('\n'):
        m=re.match(r'\[(\S+?)\]',line)
        if m: tgt.append(m.group(1))
    allids=set(re.findall(r'^\[(\S+?)\]',txt,re.M))
    out={}
    for e in entries:
        k=full(e[0]); 
        assert k not in out,k
        if cost: out[k]={"cost":e[1],"needs":e[2]}
        else: out[k]={"needs":e[1]}
    assert list(out)==tgt,(set(tgt)^set(out))
    nl=lo=c2=0
    for k,v in out.items():
        for n in v['needs']:
            assert n['id'] in allids and n['id']!=k,(k,n['id'])
            if not cost: assert n['id'] not in tgt
            nl+=1; lo+=n['confidence']=='low'
        c2+= cost and v['cost']==2
    json.dump(out,open(P+'point-links/'+name+'.json','w'),indent=1,ensure_ascii=False)
    print(name,len(out),nl,c2 if cost else '-',lo)
