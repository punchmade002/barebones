import json,re
H='/Users/gabrielwhelan/barebones/drafts/crunch/history/'
def L(i,s,w,c='high'): return {"id":i,"strength":s,"why":w,"confidence":c}
E,H_='essential','helpful'
p='hist-eur5-s2.'
def X(k,*a): return L(p+k,*a)
P={
"0.b":(1,[L("hist-eur5-s1.0.4",H_,"Japanese takeover of Indochina")]),
"0.0":(2,[]),
"0.1":(2,[X("0.0",H_,"the Indochina territories")]),
"0.2":(1,[L("hist-eur5-s1.0.4",H_,"Japanese control of Indochina")]),
"0.3":(1,[]),
"0.4":(1,[]),
"0.5":(1,[X("0.3",H_,"uses the Viet Minh")]),
"0.6":(1,[X("0.3",H_,"uses the Viet Minh")]),
"1.0":(1,[X("0.5",H_,"follows the August 1945 seizure of power")]),
"1.1":(2,[X("0.2",H_,"Japanese occupation and surrender")]),
"1.2":(2,[X("1.0",E,"uses the Democratic Republic"),X("1.3",H_,"free state within French Union")]),
"1.3":(1,[]),
"1.4":(1,[X("1.2",H_,"failure of the 1946 agreement")]),
"1.5":(2,[X("1.2",H_,"the March 1946 agreement")]),
"1.6":(1,[]),
"2.b":(1,[X("1.4",H_,"the First Indochina War")]),
"2.0":(1,[X("1.0",H_,"the Democratic Republic as rival")]),
"2.1":(2,[X("1.4",H_,"the First Indochina War")]),
"2.2":(2,[X("2.1",H_,"Chinese and American backing")]),
"2.3":(2,[X("2.2",E,"Navarre's fortified valley")]),
"2.4":(2,[X("2.3",H_,"the defeat that led to Geneva")]),
"2.5":(2,[X("2.4",E,"uses the Geneva division")]),
"2.6":(2,[]),
"2.7":(2,[X("2.3",E,"the siege of Dien Bien Phu")]),
"2.8":(1,[X("2.4",E,"the Geneva division of Vietnam")]),
"2.9":(2,[X("2.4",H_,"northern government after division",'low')]),
"3.b":(1,[L("hist-eur5-s1.0.3",H_,"fall of the Dutch East Indies")]),
"3.0":(2,[L("hist-eur5-s1.0.3",H_,"Japanese conquest of the East Indies")]),
"3.1":(1,[X("3.0",H_,"the Japanese occupation")]),
"3.2":(1,[X("3.1",H_,"Sukarno under Japanese rule")]),
"3.3":(1,[X("3.1",H_,"Sukarno and Hatta")]),
"3.4":(2,[X("3.3",H_,"the independence proclamation")]),
"4.0":(2,[X("3.3",H_,"the Republic of Indonesia")]),
"4.1":(1,[X("4.0",E,"the Linggadjati Agreement")]),
"4.2":(2,[X("4.1",E,"the first police action")]),
"4.3":(2,[X("4.2",H_,"the Renville settlement")]),
"4.4":(1,[X("4.3",H_,"the second police action")]),
"4.5":(1,[X("4.3",H_,"the second police action")]),
"4.6":(1,[X("4.5",H_,"transfer of sovereignty")]),
"4.7":(1,[X("4.3",H_,"the second police action")]),
"4.8":(2,[X("4.5",E,"the Hague conference")]),
"4.9":(1,[X("4.5",E,"the 1949 Union settlement")]),
"5.0":(1,[]),
"5.1":(1,[X("4.8",H_,"Dutch businesses left after 1949")]),
"5.2":(1,[X("3.3",H_,"the 1945 constitution",'low')]),
"5.3":(1,[]),
"5.4":(1,[X("4.6",E,"West New Guinea dispute")]),
"5.5":(1,[X("5.3",H_,"Indonesian hostility to Malaysia")]),
"5.6":(2,[X("5.10",H_,"the PKI and army rivalry")]),
"5.7":(2,[X("5.6",E,"the 1965 coup and Suharto")]),
"5.8":(2,[]),
"5.9":(2,[X("5.8",H_,"unstable politics after 1955")]),
"5.10":(2,[X("5.2",H_,"Guided Democracy rule")]),
"5.11":(1,[X("5.3",E,"cost of Konfrontasi")]),
"6.b":(1,[]),
"6.0":(2,[]),
"6.1":(1,[]),
"6.2":(1,[]),
"6.3":(1,[X("1.0",E,"proclaiming the Democratic Republic")]),
"6.4":(1,[]),
"6.5":(1,[]),
"6.6":(1,[]),
"6.7":(2,[X("0.3",E,"the Viet Minh he founded")]),
"6.8":(1,[X("2.4",E,"the 1954 division of Vietnam")]),
"7.b":(1,[]),
"7.0":(1,[]),
"7.1":(1,[X("7.0",H_,"the PNI he founded")]),
"7.2":(1,[X("3.0",H_,"the Japanese occupation")]),
"7.3":(1,[X("3.3",E,"the 17 August proclamation")]),
"7.4":(2,[X("7.2",H_,"accusations of collaboration")]),
"7.5":(2,[X("5.2",E,"Guided Democracy")]),
"7.6":(1,[X("5.10",E,"the PKI under Sukarno")]),
"7.7":(1,[X("3.2",E,"the Pancasila speech")]),
"8.0":(2,[X("4.5",E,"Indonesia's 1949 success")]),
"8.1":(1,[X("2.4",E,"the 1954 division of Vietnam")]),
"8.2":(2,[X("4.4",H_,"UN and US pressure")]),
"8.3":(2,[X("4.1",H_,"the Dutch police actions")]),
"8.4":(1,[X("5.0",E,"the Bandung Conference")]),
"8.5":(2,[X("5.6",E,"the 1965 coup and killings")]),
"8.6":(1,[X("3.1",H_,"pemuda trained under the Japanese")]),
"8.7":(1,[X("2.4",H_,"Vietnam's 1954 division")]),
}
P={p+k:v for k,v in P.items()}
pk,out='hist-eur5-s2.t1g1.txt','hist-eur5-s2.t1g1.json'
txt=open(H+'packs/'+pk).read()
ids=[];tg=True
for ln in txt.split('\n'):
    if ln.startswith('CANDIDATES'): tg=False
    m=re.match(r'\[(\S+?)\] ',ln)
    if m and tg: ids.append(m.group(1))
allids=set(re.findall(r'^\[(\S+?)\] ',txt,re.M))
assert ids==list(P.keys()),(set(ids)^set(P))
d={k:{"cost":P[k][0],"needs":P[k][1]} for k in ids}
for k,v in d.items():
    for n in v["needs"]: assert n["id"] in allids and n["id"]!=k,(k,n)
json.dump(d,open(H+'point-links/'+out,'w'),indent=1)
json.loads(open(H+'point-links/'+out).read())
nl=[n for v in d.values() for n in v["needs"]]
print(out,len(ids),len(nl),sum(v["cost"]==2 for v in d.values()),sum(n["confidence"]=="low" for n in nl))
