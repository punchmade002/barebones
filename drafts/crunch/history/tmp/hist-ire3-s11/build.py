import json,re,sys
H='/Users/gabrielwhelan/barebones/drafts/crunch/history/'
def build(pack,out,pre,spec,full):
    ids=[re.match(r'\[(\S+?)\]',l).group(1) for l in open(H+'packs/'+pack) if re.match(r'\[\S+?\] ',l)]
    tids=[]
    for l in open(H+'packs/'+pack):
        if l.startswith('CANDIDATES'): break
        m=re.match(r'\[(\S+?)\] ',l)
        if m: tids.append(m.group(1))
    res={}
    for line in spec.strip().split('\n'):
        k,rest=line.split(' ',1)
        cost,_,links=rest.partition('|')
        key=pre+k
        assert key in tids and key not in res,key
        needs=[]
        for lk in [x for x in links.split(';') if x.strip()]:
            t,s,c,w=[x.strip() for x in lk.split(':')]
            tid=('hist-ire3-'+t) if t.startswith('s') else pre+t
            assert tid in ids and tid!=key,(key,tid)
            needs.append({"id":tid,"strength":{'e':'essential','h':'helpful'}[s],"why":w,"confidence":{'H':'high','L':'low'}[c]})
        res[key]={"cost":int(cost),"needs":needs}
    assert set(res)==set(tids) and len(res)==len(tids),set(tids)-set(res)
    json.dump({k:res[k] for k in tids},open(H+'point-links/'+out,'w'),indent=1)
    n=sum(len(v['needs']) for v in res.values())
    print(out,len(res),n,sum(v['cost']==2 for v in res.values()),sum(l['confidence']=='low' for v in res.values() for l in v['needs']))
s11='''0.b 1|
0.0 1|
0.1 1|0.0:h:H:uses the International Eucharistic Congress
0.2 1|s5.6.2:h:H:Cosgrave as head of government
0.3 1|
0.4 1|s5.1.b:h:H:the Civil War
0.5 1|
1.b 1|0.2:h:H:planned under Cosgrave;s5.4.5:h:H:de Valera taking power in 1932
1.0 1|s5.4.5:h:H:February 1932 election and de Valera
1.1 1|1.0:h:H:de Valera in power
1.2 1|
1.3 1|
1.4 1|s10.4.3:h:H:Athlone radio station
1.5 1|
1.6 1|
1.7 1|
2.b 1|s5.2.1:h:H:the Governor-General
2.0 1|0.3:h:H:Byrne and Cardinal Lauri
2.1 1|2.0:h:L:Lauri's arrival route
2.2 2|s5.2.1:e:H:Governor-General James McNeill;0.3:h:H:the Pope's legate
2.3 1|2.2:e:H:the Dublin Castle snub
2.4 1|s6.1.1:e:H:McNeill's dismissal;2.3:h:H:the dispute with McNeill
2.5 1|2.2:h:H:the Governor-General dispute
3.b 1|
3.0 1|
3.1 1|
3.2 2|1.3:h:H:Phoenix Park altar
3.3 1|
3.4 1|1.4:h:H:radio arrangements
3.5 1|0.3:h:H:Cardinal Lauri;3.2:h:H:the Phoenix Park Mass
3.6 1|0.3:h:H:the legate
3.7 1|
3.8 1|0.3:h:H:Cardinal Lauri
3.9 2|3.2:h:H:the closing Mass
3.10 1|0.3:h:H:the Pope's legate
4.b 1|
4.0 1|
4.1 1|1.4:h:H:radio coverage
4.2 1|
4.3 1|1.1:h:H:de Valera's role
4.4 1|s5.1.b:h:H:the Civil War
4.5 1|0.3:h:H:Archbishop Byrne
4.6 1|1.4:e:H:the Athlone station;s10.4.3:h:H:Radio Éireann history
4.7 1|3.2:h:H:the Phoenix Park Mass crowd
5.b 1|
5.0 2|1.5:h:L:pilgrims from Northern Ireland
5.1 1|5.0:h:H:attacks on pilgrims
5.2 2|s3.0.b:h:H:partition and unionist resistance;5.0:h:L:attacks on pilgrims
5.3 1|5.2:h:L:unionist reaction
5.4 1|s3.0.b:h:H:partition and Northern nationalists
6.b 1|
6.0 1|s6.4.b:e:H:the 1937 constitution;s10.3.b:h:H:Catholic social legislation
6.1 1|s10.4.7:h:H:Gaelic and Catholic Ireland
6.2 1|1.1:h:L:de Valera's government
6.3 1|2.2:e:H:the Governor-General dispute;s6.1.1:h:H:McNeill's dismissal
6.4 1|5.2:e:H:unionist reaction to the Congress
6.5 1|4.3:h:H:the Congress as success
6.6 2|6.0:h:H:Church-state alliance
6.7 2|0.2:e:H:Congress planned by Cosgrave;1.0:h:H:Fianna Fáil in power
6.8 1|1.1:h:H:de Valera's government
6.9 1|4.7:e:H:the crowd comparison with 1979
7.b 1|
7.0 1|s5.1.b:h:H:the Civil War
7.1 1|
7.2 1|
7.3 1|5.2:e:H:unionist reaction;s3.0.b:h:H:partition
7.4 1|6.5:h:H:contemporary view
7.5 1|6.6:h:H:later view'''
build('hist-ire3-s11.t1g1.txt','hist-ire3-s11.t1g1.json','hist-ire3-s11.',s11,1)
