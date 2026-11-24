import json,re
H='/Users/gabrielwhelan/barebones/drafts/crunch/history/'
def L(i,s,w,c='high'): return (i,s,w,c)
E,H_='essential','helpful'
P1='hist-ire3-s4.'
def r(x): return x if '-' in x else None
def lk(i): return i if i.startswith('hist-') else 'hist-ire3-s4.'+i
def build(pack,out,D,pre,hascost=True):
    t=open(pack).read()
    tgt=re.findall(r'^\[(%s[^\]]+)\]'%re.escape(pre),t.split('CANDIDATES')[0],re.M)
    allids=set(re.findall(r'^\[([^\]]+)\]',t,re.M))
    assert set(pre+k for k in D)==set(tgt) and len(tgt)==len(D),(set(tgt)^set(pre+k for k in D))
    res={}
    for i in tgt:
        c,ls=D[i[len(pre):]]
        needs=[]
        for a,s,w,cf in ls:
            a=a if a.startswith('hist-') else pre+a
            assert a in allids and a!=i,(i,a)
            needs.append({'id':a,'strength':s,'why':w,'confidence':cf})
        res[i]={'cost':c,'needs':needs}
    json.dump(res,open(out,'w'),ensure_ascii=False,indent=1)
    n=sum(len(v['needs']) for v in res.values())
    print(len(res),n,sum(v['cost']==2 for v in res.values()),sum(x['confidence']=='low' for v in res.values() for x in v['needs']))
D2={
'0.b':(1,[]),'0.0':(1,[]),'0.1':(1,[]),'0.2':(1,[]),'0.3':(1,[]),'0.4':(1,[]),
'0.5':(1,[L('0.0',H_,'baby boom generation')]),
'0.6':(1,[L('0.2',H_,'move to suburbs')]),
'0.7':(2,[L('0.2',H_,'white middle-class suburbanisation')]),
'0.8':(1,[L('0.3',H_,'Sun Belt growth')]),
'1.b':(1,[]),'1.0':(1,[]),
'1.1':(1,[L('hist-eur6-s6.0.4',H_,'GI Bill home loans')]),
'1.2':(1,[L('1.1',H_,'federal mortgage guarantees')]),
'1.3':(1,[L('hist-eur6-s6.2.0',H_,'Interstate Highway programme')]),
'1.4':(1,[]),
'1.5':(2,[L('1.0',H_,'Levittown houses')]),
'1.6':(1,[L('1.2',H_,'exclusion of black buyers')]),
'1.7':(1,[L('1.b',H_,'suburban abundance')]),
'2.b':(1,[]),'2.0':(1,[]),
'2.1':(1,[L('2.0',H_,'charge cards and credit')]),
'2.2':(1,[L('1.4',H_,'television advertising')]),
'2.3':(1,[]),'2.4':(1,[]),
'2.5':(1,[L('1.4',H_,'television in homes')]),
'2.6':(1,[L('2.2',H_,'advertising techniques')]),
'2.7':(1,[L('1.3',H_,'car-based suburbs')]),
'3.b':(1,[]),'3.0':(1,[]),'3.1':(1,[]),'3.2':(1,[]),
'3.3':(1,[L('hist-eur6-s6.4.0',H_,'Whyte and The Organization Man')]),
'3.4':(1,[]),
'4.b':(1,[]),
'4.0':(1,[L('hist-eur6-s6.0.0',H_,'wartime industrial jobs')]),
'4.1':(1,[]),'4.2':(1,[]),'4.3':(1,[]),'4.4':(1,[]),
'4.5':(1,[L('2.1',H_,'credit access')]),
'4.6':(1,[]),
'4.7':(2,[]),
'4.8':(2,[L('4.2',H_,'contraception')]),
'4.9':(1,[]),
'4.10':(1,[L('5.5',H_,'Equal Rights Amendment')]),
'5.b':(1,[]),'5.0':(1,[]),
'5.1':(1,[L('5.0',H_,'Friedan and Smith College')]),
'5.2':(2,[L('5.1',E,'The Feminine Mystique')]),
'5.3':(1,[L('5.2',E,'The Feminine Mystique argument')]),
'5.4':(1,[L('5.3',H_,'book launching second wave')]),
'5.5':(2,[L('5.4',E,'NOW pressing for ERA')]),
'5.6':(1,[L('5.2',H_,'her campaigning for women')]),
'5.7':(1,[L('5.2',H_,'The Feminine Mystique')]),
'5.8':(1,[L('5.4',H_,'her feminist organising')]),
'5.9':(1,[L('5.4',H_,'her movement leadership')]),
'6.b':(1,[]),
'6.0':(2,[]),
'6.1':(1,[L('6.0',H_,'Monroe film career')]),
'6.2':(1,[L('6.1',H_,'Monroe image')]),
'6.3':(1,[L('6.1',H_,'Hollywood sex symbol image')]),
'6.4':(1,[L('6.1',H_,'Monroe image')]),
'6.5':(1,[L('6.3',H_,'glamour and constraint')]),
'6.6':(1,[L('6.0',H_,'her Fox contract career')]),
'6.7':(1,[L('5.2',E,'Friedan attacked feminine ideal')]),
'7.b':(1,[]),
'7.0':(1,[L('1.1',H_,'federal mortgage and home ownership')]),
'7.1':(2,[L('1.2',E,'racial exclusion from suburbs')]),
'7.2':(1,[L('4.5',E,'1974 Credit Act')]),
'7.3':(2,[L('5.2',E,'Friedan critique of domestic ideal')]),
}
build(H+'packs/hist-eur6-s8.t1g1.txt',H+'point-links/hist-eur6-s8.t1g1.json',D2,'hist-eur6-s8.')
