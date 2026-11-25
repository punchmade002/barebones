import json,re
H='/Users/gabrielwhelan/barebones/.claude/worktrees/history-crunch/drafts/crunch/history/'
# line: id cost ; links "tid/E|H/why/h|l"  (tid without 'hist-eur4-' prefix; bare like 4.2 => s4.2, s1.x => s1.x)
SPEC='''
0.b 1
0.0 1
0.1 1 s1.11.5/H/uses satellite state/h
0.2 1 s1.10.5/H/Comecon introduced/h ; s1.19.5/H/Warsaw Pact introduced/h
0.3 2
0.4 1 0.2/H/Warsaw Pact/h
0.5 1 0.0/H/communist planned economy/h
0.6 1
0.7 2 s1.0.5/H/Cold War/h
1.b 1
1.0 1
1.1 1 1.0/E/uses the East Berlin rising/h
1.2 1
1.3 1 s1.12.4/H/Gomułka's earlier purge/h
1.4 1 1.3/E/Gomułka's return to power/h ; 0.2/H/Warsaw Pact/h
1.5 1 1.3/H/Gomułka's rise/h
1.6 1 1.5/H/1956 settlement/h
1.7 2 1.3/E/Poland 1956/h ; 0.4/E/Hungary 1956 crushed/h ; 2.6/E/1968 invasion/h
2.b 1
2.0 1
2.1 1 2.0/H/Dubček's rise/h
2.2 1 2.0/H/Dubček's government/h
2.3 1 2.1/H/reform programme/l
2.4 1 0.4/H/Nagy's step in Hungary/h ; 0.2/H/Warsaw Pact/h
2.5 2 2.1/H/reform feared to spread/l
2.6 1 2.5/H/warning before the invasion/h
2.7 1 2.6/E/the invasion/h
3.b 1
3.0 1 2.6/E/the invasion/h
3.1 2 2.6/H/the invasion it justified/h
3.2 1 2.0/H/Dubček replaced/h
3.3 1 3.2/H/Husák's normalisation/h
3.4 1 2.6/H/crushing of reform/h
3.5 1 0.6/E/Helsinki Final Act/h
3.6 1 3.5/E/Charter 77/h
3.7 1 3.5/H/Charter 77/h
4.b 1
4.0 1
4.1 1 4.0/E/Wojtyła elected pope/h
4.2 1 4.1/E/first papal visit/h
4.3 1 4.2/H/effect of the visit/h ; 5.1/E/Gdańsk strike/h
4.4 1 5.4/H/Wałęsa and Solidarity/h
4.5 1 4.0/H/the pope/h
4.6 1 4.0/H/the pope/h
4.7 2 4.2/H/Polish civil society/l
5.b 1
5.0 2 1.6/H/Gomułka's rule/h
5.1 1
5.2 1 5.1/H/Gdańsk strike/h
5.3 1 5.2/E/the 21 demands/h
5.4 1 5.3/H/right to form unions/h
5.5 1 5.4/E/Solidarity/h
6.b 1
6.0 1 5.4/E/Solidarity/h
6.1 1 6.0/E/martial law/h
6.2 2 6.0/E/martial law/h
6.3 2 6.2/E/Jaruzelski's claim/h
6.4 2 6.0/H/martial law/h
6.5 1 6.1/H/ban on Solidarity/h
6.6 2 6.5/E/Solidarity's survival/h
6.7 1 6.6/E/Round Table agreement/h
7.b 1
7.0 1
7.1 1 0.3/H/Andropov as leader/h
7.2 2 0.3/H/Chernenko and the leaders/h
7.3 2 7.2/E/Gorbachev's offices/h
7.4 2 0.4/H/Khrushchev in 1956/h
7.5 2 10.0/H/Reagan summits/h
7.6 2 15.4/H/Yeltsin's dismissal/l
7.7 2
8.b 1
8.0 1 0.5/H/economic stagnation/h ; 0.7/H/arms race/h
8.1 1
8.2 1
8.3 1 0.5/H/planned economy/h
8.4 1 8.3/H/early effort/h
8.5 2 8.3/H/uskorenie failed/h
8.6 1 8.5/E/perestroika/h
8.7 2 8.5/E/perestroika's market elements/h
9.b 1
9.0 1
9.1 1 9.0/H/case for glasnost/h
9.2 1 9.0/E/glasnost/h
9.3 1 9.0/H/glasnost/h
9.4 1 9.0/H/glasnost/h
9.5 1 9.4/E/democratisation/h
9.6 1 9.4/H/party monopoly ending/h
9.7 1 9.0/E/glasnost/h
10.b 1
10.0 1 0.7/E/SDI/h
10.1 1 10.0/H/summit diplomacy/h
10.2 1
10.3 1 0.7/H/Afghanistan invasion/h
10.4 1
10.5 1 10.1/H/INF Treaty/h
11.b 1
11.0 2 6.6/E/partly free elections/h
11.1 1 11.0/H/election result/h
11.2 1 5.4/H/Wałęsa/h
11.3 2 0.4/H/Kádár since 1956/h
11.4 1 0.4/E/1956 uprising/h
11.5 1 11.3/H/border opening/h
11.6 1 11.4/H/1956 memory/h
11.7 1 11.6/H/multi-party elections/h
12.b 1
12.0 1 11.5/E/Hungary opening border/h
12.1 1
12.2 1
12.3 1 12.1/H/demonstrations/h
12.4 1 12.3/H/mass protests/h
12.5 1 12.4/H/crowds and travel rules/l
12.6 1 12.5/E/travel announcement/h
13.b 1
13.0 1
13.1 1 13.0/E/Velvet Revolution/h ; 3.7/H/Havel/h
13.2 1 13.1/H/mass demonstrations/h ; 3.2/H/Husák/h
13.3 1 2.0/H/Dubček of 1968/h ; 3.7/H/Havel/h
13.4 1
13.5 1
13.6 1 13.5/E/Timișoara protests/h ; 3.0/H/Ceaușescu/h
13.7 1 13.6/E/Ceaușescu's fall/h
14.b 1
14.0 1 3.1/E/Brezhnev Doctrine/h
14.1 1 7.4/H/Gorbachev's aim/h
14.2 1 0.5/E/command economy failure/h
14.3 1 11.0/H/Poland's example/h ; 11.3/H/Hungary's example/h
14.4 1
14.5 1 14.0/E/no Soviet intervention/h
15.b 1
15.0 1 9.7/H/glasnost releasing nationalism/h
15.1 1
15.2 1
15.3 1 9.7/H/nationalism in republics/h
15.4 2
15.5 1 15.4/E/Yeltsin's rise/h ; 7.3/H/Gorbachev's lack of mandate/h
16.b 1
16.0 1 0.2/E/Comecon and Warsaw Pact/h
16.1 1 15.3/H/republics' demands/l
16.2 1 16.1/H/coup context/h
16.3 1 16.2/E/the coup/h ; 15.5/H/Yeltsin's role/h
16.4 1 16.3/H/coup's failure/h
16.5 1 15.3/H/independence movements/h
17.b 1
17.0 1
17.1 1 17.0/H/Ukraine's referendum/l
17.2 1 17.1/E/CIS founding/h
17.3 1 17.2/H/CIS replacing the Union/h ; 7.2/H/Gorbachev's presidency/h
17.4 1 17.3/H/resignation/h
18.b 1
18.0 1 12.6/H/the Wall's fall/h
18.1 1 18.0/H/push for unity/h
18.2 1 18.1/H/unification process/h
18.3 1 s1.19.1/H/NATO/h
18.4 1 18.3/H/NATO consent/h
18.5 1 18.4/E/Two Plus Four Treaty/h ; s1.4.3/H/Oder-Neisse border/h
18.6 1 18.4/H/treaty/h
19.b 1
19.0 1
19.1 1 19.0/H/Yugoslav breakdown/h
19.2 1 19.1/H/Serbian opposition to secession/h
19.3 1 19.2/E/Slovenia's independence/h
19.4 1 19.2/E/Croatia's independence/h
19.5 1 19.2/E/Slovenia and Croatia independence/h
19.6 1 19.5/H/recognition and war/l
19.7 1 19.6/E/Bosnian war/h
20.b 1
20.0 1
20.1 1
20.2 1 16.5/H/Baltic independence/h
20.3 1 17.1/E/CIS founding/h
20.4 2 2.2/H/Czech-Slovak federation/l
21.b 1
21.0 2 10.1/E/INF Treaty/h ; 10.2/E/UN troop cuts/h ; 10.5/E/START I/h ; 8.7/H/economic failure/h
21.1 2 10.3/E/Afghanistan withdrawal/h
21.2 2 14.1/H/non-intervention/h ; 18.3/H/Germany in NATO/h ; 16.2/H/August coup/h
21.3 2 9.5/H/partly free elections/h ; 9.7/E/nationalism released/h ; 9.6/H/party monopoly/h
21.4 2 7.5/H/Western welcome/h ; 7.6/E/domestic criticism/h
21.5 2 7.7/E/Brown and Kotkin/h
21.6 2 0.4/H/Khrushchev's force in 1956/h ; 7.4/H/Gorbachev refusing force/h
22.b 1
22.0 2 0.5/H/command economy/h ; 0.7/H/arms race/h ; 14.4/H/Western prosperity on TV/h
22.1 1 14.1/H/non-intervention/h
22.2 2 5.4/H/Solidarity/h ; 3.5/H/Charter 77/h ; 14.3/H/domino effect/h
22.3 2 7.7/E/Kotkin and Brown/h
22.4 2 0.7/E/Reagan and SDI/h
22.5 2 1.1/H/1953/h ; 0.4/H/1956/h ; 2.6/H/1968/h ; 6.0/H/1981 martial law/h
'''
out={}
for ln in SPEC.strip().splitlines():
    head,*rest=ln.split(';',0) if False else [ln]
    parts=ln.split(' ',2)
    tid,cost=parts[0],int(parts[1])
    needs=[]
    if len(parts)>2:
        for n in parts[2].split(';'):
            i,s,w,c=n.strip().split('/')
            needs.append({"id":"hist-eur4-"+(i if i.startswith('s1') else 's4.'+i),"strength":"essential" if s=='E' else "helpful","why":w,"confidence":"high" if c=='h' else "low"})
    out['hist-eur4-s4.'+tid]={"cost":cost,"needs":needs}
txt=open(H+'packs/hist-eur4-s4.t1g1.txt').read()
tgt=[];cand=[]
sec=None
for l in txt.splitlines():
    if l.startswith('TARGET'):sec='t'
    elif l.startswith('CANDIDATES'):sec='c'
    m=re.match(r'\[(\S+)\]',l)
    if m:(tgt if sec=='t' else cand).append(m.group(1))
assert list(out)==tgt,(set(tgt)-set(out),set(out)-set(tgt))
allid=set(tgt)|set(cand)
for k,v in out.items():
    for n in v['needs']:
        assert n['id'] in allid and n['id']!=k,(k,n)
json.dump(out,open(H+'point-links/hist-eur4-s4.t1g1.json','w'),ensure_ascii=False,indent=0)
print(len(out),sum(len(v['needs']) for v in out.values()),sum(v['cost']==2 for v in out.values()),sum(n['confidence']=='low' for v in out.values() for n in v['needs']))
