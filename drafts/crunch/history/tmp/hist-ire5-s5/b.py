import json,re
P='/Users/gabrielwhelan/barebones/drafts/crunch/history/'
pk=open(P+'packs/hist-ire5-s5.t1g1.txt').read()
ids=set(re.findall(r'^\[([^\]]+)\]',pk,re.M))
tg=re.findall(r'^\[([^\]]+)\]',pk.split('CANDIDATES')[0],re.M)
E,H='essential','helpful'
def L(i,s,w,c='high'):
    i=i if i.startswith('hist-') else 'hist-ire5-s5.'+i
    return {"id":i,"strength":s,"why":w,"confidence":c}
D={
'0.b':(1,[]),'0.0':(1,[]),'0.1':(1,[L('0.0',E,'the border poll')]),
'0.2':(1,[L('0.0',E,'the boycotted border poll')]),'0.3':(2,[]),
'0.4':(1,[L('0.3',H,'the White Paper proposals')]),
'0.5':(1,[L('0.3',E,'the proposed Assembly'),L('hist-ire5-s4.7.5',H,'Stormont formally abolished')]),
'1.b':(1,[]),'1.0':(1,[L('0.3',H,'proportional representation Assembly')]),
'1.1':(2,[L('0.3',E,'the power-sharing plan'),L('hist-ire5-s4.3.5',H,'Craig and Vanguard')]),
'1.2':(1,[L('hist-ire5-s4.2.4',H,'SDLP and Fitt')]),
'1.3':(2,[L('hist-ire5-s4.2.4',H,'SDLP founders'),L('hist-ire5-s4.2.5',H,'Alliance Party')]),
'1.4':(1,[L('1.2',H,'the executive')]),
'1.5':(2,[L('1.0',E,'the Assembly election')]),
'2.b':(1,[]),'2.0':(1,[]),
'2.1':(1,[L('hist-ire5-s4.2.4',H,'the SDLP')]),
'2.2':(2,[L('0.4',E,'the Council of Ireland proposal')]),
'2.3':(2,[]),'2.4':(1,[]),
'2.5':(1,[L('1.0',H,'implementing through the Assembly','low')]),
'2.6':(1,[L('2.3',E,'declaration on status of Northern Ireland')]),
'2.7':(2,[L('2.6',E,'Articles 2 and 3 concern')]),
'3.0':(2,[L('2.2',E,'the Council of Ireland')]),
'3.1':(1,[L('3.0',E,'Faulkner losing the party vote')]),
'3.2':(1,[L('3.0',H,'Council of Ireland dispute')]),
'3.3':(1,[]),
'3.4':(2,[L('4.2',E,'the strikers')]),
'3.5':(1,[L('3.2',H,'delaying the Council of Ireland')]),
'4.b':(1,[]),'4.0':(1,[L('1.1',H,'anti-Sunningdale unionists')]),
'4.1':(1,[L('4.0',E,'the UUUC')]),
'4.2':(2,[]),
'4.3':(1,[L('4.2',E,'the strike'),L('3.3',H,'Rees as Secretary of State')]),
'4.4':(1,[L('4.2',E,'the strike')]),
'4.5':(1,[L('4.3',H,'the executive collapsing')]),
'4.6':(1,[L('4.2',E,'the strike')]),
'4.7':(1,[L('4.2',H,'the strike beginning')]),
'5.0':(1,[L('2.2',E,'the Council of Ireland')]),
'5.1':(1,[L('1.1',H,'split in unionism')]),
'5.2':(1,[L('4.2',E,'the UWC strike')]),
'5.3':(1,[L('4.3',E,'government response to strike')]),
'5.4':(1,[]),
'5.5':(1,[L('0.3',H,'power-sharing arrangements')]),
'5.6':(1,[L('4.2',H,'the strike')]),
'6.b':(2,[L('1.2',H,'Faulkner as Chief Executive')]),
'6.0':(1,[L('1.2',E,'Faulkner as Chief Executive')]),
'6.1':(1,[L('2.0',E,'the Sunningdale conference')]),
'6.2':(2,[L('2.2',E,'the Council of Ireland')]),
'6.3':(1,[L('4.2',E,'the strike')]),
'6.4':(2,[]),'6.5':(2,[]),'6.6':(1,[]),
'6.7':(1,[L('3.0',H,'Faulkner resigning leadership')]),
'7.b':(1,[]),'7.0':(1,[L('1.3',H,'Hume as minister')]),
'7.1':(1,[L('2.2',E,'the Council of Ireland')]),
'7.2':(1,[L('4.2',E,'the May 1974 strike')]),
'7.3':(1,[]),'7.4':(1,[]),'7.5':(1,[]),
'8.0':(1,[]),
'8.1':(1,[L('hist-ire5-s4.7.2',E,'Direct Rule')]),
'8.2':(1,[]),'8.3':(1,[]),
'9.0':(1,[]),'9.1':(1,[L('2.3',H,'consent principle')]),
'9.2':(1,[L('4.2',H,'the general strike')]),
'9.3':(1,[L('5.1',H,'unionist split and opposition')]),
'9.4':(1,[]),'9.5':(1,[L('4.0',H,'UUUC opposition')]),
'9.6':(2,[]),'9.7':(2,[]),
}
out={}
for t in tg:
    k=t.replace('hist-ire5-s5.','')
    c,n=D[k]; out[t]={"cost":c,"needs":n}
assert set(D)=={t.replace('hist-ire5-s5.','') for t in tg} and len(tg)==len(set(tg))
for v in out.values():
    for n in v['needs']: assert n['id'] in ids
json.dump(out,open(P+'point-links/hist-ire5-s5.t1g1.json','w'),indent=1)
r=json.load(open(P+'point-links/hist-ire5-s5.t1g1.json'))
print(len(r),sum(len(v['needs']) for v in r.values()),sum(v['cost']==2 for v in r.values()),sum(n['confidence']=='low' for v in r.values() for n in v['needs']))
