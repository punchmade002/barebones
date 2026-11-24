import json,re
P='/Users/gabrielwhelan/barebones/drafts/crunch/geography/'
S='geo-option-culture-identity-s4'
cnt={0:4,1:5,2:3,3:3,4:2,5:7,6:6,7:2,8:4,9:4,10:3,11:4,12:3,13:3,14:1,15:4,16:4,17:2,18:4,19:2,20:4,21:4,22:5,23:4,24:5,25:3,26:4,27:4,28:1,29:5,30:6,31:2}
costs={0:"11111",1:"111211",2:"1111",3:"1111",4:"111",5:"12111111",6:"1121111",7:"111",8:"12111",9:"11211",10:"1111",11:"11111",12:"1111",13:"1111",14:"11",15:"11111",16:"12111",17:"111",18:"11121",19:"121",20:"12111",21:"12111",22:"111111",23:"12121",24:"111111",25:"1211",26:"11111",27:"11111",28:"12",29:"121111",30:"1111111",31:"111"}
ids=[]
for s in range(32):
    assert len(costs[s])==cnt[s]+1
    ids.append((f"{S}.{s}.b",int(costs[s][0])))
    for i in range(cnt[s]): ids.append((f"{S}.{s}.{i}",int(costs[s][i+1])))
def L(i,st,why,c='high'): return {"id":i,"strength":st,"why":why,"confidence":c}
g='geo-economic-globalisation-s4.';l='geo-option-culture-identity-s2.';r='geo-option-culture-identity-s3.';t=S+'.'
A={ # g1 links (key short id -> list)
"0.2":[L(t+"0.0","helpful","uses definition of culture")],
"0.3":[L(t+"0.2","helpful","uses everyday expressions idea")],
"1.2":[L(l+"1.1","helpful","Gaelic Revival language movement","low")],
"2.b":[L(g+"12.b","helpful","globalisation defined","low")],
"3.0":[L(l+"1.1","helpful","Gaelic League revival")],
"3.1":[],
"5.1":[L(t+"5.0","essential","GAA founding and presidency")],
"5.2":[L(t+"5.0","helpful","GAA amateur status")],
"5.3":[L(t+"5.b","helpful","GAA native games")],
"5.6":[L(t+"3.1","essential","UNESCO living traditions list")],
"6.1":[L(t+"5.0","helpful","GAA aim of native games")],
"6.3":[L(t+"6.0","helpful","Croke Park setting")],
"6.5":[L(t+"6.0","helpful","Croke Park stadium")],
"8.3":[L(t+"8.0","essential","uilleann pipes"),L(t+"3.1","helpful","UNESCO living traditions list")],
"3.1x":[],
"9.1":[L(t+"9.0","helpful","Comhaltas organises the festival")],
"9.3":[L(t+"9.2","helpful","sean-nós singing tradition")],
"10.1":[L(t+"10.0","essential","Riverdance show")],
"10.b":[L(g+"12.b","helpful","globalisation spreading culture","low")],
"11.1":[L(t+"11.0","helpful","St Patrick's Day parades")],
"15.3":[L(t+"5.3","helpful","GAA county identity")],
"17.1":[L(t+"17.0","helpful","Polish language presence")],
"17.0":[L(l+"0.2","helpful","census language data","low")],
"18.3":[L(t+"18.2","essential","Newgrange chamber")],
"19.1":[L(l+"0.0","helpful","language carries literature and songs")],
"20.1":[L(t+"12.2","helpful","Ballinasloe Horse Fair")],
"21.0":[L(t+"21.b","helpful","unionist identity")],
"21.1":[L(t+"21.b","helpful","unionist identity")],
"21.2":[L(t+"21.b","helpful","loyalist and republican identities")],
"21.3":[L(t+"21.b","helpful","two identities marked")],
"22.3":[L(t+"3.1","helpful","UNESCO living traditions list")],
"22.4":[L(t+"3.1","helpful","UNESCO living traditions list"),L(l+"1.2","helpful","Catalan suppressed under Franco")],
"23.0":[L(l+"1.2","helpful","Franco suppressing Catalan identity")],
"25.1":[L(t+"21.b","helpful","unionist identity")],
"25.2":[L(t+"25.0","helpful","Celtic's Irish origins")],
"26.1":[L(t+"26.0","helpful","Oktoberfest setting")],
"27.2":[L(t+"3.1","helpful","UNESCO living traditions list")],
"29.2":[L(t+"3.1","helpful","UNESCO living traditions list")],
"30.2":[L(l+"9.3","helpful","Celtic languages and regions","low")],
"30.3":[L(t+"3.1","helpful","UNESCO living traditions list")],
"30.4":[L(l+"26.1","helpful","National Eisteddfod promotes Welsh")],
"31.1":[L(t+"31.0","helpful","Eurovision contest")],
"4.1":[L(t+"4.0","helpful","migrants' customs blending")],
}
B={ # g2 links
"1.4":[L(r+"19.b","helpful","Northern Ireland divisions","low")],
"4.0":[L(r+"5.4","helpful","migration spreads religions","low")],
"6.2":[L(r+"20.2","helpful","British forces in Northern Ireland","low")],
"6.4":[L(r+"20.3","essential","Bloody Sunday 1972 Derry")],
"7.1":[L(r+"19.2","helpful","unionist majority, partition")],
"11.b":[L(r+"0.3","helpful","religion shapes festivals","low")],
"14.0":[L(r+"0.1","helpful","holy wells in landscape","low")],
"21.b":[L(r+"19.b","helpful","roots of unionist/nationalist divide")],
"21.0":[L(r+"19.1","helpful","Battle of the Boyne")],
"21.1":[L(r+"19.b","helpful","Northern Ireland conflict roots")],
"21.2":[L(r+"20.b","helpful","Troubles identities","low")],
"25.0":[L(r+"6.0","helpful","Roman Catholic")],
"25.1":[L(r+"6.1","helpful","Protestant")],
"28.b":[L(r+"11.2","helpful","strict church-state separation")],
"28.0":[L(r+"13.2","essential","France's laïcité"),L(r+"13.3","helpful","religious dress laws")],
}
def key(i): return i[len(S)+1:]
out1={};out2={}
for i,c in ids:
    out1[i]={"cost":c,"needs":A.get(key(i),[])}
    out2[i]={"needs":B.get(key(i),[])}
for k in list(A)+list(B):
    assert k=="3.1x" or (S+'.'+k) in out1,k
cand=set(re.findall(r'^\[([^\]]+)\]',open(P+'packs/geo-option-culture-identity-s4.t1g1.txt').read(),re.M))
cand2=set(re.findall(r'^\[([^\]]+)\]',open(P+'packs/geo-option-culture-identity-s4.t1g2.txt').read(),re.M))
for o,cs,f in((out1,cand,'t1g1'),(out2,cand2,'t1g2')):
    assert len(o)==149
    for v in o.values():
        for n in v['needs']: assert n['id'] in cs,n['id']
    json.dump(o,open(P+f'point-links/geo-option-culture-identity-s4.{f}.json','w'),indent=1,ensure_ascii=False)
    print(f,len(o),sum(len(v['needs']) for v in o.values()),sum(v.get('cost')==2 for v in o.values()),sum(n['confidence']=='low' for v in o.values() for n in v['needs']))
