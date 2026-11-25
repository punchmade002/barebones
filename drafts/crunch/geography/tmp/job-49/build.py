import json,re
P='geo-option-culture-identity-s1.'
# id suffix -> (cost, links) ; links: (target, strength, why, conf)
H,L='high','low'
E,Hl='essential','helpful'
S1=P
def l(t,s,w,c): return (t,s,w,c)
spec={
'0.b':(1,[]),'0.0':(1,[]),'0.1':(1,[]),'0.2':(1,[]),
'1.b':(1,[]),'1.0':(1,[]),'1.1':(1,[l(P+'1.0',Hl,'builds on the same-group genetic point',L)]),
'1.2':(2,[]),'1.3':(1,[l(P+'1.1',Hl,'groupings not real divisions',H)]),'1.4':(2,[]),
'2.b':(1,[]),'2.0':(1,[]),'2.1':(1,[]),'2.2':(1,[]),'2.3':(1,[]),'2.4':(1,[]),
'3.b':(1,[]),'3.0':(1,[]),'3.1':(2,[l(P+'3.0',Hl,'adaptation to environment',H)]),'3.2':(1,[l(P+'3.0',Hl,'adaptation to environment',H)]),
'4.b':(1,[]),'4.0':(1,[l(P+'2.0',E,'Caucasoid grouping',H)]),'4.1':(1,[l(P+'2.1',E,'Mongoloid grouping',H)]),
'4.2':(1,[l(P+'2.2',E,'Negroid grouping',H)]),'4.3':(1,[l(P+'2.3',E,'Australoid grouping',H)]),
'5.b':(1,[]),'5.0':(1,[]),'5.1':(2,[]),'5.2':(1,[]),'5.3':(1,[]),'5.4':(1,[]),'5.5':(1,[l(P+'5.2',Hl,'slave trade scale',H)]),
'6.b':(1,[]),'6.0':(1,[]),'6.1':(2,[]),'6.2':(1,[]),'6.3':(1,[]),'6.4':(1,[l(P+'6.2',Hl,'Stolen Generations apologised for',H)]),
'6.5':(2,[]),'6.6':(1,[l(P+'6.3',Hl,'earlier referendum on Aboriginal rights',L)]),'6.7':(1,[]),
'7.b':(1,[]),'7.0':(1,[]),'7.1':(1,[l(P+'7.0',Hl,'removals created reservations',H)]),
'8.b':(1,[]),'8.0':(2,[]),'8.1':(1,[l(P+'8.0',E,'indentured labour destinations',H)]),'8.2':(1,[l(P+'8.0',E,'indentured labour movement',H)]),
'9.b':(1,[]),'9.0':(1,[]),'9.1':(1,[l(P+'9.0',Hl,'Belgian rule of Rwanda',H)]),'9.2':(1,[l(P+'30.0',Hl,'genocide described later',H)]),
'10.b':(1,[]),'10.0':(1,[]),'10.1':(1,[l(P+'10.0',Hl,'post-war colonial migration to Britain',H)]),'10.2':(1,[]),'10.3':(1,[]),'10.4':(1,[l(P+'10.0',Hl,'colonial migration to mother country',H)]),
'11.b':(1,[]),'11.0':(1,[]),'11.1':(1,[l(P+'11.0',E,'the South-to-North movement',H)]),'11.2':(1,[l(P+'11.0',Hl,'the South-to-North movement',H)]),
'12.b':(1,[]),'12.0':(1,[]),'12.1':(2,[l(P+'12.0',Hl,'Turkish recruitment agreement',L)]),'12.2':(1,[]),'12.3':(1,[]),
'13.b':(1,[]),'13.0':(2,[]),'13.1':(1,[l(P+'13.0',E,'refugee definition',H)]),'13.2':(1,[l(P+'13.0',E,'refugee status',H)]),'13.3':(1,[]),'13.4':(1,[]),'13.5':(1,[l(P+'13.0',Hl,'forcibly displaced people',L)]),
'14.b':(1,[l(P+'13.0',Hl,'refugee meaning',H)]),'14.0':(1,[l(P+'13.0',Hl,'refugee meaning',H)]),'14.1':(1,[l(P+'14.0',E,'Syrian refugee numbers',H)]),
'14.2':(1,[]),'14.3':(1,[l(P+'13.2',Hl,'asylum seeker meaning',H)]),'14.4':(1,[l(P+'14.0',Hl,'Syrian war context',H)]),
'15.b':(1,[]),'15.0':(1,[]),'15.1':(1,[l(P+'15.0',E,'Rohingya statelessness',H)]),
'16.b':(1,[]),'16.0':(1,[]),'16.1':(1,[l(P+'16.0',Hl,'Census 2022 figures',L)]),'16.2':(1,[l(P+'0.1',Hl,'ethnic group meaning',H)]),
'16.3':(1,[]),'16.4':(1,[l(P+'0.1',Hl,'ethnic minority meaning',L)]),'16.5':(1,[]),'16.6':(2,[l(P+'13.0',Hl,'refugee protection',L)]),
'17.b':(1,[]),'17.0':(1,[l(P+'13.2',E,'asylum seeker meaning',H)]),'17.1':(1,[l(P+'17.0',E,'Direct Provision asylum system',H)]),
'17.2':(1,[l(P+'13.2',Hl,'asylum seeker meaning',H)]),'17.3':(1,[]),
'18.b':(1,[]),'18.0':(1,[]),'18.1':(1,[]),'18.2':(1,[]),'18.3':(1,[l(P+'25.1',Hl,'segregation as a cause',L)]),
'19.b':(1,[]),'19.0':(1,[l('geo-population-migration-s3.4.0',Hl,'migration is age-selective',H)]),'19.1':(1,[]),
'20.b':(1,[]),'20.0':(1,[]),'20.1':(1,[]),
'21.b':(1,[]),'21.0':(2,[]),'21.1':(1,[l(P+'21.0',Hl,'census percentages',H)]),'21.2':(1,[]),'21.3':(1,[l(P+'21.2',Hl,'contrast with melting pot',H)]),
'22.b':(1,[]),'22.0':(1,[]),'22.1':(1,[l(P+'22.0',Hl,'later immigrants to Brazil',H)]),'22.2':(2,[]),'22.3':(1,[l(P+'22.2',E,'pardo census figures',H)]),
'22.4':(1,[l(P+'22.0',Hl,'Brazil mixed population',L)]),
'23.b':(1,[]),'23.0':(1,[]),'23.1':(1,[l(P+'10.1',Hl,'Windrush generation',H)]),
'24.b':(1,[]),'24.0':(1,[]),'24.1':(2,[]),'24.2':(1,[l(P+'24.0',E,'multiculturalism policy',H)]),'24.3':(1,[l(P+'24.0',E,'multiculturalism policy',H)]),
'25.b':(1,[]),'25.0':(1,[]),'25.1':(1,[]),'25.2':(1,[]),'25.3':(1,[]),
'26.b':(1,[]),'26.0':(1,[]),'26.1':(1,[l(P+'26.0',Hl,'apartheid system',H)]),'26.2':(1,[l(P+'26.0',Hl,'apartheid system',H)]),
'26.3':(1,[l(P+'26.0',Hl,'apartheid system',H)]),'26.4':(1,[l(P+'26.2',Hl,'Group Areas Act removals',H)]),
'27.b':(1,[]),'27.0':(1,[]),'27.1':(1,[]),'27.2':(2,[]),'27.3':(1,[]),'27.4':(1,[l(P+'26.1',Hl,'racial categories',H)]),'27.5':(1,[l(P+'26.2',Hl,'land segregation legacy',L)]),
'28.b':(1,[]),'28.0':(1,[]),'28.1':(1,[l(P+'28.0',Hl,'Jim Crow segregation',H)]),'28.2':(1,[]),'28.3':(1,[l(P+'28.0',Hl,'Jim Crow laws',L)]),'28.4':(1,[]),'28.5':(1,[]),
'29.b':(1,[]),'29.0':(1,[]),'29.1':(1,[l(P+'29.0',E,'Nuremberg Laws',H)]),'29.2':(1,[l(P+'29.1',Hl,'genocide step',L)]),
'30.b':(1,[l(P+'9.1',E,'Belgian identity cards',H)]),'30.0':(1,[l(P+'9.1',Hl,'Hutu and Tutsi labels',H)]),
'31.b':(1,[]),'31.0':(1,[]),'31.1':(1,[]),'31.2':(2,[]),'31.3':(1,[l(P+'31.2',Hl,'banlieue riots precedent',H)]),
}
# package 2 links (to geo-economic-development-s3): id -> list
D='geo-economic-development-s3.'
spec2={'8.0':[(D+'0.6',Hl,'plantations used forced labour',L)],
'9.1':[(D+'1.5',Hl,'colonial divide and rule',L)],
'25.2':[(D+'1.6',Hl,'colonial racial hierarchies and power',L)],
'22.4':[(D+'14.2',Hl,'racial inequality legacy of slavery',L)],
'22.0':[(D+'14.0',Hl,'enslaved Africans in Brazil',L)]}
root='/Users/gabrielwhelan/barebones/drafts/crunch/geography/'

