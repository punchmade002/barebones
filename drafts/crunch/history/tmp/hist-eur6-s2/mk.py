import json,re,sys
H,E='helpful','essential'
def run(pack,out,pre,D):
    txt=open(pack).read()
    tg=txt.split('CANDIDATES')[0]
    tids=re.findall(r'^\[([^\]]+)\]',tg,re.M)
    allids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
    assert list(D.keys())==[pre+k for k in D_keys(D,pre)] if False else True
    res={}
    for k,(c,ns) in D.items():
        i=pre+k
        res[i]={"cost":c,"needs":[{"id":(n[0] if n[0].startswith('hist-') else pre+n[0]),"strength":n[1],"why":n[2],"confidence":n[3]} for n in ns]}
    assert list(res)==tids,(set(tids)^set(res))
    for v in res.values():
        for n in v['needs']: assert n['id'] in allids,n
    json.dump(res,open(out,'w'),indent=1)
    L=sum(len(v['needs']) for v in res.values())
    print(len(res),L,sum(v['cost']==2 for v in res.values()),sum(n['confidence']=='low' for v in res.values() for n in v['needs']))
def D_keys(*a):pass

P='/Users/gabrielwhelan/barebones/drafts/crunch/history/'
D={
'0.b':(1,[]),'0.0':(1,[]),'0.1':(1,[]),'0.2':(1,[]),
'0.3':(1,[('0.2',H,'Kennan and containment','high')]),
'0.4':(1,[]),'0.5':(1,[]),'0.6':(1,[]),
'0.7':(1,[('3.2',H,'the Korean War beginning','high')]),
'1.b':(1,[]),'1.0':(1,[]),
'1.1':(1,[('1.0',E,'Marshall proposal behind the programme','high')]),
'1.2':(1,[('1.1',E,'uses Marshall aid','high')]),
'1.3':(1,[('1.1',E,'uses Marshall aid','high')]),
'1.4':(1,[]),
'1.5':(1,[('1.4',E,'uses the NATO treaty','high')]),
'1.6':(1,[]),
'2.b':(1,[('1.6',H,'the division of Germany','high')]),
'2.0':(1,[('1.6',H,'the divided Germany','high')]),
'2.1':(1,[('2.0',E,'uses the Berlin blockade','high')]),
'2.2':(1,[]),'2.3':(1,[]),
'2.4':(1,[('2.3',E,'uses the Berlin Wall','high')]),
'2.5':(1,[('2.3',H,'the Wall stopping refugees','high')]),
'2.6':(1,[('2.3',H,'the Berlin Wall','high')]),
'3.b':(1,[]),'3.0':(1,[]),
'3.1':(1,[('3.0',E,'the divided Korea','high')]),
'3.2':(1,[('3.0',E,'North and South Korea','high')]),
'3.3':(1,[('3.2',E,'the invasion of South Korea','high')]),
'3.4':(1,[('3.2',E,'the UN forces','high')]),
'3.5':(1,[('3.4',E,'the UN advance after Inchon','high')]),
'3.6':(1,[('3.4',E,'MacArthur leading UN forces','high'),('3.5',H,'Chinese entry into the war','high')]),
'3.7':(1,[('3.5',H,'the war ending near the 38th parallel','high')]),
'3.8':(1,[]),
'4.b':(1,[]),'4.0':(1,[]),
'4.1':(1,[]),
'4.2':(1,[('4.1',E,'Castro nationalising US property','high')]),
'4.3':(1,[('4.1',H,'Castro\'s government','high')]),
'4.4':(1,[('4.3',H,'the Bay of Pigs failure','high')]),
'4.5':(1,[('4.2',H,'Cuba turning to the Soviet Union','high')]),
'4.6':(1,[('4.5',E,'the Soviet missiles in Cuba','high')]),
'4.7':(1,[('4.5',E,'the missiles discovered','high')]),
'4.8':(1,[('4.7',E,'the quarantine line','high')]),
'4.9':(1,[('4.7',H,'the crisis and quarantine','high')]),
'4.10':(1,[('4.9',E,'the missile removal deal','high'),('4.6',H,'the Jupiter missiles','high')]),
'5.b':(1,[]),'5.0':(1,[]),
'5.1':(1,[('5.0',E,'the French war in Indochina','high')]),
'5.2':(1,[('5.0',H,'Vietnam and the French defeat','high')]),
'5.3':(1,[('5.0',E,'the Viet Minh and French defeat','high')]),
'5.4':(1,[('5.3',E,'the divided South Vietnam','high')]),
'5.5':(1,[('5.4',E,'the South Vietnamese state','high')]),
'5.6':(1,[('5.4',H,'the government in the South','high')]),
'5.7':(1,[('5.4',H,'Diem\'s government','high')]),
'5.8':(1,[('5.4',E,'Diem\'s government','high')]),
'5.9':(1,[('5.8',H,'protests against Diem','high')]),
'5.10':(1,[('5.5',H,'US military advisers','high')]),
'5.11':(1,[]),
'5.12':(1,[('5.11',H,'the Nixon Doctrine','high')]),
'5.13':(2,[]),
'5.14':(2,[('5.12',H,'Vietnamisation and troop withdrawal','high')]),
'5.15':(1,[('5.14',H,'the 1972 bombing and talks','low')]),
'6.0':(1,[]),
'6.1':(1,[('3.7',E,'the Korean armistice','high'),('6.0',H,'the nuclear threat strategy','high')]),
'6.2':(1,[('6.0',E,'massive retaliation','high')]),
'6.3':(1,[('4.9',E,'the missile crisis outcome','high')]),
'7.b':(1,[]),
'7.0':(1,[('0.1',H,'the atomic bombings','high')]),
'7.1':(1,[('0.4',E,'the Truman Doctrine','high')]),
'7.2':(1,[]),
'7.3':(1,[('3.3',E,'sending forces without Congress','high')]),
'7.4':(1,[('2.1',E,'the Berlin airlift','high'),('3.6',E,'MacArthur and limited war','high')]),
'7.5':(1,[]),
'7.6':(1,[('0.6',E,'Who lost China question','high')]),
'7.7':(2,[]),
'8.0':(2,[('1.1',H,'the Marshall Plan','high'),('1.4',H,'NATO','high'),('2.1',H,'the Berlin airlift','high')]),
'8.1':(1,[('3.7',H,'the Korean stalemate','high')]),
'8.2':(1,[('3.6',H,'Truman limiting the war','high')]),
'8.3':(2,[('4.3',H,'the Bay of Pigs','high'),('4.10',H,'the secret concession','high')]),
'8.4':(1,[('5.10',H,'advisers growing to troops','high')]),
'8.5':(2,[('5.2',H,'the domino theory','low')]),
'8.6':(2,[]),
}
run(P+'packs/hist-eur6-s2.t1g1.txt',P+'point-links/hist-eur6-s2.t1g1.json','hist-eur6-s2.',D)
