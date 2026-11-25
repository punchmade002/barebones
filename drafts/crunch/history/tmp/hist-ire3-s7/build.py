import json,re,sys
H='/Users/gabrielwhelan/barebones/drafts/crunch/history/'
def run(pack,out,data):
    txt=open(H+'packs/'+pack).read()
    lines=txt.split('\n')
    tg=[];allids=set()
    mode=None
    for l in lines:
        if l.startswith('TARGET'):mode='t'
        elif l.startswith('CANDIDATES'):mode='c'
        m=re.match(r'\[([^\]]+)\]',l)
        if m:
            allids.add(m.group(1))
            if mode=='t':tg.append(m.group(1))
    res={}
    for k,cost,needs in data:
        assert k not in res,k
        res[k]={'cost':cost,'needs':[{'id':i,'strength':s,'why':w,'confidence':c} for i,s,w,c in needs]}
    assert list(res)==tg,(set(tg)-set(res),set(res)-set(tg))
    for k,v in res.items():
        for n in v['needs']:assert n['id'] in allids and n['id']!=k,(k,n)
    json.dump(res,open(H+'point-links/'+out,'w'),indent=1)
    print(len(res),sum(len(v['needs']) for v in res.values()),sum(v['cost']==2 for v in res.values()),sum(n['confidence']=='low' for v in res.values() for n in v['needs']))
P='hist-ire3-s7.'
def d(rows):
    o=[]
    for k,c,*n in rows:
        o.append((P+k,c,[(i if i.startswith('hist') else P+i,s,w,cf) for i,s,w,cf in (n[0] if n else [])]))
    return o
H_='high';L='low';E='essential';HP='helpful'
rows=[
('0.b',1),('0.0',1),
('0.1',2,[('hist-ire3-s3.6.2',HP,'partition removed industrial north-east',H_)]),
('0.2',1,[('hist-ire3-s3.6.0',HP,'border customs controls interrupted trade',H_)]),
('0.3',1),('0.4',1),('0.5',1),
('1.b',1),
('1.0',1,[('0.0',HP,'exports of beef, butter to Britain',H_)]),
('1.1',2,[('1.0',HP,'quality exports policy',L)]),
('1.2',1),('1.3',1),('1.4',1),
('1.5',1,[('hist-ire3-s5.2.7',E,'the Shannon Scheme',H_)]),
('1.6',1,[('1.0',HP,'farm export policy',L)]),
('1.7',1,[('1.1',HP,'Agricultural Credit Corporation founded',H_)]),
('2.b',1),('2.0',1),
('2.1',1,[('2.0',E,'refers to McElligott',H_)]),
('2.2',1,[('1.2',HP,'Blythe as Finance Minister',H_)]),
('2.3',1),
('2.4',1,[('4.b',HP,'Lemass protection policy',H_)]),
('2.5',1,[('2.4',HP,'Finance opposing new schemes',L)]),
('2.6',2,[('2.3',HP,'Finance orthodoxy and caution',H_)]),
('3.b',1),('3.0',1),('3.1',1),
('3.2',1,[('0.3',E,'currency tied to sterling',H_)]),
('3.3',1,[('0.0',HP,'dependence on British market',H_)]),
('3.4',1,[('1.3',HP,'government spending cuts, balanced budgets',L)]),
('3.5',1,[('hist-ire3-s5.4.4',HP,'Fianna Fail promised protection',H_)]),
('3.6',1,[('hist-ire3-s6.2.0',E,'land annuities',H_)]),
('4.b',1,[('3.5',HP,'Fianna Fail 1932 victory',H_)]),
('4.0',1,[('4.b',HP,'protectionist policy',H_)]),
('4.1',1),('4.2',1),('4.3',1),
('4.4',1,[('hist-ire3-s5.2.7',HP,'ESB and Shannon Scheme',L)]),
('4.5',1),
('4.6',2),
('4.7',2,[('4.0',HP,'tariffs and protection',H_)]),
('4.8',1,[('hist-ire3-s6.5.5',HP,'wartime neutrality, the Emergency',L)]),
('5.b',1,[('hist-ire3-s6.2.b',E,'Economic War over annuities',H_)]),
('5.0',1,[('hist-ire3-s6.2.1',HP,'British special duties from 1932',H_)]),
('5.1',1,[('5.0',E,'British duties on cattle',H_)]),
('5.2',1,[('5.0',HP,'lost income from British duties',H_)]),
('5.3',1,[('hist-ire3-s6.2.3',HP,'Coal-Cattle Pact',H_)]),
('5.4',1,[('5.1',HP,'cattle farmers hit by trade war',H_)]),
('5.5',1,[('hist-ire3-s6.5.b',E,'1938 agreements',H_)]),
('5.6',1,[('5.0',HP,'fall in prices from duties',L)]),
('6.b',1),
('6.0',2),('6.1',1),('6.2',1),('6.3',1),
('6.4',1,[('3.b',HP,'Depression closing job markets',H_)]),
('6.5',1),
('6.6',1,[('6.4',HP,'emigration and Depression',H_)]),
('7.b',1),
('7.0',1,[('1.b',HP,'Cumann na nGaedheal economic policy',H_)]),
('7.1',1,[('3.b',HP,'Depression exposed dependence',H_)]),
('7.2',1,[('4.b',HP,'Fianna Fail industrial protection',H_),('6.b',HP,'Fianna Fail social housing and welfare',L)]),
('7.3',1,[('5.b',E,'the Economic War',H_)]),
('7.4',2),('7.5',1),
('7.6',2,[('2.3',HP,'Finance Department caution',H_)]),
]
run('hist-ire3-s7.t1g1.txt','hist-ire3-s7.t1g1.json',d(rows))
