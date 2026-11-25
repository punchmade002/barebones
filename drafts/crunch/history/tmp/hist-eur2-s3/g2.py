import json,re
H='/Users/gabrielwhelan/barebones/.claude/worktrees/history-crunch/drafts/crunch/history/'
P='hist-eur2-s3.'
def L(i,w,c='high',s='helpful'): return dict(id='hist-eur2-s1.'+i,strength=s,why=w,confidence=c)
links={
'0.0':[L('1.3','Kaiser appointed and dismissed Chancellor')],
'0.1':[L('1.6','Reichstag voted laws and budget')],
'0.2':[L('5.0','satiated power'),L('12.1','colonies of 1884-85')],
'0.3':[L('13.5','Bismarck resignation')],
'0.6':[L('9.4','Triple Alliance of 1882')],
'1.1':[L('13.0','year of three emperors')],
'1.2':[L('13.0','three rulers of 1888')],
'2.0':[L('13.5','Bismarck forced to resign'),L('13.6','Dropping the Pilot cartoon')],
'2.1':[L('1.6','Reichstag held the budget')],
'2.2':[L('13.5','Caprivi becoming Chancellor')],
'2.3':[L('10.4','Reinsurance Treaty with Russia')],
'2.4':[L('3.3','Anti-Socialist Law')],
'2.6':[L('3.4','SPD growth')],
'4.2':[L('9.0','Dual Alliance with Austria-Hungary','low')],
'5.0':[L('5.0',"Bismarck's satiated, Europe-centred policy",'low')],
'5.4':[L('12.3','Wehler and social imperialism')],
'7.0':[L('0.0','balance of power')],
}
ids=re.findall(r'^\[(\S+?)\]',open(H+'packs/hist-eur2-s3.t1g2.txt').read().split('CANDIDATES')[0],re.M)
out={i:{'needs':links.get(i[len(P):],[])} for i in ids}
allids=set(re.findall(r'^\[(\S+?)\]',open(H+'packs/hist-eur2-s3.t1g2.txt').read(),re.M))
assert all(k in [i[len(P):] for i in ids] for k in links)
for k,v in out.items():
    for n in v['needs']: assert n['id'] in allids
json.dump(out,open(H+'point-links/hist-eur2-s3.t1g2.json','w'),ensure_ascii=False,indent=0)
print(len(out),sum(len(v['needs']) for v in out.values()),sum(n['confidence']=='low' for v in out.values() for n in v['needs']))
