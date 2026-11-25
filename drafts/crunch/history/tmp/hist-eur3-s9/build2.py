import json,re
P='hist-eur1-s7.'
H,L='high','low'
E,HP='essential','helpful'
def p(x):return P+x
d={
'0.b':(1,[]),'0.0':(1,[]),'0.1':(2,[]),'0.2':(1,[]),'0.3':(1,[]),
'0.4':(1,[('0.0',HP,'uses enclosure procedure',H)]),
'0.5':(1,[]),
'0.6':(1,[('0.0',E,'common rights lost through enclosure',H)]),
'0.7':(1,[]),
'1.0':(2,[]),'1.1':(2,[]),
'1.2':(1,[('1.1',HP,'Prussian reforms behind estates',L)]),
'1.3':(1,[]),
'1.4':(1,[('1.3',E,'uses mid-1840s poor harvests',H)]),
'1.5':(1,[('1.4',HP,'1840s crisis behind emigration',L)]),
'2.0':(1,[]),
'2.1':(1,[('2.0',HP,'steam power in industries',H)]),
'2.2':(2,[]),
'2.3':(1,[('2.2',HP,'cotton mills needing raw cotton',H)]),
'2.4':(1,[]),
'2.5':(2,[('2.1',HP,'steam power for locomotives',H)]),
'2.6':(1,[('2.1',HP,'steam locomotives',L)]),
'2.7':(1,[]),
'3.0':(1,[]),'3.1':(2,[]),
'3.2':(1,[('3.1',E,'French railway development',H)]),
'3.3':(2,[]),
'3.4':(1,[('3.3',HP,'German lands industrial growth',H)]),
'3.5':(1,[('3.3',HP,'Ruhr coalfield',H)]),
'3.6':(1,[]),
'4.0':(1,[]),
'4.1':(1,[('4.0',HP,'factory workforce',H)]),
'4.2':(1,[('4.1',HP,'child factory workers',H)]),
'4.3':(1,[]),
'4.4':(1,[('4.2',HP,'builds on earlier Factory Act',H)]),
'4.5':(1,[]),
'4.6':(2,[('4.1',HP,'child workers in textiles',L)]),
'5.b':(1,[]),'5.0':(1,[]),
'5.1':(1,[('0.4',HP,'uses the Corn Laws',H)]),
'5.2':(1,[('5.b',HP,'uses laissez-faire',H)]),
'5.3':(1,[('4.2',HP,'uses the Factory Acts',H)]),
'5.4':(1,[('5.b',HP,'contrasts with laissez-faire',L)]),
'5.5':(2,[('5.b',HP,'laissez-faire theory',L)]),
'6.0':(1,[]),'6.1':(1,[]),'6.2':(1,[]),'6.3':(1,[]),'6.4':(1,[]),'6.5':(1,[]),
'7.0':(1,[]),
'7.1':(1,[('7.0',HP,'uses disease in towns',H)]),
'7.2':(2,[('7.0',HP,'uses poor living conditions',H)]),
'7.3':(1,[('7.2',HP,'builds on Chadwick report',H)]),
'7.4':(1,[('7.1',HP,'uses cholera outbreaks',H)]),
'7.5':(1,[]),'7.6':(1,[]),
'7.7':(2,[('7.3',HP,'earlier Public Health Act',L)]),
'8.0':(1,[]),'8.1':(1,[]),'8.2':(1,[]),
'8.3':(1,[('8.2',HP,'uses voluntary schools and grants',H)]),
'8.4':(1,[]),
'9.0':(1,[]),
'9.1':(1,[('0.0',HP,'uses enclosure of common land',H)]),
'9.2':(1,[('7.3',HP,'uses public health reform',L)]),
'9.3':(1,[]),'9.4':(2,[]),
}
out={}
for k,(c,n) in d.items():
    out[p(k)]={"cost":c,"needs":[{"id":p(t),"strength":s,"why":w,"confidence":cf} for t,s,w,cf in n]}
txt=open('/Users/gabrielwhelan/barebones/drafts/crunch/history/packs/hist-eur1-s7.t1g1.txt').read()
tgt=re.findall(r'^\[([^\]]+)\]',txt,re.M)
assert list(out)==tgt,(set(tgt)^set(out))
for v in out.values():
    for n in v['needs']:assert n['id'] in tgt
json.dump(out,open('/Users/gabrielwhelan/barebones/drafts/crunch/history/point-links/hist-eur1-s7.t1g1.json','w'),indent=0)
chk=json.load(open('/Users/gabrielwhelan/barebones/drafts/crunch/history/point-links/hist-eur1-s7.t1g1.json'))
print(len(chk),sum(len(v['needs']) for v in chk.values()),sum(v['cost']==2 for v in chk.values()),sum(n['confidence']=='low' for v in chk.values() for n in v['needs']))
