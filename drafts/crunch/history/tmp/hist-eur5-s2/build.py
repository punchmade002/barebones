import json,re
D='/Users/gabrielwhelan/barebones/.claude/worktrees/history-crunch/drafts/crunch/history/'
def build(pack,out,pre,E):
    txt=open(D+'packs/'+pack).read()
    sec=txt.split('CANDIDATES')[0]
    targets=re.findall(r'^\[([^\]]+)\]',sec,re.M)
    allids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
    res={};seen=set()
    for k,c,links in E:
        tid=pre+k
        assert tid in targets and tid not in seen,tid
        seen.add(tid)
        needs=[]
        for t,s,w in links:
            lid=t if t.startswith('hist-') else {'s2':'hist-eur5-s2','s1':'hist-eur5-s1','s8':'hist-ire6-s8','s3':'hist-ire6-s3','r1':'hist-ire6-s1'}[t.split('.')[0]]+'.'+t.split('.',1)[1]
            assert lid in allids and lid!=tid,(tid,lid)
            low=s.endswith('?')
            needs.append({"id":lid,"strength":"essential" if s[0]=='e' else "helpful","why":w,"confidence":"low" if low else "high"})
        res[tid]={"cost":c,"needs":needs}
    assert seen==set(targets),set(targets)-seen
    json.dump(res,open(D+'point-links/'+out,'w'),indent=1,ensure_ascii=False)
    n=sum(len(v['needs']) for v in res.values())
    print(out,len(res),n,sum(v['cost']==2 for v in res.values()),sum(l['confidence']=='low' for v in res.values() for l in v['needs']))
