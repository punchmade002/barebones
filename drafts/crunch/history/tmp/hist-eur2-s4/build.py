import json,re,sys
B='/Users/gabrielwhelan/barebones/.claude/worktrees/history-crunch/drafts/crunch/history/'
E,H='e','h'
# link tuple: (id-suffix, strength e/h, why, conf H/L); ids: "4.1" -> s4 ; "s2:2.2" -> s2
def L(t):
    i,s,w,c=t
    pre='hist-eur2-s2.' if i.startswith('s2:') else 'hist-eur2-s4.'
    if i.startswith('s2:'): i=i[3:]
    return {"id":pre+i,"strength":"essential" if s=='e' else "helpful","why":w,"confidence":"high" if c=='H' else "low"}
def lk(*a): return [L(t) for t in a]
P1={
"0.b":(1,[]),"0.0":(1,[]),"0.1":(1,[]),"0.2":(1,[]),
"0.3":(1,lk(("s2:3.3",'h',"Triple Entente and Alliance formed",'L'))),
"0.4":(1,lk(("s2:9.6",'h',"Russo-Japanese War defeat",'H'))),
"1.b":(1,[]),"1.0":(1,[]),
"1.1":(1,lk(("1.0",'h',"same Congress of Berlin",'H'))),
"1.2":(1,[]),"1.3":(1,[]),
"1.4":(1,lk(("1.3",'e',"South Slav unity aim",'H'),("0.1",'h',"multinational Austria-Hungary",'H'))),
"2.b":(1,[]),"2.0":(1,[]),
"2.1":(1,lk(("2.0",'e',"1903 coup and new dynasty",'H'))),
"2.2":(1,lk(("0.2",'h',"Pan-Slavism protector role",'H'))),
"2.3":(2,lk(("1.2",'e',"Serbia's livestock export dependence",'H'))),
"2.4":(1,lk(("2.3",'e',"the Pig War",'H'))),
"2.5":(1,lk(("1.4",'h',"Slavs threatening empire",'H'))),
"2.6":(2,lk(("2.2",'e',"Russia as Serbia's protector",'H'),("0.3",'e',"alliance blocs",'H'))),
"3.b":(1,lk(("1.1",'h',"Austrian occupation of Bosnia",'H'))),
"3.0":(1,lk(("1.1",'e',"occupation of Bosnia 1878",'H'))),
"3.1":(2,lk(("3.0",'h',"Bosnia's status",'H'),("2.2",'h',"Russia and the Straits",'H'))),
"3.2":(1,lk(("3.1",'e',"the Buchlau bargain",'H'))),
"3.3":(1,lk(("3.2",'e',"the annexation",'H'))),
"3.4":(1,lk(("3.2",'e',"the annexation",'H'),("0.4",'h',"Russia weak after Japan war",'H'))),
"3.5":(2,lk(("3.4",'e',"Russia and Serbia giving way",'H'))),
"3.6":(1,lk(("3.4",'e',"Germany backing Austria 1909",'H'))),
"4.b":(1,[]),
"4.0":(1,lk(("s2:3.4",'h',"Italy's Libya war",'H'))),
"4.1":(1,lk(("4.0",'e',"the Balkan League",'H'))),
"4.2":(1,lk(("4.1",'h',"First Balkan War outcome",'H'))),
"4.3":(2,lk(("4.0",'e',"the Balkan League",'H'))),
"4.4":(1,lk(("4.1",'e',"First Balkan War gains",'H'),("4.3",'e',"Treaty of Bucharest",'H'))),
"4.5":(2,lk(("4.2",'e',"Albania and Adriatic port",'H'),("2.5",'h',"Conrad's push for war",'H'))),
"4.6":(1,lk(("4.5",'h',"Austrian conclusion on war",'L'))),
"5.b":(1,[]),
"5.0":(2,lk(("2.0",'h',"Apis in 1903 coup",'H'))),
"5.1":(1,lk(("5.0",'e',"Black Hand aid",'H'))),
"5.2":(1,lk(("5.0",'e',"the Black Hand",'H'),("3.3",'e',"Narodna Odbrana",'H'),("5.1",'e',"Young Bosnia",'H'))),
"5.3":(1,[]),
"5.4":(2,lk(("5.3",'e',"the Sarajevo visit",'H'),("5.1",'h',"Princip's group",'H'))),
"5.5":(1,lk(("5.4",'e',"Princip's assassination",'H'))),
"5.6":(1,lk(("5.0",'e',"the Black Hand",'H'),("5.4",'h',"the assassination weapons",'H'))),
"5.7":(2,lk(("5.4",'e',"the assassination",'H'))),
"6.b":(1,[]),
"6.0":(2,lk(("5.7",'e',"Hoyos mission to Berlin",'H'))),
"6.1":(1,lk(("s2:1.2",'h',"Franco-Russian alliance terms",'H'))),
"6.2":(2,lk(("5.7",'h',"Austria's decision to crush Serbia",'H'))),
"6.3":(1,lk(("6.2",'e',"the ultimatum",'H'))),
"6.4":(1,lk(("6.3",'h',"Serbia's reply to ultimatum",'L'))),
"6.5":(1,lk(("6.3",'e',"breaking off relations",'H'))),
"7.b":(1,[]),
"7.0":(2,lk(("6.5",'h',"Austria declaring war on Serbia",'H'))),
"7.1":(1,lk(("7.0",'e',"Russian mobilisation",'H'))),
"7.2":(2,lk(("s2:1.5",'h',"two-front war danger",'H'))),
"7.3":(1,lk(("7.2",'e',"the Schlieffen Plan",'H'),("7.0",'e',"Russian mobilisation",'H'))),
"7.4":(1,lk(("7.3",'e',"attack through Belgium",'H'))),
"7.5":(2,lk(("7.4",'e',"invasion of Belgium",'H'),("s2:2.5",'h',"Entente with France",'H'))),
"7.6":(1,lk(("7.5",'e',"the 1839 treaty",'H'))),
"7.7":(1,lk(("s2:3.4",'h',"Italy's unreliability in alliance",'H'))),
"8.b":(1,[]),"8.0":(1,[]),"8.1":(1,[]),
"8.2":(2,lk(("8.1",'e',"the Second International",'H'),("8.0",'h',"SPD and Marxism",'H'))),
"8.3":(2,lk(("8.0",'e',"Marxism and the SPD",'H'),("8.2",'h',"SPD members and parties",'H'))),
"8.4":(1,lk(("8.2",'e',"Jaures, SPD, International members",'H'))),
"8.5":(2,lk(("8.4",'h',"debate on stopping war",'H'))),
"8.6":(1,lk(("4.1",'h',"First Balkan War",'H'))),
"9.b":(1,[]),
"9.0":(1,lk(("8.1",'e',"International Socialist Bureau",'H'),("8.4",'h',"Jaures' general strike",'H'))),
"9.1":(2,lk(("8.2",'e',"the SPD",'H'))),
"9.2":(1,lk(("8.2",'h',"French and British socialists",'H'))),
"9.3":(2,lk(("9.1",'e',"SPD vote for war credits",'H'),("9.2",'h',"French and British socialist support",'H'),("8.4",'h',"no agreed anti-war plan",'H'))),
"9.4":(1,lk(("8.3",'h',"revolutionary Marxists",'H'))),
"9.5":(1,lk(("9.4",'e',"the anti-war minority",'H'))),
"10.b":(1,[]),"10.0":(1,[]),
"10.1":(2,lk(("8.0",'h',"SPD and class-first Marxism",'H'))),
"10.2":(2,lk(("8.3",'e',"Bernstein's revisionism",'H'))),
"10.3":(1,lk(("8.5",'e',"Stuttgart Congress resolution",'H'))),
"10.4":(1,lk(("9.1",'e',"SPD vote for war credits",'H'))),
"10.5":(2,lk(("9.4",'h',"revolutionary anti-war minority",'L'))),
"10.6":(2,lk(("10.2",'h',"her view on mass action",'L'),("10.5",'h',"Spartacus group",'L'))),
"10.7":(2,lk(("10.6",'h',"KPD and January rising",'H'))),
"11.b":(1,[]),
"11.0":(1,lk(("0.3",'e',"the two blocs",'H'))),
"11.1":(1,lk(("7.2",'e',"the Schlieffen Plan",'H'))),
"11.2":(1,lk(("s2:12.b",'h',"Moroccan crises",'H'))),
"11.3":(2,lk(("1.3",'e',"South Slav nationalism",'H'),("0.2",'e',"pan-Slavism",'H'),("s2:0.0",'h',"revanche and Alsace-Lorraine",'H'))),
"11.4":(2,lk(("3.2",'h',"Bosnian crisis",'H'),("4.1",'h',"Balkan Wars",'H'),("5.4",'h',"Sarajevo assassination",'H'),("6.0",'h',"blank cheque",'H'),("6.2",'h',"the ultimatum",'H'),("7.0",'h',"the mobilisations",'H'),("7.4",'h',"invasion of Belgium",'H'))),
"11.5":(1,lk(("0.0",'e',"Austro-Russian Balkan rivalry",'H'),("4.6",'h',"neither could give way",'L'))),
"12.b":(1,[]),
"12.0":(1,lk(("6.2",'e',"the ultimatum",'H'),("1.4",'h',"Slav nationalism threat",'H'))),
"12.1":(1,lk(("6.0",'e',"the blank cheque",'H'),("7.2",'e',"the Schlieffen Plan",'H'))),
"12.2":(1,lk(("3.5",'e',"humiliation of 1909",'H'))),
"12.3":(1,lk(("6.1",'e',"the July visit to Russia",'H'),("7.1",'h',"mobilisation",'H'))),
"12.4":(1,lk(("7.5",'e',"Belgium and Entente",'H'))),
"12.5":(1,lk(("6.3",'e',"Serbia's reply to ultimatum",'H'))),
"13.b":(1,[]),
"13.0":(2,lk(("7.0",'e',"Russian mobilisation",'H'),("6.0",'h',"the blank cheque",'H'))),
"13.1":(1,[]),
"13.2":(2,lk(("13.0",'h',"German war guilt debate",'H'))),
"13.3":(2,lk(("13.2",'h',"Fischer's opposing view",'L'))),
"13.4":(2,lk(("5.7",'e',"Austria's decision against Serbia",'H'),("6.0",'e',"German backing",'H'),("7.2",'e',"military planning",'H'),("1.3",'h',"Serbian nationalism",'H'),("2.2",'h',"Russian backing of Serbia",'H'))),
"13.5":(2,lk(("8.5",'e',"Stuttgart resolution",'H'),("8.6",'h',"Basel manifesto",'H'),("9.3",'e',"why the International failed",'H'))),
"13.6":(2,lk(("10.6",'e',"Luxemburg and KPD",'H'),("10.7",'e',"her murder",'H'))),
}
def s1(i,s,w,c): return {"id":"hist-eur2-s1."+i,"strength":"essential" if s=='e' else "helpful","why":w,"confidence":"high" if c=='H' else "low"}
P2={k:[] for k in P1}
P2.update({
"0.3":[s1("9.4",'h',"Triple Alliance of 1882",'H')],
"1.0":[s1("8.0",'h',"Congress of Berlin",'H')],
"1.1":[s1("8.3",'e',"Austria allowed to occupy Bosnia",'H')],
"2.2":[s1("0.4",'h',"the Straits",'H')],
"3.0":[s1("8.3",'h',"Bosnia occupation 1878",'H')],
"7.2":[s1("5.2",'h',"two-front war fear",'H')],
"7.7":[s1("9.5",'h',"defensive Triple Alliance terms",'H')],
"8.0":[s1("3.4",'h',"the SPD",'H')],
"8.2":[s1("3.4",'h',"the SPD",'H')],
"9.1":[s1("1.6",'h',"Reichstag's role",'L')],
"11.0":[s1("9.4",'h',"Triple Alliance",'H')],
"11.1":[s1("5.2",'h',"two-front war",'H')],
"12.1":[s1("5.2",'h',"two-front war fear",'H')],
})
def ids(f):
    t=open(f).read().split('CANDIDATES')
    return re.findall(r'^\[(\S+)\]',t[0],re.M),set(re.findall(r'^\[(\S+)\]',t[0]+t[1],re.M))
for n,P in((1,P1),(2,P2)):
    f=B+f'packs/hist-eur2-s4.t1g{n}.txt'; tg,allids=ids(f)
    out={}
    for t in tg:
        k=t.replace('hist-eur2-s4.','')
        if n==1: c,nd=P[k]; out[t]={"cost":c,"needs":nd}
        else: out[t]={"needs":P[k]}
    assert list(out)==tg,(set(tg)^set(out))
    for v in out.values():
        for x in v['needs']: assert x['id'] in allids and x['id']!=t,x
    # self-link & verify
    for t,v in out.items():
        assert all(x['id']!=t for x in v['needs']),t
    json.dump(out,open(B+f'point-links/hist-eur2-s4.t1g{n}.json','w'),ensure_ascii=False,indent=0)
    nl=sum(len(v['needs']) for v in out.values()); lo=sum(x['confidence']=='low' for v in out.values() for x in v['needs'])
    print(n,len(out),nl,sum(v.get('cost')==2 for v in out.values()),lo)
