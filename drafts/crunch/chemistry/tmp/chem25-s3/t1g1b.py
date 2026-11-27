import json,re
H,E='helpful','essential'
def n(i,s,w,c='high'): return {"id":i,"strength":s,"why":w,"confidence":c}
P='chem26-s2.'
d={}
def a(k,c,*l): d[k]=(c,list(l))
a('0.b',1); a('0.0',1)
a('0.1',1,n('chem26-s1.0.1',H,'mole ratio from balanced equation','low'))
a('0.2',1,n(P+'0.1',H,'contrast with theoretical yield'))
a('0.3',1,n(P+'0.1',E,'theoretical yield in the formula'),n(P+'0.2',E,'actual yield in the formula'))
a('0.4',1,n(P+'0.3',H,'comparing yields in percentage formula'),n('chem26-s1.1.2',H,'gas volume at STP','low'))
a('1.b',1)
a('1.0',1,n('chem26-s1.0.1',E,'coefficients give mole ratio'))
a('1.1',1,n('chem26-s1.1.1',E,'moles = mass over molar mass'))
a('1.2',1,n('chem26-s1.1.4',E,'using mole ratio to find product moles'))
a('1.3',1,n(P+'0.3',E,'percentage yield formula'))
a('2.b',1)
a('2.0',1)
a('2.1',2,n('chem26-s1.1.1',E,'moles from mass and molar mass'),n('chem26-s1.1.4',E,'mole ratio to find product moles'))
a('2.2',1,n('chem26-s1.1.5',E,'converting moles to mass'))
a('2.3',1,n(P+'0.3',E,'percentage yield formula'))
a('2.4',1,n('chem26-s1.1.2',E,'one mole of gas is 22.4 L at STP'))
a('2.5',1,n(P+'2.4',E,'theoretical gas volume'),n(P+'0.3',E,'percentage yield formula'))
a('3.b',1,n(P+'0.1',H,'limiting reactant decides theoretical yield'))
a('3.0',1)
a('3.1',1,n('chem26-s1.1.1',E,'moles from mass and molar mass'))
a('3.2',1,n('chem26-s1.1.5',E,'converting moles to mass'))
a('3.3',1,n(P+'0.3',E,'percentage yield formula'))
a('3.4',1)
a('4.b',1)
a('4.0',1)
a('4.1',1,n('chem26-s1.1.1',E,'moles from mass and molar mass'))
a('4.2',1,n('chem26-s1.1.5',E,'converting moles to mass'))
a('4.3',1,n(P+'0.3',E,'percentage yield formula'))
a('5.b',1,n(P+'0.3',H,'percentage yield formula'))
a('5.0',1)
a('5.1',2,n(P+'0.3',E,'rearranged percentage yield formula'))
a('5.2',1,n('chem26-s1.1.4',E,'mole ratio between reactant and product'))
a('5.3',1,n('chem26-s1.1.5',E,'converting moles to mass'))
a('5.4',1,n(P+'0.3',E,'percentage yield formula'))
a('6.b',1); a('6.0',1); a('6.1',1); a('6.2',1); a('6.3',1)
a('6.4',1,n(P+'0.3',H,'yield above 100% from the formula','low'))
a('7.b',1); a('7.0',1); a('7.1',1)
a('7.2',2,n(P+'0.3',E,'yield as a fraction of theoretical'))
out={P+k:{"cost":c,"needs":nd} for k,(c,nd) in d.items()}
base='/Users/gabrielwhelan/barebones/.claude/worktrees/crunch-chem-home/drafts/crunch/chemistry/'
json.dump(out,open(base+'point-links/chem26-s2.t1g1.json','w'),ensure_ascii=False)
txt=open(base+'packs/chem26-s2.t1g1.txt').read()
allids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M)); tg=[];sec=0
for l in txt.split('\n'):
    if l.startswith('TARGET'): sec=1
    elif l.startswith('CANDIDATES'): sec=0
    m=re.match(r'\[([^\]]+)\]',l)
    if m and sec: tg.append(m.group(1))
assert sorted(tg)==sorted(out) and len(tg)==len(out),set(tg)^set(out)
for k,v in out.items():
    for x in v['needs']: assert x['id'] in allids and x['id']!=k
print(len(out),sum(len(v['needs']) for v in out.values()),sum(v['cost']==2 for v in out.values()),sum(x['confidence']=='low' for v in out.values() for x in v['needs']))
