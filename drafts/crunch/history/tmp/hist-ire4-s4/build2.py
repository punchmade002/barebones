import json,re,sys
H='/Users/gabrielwhelan/barebones/drafts/crunch/history/'
def mk(P,pre,spec,out):
    txt=open(H+'packs/'+P).read()
    tgt=[];allids=set()
    sect=None
    for l in txt.split('\n'):
        if l.startswith('TARGET'): sect='t'
        elif l.startswith('CANDIDATES'): sect='c'
        m=re.match(r'\[([^\]]+)\]',l)
        if m:
            allids.add(m.group(1))
            if sect=='t': tgt.append(m.group(1))
    res={}
    for k,v in spec.items():
        cost,needs=v
        res[pre+k]={'cost':cost,'needs':[{'id':pre+n.split('|')[0],'strength':'essential' if n.split('|')[1]=='e' else 'helpful','why':n.split('|')[2],'confidence':'high' if n.split('|')[3]=='H' else 'low'} for n in needs]}
    assert list(res)==tgt,(set(tgt)^set(res))
    for k,v in res.items():
        for n in v['needs']:
            assert n['id'] in allids and n['id']!=k,(k,n)
    json.dump(res,open(out,'w'),indent=1)
    nl=sum(len(v['needs']) for v in res.values())
    print(len(res),nl,sum(v['cost']==2 for v in res.values()),sum(n['confidence']=='low' for v in res.values() for n in v['needs']))
A={
'0.b':(1,[]),
'0.0':(1,[]),
'0.1':(1,['0.0|h|American wing of the IRB movement|H']),
'0.2':(1,['0.1|h|Fenian money|H']),
'0.3':(1,['0.1|h|Fenian raid|H']),
'0.4':(1,['0.3|e|second raid follows the first|H']),
'0.5':(1,['0.1|h|Fenian Brotherhood declined|H']),
'0.6':(1,['0.1|h|Fenian prisoners|H']),
'0.7':(1,['0.2|h|American money for violence|L']),
'1.b':(1,['0.1|h|Fenians of the 1860s|H']),
'1.0':(1,['0.0|e|Irish Republican Brotherhood|H']),
'1.1':(2,['1.0|h|treason-felony for Fenian recruiting|L']),
'1.2':(1,['0.5|e|Clan na Gael|H']),
'1.3':(1,['0.5|h|Clan na Gael organised rescue|H']),
'1.4':(2,['2.0|h|Davitt and the New Departure|H']),
'1.5':(1,['1.2|h|Irish-American republican cause|L']),
'1.6':(2,['1.2|h|Clan na Gael sent money|H']),
'1.7':(2,['4.5|h|Devoy-de Valera divisions|H']),
'1.8':(1,['1.7|h|quarrel with de Valera|L']),
'1.9':(1,['0.1|h|Fenian conspiracy|H']),
'2.b':(1,[]),
'2.0':(1,['1.4|h|New Departure|H']),
'2.1':(1,['2.0|h|Davitt and Parnell cooperation|L']),
'2.2':(1,['2.1|e|Land League fundraising|H']),
'2.3':(1,['2.1|e|Land League funds|H']),
'2.4':(2,['2.1|e|Land League campaign|H']),
'2.5':(1,['2.4|h|American money for evicted tenants|H']),
'3.b':(1,[]),
'3.0':(1,[]),
'3.1':(1,[]),
'3.2':(2,['3.0|h|Irish Parliamentary Party support|L']),
'3.3':(1,[]),
'3.4':(1,['1.3|e|Catalpa rescue|H']),
'4.b':(1,[]),
'4.0':(1,['0.5|h|Clan na Gael|H']),
'4.1':(1,['1.6|h|Cohalan and Devoy|H']),
'4.2':(1,['4.0|h|German help for the Rising|H']),
'4.3':(1,['4.1|e|Friends of Irish Freedom|H']),
'4.4':(1,['4.1|h|Irish-American organisation|L']),
'4.5':(1,['1.7|h|Devoy quarrel with de Valera|H']),
'5.b':(1,[]),
'5.0':(1,[]),
'5.1':(1,['5.0|e|partition and the border|H']),
'5.2':(1,['5.1|h|anti-partition case|H']),
'5.3':(2,[]),
'5.4':(1,['5.3|e|Republic of Ireland Act|H']),
'5.5':(1,['5.0|h|partition|H']),
'5.6':(1,['5.2|h|anti-partition campaign|H']),
'6.b':(1,[]),
'6.0':(1,[]),
'6.1':(1,['6.0|e|Ulster-Scots identity|H']),
'6.2':(1,[]),
'6.3':(1,[]),
'6.4':(1,['6.3|h|Orange Order abroad|H']),
'6.5':(2,['6.0|h|Scots-Irish network|H','6.3|h|Orange network|H','7.b|h|Bonar Law|H']),
'7.b':(1,[]),
'7.0':(1,[]),
'7.1':(1,['7.0|h|Bonar Law|H']),
'7.2':(1,['7.0|h|Bonar Law|H']),
'7.3':(1,['7.2|h|Conservative leader Bonar Law|H']),
'7.4':(1,['7.2|h|Conservative leader|H']),
'7.5':(1,['7.0|h|Bonar Law|H']),
'7.6':(1,['7.5|h|Lloyd George government|L']),
'7.7':(1,['7.4|h|his Ulster stand|H']),
'7.8':(2,['7.4|h|Conservative policy on Ulster|H']),
'8.0':(1,['0.5|h|Clan na Gael network|H','2.4|h|Land League funds|H']),
'8.1':(1,['0.2|e|Fenian rising of 1867|H','0.4|e|raids into Canada|H']),
'8.2':(1,['5.6|h|anti-partition campaign|H']),
'8.3':(1,['6.5|e|unionist lobbying abroad|H']),
'8.4':(1,[]),
'8.5':(2,[]),
}
mk('hist-ire4-s4.t1g1.txt','hist-ire4-s4.',A,H+'point-links/hist-ire4-s4.t1g1.json')
