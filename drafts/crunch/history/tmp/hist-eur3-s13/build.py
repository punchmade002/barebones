import json,re
B='/Users/gabrielwhelan/barebones/.claude/worktrees/history-crunch/drafts/crunch/history/'
P='hist-eur3-s13.'
def L(i,s,w,c='high'): return {"id":i,"strength":s,"why":w,"confidence":c}
E,H='essential','helpful'
# (id, cost, needs)
A=[
('0.b',1,[]),
('0.0',2,[]),
('0.1',1,[L(P+'0.0',E,'the Roman Question quarrel')]),
('0.2',1,[L('hist-eur3-s1.5.2',H,'Mussolini taking office October 1922'),L('hist-eur3-s1.7.4',H,'ban on opposition parties, one-party state')]),
('0.3',1,[]),
('0.4',1,[L('hist-eur3-s1.1.0',H,'Popolari, the Catholic party')]),
('1.b',1,[]),
('1.0',1,[L(P+'0.3',H,'Mussolini needing Catholic support')]),
('1.1',1,[L(P+'0.0',E,'the Roman Question')]),
('1.2',1,[]),
('2.b',1,[]),
('2.0',2,[]),
('2.1',1,[]),
('2.2',1,[L(P+'0.0',E,'Papal States and Roman Question')]),
('2.3',1,[L(P+'0.0',E,'Papal States lost in 1870')]),
('2.4',1,[L(P+'2.1',E,'the concordat document')]),
('2.5',1,[L(P+'2.1',H,'the concordat document')]),
('2.6',1,[L(P+'1.2',H,'Catholic Action')]),
('3.b',1,[]),
('3.0',1,[L('hist-eur3-s1.7.7',E,'single list and 1929 plebiscite')]),
('3.1',1,[L(P+'1.0',H,'Mussolini wanting Catholic support')]),
('3.2',1,[L(P+'1.1',H,'Pope Pius XI')]),
('3.3',1,[L(P+'2.4',E,'Catholicism as state religion in concordat')]),
('4.b',1,[]),
('4.0',1,[L(P+'1.2',E,'Catholic Action'),L('hist-eur3-s1.10.0',H,'Fascist youth organisation')]),
('4.1',1,[L(P+'4.0',E,'Catholic youth groups as rivals')]),
('4.2',1,[L(P+'4.1',E,'dissolution of Catholic youth groups')]),
('4.3',1,[L(P+'4.1',E,'the 1931 youth dispute')]),
('4.4',1,[L(P+'4.2',H,'the encyclical Non abbiamo bisogno')]),
('5.b',1,[]),
('5.0',1,[L('hist-eur3-s1.13.1',E,'the Rome-Berlin Axis')]),
('5.1',1,[L(P+'5.0',H,'Manifesto of the Race','low')]),
('5.2',1,[L(P+'5.1',E,'the marriage ban'),L(P+'2.5',E,'concordat marriage terms')]),
('5.3',1,[L(P+'5.1',H,'the racial laws')]),
('5.4',1,[L(P+'5.2',H,'Pius XI objecting to marriage ban')]),
('5.5',1,[L(P+'1.1',E,'Pope Pius XI')]),
('6.b',1,[]),
('6.0',1,[]),
('6.1',1,[]),
('6.2',2,[]),
('6.3',1,[]),
('6.4',2,[]),
('6.5',1,[L(P+'6.2',H,'Nazi regime coming to power','low')]),
('7.b',1,[]),
('7.0',1,[L(P+'2.1',E,'what a concordat is'),L(P+'5.5',H,'Pacelli later Pius XII')]),
('7.1',1,[L(P+'7.0',E,'the Reich Concordat')]),
('7.2',1,[L(P+'7.0',H,'the Concordat being concluded')]),
('7.3',1,[L(P+'7.0',E,'the Reich Concordat treaty')]),
('8.b',1,[]),
('8.0',1,[L(P+'1.2',H,'Catholic Action')]),
('8.1',1,[]),
('8.2',1,[]),
('8.3',1,[]),
('8.4',1,[]),
('8.5',1,[]),
('8.6',1,[L(P+'7.1',E,'terms of the Concordat')]),
('9.b',1,[]),
('9.0',1,[L(P+'6.0',E,'the 28 regional churches')]),
('9.1',1,[L(P+'9.0',H,'the Reichskirche plan')]),
('9.2',1,[L(P+'9.1',E,'the German Christians')]),
('9.3',1,[L(P+'9.1',E,'the German Christians')]),
('9.4',1,[L(P+'9.0',H,'the Reichskirche')]),
('10.b',1,[]),
('10.0',1,[L(P+'9.1',E,'the German Christians'),L(P+'9.2',H,'demand to drop Old Testament')]),
('10.1',1,[L(P+'9.4',E,'Müller as Reich Bishop')]),
('10.2',1,[L(P+'9.0',H,'Nazi control of Protestant churches')]),
('10.3',1,[L(P+'9.1',E,'the German Christians'),L(P+'11.0',E,'the Confessing Church')]),
('11.b',1,[]),
('11.0',1,[L(P+'9.0',H,'the Reich Church it opposed')]),
('11.1',1,[L(P+'11.0',H,'the Confessing Church')]),
('11.2',1,[L(P+'11.1',E,'the Barmen Declaration')]),
('11.3',1,[L(P+'11.0',H,'the Confessing Church')]),
('12.b',1,[]),
('12.0',2,[L(P+'11.0',E,"Pastors' Emergency League, Confessing Church")]),
('12.1',2,[L(P+'12.0',E,'Niemöller')]),
('12.2',2,[L(P+'11.0',H,'the Confessing Church')]),
('12.3',2,[L(P+'12.2',E,'Bonhoeffer')]),
('12.4',1,[L(P+'12.3',H,"Bonhoeffer's resistance and arrest")]),
('13.b',1,[]),
('13.0',2,[]),
('13.1',1,[L(P+'13.0',E,'Mit brennender Sorge'),L(P+'8.6',E,'the breaches of the Concordat')]),
('13.2',1,[L(P+'13.0',E,'Mit brennender Sorge')]),
('13.3',2,[L(P+'13.4',H,'the T4 programme','low')]),
('13.4',1,[L(P+'13.3',E,'the T4 euthanasia programme')]),
('13.5',1,[L(P+'13.3',E,'Bishop Galen')]),
('14.b',1,[]),
('14.0',1,[L(P+'13.3',H,'opposition to euthanasia programme')]),
('14.1',1,[]),
('14.2',1,[]),
('14.3',2,[L(P+'5.5',H,'Pius XII')]),
('14.4',1,[L(P+'14.3',E,"Pius XII's silence")]),
('14.5',1,[L(P+'6.4',E,'Bormann, Himmler, Rosenberg hostile to Christianity')]),
('15.b',1,[]),
('15.0',1,[L(P+'2.0',H,'the 1929 Lateran settlement'),L(P+'7.0',H,'the 1933 Reich Concordat'),L(P+'4.1',H,'the youth clash'),L(P+'5.1',H,'the racial laws')]),
('15.1',1,[L(P+'4.3',E,'the 1931 compromise'),L(P+'5.4',E,'the 1938 protest without a break')]),
('15.2',1,[L(P+'8.6',H,'persecution after the Concordat')]),
('15.3',1,[]),
('16.b',1,[]),
('16.0',1,[]),
('16.1',1,[]),
('16.2',1,[L(P+'16.1',E,'the British Broadcasting Company')]),
('16.3',1,[L(P+'16.2',H,'the BBC as a corporation')]),
('16.4',1,[L(P+'16.2',H,'Reith as director-general')]),
('16.5',1,[L(P+'16.2',H,'the BBC')]),
('17.b',1,[]),
('17.0',1,[]),
('17.1',1,[L(P+'17.0',H,'American commercial networks')]),
('17.2',1,[L(P+'16.3',H,'the BBC monopoly')]),
]
S=[
('5.1',[L('hist-eur3-s3.10.4',H,'Nuremberg Laws against Jews')]),
('6.2',[L('hist-eur3-s3.1.5',H,'Enabling Act vote and Centre Party'),L('hist-eur3-s3.2.b',H,'Gleichschaltung')]),
('6.4',[L('hist-eur3-s3.5.0',H,'Himmler')]),
('7.0',[L('hist-eur3-s3.0.0',H,'Papen as Vice-Chancellor')]),
('7.2',[L('hist-eur3-s3.2.4',H,'parties dissolved in 1933')]),
('8.0',[L('hist-eur3-s3.3.2',E,'the Night of the Long Knives'),L('hist-eur3-s3.3.3',H,'Klausener killed in purge')]),
('8.1',[L('hist-eur3-s3.9.4',E,'Hitler Youth Law of 1936')]),
('8.4',[L('hist-eur3-s3.6.0',E,'Dachau camp')]),
('11.1',[L('hist-eur3-s3.4.2',H,'the Führer principle')]),
('12.1',[L('hist-eur3-s3.6.0',H,'Dachau camp'),L('hist-eur3-s3.6.1',H,'Sachsenhausen camp')]),
('12.2',[L('hist-eur3-s3.5.2',H,'the Gestapo')]),
('13.2',[L('hist-eur3-s3.5.2',H,'the Gestapo')]),
('13.3',[L('hist-eur3-s3.5.2',H,'Gestapo seizures')]),
]
Sd=dict(S)
def pkg(f):
    t=open(B+'packs/'+f+'.txt').read()
    ids=re.findall(r'^\[(\S+)\]',t,re.M)
    tgt=[]
    sec=None
    for line in t.splitlines():
        if line.startswith('TARGET'): sec='T'
        elif line.startswith('CANDIDATES'): sec='C'
        m=re.match(r'\[(\S+)\]',line)
        if m and sec=='T': tgt.append(m.group(1))
    return set(ids),tgt
out=[(('t1g1'),{}),('t1g2',{})]
d1={P+i:{"cost":c,"needs":n} for i,c,n in A}
d2={P+i:{"needs":Sd.get(i,[])} for i,_,_ in A}
for name,d in (('t1g1',d1),('t1g2',d2)):
    ids,tgt=pkg('hist-eur3-s13.'+name)
    assert list(d)==tgt,(set(tgt)^set(d))
    for k,v in d.items():
        for n in v['needs']: assert n['id'] in ids and n['id']!=k,(k,n['id'])
    json.dump(d,open(B+'point-links/hist-eur3-s13.'+name+'.json','w'),ensure_ascii=False)
    links=sum(len(v['needs']) for v in d.values())
    low=sum(1 for v in d.values() for n in v['needs'] if n['confidence']=='low')
    print(name,len(d),links,sum(1 for v in d.values() if v.get('cost')==2),low)