import json,re
def ids(pack):
    txt=open(root+'packs/'+pack).read()
    t=[];allids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
    for ln in txt.split('\n'):
        if ln.startswith('CANDIDATES'):break
        m=re.match(r'\[(geo-option-culture-identity-s1\.[\d.b]+)\]',ln)
        if m:t.append(m.group(1))
    return t,allids
def lk(x): return [{"id":a,"strength":b,"why":c,"confidence":d} for a,b,c,d in x]
t,a=ids('geo-option-culture-identity-s1.t1g1.txt')
keys={i[len(P):] for i in t}
assert keys==set(spec),(keys^set(spec))
r={i:{"cost":spec[i[len(P):]][0],"needs":lk(spec[i[len(P):]][1])} for i in t}
for v in r.values():
    for n in v['needs']: assert n['id'] in a,n
json.dump(r,open(root+'point-links/geo-option-culture-identity-s1.t1g1.json','w'),indent=1)
print(len(r),sum(len(v['needs']) for v in r.values()),sum(v['cost']==2 for v in r.values()),sum(n['confidence']=='low' for v in r.values() for n in v['needs']))
t2,a2=ids('geo-option-culture-identity-s1.t1g2.txt')
assert t2==t
r2={i:{"needs":lk(spec2.get(i[len(P):],[]))} for i in t2}
for v in r2.values():
    for n in v['needs']: assert n['id'] in a2,n
json.dump(r2,open(root+'point-links/geo-option-culture-identity-s1.t1g2.json','w'),indent=1)
print(len(r2),sum(len(v['needs']) for v in r2.values()),sum(n['confidence']=='low' for v in r2.values() for n in v['needs']))
