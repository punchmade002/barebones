import json,re,sys
H='/Users/gabrielwhelan/barebones/drafts/crunch/history/'
def L(i,s,w,c='high'): return {"id":i,"strength":s,"why":w,"confidence":c}
E,H_='essential','helpful'
P1={
"hist-ire4-s3.0.b":(1,[]),
"hist-ire4-s3.0.0":(1,[]),
"hist-ire4-s3.0.1":(1,[L("hist-ire4-s1.2.3",H_,"Famine-era mass emigration")]),
"hist-ire4-s3.0.2":(1,[]),
"hist-ire4-s3.0.3":(1,[]),
"hist-ire4-s3.0.4":(1,[]),
"hist-ire4-s3.0.5":(1,[]),
"hist-ire4-s3.1.b":(1,[]),
"hist-ire4-s3.1.0":(1,[L("hist-ire4-s3.0.0",H_,"anti-Catholic hostility to Irish")]),
"hist-ire4-s3.1.1":(1,[L("hist-ire4-s3.1.b",H_,"uses the nativism movement")]),
"hist-ire4-s3.1.2":(1,[L("hist-ire4-s3.1.1",E,"uses the Know-Nothings")]),
"hist-ire4-s3.1.3":(2,[L("hist-ire4-s3.1.1",E,"uses the Know-Nothings")]),
"hist-ire4-s3.1.4":(2,[]),
"hist-ire4-s3.1.5":(1,[L("hist-ire4-s3.0.4",H_,"ape-like racial stereotype")]),
"hist-ire4-s3.1.6":(1,[]),
"hist-ire4-s3.2.b":(1,[]),
"hist-ire4-s3.2.0":(1,[L("hist-ire4-s3.0.4",H_,"simian racial stereotype")]),
"hist-ire4-s3.2.1":(1,[]),
"hist-ire4-s3.2.2":(1,[]),
"hist-ire4-s3.2.3":(1,[]),
"hist-ire4-s3.2.4":(2,[]),
"hist-ire4-s3.2.5":(1,[L("hist-ire4-s3.2.4",H_,"Fenian scare after Clerkenwell")]),
"hist-ire4-s3.2.6":(1,[L("hist-ire4-s3.0.1",H_,"blamed for typhus and poverty")]),
"hist-ire4-s3.3.b":(1,[]),
"hist-ire4-s3.3.0":(1,[]),
"hist-ire4-s3.3.1":(1,[L("hist-ire4-s3.3.0",H_,"Democratic Party help for immigrants")]),
"hist-ire4-s3.3.2":(2,[L("hist-ire4-s3.3.1",H_,"patronage in ward politics")]),
"hist-ire4-s3.3.3":(2,[]),
"hist-ire4-s3.3.4":(1,[]),
"hist-ire4-s3.3.5":(1,[]),
"hist-ire4-s3.3.6":(1,[]),
"hist-ire4-s3.3.7":(1,[]),
"hist-ire4-s3.4.b":(1,[L("hist-ire4-s3.3.2",E,"uses Tammany Hall")]),
"hist-ire4-s3.4.0":(1,[]),
"hist-ire4-s3.4.1":(1,[L("hist-ire4-s3.4.0",H_,"Croker's background")]),
"hist-ire4-s3.4.2":(2,[L("hist-ire4-s3.3.2",E,"uses Tammany Hall")]),
"hist-ire4-s3.4.3":(1,[L("hist-ire4-s3.4.2",H_,"Croker's control of Tammany")]),
"hist-ire4-s3.4.4":(2,[L("hist-ire4-s3.4.2",E,"Croker's leadership of Tammany")]),
"hist-ire4-s3.4.5":(1,[]),
"hist-ire4-s3.4.6":(1,[L("hist-ire4-s3.4.2",H_,"Croker's patronage system")]),
"hist-ire4-s3.4.7":(2,[L("hist-ire4-s3.4.2",H_,"Croker's machine politics")]),
"hist-ire4-s3.5.b":(1,[]),
"hist-ire4-s3.5.0":(1,[L("hist-ire4-s3.3.4",H_,"Mayor John F. Fitzgerald")]),
"hist-ire4-s3.5.1":(1,[]),
"hist-ire4-s3.5.2":(1,[]),
"hist-ire4-s3.5.3":(1,[]),
"hist-ire4-s3.5.4":(2,[L("hist-ire4-s3.5.3",E,"his post as ambassador")]),
"hist-ire4-s3.5.5":(1,[L("hist-ire4-s3.5.4",H_,"his appeasement stance")]),
"hist-ire4-s3.5.6":(2,[L("hist-ire4-s3.5.4",E,"his appeasement and resignation")]),
"hist-ire4-s3.6.b":(1,[]),
"hist-ire4-s3.6.0":(1,[]),
"hist-ire4-s3.6.1":(1,[]),
"hist-ire4-s3.6.2":(1,[]),
"hist-ire4-s3.6.3":(1,[]),
"hist-ire4-s3.6.4":(1,[L("hist-ire4-s3.6.3",H_,"his Northern Ireland views")]),
"hist-ire4-s3.6.5":(2,[L("hist-ire4-s3.6.3",H_,"civil rights and Irish nationalism")]),
"hist-ire4-s3.7.b":(1,[]),
"hist-ire4-s3.7.0":(1,[]),
"hist-ire4-s3.7.1":(2,[L("hist-ire4-s3.7.0",H_,"organised Irish voters in Britain")]),
"hist-ire4-s3.7.2":(1,[]),
"hist-ire4-s3.7.3":(1,[L("hist-ire4-s3.7.2",E,"uses T. P. O'Connor")]),
"hist-ire4-s3.7.4":(1,[]),
"hist-ire4-s3.7.5":(1,[]),
"hist-ire4-s3.7.6":(1,[]),
"hist-ire4-s3.8.b":(1,[]),
"hist-ire4-s3.8.0":(2,[]),
"hist-ire4-s3.8.1":(1,[]),
"hist-ire4-s3.8.2":(1,[]),
"hist-ire4-s3.8.3":(2,[L("hist-ire4-s3.8.0",H_,"the Molly Maguires society")]),
"hist-ire4-s3.8.4":(2,[L("hist-ire4-s3.8.3",E,"McParland's infiltration of the society")]),
"hist-ire4-s3.8.5":(2,[L("hist-ire4-s3.8.4",H_,"the trials and convictions")]),
"hist-ire4-s3.8.6":(2,[L("hist-ire4-s3.8.5",H_,"the trials and hangings")]),
"hist-ire4-s3.8.7":(1,[L("hist-ire4-s3.8.5",E,"uses Jack Kehoe's hanging")]),
"hist-ire4-s3.9.b":(1,[]),
"hist-ire4-s3.9.0":(1,[]),
"hist-ire4-s3.9.1":(1,[L("hist-ire4-s3.3.2",H_,"machine politics, Tammany example")]),
"hist-ire4-s3.9.2":(1,[]),
"hist-ire4-s3.9.3":(1,[]),
"hist-ire4-s3.9.4":(2,[]),
"hist-ire4-s3.9.5":(2,[L("hist-ire4-s3.7.0",H_,"Irish Parliamentary Party organisation")]),
}
def run(pk,out,P):
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
run('hist-ire4-s3.t1g1.txt','hist-ire4-s3.t1g1.json',P1)
