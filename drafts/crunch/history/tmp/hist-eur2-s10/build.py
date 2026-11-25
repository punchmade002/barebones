import json,re,sys
B='/Users/gabrielwhelan/barebones/.claude/worktrees/history-crunch/drafts/crunch/history/'
P='hist-eur2-s10.'
def L(i,s,w,c='high'): return (i,s,w,c)
E,H='essential','helpful'
S1=lambda n:'hist-eur2-s1.'+n
S5=lambda n:'hist-eur2-s5.'+n
T=lambda n:P+n
# package 1: id -> (cost, links)
p1={
'0.b':(1,[]),'0.0':(1,[]),'0.1':(1,[L(T('0.0'),H,'cultural nationalism')]),'0.2':(1,[]),
'0.3':(1,[L(T('0.0'),H,'cultural nationalism')]),
'1.b':(1,[]),'1.0':(1,[]),
'1.1':(1,[L(T('1.0'),E,'uses Wagner and Bayreuth'),L(T('19.0'),H,'uses anti-Semitism','low')]),
'1.2':(1,[L(S1('1.0'),H,'uses the new Reich of 1871')]),
'1.3':(1,[]),'1.4':(1,[]),'1.5':(1,[]),'1.6':(1,[L(T('1.5'),E,'uses Kipling')]),
'2.b':(1,[]),'2.0':(1,[]),'2.1':(1,[L(T('23.0'),H,'uses Russification')]),'2.2':(1,[]),'2.3':(1,[L(T('0.1'),H,'peoples without a state')]),
'3.b':(1,[]),'3.0':(1,[]),'3.1':(1,[]),'3.2':(1,[]),
'3.3':(1,[L(T('6.0'),H,'uses Le Feu'),L(T('5.1'),H,'uses Sassoon statement')]),
'3.4':(2,[L(T('4.b'),H,'patriotic idealism phase','low')]),
'4.b':(1,[L(T('0.3'),H,'pre-war cultural nationalism')]),'4.0':(1,[]),'4.1':(1,[L(T('4.0'),H,'uses Brooke')]),'4.2':(1,[]),'4.3':(1,[L(T('4.0'),H,'patriotic verse of Brooke','low')]),
'5.b':(1,[]),'5.0':(1,[]),'5.1':(1,[L(T('5.0'),H,'uses Sassoon')]),'5.2':(1,[L(T('5.1'),E,'uses Sassoon protest')]),
'5.3':(1,[L(T('5.0'),H,'uses Sassoon')]),'5.4':(1,[]),'5.5':(1,[L(T('8.b'),E,'uses Wilfred Owen')]),
'6.b':(1,[]),'6.0':(1,[]),'6.1':(1,[]),'6.2':(1,[]),'6.3':(1,[]),
'6.4':(1,[L(T('6.2'),H,'uses Remarque'),L(T('6.3'),H,'uses Graves and Brittain')]),
'7.b':(1,[]),'7.0':(1,[]),'7.1':(1,[]),'7.2':(1,[L(T('7.1'),H,'limits of poets view','low')]),
'8.b':(1,[]),'8.0':(2,[]),'8.1':(2,[]),'8.2':(1,[]),'8.3':(1,[L(T('5.2'),H,'uses Craiglockhart and Sassoon')]),
'8.4':(2,[]),'8.5':(1,[]),
'9.b':(1,[L(T('8.5'),H,'Owen as witness')]),
'9.0':(1,[L(T('8.4'),H,'uses Dulce et Decorum Est')]),'9.1':(1,[L(T('8.4'),H,'uses Owen poems')]),
'9.2':(1,[]),'9.3':(1,[]),'9.4':(1,[L(T('5.0'),H,'uses Sassoon','low')]),
'9.5':(1,[L(T('4.0'),H,'uses Brooke')]),'9.6':(1,[]),
'9.7':(2,[L(T('7.2'),H,'uses Todman myth argument')]),
'10.b':(1,[]),'10.0':(1,[L(S1('1.0'),H,'uses the Reich of 1871')]),'10.1':(1,[L(T('10.0'),H,'Catholic minority in Reich')]),
'10.2':(1,[L(S1('3.0'),H,'uses Reichsfeinde and Centre')]),
'10.3':(1,[L(T('10.2'),H,'uses Reichsfeinde')]),
'10.4':(1,[L(S1('3.0'),H,'uses National Liberals as partners')]),
'10.5':(1,[L(T('10.b'),H,'Kulturkampf conflict')]),
'11.b':(1,[]),'11.0':(1,[]),'11.1':(1,[L(T('11.0'),H,'earlier laws','low')]),'11.2':(1,[L(T('10.1'),H,'papacy and infallibility','low')]),
'11.3':(1,[]),'11.4':(2,[]),
'11.5':(1,[L(T('11.3'),E,'uses Prussian May Laws'),L(T('23.5'),E,'uses Russian May Laws'),L(S1('3.3'),E,'uses Anti-Socialist Law')]),
'12.b':(1,[]),'12.0':(1,[L(T('11.3'),E,'uses the Prussian laws')]),'12.1':(1,[L(T('11.3'),E,'uses state approval of priests')]),
'12.2':(1,[L(T('10.2'),E,'uses Centre Party and Windthorst')]),
'12.3':(2,[L(S1('3.5'),E,'uses tariff law of 1879'),L(S1('3.3'),E,'uses Anti-Socialist Law'),L(T('12.2'),H,'Centre strengthened')]),
'12.4':(1,[L(T('12.0'),H,'uses Pius IX')]),'12.5':(1,[L(T('12.4'),E,'uses Leo XIII negotiating')]),
'12.6':(1,[L(T('11.4'),H,'uses civil marriage'),L(T('11.1'),H,'uses Jesuit Law')]),
'13.b':(1,[]),'13.0':(1,[L(T('10.2'),H,'uses Centre Party')]),'13.1':(1,[L(T('12.2'),H,'Catholics united behind Centre')]),
'13.2':(1,[L(T('10.0'),H,'Protestant-led Reich')]),'13.3':(1,[L(T('10.4'),H,'liberals backed attack')]),
'14.b':(1,[]),'14.0':(1,[]),'14.1':(1,[L(T('10.1'),E,'uses papal infallibility')]),'14.2':(1,[L(T('14.0'),E,'uses loss of Rome')]),
'14.3':(1,[L(T('14.2'),E,'uses Law of Guarantees')]),'14.4':(1,[L(T('14.3'),E,'uses prisoner in Vatican')]),
'15.b':(1,[L(T('14.4'),H,'uses Roman Question')]),'15.0':(1,[]),'15.1':(1,[L(T('15.0'),E,'uses non expedit')]),'15.2':(1,[L(T('15.0'),H,'uses non expedit')]),
'15.3':(1,[]),'15.4':(2,[L(T('15.0'),E,'uses non expedit'),L(T('17.5'),H,'Leo XIII hard line')]),
'15.5':(1,[L(T('14.4'),E,'uses Roman Question')]),
'15.6':(1,[L(T('12.5'),H,'German conflict ended by compromise'),L(T('14.4'),H,'Italian Roman Question')]),
'16.b':(1,[]),'16.0':(1,[L(S1('2.0'),H,'uses Treaty of Frankfurt')]),'16.1':(1,[L(T('16.0'),H,'Third Republic origins')]),
'16.2':(2,[L(T('16.1'),E,'uses anticlerical republicans'),L(T('21.2'),H,'uses Dreyfus sides')]),
'17.b':(1,[L(T('14.4'),H,'confrontational Pius IX')]),'17.0':(1,[]),'17.1':(1,[L(T('14.3'),H,'prisoner in the Vatican')]),
'17.2':(1,[L(T('12.5'),H,'uses ending Kulturkampf')]),'17.3':(1,[]),'17.4':(1,[]),
'17.5':(1,[L(T('14.4'),E,'uses Roman Question'),L(T('15.0'),H,'uses non expedit')]),
'18.b':(1,[L(T('17.b'),H,'uses Leo XIII')]),'18.0':(1,[]),'18.1':(1,[L(T('18.0'),E,'uses Rerum Novarum')]),
'18.2':(1,[L(T('18.0'),E,'uses Rerum Novarum')]),'18.3':(1,[L(T('16.1'),H,'republicans and monarchist Catholics')]),
'18.4':(1,[L(T('18.3'),E,'uses the ralliement'),L(T('21.2'),H,'uses Dreyfus sides')]),
'18.5':(1,[L(T('18.0'),H,'uses Rerum Novarum')]),'18.6':(1,[L(T('18.3'),H,'uses the ralliement')]),
'19.b':(1,[]),'19.0':(1,[]),'19.1':(1,[]),'19.2':(1,[]),'19.3':(1,[]),
'20.b':(1,[L(T('19.b'),H,'anti-Semitism')]),'20.0':(1,[]),'20.1':(1,[]),'20.2':(1,[]),'20.3':(1,[L(T('20.2'),E,'uses Dreyfus and bordereau')]),
'21.b':(1,[]),'21.0':(1,[L(T('20.2'),E,'uses Dreyfus and bordereau')]),'21.1':(1,[L(T('21.0'),E,'uses Esterhazy cover-up')]),
'21.2':(1,[L(T('21.1'),H,'uses Zola and Dreyfus case')]),'21.3':(1,[]),'21.4':(1,[L(T('21.0'),H,'army forgery cover-up')]),
'21.5':(1,[L(T('20.3'),H,'first court martial')]),'21.6':(1,[L(T('21.5'),E,'uses Rennes verdict')]),
'22.b':(1,[]),'22.0':(1,[]),'22.1':(1,[L(T('16.2'),H,'uses anticlerical laws')]),'22.2':(1,[]),
'22.3':(1,[L(T('20.2'),H,'uses Dreyfus case')]),'22.4':(1,[L(T('22.3'),H,'uses Herzl')]),
'23.b':(1,[]),'23.0':(1,[]),'23.1':(1,[]),'23.2':(1,[]),'23.3':(1,[]),'23.4':(1,[L(T('23.3'),H,'uses pogroms')]),
'23.5':(1,[L(T('23.2'),H,'uses the Pale of Settlement','low')]),
'24.b':(1,[]),'24.0':(1,[]),'24.1':(1,[L(T('23.0'),H,'uses Russification')]),'24.2':(1,[]),
'24.3':(1,[L(T('23.3'),H,'uses pogroms')]),'24.4':(1,[L(T('23.3'),H,'uses pogroms')]),'24.5':(1,[]),
'25.b':(1,[]),'25.0':(1,[]),'25.1':(1,[L(T('25.0'),E,'uses the Protocols')]),'25.2':(1,[]),'25.3':(1,[]),'25.4':(1,[]),
'25.5':(1,[L(T('23.2'),H,'uses the Pale')]),
'26.b':(1,[]),'26.0':(1,[L(T('0.1'),H,'two kinds of nationalism')]),
'26.1':(2,[L(T('9.7'),H,'uses myth argument'),L(T('4.3'),H,'contemporaries preferred Brooke','low')]),
'26.2':(1,[L(T('13.0'),H,'uses political defeat')]),'26.3':(1,[L(T('15.6'),H,'uses Italy comparison','low')]),
'26.4':(1,[L(T('18.3'),H,'uses failed ralliement')]),
'26.5':(2,[L(T('21.6'),H,'uses Dreyfus outcome','low'),L(T('24.0'),H,'uses Russian policy','low')]),
}
# package 2: links to s5 only
p2={k:[] for k in p1}
def a(k,i,s,w,c='high'): p2[k].append(L(S5(i),s,w,c))
a('1.6','5.1','H' and H,'uses Battle of Loos')
a('3.0','3.0',H,'uses machine guns and artillery')
a('3.1','7.1',H,'uses Somme first day')
a('4.1','13.1',H,'uses Gallipoli landings')
a('5.2','2.3',H,'uses shell shock','low')
a('8.1','7.0',H,'uses the Somme sector','low')
a('9.1','4.0',H,'uses gas attacks')
a('9.3','20.3',H,'uses armistice 11 November')
a('25.5','12.0',H,'uses the Provisional Government')
# fix the Loos link id: Loos is s5.5.1
p2['1.6']=[L(S5('5.1'),H,'uses Battle of Loos')]
# a() prefixes 's5.' to 'i' e.g. '3.0' -> s5.3.0 correct
def fmt(l): return [{"id":i,"strength":s,"why":w,"confidence":c} for i,s,w,c in l]
def pack(p): return open(B+'packs/'+p).read()
def ids(txt):
    t=txt.split('CANDIDATES')[0]; return re.findall(r'^\[(hist-eur2-s10\.[^\]]+)\]',t,re.M)
def cands(txt): return set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
for name,mode in (('hist-eur2-s10.t1g1',1),('hist-eur2-s10.t1g2',2)):
    txt=pack(name+'.txt'); tid=ids(txt); allid=cands(txt)
    assert set(tid)=={P+k for k in p1}, (set(tid)^{P+k for k in p1})
    out={}; nl=lo=c2=0
    for i in tid:
        k=i[len(P):]
        if mode==1:
            c,l=p1[k]; out[i]={"cost":c,"needs":fmt(l)}; c2+=c==2
        else:
            l=p2[k]; out[i]={"needs":fmt(l)}
        for n in out[i]['needs']:
            assert n['id'] in allid and n['id']!=i,(i,n); nl+=1; lo+=n['confidence']=='low'
            if mode==2: assert n['id'].startswith('hist-eur2-s5.')
    json.dump(out,open(B+'point-links/'+name+'.json','w'),indent=1)
    json.loads(open(B+'point-links/'+name+'.json').read())
    print(name,len(out),nl,c2,lo)
