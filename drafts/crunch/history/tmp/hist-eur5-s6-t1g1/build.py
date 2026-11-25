import json,re
H,E='helpful','essential'
def L(i,s,w,c='high'): return {"id":i,"strength":s,"why":w,"confidence":c}
P='hist-eur5-s6.'; Q='hist-eur5-s5.'
D={
'0.b':(1,[]),
'0.0':(2,[L(Q+'6.1',H,'paternalistic Belgian administration')]),
'0.1':(2,[L(Q+'7.0',H,'Kasa-Vubu and Lumumba in power','low')]),
'0.2':(1,[L(Q+'0.4',H,'Cold War superpower rivalry')]),
'0.3':(1,[L(Q+'6.2',H,'Congo mineral wealth')]),
'0.4':(1,[L(Q+'6.2',H,'Union Minière in Katanga')]),
'0.5':(1,[L(P+'0.6',E,'uses Conakat')]),
'0.6':(2,[L(P+'0.3',H,'Katanga revenue')]),
'0.7':(2,[L(P+'0.6',E,'rivalry with Conakat')]),
'1.b':(1,[]),
'1.0':(1,[L(P+'0.1',H,'Congo independence 30 June')]),
'1.1':(2,[L(P+'0.6',E,'uses Conakat and Tshombe'),L(Q+'6.4',H,'Lumumba\'s MNC strong nationally')]),
'1.2':(1,[L(P+'0.3',E,'Katanga\'s revenue')]),
'1.3':(2,[L(P+'1.0',H,'the proclamation of secession')]),
'1.4':(1,[L(P+'1.0',H,'the secession')]),
'1.5':(1,[L(P+'3.0',H,'ONUC introduced')]),
'1.6':(2,[L(P+'1.5',E,'uses the UN force ONUC'),L(P+'1.3',H,'Belgian officers in Katanga')]),
'2.b':(1,[]),
'2.0':(2,[L(P+'3.0',E,'ONUC would not use force')]),
'2.1':(2,[L(P+'2.0',H,'Soviet aid to Lumumba'),L(Q+'7.5',H,'Mobutu\'s September 1960 coup')]),
'2.2':(1,[L(P+'2.1',E,'Lumumba dismissed and Mobutu coup')]),
'2.3':(1,[L(P+'2.2',H,'Lumumba\'s capture')]),
'2.4':(2,[L(P+'2.3',E,'uses Lumumba\'s murder'),L(P+'3.2',H,'Resolution 161')]),
'2.5':(1,[L(P+'2.3',H,'Lumumba\'s death')]),
'3.b':(1,[]),
'3.0':(2,[L(P+'1.5',H,'creation of ONUC')]),
'3.1':(1,[L(P+'3.0',H,'ONUC soldiers')]),
'3.2':(2,[L(P+'2.4',H,'Resolution 161 first mentioned')]),
'3.3':(2,[L(P+'3.2',H,'firmer UN policy')]),
'3.4':(2,[L(P+'3.3',E,'uses Operation Morthor')]),
'3.5':(1,[L(P+'3.4',E,'uses the Jadotville siege')]),
'3.6':(1,[L(P+'3.3',H,'Conor Cruise O\'Brien')]),
'4.b':(1,[]),
'4.0':(1,[L(P+'3.0',H,'Hammarskjöld and the Congo operation')]),
'4.1':(1,[L(P+'3.0',H,'Hammarskjöld and ONUC')]),
'4.2':(2,[L(P+'3.3',H,'fighting after Morthor')]),
'4.3':(1,[L(P+'4.1',H,'Hammarskjöld\'s death')]),
'4.4':(2,[L(P+'4.3',E,'uses Operation Grand Slam')]),
'4.5':(1,[L(P+'4.4',H,'end of the secession')]),
'5.b':(1,[]),
'5.0':(1,[L(P+'4.5',H,'Tshombe in exile')]),
'5.1':(2,[L(P+'2.3',H,'Lumumba supporters')]),
'5.2':(2,[L(P+'2.1',E,'first Mobutu coup of 1960')]),
'5.3':(1,[L(P+'5.0',H,'Tshombe as prime minister')]),
'5.4':(2,[L(P+'5.2',H,'Mobutu\'s coup')]),
'5.5':(2,[L(P+'1.3',H,'Katanga Gendarmerie origins')]),
'5.6':(1,[L(P+'5.2',H,'Mobutu\'s regime')]),
'6.b':(2,[L(Q+'1.5',H,'Force Publique','low')]),
'6.0':(2,[L(P+'2.1',E,'the 1960 coup')]),
'6.1':(1,[L(P+'6.0',H,'Mobutu in 1960')]),
'6.2':(1,[L(P+'5.2',H,'1965 coup')]),
'6.3':(1,[L(P+'5.2',H,'1965 coup')]),
'6.4':(1,[L(P+'0.4',E,'Union Minière')]),
'6.5':(1,[L(P+'6.1',H,'US view of Mobutu','low')]),
'6.6':(1,[]),
'6.7':(1,[]),
'7.b':(1,[]),
'7.0':(1,[L(P+'5.0',H,'Tshombe and the secession ending')]),
'7.1':(1,[L(P+'2.0',H,'Soviet aid and Cold War')]),
'7.2':(1,[L(P+'3.0',H,'UN force ONUC')]),
'7.3':(1,[L(P+'3.0',H,'UN used force in the Congo','low')]),
'7.4':(1,[L(P+'0.4',E,'Union Minière')]),
'7.5':(2,[L(P+'2.3',H,'Lumumba backed by these states')]),
'7.6':(1,[L(P+'4.1',H,'Hammarskjöld\'s death')]),
'8.b':(1,[]),
'8.0':(2,[L(P+'0.4',E,'Union Minière')]),
'8.1':(1,[L(P+'0.6',E,'uses Conakat')]),
'8.2':(2,[L(P+'2.0',H,'Soviet aid to Lumumba'),L(P+'6.1',H,'CIA role')]),
'8.3':(1,[L(Q+'0.1',H,'colonial borders from partition')]),
'8.4':(2,[L(P+'5.1',E,'uses the Simba rebellion')]),
'8.5':(2,[L(P+'1.2',H,'Tshombe\'s case for secession')]),
'8.6':(1,[L(P+'3.0',H,'the UN\'s role')]),
'8.7':(2,[L(P+'2.3',H,'Lumumba\'s murder'),L(P+'0.4',H,'Union Minière')]),
}
out='/Users/gabrielwhelan/barebones/.claude/worktrees/history-crunch/drafts/crunch/history/point-links/hist-eur5-s6.t1g1.json'
pk=open('/Users/gabrielwhelan/barebones/.claude/worktrees/history-crunch/drafts/crunch/history/packs/hist-eur5-s6.t1g1.txt').read()
tg=re.findall(r'^\[([^\]]+)\]',pk.split('CANDIDATES')[0],re.M)
allids=set(re.findall(r'^\[([^\]]+)\]',pk,re.M))
res={}
for t in tg:
    c,n=D[t.replace(P,'')]; res[t]={"cost":c,"needs":n}
assert len(D)==len(tg)
for t,v in res.items():
    for n in v['needs']: assert n['id'] in allids and n['id']!=t,(t,n)
json.dump(res,open(out,'w'),ensure_ascii=False,indent=0)
print(len(res),sum(len(v['needs']) for v in res.values()),sum(v['cost']==2 for v in res.values()),sum(n['confidence']=='low' for v in res.values() for n in v['needs']))
