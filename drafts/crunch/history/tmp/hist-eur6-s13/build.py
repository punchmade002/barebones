import json,re
H='/Users/gabrielwhelan/barebones/drafts/crunch/history/'
def run(sub,pack,out,items):
    txt=open(H+'packs/'+pack).read()
    tgt=[]
    for l in txt.split('CANDIDATES')[0].splitlines():
        m=re.match(r'\[([^\]]+)\]',l)
        if m: tgt.append(m.group(1))
    allids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
    res={}
    for suf,cost,needs in items:
        i=sub+'.'+suf if not suf.startswith('hist') else suf
        res[i]={"cost":cost,"needs":[{"id":(n[0] if n[0].startswith('hist') else sub+'.'+n[0]),"strength":n[1],"why":n[2],"confidence":n[3]} for n in needs]}
    assert list(res)==tgt,(set(tgt)^set(res))
    for v in res.values():
        for n in v['needs']: assert n['id'] in allids,n
    json.dump(res,open(H+'point-links/'+out,'w'),indent=1)
    print(out,len(res),sum(len(v['needs']) for v in res.values()),sum(v['cost']==2 for v in res.values()),sum(n['confidence']=='low' for v in res.values() for n in v['needs']))
E,Hp,L='essential','helpful','low';Hi='high'
s='hist-eur6-s13'
it=[
('0.b',1,[]),
('0.0',1,[]),
('0.1',2,[]),
('0.2',1,[]),
('0.3',1,[]),
('0.4',1,[]),
('0.5',1,[]),
('0.6',2,[('hist-eur6-s2.0.1',Hp,'uses the Soviet atomic test',Hi),('0.0',Hp,'links to the thermonuclear bomb',Hi)]),
('0.7',2,[('0.1',Hp,'uses Soviet and US missiles',Hi),('0.4',Hp,'satellite pictures revealed the lead',Hi)]),
('0.8',2,[('0.1',E,'uses Minuteman missiles',Hi),('0.2',Hp,'uses Polaris submarines',Hi)]),
('0.9',2,[]),
('0.10',1,[('hist-eur6-s5.4.1',Hp,'uses the Strategic Defense Initiative',Hi)]),
('0.11',1,[]),
('1.b',1,[]),
('1.0',1,[]),
('1.1',1,[]),
('1.2',2,[]),
('1.3',1,[]),
('1.4',1,[('1.3',Hp,'responds to Gagarin',Hi)]),
('1.5',1,[('1.4',Hp,'serves the Moon landing goal',L)]),
('1.6',2,[('1.0',E,'uses Sputnik',Hi),('hist-eur6-s6.2.4',Hp,'uses National Defense Education Act',Hi),('1.1',Hp,'links to creation of NASA',Hi)]),
('1.7',1,[]),
('1.8',2,[('1.3',E,'uses Gagarin success',Hi),('hist-eur6-s2.4.3',E,'uses the Bay of Pigs',Hi),('1.4',Hp,'explains the Moon decision',Hi)]),
('1.9',1,[('2.3',Hp,'uses lunar and command modules',Hi)]),
('1.10',1,[]),
('2.b',1,[]),
('2.0',2,[]),
('2.1',1,[]),
('2.2',2,[]),
('2.3',1,[]),
('2.4',2,[]),
('2.5',2,[]),
('2.6',1,[]),
('2.7',1,[]),
('2.8',2,[('2.1',E,'describes the Saturn V',Hi)]),
('2.9',1,[('5.3',Hp,'uses integrated circuits',Hi)]),
('2.10',2,[('2.3',Hp,'uses command and lunar modules',Hi)]),
('2.11',1,[('2.0',Hp,'uses programme employment',L)]),
('2.12',1,[('2.2',Hp,'criticises the cost',Hi)]),
('3.b',1,[]),
('3.0',1,[]),
('3.1',1,[]),
('3.2',1,[('3.0',Hp,'uses Armstrong',Hi),('2.3',Hp,'uses the lunar module',Hi)]),
('3.3',1,[('3.0',E,'uses Armstrong and Aldrin',Hi),('3.2',Hp,'follows the landing',Hi)]),
('3.4',1,[]),
('3.5',1,[]),
('3.6',1,[]),
('3.7',1,[('3.2',E,'describes the landing of Eagle',Hi)]),
('3.8',1,[('3.3',E,'elaborates Armstrong first words',Hi)]),
('3.9',1,[]),
('3.10',1,[]),
('3.11',1,[('3.2',Hp,'contrasts with the Apollo landing',Hi)]),
('3.12',1,[('hist-eur6-s2.5.13',Hp,'uses protests against the war',L)]),
('4.b',1,[]),
('4.0',1,[('3.2',Hp,'follows Apollo 11 landing',Hi)]),
('4.1',1,[]),
('4.2',2,[]),
('4.3',1,[]),
('4.4',2,[]),
('4.5',1,[('2.6',E,'uses Apollo 13 explosion',Hi)]),
('4.6',1,[('4.0',Hp,'uses the later Apollo missions',Hi)]),
('4.7',1,[('3.2',Hp,'describes the landing',Hi)]),
('4.8',2,[('4.4',E,'uses the Challenger disaster',Hi)]),
('5.b',1,[]),
('5.0',1,[]),
('5.1',1,[]),
('5.2',1,[]),
('5.3',2,[('5.1',Hp,'builds on the transistor',Hi)]),
('5.4',1,[('5.3',Hp,'uses components on a chip',Hi)]),
('5.5',1,[('5.3',Hp,'builds on the integrated circuit',Hi)]),
('5.6',1,[]),
('5.7',2,[('5.5',Hp,'uses the microprocessor',L)]),
('5.8',1,[]),
('5.9',1,[('5.6',Hp,'uses the ARPANET',Hi),('1.0',Hp,'uses Sputnik',Hi)]),
('5.10',1,[('hist-eur6-s6.3.3',Hp,'defence contracts aided Silicon Valley',Hi)]),
('5.11',1,[('5.7',Hp,'uses the IBM PC',Hi)]),
('6.b',1,[]),
('6.0',1,[]),
('6.1',1,[]),
('6.2',1,[('6.1',Hp,'uses Telstar satellite',Hi)]),
('6.3',1,[]),
('7.b',1,[]),
('7.0',1,[('2.9',Hp,'uses computing advances',L)]),
('7.1',1,[('2.2',Hp,'uses the cost of Apollo',Hi)]),
('7.2',1,[('2.12',Hp,'uses criticism of cost',Hi)]),
('7.3',2,[('4.1',Hp,'uses lack of follow-up missions',Hi),('5.6',Hp,'uses computing technologies',L)]),
]
run(s,'hist-eur6-s13.t1g1.txt','hist-eur6-s13.t1g1.json',it)
