import json,re
B='/Users/gabrielwhelan/barebones/.claude/worktrees/history-crunch/drafts/crunch/history/'
def build(pack,out,rows,pre):
    res={}
    for r in rows:
        i=pre+r[0]; assert i not in res,i
        needs=[]
        for t in r[2]:
            tid=t[0] if t[0].startswith('hist-') else pre+t[0]
            needs.append({"id":tid,"strength":"essential" if t[1]=='e' else "helpful","why":t[2],"confidence":"low" if len(t)>3 else "high"})
        res[i]={"cost":r[1],"needs":needs}
    txt=open(B+pack).read()
    tgt=re.findall(r'^\[(hist-[^\]]+)\]',txt.split('CANDIDATES')[0],re.M)
    allids=set(re.findall(r'^\[(hist-[^\]]+)\]',txt,re.M))
    assert list(res)==tgt,(set(tgt)-set(res),set(res)-set(tgt))
    for k,v in res.items():
        for n in v['needs']: assert n['id'] in allids and n['id']!=k,(k,n)
    json.dump(res,open(B+out,'w'),indent=1)
    L=sum(len(v['needs']) for v in res.values())
    print(len(res),L,sum(v['cost']==2 for v in res.values()),sum(n['confidence']=='low' for v in res.values() for n in v['needs']))
