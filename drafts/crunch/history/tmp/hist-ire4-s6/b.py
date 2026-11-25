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
('0.b',1,[('hist-ire4-s2.0.0','h','post-Famine emigration scale')]),
('0.0',1,[('hist-ire4-s2.0.0','h','mass emigration of the poor','l')]),
('0.1',1,[('hist-ire4-s3.0.0','h','anti-Catholic prejudice')]),
('0.2',1,[('hist-ire4-s2.10.b','h','assimilation defined')]),
('0.3',1,[('7.0','h','Ulster Presbyterian emigration','l')]),
('0.4',1,[]),
('1.b',1,[('0.1','h','church as a refuge for emigrants','l')]),
('1.0',1,[('hist-ire4-s2.0.1','h','USA took most emigrants')]),
('1.1',1,[('1.0','h','Irish dominance of the hierarchy')]),
('1.2',1,[('1.0','h','Irish leaders of the American church')]),
('1.3',1,[('0.1','h','parish gave identity to emigrants','l')]),
('1.4',1,[('1.0','h','Irish-led Catholic presence')]),
('1.5',1,[('1.3','h','parish church as community centre')]),
('2.b',1,[]),
('2.0',1,[('1.5','h','the parish and its school')]),
('2.1',2,[]),
('2.2',1,[('0.0','h','poor emigrants without a safety net')]),
('2.3',1,[('2.2','e','fraternal society defined')]),
('2.4',1,[('2.2','e','fraternal society defined'),('2.3','h','compare Irish-only Hibernians')]),
('3.b',1,[('1.b','h','same Irish-led Church pattern')]),
('3.0',1,[('hist-ire4-s2.3.4','h','Irish settled in Liverpool, Glasgow')]),
('3.1',1,[('hist-ire4-s2.0.0','h','Famine emigration swelling numbers','l')]),
('3.2',1,[('3.0','h','Catholic schools for poor congregations')]),
('3.3',2,[('3.0','h','Glasgow’s poor Irish Catholics')]),
('3.4',1,[('3.0','h','work for poor Irish districts')]),
('3.5',1,[('2.1','e','Christian Brothers and Sisters of Mercy')]),
('3.6',2,[('3.5','h','Irish orders staffing schools')]),
('3.7',1,[('3.0','h','Catholic institutions in Britain'),('hist-ire4-s3.2.b','h','sectarian rivalry in Britain')]),
('4.b',1,[('8.b','h','the Orange Order')]),
('4.0',1,[]),
('4.1',1,[]),
('4.2',2,[]),
('4.3',1,[]),
('4.4',1,[('8.1','e','Orange lodges in Canada'),('4.b','h','conflict in Ontario')]),
('5.b',1,[]),
('5.0',1,[]),
('5.1',1,[('5.0','h','Mannix introduced')]),
('5.2',2,[('5.1','h','Mannix as Melbourne archbishop')]),
('5.3',1,[('5.2','h','his opposition to conscription')]),
('5.4',1,[('5.3','e','his support for Irish independence'),('5.2','h','conflict with imperial loyalists')]),
('5.5',1,[('8.5','e','Orange Order in Victoria'),('5.2','h','First World War pressures')]),
('5.6',1,[('5.1','h','archbishop of Melbourne')]),
('5.7',1,[('5.2','e','conscription conflict'),('5.5','h','Protestant organisations denounced him')]),
('5.8',1,[('5.3','h','his Irish nationalism'),('0.1','h','anti-Catholic prejudice')]),
('6.b',1,[]),
('6.0',1,[]),
('6.1',1,[('6.0','h','what the GAA promoted')]),
('6.2',1,[('hist-ire4-s2.0.1','h','USA took most emigrants','l'),('6.1','h','Gaelic sport and the GAA')]),
('6.3',1,[('1.0','h','Irish-American crowds','l')]),
('6.4',1,[('hist-ire4-s2.3.0','h','Irish settled in US cities')]),
('6.5',1,[('6.4','h','GAA clubs abroad'),('hist-ire4-s2.3.4','h','Irish in British cities')]),
('6.6',2,[('6.4','e','New York as GAA centre')]),
('7.b',1,[('0.3','h','Ulster Protestant emigration')]),
('7.0',2,[('0.3','h','Ulster Protestant emigration')]),
('7.1',1,[('7.0','e','Presbyterian settlers in America')]),
('7.2',1,[('7.0','h','Presbyterian congregations')]),
('7.3',1,[('7.2','h','Methodist congregations')]),
('7.4',1,[('7.1','h','Scotch-Irish identity'),('7.b','h','distinct from Irish Catholics')]),
('7.5',1,[('0.2','e','assimilation'),('7.4','h','Protestant identity')]),
('7.6',1,[('7.4','h','Ulster-Scots loyalty'),('4.4','h','Orange rivalry in Ontario','l')]),
('8.b',1,[('7.b','h','Protestant loyalist identity')]),
('8.0',1,[]),
('8.1',1,[('8.0','e','the Orange Order and its lodges')]),
('8.2',1,[('8.1','h','Orange lodges in Canada')]),
('8.3',2,[('8.1','h','Orange lodges in Canada')]),
('8.4',1,[('8.0','h','the Orange tradition and the Boyne')]),
('8.5',1,[('8.1','h','Orange lodges overseas'),('hist-ire4-s3.7.4','h','Home Rule explained','l')]),
('8.6',1,[('8.5','e','Orange lodges in Australia')]),
('8.7',1,[('8.4','e','Orange parades on the Twelfth'),('hist-ire4-s3.2.3','h','Orange versus Catholic clashes')]),
('9.b',1,[]),
('9.0',1,[('1.5','h','parish social life')]),
('9.1',1,[('1.3','h','public display of Irish identity','l')]),
('9.2',1,[('2.0','h','parochial schools')]),
('9.3',1,[('0.2','e','assimilation'),('hist-ire4-s2.10.0','h','second generation becoming American')]),
('9.4',1,[('8.7','h','sectarian riots'),('4.4','h','Ontario rivalry'),('8.6','h','Australia')]),
('9.5',1,[('0.2','e','assimilation'),('1.0','h','church leaders in America')]),
('10.b',1,[]),
('10.0',2,[('1.5','h','church reached nearly every Catholic'),('6.1','h','GAA narrower and sporting')]),
('10.1',1,[('9.3','e','assimilation of the second generation')]),
('10.2',1,[('hist-ire4-s3.1.b','h','nativists'),('5.7','h','imperial loyalists denounced Mannix','l')]),
('10.3',2,[('0.2','h','assimilation versus identity'),('hist-ire4-s3.3.b','h','communities gaining power','l')]),
('10.4',1,[('8.3','h','Orange influence in Canada'),('7.4','e','Ulster-Scots loyalty to Crown')]),
('10.5',1,[('8.7','e','Orange riots in America'),('4.4','h','Catholic against Orange in Canada')]),
]
build('packs/hist-ire4-s6.t1g1.txt','point-links/hist-ire4-s6.t1g1.json',rows,'hist-ire4-s6.')
