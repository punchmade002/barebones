import json,re
D='/Users/gabrielwhelan/barebones/.claude/worktrees/crunch-chem-home/drafts/crunch/chemistry/'
P={'a':'chem23-s4.','b':'chem14-s1.','c':'chem11-s1.'}
def L(x,s,why,c='h'):
    return {"id":P[x[0]]+x[1:],"strength":{'e':'essential','h':'helpful'}[s],"why":why,"confidence":{'h':'high','l':'low'}[c]}
R={}
def A(i,*links): R['chem25-s1.'+i]={"needs":list(links)}
A('0.b');A('0.0');A('0.1');A('0.2');A('0.3');A('0.4');A('0.5');A('0.6');A('0.7')
A('1.b');A('1.0');A('1.1');A('1.2');A('1.3');A('1.4');A('1.5');A('1.6');A('1.7')
A('2.b');A('2.0');A('2.1');A('2.2');A('2.3');A('2.4');A('2.5');A('2.6')
A('3.b')
A('3.0',L('b0.0','h','early oxygen/hydrogen oxidation definition'))
A('3.1',L('b0.1','h','early reduction definition'))
A('3.2',L('b1.0','e','oxidation as loss of electrons'),L('b11.4','h','oxidation number increase'))
A('3.3',L('b3.0','h','oxidising agent'))
A('3.4',L('b0.1','h','reduction as gain of hydrogen'))
A('3.5',L('b9.0','h','combustion as oxidation'))
A('4.b');A('4.0')
A('4.1',L('c6.0','h','acid plus base gives salt and water'))
A('4.2',L('c8.0','h','acid plus carbonate gives CO2'))
A('4.3',L('c1.3','h','hydroxide as alkali base','l'))
A('4.4',L('c2.0','h','indicator colour showing neutral','l'))
A('4.5',L('c7.0','h','reactive metal releases hydrogen from acid','l'))
A('5.b');A('5.0')
A('5.1',L('b11.4','e','oxidation number change'))
A('5.2');A('5.3')
A('6.b',L('a10.1','h','double bond is sigma plus pi'))
A('6.0',L('a10.1','h','double bond is sigma plus pi'))
A('6.1',L('a10.1','h','pi bond of double bond'))
A('6.2',L('a10.1','h','C=O is sigma plus pi','l'))
A('6.3')
A('6.4',L('b1.0','e','oxidation as loss of electrons'),L('c7.0','h','acid plus metal gives hydrogen'))
A('6.5',L('b2.0','h','redox means oxidation and reduction together','l'))
for i in ['7.b','7.0','7.1','7.2','7.3','7.4','7.5','8.b','8.0']: A(i)
A('8.1',L('a10.0','h','pi bond from sideways overlap'))
for i in ['8.2','8.3','8.4','8.5','8.6','9.b','9.0','9.1','9.2','9.3','9.4','9.5','10.b','10.0','10.1','10.2','10.3','10.4','10.5','10.6','11.b']: A(i)
A('11.0',L('a11.0','h','benzene ring structure'))
for i in ['11.1','11.2','11.3','11.4','11.5','12.b','12.0','12.1','12.2','12.3','12.4','12.5','12.6','13.b','13.0','13.1','13.2']: A(i)
A('13.3',L('a10.1','h','pi bonds in double bonds','l'))
for i in ['13.4','13.5','14.b','14.0','14.1','14.2','15.b','15.0','15.1','15.2','15.3','15.4']: A(i)
txt=open(D+'packs/chem25-s1.t1g2.txt').read().split('\n')
mode=None;tg=[];allids=set()
for ln in txt:
    if ln.startswith('TARGET'): mode='t'
    elif ln.startswith('CANDIDATES'): mode='c'
    m=re.match(r'\[([^\]]+)\]',ln)
    if m:
        allids.add(m.group(1))
        if mode=='t': tg.append(m.group(1))
assert list(R)==tg,(set(tg)-set(R),set(R)-set(tg))
n=low=0
for k,v in R.items():
    for x in v['needs']:
        assert x['id'] in allids and x['id']!=k,(k,x)
        n+=1;low+=x['confidence']=='low'
json.dump(R,open(D+'point-links/chem25-s1.t1g2.json','w'),indent=1)
print(len(R),n,low)
