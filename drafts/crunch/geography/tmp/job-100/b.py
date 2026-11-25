import json,re
P='/Users/gabrielwhelan/barebones/drafts/crunch/geography/'
S='geo-region-continental-s1.'
H,L,E='high','low',None
# id: cost (explicit for every target)
cost={'87.2':1,'87.3':1,'87.4':1,'88.b':1,'88.0':1,'88.1':1,'88.2':1,'88.3':1,'89.b':1,'89.0':1,'89.1':1,'89.2':1,'89.3':1,
'90.b':1,'90.0':1,'90.1':1,'91.b':1,'91.0':2,'91.1':2,'92.b':1,'92.0':1,'92.1':2,'92.2':2,'92.3':1,'93.b':1,'93.0':1,'93.1':1,
'94.b':1,'94.0':1,'94.1':1,'95.b':1,'95.0':1,'95.1':1,'96.b':1,'96.0':1,'96.1':1,'96.2':2,'97.b':1,'97.0':1,'97.1':1,'97.2':1,'97.3':1,
'98.b':1,'98.0':1,'98.1':1,'98.2':1,'98.3':1,'99.b':1,'99.0':1,'99.1':1,'99.2':1,'100.b':1,'100.0':1,'100.1':1,'100.2':1,
'101.b':1,'101.0':1,'101.1':1,'101.2':1,'101.3':2,'101.4':1,'102.b':1,'102.0':1,'102.1':1,'102.2':1,'102.3':1,
'103.b':1,'103.0':1,'103.1':1,'103.2':1,'104.b':1,'104.0':1,'104.1':1,'104.2':1,
'105.b':1,'105.0':1,'105.1':1,'105.2':1,'105.3':2,'105.4':1,'105.5':1,'105.6':1,'105.7':1,
'106.b':1,'106.0':1,'106.1':1,'106.2':2,'106.3':1,'106.4':1,'106.5':1,'107.b':1,'107.0':1,'107.1':1,'107.2':1,'107.3':2,'107.4':1,'107.5':1,
'108.b':1,'108.0':1,'108.1':1,'108.2':1,'108.3':1,'109.b':1,'109.0':1,'109.1':1,'109.2':1,'109.3':1,
'110.b':1,'110.0':1,'110.1':1,'110.2':1,'111.b':1,'111.0':1,'111.1':1,'111.2':1,'111.3':1,'112.b':1,'112.0':1,'112.1':1,
'113.b':1,'113.0':1,'113.1':1,'113.2':1,'113.3':1,'113.4':1,'113.5':1,'114.b':1,'114.0':2,'114.1':2,'114.2':1,'114.3':1,'114.4':1,'114.5':1,'114.6':1,
'115.b':1,'115.0':2,'115.1':2,'115.2':1,'116.b':1,'116.0':2,'116.1':2,'116.2':2,'116.3':2,'117.b':1,'117.0':2,'117.1':2,'117.2':2,'117.3':1}
E_,H_='essential','helpful'
def n(i,s,w,c='high'): return {'id':(i if i.startswith('geo-') else S+i),'strength':s,'why':w,'confidence':c}
p1={'88.0':[n('88.b',H_,'density definition')],'88.1':[n('88.b',H_,'density definition')],'88.2':[n('88.b',H_,'density definition')],
'89.0':[n('89.b',E_,'definition of migration')],'89.1':[n('89.b',H_,'migration meaning')],'89.2':[n('89.b',H_,'migration meaning')],'89.3':[n('89.2',H_,'emigration to the Gulf')],
'90.0':[n('90.b',H_,'language as human process')],'90.1':[n('90.b',H_,'language as human process')],
'91.0':[n('91.b',E_,'language family')],'91.1':[n('91.b',E_,'language family')],
'92.1':[n('92.0',H_,'Hindi as main language')],'92.3':[n('92.2',H_,'official language of the Union')],
'93.0':[n('0.4',H_,'states of India')],'93.1':[n('93.0',H_,'states formed on language')],
'94.0':[n('92.2',H_,'Hindi as official language')],'94.1':[n('94.0',H_,'Hindi conflict compromise')],
'95.0':[n('90.b',H_,'many Indian languages')],'95.1':[n('68.0',H_,'English-speaking IT workforce'),n('95.0',H_,'English as link language')],
'98.1':[n('98.0',H_,'holy places of Indian religions')],'99.1':[n('99.0',E_,'1947 partition of British India')],
'99.2':[n('0.3',H_,'neighbours incl. Bangladesh')],'100.1':[n('100.0',H_,'secular state and tension','low')],
'100.2':[n('97.2',H_,'Muslim-majority Kashmir','low')],'101.1':[n('101.0',E_,'caste system')],'101.2':[n('101.1',H_,'untouchability')],
'101.3':[n('101.0',H_,'caste groups')],'101.4':[n('101.0',E_,'caste system')],
'102.0':[n('43.3',H_,'cow sacred to Hindus')],'102.2':[n('98.1',H_,'Varanasi holy city')],
'103.0':[n('103.b',H_,'urbanisation')],'103.2':[n('103.b',H_,'urbanisation')],'104.b':[n('103.1',H_,'urban agglomerations')],
'105.0':[n('1.3',H_,'Mumbai on west coast')],'105.1':[n('105.0',H_,'sheltered harbour site')],
'105.2':[n('58.1',H_,'cotton mills near raw material')],'105.7':[n('0.4',H_,'capital is New Delhi')],
'106.0':[n('111.0',H_,'meaning of slum')],'106.2':[n('8.1',H_,'heavy monsoon causes floods','low')],'106.5':[n('106.0',H_,'slum redevelopment')],
'107.0':[n('105.1',H_,'British East India Company','low')],'107.2':[n('27.7',H_,'Hooghly flows through Kolkata')],
'107.3':[n('99.0',E_,'1947 Partition'),n('107.2',H_,'jute industry')],
'108.0':[n('67.b',H_,'IT outsourcing centre')],'108.2':[n('7.2',H_,'altitude lowers temperature')],
'109.0':[n('107.1',H_,'British India capital','low')],'109.3':[n('46.1',E_,'stubble burning')],
'113.0':[n('44.0',H_,'small holdings')],'113.1':[n('8.0',H_,'late or weak monsoon')],'113.2':[n('114.3','helpful','x')][:0],
'113.4':[n('101.4',H_,'caste in rural life')],'113.5':[n('89.0',H_,'rural-to-urban migration')],
'114.1':[n('113.1',H_,'under-employment')],'114.3':[n('113.2',H_,'poor sanitation')],
'115.0':[n('89.3',H_,'remittances')],'115.2':[n('115.0',E_,'Kerala case'),n('115.1',E_,'Bihar case')],
'116.2':[n('116.1',H_,'poorer states named')],'116.3':[n('116.0',E_,'wealthy core'),n('116.1',E_,'poorer periphery')],
'117.0':[n('9.0',E_,'monsoon and farming calendar'),n('89.0',H_,'rural-to-urban migration'),n('111.0',H_,'urban slums')],
'117.1':[n('50.1',E_,'Chota Nagpur coal and iron'),n('54.3',H_,'Jamshedpur steel works')],
'117.2':[n('95.1',E_,'English and IT growth'),n('108.0',H_,'Bengaluru IT growth')],
'117.3':[n('102.0',E_,'sacred cattle dairying'),n('102.2',E_,'pilgrimage tourism')]}
p2={'87.2':[n('87.b',H_,'sparse areas explained')],'87.3':[n('87.b',H_,'sparse areas explained')],'87.4':[n('87.b',H_,'sparse-area physical factors')],
'88.b':[n('79.b',H_,'census as source')],'106.5':[n('77.3',H_,'metro systems')],'110.2':[n('77.3',H_,'metro systems')],
'113.3':[n('85.b',H_,'literacy by sex')],'114.2':[n('76.1',H_,'rural roads programme')],
'115.0':[n('85.1',H_,'Kerala highest literacy'),n('81.2',H_,'literacy and fertility')],'115.1':[n('85.1',H_,'Bihar lowest literacy'),n('81.1',H_,'Bihar fertility')]}
p3={'87.4':[n('geo-population-migration-s1.5.b',H_,'physical factors')],'88.b':[n('geo-population-migration-s1.4.1',H_,'density formula')],
'89.b':[n('geo-population-migration-s1.0.3',H_,'net migration','low')],'89.0':[n('geo-population-migration-s1.29.1',H_,'young adults migrate for jobs','low')],
'103.b':[n('geo-population-migration-s1.22.3',H_,'urbanisation meaning','low')],
'115.0':[n('geo-population-migration-s1.22.0',H_,'female education lowers fertility')],'115.1':[n('geo-population-migration-s1.32.1',H_,'low female status raises births')],
'116.3':[n('geo-population-migration-s1.9.b',H_,'core and periphery','low')]}
def fix(l): return [dict(x,id=x['id'].replace(S+'geo-',  'geo-')) for x in l]
def run(name,mode):
    txt=open(P+'packs/'+name+'.txt').read()
    ids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
    tgt=[S+k for k in cost]
    links={1:p1,2:p2,3:p3}[mode]
    out={}
    for k in cost:
        nd=[dict(x,id=x['id'].replace(S+'geo-','geo-')) for x in links.get(k,[])]
        out[S+k]={'cost':cost[k],'needs':nd} if mode==1 else {'needs':nd}
    assert list(out)==tgt
    for t in tgt: assert t in ids,t
    for k,v in out.items():
        for x in v['needs']: assert x['id'] in ids and x['id']!=k,(k,x['id'])
    json.dump(out,open(P+'point-links/'+name+'.json','w'),indent=1)
    nl=sum(len(v['needs']) for v in out.values())
    print(name,len(out),nl,sum(v.get('cost')==2 for v in out.values()),sum(x['confidence']=='low' for v in out.values() for x in v['needs']))
run('geo-region-continental-s1.t4g1',1);run('geo-region-continental-s1.t4g2',2);run('geo-region-continental-s1.t4g3',3)
