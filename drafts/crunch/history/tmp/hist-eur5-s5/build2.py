import json,re
P='hist-eur5-s5.'
E,H='essential','helpful'
D={
'0.b':(1,[]),
'0.0':(1,[]),
'0.1':(2,[]),
'0.2':(1,[('.0.1',H,'three main ethnic groups','high')]),
'0.3':(2,[('.0.2',H,'federation of regions','low')]),
'0.4':(1,[('.0.2',E,'the three regions','high')]),
'0.5':(1,[('.0.3',H,'Azikiwe and the Queen as head of state','high')]),
'0.6':(2,[('.0.1',H,'regional ethnic groups','high')]),
'0.7':(1,[('.0.2',H,'the Eastern Region','high')]),
'1.0':(2,[('.0.6',H,'the federal prime minister Balewa','low'),('.0.1',H,'Igbo and northern groups','high')]),
'1.1':(1,[('.1.0',E,'the January 1966 coup','high')]),
'1.2':(1,[('.1.1',H,'Gowon coup and unrest in 1966','low'),('.0.1',H,'Igbo in the north','high')]),
'1.3':(2,[('.0.2',E,'the Eastern Region','high'),('.1.2',H,'massacres driving Igbo east','high')]),
'1.4':(2,[('.1.3',E,'Biafra and the blockade','high')]),
'1.5':(2,[('.1.3',E,'Biafra','high')]),
'1.6':(2,[('.1.3',E,'Biafra\'s declaration','high'),('.1.1',H,'Gowon taking power','high'),('.0.7',H,'oil in the Eastern Region','high')]),
'1.7':(1,[('.1.4',E,'the Biafran War ending','high')]),
'1.8':(1,[('.1.4',H,'the famine in Biafra','high')]),
'2.b':(1,[]),
'2.0':(2,[]),
'2.1':(1,[('.2.0',H,'the Congo Free State before 1908','high')]),
'2.2':(1,[]),
'2.3':(1,[]),
'2.4':(1,[]),
'2.5':(1,[]),
'2.6':(1,[('.2.5',H,'Belgian promise of independence','high')]),
'3.0':(1,[('.2.4',E,'Lumumba and the MNC','high'),('.2.6',H,'independence date','high')]),
'3.1':(1,[('.3.0',H,'Lumumba as prime minister','high')]),
'3.2':(1,[('.2.3',E,'the Force Publique and Belgian officers','high')]),
'3.3':(1,[('.2.2',H,'Katanga\'s mineral wealth','low')]),
'3.4':(1,[('.3.2',H,'the mutiny and Belgian troops','high')]),
'3.5':(1,[('.3.0',E,'Kasa-Vubu and Lumumba in office','high')]),
'3.6':(2,[('.3.5',E,'the dismissal dispute','high')]),
'3.7':(2,[('.3.6',E,'Lumumba confined under Mobutu','high'),('.3.3',H,'Katanga','high')]),
'4.0':(1,[('.3.6',E,'Mobutu\'s earlier intervention','high')]),
'4.1':(2,[('.4.0',H,'Mobutu\'s regime','high')]),
'4.2':(2,[('.4.1',H,'Zaire and Mobutu\'s regime','high')]),
'4.3':(1,[('.4.0',H,'Mobutu\'s regime','high')]),
'4.4':(2,[('.4.0',H,'Mobutu\'s regime','high'),('.3.3',H,'Katanga secession','low')]),
'4.5':(1,[('.4.3',E,'the one-party state','high')]),
'5.b':(1,[]),
'5.0':(1,[]),
'5.1':(1,[]),
'5.2':(1,[('.5.1',E,'Nyerere and TANU','high')]),
'5.3':(2,[('.5.2',H,'Tanganyika\'s independence','low')]),
'5.4':(1,[('.5.2',E,'Tanganyika','high'),('.5.3',E,'Zanzibar\'s revolution','high')]),
'5.5':(1,[('.5.4',H,'the united Tanzania','high')]),
'5.6':(1,[('.5.2',H,'Nyerere as leader','high')]),
'5.7':(1,[('.5.4',H,'Tanzania','high')]),
'6.0':(1,[]),
'6.1':(2,[('.6.0',E,'Portuguese rule of Angola','high')]),
'6.2':(2,[('.6.1',H,'the war of independence','high')]),
'6.3':(1,[('.6.0',E,'Portugal\'s Estado Novo regime','high')]),
'6.4':(1,[('.6.2',E,'the three movements','high'),('.6.3',E,'Portuguese agreement to independence','high')]),
'6.5':(2,[('.6.2',E,'the MPLA, UNITA and FNLA','high'),('.6.4',H,'the Alvor breakdown','high')]),
'6.6':(1,[('.6.5',H,'independence in 1975','high')]),
'7.0':(1,[('.0.5',E,'the republic of 1963','high'),('.0.7',H,'Shell-BP oil','high')]),
'7.1':(2,[('.2.2',E,'the Union Minière','high')]),
'7.2':(1,[('.6.5',H,'the war that followed independence','high')]),
'7.3':(2,[('.5.7',H,'Tanzania and Britain','low'),('.1.5',H,'British arms to Nigeria','low')]),
'7.4':(1,[('hist-eur5-s4.0.7',H,'co-operation accords with France','high')]),
'8.0':(1,[('.0.0',H,'indirect rule','high')]),
'8.1':(2,[('.0.1',E,'the three main ethnic groups','high'),('.1.0',E,'the 1966 coups','high'),('.1.2',H,'the massacres','high')]),
'8.2':(2,[('.2.4',H,'Lumumba\'s MNC','low'),('.3.0',H,'Kasa-Vubu','high'),('.3.3',H,'Katanga','high')]),
'8.3':(1,[('.3.3',E,'Katanga\'s secession','high')]),
'8.4':(1,[('.5.5',E,'Swahili as national language','high')]),
'9.0':(1,[('.5.4',H,'Tanzania\'s union','low')]),
'9.1':(1,[('.2.3',H,'few trained Congolese','high'),('.3.2',E,'the mutiny','high'),('.3.3',E,'Katanga\'s secession','high')]),
'9.2':(1,[('.1.4',E,'the Biafran War','high'),('.0.7',H,'Nigeria\'s oil','high')]),
'9.3':(1,[('.1.0',E,'the 1966 coups','high'),('.1.4',E,'the Biafran War','high')]),
'9.4':(1,[]),
'9.5':(1,[]),
'9.6':(1,[('.6.2',E,'the three movements','high'),('.6.5',E,'the civil war','high')]),
}
out={}
for k,(c,n) in D.items():
    out[P+k]={"cost":c,"needs":[{"id":(P[:-1]+t if t.startswith('.') else t),"strength":s,"why":w,"confidence":cf} for t,s,w,cf in n]}
base='/Users/gabrielwhelan/barebones/drafts/crunch/history/'
txt=open(base+'packs/hist-eur5-s5.t1g1.txt').read()
ids=re.findall(r'^\[([^\]]+)\]',txt,re.M)
tgt=[i for i in ids if i.startswith(P)]
assert list(out)==tgt,(set(tgt)^set(out),)
for k,v in out.items():
    for n in v['needs']: assert n['id'] in ids and n['id']!=k,(k,n)
json.dump(out,open(base+'point-links/hist-eur5-s5.t1g1.json','w'),indent=0)
d=json.load(open(base+'point-links/hist-eur5-s5.t1g1.json'))
print(len(d),sum(len(v['needs']) for v in d.values()),sum(v['cost']==2 for v in d.values()),sum(n['confidence']=='low' for v in d.values() for n in v['needs']))
