import json,re
P='bio32-s1.'
pkg=open('../../points/bio32-s1.txt').read()
ids=re.findall(r'^\[([^\]]+)\]',pkg,re.M)
tgt=[i for i in ids if i.startswith(P)]
E,H='essential','helpful'
# id: (cost, [(need, strength, why, conf)])
D={
'0.b':(1,[('bio31-s1.3.0',H,'habitat','high')]),
'0.0':(1,[('bio6-s3.1.0',H,'species concept','low')]),
'0.5':(1,[('bio31-s1.2.2',H,'abiotic factors','high')]),
'1.0':(1,[('bio31-s1.3.1',H,'microhabitat','high')]),
'1.4':(1,[('11.0',H,'identification keys','high')]),
'1.3':(2,[]),
'3.4':(1,[('bio31-s1.3.1',H,'microhabitat','high')]),
'3.6':(1,[('11.0',H,'checking against keys','low')]),
'4.1':(1,[('4.0',E,'pitfall trap design','high')]),
'4.2':(1,[('4.0',H,'pitfall trap','high')]),
'4.3':(1,[('4.0',H,'pitfall trap','high')]),
'4.4':(1,[('4.0',H,'pitfall trap','high')]),
'4.5':(1,[('4.0',E,'pitfall trap structure','high')]),
'5.1':(1,[('5.0',E,'Tullgren funnel','high')]),
'5.2':(2,[('5.1',E,'funnel set-up with lamp','high')]),
'5.3':(1,[('5.1',H,'funnel beaker position','high')]),
'5.4':(1,[('5.0',H,'Tullgren funnel','high')]),
'5.5':(1,[('5.1',E,'mesh and lamp','high')]),
'5.6':(2,[('5.1',E,'funnel parts','high')]),
'6.1':(1,[('6.0',H,'earthworm collection','high')]),
'6.3':(1,[('6.2',E,'small-mammal trap','high')]),
'7.1':(1,[('7.0',E,'sweep net','high')]),
'7.2':(1,[('7.0',H,'sweep net','high')]),
'7.3':(1,[('2.2',H,'controlled variables, fair comparison','high')]),
'7.4':(1,[('7.0',E,'sweep net','high')]),
'7.6':(1,[('7.5',E,'beating tray','high')]),
'8.1':(2,[('8.0',E,'pooter structure','high')]),
'8.2':(1,[('8.1',E,'mouthpiece tube use','high')]),
'8.3':(1,[('8.0',H,'pooter','high')]),
'8.5':(2,[('8.1',E,'pooter parts and airflow','high')]),
'9.1':(1,[('9.0',H,'butterfly net','high')]),
'9.3':(1,[('9.2',E,'light trap','high')]),
'11.1':(1,[('11.0',E,'identification key','high')]),
'11.2':(1,[('11.1',E,'couplets','high')]),
'11.3':(2,[('11.0',H,'identification key','high')]),
'11.4':(1,[('11.3',H,'good key features','high')]),
'12.0':(1,[('11.1',E,'couplets','high')]),
'12.1':(1,[('12.0',E,'key continues','high')]),
'12.2':(2,[('12.1',E,'key continues','high')]),
'12.3':(1,[('12.2',E,'key continues','high')]),
'12.4':(2,[('12.3',E,'whole key','high')]),
'12.5':(1,[('11.1',H,'two-way splits','high')]),
'12.6':(1,[('12.5',E,'making a key','high')]),
'12.7':(1,[('12.5',H,'key splits','low')]),
'13.1':(1,[('11.0',H,'checking against a key','high')]),
'14.0':(2,[]),'14.2':(2,[]),'14.3':(2,[]),
'15.0':(2,[('7.5',H,'beating tray','high'),('4.0',H,'pitfall trap','high'),('5.0',H,'Tullgren funnel','high')]),
'15.1':(1,[('11.0',H,'seaweed key','low')]),
'15.3':(1,[('7.0',H,'sweeping like sweep net','low')]),
'15.4':(2,[('15.3',H,'pond net','high')]),
'15.5':(2,[('15.4',E,'kick sampling','high')]),
'18.0':(1,[('4.0',H,'pitfall trap limits','low')]),
'18.2':(1,[('2.2',H,'controlling variables','low')]),
'18.3':(1,[('4.3',H,'checking traps','high')]),
'18.4':(1,[('11.0',H,'identification keys','low')]),
}
out={}
for t in tgt:
    k=t[len(P):]
    c,n=D.get(k,(1,[]))
    out[t]={"cost":c,"needs":[{"id":(i if i.startswith('bio') else P+i),"strength":s,"why":w,"confidence":f} for i,s,w,f in n]}
for k in D: assert P+k in out,k
for t,v in out.items():
    for n in v['needs']: assert n['id'] in ids and n['id']!=t,n
json.dump(out,open('../../point-links/bio32-s1.json','w'),indent=0)
print(len(out),sum(len(v['needs']) for v in out.values()),sum(v['cost']==2 for v in out.values()),sum(n['confidence']=='low' for v in out.values() for n in v['needs']))
