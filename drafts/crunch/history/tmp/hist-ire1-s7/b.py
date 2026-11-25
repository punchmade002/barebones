import json,re
H='/Users/gabrielwhelan/barebones/.claude/worktrees/history-crunch/drafts/crunch/history/'
def run(pack,out,spec):
    txt=open(H+'packs/'+pack).read()
    tgt=txt.split('CANDIDATES')[0]
    tids=re.findall(r'^\[([^\]]+)\]',tgt,re.M)
    allids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
    res={}
    for line in spec.strip().split('\n'):
        p=line.split('|')
        i,c=p[0],int(p[1]); needs=[]
        for l in p[2:]:
            if not l: continue
            a,s,w,cf=l.split(';')
            assert a in allids and a!=i,(i,a)
            needs.append({"id":a,"strength":{'E':'essential','H':'helpful'}[s],"why":w,"confidence":{'h':'high','l':'low'}[cf]})
        res[i]={"cost":c,"needs":needs}
    assert list(res)==tids,(set(tids)^set(res))
    json.dump(res,open(H+'point-links/'+out,'w'),indent=1)
    n=sum(len(v['needs']) for v in res.values())
    print(out,len(res),n,sum(v['cost']==2 for v in res.values()),sum(l['confidence']=='low' for v in res.values() for l in v['needs']))
