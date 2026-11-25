import json,re
H='/Users/gabrielwhelan/barebones/drafts/crunch/history/'
E,Hh='essential','helpful'
def L(i,s,w,c='high'): return {"id":i,"strength":s,"why":w,"confidence":c}
def build(pack,out,data,pre):
    txt=open(H+'packs/'+pack).read()
    tgt=txt.split('CANDIDATES')[0]
    tids=re.findall(r'^\[([^\]]+)\]',tgt,re.M)
    allids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
    res={}
    for k in tids:
        short=k[len(pre):]
        assert short in data,k
        c,n=data[short]
        res[k]={"cost":c,"needs":[L(pre+a if a.startswith('.') else a,s,w,cf) if False else L(a if a.startswith('hist-') else pre+a,s,w,cf) for a,s,w,cf in n]}
    assert set(data)==set(k[len(pre):] for k in tids)
    for k,v in res.items():
        for n in v['needs']: assert n['id'] in allids and n['id']!=k,(k,n)
    json.dump(res,open(H+'point-links/'+out,'w'),indent=1)
    d=json.load(open(H+'point-links/'+out))
    ln=sum(len(v['needs']) for v in d.values())
    print(pack,len(d),ln,sum(v['cost']==2 for v in d.values()),sum(n['confidence']=='low' for v in d.values() for n in v['needs']))
