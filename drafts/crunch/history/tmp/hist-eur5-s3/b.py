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
'0.b':(1,[]),'0.0':(1,[]),
'0.1':(1,['0.0|h|Zionist national homeland aim|H']),
'0.2':(1,[]),
'0.3':(2,['0.0|h|Zionism and Jewish immigration|H']),
'0.4':(1,['0.2|h|Mandate rule|H','0.6|e|Peel partition proposal|H']),
'0.5':(2,['0.3|h|Jewish immigration|H']),
'0.6':(1,['0.2|h|Transjordan|H']),
'1.0':(1,[]),'1.1':(1,[]),'1.2':(1,[]),
'1.3':(1,['1.2|e|Irgun|H']),
'1.4':(2,['1.1|e|Haganah|H','1.2|e|Irgun and Lehi|H']),
'1.5':(1,['0.5|h|British immigration restrictions|H']),
'1.6':(1,['1.0|h|Holocaust refugees|H']),
'2.b':(1,[]),'2.0':(1,[]),
'2.1':(2,['2.0|h|referral to the UN|H']),
'2.2':(1,['2.1|e|UN partition plan|H']),
'2.3':(1,['2.1|e|partition rejected|H']),
'2.4':(1,['2.1|h|partition|H']),
'2.5':(1,['3.0|h|Israel proclaimed|H']),
'2.6':(1,['2.1|e|partition plan|H']),
'2.7':(1,['2.3|h|fighting from December 1947|H']),
'3.b':(1,[]),
'3.0':(1,['7.b|h|Ben-Gurion|H']),
'3.1':(1,['3.0|e|declaration of Israel|H']),
'3.2':(2,['1.2|e|Irgun and Lehi|H']),
'3.3':(2,['2.7|h|flight of Arabs in civil war|H']),
'3.4':(1,['2.1|e|UN plan|H']),
'3.5':(1,['3.4|e|West Bank|H']),
'3.6':(2,['3.1|h|first Arab-Israeli war|H']),
'3.7':(1,['3.0|h|declaration of Israel|H']),
'4.0':(1,[]),'4.1':(1,[]),'4.2':(1,[]),
'4.3':(1,['4.0|h|Nasser|H']),
'4.4':(1,['4.0|h|Nasser|H']),
'4.5':(2,['4.3|e|Soviet-bloc arms deal|H']),
'4.6':(2,['4.3|h|Nasser seeking arms|H']),
'5.b':(1,[]),'5.0':(2,[]),
'5.1':(1,['5.0|e|Suez Canal Company|H','4.5|h|Aswan High Dam|H']),
'5.2':(2,['5.1|e|nationalisation of canal|H']),
'5.3':(2,['5.2|e|Sèvres plan|H']),
'5.4':(2,['5.3|e|ultimatum and bombing|H']),
'5.5':(1,['5.4|h|the invasion|H']),
'5.6':(1,['5.4|h|the invasion|H']),
'5.7':(2,['5.4|h|withdrawal supervised|H']),
'5.8':(1,['5.5|h|Eisenhower angry at allies|L']),
'5.9':(1,['5.4|e|Port Said landings|H']),
'6.0':(1,['5.5|h|American pressure on Britain|H']),
'6.1':(1,['5.3|e|Israeli invasion of Sinai|H']),
'6.2':(1,['5.4|h|Anglo-French invasion|H']),
'6.3':(1,['5.1|h|canal nationalisation|H']),
'6.4':(1,['5.5|h|US pressure at Suez|H']),
'6.5':(2,['6.4|h|loss of Western position|H']),
'6.6':(1,['4.2|e|Baghdad Pact|H']),
'7.b':(1,[]),'7.0':(1,[]),
'7.1':(2,['2.1|e|1947 partition plan|H']),
'7.2':(2,['3.0|h|proclaiming Israel|H']),
'7.3':(2,['5.2|e|Sèvres talks|H','1.2|h|Irgun|H']),
'7.4':(1,['3.3|h|displaced Palestinians|H']),
'7.5':(2,['3.3|e|1948 expulsions|H']),
'8.b':(1,[]),
'8.0':(1,['4.0|h|Free Officers overthrow Farouk|H']),
'8.1':(1,['4.5|h|Aswan High Dam|H']),
'8.2':(1,['5.1|e|nationalisation of canal|H']),
'8.3':(1,[]),
'8.4':(1,['5.1|h|Suez nationalisation|L']),
'8.5':(2,['8.6|h|military failure of 1967|H']),
'8.6':(2,[]),
'8.7':(1,['8.6|e|1967 defeat|H']),
'9.0':(2,['2.0|h|referral to the UN|H']),
'9.1':(2,['0.1|h|conflicting promises|H','3.3|h|refugees|H']),
'9.2':(2,['5.3|e|Israeli advance in Sinai|H','5.4|e|Anglo-French advance|H']),
'9.3':(2,['5.5|e|US forced ceasefire|H','5.6|h|Soviet threat|H']),
'9.4':(2,['5.2|e|collusion with Israel|H']),
'9.5':(2,['0.1|e|1917 declaration|H','0.5|e|1939 White Paper|H']),
}
mk('hist-eur5-s3.t1g1.txt','hist-eur5-s3.',A,H+'point-links/hist-eur5-s3.t1g1.json')
