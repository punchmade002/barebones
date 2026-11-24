import json,re,sys
D='/Users/gabrielwhelan/barebones/drafts/crunch/history/'
# id|cost|links  (link = target:E|H:why:H|L, ';' separated)
RAW='''0.b|1|
0.0|1|
0.1|1|
0.2|1|
0.3|1|
0.4|1|
0.5|1|s4.2.b:H:Parnell and the Irish Party:L
0.6|1|9.0.3:H:Cusack's Metropolitan Hurling Club:H
1.b|1|
1.0|1|
1.1|1|
1.2|1|9.1.0:H:Cusack as author of the article:H
1.3|1|9.1.0:H:Cusack as organiser:H;9.1.1:H:Davin as organiser:H
1.4|2|9.1.0:H:Cusack as secretary:H;9.1.1:H:Davin as president:H
1.5|1|
1.6|1|
2.b|1|
2.0|1|
2.1|1|9.2.0:H:Croke as patron:H
2.2|1|s4.2.b:H:Parnell as Home Rule leader:L
2.3|1|9.2.0:H:Croke's patronage letter:H
2.4|1|9.2.2:H:Davitt's patronage:H
2.5|1|9.2.0:H:Croke as patron:H
2.6|1|9.1.4:H:Wyse Power as first secretary:H
3.b|1|
3.0|1|9.1.1:H:Davin as president:H
3.1|1|9.0.0:E:old amateur rules excluding workers:H
3.2|1|9.0.1:H:rugby, cricket and soccer as foreign games:H
3.3|1|
3.4|1|
3.5|1|9.3.4:E:parish club structure:H
3.6|1|
4.b|1|
4.0|1|
4.1|1|
4.2|1|
4.3|1|9.4.2:H:first All-Ireland championships:H
4.4|1|9.4.2:H:first All-Ireland championships:H
4.5|1|9.1.0:H:Cusack as founder:H
5.b|1|
5.0|1|
5.1|1|9.5.0:H:IRB involvement in the GAA:H
5.2|1|9.1.0:H:Cusack as secretary:H;9.5.0:H:IRB as the secret society:H
5.3|2|9.5.0:E:IRB control of the Central Council:H;9.3.4:H:Central Council and conventions:H
5.4|1|9.2.0:H:Croke as patron:H;9.1.1:H:Davin as president:H
5.5|1|9.5.0:E:IRB infiltration:H
6.b|1|
6.0|1|
6.1|1|9.6.0:E:the American Invasion tour:H
6.2|2|s4.1.b:E:O'Shea divorce and Irish Party split:H;9.5.0:H:IRB position on Parnell:L
6.3|1|s4.1.9:H:Parnell's death in 1891:H
6.4|1|9.6.1:H:tour debts:L;9.6.2:H:Parnell split effects:H
6.5|1|
7.b|1|
7.0|1|9.3.4:E:parish-based club system:H
7.1|1|9.2.0:H:Croke's patronage:H;9.2.3:H:clergy as club officers:H
7.2|1|
7.3|2|9.5.2:E:Cusack's removal:H;9.5.4:H:Davin stepping down:H
7.4|2|9.6.2:E:Parnell split:H;9.5.0:H:IRB links:H
7.5|2|9.3.2:H:Irish-only foreign games ban:H
8.b|1|
8.0|1|9.1.2:E:Cusack's article:H
8.1|2|9.2.1:H:Croke attacking English games:H
8.2|1|9.2.2:E:Davitt and Parnell as patrons:H
8.3|1|9.5.1:H:Dublin Castle reports on Fenianism:H
8.4|1|9.5.3:H:moderates versus IRB at conventions:H
8.5|2|
9.b|1|
9.0|2|9.3.0:H:Davin's rules:H;9.3.4:H:parish structure:H
9.1|2|9.5.0:H:IRB infiltration:H;9.5.4:H:quarrel with the Church:H;9.6.0:H:American tour:H;9.6.2:H:Parnell split:H
9.2|1|9.5.1:H:authorities seeing it as Fenian:H
9.3|1|
'''
def build(sub,pre,RAW,pack,out):
    txt=open(D+'packs/'+pack).read()
    tgt=[];allids=set();mode=None
    for l in txt.split('\n'):
        if l.startswith('TARGET'): mode='t'
        elif l.startswith('CANDIDATES'): mode='c'
        m=re.match(r'\[(\S+?)\]',l)
        if m:
            allids.add(m.group(1))
            if mode=='t': tgt.append(m.group(1))
    res={}
    for line in RAW.strip().split('\n'):
        i,c,ls=line.split('|')
        i=sub+'.'+i
        needs=[]
        for k in filter(None,ls.split(';')):
            t,st,w,cf=k.split(':')
            t=pre+(t if t.startswith('s') else 's'+t)
            needs.append({"id":t,"strength":"essential" if st=='E' else "helpful","why":w,"confidence":"high" if cf=='H' else "low"})
        assert i not in res,i
        res[i]={"cost":int(c),"needs":needs}
    assert list(res)==tgt,(set(tgt)-set(res),set(res)-set(tgt))
    for i,v in res.items():
        for n in v['needs']: assert n['id'] in allids and n['id']!=i,(i,n['id'])
    json.dump(res,open(out,'w'),indent=1)
    print(len(res),sum(len(v['needs']) for v in res.values()),sum(v['cost']==2 for v in res.values()),sum(n['confidence']=='low' for v in res.values() for n in v['needs']))
build('hist-ire2-s9','hist-ire2-',RAW,'hist-ire2-s9.t1g1.txt',D+'point-links/hist-ire2-s9.t1g1.json')
