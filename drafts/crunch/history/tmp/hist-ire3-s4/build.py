import json,re
H='/Users/gabrielwhelan/barebones/drafts/crunch/history/'
def L(i,s,w,c='high'): return (i,s,w,c)
E,H_='essential','helpful'
P1='hist-ire3-s4.'
def r(x): return x if '-' in x else None
def lk(i): return i if i.startswith('hist-') else 'hist-ire3-s4.'+i
D1={
'0.b':(1,[]),
'0.0':(1,[L('hist-ire3-s2.5.6',H_,'George V speech and invitation')]),
'0.1':(1,[L('0.0',H_,'invitation and Truce')]),
'0.2':(2,[L('0.1',H_,'July talks'),L('hist-ire3-s3.1.0',H_,'six counties of Northern Ireland')]),
'0.3':(2,[L('0.2',E,'the British offer rejected')]),
'0.4':(1,[L('0.3',H_,'Crown and external association')]),
'0.5':(1,[L('0.3',H_,'association with Empire')]),
'0.6':(2,[L('hist-ire3-s2.5.8',H_,'reasons Britain sought talks')]),
'0.7':(1,[L('hist-ire3-s2.9.2',H_,'IRA short of arms')]),
'1.b':(1,[]),
'1.0':(2,[L('hist-ire3-s2.3.3',H_,'Dáil cabinet ministers','low')]),
'1.1':(1,[L('1.0',H_,'the Irish delegation')]),
'1.2':(1,[L('1.0',H_,'the Irish delegation')]),
'1.3':(2,[L('hist-ire3-s2.3.3',H_,'Brugha and cabinet roles'),L('1.0',H_,'delegation he stayed from')]),
'1.4':(1,[L('1.3',E,'de Valera staying in Dublin')]),
'1.5':(1,[L('1.0',H_,'the delegates')]),
'1.6':(1,[L('1.5',E,'plenipotentiary credentials')]),
'1.7':(2,[]),
'1.8':(1,[L('1.7',H_,'the British team')]),
'2.b':(1,[]),
'2.0':(1,[L('0.5',H_,'conference opening 11 October')]),
'2.1':(2,[L('0.3',E,'external association'),L('4.2',H_,'oath in the Treaty','low')]),
'2.2':(2,[L('hist-ire3-s3.1.0',H_,'six-county Northern Ireland'),L('4.5',H_,'Boundary Commission outcome')]),
'2.3':(1,[L('0.2',H_,'British demand for ports')]),
'2.4':(2,[L('0.2',H_,'free trade demand')]),
'2.5':(1,[L('hist-ire3-s3.7.b',H_,'Craig, Northern leader')]),
'2.6':(1,[L('1.3',H_,'cabinet and de Valera in Dublin')]),
'2.7':(1,[L('1.8',E,'Jones and Curtis as go-betweens'),L('1.7',H_,'Birkenhead on British team')]),
'3.b':(1,[]),
'3.0':(2,[L('2.2',E,'Boundary Commission and Ulster')]),
'3.1':(1,[L('2.1',E,'the oath dispute')]),
'3.2':(2,[L('3.1',H_,'cabinet instruction before signing'),L('2.5',H_,'Craig and the courier')]),
'3.3':(1,[L('3.2',E,'Lloyd George war threat')]),
'3.4':(2,[L('3.2',E,'war threat and deadline')]),
'3.5':(1,[L('1.0',H_,'five Irish delegates')]),
'3.6':(1,[L('3.5',H_,'the signing')]),
'3.7':(1,[L('1.6',H_,'instruction to report text')]),
'4.b':(1,[]),
'4.0':(1,[]),
'4.1':(1,[L('4.0',H_,'dominion status')]),
'4.2':(1,[L('2.1',H_,'oath dispute')]),
'4.3':(2,[L('2.3',H_,'British defence demands')]),
'4.4':(1,[L('2.4',H_,'debt and counter-claims')]),
'4.5':(2,[L('2.2',H_,'Boundary Commission and Ulster')]),
'4.6':(1,[]),
'4.7':(1,[L('hist-ire3-s3.1.0',H_,'Parliament of Southern Ireland')]),
'5.b':(1,[]),
'5.0':(1,[L('3.5',H_,'the Treaty signed')]),
'5.1':(1,[L('5.0',H_,'cabinet split on Treaty')]),
'5.2':(2,[L('0.3',E,'external association')]),
'5.3':(1,[]),
'5.4':(1,[]),
'5.5':(1,[L('hist-ire3-s2.3.1',H_,'1919 Declaration of Independence')]),
'5.6':(1,[]),
'5.7':(1,[]),
'5.8':(1,[L('5.7',E,'Dáil vote on Treaty')]),
'5.9':(1,[L('4.6',H_,'Provisional Government')]),
'6.b':(1,[]),
'6.0':(2,[L('hist-ire3-s2.0.0',H_,'Griffith founding Sinn Féin')]),
'6.1':(1,[L('hist-ire3-s2.0.5',H_,'1917 Sinn Féin presidency')]),
'6.2':(1,[L('hist-ire3-s2.7.4',H_,'de Valera American tour')]),
'6.3':(1,[L('2.2',H_,'Crown and Ulster talks')]),
'6.4':(1,[]),
'6.5':(1,[L('5.8',H_,'elected Dáil President')]),
'6.6':(1,[]),
'6.7':(1,[]),
'7.b':(1,[]),
'7.0':(1,[L('hist-ire3-s2.6.3',H_,'Collins as Finance and intelligence')]),
'7.1':(1,[L('1.7',H_,'Birkenhead and Churchill')]),
'7.2':(2,[L('2.2',E,'Boundary Commission clause')]),
'7.3':(1,[L('3.2',H_,'5 December war threat')]),
'7.4':(1,[L('5.4',H_,'freedom to achieve freedom')]),
'7.5':(1,[L('5.9',H_,'Provisional Government formed')]),
'7.6':(1,[L('7.0',H_,'Collins and the IRB')]),
'7.7':(1,[]),
'8.b':(1,[]),
'8.0':(1,[L('0.1',E,'July 1921 talks'),L('0.3',H_,'external association')]),
'8.1':(1,[L('1.3',E,'staying in Dublin'),L('1.6',H_,'delegates instructions')]),
'8.2':(1,[L('2.1',H_,'Crown and oath issue')]),
'8.3':(1,[L('1.6',H_,'instruction to report text')]),
'8.4':(2,[L('5.2',E,'Document No. 2'),L('0.3',H_,'external association')]),
'8.5':(1,[L('1.4',H_,'absence of de Valera','low')]),
'8.6':(2,[L('1.3',H_,'de Valera staying at home')]),
'9.b':(1,[]),
'9.0':(1,[L('4.0',H_,'Free State dominion status')]),
'9.1':(1,[L('4.b',H_,'Treaty terms: Crown, oath, bases')]),
'9.2':(1,[L('5.4',H_,'freedom to achieve freedom')]),
'9.3':(1,[L('3.2',H_,'ultimatum pressure to sign')]),
'9.4':(2,[]),
'9.5':(1,[L('4.5',H_,'Boundary Commission')]),
'9.6':(2,[L('3.3',H_,'ultimatum bluff'),L('1.3',H_,'de Valera absence')]),
}
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
build(H+'packs/hist-ire3-s4.t1g1.txt',H+'point-links/hist-ire3-s4.t1g1.json',D1,'hist-ire3-s4.')
