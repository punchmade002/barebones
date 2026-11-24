import json,re
P='hist-ire5-s7.'
H,E,h,l='helpful','essential','high','low'
def L(i,s,w,c=h): return {"id":i,"strength":s,"why":w,"confidence":c}
spec={
'0.b':(1,[]),
'0.0':(1,[L('hist-ire5-s4.2.0',H,'Provisional IRA origins')]),
'0.1':(1,[L('hist-ire5-s4.0.8',H,'uses the Ulster Defence Regiment')]),
'0.2':(1,[L('hist-ire5-s4.8.0',H,'Bloody Friday bombs')]),
'0.3':(2,[]),
'0.4':(1,[]),
'0.5':(2,[]),
'0.6':(1,[L('hist-ire5-s6.3.5',H,'Brighton bombing details')]),
'0.7':(1,[L('hist-ire5-s6.8.0',H,'Enniskillen bombing details')]),
'0.8':(1,[]),
'0.9':(2,[]),
'0.10':(2,[]),
'0.11':(2,[]),
'1.b':(1,[]),
'1.0':(1,[]),
'1.1':(2,[]),
'1.2':(1,[L('hist-ire5-s4.3.2',H,'uses the UDA'),L('hist-ire5-s4.3.0',H,'uses the UVF')]),
'1.3':(1,[L('hist-ire5-s4.8.4',H,'1972 deadliest year')]),
'1.4':(1,[]),
'1.5':(1,[L('hist-ire5-s7.3.1',H,'uses the UFF')]),
'1.6':(1,[L('hist-ire5-s7.3.0',H,'uses the UVF')]),
'1.7':(2,[L('hist-ire5-s7.3.4',H,'Greysteel loyalist response')]),
'1.8':(1,[]),
'2.0':(2,[L('hist-ire5-s7.2.5',H,"'shoot to kill' allegations")]),
'2.1':(1,[]),
'2.2':(1,[]),
'2.3':(1,[L('hist-ire5-s6.1.0',H,'special category and H-Block protests')]),
'2.4':(1,[L('hist-ire5-s4.5.5',H,'arrests increasing IRA recruitment',l)]),
'2.5':(2,[L('hist-ire5-s7.2.0',H,"'shoot to kill' controversy")]),
'2.6':(1,[]),
'3.b':(1,[]),
'3.0':(1,[]),
'3.1':(1,[]),
'3.2':(2,[L('hist-ire5-s7.3.0',H,'uses the UVF')]),
'3.3':(2,[L('hist-ire5-s7.3.0',H,'uses the UVF')]),
'3.4':(1,[L('hist-ire5-s7.1.7',H,'Shankill bomb a week earlier'),L('hist-ire5-s7.3.1',H,'uses the UFF')]),
'3.5':(1,[]),
'3.6':(1,[L('hist-ire5-s7.3.0',H,'uses the UVF'),L('hist-ire5-s7.3.1',H,'uses the UDA')]),
'4.b':(1,[]),
'4.0':(1,[L('hist-ire5-s7.3.0',H,'uses the UVF')]),
'4.1':(1,[]),
'4.2':(1,[]),
'4.3':(2,[L('hist-ire5-s7.4.1',H,'Lenny Murphy leader')]),
'5.b':(1,[]),
'5.0':(1,[L('hist-ire5-s6.1.1',H,'uses the hunger strikers')]),
'5.1':(1,[L('hist-ire5-s7.3.0',H,'uses the UVF',l)]),
'5.2':(1,[]),
'5.3':(2,[L('hist-ire5-s6.2.4',H,'same 1988 broadcast ban')]),
'5.4':(1,[L('hist-ire5-s7.5.3',H,'uses the broadcasting ban')]),
'5.5':(1,[]),
'5.6':(2,[L('hist-ire5-s7.5.3',H,'related British broadcasting ban',l)]),
'5.7':(1,[L('hist-ire5-s6.1.1',H,'hunger strikers as martyrs',l)]),
'6.b':(1,[]),
'6.0':(1,[L('hist-ire5-s4.0.b',H,'August 1969 violence')]),
'6.1':(1,[L('hist-ire5-s4.0.4',H,'refugees fleeing Belfast')]),
'6.2':(2,[L('hist-ire5-s7.6.0',H,'Jack Lynch as Taoiseach',l)]),
'6.3':(2,[L('hist-ire5-s7.6.2',E,'the Arms Crisis')]),
'6.4':(2,[L('hist-ire5-s4.6.1',E,'uses Bloody Sunday')]),
'7.0':(1,[]),
'7.1':(2,[L('hist-ire5-s7.7.0',H,'IRA membership offence')]),
'7.2':(1,[]),
'7.3':(2,[]),
'7.4':(1,[]),
'7.5':(1,[]),
'7.6':(2,[]),
'7.7':(1,[L('hist-ire5-s6.8.0',H,'Enniskillen bombing')]),
'8.0':(2,[L('hist-ire5-s6.7.0',H,'Anglo-Irish Agreement'),L('hist-ire5-s6.3.0',H,'New Ireland Forum')]),
'8.1':(1,[L('hist-ire5-s6.7.b',H,'Anglo-Irish Agreement')]),
'8.2':(1,[L('hist-ire5-s6.7.1',E,'the Intergovernmental Conference')]),
'8.3':(1,[L('hist-ire5-s6.7.1',H,'Anglo-Irish Agreement security role')]),
'8.4':(1,[]),
'8.5':(1,[L('hist-ire5-s6.7.b',H,'Anglo-Irish Agreement')]),
'9.0':(1,[]),'9.1':(1,[]),'9.2':(1,[]),'9.3':(1,[]),'9.4':(1,[]),'9.5':(1,[]),
'9.6':(2,[]),
}
d='/Users/gabrielwhelan/barebones/drafts/crunch/history/'
txt=open(d+'packs/hist-ire5-s7.t1g1.txt').read()
tgt=[];allid=set()
sec=None
for ln in txt.split('\n'):
    if ln.startswith('TARGET'):sec='t'
    elif ln.startswith('CANDIDATES'):sec='c'
    m=re.match(r'\[([^\]]+)\]',ln)
    if m:
        allid.add(m.group(1))
        if sec=='t':tgt.append(m.group(1))
out={}
for t in tgt:
    k=t[len(P):]
    c,n=spec[k]
    for x in n:
        assert x['id'] in allid and x['id']!=t,(t,x)
    out[t]={"cost":c,"needs":n}
assert len(out)==len(spec),(len(out),len(spec))
json.dump(out,open(d+'point-links/hist-ire5-s7.t1g1.json','w'),indent=0)
r=json.load(open(d+'point-links/hist-ire5-s7.t1g1.json'))
print(len(r),sum(len(v['needs']) for v in r.values()),sum(v['cost']==2 for v in r.values()),sum(x['confidence']=='low' for v in r.values() for x in v['needs']))
