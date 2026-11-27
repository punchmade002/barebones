import json,re
P='/Users/gabrielwhelan/barebones/.claude/worktrees/crunch-chem-home/drafts/crunch/home-economics/'
E,H='essential','helpful'
def L(i,s,w,c='high'): return {"id":i,"strength":s,"why":w,"confidence":c}
D='hom-social-change-s4.'
def dl(k,s,w,c='high'): return L(D+k,s,w,c)
d={'0.b':(1,[])}
for k in ['0.0','0.1','0.4','0.5']: d[k]=(1,[])
d['0.2']=(1,[dl('0.1',H,'cohabitation and births outside marriage')])
d['0.3']=(1,[dl('0.1',E,'cohabitation being recognised')])
d['1.b']=(1,[]);d['1.0']=(1,[])
d['1.1']=(1,[dl('1.0',E,'divorce Act sets conditions')])
d['1.2']=(1,[]);d['1.3']=(1,[])
d['1.4']=(1,[])
d['1.5']=(1,[dl('1.4',E,'judicial separation'),dl('1.0',H,'divorce ends marriage')])
d['2.b']=(1,[])
for k in ['2.0','2.1','2.3','2.4','2.5']: d[k]=(1,[])
d['2.2']=(1,[dl('1.0',H,'divorce and separation make breakdown possible','low')])
d['3.b']=(1,[])
for k in ['3.0','3.1','3.2','3.3','3.5','3.7']: d[k]=(1,[])
d['3.4']=(2,[dl('7.1',H,'contraception and family planning')])
d['3.6']=(2,[])
d['4.b']=(1,[]);d['4.0']=(1,[]);d['4.1']=(1,[dl('3.0',H,'child-centred, children\'s views')])
d['4.2']=(1,[]);d['4.3']=(1,[]);d['4.4']=(1,[dl('3.0',H,'negotiated rules, child-centred parenting')]);d['4.5']=(1,[])
d['5.b']=(1,[]);d['5.0']=(1,[])
d['5.1']=(1,[dl('5.0',H,'traditional roles contrasted')])
d['5.2']=(1,[dl('5.1',H,'egalitarian shared roles')])
d['5.3']=(1,[dl('5.1',H,'egalitarian roles')])
d['5.4']=(1,[]);d['5.5']=(1,[])
d['5.6']=(2,[dl('2.0',H,'lone-parent, blended, cohabiting families')])
d['6.b']=(1,[])
d['6.0']=(1,[dl('5.1',H,'shared roles between partners')])
d['6.1']=(1,[dl('5.1',H,'both partners working')])
d['6.2']=(1,[])
d['6.3']=(1,[L('hom-family-caring-s1.5.1',H,'role overload')])
d['6.4']=(1,[]);d['6.5']=(1,[dl('5.0',H,'breadwinner role')])
for k in ['7.b','7.0','7.1','7.2','7.3','7.4','7.5','7.6']: d[k]=(1,[])
d['7.7']=(1,[L('hom-sociological-concepts-s5.2.b',H,'law both reflects and drives change','low')])
for k in ['8.b','8.0','8.1','8.2','8.3','8.4','9.b','9.0','9.1']: d[k]=(1,[])
out={D+k:{"cost":c,"needs":n} for k,(c,n) in d.items()}
t=open(P+'packs/hom-social-change-s4.t1g1.txt').read()
ids=set(re.findall(r'^\[([^\]]+)\]',t,re.M))
tgt=re.findall(r'^\[([^\]]+)\]',t.split('CANDIDATES')[0],re.M)
assert sorted(tgt)==sorted(out),set(tgt)^set(out)
for k,v in out.items():
  for n in v['needs']: assert n['id'] in ids and n['id']!=k,(k,n)
out={k:out[k] for k in tgt}
json.dump(out,open(P+'point-links/hom-social-change-s4.t1g1.json','w'),indent=1)
print(len(out),sum(len(v['needs']) for v in out.values()),sum(v['cost']==2 for v in out.values()),sum(n['confidence']=='low' for v in out.values() for n in v['needs']))
