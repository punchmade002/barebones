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

P='hist-ire5-s10.'
def d(rows):
    o=[]
    for k,c,*n in rows:
        o.append((P+k,c,[(i if i.startswith('hist') else P+i,s,w,cf) for i,s,w,cf in (n[0] if n else [])]))
    return o
H_='high';L='low';E='essential';HP='helpful'
rows=[
('0.b',1),('0.0',1),
('0.1',1,[('0.0',HP,'the shutting of the gates',L)]),
('0.2',2,[('0.0',HP,'siege follows the closing of gates',H_)]),
('0.3',1,[('0.2',E,'the siege being relieved',H_)]),
('0.4',1,[('0.2',E,'the siege of Derry',H_)]),
('0.5',1),
('0.6',1,[('0.2',E,'the siege and its hunger',H_)]),
('0.7',1,[('0.2',HP,'defenders during the siege',H_)]),
('0.8',1,[('0.3',E,'Mountjoy breaking the boom',H_)]),
('1.b',1,[('0.b',HP,'the siege being commemorated',H_)]),
('1.0',1,[('0.b',HP,'the siege commemorated',H_)]),
('1.1',1,[('0.0',E,'apprentices who shut the gates',H_)]),
('1.2',1,[('0.0',HP,'thirteen apprentice boys',H_)]),
('1.3',1,[('1.0',E,'the Derry club',H_)]),
('1.4',1,[('1.0',HP,'the Apprentice Boys organisation',L)]),
('1.5',1,[('1.0',HP,'the commemorative tradition',L)]),
('1.6',1,[('1.0',E,'the Derry parent club',H_)]),
('2.b',1,[('1.b',HP,'the Apprentice Boys organisation',L)]),
('2.0',1,[('0.3',E,'relief of the siege',H_)]),
('2.1',1,[('2.0',HP,'the August commemoration',H_),('0.5',HP,'the city walls',L)]),
('2.2',2,[('0.0',E,'the Shutting of the Gates',H_),('0.1',E,'Governor Lundy',H_)]),
('2.3',1,[('0.7',HP,'crimson flags and cannon',H_)]),
('2.4',1,[('2.1',HP,'the parade route',H_)]),
('3.b',1,[('2.b',HP,'the parades',L)]),
('3.0',1,[('0.2',HP,'the siege story',H_)]),
('3.1',1,[('3.0',HP,'sense of threat',L)]),
('3.2',1,[('0.3',E,'the relief of 1689',H_)]),
('3.3',2,[('4.0',E,'the Bogside',H_),('3.2',HP,'unionist view of relief',L)]),
('3.4',1),
('3.5',1,[('0.4',HP,'the siege of 1689',H_)]),
('3.6',1,[('1.0',E,'the No Surrender Club',H_)]),
('4.0',1),
('4.1',1),
('4.2',1,[('4.0',E,'the Bogside',H_),('2.1',HP,'the August parade route',H_)]),
('4.3',2,[('4.1',HP,'gerrymandering grievance',H_)]),
('4.4',1,[('4.0',HP,'the Bogside',H_)]),
('5.b',1,[('4.0',E,'the Bogside',H_)]),
('5.0',1,[('4.0',E,'the Bogside',H_),('2.1',HP,'August parade along the walls',L)]),
('5.1',1,[('5.0',E,'the 12 August clashes',H_)]),
('5.2',1,[('5.1',E,'the Battle of the Bogside',H_)]),
('5.3',1,[('5.1',HP,'Battle of the Bogside',H_)]),
('5.4',2,[('5.1',HP,'August 1969 events',H_)]),
('5.5',1,[('5.0',HP,'the 1969 parade',H_)]),
('6.0',1,[('5.4',HP,'violence linked to parade',L)]),
('6.1',1),
('6.2',1,[('0.2',HP,'George Walker',H_)]),
('6.3',1,[('6.0',HP,'parade restrictions',L)]),
('6.4',1,[('3.0',HP,'siege mentality',H_)]),
('7.b',1,[('3.b',HP,'symbols and slogans',L)]),
('7.0',1,[('3.2',HP,'defence of Protestant liberty',H_)]),
('7.1',1,[('3.3',E,'nationalist view of parades',H_)]),
('7.2',2,[('4.3',E,'civil rights grievances in Derry',H_)]),
('7.3',2,[('7.0',HP,'contested meanings',L)]),
('7.4',1,[('4.0',HP,'the Bogside',L)]),
('7.5',1,[('4.3',E,'Derry civil rights movement',H_)]),
('8.0',1,[('5.0',E,'1969 parade',H_),('4.3',HP,'civil rights crisis',H_)]),
('8.1',1,[('5.3',E,'British troops deployed',H_)]),
('8.2',1,[('1.2',HP,'the Memorial Hall',H_)]),
('8.3',1,[('7.1',HP,'nationalist interpretation',L)]),
('8.4',1,[('6.3',HP,'parade routes negotiated',L)]),
('8.5',1,[('6.4',E,'Protestants leaving west bank',H_)]),
('9.0',1,[('1.0',HP,'commemorative tradition',H_)]),
('9.1',1,[('4.2',E,'parade route past the Bogside',H_)]),
('9.2',1,[('7.0',HP,'unionist view of parades',H_)]),
('9.3',1,[('3.4',E,'triumphalism',H_)]),
('9.4',2,[('7.3',HP,'commemoration with political meaning',L)]),
]
run('hist-ire5-s10.t1g1.txt','hist-ire5-s10.t1g1.json',d(rows))