E1=[
("0.b",1,[]),("0.0",1,[]),("0.1",1,[("s2.0.0","h","uses colonial rule")]),("0.2",1,[]),
("0.3",2,[("s2.2.2","h","Ho Chi Minh and the Viet Minh")]),
("1.b",1,[]),("1.0",2,[]),("1.1",1,[("s2.1.0","h","the Indochinese federation")]),
("1.2",1,[("s2.1.0","h","regions of the federation")]),("1.3",1,[]),
("1.4",1,[("s2.1.0","h","Indochinese Federation of 1887"),("s2.3.3","h","French Union of 1946")]),
("2.b",1,[]),("2.0",1,[]),("2.1",1,[("s2.2.0","h","Japanese presence in Indochina")]),
("2.2",2,[]),("2.3",1,[("s2.2.2","h","the Viet Minh")]),("2.4",1,[]),
("2.5",1,[("s2.2.2","e","the Viet Minh"),("s2.1.3","h","emperor kept as figurehead")]),
("3.b",1,[]),("3.0",1,[("s2.2.2","h","Ho and the Viet Minh")]),("3.1",1,[]),
("3.2",2,[("s2.3.0","e","the Democratic Republic"),("s2.1.2","h","status of Cochinchina"),("s2.3.3","e","the French Union")]),
("3.3",1,[]),("3.4",1,[("s2.3.3","e","the French Union")]),
("4.b",1,[]),("4.0",1,[("s2.3.2","h","the March 1946 agreement")]),("4.1",1,[]),
("4.2",1,[("s2.2.2","h","the Viet Minh")]),("4.3",1,[]),
("5.b",1,[]),("5.0",1,[("s2.2.5","h","Bao Dai's abdication"),("s2.3.0","h","the Democratic Republic")]),
("5.1",1,[("s2.5.0","e","the State of Vietnam of 1949"),("s2.3.0","e","the Democratic Republic")]),
("5.2",1,[("s2.2.2","h","the Viet Minh")]),("5.3",1,[("s2.0.3","h","Cold War view of Vietnam")]),
("5.4",1,[("s2.3.0","h","Ho's government in the north")]),
("6.b",1,[]),("6.0",1,[("s2.2.2","h","the Viet Minh")]),("6.1",1,[("s2.6.0","h","Dien Bien Phu battle")]),
("6.2",1,[("s2.2.2","h","Giap and the Viet Minh")]),("6.3",1,[]),("6.4",1,[("s2.7.0","h","the Geneva Conference")]),
("7.b",1,[]),("7.0",1,[("s2.6.3","h","French defeat at Dien Bien Phu","l")]),
("7.1",1,[("s2.7.0","h","the Geneva Conference")]),("7.2",1,[("s2.7.1","h","the Geneva Accords")]),
("7.3",1,[("s2.7.1","e","the Geneva Accords")]),
("8.b",1,[]),("8.0",1,[("s2.7.1","e","elections planned at Geneva")]),
("8.1",1,[("s2.7.1","h","the South after division")]),("8.2",1,[("s2.7.1","h","the South after Geneva")]),
("8.3",1,[("s2.7.1","h","the North after division")]),("8.4",1,[]),
("9.b",1,[]),("9.0",1,[("s2.1.0","h","Cambodia in Indochina")]),("9.1",1,[("s2.7.2","h","Geneva and Laos, Cambodia")]),
("9.2",1,[("s2.2.2","h","the Viet Minh")]),
("10.b",1,[]),("10.0",1,[]),("10.1",1,[("s2.10.0","h","Japanese occupation")]),
("10.2",1,[("s2.10.0","h","Japanese occupation")]),("10.3",1,[("s2.10.2","h","Sukarno as nationalist")]),
("10.4",1,[("s2.10.2","h","Sukarno and Hatta")]),("10.5",1,[("s2.10.4","e","the proclamation")]),
("10.6",1,[("s2.10.4","h","the Republic")]),
("11.b",1,[]),("11.0",2,[("s2.10.4","h","the Republic")]),("11.1",1,[("s2.11.0","e","the Linggadjati Agreement")]),
("11.2",1,[("s2.11.1","h","dispute over Linggadjati")]),("11.3",1,[("s2.11.2","e","the first police action")]),
("11.4",1,[("s2.11.3","h","UN Good Offices Committee")]),
("12.b",1,[]),("12.0",1,[("s2.10.4","h","the Republic")]),("12.1",1,[("s2.11.2","e","the first police action")]),
("12.2",1,[("s2.12.1","e","the second police action")]),("12.3",1,[("s2.12.1","h","the second police action")]),
("13.b",1,[]),("13.0",1,[("s2.12.3","h","pressure leading to talks")]),("13.1",1,[("s2.13.0","h","settlement terms")]),
("13.2",1,[("s2.13.1","h","sovereignty transfer")]),("13.3",1,[("s2.13.0","h","the Hague settlement")]),
("13.4",1,[("s2.13.0","h","the Hague settlement")]),
("14.b",1,[]),("14.0",1,[]),("14.1",1,[("s2.0.3","h","Cold War blocs"),("s2.14.0","h","the Bandung conference")]),
("14.2",1,[("s2.14.0","h","the Bandung conference")]),
("15.b",1,[]),("15.0",2,[]),("15.1",1,[]),("15.2",1,[("s2.15.1","e","the regional rebellions")]),
("16.b",1,[]),("16.0",1,[("s2.15.0","h","unstable parliamentary government")]),
("16.1",1,[("s2.16.0","h","Guided Democracy")]),("16.2",1,[("s2.16.0","h","Sukarno's rule")]),
("16.3",1,[("s2.15.0","h","the PKI as a party")]),
("17.b",1,[]),("17.0",1,[]),("17.1",1,[("s2.13.3","e","West New Guinea left open")]),
("17.2",1,[("s2.17.1","e","West New Guinea transfer")]),
("18.b",1,[]),("18.0",1,[]),("18.1",1,[("s2.18.0","h","isolation after Konfrontasi","l")]),
("19.b",1,[]),("19.0",1,[("s2.18.0","h","cost of Konfrontasi")]),("19.1",1,[("s2.16.3","h","army and PKI rivalry")]),
("19.2",1,[("s2.19.1","e","the coup attempt")]),("19.3",1,[("s2.19.1","e","the coup attempt and Suharto")]),
("19.4",1,[("s2.19.3","h","Sukarno stripped of power")]),
("20.b",1,[]),("20.0",2,[("s2.15.0","h","instability after 1955 election"),("s2.15.1","h","PRRI and Permesta"),("s2.19.1","h","coup attempt 1965"),("s2.19.0","h","economic decline")]),
("20.1",2,[("s2.17.1","h","West New Guinea dispute"),("s2.18.0","h","Konfrontasi"),("s2.18.1","h","leaving the UN")]),
("21.b",1,[]),("21.0",2,[]),("21.1",2,[]),
("21.2",2,[("s2.2.2","e","founding the Viet Minh"),("s2.2.5","h","the August Revolution"),("s2.3.0","h","proclaiming the Democratic Republic")]),
("21.3",1,[("s2.4.2","e","the war against France"),("s2.2.2","h","Giap and the Viet Minh")]),
("21.4",2,[("s2.2.1","h","Japan broke French rule"),("s2.4.2","h","French attempt to return")]),
("21.5",1,[]),("21.6",1,[]),
("21.7",1,[("s2.8.3","h","North Vietnam under Lao Dong"),("s2.7.1","h","the 1954 division")]),
("22.b",1,[]),("22.0",2,[]),("22.1",1,[("s2.10.2","h","Japanese platform for nationalists")]),
("22.2",1,[("s2.10.3","e","the Pancasila speech"),("s2.10.4","e","the proclamation")]),
("22.3",1,[("s2.16.3","h","the PKI and the army")]),
("22.4",2,[("s2.19.1","e","the coup attempt and Suharto"),("s2.19.3","e","the Supersemar order")]),
("22.5",2,[("s2.22.1","h","collaboration with Japan")]),
("22.6",2,[("s2.16.0","h","Guided Democracy"),("s2.18.0","h","confrontation policy")]),
("22.7",1,[("s2.10.1","h","Japanese-trained forces")]),
("23.b",1,[]),("23.0",2,[("s2.6.3","h","Dien Bien Phu defeat"),("s2.11.2","h","first police action"),("s2.12.3","h","US pressure on the Dutch")]),
("23.1",1,[("s2.8.3","e","Lao Dong Party state")]),
("23.2",2,[("s2.16.1","h","balancing Nasakom"),("s2.19.3","h","collapse in 1965-66")]),
("23.3",1,[("s2.21.5","e","views of Ho"),("s2.22.5","e","views of Sukarno")]),
("24.b",1,[]),("24.0",1,[("s2.13.1","h","Indonesian sovereignty 1949"),("s2.6.3","h","Viet Minh victory 1954")]),
("24.1",1,[("s2.12.3","h","US pressure on the Dutch")]),("24.2",1,[("s2.14.2","h","Sukarno at Bandung")]),
("24.3",1,[("s2.11.2","h","Dutch police actions"),("s2.7.1","h","Geneva settlement")]),
("24.4",1,[("s2.7.1","e","division at Geneva"),("s2.8.0","h","elections never held")]),
("24.5",2,[("s2.16.0","h","Guided Democracy"),("s2.19.1","h","1965 coup"),("s2.19.2","h","the killings")]),
("24.6",1,[("s2.7.1","h","Vietnam divided"),("s2.16.0","h","authoritarian rule")]),
("24.7",1,[("s2.22.7","h","Anderson's argument")]),
]
# fix tuples with 4th element 'l' meaning low
E1=[(k,c,[(t,(s+'?') if len(x)>3 else s,w) for x in l for (t,s,w) in [x[:3]]]) for k,c,l in E1]
build('hist-eur5-s2.t1g1.txt','hist-eur5-s2.t1g1.json','hist-eur5-s2.',E1)

