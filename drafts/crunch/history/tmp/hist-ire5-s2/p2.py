import json,re
P='/Users/gabrielwhelan/barebones/drafts/crunch/history/'
def L(i,s,w):
    i='hist-ire5-s1.'+i[1:] if i[0]=='c' else 'hist-ire5-s2.'+i
    return {"id":i,"strength":s,"why":w,"confidence":"high"}
E,H='essential','helpful'
D={
'0.b':(1,[]),
'0.0':(1,[L('c1.1.0',H,'Brookeborough as predecessor')]),
'0.1':(2,[]),'0.2':(1,[]),'0.3':(2,[]),
'0.4':(1,[L('0.3',E,'the Lemass meeting')]),
'0.5':(1,[L('0.1',H,'Craigavon planning')]),
'0.6':(1,[L('c1.6.3',H,'Catholic discrimination grievances')]),
'0.7':(1,[L('c1.1.6',H,'Nationalist Party abstentionism')]),
'1.b':(1,[L('0.3',H,'the Lemass meeting')]),
'1.0':(1,[]),
'1.1':(1,[L('0.3',E,'the Lemass meeting')]),
'1.2':(2,[L('5.0',E,'the banned Derry march')]),
'1.3':(1,[]),
'1.4':(1,[L('1.0',H,'Paisley leading critic')]),
'1.5':(1,[]),
'1.6':(2,[L('1.0',H,'Paisley as critic')]),
'1.7':(2,[]),
'2.b':(1,[]),'2.0':(1,[]),'2.1':(1,[]),'2.2':(1,[]),
'2.3':(2,[L('4.b',H,'civil rights movement pressure')]),
'2.4':(2,[L('5.6',H,'the five-point package')]),
'2.5':(2,[L('6.8',H,'bomb attacks on installations')]),
'2.6':(1,[]),'2.7':(1,[]),
'2.8':(2,[]),
'3.b':(1,[]),'3.0':(2,[]),
'3.1':(1,[L('c1.3.2',H,'discrimination in housing allocation')]),
'3.2':(1,[L('3.0',E,'the Campaign for Social Justice')]),
'3.3':(1,[L('3.0',H,'the Campaign for Social Justice')]),
'3.4':(1,[L('3.0',H,'the Campaign for Social Justice')]),
'3.5':(1,[L('3.0',E,'the Campaign for Social Justice')]),
'4.b':(1,[]),'4.0':(1,[]),
'4.1':(2,[L('c1.0.6',H,'restricted local franchise'),L('c1.3.4',H,'gerrymandering'),L('c1.3.2',H,'housing points system')]),
'4.2':(1,[L('c1.1.3',E,'Special Powers Act'),L('c1.1.4',E,'the B Specials')]),
'4.3':(1,[]),'4.4':(1,[]),
'4.5':(1,[L('1.0',H,'Paisley and supporters')]),
'4.6':(1,[L('4.1',H,'one man, one vote demand')]),
'5.b':(1,[]),
'5.0':(1,[L('4.0',E,'NICRA organised march'),L('1.2',H,'Craig banned march')]),
'5.1':(1,[L('c1.1.5',H,'the RUC')]),
'5.2':(1,[L('5.1',E,'the violent police action')]),
'5.3':(1,[L('5.1',H,'the police violence')]),
'5.4':(1,[L('5.1',H,'the police action')]),
'5.5':(2,[L('5.1',H,'the Derry disturbances')]),
'5.6':(1,[L('c1.3.2',H,'housing points system')]),
'5.7':(1,[]),
'5.8':(1,[L('c1.3.3',H,'Londonderry Corporation')]),
'5.9':(2,[L('c1.1.3',E,'Special Powers Act'),L('c1.0.6',H,'company vote')]),
'5.10':(1,[L('4.1',H,'one man, one vote')]),
'6.b':(1,[]),
'6.0':(1,[L('5.0',H,'the Derry march')]),
'6.1':(1,[L('6.0',E,'People\'s Democracy')]),
'6.2':(2,[L('6.1',E,'the PD march'),L('c1.1.4',H,'the B Specials')]),
'6.3':(1,[L('6.2',E,'the Burntollet attack')]),
'6.4':(1,[L('6.2',H,'the Burntollet attack')]),
'6.5':(2,[L('1.0',H,'Paisley')]),
'6.6':(2,[L('7.2',H,'Devlin elected at by-election')]),
'6.7':(2,[L('2.5',H,'O\'Neill\'s resignation')]),
'6.8':(2,[L('c1.7.0',H,'IRA campaign')]),
'7.b':(1,[]),'7.0':(1,[]),
'7.1':(1,[L('6.0',E,'People\'s Democracy')]),
'7.2':(1,[L('6.6',H,'Mid Ulster by-election')]),
'7.3':(1,[L('6.1',E,'the march to Derry')]),
'7.4':(1,[]),'7.5':(1,[]),'7.6':(1,[]),'7.7':(1,[]),'7.8':(1,[]),'7.9':(1,[]),
'8.b':(1,[]),'8.0':(1,[]),'8.1':(1,[]),
'8.2':(1,[L('0.3',E,'the Lemass meeting')]),
'8.3':(1,[L('1.4',E,'the O\'Neill must go campaign')]),
'8.4':(1,[]),
'8.5':(1,[L('1.4',H,'campaign against O\'Neill')]),
'8.6':(1,[L('1.6',H,'1966 jailing')]),
'9.0':(2,[L('5.6',H,'housing points system'),L('5.7',H,'ombudsman'),L('5.10',H,'one man one vote timing')]),
'9.1':(1,[L('5.0',E,'the Derry march')]),
'9.2':(1,[L('3.5',H,'discrimination made public issue')]),
'9.3':(1,[L('2.5',H,'O\'Neill\'s resignation')]),
'9.4':(1,[]),'9.5':(1,[]),
'9.6':(2,[L('2.8',H,'historians on O\'Neill')]),
}
txt=open(P+'packs/hist-ire5-s2.t1g1.txt').read()
tg=re.findall(r'^\[(hist-ire5-s2\.[^\]]+)\]',txt.split('CANDIDATES')[0],re.M)
allids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
out={}
for t in tg:
    c,n=D[t[len('hist-ire5-s2.'):]]; out[t]={"cost":c,"needs":n}
assert len(out)==len(D)==len(tg),(len(out),len(D),len(tg))
for k,v in out.items():
    for n in v['needs']: assert n['id'] in allids and n['id']!=k,n
json.dump(out,open(P+'point-links/hist-ire5-s2.t1g1.json','w'),ensure_ascii=False)
o=json.load(open(P+'point-links/hist-ire5-s2.t1g1.json'))
ln=[n for v in o.values() for n in v['needs']]
print(len(o),len(ln),sum(v['cost']==2 for v in o.values()),sum(n['confidence']=='low' for n in ln))
