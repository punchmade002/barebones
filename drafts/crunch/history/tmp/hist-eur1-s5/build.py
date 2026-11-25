import json,re
P='/Users/gabrielwhelan/barebones/.claude/worktrees/history-crunch/drafts/crunch/history/'
D='''
0.b|1|
0.0|1|
0.1|1|0.0,h,uses the Sultan and Orthodox Christians,H
0.2|1|0.1,e,uses the millet system,H
0.3|2|
0.4|2|0.0,h,Moldavia and Wallachia introduced,H
0.5|2|0.4,h,Russian expansion fears,L
0.6|1|0.5,h,Powers wanting different outcomes,L
1.b|1|
1.0|1|
1.1|1|0.3,h,uses the Janissaries,H
1.2|1|4.0,h,Philiki Etaireia explained there,H
1.3|1|s1.0.0,h,French Revolution spreading national ideas,H
1.4|1|0.4,h,Russia as Orthodox protector,H
1.5|1|
2.b|1|
2.0|1|0.3,h,uses the Janissaries,H
2.1|2|2.0,e,the First Serbian Uprising,H
2.2|1|2.1,h,follows the crushed first rising,H
2.3|2|2.2,h,Serbian risings behind the agreements,L
2.4|1|2.2,e,uses Miloš Obrenović,H;2.3,h,agreements granting autonomy,H
2.5|1|2.4,e,uses Serbian autonomy,H
3.b|1|
3.0|1|2.2,e,uses Miloš Obrenović,H;2.0,e,uses Karadjordje,H
3.1|1|3.0,h,uses Miloš's rule,H;s1.1.0,h,liberal constitution idea,L
3.2|2|3.0,e,uses Miloš as prince,H
3.3|2|3.2,e,follows Miloš and Mihailo,H
3.4|2|2.5,h,Ottoman garrisons and suzerainty,H
3.5|1|1.5,h,nationalism defined,L
3.6|1|2.4,e,uses Serbian autonomy under a prince,H
4.b|1|
4.0|1|
4.1|1|4.0,e,uses the Philiki Etaireia,H;0.0,h,Moldavia and the principalities,L
4.2|1|4.1,e,uses Ypsilantis rising,H
4.3|1|
4.4|1|4.3,h,the Peloponnese rising,H
4.5|1|0.1,h,uses the Patriarch,L
4.6|1|4.3,h,rising now claiming statehood,L
4.7|1|
5.b|1|4.5,h,uses the Chios massacre,H
5.0|1|
5.1|1|5.0,h,uses philhellenism,H
5.2|1|4.5,e,uses the Chios massacre,H;5.5,h,uses Missolonghi's fall,L
5.3|1|s1.19.b,h,uses Metternich,H;s1.8.3,h,uses the Congress of Verona,H
5.4|1|4.3,h,the Peloponnese rising,L
5.5|1|5.0,h,European sympathy for Greeks,L
6.b|1|
6.0|2|0.4,h,Russia protecting Orthodox Christians,H
6.1|1|6.0,h,begins joint approach,H
6.2|2|6.1,e,Navarino fought as a result,H
6.3|2|6.2,e,uses the battle of Navarino,H;5.4,h,uses Ibrahim,H
6.4|1|6.3,h,Greek settlement context,L
6.5|1|6.4,e,uses the Treaty of Adrianople,H
7.b|1|
7.0|1|
7.1|1|7.0,e,uses Kapodistrias,H
7.2|2|6.4,h,the Powers' settlement on Greece,L
7.3|1|7.2,h,follows Greek independence status,L
7.4|1|
7.5|1|7.3,e,uses King Otto,H
7.6|2|7.5,e,uses Otto's rule,H
7.7|1|7.3,e,uses King Otto,H
8.b|1|
8.0|2|0.6,h,France protector of Catholics,H;0.4,h,Russia protecting Orthodox,H
8.1|2|8.0,e,follows the Menshikov mission,H;0.0,h,Moldavia and Wallachia,L
8.2|2|8.1,h,continues the war narrative,H
8.3|2|8.2,h,ends the Crimean War,H
8.4|1|8.3,e,uses the Treaty of Paris,H;0.4,h,Russia's protectorate,L
8.5|1|8.3,e,uses the Black Sea clauses,H;16.0,h,emancipation after defeat,L
8.6|1|8.4,h,principalities under collective guarantee,L
8.7|1|8.6,e,uses Cuza and union,H
9.b|1|
9.0|1|0.5,h,Austrian and British interests,L
9.1|1|s1.7.3,e,uses the Congress System,H;s1.14.3,h,Metternich against Greek support,L
9.2|2|8.2,h,uses the Crimean War,H;6.4,h,uses the 1828-29 war,H
9.3|2|6.1,h,uses the Treaty of London,H;7.2,h,uses the London Protocol,H;8.3,h,uses the Treaty of Paris,H
9.4|2|2.5,h,Serbia autonomous but tributary,H;8.7,h,Romania status,H
9.5|1|
10.b|1|
10.0|1|
10.1|2|10.0,h,uses autocracy and Tsar,L
10.2|1|13.0,e,uses serfs,H;10.1,h,uses Alexander I,H
10.3|2|s1.4.3,h,Kingdom of Poland,H;s1.7.0,h,Holy Alliance,H;s1.7.3,h,Congress System,H
11.b|1|
11.0|1|
11.1|1|10.1,h,uses Alexander I,L
11.2|1|11.0,e,uses the Decembrists,H;11.1,h,succession confusion,H
11.3|2|11.2,e,uses the Senate Square revolt,H
11.4|1|11.3,h,uses the crushed revolt,H
12.b|1|
12.0|1|
12.1|1|
12.2|1|
12.3|1|10.1,h,uses Speransky,H
12.4|1|13.2,h,uses state peasants,H
12.5|2|s1.15.3,h,Polish rising of 1830-31,H
12.6|1|
13.b|1|
13.0|1|
13.1|1|13.0,h,uses serfs,H
13.2|1|13.0,e,uses serfs,H
13.3|1|13.0,h,uses serfdom,H
14.b|1|13.0,h,uses serfs and owners,H
14.0|1|13.0,e,uses serfs and landlords,H
14.1|1|14.0,h,contrast with barshchina,H
14.2|1|13.0,h,uses serfdom,H
14.3|1|
14.4|1|13.0,h,uses serfs,L
14.5|1|13.2,h,uses privately owned serfs,H
14.6|1|13.0,h,uses serf unrest,L
15.b|1|8.5,h,Crimean defeat triggering emancipation,L
15.0|1|13.1,h,cruelty of serf life,L
15.1|1|14.5,h,mortgaged noble estates,H
15.2|1|8.2,h,uses the Crimean War,H
15.3|1|8.2,h,uses the Crimean War,H
15.4|1|14.6,h,landlords fearing Pugachev,H
16.b|1|
16.0|1|8.2,e,uses the Crimean War and Sevastopol,H
16.1|1|16.0,h,Alexander II's motive,H
16.2|1|16.1,h,preparation for abolition,L
16.3|1|16.2,h,follows the drafting commissions,H
16.4|1|16.3,e,uses the 1861 edict,H
16.5|1|16.4,h,uses the emancipation terms,H
16.6|1|14.1,e,uses household serfs,H
17.b|1|16.5,h,uses allotments of land,L
17.0|1|16.4,h,uses emancipated peasants,H;14.1,h,uses obrok,L
17.1|1|17.0,e,uses redemption and obligation,H
17.2|2|17.0,e,uses redemption,H
17.3|1|17.2,e,uses redemption payments,H
17.4|1|16.5,h,uses land allotments,H
17.5|1|17.4,e,uses the mir,H
17.6|1|17.2,e,uses redemption payments,H
18.b|1|16.4,h,uses emancipation,H
18.0|1|16.5,h,uses land allotments,H
18.1|1|17.5,h,uses the mir tying peasants,H
18.2|1|17.2,h,uses compensation to landlords,L
18.3|1|16.1,h,emancipation from above,H
18.4|2|18.3,h,reforms following emancipation,L
18.5|1|18.4,h,follows the zemstva reforms,L
19.b|1|
19.0|2|2.4,e,uses Serbian autonomy,H;7.2,e,uses Greek independence,H;8.6,e,uses Romanian union,H
19.1|1|9.4,h,uses limits of Balkan achievement,H
19.2|2|6.2,h,uses Navarino,H;9.2,h,uses the wars as threat,H;9.3,h,uses Power co-operation,H
19.3|1|16.4,e,uses emancipation,H
19.4|1|17.3,e,uses redemption debt,H;17.4,h,uses the mir,H
19.5|1|17.3,h,peasant grievance over land,L
19.6|1|19.0,h,Balkan summary,H;19.3,h,emancipation as major reform,H
'''
out={}
for l in D.strip().split('\n'):
    k,c,n=l.split('|')
    k='hist-eur1-s5.'+k
    needs=[]
    for x in filter(None,re.split(r';(?=s?\d)',n)):
        # entries separated by ';' ; fields by ','
        pass
    out[k]={'cost':int(c),'needs':needs}
    for x in filter(None,n.split(';')):
        parts=x.split(',')
        if len(parts)<4: raise SystemExit('bad '+l)
        i=parts[0]; i=i if i.startswith('s1.') else 'eur1-s5.'+i
        i='hist-'+(i.replace('s1.','eur1-s1.',1) if i.startswith('s1.') else i)
        needs.append({'id':i,'strength':'essential' if parts[1]=='e' else 'helpful','why':','.join(parts[2:-1]),'confidence':'high' if parts[-1]=='H' else 'low'})
# validate
txt=open(P+'packs/hist-eur1-s5.t1g1.txt').read()
tg=txt.split('CANDIDATES')[0]
tids=re.findall(r'^\[(hist-[^\]]+)\]',tg,re.M)
allids=set(re.findall(r'^\[(hist-[^\]]+)\]',txt,re.M))
assert list(out)==tids,(set(tids)-set(out),set(out)-set(tids))
for k,v in out.items():
    for n in v['needs']:
        assert n['id'] in allids and n['id']!=k,(k,n)
json.dump(out,open(P+'point-links/hist-eur1-s5.t1g1.json','w'),indent=1)
print(len(out),sum(len(v['needs']) for v in out.values()),sum(v['cost']==2 for v in out.values()),sum(n['confidence']=='low' for v in out.values() for n in v['needs']))
