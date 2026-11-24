import json,re
P='hist-ire6-s6.'
def L(i,s,w,c='high'): return {"id":i,"strength":s,"why":w,"confidence":c}
E,H='essential','helpful'
D={
'0.b':(1,[]),'0.0':(2,[]),'0.1':(1,[L(P+'0.0',E,'the Soviet veto of 1946')]),
'0.2':(2,[L(P+'0.1',H,'the 1955 package deal')]),'0.3':(1,[]),'0.4':(1,[]),
'1.b':(1,[]),'1.0':(1,[]),'1.1':(1,[]),'1.2':(1,[]),'1.3':(1,[]),
'1.4':(2,[]),'1.5':(1,[L(P+'1.4',E,'Resolution 1665 on nuclear weapons')]),'1.6':(2,[]),
'2.b':(1,[]),'2.0':(1,[]),'2.1':(1,[L(P+'2.0',E,'Irish troops in the Congo')]),
'2.2':(2,[L(P+'2.0',H,'Irish troops in the Congo')]),
'2.3':(1,[L(P+'2.0',E,'Irish troops in the Congo')]),'2.4':(1,[]),'2.5':(1,[]),
'2.6':(1,[L(P+'7.0',H,'policy of military neutrality')]),
'3.0':(1,[]),'3.1':(1,[L(P+'3.0',E,'Boland as UN representative')]),
'3.2':(1,[L(P+'3.1',E,'fifteenth session presidency'),L(P+'2.0',H,'the Congo crisis')]),
'3.3':(1,[L(P+'3.1',E,'Boland elected President')]),'3.4':(1,[]),
'4.b':(1,[]),'4.0':(2,[]),
'4.1':(1,[L(P+'4.0',E,'the EEC and its market'),L('hist-ire6-s5.2.0',H,'Britain as main export market')]),
'4.2':(1,[L(P+'4.0',E,'the EEC')]),
'4.3':(1,[L('hist-ire6-s2.6.b',H,'Lemass: compete in open markets')]),
'4.4':(1,[L(P+'4.1',E,'British application to join')]),
'4.5':(1,[L('hist-ire6-s2.6.2',E,'the Anglo-Irish Free Trade Agreement')]),
'5.0':(1,[L(P+'4.4',E,'de Gaulle\'s first veto')]),
'5.1':(1,[L(P+'5.0',E,'the 1967 veto and applications')]),
'5.2':(2,[L(P+'5.1',H,'the negotiations opened in 1970')]),
'5.3':(1,[L(P+'5.2',E,'the negotiated terms')]),
'5.4':(2,[L(P+'5.3',H,'the Treaty of Accession')]),
'5.5':(1,[]),
'5.6':(1,[L(P+'5.0',H,'applications of Britain, Denmark, Norway')]),
'5.7':(1,[L(P+'5.2',E,'Hillery led the negotiations')]),
'6.0':(2,[L(P+'4.0',H,'the European Economic Community')]),
'6.1':(1,[L(P+'6.0',E,'the Single European Act')]),
'6.2':(1,[L(P+'6.0',E,'the Single European Act')]),
'6.3':(2,[L(P+'6.2',E,'Crotty\'s challenge'),L(P+'6.1',E,'political cooperation provisions')]),
'6.4':(1,[L(P+'6.3',E,'Supreme Court ruling needing amendment')]),
'6.5':(1,[L(P+'6.3',E,'the Crotty judgment')]),
'7.0':(1,[]),
'7.1':(1,[L(P+'2.0',H,'the Congo mission')]),
'7.2':(1,[L(P+'7.1',H,'the 1960 Defence Act')]),
'7.3':(1,[]),
'7.4':(1,[L(P+'5.5',H,'opposition arguments in 1972')]),
'8.0':(1,[L('hist-ire6-s2.0.b',H,'failure of protection')]),
'8.1':(1,[L('hist-ire6-s5.2.0',H,'dependence on the British market')]),
'8.2':(1,[]),
'8.3':(2,[L(P+'5.5',H,'1972 opposition to entry')]),
'8.4':(1,[L(P+'5.5',H,'who opposed and supported entry')]),
'8.5':(1,[L(P+'6.2',H,'Crotty and the Single European Act')]),
'8.6':(1,[L(P+'5.4',E,'the 1972 referendum result')]),
'9.0':(1,[]),'9.1':(2,[L(P+'8.2',H,'Common Agricultural Policy prices')]),
'9.2':(2,[]),'9.3':(2,[]),
}
txt=open('/Users/gabrielwhelan/barebones/drafts/crunch/history/packs/hist-ire6-s6.t1g1.txt').read()
tids=re.findall(r'^\[(hist-ire6-s6\.[^\]]+)\]',txt.split('CANDIDATES')[0],re.M)
allids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
assert set(P+k for k in D)==set(tids) and len(tids)==len(D)
out={}
for t in tids:
    c,n=D[t[len(P):]]; out[t]={"cost":c,"needs":n}
    for x in n: assert x['id'] in allids and x['id']!=t,(t,x)
json.dump(out,open('/Users/gabrielwhelan/barebones/drafts/crunch/history/point-links/hist-ire6-s6.t1g1.json','w'),ensure_ascii=False,indent=1)
print(len(out),sum(len(v['needs']) for v in out.values()),sum(v['cost']==2 for v in out.values()),sum(x['confidence']=='low' for v in out.values() for x in v['needs']))