E2=[
("0.b",1,[]),("0.0",1,[]),("0.1",1,[]),("0.2",1,[("r1.8.1","h","1950s emigration")]),
("0.3",2,[]),("0.4",1,[]),("0.5",1,[("s3.0.0","h","equality of opportunity")]),
("1.b",1,[]),("1.0",2,[]),("1.1",2,[]),("1.2",2,[]),("1.3",1,[]),("1.4",1,[]),
("2.b",1,[]),("2.0",1,[("r1.8.1","h","1950s net emigration")]),("2.1",1,[]),("2.2",2,[]),("2.3",1,[]),("2.4",1,[]),("2.5",1,[]),
("3.b",1,[]),("3.0",1,[]),("3.1",1,[]),("3.2",1,[]),("3.3",1,[]),
("3.4",1,[("s8.6.4","h","contraception legalised late 1970s")]),
("4.b",1,[]),("4.0",1,[]),("4.1",1,[("s8.4.0","e","the marriage bar")]),("4.2",1,[]),("4.3",1,[]),
("4.4",2,[("s8.4.3","e","the Commission on the Status of Women")]),
("4.5",1,[("s8.4.4","e","the Commission's reports")]),
("5.b",1,[]),("5.0",2,[]),("5.1",2,[("s8.5.0","h","the movement that wrote it")]),
("5.2",2,[("s8.0.3","e","the contraception ban")]),
("5.3",1,[("s8.5.2","e","the train protest")]),("5.4",1,[]),("5.5",1,[]),
("6.b",1,[]),("6.0",1,[]),("6.1",2,[("s8.6.0","e","Mary McGee's case")]),
("6.2",1,[("s8.6.1","e","the McGee ruling")]),("6.3",1,[("s8.6.1","h","McGee ruling prompted a bill")]),
("6.4",2,[("s8.6.2","h","sale still restricted after McGee")]),
("6.5",1,[("s8.6.4","e","the 1979 Act")]),("6.6",1,[("s8.0.3","h","1968 papal encyclical")]),
("7.b",1,[]),("7.0",1,[("s8.0.2","h","EEC membership")]),("7.1",1,[("s8.0.4","h","definition of discrimination")]),
("7.2",1,[("s8.7.1","e","the 1977 Act")]),("7.3",1,[]),("7.4",1,[]),("7.5",1,[]),
("7.6",1,[("s8.0.2","h","EEC membership")]),
("8.b",1,[]),("8.0",1,[]),("8.1",1,[]),("8.2",1,[("s8.5.0","h","Nuala Fennell as activist")]),("8.3",1,[]),
("8.4",1,[("s8.10.1","h","Robinson in the Seanad")]),
("9.b",1,[]),("9.0",1,[]),("9.1",1,[("s8.7.2","e","the Employment Equality Agency")]),
("9.2",1,[("s8.7.0","h","equal pay law"),("s8.7.1","h","equal treatment law")]),
("9.3",1,[("s8.7.2","h","the agency's role")]),("9.4",1,[("s8.9.2","h","her agency work")]),
("9.5",1,[("s8.7.2","h","the agency's limited powers")]),
("10.b",1,[]),("10.0",2,[]),("10.1",1,[("s8.7.3","h","Juries Act 1976")]),
("10.2",1,[("s8.0.3","h","contraception ban")]),("10.3",1,[]),("10.4",2,[]),
("10.5",2,[("s8.10.3","e","Robinson's homosexuality reform work")]),
("10.6",1,[]),("10.7",1,[]),("10.8",1,[]),
("11.b",1,[]),
("11.0",2,[("s8.4.1","h","marriage bar ended"),("s8.7.0","h","equal pay"),("s8.7.1","h","employment equality"),("s8.6.4","h","contraception available")]),
("11.1",2,[("s8.8.0","h","women scarce in politics"),("s8.4.2","h","pay gaps")]),
("11.2",1,[]),("11.3",2,[("s8.0.2","h","EEC law")]),
]
E2=[(k,c,[(t,(s+'?') if len(x)>3 else s,w) for x in l for (t,s,w) in [x[:3]]]) for k,c,l in E2]
build('hist-ire6-s8.t1g1.txt','hist-ire6-s8.t1g1.json','hist-ire6-s8.',E2)
