import json,re
P='/Users/gabrielwhelan/barebones/.claude/worktrees/history-crunch/drafts/crunch/history/'
D='''
0.b|1|
0.0|1|
0.1|1|
0.2|1|
0.3|1|
0.4|1|
1.b|1|
1.0|1|
1.1|1|
1.2|1|
1.3|1|
1.4|1|
1.5|2|
1.6|2|
2.b|1|
2.0|1|1.2,h,indirect rule,H
2.1|1|
2.2|1|
2.3|1|1.3,h,federation defined,H
2.4|1|2.3,e,uses the three regions,H
2.5|2|2.1,h,ethnic groups behind parties,H;2.3,h,regional bases,H
2.6|1|2.3,h,Eastern Region,H
3.b|1|
3.0|1|2.5,e,uses the NPC and NCNC,H
3.1|1|1.1,h,Commonwealth defined,H;3.0,h,Balewa as prime minister,H
3.2|1|3.1,e,uses independence and Queen as head,H;2.3,h,regions of Nigeria,L
3.3|1|2.4,h,regional parties and tension,L
4.b|1|
4.0|2|3.0,e,uses Balewa,H;2.1,h,uses the Igbo,H
4.1|1|4.0,h,follows the January coup,H
4.2|1|2.1,h,uses the Igbo,H
4.3|1|4.2,h,crisis being settled,L
4.4|1|2.3,e,uses the Eastern Region,H;2.6,h,oil in the east,H
4.5|1|4.4,e,follows the twelve states decree,H;1.4,h,secession defined,H
5.b|1|
5.0|1|4.5,e,uses the Biafran secession,H
5.1|1|
5.2|1|4.5,e,uses Biafra,H
5.3|1|0.4,h,Soviet and Western rivalry,L
5.4|1|5.0,h,uses the Biafran famine,H
5.5|1|5.0,e,uses the end of the war,H
6.b|1|
6.0|2|
6.1|1|6.0,h,follows Leopold's rule,H
6.2|1|
6.3|1|1.5,h,uses the Force Publique,H
6.4|1|
6.5|1|
6.6|1|6.5,h,follows promise of independence,H
7.b|1|
7.0|1|6.4,h,uses Lumumba and the MNC,H
7.1|1|7.0,h,uses Baudouin and Lumumba,L
7.2|1|1.5,h,uses the Force Publique,H
7.3|1|1.4,h,secession defined,H;6.2,h,uses Katanga's mines,L
7.4|1|1.5,h,ONUC defined,H
7.5|2|7.0,e,uses Kasa-Vubu and Lumumba,H
7.6|1|7.5,e,uses the dismissal of Lumumba,H;0.4,h,Soviet help in the Cold War,H
7.7|1|7.6,e,follows Lumumba's capture,H;7.3,h,uses Katanga,H
8.b|1|7.5,h,uses first power seizure,H
8.0|1|7.5,e,uses the first coup,H
8.1|1|8.0,h,Mobutu in power,H
8.2|2|1.6,h,Zairianisation defined,H;8.1,h,uses Zaire under Mobutu,L
8.3|1|8.0,h,uses Mobutu's regime,H
8.4|2|0.4,h,Cold War anti-communism,H;7.3,h,Katangan exiles,L
8.5|1|8.3,e,uses the one-party state,H
9.b|1|
9.0|1|
9.1|1|
9.2|1|9.1,e,uses Nyerere and TANU,H
9.3|1|
9.4|2|9.3,e,uses Zanzibar after the revolution,H;9.2,h,uses Tanganyika's independence,H
9.5|1|9.2,h,uses Nyerere as leader,L
10.b|1|
10.0|1|
10.1|1|10.0,h,uses Tanzania's many groups,H
10.2|1|
10.3|1|1.1,e,Commonwealth defined,H;10.2,h,uses the break with Britain,H
11.b|1|
11.0|1|1.5,h,Estado Novo defined,H
11.1|2|11.0,h,Portuguese refusal behind the war,H
11.2|1|
11.3|1|
11.4|1|
11.5|1|11.0,h,uses the Portuguese regime,H
12.b|1|
12.0|1|11.b,h,names the three movements,H
12.1|1|11.2,e,uses the MPLA,H;12.0,h,follows the Alvor settlement,L
12.2|2|11.b,h,uses the three movements,H;0.4,h,Cold War backers,H
12.3|1|11.5,h,Portugal's withdrawal,L
12.4|1|
13.b|1|
13.0|2|3.2,e,uses the 1963 republic,H;5.3,h,arms in the Biafran War,H;2.6,h,uses Shell-BP oil,H
13.1|1|6.2,e,uses the Union Minière,H;7.3,h,uses Katanga's secession,H;8.4,h,Belgian support for Mobutu,H
13.2|1|6.2,e,uses the Union Minière,H;8.0,h,uses Mobutu in power,H
13.3|1|11.5,h,Portugal's exit in 1974,H;12.3,h,few skilled people left,H
13.4|1|10.2,e,uses the Rhodesia break,H;10.3,h,uses Commonwealth membership,H
13.5|1|s4.2.2,h,uses co-operation accords,H
14.b|1|14.0,h,uses colonial ethnic policy,L
14.0|1|1.0,h,tribalism defined,H
14.1|1|2.5,e,uses the three main parties,H;4.0,h,uses the 1966 coups,H
14.2|2|6.4,h,uses Lumumba and the MNC,H;7.0,h,uses Kasa-Vubu,H;7.3,h,uses Tshombe,H
14.3|1|7.3,e,uses Katanga's secession,H
14.4|1|10.1,e,uses Swahili and national identity,H;14.1,h,contrast with Nigeria,L
15.b|1|
15.0|1|10.1,h,uses Nyerere's national unity,H
15.1|1|6.3,e,uses lack of trained Congolese,H;7.2,h,uses the mutiny,H;7.3,h,uses Katanga's secession,H
15.2|1|5.5,h,uses the end of the Biafran War,H;2.6,h,uses Nigeria's oil,H
15.3|1|4.0,h,uses the 1966 coups,H;4.5,h,uses Biafra's secession,H
15.4|1|12.2,e,uses the Angolan civil war,H;11.b,h,uses the three movements,H
15.5|1|
15.6|1|0.1,h,uses colonial borders,H;0.4,h,uses the Cold War,H;14.0,h,uses colonial ethnic policies,H
15.7|1|15.0,h,uses Tanzania example,H;15.1,h,uses the Congo crisis,H;15.3,h,uses Nigeria's war,H;15.4,h,uses Angola's war,H
'''
out={}
for l in D.strip().split('\n'):
    k,c,n=l.split('|')
    k='hist-eur5-s5.'+k
    needs=[]
    out[k]={'cost':int(c),'needs':needs}
    for x in filter(None,n.split(';')):
        p=x.split(',')
        if len(p)<4: raise SystemExit('bad '+l)
        i='hist-eur5-'+p[0] if p[0].startswith('s4.') else 'hist-eur5-s5.'+p[0]
        needs.append({'id':i,'strength':'essential' if p[1]=='e' else 'helpful','why':','.join(p[2:-1]),'confidence':'high' if p[-1]=='H' else 'low'})
txt=open(P+'packs/hist-eur5-s5.t1g1.txt').read()
tids=re.findall(r'^\[(hist-[^\]]+)\]',txt.split('CANDIDATES')[0],re.M)
allids=set(re.findall(r'^\[(hist-[^\]]+)\]',txt,re.M))
assert list(out)==tids,(set(tids)-set(out),set(out)-set(tids))
for k,v in out.items():
    for n in v['needs']:
        assert n['id'] in allids and n['id']!=k and len(n['why'].split())<=8,(k,n)
json.dump(out,open(P+'point-links/hist-eur5-s5.t1g1.json','w'),indent=1)
print(len(out),sum(len(v['needs']) for v in out.values()),sum(v['cost']==2 for v in out.values()),sum(n['confidence']=='low' for v in out.values() for n in v['needs']))
