import json,re,sys
H='/Users/gabrielwhelan/barebones/drafts/crunch/history/'
def L(i,s,w,c='high'): return {"id":i,"strength":s,"why":w,"confidence":c}
E,H_='essential','helpful'
P1={
'0.b':(1,[]),'0.0':(2,[]),'0.1':(2,[]),'0.2':(1,[]),
'0.3':(1,[L('hist-eur4-s2.7.0',H_,'Soviet invasion of Afghanistan')]),
'0.4':(1,[L('hist-eur4-s4.6.1',H_,'arms agreements with Reagan','low')]),
'0.5':(1,[]),'0.6':(2,[]),'0.7':(2,[]),
'0.8':(2,[L('hist-eur4-s4.0.2',H_,'perestroika and openness')]),
'0.9':(1,[]),'0.10':(1,[]),
'1.b':(1,[]),'1.0':(2,[]),'1.1':(1,[]),
'1.2':(1,[L('hist-eur4-s4.4.1',H_,'Wałęsa and Solidarity')]),
'1.3':(1,[]),'1.4':(1,[]),
'1.5':(2,[L('hist-eur4-s4.5.b',H_,'1989 revolutions')]),
'1.6':(1,[L('hist-eur4-s4.1.1',E,'the 1979 papal visit')]),
'1.7':(1,[L('hist-eur4-s4.4.0',H_,'Gdańsk strikes of 1980')]),
'1.8':(2,[L('hist-eur4-s4.4.3',E,'martial law in Poland'),L('hist-eur4-s4.0.1',H_,'Gorbachev as Soviet leader','low')]),
'2.b':(1,[]),'2.0':(1,[]),'2.1':(2,[]),
'2.2':(1,[L('hist-eur4-s4.2.1',E,'October 1956 Polish settlement')]),
'2.3':(1,[]),
'2.4':(2,[L('hist-eur4-s4.2.1',H_,'Poland 1956 new leadership'),L('hist-eur4-s3.4.b',H_,'Hungary 1956 crushed'),L('hist-eur4-s4.3.2',H_,'1968 invasion of Czechoslovakia')]),
'2.5':(1,[L('hist-eur4-s4.2.1',H_,'Gomułka and Poland 1956')]),
'3.b':(1,[]),'3.0':(1,[L('hist-eur4-s4.2.3',H_,'Dubček and Prague Spring')]),
'3.1':(1,[L('hist-eur4-s4.2.3',H_,'Dubček government')]),
'3.2':(2,[L('hist-eur4-s4.2.3',H_,'Dubček as party leader')]),
'3.3':(1,[L('hist-eur4-s4.3.2',E,'the 1968 invasion')]),
'3.4':(2,[L('hist-eur4-s4.3.2',E,'the 1968 invasion')]),
'3.5':(1,[L('hist-eur4-s4.3.2',H_,'Dubček arrested after invasion')]),
'3.6':(1,[L('hist-eur4-s2.6.5',H_,'Helsinki human rights commitment')]),
'4.b':(1,[]),'4.0':(1,[]),'4.1':(1,[L('hist-eur4-s4.4.0',H_,'Solidarity origins')]),
'4.2':(1,[]),'4.3':(1,[]),
'4.4':(2,[L('hist-eur4-s4.4.3',E,'martial law'),L('hist-eur4-s4.3.4',H_,'fear of Soviet intervention','low')]),
'4.5':(1,[L('hist-eur4-s4.4.3',H_,'Solidarity banned')]),
'5.b':(1,[]),'5.0':(2,[L('hist-eur4-s4.4.5',H_,'Round Table talks')]),
'5.1':(2,[L('hist-eur4-s3.0.b',H_,'Imre Nagy')]),
'5.2':(1,[L('hist-eur4-s4.5.1',H_,'Hungary opening border')]),
'5.3':(1,[L('hist-eur4-s2.3.4',H_,'building of the Berlin Wall')]),
'5.4':(1,[L('hist-eur4-s4.3.6',H_,'Havel and Charter 77','low')]),
'5.5':(1,[]),
'6.b':(1,[]),'6.0':(1,[L('hist-eur4-s4.0.2',H_,'glasnost')]),
'6.1':(1,[L('hist-eur4-s2.7.2',H_,'Soviet intermediate-range missiles')]),
'6.2':(1,[L('hist-eur4-s4.3.4',E,'Brezhnev Doctrine')]),
'6.3':(1,[]),
'6.4':(1,[L('hist-eur4-s1.6.3',H_,'Warsaw Pact'),L('hist-eur4-s1.4.2',H_,'Comecon')]),
'6.5':(2,[L('hist-eur4-s4.6.9',H_,'Boris Yeltsin')]),
'6.6':(1,[L('hist-eur4-s4.6.5',H_,'August 1991 coup')]),
'6.7':(2,[L('hist-eur4-s4.6.1',H_,'INF Treaty')]),
'6.8':(1,[]),'6.9':(1,[]),
'6.10':(1,[L('hist-eur4-s4.6.5',E,'the August 1991 coup')]),
'7.b':(1,[]),
'7.0':(1,[L('hist-eur4-s1.5.5',H_,'East Germany founded'),L('hist-eur4-s1.5.4',H_,'West Germany founded')]),
'7.1':(2,[L('hist-eur4-s1.6.1',H_,'NATO')]),
'7.2':(1,[]),'7.3':(1,[]),'7.4':(1,[]),
'7.5':(2,[L('hist-eur4-s4.5.3',H_,'fall of the Berlin Wall'),L('hist-eur4-s4.7.0',H_,'Two Plus Four settlement')]),
'7.6':(2,[L('hist-eur4-s4.7.2',H_,'Slovenia and Croatia secession')]),
'7.7':(1,[L('hist-eur4-s4.7.2',E,'Slovenia and Croatia independence')]),
'8.b':(1,[]),
'8.0':(1,[L('hist-eur4-s2.7.0',H_,'Afghanistan withdrawal'),L('hist-eur4-s4.6.1',H_,'arms control')]),
'8.1':(1,[]),
'8.2':(2,[L('hist-eur4-s2.8.6',H_,'Reagan defence spending','low')]),
'8.3':(2,[L('hist-eur4-s4.4.b',H_,'Solidarity'),L('hist-eur4-s4.3.6',H_,'Charter 77')]),
'8.4':(2,[L('hist-eur4-s2.8.6',H_,'Reagan firm policy')]),
}
def N(s):return {'0.b':0}
P2={}
def p2(k,c,n=None):P2[k]=(c,[L('hist-ire2-s11.'+i,s,w,cf) for i,s,w,cf in (n or [])])
for k in ['0.b','0.0','0.1','0.2','0.5','0.6','0.7','0.8','0.9','1.b','1.0','1.1','1.2','1.3','1.4','1.6','1.7','2.b','2.0','2.1','2.2','2.3','2.5','2.7','3.b','3.0','3.1','3.2','4.b','4.0','4.2','4.3','4.5','4.6','5.b','5.0','5.1','5.2','5.3','5.4','5.6','6.b','6.0','6.1','6.2','6.5','6.6','6.7','7.b','7.0','7.1','7.3','7.5','8.b','8.1','8.3','8.5','8.6','9.b','9.0','9.1','9.2','9.4','9.5']: p2(k,1)
p2('0.3',2,[('0.2','helpful','history as historian account','high')])
p2('0.4',1,[('0.1','helpful','source versus evidence','high')])
p2('1.5',2); p2('1.8',1,[('1.6','essential','primary and secondary sources','high')])
p2('2.4',1,[('2.2','essential','bias','high')]); p2('2.6',2); 
p2('3.3',1,[('3.0','helpful','part (a) comprehension','high')])
for k in ['3.4','3.5','3.6','3.7','3.8']: p2(k,1,[('3.3','essential','part (a) approach','high')])
p2('4.1',1,[('4.0','helpful','point named in comparison','high')])
p2('4.4',1,[('2.2','helpful','author bias','low')])
p2('5.5',2,[('2.4','helpful','biased source still useful','high')])
p2('5.7',1,[('2.0','helpful','fact','high'),('2.1','helpful','opinion','high')])
p2('6.3',1); p2('6.4',1,[('2.4','helpful','opinion as attitude evidence','low')])
p2('7.2',2); p2('7.4',2); p2('7.6',2)
p2('8.0',2); p2('8.2',2); p2('8.4',2)
p2('9.3',2,[('7.b','helpful','part (d) essay','high')])
def run(pack,out,P,pre):
    txt=open(H+'packs/'+pack).read()
    tgt=txt.split('CANDIDATES')[0]
    ids=re.findall(r'^\[(hist-[^\]]+)\]',tgt,re.M)
    allids=set(re.findall(r'^\[(hist-[^\]]+)\]',txt,re.M))
    res={}
    for i in ids:
        k=i[len(pre):]
        c,n=P[k]  # KeyError if unjudged
        for x in n: assert x['id'] in allids and x['id']!=i,(i,x)
        res[i]={"cost":c,"needs":n}
    assert len(P)==len(ids),(len(P),len(ids))
    json.dump(res,open(H+'point-links/'+out,'w'),ensure_ascii=False,indent=1)
    r=json.load(open(H+'point-links/'+out))
    ln=sum(len(v['needs']) for v in r.values())
    print(out,len(r),ln,sum(v['cost']==2 for v in r.values()),sum(x['confidence']=='low' for v in r.values() for x in v['needs']))
run('hist-eur4-s4.t1g1.txt','hist-eur4-s4.t1g1.json',P1,'hist-eur4-s4.')
run('hist-ire2-s11.t1g1.txt','hist-ire2-s11.t1g1.json',P2,'hist-ire2-s11.')
