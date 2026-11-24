import json,re
P='/Users/gabrielwhelan/barebones/drafts/crunch/history/'
p='hist-ire4-s7.'
def L(i,s,w,c='high'):return {"id":p+i,"strength":s,"why":w,"confidence":c}
E,H='essential','helpful'
D={
'0.b':(1,[]),'0.0':(2,[]),'0.1':(1,[L('0.0',H,'Church growth producing surplus clergy')]),
'0.2':(1,[]),'0.3':(1,[]),'0.4':(1,[]),'0.5':(1,[]),'0.6':(1,[]),'0.7':(1,[]),
'1.0':(2,[]),'1.1':(1,[L('1.0',E,'uses the Columbans')]),'1.2':(2,[]),'1.3':(1,[]),'1.4':(1,[]),
'1.5':(1,[L('4.2',H,'founder Joseph Shanahan')]),'1.6':(1,[]),
'2.b':(1,[]),'2.0':(1,[]),'2.1':(1,[L('1.0',H,'the Maynooth Mission to China','low')]),
'2.2':(1,[L('2.1',E,'uses the Maynooth Mission to China')]),
'2.3':(2,[L('2.2',H,'his Hanyang mission area')]),
'2.4':(1,[L('2.2',H,'the Hanyang mission')]),
'2.5':(1,[L('2.2',H,'the Hanyang mission')]),
'2.6':(2,[L('2.2',H,'the Hanyang mission he led')]),
'2.7':(1,[L('2.1',H,'the China mission')]),'2.8':(1,[]),
'2.9':(1,[L('1.1',H,'the Columbans in China')]),
'3.b':(1,[]),'3.0':(1,[]),'3.1':(2,[]),
'3.2':(1,[L('3.1',H,'the 1936 change enabling her order')]),
'3.3':(1,[L('3.2',E,'uses the Medical Missionaries of Mary')]),
'3.4':(1,[L('3.2',E,'uses the Medical Missionaries of Mary')]),
'3.5':(1,[L('3.2',E,'uses the order she founded')]),
'3.6':(1,[L('3.0',H,'Mary Martin background')]),
'3.7':(1,[L('3.2',E,'uses the order praised')]),
'3.8':(2,[L('3.2',E,'uses the Medical Missionaries of Mary')]),
'4.b':(1,[]),'4.0':(1,[]),'4.1':(1,[L('4.0',H,'the Holy Ghost Fathers mission')]),
'4.2':(1,[L('4.1',H,'the Igbo mission area')]),
'4.3':(1,[L('4.2',E,'uses Joseph Shanahan')]),
'4.4':(1,[L('4.2',E,'uses Joseph Shanahan')]),
'4.5':(1,[]),'4.6':(1,[L('4.0',H,'the mission begun in 1885')]),
'5.b':(1,[]),'5.0':(1,[L('4.6',H,'the existing 1945 mission network')]),
'5.1':(2,[]),'5.2':(1,[]),
'5.3':(1,[L('4.2',H,'schools as the mission instrument')]),
'5.4':(1,[L('5.3',H,'mission schools system')]),
'5.5':(1,[L('1.5',H,'Holy Rosary Sisters'),L('3.4',H,'Medical Missionaries of Mary hospitals')]),
'5.6':(1,[]),'5.7':(1,[L('5.6',H,'local vocations','low')]),
'6.b':(1,[]),'6.0':(1,[L('5.3',H,'mission schools')]),
'6.1':(1,[L('6.0',E,'uses the grant system')]),
'6.2':(1,[L('6.0',H,'colonial-mission school relations')]),
'6.3':(1,[L('6.0',H,'mission schools under grants')]),
'6.4':(1,[]),'6.5':(1,[L('6.4',E,'uses independence in 1960')]),
'6.6':(1,[L('5.3',H,'mission schools educated Nigerians')]),
'7.b':(1,[]),'7.0':(2,[]),'7.1':(1,[L('5.3',H,'mission education')]),
'7.2':(1,[L('6.5',H,'localisation of leadership')]),
'7.3':(1,[L('4.5',H,'Methodist and Anglican rivalry')]),
'7.4':(1,[]),'7.5':(2,[L('7.4',E,'uses the Biafran war')]),
'7.6':(1,[L('7.4',E,'uses the Biafran famine')]),
'7.7':(1,[L('7.4',H,'the Biafran war aftermath'),L('5.1',H,'Bishop Whelan of Owerri')]),
'8.0':(1,[L('0.2',H,'Ireland spiritual empire idea')]),
'8.1':(1,[L('0.2',E,'uses Irish spiritual empire')]),
'8.2':(1,[L('0.5',H,'parish fundraising for missions')]),
'8.3':(2,[L('8.1',E,'questions the empire idea')]),
'8.4':(1,[L('6.5',H,'localisation of churches')]),
'9.0':(1,[L('7.0',H,'mission achievements')]),
'9.1':(1,[L('6.0',H,'ties through grants'),L('7.2',H,'slow handover to local clergy')]),
'9.2':(2,[L('7.2',H,'paternalism criticism')]),
'9.3':(2,[L('7.1',H,'cultural costs')]),
'9.4':(2,[L('2.6',E,'Galvin mission expelled 1952'),L('3.2',E,'Martin order grew in Africa')]),
}
txt=open(P+'packs/hist-ire4-s7.t1g1.txt').read()
ids=re.findall(r'^\[([^\]]+)\]',txt,re.M)
tgt=[i for i in ids if i.startswith(p)]
assert set(i[len(p):] for i in tgt)==set(D) and len(tgt)==len(D),(set(i[len(p):] for i in tgt)^set(D))
out={i:{"cost":D[i[len(p):]][0],"needs":D[i[len(p):]][1]} for i in tgt}
for k,v in out.items():
  for n in v['needs']: assert n['id'] in ids and n['id']!=k
json.dump(out,open(P+'point-links/hist-ire4-s7.t1g1.json','w'),indent=1)
print(len(out),sum(len(v['needs']) for v in out.values()),sum(v['cost']==2 for v in out.values()),sum(n['confidence']=='low' for v in out.values() for n in v['needs']))
