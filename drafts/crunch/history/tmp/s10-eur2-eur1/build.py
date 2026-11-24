import json,re,sys
H='/Users/gabrielwhelan/barebones/drafts/crunch/history/'
def run(pack,out,data):
    p='hist-eur2-s10.' if 's10' in pack else 'hist-eur1-s1.'
    txt=open(H+'packs/'+pack).read()
    targ=[]
    sec=None
    for ln in txt.split('\n'):
        if ln.startswith('TARGET'): sec='t'
        elif ln.startswith('CANDIDATES'): sec='c'
        m=re.match(r'\[([^\]]+)\]',ln)
        if m and sec=='t': targ.append(m.group(1))
    allids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
    res={}
    for k,(cost,needs) in data:
        res[p+k]={'cost':cost,'needs':[{'id':(i if i.startswith('hist-') else p+i),'strength':s,'why':w,'confidence':c} for i,s,w,c in needs]}
    assert list(res)==targ,(set(targ)^set(res),len(targ),len(res))
    for k,v in res.items():
        for n in v['needs']:
            assert n['id'] in allids and n['id']!=k,(k,n)
    json.dump(res,open(H+'point-links/'+out,'w'),indent=1)
    nl=sum(len(v['needs']) for v in res.values())
    lo=sum(n['confidence']=='low' for v in res.values() for n in v['needs'])
    print(out,len(res),nl,sum(v['cost']==2 for v in res.values()),lo)
