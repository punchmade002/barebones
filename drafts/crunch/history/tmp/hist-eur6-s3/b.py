import json,re
P='/Users/gabrielwhelan/barebones/drafts/crunch/history/'
H,E='high','essential'
def n(i,s='helpful',w='',c='high'): return (i,s,w,c)
D={
'0.b':(1,[n('hist-eur6-s2.5.6',w='uses the Viet Cong')]),
'0.0':(2,[]),'0.1':(1,[]),'0.2':(1,[]),
'0.3':(1,[n('hist-eur6-s1.5.6',w='Kennedy assassinated in Dallas')]),
'0.4':(1,[n('hist-eur6-s2.5.9',w="Diem's overthrow and killing")]),
'0.5':(1,[]),'0.6':(1,[]),
'0.7':(1,[n('hist-eur6-s2.0.6',E,'loss of China to communists')]),
'0.8':(1,[n('hist-eur6-s2.5.10',w='advisers numbers under Kennedy')]),
'0.9':(1,[n('hist-eur6-s2.5.6',w='uses the Viet Cong')]),
'0.10':(1,[]),
'1.b':(1,[]),'1.0':(2,[]),
'1.1':(2,[n('hist-eur6-s3.1.0',E,'the Maddox and Gulf of Tonkin')]),
'1.2':(1,[n('hist-eur6-s3.1.1',E,'the reported 4 August attack')]),
'1.3':(2,[n('hist-eur6-s3.1.2',w='retaliatory strikes prompting resolution')]),
'1.4':(1,[n('hist-eur6-s3.1.3',E,'the Tonkin Gulf Resolution')]),
'1.5':(1,[]),
'1.6':(1,[n('hist-eur6-s3.1.5',w='the 1964 campaign')]),
'2.b':(1,[]),
'2.0':(1,[n('hist-eur6-s2.5.6',w='Viet Cong attack')]),
'2.1':(1,[n('hist-eur6-s3.2.0',w='reprisal raids leading to bombing')]),
'2.2':(1,[]),'2.3':(1,[]),
'2.4':(2,[n('hist-eur6-s3.2.2',w='first ground combat troops')]),
'2.5':(2,[n('hist-eur6-s3.2.4',w='the July 1965 increase')]),
'2.6':(1,[]),
'2.7':(1,[n('hist-eur6-s3.2.1',E,'the bombing of North Vietnam')]),
'2.8':(2,[n('hist-eur6-s3.0.6',E,'McNamara, Rusk and Bundy')]),
'2.9':(1,[n('hist-eur6-s1.6.2',w='the Great Society')]),
'3.0':(2,[n('hist-eur6-s3.2.3',E,'Westmoreland and attrition')]),
'3.1':(1,[n('hist-eur6-s3.3.0',E,'attrition by search and destroy')]),
'3.2':(1,[n('hist-eur6-s3.3.0',w='heavy firepower strategy')]),
'3.3':(2,[n('hist-eur6-s2.5.9',w='unstable post-Diem governments')]),
'3.4':(1,[n('hist-eur6-s3.6.0',w='the Tet shock')]),
'3.5':(1,[]),
'3.6':(1,[]),
'4.b':(1,[]),'4.0':(1,[]),'4.1':(1,[]),'4.2':(1,[]),'4.3':(1,[]),'4.4':(1,[]),
'4.5':(1,[n('hist-eur6-s3.3.6',w='the draft')]),
'4.6':(1,[n('hist-eur6-s1.6.2',E,'the Great Society')]),
'4.7':(1,[]),
'5.b':(1,[n('hist-eur6-s1.6.2',w='the Great Society')]),
'5.0':(1,[n('hist-eur6-s1.6.2',E,'the Great Society')]),
'5.1':(1,[n('hist-eur6-s3.5.0',w='paying for war and Great Society')]),
'5.2':(1,[n('hist-eur6-s1.6.3',E,'the War on Poverty')]),
'5.3':(1,[n('hist-eur6-s1.6.1',w='the Civil Rights Act'),n('hist-eur6-s1.6.4',w='the Voting Rights Act')]),
'5.4':(1,[n('hist-eur6-s1.6.2',w='the Great Society')]),
'6.b':(1,[]),'6.0':(1,[]),
'6.1':(1,[n('hist-eur6-s3.6.0',w='the Tet attacks')]),
'6.2':(1,[n('hist-eur6-s3.3.4',E,"Westmoreland's end-in-view claim")]),
'6.3':(1,[n('hist-eur6-s3.6.2',w='official optimism contradicted')]),
'6.4':(1,[]),
'6.5':(2,[n('hist-eur6-s3.2.3',w='Westmoreland and troop strategy')]),
'6.6':(1,[]),
'6.7':(1,[n('hist-eur6-s3.2.1',w='the bombing campaign')]),
'6.8':(1,[n('hist-eur6-s3.6.7',w='peace talks offered')]),
'6.9':(2,[]),
'7.b':(1,[]),'7.0':(1,[]),
'7.1':(1,[n('hist-eur6-s3.2.7',w='Ho Chi Minh Trail supplies')]),
'7.2':(1,[n('hist-eur6-s3.3.3',w='weak Saigon regime')]),
'7.3':(1,[n('hist-eur6-s3.3.0',E,'attrition and body count')]),
'7.4':(2,[n('hist-eur6-s3.2.4',w='gradual escalation')]),
'7.5':(1,[n('hist-eur6-s3.4.0',w='the credibility gap')]),
'8.b':(1,[]),'8.0':(1,[]),'8.1':(1,[]),
'8.2':(2,[n('hist-eur6-s2.3.5',w='Chinese entry in Korea')]),
'8.3':(1,[n('hist-eur6-s3.4.0',E,'the credibility gap')]),
'8.4':(1,[]),'8.5':(2,[]),'8.6':(1,[]),
'9.b':(1,[]),'9.0':(1,[]),'9.1':(1,[]),'9.2':(1,[]),'9.3':(1,[]),
'9.4':(1,[n('hist-eur6-s3.4.0',E,'the credibility gap')]),
}
txt=open(P+'packs/hist-eur6-s3.t1g1.txt').read()
tgt=re.findall(r'^\[(hist-eur6-s3\.[^\]]+)\]',txt,re.M)
allids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
out={}
for t in tgt:
    k=t.split('hist-eur6-s3.')[1]
    c,ns=D[k]
    out[t]={'cost':c,'needs':[{'id':i,'strength':s,'why':w,'confidence':cf} for i,s,w,cf in ns]}
assert set(D)=={t.split('s3.',1)[1] for t in tgt}, set(D)^{t.split('s3.',1)[1] for t in tgt}
for v in out.values():
    for x in v['needs']: assert x['id'] in allids
json.dump(out,open(P+'point-links/hist-eur6-s3.t1g1.json','w'),indent=1)
print(len(out),sum(len(v['needs']) for v in out.values()),sum(v['cost']==2 for v in out.values()),sum(x['confidence']=='low' for v in out.values() for x in v['needs']))