S1='''hist-ire1-s7.0.b|1|hist-ire1-s2.0.2;H;Catholic Emancipation 1829;h
hist-ire1-s7.0.0|1|
hist-ire1-s7.0.1|1|
hist-ire1-s7.0.2|2|
hist-ire1-s7.0.3|2|
hist-ire1-s7.0.4|2|hist-ire1-s7.0.b;H;Larkin's devotional revolution;h
hist-ire1-s7.0.5|2|hist-ire1-s4.8.1;H;poor cottiers died or emigrated;l
hist-ire1-s7.0.6|1|hist-ire1-s7.0.b;H;the devotional revolution;h
hist-ire1-s7.0.7|1|
hist-ire1-s7.1.b|1|hist-ire1-s7.0.b;H;Catholic revival;l
hist-ire1-s7.1.0|1|
hist-ire1-s7.1.1|1|hist-ire1-s7.1.0;H;evangelicalism;h
hist-ire1-s7.1.2|1|hist-ire1-s7.1.1;E;the conversion drive;h
hist-ire1-s7.1.3|1|hist-ire1-s4.3.3;H;souperism in the Famine;h
hist-ire1-s7.1.4|1|
hist-ire1-s7.1.5|1|hist-ire1-s2.10.b;H;O'Connell;l
hist-ire1-s7.1.6|1|hist-ire1-s7.1.0;H;evangelical revival;h
hist-ire1-s7.1.7|1|hist-ire1-s2.3.2;H;disestablishment of 1869;l
hist-ire1-s7.2.b|1|hist-ire1-s2.7.b;H;Young Ireland and The Nation;h
hist-ire1-s7.2.0|1|hist-ire1-s2.7.2;H;Young Ireland's cultural nationality;h
hist-ire1-s7.2.1|2|hist-ire1-s2.7.0;H;The Nation's founders;h
hist-ire1-s7.2.2|1|hist-ire1-s7.2.0;H;cultural nationalism;h
hist-ire1-s7.2.3|1|
hist-ire1-s7.2.4|1|
hist-ire1-s7.2.5|1|hist-ire1-s4.9.4;H;Famine hit Irish language;l
hist-ire1-s7.2.6|1|
hist-ire1-s7.3.b|1|hist-ire1-s7.6.1;H;Romanisation defined;h
hist-ire1-s7.3.0|2|
hist-ire1-s7.3.1|2|hist-ire1-s7.4.b;H;the Synod of Thurles;h
hist-ire1-s7.3.2|2|hist-ire1-s7.0.b;E;the devotional revolution;h|hist-ire1-s7.6.0;H;ultramontanism;h
hist-ire1-s7.3.3|1|hist-ire1-s2.7.b;H;Young Ireland;h|hist-ire1-s2.9.3;H;the Fenians;l
hist-ire1-s7.3.4|1|hist-ire1-s2.9.2;H;MacManus, a Young Irelander;h
hist-ire1-s7.3.5|1|hist-ire1-s7.1.7;H;disestablishment of Church of Ireland;h
hist-ire1-s7.3.6|2|hist-ire1-s7.4.3;H;MacHale's resistance;h|hist-ire1-s7.6.2;H;Catholic University failed;h
hist-ire1-s7.3.7|2|hist-ire1-s7.4.3;H;MacHale resented him;h|hist-ire1-s7.0.b;H;the devotional revolution;h
hist-ire1-s7.4.b|1|
hist-ire1-s7.4.0|1|
hist-ire1-s7.4.1|1|
hist-ire1-s7.4.2|2|
hist-ire1-s7.4.3|1|hist-ire1-s7.4.2;E;the Queen's Colleges;h
hist-ire1-s7.4.4|1|hist-ire1-s7.4.2;H;the Queen's Colleges;h
hist-ire1-s7.4.5|1|hist-ire1-s7.3.b;H;Paul Cullen;h
hist-ire1-s7.5.b|1|hist-ire1-s7.4.b;H;the Synod's purpose;h
hist-ire1-s7.5.0|1|hist-ire1-s7.3.1;H;Apostolic Delegate;h
hist-ire1-s7.5.1|1|hist-ire1-s7.4.2;E;the Queen's Colleges;h
hist-ire1-s7.5.2|1|hist-ire1-s7.5.1;H;rejection of the Queen's Colleges;h
hist-ire1-s7.5.3|1|
hist-ire1-s7.5.4|1|
hist-ire1-s7.5.5|1|
hist-ire1-s7.5.6|1|hist-ire1-s7.5.1;H;the Queen's Colleges condemned;h|hist-ire1-s7.4.3;H;MacHale's opposition;h
hist-ire1-s7.5.7|1|
hist-ire1-s7.6.b|1|
hist-ire1-s7.6.0|1|
hist-ire1-s7.6.1|1|hist-ire1-s7.6.0;H;ultramontanism;h
hist-ire1-s7.6.2|1|hist-ire1-s7.5.2;E;the Catholic University;h
hist-ire1-s7.6.3|1|hist-ire1-s7.6.2;H;Catholic University's failure;h
hist-ire1-s7.6.4|1|hist-ire1-s7.3.b;H;Cullen's role;h
hist-ire1-s7.6.5|1|
hist-ire1-s7.6.6|1|hist-ire1-s7.0.b;H;the devotional revolution;h
hist-ire1-s7.7.b|1|
hist-ire1-s7.7.0|1|
hist-ire1-s7.7.1|2|hist-ire1-s7.4.3;H;Archbishop Murray;l
hist-ire1-s7.7.2|1|
hist-ire1-s7.7.3|1|
hist-ire1-s7.7.4|1|
hist-ire1-s7.7.5|1|
hist-ire1-s7.7.6|1|
hist-ire1-s7.7.7|1|
hist-ire1-s7.8.b|1|
hist-ire1-s7.8.0|1|
hist-ire1-s7.8.1|1|
hist-ire1-s7.8.2|2|
hist-ire1-s7.8.3|1|
hist-ire1-s7.8.4|1|
hist-ire1-s7.8.5|1|hist-ire1-s7.8.1;H;his early anti-Catholic writing;h
hist-ire1-s7.8.6|1|
hist-ire1-s7.9.b|1|
hist-ire1-s7.9.0|1|hist-ire1-s7.2.1;H;founding of The Nation;h
hist-ire1-s7.9.1|1|
hist-ire1-s7.9.2|1|
hist-ire1-s7.9.3|1|hist-ire1-s7.2.0;H;Young Ireland's inclusive nation;h
hist-ire1-s7.9.4|1|
hist-ire1-s7.9.5|1|
hist-ire1-s7.9.6|1|
hist-ire1-s7.10.b|1|
hist-ire1-s7.10.0|1|
hist-ire1-s7.10.1|1|hist-ire1-s7.2.1;H;The Nation newspaper;h
hist-ire1-s7.10.2|2|
hist-ire1-s7.10.3|2|hist-ire1-s7.10.2;H;Petrie, worked with them;h
hist-ire1-s7.10.4|1|hist-ire1-s7.10.3;H;O'Donovan and O'Curry;h
hist-ire1-s7.10.5|1|
hist-ire1-s7.10.6|1|hist-ire1-s7.8.3;H;The Black Prophet;h
hist-ire1-s7.11.b|1|
hist-ire1-s7.11.0|1|
hist-ire1-s7.11.1|1|
hist-ire1-s7.11.2|1|hist-ire1-s7.11.1;E;Rosse's telescope;h
hist-ire1-s7.11.3|1|
hist-ire1-s7.11.4|1|hist-ire1-s7.4.2;H;the Queen's Colleges;l
hist-ire1-s7.11.5|1|hist-ire1-s7.4.2;H;the Queen's Colleges;l
hist-ire1-s7.11.6|1|hist-ire1-s7.4.2;H;the Queen's Colleges;l
hist-ire1-s7.12.b|1|hist-ire1-s7.0.6;H;imposed from above or below;h
hist-ire1-s7.12.0|1|hist-ire1-s7.0.b;E;the devotional revolution;h
hist-ire1-s7.12.1|2|hist-ire1-s7.6.2;H;Catholic University weak;h
hist-ire1-s7.12.2|1|hist-ire1-s7.6.5;H;contemporary reactions;l
hist-ire1-s7.12.3|2|hist-ire1-s7.0.b;H;Larkin's devotional revolution;h
hist-ire1-s7.12.4|1|
hist-ire1-s7.12.5|1|hist-ire1-s7.2.5;H;Famine's effect on Irish;h'''
run('hist-ire1-s7.t1g1.txt','hist-ire1-s7.t1g1.json',S1)
