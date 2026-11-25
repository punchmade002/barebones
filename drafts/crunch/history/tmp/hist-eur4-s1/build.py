import json,re
P='hist-eur4-s1.'
D='/Users/gabrielwhelan/barebones/.claude/worktrees/history-crunch/drafts/crunch/history/'
def H(t,w,c='high'): return (t,'helpful',w,c)
def E(t,w,c='high'): return (t,'essential',w,c)
d={
'0.b':(1,[]),'0.0':(1,[]),'0.1':(1,[]),'0.2':(1,[]),'0.3':(1,[]),'0.4':(1,[]),'0.5':(1,[]),'0.6':(1,[]),
'1.b':(1,[]),'1.0':(1,[H('0.0','the Grand Alliance')]),'1.1':(2,[]),'1.2':(1,[]),'1.3':(1,[]),'1.4':(2,[E('1.3','the percentages agreement')]),
'2.b':(1,[]),'2.0':(1,[]),'2.1':(1,[]),'2.2':(2,[H('12.0','the Lublin government')]),'2.3':(1,[]),'2.4':(1,[]),
'2.5':(1,[H('2.1','the zones agreed at Yalta'),H('2.2','the promises on Poland')]),
'3.b':(1,[]),'3.0':(1,[]),'3.1':(1,[H('4.0','the Potsdam Conference')]),'3.2':(1,[]),'3.3':(1,[H('3.2','Red Army occupation')]),
'3.4':(1,[H('0.4','invasions of 1914 and 1941')]),'3.5':(1,[E('3.4','the buffer zone')]),'3.6':(2,[]),
'4.b':(1,[]),'4.0':(1,[H('3.1','Attlee replacing Churchill')]),'4.1':(2,[]),'4.2':(1,[]),'4.3':(1,[]),'4.4':(1,[]),
'5.b':(1,[]),'5.0':(1,[]),'5.1':(1,[H('2.1','France getting a zone at Yalta')]),'5.2':(1,[H('5.0','the Soviet zone')]),'5.3':(1,[E('5.2','Berlin inside the Soviet zone')]),
'6.b':(1,[]),'6.0':(1,[H('4.2','reparations at Potsdam')]),'6.1':(1,[H('6.0','reparations from zones')]),'6.2':(1,[]),'6.3':(1,[]),'6.4':(1,[H('4.1','Potsdam single economic unit')]),
'7.b':(1,[]),'7.0':(1,[]),'7.1':(1,[]),'7.2':(1,[E('7.1','Kennan and the Long Telegram')]),'7.3':(1,[H('7.1','Western counterpart telegram')]),
'7.4':(1,[]),'7.5':(1,[E('7.4','Churchill\'s Fulton speech')]),'7.6':(1,[E('7.4','replying to the Fulton speech')]),
'8.b':(1,[]),'8.0':(1,[]),'8.1':(2,[H('8.4','the Truman Doctrine')]),'8.2':(1,[]),'8.3':(1,[H('8.0','Greece and Turkey aid')]),'8.4':(1,[H('8.3','the request to Congress')]),
'9.b':(1,[]),'9.0':(1,[]),'9.1':(1,[H('9.0','the Marshall Plan')]),'9.2':(1,[H('9.0','the Marshall Plan')]),'9.3':(1,[H('9.2','the aid being shared')]),'9.4':(1,[E('9.0','the Marshall Plan offer')]),
'10.b':(1,[]),'10.0':(1,[E('9.0','the Marshall Plan talks')]),'10.1':(1,[H('9.0','answer to Marshall aid')]),'10.2':(1,[]),
'10.3':(1,[E('10.2','the Cominform meeting')]),'10.4':(1,[E('10.2','the Cominform')]),'10.5':(1,[H('9.0','answer to Marshall Plan')]),
'11.b':(1,[]),'11.0':(2,[]),'11.1':(1,[H('11.0','the first stage')]),'11.2':(1,[]),'11.3':(2,[H('11.4','land reform')]),'11.4':(1,[]),'11.5':(1,[]),
'12.b':(1,[]),'12.0':(1,[H('2.2','Yalta promises on Poland')]),'12.1':(1,[H('12.0','Polish underground and Lublin')],),'12.2':(1,[]),'12.3':(2,[]),'12.4':(1,[H('12.3','the PZPR')]),
'12.5':(1,[]),'12.6':(1,[H('12.5','the Smallholders')]),'12.7':(2,[H('12.5','the Smallholders')]),
'13.b':(1,[]),'13.0':(1,[]),'13.1':(1,[]),'13.2':(1,[]),'13.3':(1,[H('13.2','Romania\'s communist government')]),'13.4':(1,[]),'13.5':(1,[H('13.4','Bulgarian Fatherland Front')]),
'13.6':(1,[]),'13.7':(1,[H('13.6','Czechoslovak communist government')]),
'14.b':(1,[]),'14.0':(1,[H('13.7','the 1948 Czechoslovak takeover')]),'14.1':(1,[E('6.3','the SED')]),'14.2':(1,[]),
'14.3':(1,[E('14.2','Tito and Yugoslavia'),H('10.2','the Cominform')]),
'14.4':(2,[H('13.1','Rajk'),H('14.3','Titoists')]),
'15.b':(1,[]),'15.0':(1,[H('11.5','satellite states')]),'15.1':(1,[E('11.2','salami tactics')]),
'15.2':(2,[H('12.2','Mikolajczyk'),H('12.6','Kovacs'),H('13.5','Petkov'),H('13.2','Maniu'),H('12.3','the PZPR merger')]),
'15.3':(1,[E('13.0','Mindszenty\'s trial')]),'15.4':(1,[E('14.2','Tito and Yugoslavia')]),
'16.b':(1,[]),'16.0':(1,[H('6.4','Germany as a single unit')]),'16.1':(1,[E('4.4','the Allied Control Council')]),'16.2':(1,[E('6.4','Bizonia')]),'16.3':(1,[]),'16.4':(1,[E('16.3','the currency reform')]),
'17.b':(1,[]),'17.0':(1,[H('16.3','currency reform and West Berlin')]),'17.1':(1,[E('16.3','the new currency'),H('16.0','the West German state')]),
'17.2':(1,[E('17.0','the blockade')]),'17.3':(1,[H('17.2','the airlift'),H('5.2','Berlin sectors')]),'17.4':(1,[H('17.2','the airlift')]),
'17.5':(2,[H('6.1','Lucius Clay'),H('17.0','the blockade')]),'17.6':(1,[E('17.0','the blockade')]),
'18.b':(1,[]),'18.0':(1,[E('17.0','the blockade')]),'18.1':(1,[]),'18.2':(1,[H('14.1','Ulbricht and the SED')]),'18.3':(1,[H('5.2','the divided Berlin sectors')]),
'19.b':(1,[]),'19.0':(1,[]),'19.1':(2,[]),'19.2':(1,[E('19.1','NATO')]),'19.3':(1,[H('19.1','NATO')]),'19.4':(1,[H('19.1','NATO')]),
'19.5':(2,[E('19.4','West German entry into NATO')]),'19.6':(1,[E('19.5','the Warsaw Pact')]),
'20.b':(1,[]),'20.0':(1,[H('11.0','how eastern Europe was taken over')]),'20.1':(1,[H('3.6','the atomic monopoly')]),'20.2':(2,[]),'20.3':(2,[H('3.4','the buffer zone')]),'20.4':(1,[E('16.3','the currency reform')]),
'21.b':(1,[]),'21.0':(1,[H('11.5','satellite states')]),'21.1':(1,[H('10.2','the Cominform'),H('10.5','Comecon')]),'21.2':(1,[H('13.1','Rajk'),H('14.4','Kostov and purges')]),
'21.3':(1,[E('14.3','Yugoslavia\'s expulsion')]),'21.4':(1,[E('17.2','the airlift')]),'21.5':(2,[H('9.4','Marshall aid'),H('19.1','NATO')]),
}
ids=[l.split(']')[0][1:] for l in open(D+'packs/hist-eur4-s1.t1g1.txt') if l.startswith('[')]
assert [P+k for k in d]==ids or set(P+k for k in d)==set(ids),(set(ids)^set(P+k for k in d))
out={};low=0;links=0;c2=0
for i in ids:
    c,n=d[i[len(P):]]
    needs=[]
    for t,s,w,cf in n:
        assert P+t in ids and P+t!=i
        needs.append({'id':P+t,'strength':s,'why':w,'confidence':cf});low+=cf=='low'
    links+=len(needs);c2+=c==2
    out[i]={'cost':c,'needs':needs}
json.dump(out,open(D+'point-links/hist-eur4-s1.t1g1.json','w'),indent=0)
print(len(out),links,c2,low)
