import json,re
P='bio22-s6.'
# id -> (cost, [(need, strength, why, conf)])
E,H='essential','helpful'
d={
'0.0':(1,[]),'0.1':(1,[('s6.0.0',H,'emerging disease idea','low')]),'0.2':(1,[]),
'0.3':(1,[('s6.0.2',H,'expected level (endemic)','high')]),
'0.4':(1,[('s6.0.3',E,'epidemic definition','high')]),
'1.0':(1,[]),'1.1':(1,[('s6.1.0',E,'zoonosis definition','high')]),
'1.2':(1,[]),'1.3':(1,[]),
'2.6':(1,[('s1.1.1',H,'vector definition','high')]),
'3.3':(1,[('s6.3.2',E,'that epidemic','high')]),
'4.4':(1,[('s6.2.6',H,'vectors spreading disease','high')]),
'5.0':(1,[('s1.8.3',H,'chytrid fungus identity','high')]),
'5.1':(1,[('s6.5.0',H,'chytrid spread','high')]),
'6.1':(1,[('s6.1.3',H,'carriers','high'),('s6.1.2',H,'reservoir hosts','high')]),
'6.3':(1,[('s4.3.5',H,'latent virus in nerve cells','low')]),
'7.0':(1,[('s6.1.3',E,'carrier without symptoms','high')]),
'7.1':(1,[('s6.1.3',H,'carriers unidentifiable','high')]),
'7.2':(1,[('s6.1.2',E,'reservoir host','high')]),
'8.0':(1,[('s6.8.b',H,'mutation','high')]),
'8.1':(1,[('s4.5.6',E,'RNA polymerase lacks proofreading','high')]),
'8.2':(2,[('s6.8.b',H,'mutation changes antigens','low')]),
'8.3':(1,[('s6.8.2',E,'antigenic drift','high')]),
'8.4':(1,[('s6.8.2',H,'mutations alter antigens','low')]),
'9.0':(2,[('s6.8.2',H,'surface antigens, drift contrast','high')]),
'9.1':(1,[('s6.9.0',E,'antigenic shift','high')]),
'9.2':(1,[('s6.8.b',H,'mutation','high')]),
'9.3':(1,[('s1.8.2',H,'cereal rusts','low')]),
'10.0':(1,[('s6.8.b',H,'random mutation','high')]),
'10.1':(1,[]),'10.2':(1,[]),'10.3':(1,[]),
'11.0':(1,[('s6.10.b',H,'resistance by selection','high')]),
'11.1':(1,[]),
'11.2':(1,[('s1.5.3',H,'antibiotic-resistant bacteria','high')]),
'11.3':(1,[]),'11.4':(1,[]),
'11.5':(1,[('s6.6.b',H,'persistence factor','low')]),
'12.0':(2,[]),
'12.1':(1,[('s6.12.0',H,'susceptible hosts','high')]),
'12.2':(1,[('s6.12.1',H,'new pathogen, no immunity','high')]),
'12.3':(1,[('s6.12.0',H,'herd immunity','high')]),
'12.4':(1,[]),
'13.0':(1,[('s6.12.0',H,'immune proportion idea','low')]),
'13.1':(1,[('s6.13.0',H,'monoculture','high')]),
'13.2':(1,[('s6.13.1',E,'Lumper potato background','high')]),
'14.0':(1,[('s6.3.b',H,'local/regional spread routes','low')]),
'14.1':(1,[]),
'14.2':(1,[('s6.4.5',H,'migrating birds','low')]),
'14.3':(1,[('s6.2.6',H,'vectors','high')]),
'14.4':(1,[('s6.14.3',H,'vector range expansion','low')]),
'14.5':(1,[('s6.3.3',H,'movement ban example','low')]),
'15.0':(2,[('s6.12.b',H,'susceptible hosts','high')]),
'15.1':(1,[('s6.15.0',E,'R0 definition','high')]),
'15.2':(1,[('s6.15.0',E,'R0 definition','high'),('s6.0.2',H,'endemic meaning','high')]),
'15.3':(1,[('s6.15.0',E,'R0 definition','high')]),
'16.0':(2,[('s6.15.0',E,'R0 secondary infections','high')]),
'16.1':(1,[('s6.15.3',E,'R0 below 1','high')]),
'16.2':(1,[('s6.16.0',H,'branching growth example','high')]),
'17.0':(1,[('s6.6.b',H,'persistence','high')]),
'17.1':(1,[('s6.14.0',H,'mobility and contacts','high')]),
'17.2':(1,[('s6.9.2',H,'mutations raising transmissibility','low')]),
'17.3':(1,[('s6.15.0',H,'R0 definition','high')]),
'18.0':(1,[('s6.15.0',E,'R0 as comparison','high')]),
'18.1':(2,[('s6.18.0',E,'effective reproduction number','high'),('s6.15.0',E,'R0','high')]),
'18.2':(1,[('s6.18.0',E,'R below 1','high')]),
'19.0':(2,[('s6.15.0',E,'R0','high'),('s6.12.0',E,'herd immunity','high')]),
'19.1':(1,[('s6.19.0',E,'threshold formula','high')]),
'19.2':(1,[('s6.19.0',H,'threshold formula','high')]),
'19.3':(1,[('s6.19.2',E,'95% immune needed','high')]),
'20.0':(1,[('s6.15.0',E,'R0 model','high')]),
'20.1':(1,[('s6.20.0',H,'model assumptions','high')]),
'21.0':(2,[('s6.15.0',H,'R0','high'),('s6.9.2',H,'transmissibility mutation','low')]),
'21.1':(1,[('s6.6.1',H,'carriers persistence','high')]),
'21.2':(1,[('s6.13.0',H,'monoculture','high')]),
'21.3':(2,[('s6.1.1',H,'wild animal zoonoses','low')]),
}
src=open('points/bio22-s6.txt').read().split('CANDIDATES')[0]
tids=re.findall(r'^\[(bio22-s6\.[\w.]+)\]',src,re.M)
allids=set(re.findall(r'^\[([\w.\-]+)\]',open('points/bio22-s6.txt').read(),re.M))
out={}
for t in tids:
    k=t[len(P):]
    c,n=d.get(k,(1,[]))
    out[t]={'cost':c,'needs':[{'id':'bio22-'+a,'strength':s,'why':w,'confidence':f} for a,s,w,f in n]}
for t,v in out.items():
    for n in v['needs']:
        assert n['id'] in allids and n['id']!=t,(t,n)
json.dump(out,open('point-links/bio22-s6.json','w'),indent=1)
chk=json.load(open('point-links/bio22-s6.json'))
assert list(chk)==tids
print(len(chk),sum(len(v['needs']) for v in chk.values()),sum(v['cost']==2 for v in chk.values()),sum(n['confidence']=='low' for v in chk.values() for n in v['needs']))
