import json,re
B='/Users/gabrielwhelan/barebones/drafts/crunch/geography/'
P='geo-economic-eu-s1.';G='geo-graph-skills-s1.';W='geo-economic-globalisation-s3.';S4='geo-region-european-s4.';S3='geo-region-european-s3.'
c2={'3.0','3.2','3.4','4.2','6.3','7.1','7.2','8.0','9.0','9.1','9.2','10.0','11.1','12.0','12.1','12.2','12.4','13.0','5.2','1.3'}
E,H='essential','helpful'
def L(*a): return a
l1={
'1.b':[(P+'0.1',E,'contrasts with customs union')],
'1.1':[(P+'2.3',H,'uses the term tariff')],
'1.2':[(P+'1.1',E,'replaces non-tariff barriers')],
'1.3':[(P+'1.b',H,'single market extends beyond members')],
'2.2':[(P+'2.0',E,'uses exports and imports')],
'3.0':[(P+'2.4',E,'intra-EU and extra-EU terms')],
'3.1':[(P+'2.4',H,'intra-EU term')],
'3.3':[(P+'3.2',H,'contrast with the core')],
'3.4':[(P+'4.2',H,'supply chains around Germany')],
'3.b':[(P+'1.b',H,'single market lowers trade costs')],
'4.2':[(P+'4.1',H,'supply chains'),(P+'7.1',H,'2004 enlargement')],
'5.1':[(P+'5.0',E,'these ports')],
'5.2':[(P+'5.1',E,'port trade counted to Netherlands')],
'6.0':[(P+'0.1',H,'customs union'),(P+'1.b',H,'single market')],
'6.2':[(P+'6.1',H,'the euro')],
'6.4':[(P+'6.3',H,'transport links')],
'7.2':[(P+'2.4',E,'internal versus external partner'),(P+'2.3',H,'tariffs and quotas')],
'7.3':[(P+'7.2',E,'post-Brexit UK trade terms')],
'8.1':[(P+'0.1',E,'common external tariff')],
'9.0':[(P+'2.4',H,'extra-EU trade')],
'9.1':[(P+'2.4',H,'extra-EU trade')],
'9.2':[(P+'2.2',H,'trade surplus')],
'9.3':[(P+'2.2',H,'surplus and deficit')],
'11.b':[(P+'10.1',H,'energy imports')],
'11.1':[(P+'11.0',H,'Russian gas supply')],
'11.2':[(P+'11.1',H,'lost Russian gas')],
'11.3':[(P+'11.1',H,'reduction of Russian gas')],
'12.1':[(P+'12.0',H,'trade agreements')],
'12.3':[(P+'2.3',H,'duty-free and quota-free')],
'12.4':[(P+'2.3',H,'tariffs')],
'13.b':[(P+'8.1',H,'EU acts as one bloc')],
'13.0':[(P+'2.3',H,'tariffs'),(W+'8.6',H,'US 2025 tariff rise',"low")],
'13.1':[(P+'2.3',H,'tariff duties')],
'13.2':[(P+'13.0',E,'first dispute'),(P+'13.1',E,'second dispute'),(P+'8.1',H,'EU acts as one bloc')],
'14.0':[(P+'7.0',H,'size of market')],
'14.1':[(P+'10.0',H,'manufactured exports')],
'14.2':[(P+'10.1',H,'energy imports')],
'14.3':[(P+'12.2',H,'preferential agreements')],
'14.4':[(P+'10.2',H,'imports from China and Asia')],
'14.5':[(W+'7.b',H,'defines the trading triad')],
'14.6':[(P+'11.1',H,'sanctions on Russia'),(P+'13.0',H,'US tariff disputes'),(P+'7.2',H,'Brexit')],
'15.0':[(G+'0.4',H,'finding the largest value')],
'15.1':[(G+'4.5',H,'missing value from 100%')],
'15.2':[(P+'2.2',H,'surplus and deficit')],
}
l2={
'0.1':[(S4+'12.3',H,'EEC set up by Treaty of Rome')],
'1.b':[(S4+'13.1',H,'single market 1993')],
'3.4':[(S4+'14.3',H,'which eastern states joined 2004')],
'4.2':[(S4+'14.3',H,'2004 enlargement countries')],
'6.0':[(S4+'15.5',H,'Schengen area')],
'6.1':[(S3+'13.2',H,'euro benefits')],
'6.2':[(S3+'12.1',H,'euro members'),(S4+'13.3',H,'euro history','low')],
'7.1':[(S4+'14.3',H,'2004 enlargement'),(S4+'14.4',H,'2007 and 2013 joiners')],
'7.2':[(S3+'6.1',H,'UK left the EU')],
'7.3':[(S3+'6.2',H,'customs checks at border','low')],
'11.0':[(S3+'17.2',H,'invasion of Ukraine')],
}
def ids(path):
    t=open(path).read().split('\n\n')[0]
    return re.findall(r'^\[([^\]]+)\]',t,re.M),set(re.findall(r'^\[([^\]]+)\]',open(path).read(),re.M))
def build(pk,links,withcost):
    tid,allid=ids(B+'packs/geo-economic-eu-s1.%s.txt'%pk)
    out={}
    for i in tid:
        k=i[len(P):]
        needs=[{'id':x[0],'strength':x[1],'why':x[2],'confidence':x[3] if len(x)>3 else 'high'} for x in links.get(k,[])]
        d={'cost':2 if k in c2 else 1} if withcost else {}
        d['needs']=needs;out[i]=d
    assert set(links)<={i[len(P):] for i in tid},set(links)
    for v in out.values():
        for n in v['needs']: assert n['id'] in allid and len(n['why'].split())<=8,n
    json.dump(out,open(B+'point-links/geo-economic-eu-s1.%s.json'%pk,'w'),indent=1)
    j=json.load(open(B+'point-links/geo-economic-eu-s1.%s.json'%pk))
    nl=sum(len(v['needs']) for v in j.values())
    print(pk,len(j),nl,sum(v.get('cost')==2 for v in j.values()),sum(n['confidence']=='low' for v in j.values() for n in v['needs']))
build('t1g1',l1,True);build('t1g2',l2,False)
