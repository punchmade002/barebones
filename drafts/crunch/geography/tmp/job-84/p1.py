import json,re
P='geo-population-migration-s3.'
S='geo-population-migration-s1.'
H,E='helpful','essential'
c2={'1.0','3.1','5.2','6.0','9.3','10.0','10.2','11.1','12.0','13.2'}
L={
'0.5':[(P+'0.1',H,'uses emigration','high')],
'3.2':[(P+'1.b',H,'push and pull factors','high'),(P+'2.b',E,'intervening obstacles','high')],
'5.1':[(S+'1.1',H,'census as population count','low')],
'6.3':[(P+'0.6',E,'chain migration','high')],
'6.4':[(P+'0.1',H,'net migration','high')],
'7.2':[(P+'0.5',H,'return migration','high')],
'8.3':[(P+'8.2',E,'undocumented emigrants','high')],
'9.0':[(P+'0.4',H,'asylum seekers','low')],
'9.2':[(P+'9.1',E,'EU enlargement 2004','high')],
'9.3':[(P+'9.1',H,'2004 accession countries','high')],
'9.5':[(P+'0.1',H,'immigration and net migration','low')],
'11.1':[(P+'0.4',H,'refugees and protection','low')],
'11.2':[(P+'0.4',H,'asylum seekers','high')],
'12.0':[(S+'1.0',E,'population change formula','high'),(P+'0.1',H,'net migration','high')],
'16.2':[(P+'0.5',H,'return migration','low')],
'17.1':[(S+'30.b',H,'ageing and dependency','low')],
'17.5':[(P+'12.0',E,'net migration vs natural increase','high')],
'18.4':[(P+'16.0',H,'remittances','high')],
'19.3':[(P+'0.5',H,'return migration','high')],
'20.1':[(P+'9.1',E,'2004 EU accession','high')],
}
ids='0.b 0.0 0.1 0.2 0.3 0.4 0.5 0.6 1.b 1.0 1.1 2.b 2.0 2.1 2.2 2.3 2.4 2.5 3.b 3.0 3.1 3.2 4.b 4.0 4.1 5.b 5.0 5.1 5.2 5.3 5.4 6.b 6.0 6.1 6.2 6.3 6.4 6.5 6.6 6.7 7.b 7.0 7.1 7.2 7.3 7.4 8.b 8.0 8.1 8.2 8.3 8.4 9.b 9.0 9.1 9.2 9.3 9.4 9.5 10.b 10.0 10.1 10.2 10.3 11.b 11.0 11.1 11.2 11.3 12.b 12.0 13.b 13.0 13.1 13.2 13.3 14.b 14.0 15.b 15.0 15.1 15.2 15.3 16.b 16.0 16.1 16.2 16.3 17.b 17.0 17.1 17.2 17.3 17.4 17.5 18.b 18.0 18.1 18.2 18.3 18.4 19.b 19.0 19.1 19.2 19.3 19.4 20.b 20.0 20.1'.split()
out={}
for i in ids:
    out[P+i]={'cost':2 if i in c2 else 1,'needs':[dict(id=a,strength=b,why=w,confidence=c) for a,b,w,c in L.get(i,[])]}
assert set(L)<=set(ids)
txt=open('packs/geo-population-migration-s3.t1g1.txt').read()
pk=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
tg=set(re.findall(r'^\[(geo-population-migration-s3\.[^\]]+)\]',txt.split('CANDIDATES')[0],re.M))
assert set(out)==tg and len(out)==len(ids)
for v in out.values():
    for n in v['needs']: assert n['id'] in pk,n
json.dump(out,open('point-links/geo-population-migration-s3.t1g1.json','w'),indent=1)
print(len(out),sum(len(v['needs']) for v in out.values()),sum(v['cost']==2 for v in out.values()),sum(n['confidence']=='low' for v in out.values() for n in v['needs']))
