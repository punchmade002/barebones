import json,re
P='/Users/gabrielwhelan/barebones/drafts/crunch/geography/'
S='geo-region-european-s4.'
C='geo-region-concept-s3.'
def L(i,s,w,c='high'): return {"id":i,"strength":s,"why":w,"confidence":c}
# (cost, links) per target id suffix, every id explicit
T={
'0.b':(1,[L(C+'1.b','helpful','Gaeltacht as cultural region')]),
'0.0':(2,[]),'0.1':(1,[]),'0.2':(1,[]),'0.3':(1,[]),
'0.4':(1,[L(S+'0.0','helpful','compares with 1851 figure')]),
'1.b':(1,[]),'1.0':(1,[]),'1.1':(1,[]),
'1.2':(2,[L(C+'1.b','helpful','what the Gaeltacht is')]),
'1.3':(2,[L(S+'1.2','essential','1926 two-type definition')]),
'1.4':(2,[L(S+'1.3','essential','Breac-Ghaeltacht districts')]),
'1.5':(1,[]),
'2.b':(1,[]),'2.0':(1,[]),
'2.1':(2,[L(C+'1.5','helpful','state-created Gaeltacht')]),
'2.2':(1,[]),'2.3':(2,[]),'2.4':(2,[]),
'3.b':(1,[]),
'3.0':(2,[L(S+'1.5','essential','Gaeltarra Éireann replaced')]),
'3.1':(1,[]),'3.2':(1,[]),'3.3':(1,[]),'3.4':(1,[]),'3.5':(1,[]),
'4.b':(1,[]),
'4.0':(2,[L(S+'1.4','helpful','earlier fixed-map boundaries','low')]),
'4.1':(2,[L(S+'4.0','essential','Gaeltacht defined by language use')]),
'4.2':(1,[L(S+'4.1','helpful','core planning areas')]),
'5.b':(1,[]),'5.0':(2,[]),
'5.1':(1,[L(S+'5.0','essential','refers to the 2007 study')]),
'5.2':(1,[]),'5.3':(1,[]),'5.4':(1,[]),
'6.b':(1,[]),'6.0':(1,[]),
'6.1':(1,[L(S+'3.0','essential','Údarás na Gaeltachta role')]),
'6.2':(1,[]),
'6.3':(1,[L(S+'4.1','essential','Language Planning Areas')]),
'6.4':(1,[L(S+'3.1','helpful','TG4 and Raidió na Gaeltachta')]),
'7.b':(1,[]),
'7.0':(1,[L(C+'3.4','helpful','language border in Belgium')]),
'7.1':(2,[L(C+'3.1','helpful','Belgian regions and communities')]),
'8.b':(1,[]),'8.0':(2,[]),'8.1':(1,[]),'8.2':(1,[]),'8.3':(1,[]),'8.4':(1,[]),
'9.b':(1,[]),'9.0':(1,[]),
'9.1':(2,[L('geo-region-concept-s2.3.1','helpful','Dublin split into four councils')]),
'9.2':(1,[L('geo-region-concept-s2.4.0','helpful','corporations renamed city councils')]),
'9.3':(2,[L(S+'9.1','helpful','the four Dublin authorities')]),
'9.4':(1,[]),
'9.5':(2,[L(S+'9.4','essential','Dublin Regional Authority replaced')]),
'10.b':(1,[]),'10.0':(2,[]),'10.1':(2,[]),'10.2':(2,[]),
'10.3':(1,[L(S+'8.1','helpful','Ballymun regeneration')]),
'10.4':(1,[]),
'10.5':(1,[L(S+'10.4','helpful','directly elected mayor')]),
'11.b':(1,[]),
'11.0':(1,[L('geo-region-concept-s2.5.0','helpful','Cork boundary extension')]),
'11.1':(1,[]),'11.2':(2,[]),
'11.3':(1,[L(S+'11.2','essential','BMW region')]),
'11.4':(1,[L(S+'11.2','helpful','economic regions drawn for EU')]),
'12.b':(1,[]),'12.0':(2,[]),
'12.1':(1,[L(S+'12.0','helpful','coal and steel pooling')]),
'12.2':(1,[L(S+'12.1','helpful','Schuman proposal put into practice')]),
'12.3':(1,[L(S+'12.2','helpful','follows ECSC')]),
'12.4':(1,[]),
'13.b':(1,[]),'13.0':(1,[]),'13.1':(1,[]),'13.2':(1,[]),'13.3':(1,[]),'13.4':(1,[]),
'14.b':(1,[]),'14.0':(1,[]),'14.1':(1,[]),'14.2':(1,[]),'14.3':(2,[]),'14.4':(1,[]),'14.5':(1,[]),
'15.b':(1,[]),'15.0':(1,[]),'15.1':(2,[]),
'15.2':(1,[L(S+'15.0','helpful','fall of communism')]),
'15.3':(1,[L(S+'15.2','helpful','newer members')]),
'15.4':(1,[L(S+'15.2','helpful','newer members')]),
'15.5':(1,[]),
'16.b':(1,[]),
'16.0':(1,[L(S+'14.3','essential','2004 new members')]),
'16.1':(1,[]),'16.2':(1,[]),
'16.3':(2,[L(S+'11.3','helpful','EU regional funding')]),
'16.4':(1,[L(S+'16.3','helpful','investment competition')]),
'17.b':(1,[]),
'17.0':(1,[L(S+'13.1','helpful','single market')]),
'17.1':(1,[L(S+'15.1','essential','Copenhagen criteria')]),
'18.b':(1,[]),'18.0':(1,[]),'18.1':(1,[]),'18.2':(1,[]),'18.3':(1,[]),
'18.4':(1,[L(C+'6.4','helpful','nationalists and unionists')]),
'18.5':(1,[L(S+'18.4','essential','nationalist minority in north')]),
'18.6':(1,[]),
'19.b':(1,[]),'19.0':(1,[]),'19.1':(1,[]),'19.2':(1,[]),
'19.3':(1,[L(S+'19.2','helpful','Bosnian war')]),
'19.4':(2,[]),'19.5':(2,[]),
'20.b':(1,[]),'20.0':(2,[]),'20.1':(1,[]),'20.2':(1,[]),
'20.3':(1,[L(S+'20.2','helpful','Berlin division ended')]),
'21.b':(1,[]),'21.0':(1,[]),
'21.1':(1,[L(S+'21.0','essential','USSR break-up')]),
'21.2':(1,[]),
'22.b':(1,[]),'22.0':(1,[]),
'22.1':(1,[L(S+'22.0','helpful','division of Cyprus')]),
'22.2':(1,[]),'22.3':(2,[]),
'22.4':(1,[L(S+'14.3','helpful','2004 ten new members')]),
'23.b':(1,[]),'23.0':(1,[]),'23.1':(1,[]),
'24.b':(1,[]),'24.0':(1,[]),
'24.1':(1,[L(S+'7.1','helpful','Belgium language regions')]),
'24.2':(1,[]),
}
I='geo-region-ireland-s1.'
U={
'8.b':[L(I+'1.b','helpful','core region idea','low')],
'8.0':[L(I+'37.1','helpful','Wright Report new towns')],
'8.1':[L(I+'37.2','helpful','Ballymun high-rise demolition')],
'8.3':[L(I+'0.0','helpful','which counties form GDA')],
'8.4':[L(I+'37.5','helpful','commuter towns named')],
'9.1':[L(I+'0.1','helpful','four Dublin authorities')],
'10.0':[L(I+'38.0','helpful','urban sprawl')],
'10.2':[L(I+'29.0','helpful','M50 and radial motorways')],
'10.3':[L(I+'31.0','helpful','IFSC set up 1987')],
'2.1':[L(I+'40.3','helpful','Ráth Chairn Gaeltacht','low')],
}
ids=[l.split(']')[0][1:] for l in open(P+'packs/geo-region-european-s4.t1g1.txt').read().split('CANDIDATES')[0].splitlines() if l.startswith('[')]
assert [i[len(S):] for i in ids]==list(T), (set(ids^0 if 0 else 0))
out1={i:{"cost":T[i[len(S):]][0],"needs":T[i[len(S):]][1]} for i in ids}
out2={i:{"needs":U.get(i[len(S):],[])} for i in ids}
for n,o in (('t1g1',out1),('t1g2',out2)):
    pk=open(P+'packs/geo-region-european-s4.%s.txt'%n).read()
    ok=set(re.findall(r'^\[([^\]]+)\]',pk,re.M))
    assert set(o)==set(ids)
    for v in o.values():
        for x in v['needs']: assert x['id'] in ok,(n,x['id'])
    json.dump(o,open(P+'point-links/geo-region-european-s4.%s.json'%n,'w'),ensure_ascii=False,indent=0)
    ln=sum(len(v['needs']) for v in o.values()); lo=sum(x['confidence']=='low' for v in o.values() for x in v['needs'])
    print(n,len(o),ln,sum(v.get('cost')==2 for v in o.values()),lo)