P='hist-ire6-s5'
d1={
'0.b':(1,[]),
'0.0':(1,[('hist-ire6-s1.1.1',Hh,'Republic of Ireland Act 1948','high')]),
'0.1':(1,[('.0.0',E,'follows the declaration of a republic','high')]),
'0.2':(1,[('.0.1',E,'the Ireland Act 1949','high')]),
'0.3':(1,[('.0.2',E,'Northern Ireland consent guarantee','high')]),
'0.4':(1,[]),
'0.5':(1,[]),
'1.0':(1,[('hist-ire6-s1.0.2',Hh,'the Inter-Party Government','high')]),
'1.1':(1,[('.1.0',E,'the anti-partition campaign','high')]),
'1.2':(1,[('.1.0',Hh,'the anti-partition campaign','high')]),
'1.3':(2,[('hist-ire6-s1.5.5',Hh,'IRA Border Campaign began 1956','high')]),
'1.4':(1,[('hist-ire6-s2.1.5',Hh,'economic recovery via First Programme','low')]),
'2.0':(1,[('hist-ire6-s1.6.3',Hh,'cattle exports to Britain','high')]),
'2.1':(1,[]),
'2.2':(1,[('.2.0',E,'dependence on British market','high'),('hist-ire6-s2.6.0',Hh,'Ireland applied to EEC with Britain','high'),('hist-ire6-s2.6.2',Hh,'Anglo-Irish Free Trade Agreement','high')]),
'2.3':(2,[('hist-ire6-s4.0.4',E,'European Monetary System','high'),('.2.0',Hh,'exports to Britain','high')]),
'3.b':(1,[]),
'3.0':(1,[('hist-ire6-s2.5.0',Hh,'Lemass as Taoiseach','high')]),
'3.1':(1,[('.3.0',E,'Lemass-O\'Neill meetings','high')]),
'3.2':(1,[('.3.0',E,'the 1965 meetings','high'),('.1.0',Hh,'1950s anti-partition rhetoric','high')]),
'3.3':(1,[('.3.0',E,'the 1965 meetings','high')]),
'3.4':(1,[('hist-ire6-s2.6.2',Hh,'Anglo-Irish Free Trade Agreement','high')]),
'4.b':(1,[]),
'4.0':(1,[('hist-ire6-s4.1.3',Hh,'Lynch\'s 1969 broadcast','high')]),
'4.1':(1,[('hist-ire6-s4.2.b',Hh,'the Arms Crisis','high')]),
'4.2':(1,[('hist-ire6-s4.1.4',Hh,'Lynch\'s Northern policy','low')]),
'4.3':(2,[]),
'4.4':(1,[]),
'4.5':(1,[('.4.4',E,'the aftermath of Bloody Sunday','high')]),
'4.6':(1,[('.4.4',Hh,'Bloody Sunday prompting action','high')]),
'4.7':(1,[('.4.0',Hh,'August 1969 rioting','high')]),
'5.0':(1,[('hist-ire6-s2.6.0',Hh,'Ireland\'s EEC application','low')]),
'5.1':(1,[('hist-ire6-s4.6.0',Hh,'Garret FitzGerald','high')]),
'5.2':(2,[('.5.1',Hh,'the coalition government','high'),('.4.6',Hh,'Stormont suspended, direct rule','low')]),
'5.3':(2,[('.5.2',E,'Sunningdale Agreement','high')]),
'5.4':(1,[('.5.2',E,'Sunningdale Agreement','high'),('.0.2',Hh,'consent principle','high')]),
'5.5':(1,[('.5.3',E,'Council of Ireland and executive','high')]),
'5.6':(1,[('.5.5',E,'the Ulster Workers\' Council strike','high')]),
'6.0':(2,[]),
'6.1':(1,[('hist-ire6-s4.4.b',Hh,'Charles Haughey','high')]),
'6.2':(2,[('.6.1',E,'Haughey-Thatcher meetings','high')]),
'6.3':(1,[]),
'6.4':(1,[('hist-ire6-s4.6.b',Hh,'Garret FitzGerald','high'),('.6.1',Hh,'Thatcher as Prime Minister','high')]),
'6.5':(2,[('hist-ire6-s4.5.2',Hh,'Haughey in office 1982','high')]),
'6.6':(1,[('.6.5',E,'Haughey\'s Falklands stance','high')]),
'6.7':(1,[]),
'7.b':(1,[]),
'7.0':(2,[('hist-ire6-s4.6.5',Hh,'FitzGerald set up the Forum','high')]),
'7.1':(1,[('.7.0',E,'the Forum\'s three options','high')]),
'7.2':(2,[('.7.1',Hh,'Thatcher rejected the Forum report','high')]),
'7.3':(1,[('.7.2',E,'Anglo-Irish Agreement','high'),('.0.2',Hh,'consent principle','high')]),
'7.4':(1,[('.7.2',E,'Anglo-Irish Agreement','high')]),
'7.5':(1,[('.7.2',E,'Anglo-Irish Agreement','high')]),
'7.6':(1,[('.7.2',E,'Anglo-Irish Agreement','high')]),
'7.7':(1,[('.7.2',E,'Anglo-Irish Agreement','high')]),
'8.0':(1,[('.7.4',E,'Intergovernmental Conference','high')]),
'8.1':(1,[]),
'8.2':(1,[]),
'8.3':(1,[('.7.2',E,'1985 Anglo-Irish Agreement','high'),('.7.6',Hh,'Progressive Democrats','high')]),
'8.4':(2,[('.5.0',Hh,'joint EEC membership 1973','high')]),
'9.0':(2,[('.0.1',E,'Ireland Act 1949','high'),('.7.3',Hh,'consent principle in 1985','high'),('.7.4',Hh,'1985 consultative role','high')]),
'9.1':(2,[('.5.5',E,'Sunningdale collapse','high'),('.7.2',E,'1985 agreement','high')]),
'9.2':(1,[('.7.2',E,'Anglo-Irish Agreement','high')]),
'9.3':(2,[('.7.2',E,'Anglo-Irish Agreement','high')]),
}
d1={k:(c,[(P+a if a.startswith('.') else a,s,w,cf) for a,s,w,cf in n]) for k,(c,n) in d1.items()}
build('hist-ire6-s5.t1g1.txt','hist-ire6-s5.t1g1.json',d1,P+'.')
P2='hist-ire2-s8'
d2={
'0.b':(1,[]),'0.0':(1,[]),'0.1':(1,[]),'0.2':(1,[]),
'0.3':(1,[('.0.2',Hh,'Danish butter competition','high')]),
'0.4':(1,[('.0.3',E,'co-operative creameries model','high')]),
'0.5':(1,[('.0.0',E,'Horace Plunkett','high')]),
'0.6':(1,[('.0.5',Hh,'AE and the Irish Homestead','high')]),
'1.b':(1,[('.0.0',Hh,'Horace Plunkett','high')]),
'1.0':(1,[('.0.3',Hh,'co-operative societies','high')]),
'1.1':(1,[('.1.0',E,'the IAOS','high')]),
'1.2':(1,[('.0.3',Hh,'co-operative creameries','high')]),
'1.3':(1,[('.0.2',Hh,'moneylenders and shopkeepers','high')]),
'1.4':(1,[]),
'1.5':(2,[('.1.0',Hh,'co-operative societies body','low')]),
'1.6':(1,[('.0.3',Hh,'creamery separators','high')]),
'2.b':(1,[('.0.0',Hh,'Horace Plunkett','high')]),
'2.0':(1,[]),
'2.1':(1,[('.2.0',E,'the Recess Committee','high')]),
'2.2':(2,[('.2.1',E,'Recess Committee recommendation','high'),('.0.0',Hh,'Plunkett','high')]),
'2.3':(1,[('.2.2',E,'DATI','high')]),
'2.4':(1,[('.2.2',E,'Plunkett as DATI vice-president','high')]),
'2.5':(1,[('.2.2',E,'DATI','high'),('.2.4',Hh,'Plunkett losing vice-presidency','high')]),
'3.b':(1,[]),
'3.0':(1,[('.0.1',Hh,'Plunkett as Unionist MP','high')]),
'3.1':(1,[('.0.1',Hh,'Plunkett as Unionist','high')]),
'3.2':(2,[('.0.1',Hh,'Plunkett\'s 1900 defeat','low')]),
'3.3':(1,[('.1.2',Hh,'creameries competing','high')]),
'3.4':(1,[]),
'3.5':(1,[('hist-ire2-s2.5.2',E,'Congested Districts Board','high')]),
'4.b':(1,[]),
'4.0':(2,[]),'4.1':(1,[]),'4.2':(1,[]),'4.3':(1,[]),'4.4':(1,[]),'4.5':(1,[]),
'4.6':(1,[('.4.1',Hh,'linen industry','high')]),
'4.7':(1,[]),'4.8':(1,[]),
'5.b':(1,[]),'5.0':(1,[]),
'5.1':(2,[('.5.0',Hh,'Harland and Wolff yard','high')]),
'5.2':(1,[('.5.0',Hh,'Harland and Wolff yard','low')]),
'5.3':(1,[('.5.2',E,'the Titanic','high')]),
'5.4':(1,[]),
'5.5':(1,[('.5.0',Hh,'Harland and Wolff','high')]),
'5.6':(1,[('.5.2',Hh,'Olympic and Titanic','high')]),
'6.b':(1,[]),
'6.0':(1,[('.4.1',Hh,'linen mills','high')]),
'6.1':(1,[]),'6.2':(1,[]),'6.3':(2,[]),
'6.4':(1,[('.6.2',Hh,'Protestant dominance of skilled jobs','low')]),
'6.5':(1,[]),
'6.6':(1,[('.6.2',Hh,'Protestant industrial interests','low')]),
'6.7':(1,[('.6.0',Hh,'mill workers','high')]),
'7.b':(1,[]),
'7.0':(1,[('.4.1',Hh,'linen','high'),('.5.b',Hh,'shipbuilding','high')]),
'7.1':(1,[]),'7.2':(1,[]),'7.3':(1,[]),
'7.4':(1,[('.7.0',Hh,'Belfast\'s export economy','high'),('.6.6',Hh,'industrial interests and unionism','high')]),
'7.5':(1,[('.4.5',Hh,'Catholic districts of Belfast','high')]),
'8.b':(1,[]),
'8.0':(2,[('.3.4',Hh,'co-operative results','high'),('.4.b',Hh,'Belfast industrial growth','high')]),
'8.1':(2,[('.3.5',Hh,'western farmers and Ulster','high'),('.6.2',Hh,'sectarian divisions in work','high')]),
'8.2':(1,[('.3.0',Hh,'nationalist suspicion of Plunkett','high'),('.6.6',Hh,'unionist Belfast and the Union','high')]),
'8.3':(2,[('hist-ire2-s2.8.b',Hh,'land reform comparison','high')]),
}
d2={k:(c,[(P2+a if a.startswith('.') else a,s,w,cf) for a,s,w,cf in n]) for k,(c,n) in d2.items()}
build('hist-ire2-s8.t1g1.txt','hist-ire2-s8.t1g1.json',d2,P2+'.')
