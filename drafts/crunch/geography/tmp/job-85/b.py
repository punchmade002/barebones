import json,re
P='/Users/gabrielwhelan/barebones/drafts/crunch/geography/'
N='geo-population-migration-s4.'
E,H='essential','helpful'
# id: (cost, [(target, strength, why, conf)])
D={
'0.b':(1,[]),
'0.0':(2,[('0.3',H,'refugee duties','high')]),
'0.1':(1,[]),'0.2':(1,[]),'0.3':(2,[]),
'0.4':(1,[('0.3',H,'contrasts with refugee status','high')]),
'0.5':(1,[('0.3',H,'refugee definition','high')]),
'0.6':(1,[]),
'1.b':(1,[]),'1.0':(1,[]),
'1.1':(1,[('0.3',H,'persecution grounds','high')]),'1.2':(1,[]),
'2.b':(1,[]),'2.0':(1,[]),'2.1':(1,[]),
'2.2':(1,[('s3.0.6',H,'chain migration','low')]),'2.3':(1,[]),
'3.b':(1,[]),'3.0':(1,[]),
'3.1':(1,[('3.0',E,'uses Common Travel Area','high'),('10.1',H,'Schengen defined','high')]),
'3.2':(1,[]),
'3.3':(1,[('s3.9.1',H,'2004 enlargement members','high')]),
'3.4':(1,[('3.3',H,'contrast with 2004 opening','high')]),
'3.5':(1,[('3.3',H,'open labour market','high')]),
'4.b':(1,[]),'4.0':(1,[]),
'4.1':(2,[]),
'4.2':(1,[('4.1',H,'compares with Critical Skills permit','high')]),
'4.3':(1,[('4.1',H,'permit hiring logic','low')]),
'4.4':(1,[('4.3',H,'labour-market test','high')]),
'5.b':(1,[]),'5.0':(1,[]),
'5.1':(2,[('5.0',H,'original asylum system','low')]),
'5.2':(1,[('5.1',H,'claims procedure','low')]),
'5.3':(1,[]),'5.4':(2,[]),
'6.b':(1,[]),'6.0':(1,[]),'6.1':(1,[]),'6.2':(2,[]),
'6.3':(1,[('6.2',H,'criticisms of direct provision','high')]),
'6.4':(2,[]),
'6.5':(2,[('6.0',H,'direct provision system','high')]),
'6.6':(1,[('5.3',H,'rising application numbers','low')]),
'7.b':(1,[]),'7.0':(1,[]),
'7.1':(1,[('7.0',H,'2004 amendment','high')]),
'7.2':(1,[]),
'8.b':(1,[]),
'8.0':(2,[('0.6',H,'UNHCR resettlement','high')]),
'8.1':(2,[('5.b',H,'asylum claim system','low')]),
'8.2':(1,[('5.b',E,'international protection system','high'),('8.1',H,'temporary protection','high')]),
'8.3':(1,[('8.1',H,'Ukrainian arrivals','high')]),
'8.4':(1,[('6.b',H,'direct provision accommodation','high'),('8.1',H,'Ukrainian arrivals','high')]),
'9.b':(1,[]),
'9.0':(1,[('0.1',H,'EU free movement','high')]),
'9.1':(1,[('6.b',E,'direct provision','high')]),
'9.2':(1,[]),
'9.3':(1,[]),
'10.b':(1,[]),
'10.0':(2,[('0.1',H,'free movement rights','high')]),
'10.1':(2,[]),
'10.2':(1,[('10.1',E,'Schengen area','high')]),
'10.3':(2,[('10.1',H,'Schengen membership','high')]),
'10.4':(1,[('10.1',E,'Schengen','high'),('3.1',H,'Common Travel Area reason','high')]),
'10.5':(1,[('10.1',E,'internal border checks','high')]),
'11.b':(1,[]),'11.0':(1,[]),'11.1':(2,[]),'11.2':(1,[]),
'11.3':(1,[('11.0',H,'first-entry rule','high')]),
'11.4':(1,[('11.0',H,'first-entry responsibility','high')]),
'11.5':(1,[('11.4',H,'frontier states','high'),('13.1',H,'2015 arrivals','high')]),
'12.b':(1,[]),'12.0':(1,[]),
'12.1':(1,[('12.0',H,'Frontex role','low')]),
'12.2':(1,[('0.1',H,'third-country nationals','low')]),
'12.3':(1,[('s3.17.1',H,'ageing offset by workers','low')]),
'13.b':(1,[]),'13.0':(1,[]),
'13.1':(1,[('13.0',H,'drivers of flows','low')]),
'13.2':(2,[]),
'13.3':(2,[]),
'13.4':(1,[('13.3',H,'route comparison','low')]),
'13.5':(2,[('13.4',H,'Lampedusa and route','high')]),
'13.6':(1,[]),
'13.7':(1,[('8.1',H,'Ukrainian temporary protection','high')]),
'14.b':(1,[]),'14.0':(1,[]),
'14.1':(1,[('11.4',H,'frontier states','high')]),
'14.2':(1,[('14.1',H,'relocation scheme','high')]),
'14.3':(1,[]),
'14.4':(2,[]),
'14.5':(2,[('14.4',H,'EU-Turkey deal','high')]),
'14.6':(1,[('12.0',H,'Frontex','high'),('10.5',H,'internal border checks','high')]),
'15.b':(1,[]),
'15.0':(1,[('8.1',H,'Temporary Protection Directive','high')]),
'15.1':(1,[('15.0',H,'temporary protection','high')]),
'15.2':(1,[]),
'15.3':(2,[('14.1',H,'relocation of asylum seekers','high')]),
'15.4':(1,[('15.2',E,'the Pact','high')]),
'16.b':(1,[]),'16.0':(1,[]),
'16.1':(1,[('5.b',H,'asylum claims system','low')]),
'16.2':(1,[]),
'16.3':(1,[('11.0',E,'Dublin rule','high')]),
'16.4':(1,[]),'16.5':(1,[]),
'16.6':(1,[('13.6',H,'deaths at sea','high')]),
'17.b':(1,[]),'17.0':(1,[]),
'17.1':(2,[('14.2',H,'relocation dispute','high')]),
'17.2':(1,[('12.3',H,'labour need','low')]),
}
txt=open(P+'packs/geo-population-migration-s4.t1g1.txt').read()
ids=[];allid=set()
sec=None
for l in txt.split('\n'):
    if l.startswith('TARGET'):sec='t'
    elif l.startswith('CANDIDATES'):sec='c'
    m=re.match(r'\[([^\]]+)\]',l)
    if m:
        allid.add(m.group(1))
        if sec=='t':ids.append(m.group(1))
out={}
for i in ids:
    k=i[len(N):]
    c,ns=D[k]
    out[i]={'cost':c,'needs':[{'id':(t if t.startswith('s3.') else N+t),'strength':s,'why':w,'confidence':cf} for t,s,w,cf in ns]}
    for n in out[i]['needs']:
        nid=n['id'] if not n['id'].startswith('s3.') else 'geo-population-migration-'+n['id']
        n['id']=nid
        assert nid in allid and nid!=i,(i,nid)
assert set(D)=={i[len(N):] for i in ids} and len(D)==len(ids)
json.dump(out,open(P+'point-links/geo-population-migration-s4.t1g1.json','w'),indent=1)
v=list(out.values())
print(len(v),sum(len(x['needs']) for x in v),sum(x['cost']==2 for x in v),sum(n['confidence']=='low' for x in v for n in x['needs']))