h,e='helpful','essential'
H_,L_='high','low'
S10=[
('0.b',(1,[])),('0.0',(1,[])),('0.1',(1,[])),('0.2',(1,[])),('0.3',(1,[])),('0.4',(1,[])),
('0.5',(2,[('hist-eur2-s5.2.0',h,'Loos battle, 1915',H_)])),
('0.6',(1,[])),
('1.b',(1,[])),
('1.0',(2,[('hist-eur2-s5.4.0',h,'Gallipoli campaign',H_)])),
('1.1',(2,[])),('1.2',(2,[])),('1.3',(1,[])),('1.4',(1,[])),
('1.5',(2,[('1.2',h,'Graves as war writer',H_)])),
('1.6',(1,[])),
('2.b',(1,[])),('2.0',(1,[])),
('2.1',(1,[('hist-eur2-s5.2.3',h,'the Somme battle',H_)])),
('2.2',(1,[('1.1',h,'Craiglockhart, shell shock treatment',H_)])),
('2.3',(1,[('1.1',h,'Sassoon introduced',H_),('2.2',h,'Owen at Craiglockhart',H_)])),
('2.4',(2,[])),('2.5',(1,[])),('2.6',(2,[])),('2.7',(1,[])),
('2.8',(1,[('1.0',h,'Brooke as popular war poet',H_)])),
('2.9',(2,[('1.b',h,"the 'poets' war' view",L_)])),
('3.0',(2,[('hist-eur2-s1.0.0',h,'the new German Reich',L_)])),
('3.1',(1,[('3.0',h,'Catholic loyalty and Centre Party',H_)])),
('3.2',(2,[('3.1',h,'Kulturkampf campaign',H_)])),
('3.3',(2,[])),
('3.4',(2,[('3.3',e,'the May Laws',H_)])),
('3.5',(2,[('hist-eur2-s1.1.3',h,'tariffs of 1879',H_),('hist-eur2-s1.1.1',h,'Anti-Socialist Law',L_)])),
('3.6',(1,[('3.4',h,'Centre Party strengthened by resistance',H_)])),
('4.0',(1,[])),
('4.1',(1,[('4.0',e,'loss of Rome and temporal power',H_)])),
('4.2',(1,[('4.1',e,'Pope refusing to accept Italy',H_)])),
('4.3',(1,[('4.2',h,'Roman Question dispute',H_)])),
('4.4',(1,[('4.2',h,'anticlerical state vs Catholics',L_)])),
('4.5',(2,[('4.3',e,'the non expedit ban',H_),('4.2',h,'the Roman Question',H_)])),
('5.b',(1,[])),('5.0',(1,[])),
('5.1',(1,[('3.5',e,'Kulturkampf repeal negotiations',H_),('3.1',h,'the Kulturkampf',H_)])),
('5.2',(2,[])),
('5.3',(1,[('5.2',e,'Rerum Novarum',H_)])),
('5.4',(2,[('6.1',h,'the Dreyfus Affair',H_)])),
('5.5',(2,[])),
('5.6',(1,[('4.1',e,"'prisoner in the Vatican' stance",H_),('4.2',h,'Roman Question',H_)])),
('5.7',(1,[('5.4',h,'accommodation with republics',L_)])),
('5.8',(2,[('5.2',h,'Rerum Novarum',H_),('5.4',h,'ralliement policy',H_)])),
('6.b',(1,[])),
('6.0',(2,[('hist-eur2-s1.0.6',h,'1871 defeat, loss of Alsace',H_)])),
('6.1',(2,[])),
('6.2',(2,[('6.1',e,'Dreyfus case and bordereau',H_)])),
('6.3',(1,[('6.2',e,'army cover-up of Esterhazy',H_)])),
('6.4',(1,[('6.1',e,'the Dreyfus Affair',H_)])),
('6.5',(2,[('6.1',e,"Dreyfus's conviction",H_)])),
('6.6',(2,[('6.1',e,'the Affair',H_),('5.4',h,'anticlerical measures',L_)])),
('7.0',(1,[])),
('7.1',(1,[('hist-eur2-s8.0.4',h,'assassination of Alexander II',H_)])),
('7.2',(2,[('7.0',e,'the Pale of Settlement',H_)])),
('7.3',(1,[('hist-eur2-s8.0.5',h,'Alexander III, Nicholas II, Russification',H_)])),
('7.4',(1,[('7.1',h,'pogroms',H_),('hist-eur2-s8.4.0',h,'1905 revolution',L_)])),
('7.5',(1,[])),
('7.6',(1,[('6.6',h,'Zionism',L_)])),
('8.0',(2,[('0.2',h,'Czech cultural nationalism',H_),('0.3',h,'Finnish cultural nationalism',H_)])),
('8.1',(2,[('1.0',h,"Brooke's patriotism",H_),('2.9',h,"Owen's reputation",H_)])),
('8.2',(2,[('3.6',e,'Kulturkampf failure',H_),('3.2',h,'laws on schools and marriage',H_)])),
('8.3',(1,[('4.2',e,'the Roman Question',H_),('4.3',h,'non expedit ban',H_)])),
('8.4',(2,[('5.1',h,'ending Kulturkampf',H_),('5.3',h,'social teaching',H_),('5.4',h,'failed ralliement',H_),('5.6',h,'refusing unification',H_)])),
('8.5',(2,[('6.5',e,'Dreyfus outcome',H_),('7.3',h,'state-encouraged anti-Semitism',H_),('7.6',h,'mass emigration',H_)])),
]
S1=[
('0.b',(1,[])),('0.0',(1,[])),('0.1',(2,[])),('0.2',(1,[])),('0.3',(2,[])),
('0.4',(2,[('0.3',h,'Austrian Netherlands/Belgium arrangements',L_)])),
('0.5',(1,[])),('0.6',(1,[])),('0.7',(1,[])),('0.8',(1,[])),('0.9',(1,[])),
('1.0',(1,[])),('1.1',(1,[('1.0',e,'the German Confederation',H_)])),
('1.2',(1,[('1.1',h,'the Diet',H_)])),('1.3',(1,[('1.0',h,'the Bund',H_)])),
('1.4',(2,[('1.0',h,'the Federal Act',H_)])),('1.5',(1,[])),
('2.b',(1,[])),('2.0',(1,[])),('2.1',(1,[])),('2.2',(1,[('2.0',h,'allied settlement and Concert',L_)])),
('2.3',(2,[('2.b',h,'Congress System',H_)])),
('2.4',(1,[('2.3',e,'right to intervene',H_)])),
('2.5',(2,[('2.3',h,'intervention principle',H_)])),
('2.6',(1,[('2.5',e,"Britain leaving the Congress System",H_)])),
('3.b',(1,[])),('3.0',(1,[])),('3.1',(1,[])),
('3.2',(2,[('1.1',h,'the Diet adopting the Decrees',H_)])),
('3.3',(1,[('4.0',e,'the Burschenschaften',H_),('3.2',e,'the Carlsbad Decrees',H_)])),
('3.4',(1,[('3.3',e,'the Carlsbad Decrees',H_)])),
('3.5',(2,[('4.9',e,'the Hambach Festival',H_),('1.1',h,'the Diet',H_)])),
('3.6',(1,[('3.5',h,'the 1832 measures',H_)])),
('3.7',(1,[('2.3',h,'congress justification for intervention',H_),('4.2',h,'1821 Italian risings',H_)])),
('3.8',(1,[('1.2',h,'Austria-Prussia cooperation in Bund',H_)])),
('4.0',(1,[])),('4.1',(1,[('4.0',h,'student movement',L_)])),('4.2',(1,[])),('4.3',(2,[])),
('4.4',(1,[('4.3',e,'Greek independence war',H_)])),
('4.5',(1,[('0.2',h,'Bourbon legitimacy',L_)])),
('4.6',(2,[('0.3',h,'Netherlands including Belgium',H_)])),
('4.7',(1,[('0.6',e,'Congress Kingdom of Poland',H_)])),
('4.8',(1,[('0.8',h,'the Papal States',H_)])),
('4.9',(1,[])),
('5.0',(1,[])),('5.1',(1,[('5.0',h,'Prussian customs system',H_)])),
('5.2',(1,[('5.1',h,'the Zollverein',H_)])),('5.3',(1,[('5.1',h,'the Zollverein',H_)])),
('5.4',(1,[('5.1',h,'leadership of the Zollverein',H_)])),
('6.0',(1,[])),('6.1',(1,[('7.b',h,'who Metternich was',H_)])),
('6.2',(1,[('6.1',e,"Metternich's fall",H_)])),('6.3',(1,[('6.2',h,'1848 revolutions',H_)])),
('7.b',(1,[])),('7.0',(1,[])),('7.1',(1,[('0.b',h,'the Congress of Vienna',H_)])),
('7.2',(1,[])),
('7.3',(2,[('3.2',e,'the Carlsbad Decrees',H_),('2.3',h,'Troppau congress',H_),('2.4',h,'Laibach congress',H_)])),
('7.4',(2,[('4.3',h,'Greek independence',H_),('4.5',h,'1830 July Revolution',H_),('5.1',h,'the Zollverein',H_)])),
('7.5',(1,[])),('7.6',(1,[])),
('7.7',(1,[('3.1',h,'censorship and police rule',L_)])),
('7.8',(2,[('6.2',h,'1848 return of unrest',H_)])),
('8.0',(1,[])),('8.1',(1,[])),
('8.2',(1,[('4.2',h,'1821 and 1831 Italian risings',H_),('3.3',h,'German movements crushed 1819',H_)])),
('8.3',(2,[('2.6',h,'Congress System break-up',H_),('4.3',h,'Greek independence',H_),('4.6',h,'Belgian independence',H_)])),
('8.4',(1,[('1.1',h,'Austrian presidency of Diet',H_)])),
('8.5',(1,[('5.4',e,'Zollverein under Prussia',H_)])),
('8.6',(2,[('6.2',h,'1848 Vienna rising',H_)])),
]
run('hist-eur2-s10.t1g1.txt','hist-eur2-s10.t1g1.json',S10)
run('hist-eur1-s1.t1g1.txt','hist-eur1-s1.t1g1.json',S1)