rows=[
('0.b',1,[]),
('0.0',1,[]),
('0.1',1,[('0.0','h','English customs replacing Irish after Famine')]),
('0.2',1,[('0.1','h','de-anglicisation aim of preserving Irish','l')]),
('0.3',2,[]),
('0.4',1,[]),
('0.5',1,[('0.4','e','conflict with the IRB')]),
('0.6',1,[('0.1','h','de-anglicisation idea')]),
('1.b',1,[('1.2','h','native game of hurling declined','l')]),
('1.0',1,[('0.1','h','anglicisation of sport')]),
('1.1',2,[]),
('1.2',1,[('0.0','h','Famine caused decline')]),
('1.3',1,[('1.2','h','hurling and its local variants')]),
('1.4',1,[('1.3','h','varying rules needing a standard code'),('2.0','h','introduces Cusack','l')]),
('2.b',1,[]),
('2.0',1,[]),
('2.1',1,[('7.2','h','falls out with officers in 1886'),('2.0','h','Cusack introduced')]),
('2.2',1,[('2.0','e','Cusack as the model')]),
('2.3',1,[]),
('2.4',1,[('2.3','h','Davin introduced')]),
('2.5',2,[('2.0','e','Cusack facts'),('2.3','e','Davin facts'),('7.2','h','Cusack removed 1886'),('7.5','h','Davin resigned 1889')]),
('3.b',1,[]),
('3.0',1,[('2.0','h','Cusack wrote the article')]),
('3.1',1,[('3.0','e','the article in United Ireland'),('0.3','h','Parnell as nationalist leader')]),
('3.2',1,[('3.0','h','the call leading to the meeting'),('2.3','h','Davin introduced')]),
('3.3',2,[('3.2','e','the meeting at Hayes Hotel'),('2.3','h','Davin attended')]),
('3.4',1,[('3.3','e','the Thurles meeting elections'),('2.4','h','Davin as first president')]),
('3.5',1,[('1.0','h','athletics closed to most classes'),('0.1','h','revival of Irish games')]),
('3.6',1,[('3.5','h','aims behind the full title','l')]),
('4.b',1,[]),
('4.0',1,[('0.3','e','Land War and nationalist background')]),
('4.1',2,[('4.0','e','Croke as patron and nationalist'),('0.1','h','English imitation versus Irish revival')]),
('4.2',1,[('0.3','e','Parnell, Davitt and Home Rule')]),
('4.3',1,[('0.3','e','Davitt and the land movement'),('0.1','h','breaking from English influence')]),
('4.4',1,[('3.1','e','United Ireland and O’Brien')]),
('4.5',1,[('4.1','e','Croke’s letter')]),
('5.b',1,[]),
('5.0',1,[('1.3','e','old local variations replaced'),('2.3','h','Davin as president','l')]),
('5.1',1,[('1.0','e','English amateur definition excluded workers')]),
('5.2',1,[('1.0','h','amateur athletics context','l')]),
('5.3',1,[('0.1','e','de-anglicisation purpose'),('1.1','h','rugby, soccer, cricket as foreign games')]),
('5.4',1,[('5.3','e','the first ban on games')]),
('5.5',1,[('3.4','h','Thurles and Central Council origins','l')]),
('5.6',1,[('5.5','e','parish club structure'),('0.5','h','Church organisation and priests')]),
('6.b',1,[('5.5','h','parish club system')]),
('6.0',1,[('5.5','h','clubs affiliating through parishes')]),
('6.1',1,[('6.0','h','spread of clubs','l')]),
('6.2',2,[('6.0','h','growth leading to championships','l')]),
('6.3',2,[('6.2','e','first All-Ireland championship')]),
('6.4',2,[('6.2','e','first All-Ireland championship')]),
('6.5',1,[('2.0','e','Cusack as founder')]),
('7.b',1,[('0.4','h','Fenians as the IRB'),('0.5','h','Church concern')]),
('7.0',1,[('0.4','e','the IRB'),('5.5','h','county boards structure')]),
('7.1',1,[('7.0','e','IRB involvement in clubs')]),
('7.2',1,[('2.0','e','Cusack as secretary'),('2.1','h','quarrelsome character')]),
('7.3',1,[('7.0','e','IRB control contest'),('5.5','h','Central Council and convention')]),
('7.4',2,[('0.5','e','Church wary of the IRB'),('4.1','h','Croke as patron'),('7.0','h','IRB growth causing unease')]),
('7.5',1,[('2.4','e','Davin as president')]),
('7.6',1,[('7.0','e','IRB influence'),('0.5','h','Church reaction')]),
('8.b',1,[('6.2','h','success preceding collapse','l')]),
('8.0',1,[]),
('8.1',1,[('8.0','e','the American tour'),('6.2','h','1888 championship')]),
('8.2',2,[('0.3','e','Parnell and the Irish Party'),('4.2','h','Parnell as patron'),('s4.2.2' if False else 'hist-ire2-s4.2.2','h','Committee Room 15 split')]),
('8.3',1,[('8.2','e','the Parnell split'),('7.0','h','IRB members'),('4.2','h','Parnell as patron')]),
('8.4',1,[('8.2','h','the Parnell split context'),('hist-ire2-s4.2.5','h','Parnell’s death')]),
('8.5',1,[('8.4','h','demoralisation after Parnell’s death'),('8.1','h','debts from American tour')]),
('8.6',1,[('8.5','e','the collapse it recovered from')]),
('9.b',1,[]),
('9.0',1,[('5.5','e','parish-based club system')]),
('9.1',1,[('4.1','e','Croke patronage'),('4.5','h','priests as club officers')]),
('9.2',1,[('6.1','h','matches and local crowds')]),
('9.3',1,[('7.2','e','Cusack removed'),('7.5','e','Davin resigned')]),
('9.4',2,[('4.2','e','Parnell and Davitt as patrons'),('7.0','e','the IRB links'),('8.2','e','the Parnell split')]),
('9.5',1,[('0.6','e','Irish Ireland'),('5.3','e','de-anglicisation via foreign games ban'),('5.2','h','amateur status')]),
('10.b',1,[]),
('10.0',1,[('3.0','e','Cusack’s article'),('3.5','h','aim of opening athletics')]),
('10.1',1,[('4.1','e','Croke’s letter')]),
('10.2',1,[('7.4','e','Croke’s complaint about drinking'),('6.1','h','crowds and bands')]),
('10.3',1,[('4.3','h','Davitt and the land movement'),('4.2','e','Parnell and Davitt as patrons')]),
('10.4',1,[('7.1','e','Castle reports of Fenianism')]),
('10.5',1,[('7.3','h','dispute at conventions'),('7.0','e','IRB involvement')]),
('10.6',2,[]),
('11.b',1,[]),
('11.0',1,[('5.0','h','standardised rules'),('5.5','h','parish network'),('3.5','h','open to all classes')]),
('11.1',2,[('7.0','e','IRB entanglement'),('7.4','e','quarrel with the Church'),('8.1','e','American tour debts'),('8.2','e','Parnell split')]),
('11.2',2,[('7.1','h','authorities saw it as Fenian'),('7.4','h','bishops uneasy')]),
('11.3',2,[('0.6','e','Irish Ireland'),('0.1','h','cultural nationalism and de-anglicisation')]),
]
build('packs/hist-ire2-s9.t1g1.txt','point-links/hist-ire2-s9.t1g1.json',rows,'hist-ire2-s9.')
