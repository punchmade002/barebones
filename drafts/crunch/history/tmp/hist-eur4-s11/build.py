import json,re
P='/Users/gabrielwhelan/barebones/.claude/worktrees/history-crunch/drafts/crunch/history/'
H,E='high','essential'
def n(i,s,w,c=H): return {"id":"hist-eur4-s11."+i if not i.startswith('s4') else "hist-eur4-"+i,"strength":s,"why":w,"confidence":c}
h='helpful'
D={
'0.b':(1,[]),'0.0':(1,[]),'0.1':(2,[]),'0.2':(2,[]),'0.3':(1,[]),
'0.4':(1,[n('0.3',h,'John XXIII elected pope')]),
'0.5':(1,[n('0.4',h,'the Council he announced')]),
'0.6':(1,[n('0.4',h,'the Council he announced')]),
'0.7':(1,[n('0.0',h,'the Roman Curia')]),
'1.b':(1,[]),
'1.0':(1,[n('0.4',h,'the Council announced')]),
'1.1':(2,[n('0.7',E,'Curia prepared drafts, clash at opening')]),
'1.2':(1,[n('0.3',h,'John XXIII as pope')]),
'1.3':(2,[n('2.0',h,'Sacrosanctum Concilium content')]),
'1.4':(2,[n('2.1',h,'Lumen Gentium content'),n('2.4',h,'Unitatis Redintegratio content')]),
'1.5':(2,[n('2.b',h,'document types and ranks','low')]),
'1.6':(1,[]),
'2.b':(1,[]),'2.0':(1,[]),
'2.1':(1,[n('1.3',h,'collegiality defined')]),
'2.2':(1,[]),'2.3':(1,[]),
'2.4':(1,[n('3.3',h,'ecumenical movement explained')]),
'2.5':(1,[]),'2.6':(1,[]),
'3.b':(1,[]),
'3.0':(1,[n('2.0',h,'liturgy reform document')]),
'3.1':(1,[n('3.0',h,'Missal and Latin Mass')]),
'3.2':(1,[]),
'3.3':(1,[n('2.4',h,'Unitatis Redintegratio decree')]),
'3.4':(1,[]),
'3.5':(1,[n('2.5',E,'Nostra Aetate declaration')]),
'3.6':(1,[]),
'3.7':(2,[n('2.6',E,'Dignitatis Humanae religious liberty')]),
'4.b':(1,[]),
'4.0':(1,[n('2.6',h,'religious liberty teaching'),n('3.0',h,'new liturgy')]),
'4.1':(1,[n('4.0',E,'Lefebvre and the Society')]),
'4.2':(1,[n('1.3',h,'collegiality idea')]),
'4.3':(1,[]),
'4.4':(2,[n('4.3',E,'Humanae Vitae ban on contraception')]),
'4.5':(1,[n('4.3',E,'dissent from Humanae Vitae')]),
'4.6':(1,[n('4.3',E,'Humanae Vitae as turning point')]),
'4.7':(2,[]),
'5.b':(1,[]),
'5.0':(1,[n('2.3',h,'Gaudium et Spes document')]),
'5.1':(1,[n('5.0',h,'Wojtyla as John Paul II')]),
'5.2':(2,[n('s4.5.4',E,'Solidarity union and Walesa'),n('5.1',h,'1979 visit to Poland')]),
'5.3':(1,[]),
'5.4':(2,[n('1.6',h,'Ratzinger background','low')]),
'5.5':(1,[n('3.5',h,'Nostra Aetate and Jewish dialogue')]),
'5.6':(1,[]),
'5.7':(2,[n('5.4',h,'conservative teaching under him')]),
'6.b':(1,[]),'6.0':(2,[]),'6.1':(1,[]),'6.2':(1,[]),'6.3':(1,[]),
'6.4':(1,[n('3.2',h,'lay participation reforms')]),
'7.b':(1,[]),
'7.0':(1,[n('3.0',h,'vernacular liturgy'),n('3.3',h,'ecumenical relations')]),
'7.1':(2,[n('4.3',h,'Humanae Vitae dispute')]),
'7.2':(1,[]),
'7.3':(1,[n('6.b',h,'social change coinciding with Council')]),
'7.4':(1,[n('4.0',h,'traditionalist reaction'),n('4.2',h,'progressive complaints')]),
}
out={}
for k,(c,l) in D.items(): out["hist-eur4-s11."+k]={"cost":c,"needs":l}
json.dump(out,open(P+'point-links/hist-eur4-s11.t1g1.json','w'),indent=1)
txt=open(P+'packs/hist-eur4-s11.t1g1.txt').read()
ids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
tg=re.findall(r'^\[(hist-eur4-s11\.[^\]]+)\]',txt,re.M)
assert sorted(tg)==sorted(out) and len(tg)==len(set(tg)),(set(tg)^set(out))
assert all(x['id'] in ids and x['id']!=k for k,v in out.items() for x in v['needs'])
print(len(out),sum(len(v['needs']) for v in out.values()),sum(v['cost']==2 for v in out.values()),sum(x['confidence']=='low' for v in out.values() for x in v['needs']))
