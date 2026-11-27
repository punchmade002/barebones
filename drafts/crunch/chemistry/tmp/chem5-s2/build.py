import json,re,sys
B='/Users/gabrielwhelan/barebones/.claude/worktrees/crunch-chem-home/drafts/crunch/chemistry'
def L(i,s,w,c='high'): return {"id":i,"strength":"essential" if s=='E' else "helpful","why":w,"confidence":c}
def check(pack,out,data):
    txt=open(pack).read().split('\n')
    tgt=[];allids=set();cur=None
    for l in txt:
        if l.startswith('TARGET'):cur='T'
        elif l.startswith('CANDIDATES'):cur='C'
        m=re.match(r'\[([^\]]+)\]',l)
        if m:
            allids.add(m.group(1))
            if cur=='T':tgt.append(m.group(1))
    assert list(data)==tgt,(set(tgt)-set(data),set(data)-set(tgt))
    n=lo=c2=0
    for k,v in data.items():
        for x in v['needs']:
            assert x['id'] in allids and x['id']!=k,(k,x);n+=1;lo+=x['confidence']=='low'
        c2+=v.get('cost')==2
    json.dump(data,open(out,'w'),ensure_ascii=False,indent=1)
    print(len(tgt),n,c2,lo)
def D(*rows):
    d={}
    for r in rows:
        k,c,*ls=r
        d[k]={"cost":c,"needs":list(ls)}
    return d
P='chem5-s2'
def run(name,rows,nocost=False):
    d=D(*rows)
    if nocost:
        for v in d.values():del v['cost']
    check(f'{B}/packs/{name}.txt',f'{B}/point-links/{name}.json',d)
g1=[
(P+'.0.b',1),(P+'.0.0',1),(P+'.0.1',1),(P+'.0.2',1),(P+'.0.3',1),(P+'.0.4',1),(P+'.0.5',1),(P+'.0.6',1),
(P+'.1.b',1),
(P+'.1.0',2,L('chem3-s1.11.b','H','flame colour of each metal')),
(P+'.2.b',1),(P+'.2.0',1),
(P+'.2.1',1,L('chem10-s2.11.1','H','writing an ionic precipitation equation')),
(P+'.2.2',1),
(P+'.2.3',1,L(P+'.2.1','H','chloride gives silver chloride precipitate')),
(P+'.2.4',1,L('chem11-s1.8.b','H','acid reacts with carbonate')),
(P+'.3.b',1),
(P+'.3.0',1,L(P+'.0.5','H','what a precipitate is')),
(P+'.3.1',1,L('chem5-s1.8.0','H','sulfate ion formula')),
(P+'.3.2',1,L('chem5-s1.8.0','H','sulfite ion formula')),
(P+'.3.3',1,L(P+'.3.0','E','both ions give white precipitate')),
(P+'.3.4',1,L(P+'.3.2','E','barium sulfite precipitate')),
(P+'.3.5',1),(P+'.3.6',1),
(P+'.4.b',1),
(P+'.4.0',1,L('chem11-s1.8.b','H','acid plus carbonate gives CO2'),L(P+'.0.6','H','effervescence')),
(P+'.4.1',1,L('chem11-s1.8.0','H','carbonate plus acid equation')),
(P+'.4.2',1,L('chem11-s1.8.2','H','hydrogencarbonate plus acid equation')),
(P+'.4.3',1,L('chem11-s1.8.3','E','limewater test for CO2')),
(P+'.4.4',1,L(P+'.0.5','H','what a precipitate is')),
(P+'.4.5',1,L(P+'.4.4','E','carbonate precipitate in the cold')),
(P+'.4.6',1,L(P+'.4.5','E','hydrogencarbonate gives no cold precipitate')),
(P+'.5.b',1),(P+'.5.0',1),(P+'.5.1',1),
(P+'.5.2',1,L(P+'.5.1','E','layering of acid under solution')),
(P+'.5.3',2,L('chem10-s2.11.4','H','charge balance in ionic equation','low')),
(P+'.5.4',1,L(P+'.5.3','E','nitrogen monoxide is produced')),
(P+'.5.5',1),
(P+'.6.b',1),(P+'.6.0',1),
(P+'.6.1',1,L(P+'.6.0','E','ammonium molybdate test reagents')),
(P+'.6.2',2,L('chem5-s1.8.0','H','phosphate and ammonium ion formulae')),
(P+'.6.3',1),
(P+'.7.b',1),(P+'.7.0',1),(P+'.7.1',1),
(P+'.7.2',1,L(P+'.7.1','E','nitrates and phosphates enter water')),
(P+'.7.3',1),
(P+'.7.4',1,L(P+'.7.3','E','hard water from calcium and magnesium')),
(P+'.7.5',1,L(P+'.7.3','E','hard water from calcium and magnesium')),
(P+'.7.6',1),
(P+'.8.b',1),(P+'.8.0',1),
(P+'.8.1',1,L(P+'.1.0','E','flame colours identify cation')),
(P+'.8.2',1,L(P+'.4.0','E','acid test for carbonates')),
(P+'.8.3',2,L(P+'.2.b','H','chloride test'),L(P+'.3.b','H','sulfate and sulfite test'),L(P+'.5.b','H','nitrate test'),L(P+'.6.b','H','phosphate test')),
(P+'.8.4',1,L(P+'.0.4','E','blank as a control')),
(P+'.8.5',1,L('chem3-s1.11.2','E','potassium flame is lilac'),L(P+'.2.2','E','silver chloride dissolves in ammonia')),
(P+'.8.6',1,L(P+'.5.1','E','acid layered under solution')),
]
run('chem5-s2.t1g1',g1)
g2=[(r[0],) for r in g1]
g2=[(k,0) for k, *_ in g1]
x={k:[] for k,*_ in g1}
x[P+'.5.3']=[L('chem14-s1.1.0','H','reduction as electron gain')]
x[P+'.5.4']=[]
x[P+'.6.3']=[L('chem14-s1.3.0','H','oxidising agent meaning','low')]
rows=[(k,0,*x[k]) for k in x]
run('chem5-s2.t1g2',rows,nocost=True)
