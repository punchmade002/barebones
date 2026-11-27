import json,re
P='/Users/gabrielwhelan/barebones/.claude/worktrees/crunch-chem-home/drafts/crunch/home-economics/'
S='hom-appliances-equipment-s2.'
def L(i,s,w,c='high'): return {"id":i,"strength":s,"why":w,"confidence":c}
D={
'0.b':(1,[]),'0.0':(1,[]),
'0.1':(1,[L(S+'4.b','helpful','energy label shows running cost')]),
'0.2':(1,[]),'0.3':(1,[]),
'0.4':(1,[L('hom-consumer-rights-s1.7.b','helpful','credit and easy-pay arrangements')]),
'1.b':(1,[]),'1.0':(1,[]),
'1.1':(2,[L('hom-consumer-rights-s3.0.3','helpful','manufacturer guarantee meaning')]),
'1.2':(2,[]),
'1.3':(2,[L(S+'6.b','helpful','recognised safety marks')]),
'1.4':(1,[]),
'2.b':(1,[]),
'2.0':(2,[L(S+'0.b','helpful','selection criteria applied','low')]),
'2.1':(1,[]),'2.2':(1,[]),
'3.b':(1,[]),'3.0':(1,[]),'3.1':(1,[]),'3.2':(1,[]),'3.3':(2,[]),'3.4':(1,[]),'3.5':(2,[]),'3.6':(1,[]),
'4.b':(1,[]),'4.0':(2,[]),'4.1':(1,[]),
'4.2':(1,[L(S+'4.0','essential','A to G efficiency scale')]),
'4.3':(1,[]),'4.4':(1,[]),'4.5':(1,[]),
'4.6':(2,[L(S+'4.3','helpful','energy in kWh on label')]),
'4.7':(2,[]),
'5.b':(1,[]),'5.0':(1,[]),'5.1':(1,[]),'5.2':(1,[]),'5.3':(1,[]),'5.4':(2,[]),
'5.5':(1,[L(S+'4.b','helpful','energy label compares running costs')]),
'6.b':(1,[]),'6.0':(1,[]),'6.1':(2,[]),'6.2':(1,[]),'6.3':(1,[]),'6.4':(1,[]),'6.5':(1,[]),'6.6':(1,[]),
'7.b':(1,[]),'7.0':(1,[]),'7.1':(1,[]),'7.2':(2,[]),'7.3':(1,[]),'7.4':(1,[]),'7.5':(1,[]),'7.6':(1,[]),'7.7':(2,[]),
'8.b':(1,[]),
'8.0':(2,[L(S+'4.b','helpful','best energy class')]),
'8.1':(2,[L(S+'4.7','helpful','efficient use habits')]),
'8.2':(1,[]),'8.3':(1,[]),'8.4':(1,[]),'8.5':(2,[]),'8.6':(1,[]),
'8.7':(1,[L('hom-environmental-issues-s2.7.1','helpful','crossed-out wheeled bin symbol')]),
'9.b':(1,[]),'9.0':(1,[]),'9.1':(1,[]),
'9.2':(1,[L(S+'4.b','helpful','energy label rating')]),
'9.3':(1,[]),
'10.b':(1,[]),'10.0':(1,[]),'10.1':(1,[]),'10.2':(1,[]),
}
txt=open(P+'packs/hom-appliances-equipment-s2.t1g1.txt').read()
tgt=re.findall(r'^\[('+re.escape(S)+r'[^\]]+)\]',txt,re.M)
allids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
out={}
for t in tgt:
    c,n=D[t[len(S):]]; out[t]={"cost":c,"needs":n}
assert len(out)==len(D)==len(tgt),(len(out),len(D),len(tgt))
assert all(n['id'] in allids and n['id']!=k for k,v in out.items() for n in v['needs'])
json.dump(out,open(P+'point-links/hom-appliances-equipment-s2.t1g1.json','w'),indent=1)
v=out.values()
print(len(out),sum(len(x['needs']) for x in v),sum(x['cost']==2 for x in v),sum(n['confidence']=='low' for x in v for n in x['needs']))
