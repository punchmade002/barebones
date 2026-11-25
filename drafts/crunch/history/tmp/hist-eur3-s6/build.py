import json,re
B='/Users/gabrielwhelan/barebones/.claude/worktrees/history-crunch/drafts/crunch/history/'
P='hist-eur3-s6.'
def L(i,s,w,c='high'): return (i,s,w,c)
E,H='essential','helpful'
# id: (cost, [links])
A={
'0.b':(1,[]),'0.0':(1,[]),'0.1':(1,[]),'0.2':(1,[]),'0.3':(1,[]),
'0.4':(1,[L('0.3',H,'governments need a majority')]),
'0.5':(1,[L('0.4',H,'coalition government')]),
'0.6':(1,[]),'0.7':(1,[]),
'1.b':(1,[]),'1.0':(1,[]),'1.1':(1,[]),'1.2':(1,[]),
'1.3':(1,[L('0.4',H,'coalitions of right-wing groups')]),
'1.4':(1,[]),
'1.5':(1,[L('1.2',H,'reliance on German reparations')]),
'2.b':(1,[]),
'2.0':(1,[L('1.3',H,'Bloc National parties')]),
'2.1':(1,[L('1.2',H,'German reparations')]),
'2.2':(1,[L('2.1',E,'the Ruhr occupation')]),
'2.3':(1,[L('2.1',E,'the Ruhr occupation')]),
'2.4':(1,[L('2.1',E,'the Ruhr occupation')]),
'3.b':(1,[]),'3.0':(1,[]),
'3.1':(1,[L('2.0',H,"Poincare's hard line")]),
'3.2':(1,[L('3.1',E,'Briand and his policy')]),
'3.3':(1,[L('3.1',H,'Briand')]),
'3.4':(1,[]),
'4.b':(1,[]),
'4.0':(1,[L('0.5',H,'Radical Party'),L('0.6',H,'Socialists','low')]),
'4.1':(2,[L('4.0',E,'the Cartel government'),L('1.5',H,'falling franc')]),
'4.2':(1,[L('4.1',E,'franc crisis and fall of Cartel')]),
'4.3':(1,[L('4.2',E,'Poincare returns to power')]),
'4.4':(1,[L('4.3',H,'franc stabilisation')]),
'5.b':(1,[]),
'5.0':(1,[L('0.4',H,'coalition government')]),
'5.1':(1,[L('0.5',E,'Radical Party as hinge')]),
'5.2':(1,[L('0.3',E,'governments fall on lost votes')]),
'5.3':(1,[L('0.2',H,'role of the President','low')]),
'5.4':(1,[L('0.1',H,'Senate can block laws')]),
'5.5':(1,[L('0.2',E,'ceremonial role of President')]),
'6.b':(1,[]),'6.0':(1,[]),'6.1':(1,[]),'6.2':(1,[]),
'6.3':(2,[L('4.4',E,'franc fixed at 1928 value'),L('6.1',H,'the slump from 1931')]),
'6.4':(1,[L('6.3',E,'policy of deflation')]),
'6.5':(1,[L('6.3',H,'franc held at gold value'),L('9.b',H,'the Popular Front')]),
'6.6':(1,[L('7.b',H,'the leagues')]),
'7.b':(1,[]),'7.0':(1,[]),'7.1':(1,[]),'7.2':(1,[]),'7.3':(1,[]),
'7.4':(1,[L('8.6',H,'left unity after February 1934')]),
'7.5':(2,[]),
'7.6':(1,[L('7.2',E,'the Croix-de-Feu'),L('11.0',H,'leagues dissolved in 1936')]),
'8.b':(1,[]),'8.0':(1,[]),
'8.1':(1,[L('8.0',E,'Stavisky')]),
'8.2':(1,[L('8.1',H,'the Stavisky scandal')]),
'8.3':(1,[L('8.2',H,'Chautemps resignation')]),
'8.4':(2,[L('8.3',H,'Chiappe dismissal angered right'),L('7.b',H,'the leagues')]),
'8.5':(1,[L('8.4',E,'6 February riot')]),
'8.6':(1,[L('8.4',E,'6 February riot')]),
'9.b':(1,[]),
'9.0':(2,[L('0.6',H,'Communists and Socialists')]),
'9.1':(1,[L('8.6',H,'left unity after 1934')]),
'9.2':(1,[L('9.1',H,'Popular Front alliance')]),
'9.3':(1,[L('9.2',E,'Popular Front government')]),
'9.4':(1,[L('4.0',H,'Herriot and the Cartel')]),
'9.5':(1,[L('7.0',H,'Action francaise')]),
'9.6':(1,[L('0.1',H,'women had no vote')]),
'10.b':(1,[]),
'10.0':(1,[L('9.2',H,'Blum took office')]),
'10.1':(1,[]),
'10.2':(2,[L('10.1',E,'the strike wave'),L('9.2',H,'Blum as Prime Minister')]),
'10.3':(2,[L('10.2',E,'the Matignon Agreements')]),
'10.4':(1,[L('10.2',H,'June 1936 reforms')]),
'11.b':(1,[]),
'11.0':(1,[L('8.4',E,'the 6 February 1934 riot'),L('7.b',H,'the leagues')]),
'11.1':(1,[L('6.3',H,'deflation hurting farmers')]),
'11.2':(1,[]),'11.3':(1,[]),'11.4':(1,[]),
'11.5':(1,[L('6.5',H,'franc devaluation')]),
'11.6':(1,[L('12.0',H,'capital flight')]),
'12.b':(1,[]),'12.0':(1,[]),
'12.1':(1,[L('10.4',E,'the 40-hour week')]),
'12.2':(2,[]),
'12.3':(1,[]),
'12.4':(1,[L('9.5',H,'anti-Semitic attacks on Blum')]),
'13.b':(1,[]),
'13.0':(1,[L('12.0',H,'financial pressure and capital flight')]),
'13.1':(1,[L('0.1',H,'Senate powers')]),
'13.2':(1,[L('13.1',H,'Blum resigns first time')]),
'13.3':(1,[L('10.4',E,'the 40-hour week')]),
'13.4':(1,[L('13.3',H,'Reynaud decree-laws')]),
'14.b':(1,[]),'14.0':(1,[]),
'14.1':(1,[L('14.0',H,'the Maginot Line')]),
'14.2':(1,[]),
'14.3':(1,[L('14.1',H,'the Maginot Line')]),
'14.4':(1,[]),
'14.5':(1,[L('14.4',H,'army doctrine on tanks'),L('21.0','helpful','de Gaulle on armoured warfare')]),
'15.b':(1,[]),'15.0':(1,[]),'15.1':(1,[]),'15.2':(1,[]),
'16.b':(1,[]),
'16.0':(1,[L('14.1',H,'Maginot Line')]),
'16.1':(1,[]),
'16.2':(2,[L('14.3',H,'Ardennes weakness'),L('16.0',H,'Gamelin as commander')]),
'16.3':(2,[L('16.2',E,'Ardennes and the Dyle plan')]),
'16.4':(1,[L('16.3',H,'northern armies cut off')]),
'17.b':(1,[]),'17.0':(1,[]),
'17.1':(1,[L('17.0',H,'government leaving Paris'),L('20.2','helpful','Petain becoming Prime Minister','low')]),
'17.2':(1,[L('17.1',E,'Petain asking for armistice')]),
'17.3':(1,[L('17.2',E,'the armistice terms')]),
'17.4':(1,[L('17.2',E,'the armistice')]),
'17.5':(1,[L('17.2',E,'the armistice')]),
'17.6':(1,[]),
'18.b':(1,[]),
'18.0':(1,[L('17.3',H,'the unoccupied zone')]),
'18.1':(2,[L('18.0',H,'government settled at Vichy'),L('17.1',H,'Petain as leader')]),
}
def build(pack,out,table,costs):
    txt=open(B+'packs/'+pack).read()
    tg=txt.split('CANDIDATES')[0]
    ids=re.findall(r'^\[([^\]]+)\]',tg,re.M)
    allids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
    res={}
    for i in ids:
        k=i[len(P):]
        c,ls=table[k]
        d={}
        if costs: d['cost']=c
        d['needs']=[{'id':P+l[0],'strength':l[1],'why':l[2],'confidence':l[3]} for l in ls]
        res[i]=d
    assert set(table)=={i[len(P):] for i in ids},(set(table)^{i[len(P):] for i in ids})
    for d in res.values():
        for n in d['needs']:
            assert n['id'] in allids and n['id']!=list(res)[0] or True
    json.dump(res,open(B+'point-links/'+out,'w'),ensure_ascii=False,indent=0)
    return res,allids
