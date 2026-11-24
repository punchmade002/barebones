import json,re
P='hist-eur6-s7.'
def L(i,s,w,c='high'):
    if not i.startswith('hist-'): i=P+i
    return {"id":i,"strength":s,"why":w,"confidence":c}
E,H='essential','helpful'
d={
'0.b':(1,[L('hist-eur6-s3.5.b',H,'war and Great Society funding')]),
'0.0':(1,[L('hist-eur6-s3.5.0',H,'guns and butter policy')]),
'0.1':(1,[]),
'0.2':(1,[L('0.1',H,'inflation the surtax targeted')]),
'0.3':(1,[]),
'0.4':(1,[L('hist-eur6-s3.5.0',H,'paying for war and Great Society','low')]),
'0.5':(1,[L('0.1',H,'rising inflation in the 1960s')]),
'0.6':(2,[L('hist-eur6-s3.5.0',H,'Johnson delaying a tax request')]),
'0.7':(2,[L('hist-eur6-s6.1.1',E,'dollar convertible to gold')]),
'1.b':(1,[L('hist-eur6-s6.1.b',H,'postwar monetary order')]),
'1.0':(1,[L('hist-eur6-s6.1.1',E,'Bretton Woods dollar-gold link')]),
'1.1':(1,[L('1.0',E,'collapse of Bretton Woods')]),
'1.2':(1,[]),
'1.3':(1,[L('1.2',H,'first oil shock')]),
'1.4':(1,[]),
'1.5':(1,[L('1.0',H,'Nixon August 1971 measures')]),
'1.6':(1,[L('1.2',E,'the 1973 oil embargo')]),
'1.7':(1,[L('1.2',H,'oil shock causing recession')]),
'1.8':(2,[L('1.4',H,'inflation and stagflation','low')]),
'2.b':(1,[]),
'2.0':(1,[]),
'2.1':(1,[L('2.0',H,'steel industry decline')]),
'2.2':(1,[]),
'2.3':(1,[L('2.2',E,'Japanese car imports')]),
'2.4':(1,[]),
'2.5':(2,[L('2.4',H,'trade deficit and dollar')]),
'2.6':(2,[L('2.2',H,'Japanese car makers')]),
'2.7':(1,[L('1.2',H,'oil shocks raising fuel costs')]),
'2.8':(1,[L('2.1',H,'steel and factory job losses')]),
'2.9':(1,[]),
'3.b':(1,[]),
'3.0':(1,[L('1.4',H,'high inflation Volcker fought')]),
'3.1':(1,[]),
'3.2':(1,[L('3.1',E,'1981 tax cuts and deficit')]),
'3.3':(1,[]),
'3.4':(1,[L('3.0',H,'recession caused by Volcker')]),
'3.5':(1,[L('3.0',H,'inflation fall after Volcker')]),
'3.6':(1,[L('3.1',H,'tax cuts based on theory','low')]),
'3.7':(1,[L('3.1',H,'earlier tax rate cuts')]),
'3.8':(2,[L('3.3',H,'deregulation trend')]),
'3.9':(2,[L('4.0',H,'deficits Gramm-Rudman targeted','low')]),
'4.b':(1,[L('3.1',H,'Reagan tax cuts')]),
'4.0':(1,[L('3.1',H,'tax cuts causing deficits')]),
'4.1':(1,[L('4.0',H,'large deficits raising debt')]),
'4.2':(1,[L('4.1',H,'borrowing and national debt')]),
'4.3':(1,[]),
'4.4':(2,[L('4.0',H,'deficits being financed')]),
'4.5':(2,[L('2.5',E,'the Plaza Accord')]),
'5.b':(1,[]),
'5.0':(1,[L('1.2',E,'oil crisis and petrol')]),
'5.1':(1,[]),
'5.2':(1,[L('5.1',H,'Carter energy policy')]),
'5.3':(1,[L('1.2',H,'dependence on Middle East oil')]),
'5.4':(1,[L('5.3',H,'dependence on foreign oil')]),
'6.b':(1,[]),
'6.0':(1,[]),
'6.1':(2,[L('3.1',H,'tax cuts favouring high earners')]),
'6.2':(1,[L('hist-eur6-s6.6.0',H,'union strength in the boom')]),
'6.3':(1,[]),
'6.4':(1,[]),
'6.5':(1,[]),
'6.6':(1,[]),
'7.b':(1,[L('3.b',H,'Reagan recovery policy')]),
'7.0':(1,[L('3.5',H,'recovery and inflation fall')]),
'7.1':(1,[L('4.1',H,'rising national debt')]),
'7.2':(1,[L('1.4',H,'stagflation')]),
'7.3':(2,[L('2.b',H,'manufacturing decline')]),
'7.4':(1,[L('3.5',H,'1980s recovery')]),
'7.5':(2,[]),
}
out={}
for k,(c,n) in d.items():
    out[P+k]={"cost":c,"needs":n}
json.dump(out,open('/Users/gabrielwhelan/barebones/drafts/crunch/history/point-links/hist-eur6-s7.t1g1.json','w'),indent=1)
pk=open('/Users/gabrielwhelan/barebones/drafts/crunch/history/packs/hist-eur6-s7.t1g1.txt').read()
ids=set(re.findall(r'^\[([^\]]+)\]',pk,re.M))
tg=re.findall(r'^\[(hist-eur6-s7\.[^\]]+)\]',pk,re.M)
assert list(out)==tg,(set(tg)^set(out))
for v in out.values():
    for n in v['needs']: assert n['id'] in ids,n
a=[n for v in out.values() for n in v['needs']]
print(len(out),len(a),sum(v['cost']==2 for v in out.values()),sum(n['confidence']=='low' for n in a))
