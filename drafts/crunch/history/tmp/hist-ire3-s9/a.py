import json,re
P='hist-ire3-s9.'
E,H='essential','helpful'
def n(i,s,w,c='high'):return {"id":i if i.startswith('hist') else P+i,"strength":s,"why":w,"confidence":c}
d={
'0.b':(1,[n('hist-ire3-s8.0.b',H,'Irish neutrality in the South')]),
'0.0':(1,[n('hist-ire3-s8.0.b',H,'the South\'s neutrality')]),
'0.1':(1,[]),'0.2':(2,[]),'0.3':(1,[]),
'0.4':(1,[n('hist-ire3-s3.7.3',H,'Craig as Prime Minister')]),
'0.5':(2,[n('0.4',E,'Andrews succeeded Craig'),n('4.3',H,'criticism over the Blitz')]),
'0.6':(1,[n('0.5',H,'Brooke succeeded Andrews')]),
'1.b':(1,[n('hist-ire3-s3.5.1',H,'mass unemployment of the 1920s-30s')]),
'1.0':(1,[n('hist-ire3-s3.5.0',H,'Harland and Wolff shipbuilding')]),
'1.1':(1,[]),'1.2':(1,[]),'1.3':(1,[]),'1.4':(1,[]),'1.5':(1,[]),'1.6':(1,[]),'1.7':(1,[]),
'2.b':(1,[]),
'2.0':(1,[n('1.0',H,'the shipyard and industry')]),
'2.1':(1,[]),'2.2':(1,[]),'2.3':(1,[]),'2.4':(1,[]),
'2.5':(1,[n('hist-ire3-s3.5.4',H,'Belfast slum housing')]),
'3.b':(2,[n('2.b',H,'weak civil defence')]),
'3.0':(1,[]),'3.1':(1,[]),
'3.2':(1,[n('3.1',E,'the Easter Tuesday raid')]),
'3.3':(1,[]),
'3.4':(1,[n('3.1',H,'the raids')]),
'3.5':(1,[n('3.1',H,'the raids')]),
'3.6':(2,[n('3.1',E,'the 15-16 April raid'),n('hist-ire3-s8.5.7',H,'fire brigades went north',)]),
'3.7':(1,[n('3.1',H,'the raids')]),
'3.8':(1,[n('3.1',H,'the raids')]),
'4.b':(1,[]),
'4.0':(1,[n('3.5',H,'people evacuated after raids')]),
'4.1':(1,[n('4.0',E,'the evacuees')]),
'4.2':(1,[n('4.1',H,'condition of evacuees')]),
'4.3':(1,[n('0.5',E,'Andrews resigned 1943'),n('3.b',H,'the Blitz')]),
'4.4':(1,[n('4.0',H,'evacuation')]),
'4.5':(1,[n('4.0',H,'evacuation of refugees')]),
'5.b':(1,[]),'5.0':(1,[]),
'5.1':(1,[n('5.0',H,'American troops arrival')]),
'5.2':(1,[]),'5.3':(1,[]),'5.4':(1,[]),
'6.b':(1,[]),
'6.0':(1,[n('hist-ire3-s3.5.3',H,'step by step parity policy')]),
'6.1':(1,[n('3.b',H,'the Blitz destroyed housing')]),
'6.2':(1,[n('4.3',H,'discontent with Unionist government','low')]),
'6.3':(1,[n('hist-ire3-s3.3.5',H,'Unionist hold on Stormont')]),
'6.4':(1,[n('6.0',H,'wartime reform climate')]),
'6.5':(1,[n('hist-ire3-s3.3.2',H,'electoral system rules'),n('hist-ire3-s3.2.4',H,'the RUC and policing','low')]),
'7.b':(1,[]),
'7.0':(1,[n('1.b',H,'war contracts and full employment')]),
'7.1':(1,[n('3.b',H,'the Blitz damage')]),
'7.2':(1,[n('1.0',H,'shipbuilding wartime orders')]),
'7.3':(1,[n('4.3',H,'civil defence failures')]),
'7.4':(1,[n('6.0',H,'welfare reform promise')]),
'7.5':(1,[n('hist-ire3-s3.1.4',H,'the border and partition','low')]),
'8.b':(1,[]),
'8.0':(1,[n('1.b',H,'war production and employment')]),
'8.1':(1,[n('6.0',H,'welfare state participation')]),
'8.2':(1,[n('3.b',H,'the Blitz exposed poor preparation')]),
'8.3':(1,[n('hist-ire3-s3.3.5',H,'Unionist control of Stormont')]),
'8.4':(1,[n('0.0',H,'unionist loyalty argument')]),
'8.5':(2,[]),
}
f='/Users/gabrielwhelan/barebones/drafts/crunch/history/'
src=open(f+'packs/hist-ire3-s9.t1g1.txt').read()
tgt=re.findall(r'^\[(hist-ire3-s9\.[^\]]+)\]',src,re.M)
ids=set(re.findall(r'^\[([^\]]+)\]',src,re.M))
out={}
for t in tgt:
    c,nd=d[t[len(P):]]
    for x in nd:
        assert x['id'] in ids and x['id']!=t,(t,x)
    out[t]={"cost":c,"needs":nd}
assert len(out)==len(d)==len(tgt),(len(out),len(d),len(tgt))
json.dump(out,open(f+'point-links/hist-ire3-s9.t1g1.json','w'),ensure_ascii=False,indent=0)
print(len(out),sum(len(v['needs']) for v in out.values()),sum(v['cost']==2 for v in out.values()),sum(x['confidence']=='low' for v in out.values() for x in v['needs']))