r,a=build('hist-eur3-s6.t1g1.txt','hist-eur3-s6.t1g1.json',A,True)
for i,d in r.items():
    for n in d['needs']:
        assert n['id'] in a and n['id']!=i,(i,n)
print(len(r),sum(len(d['needs']) for d in r.values()),sum(d['cost']==2 for d in r.values()),sum(n['confidence']=='low' for d in r.values() for n in d['needs']))
# package 2
S='hist-eur3-s9.'
def M(i,s,w,c='high'): return (S+i,s,w,c)
T={k:[] for k in A}
T['14.3']=[M('3.0',H,'Ardennes unsuitable for tanks','low')]
T['14.4']=[M('17.0',H,'tanks spread among infantry')]
T['14.5']=[M('1.0',H,'concentrated armoured Panzer divisions','low')]
T['15.2']=[M('22.4',H,'appeasement policy','low')]
T['16.0']=[M('2.2',H,'the Phoney War')]
T['16.1']=[M('0.1',E,'the Nazi-Soviet Pact')]
T['16.2']=[M('3.0',H,'German thrust through the Ardennes')]
T['16.3']=[M('3.2',H,'the sickle cut through the Ardennes')]
T['16.4']=[M('3.4',H,'Operation Dynamo and Dunkirk')]
T['17.0']=[M('3.5',H,'Italy entering the war')]
T['17.2']=[M('3.6',H,'the Franco-German armistice')]
res={}
txt=open(B+'packs/hist-eur3-s6.t1g2.txt').read()
allids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
ids=re.findall(r'^\[([^\]]+)\]',txt.split('CANDIDATES')[0],re.M)
for i in ids:
    k=i[len(P):]
    res[i]={'needs':[{'id':l[0],'strength':l[1],'why':l[2],'confidence':l[3]} for l in T[k]]}
for i,d in res.items():
    for n in d['needs']: assert n['id'] in allids
json.dump(res,open(B+'point-links/hist-eur3-s6.t1g2.json','w'),ensure_ascii=False,indent=0)
print(len(res),sum(len(d['needs']) for d in res.values()),sum(n['confidence']=='low' for d in res.values() for n in d['needs']))
