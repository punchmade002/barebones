import json,re
D='/Users/gabrielwhelan/barebones/.claude/worktrees/crunch-chem-home/drafts/crunch/home-economics/'
def H(i,w,c='high'):return (i,'helpful',w,c)
def E(i,w,c='high'):return (i,'essential',w,c)
def build(name,rows):
    p=D+'packs/'+name+'.txt'
    ids=re.findall(r'^\[([^\]]+)\]',open(p).read(),re.M)
    out={}
    for r in rows:
        k=r[0]; out[k]={'cost':r[1],'needs':[{'id':l[0],'strength':l[1],'why':l[2],'confidence':l[3]} for l in r[2:]]}
    assert list(out)==ids,(set(ids)^set(out))
    for v in out.values():
        for n in v['needs']: assert n['id'] in ids
    json.dump(out,open(D+'point-links/'+name+'.json','w'),indent=1)
    print(name,len(out),sum(len(v['needs']) for v in out.values()),sum(v['cost']==2 for v in out.values()),sum(n['confidence']=='low' for v in out.values() for n in v['needs']))
a='hom-appliances-equipment-s1.'
build('hom-appliances-equipment-s1.t1g1',[
(a+'0.b',1),(a+'0.0',1),(a+'0.1',1),(a+'0.2',1),(a+'0.3',1),(a+'0.4',1),
(a+'0.5',1,H(a+'0.3','uses steam cleaning')),
(a+'1.b',1),(a+'1.0',1),(a+'1.1',1),(a+'1.2',1),(a+'1.3',1),(a+'1.4',1),(a+'1.5',1),
(a+'2.b',1),(a+'2.0',1),(a+'2.1',1),(a+'2.2',1),(a+'2.3',1),(a+'2.4',1),(a+'2.5',2),(a+'2.6',1),
(a+'3.b',1),(a+'3.0',1),(a+'3.1',1),(a+'3.2',1),(a+'3.3',1),(a+'3.4',1),(a+'3.5',1),(a+'3.6',1),
(a+'4.b',1),(a+'4.0',1),(a+'4.1',1),(a+'4.2',1),(a+'4.3',1),(a+'4.4',1),(a+'4.5',1),
(a+'5.b',1),(a+'5.0',1,H(a+'1.0','timers example used')),(a+'5.1',2),(a+'5.2',2),(a+'5.3',1)])
e='hom-energy-nutrition-s1.'
build('hom-energy-nutrition-s1.t1g1',[
(e+'0.b',1),(e+'0.0',2),(e+'0.1',1),(e+'0.2',1),(e+'0.3',2),
(e+'0.4',2,H(e+'1.0','basal metabolism defined as BMR')),
(e+'1.b',1),(e+'1.0',1),(e+'1.1',2),(e+'1.2',1),(e+'1.3',2),(e+'1.4',1,H(e+'4.0','compared with activity energy')),
(e+'2.b',1,H(e+'1.0','uses BMR')),
(e+'2.0',1,E(e+'1.0','factor affecting BMR')),(e+'2.1',1,E(e+'1.0','factor affecting BMR')),
(e+'2.2',1,E(e+'1.0','factor affecting BMR')),(e+'2.3',1,E(e+'1.0','factor affecting BMR')),
(e+'2.4',2,E(e+'1.0','factor affecting BMR')),(e+'2.5',1,E(e+'1.0','factor affecting BMR')),
(e+'2.6',1,E(e+'1.0','factor affecting BMR')),(e+'2.7',1,H(e+'5.0','activity is separate total component')),
(e+'3.b',1),(e+'3.0',1),(e+'3.1',1),(e+'3.2',1),(e+'3.3',1),(e+'3.4',1),
(e+'4.b',1),(e+'4.0',1),(e+'4.1',1),(e+'4.2',1),(e+'4.3',1),
(e+'5.b',1,H(e+'1.0','uses BMR')),
(e+'5.0',2,E(e+'1.0','BMR is a component'),H(e+'4.0','physical activity component')),
(e+'5.1',1),(e+'5.2',1),(e+'5.3',1),(e+'5.4',1),(e+'5.5',1),
(e+'5.6',2),(e+'5.7',2,H(e+'5.6','factors list to name'))])
l='hom-lipids-s1.'
build('hom-lipids-s1.t1g1',[
(l+'0.b',1),(l+'0.0',1),(l+'0.1',1),(l+'0.2',1),(l+'0.3',1),(l+'0.4',1,H(l+'0.1','saturated fats')),(l+'0.5',2),
(l+'1.b',1),(l+'1.0',1,E(l+'0.1','saturated no double bonds')),
(l+'1.1',1,E(l+'2.1','cis double bond shape'),H(l+'0.2','unsaturated double bonds')),
(l+'1.2',1,E(l+'1.1','kink per cis bond'),H(l+'0.2','monounsaturated one double bond')),
(l+'1.3',2,H(l+'0.3','polyunsaturated double bonds')),
(l+'1.4',2,E(l+'0.0','carboxyl and methyl ends')),
(l+'2.b',1),(l+'2.0',1,H(l+'0.2','double bonds in unsaturated acids')),(l+'2.1',1),(l+'2.2',1,H(l+'2.1','contrast with cis')),
(l+'2.3',1,H(l+'2.1','cis fatty acids')),(l+'2.4',2,H(l+'2.2','trans fatty acids')),
(l+'3.b',1),(l+'3.0',1,E(l+'0.3','polyunsaturated acids')),(l+'3.1',1,H(l+'1.3','omega-6 and omega-3')),
(l+'3.2',1,H(l+'3.1','linoleic acid')),(l+'3.3',2),(l+'3.4',1),(l+'3.5',2),
(l+'4.b',1,H(l+'1.3','omega-3 definition')),(l+'4.0',2,H(l+'5.2','HDL cholesterol')),(l+'4.1',1),(l+'4.2',1),(l+'4.3',1),(l+'4.4',1),
(l+'5.b',1),(l+'5.0',1),(l+'5.1',2,E(l+'5.0','LDL is a lipoprotein')),
(l+'5.2',1,E(l+'5.0','HDL is a lipoprotein')),
(l+'5.3',1,E(l+'0.1','saturated fatty acids'),H(l+'5.1','raises LDL')),
(l+'5.4',1,E(l+'2.1','cis unsaturated acids'),H(l+'5.2','raises HDL')),
(l+'5.5',2,E(l+'2.2','trans fatty acids'),H(l+'5.1','LDL and HDL effects')),
(l+'5.6',1,H(l+'5.3','replaces saturated fats')),
(l+'5.7',1,E(l+'3.0','essential fatty acids'),H(l+'4.0','omega-3 benefits'))])
