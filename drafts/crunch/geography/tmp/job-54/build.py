import json,re
G='/Users/gabrielwhelan/barebones/drafts/crunch/geography/'
P='geo-option-culture-identity-s6.'
# explicit id list per block
blocks={0:'b0123',1:'b01234',2:'b0123',3:'b01234',4:'b01',5:'b01234',6:'b012',7:'b01',8:'b0123',9:'b012',10:'b012',11:'b012',12:'b012',13:'b0123',14:'b0123',15:'b01',16:'b012',17:'b012',18:'b012',19:'b0123',20:'b012',21:'b0123',22:'b01',23:'b01234',24:'b01',25:'b0123',26:'b01234',27:'b0123',28:'b0123',29:'b012345',30:'b012'}
ids=[P+str(n)+'.'+c for n,s in blocks.items() for c in s]
cost2={'3.3','5.0','5.1','8.1','8.2','9.2','14.1','15.0','17.0','20.1','23.2','23.3','26.2','26.3','27.0','27.1','28.3','29.3','29.4','12.2','21.2','0.1','18.0'}
def L(i,s,w,c='high'): return {'id':i,'strength':s,'why':w,'confidence':c}
H,E='helpful','essential'
own={ # within-package-1 links
'0.2':[L(P+'0.1',H,'uses the six headings')],
'1.1':[L(P+'1.0',H,'Alps and Jura mountains')],
'1.2':[L(P+'1.0',H,'mountain geography isolating valleys')],
'2.1':[L(P+'2.0',H,'cantons joining the alliance')],
'3.0':[L(P+'2.0',H,'cantons')],
'3.1':[L(P+'3.0',E,'war the 1848 constitution settled')],
'3.2':[L(P+'2.0',H,'what a canton is')],
'5.2':[L(P+'5.1',H,'canton language distribution')],
'6.0':[L(P+'5.0',H,'Romansh as a national language')],
'6.1':[L(P+'5.1',H,'Fribourg German-French canton')],
'6.2':[L(P+'5.0',H,'four language groups')],
'7.0':[L(P+'5.0',H,'language groups')],
'7.1':[L(P+'3.2',E,'cantonal system'),L(P+'5.0',H,'four language groups')],
'8.1':[L(P+'8.0',H,'Reformation in Zurich and Geneva')],
'8.3':[L(P+'3.0',E,'Sonderbund War')],
'9.0':[L(P+'8.1',E,'Protestant cantons by language'),L(P+'8.2',E,'Catholic cantons by language')],
'9.1':[L(P+'9.0',H,'religion cuts across language')],
'10.2':[L(P+'10.0',E,'minaret ban')],
'11.2':[L(P+'2.0',E,'Federal Charter of 1291')],
'14.2':[L(P+'14.1',H,'foreign communities from Yugoslavia/Turkey')],
'15.1':[L(P+'4.0',H,'Switzerland outside the EU')],
'16.0':[L(P+'14.0',H,'foreign population share')],
'16.1':[L(P+'15.1',H,'free movement with the EU')],
'17.1':[L(P+'17.0',E,'Jura split from Bern')],
'17.2':[L(P+'17.0',E,'canton of Jura boundary')],
'18.0':[L(P+'15.1',H,'bilateral agreements with the EU')],
'18.2':[L(P+'18.1',H,'women gaining the vote')],
'19.0':[L(P+'3.2',E,'cantonal powers')],
'19.1':[L(P+'3.3',E,'direct democracy')],
'19.2':[L(P+'2.3',H,'permanent neutrality')],
'19.3':[L(P+'9.0',E,'religion cutting across language')],
'21.3':[L(P+'21.0',E,'Ottoman rule')],
'22.0':[L(P+'21.1',H,'Austria-Hungary annexed Bosnia')],
'23.0':[L(P+'22.1',H,'Yugoslavia formed in 1918')],
'23.1':[L(P+'23.2',H,'Tito and the Yugoslav republics')],
'23.2':[L(P+'22.1',H,'Yugoslavia created in 1918')],
'23.3':[L(P+'23.2',H,'six republics of Yugoslavia')],
'24.1':[L(P+'23.3',E,'Kosovo as autonomous province')],
'25.1':[L(P+'25.0',E,'the South Slav peoples')],
'25.2':[L(P+'25.1',H,'Serbian and Croatian languages')],
'25.3':[L(P+'27.0',H,'religious groups define ethnicity')],
'26.0':[L(P+'25.0',E,'South Slav pattern')],
'26.1':[L(P+'23.3',H,'Vojvodina autonomous province')],
'26.3':[L(P+'26.2',E,'1991 census comparison')],
'26.4':[L(P+'26.2',H,'Muslims in 1991 census')],
'27.0':[L(P+'25.0',H,'South Slav peoples'),L(P+'21.0',H,'Ottoman conversion')],
'28.0':[L(P+'23.2',E,'republics of Yugoslavia')],
'28.1':[L(P+'28.0',H,'independence declared same day')],
'28.2':[L(P+'28.1',E,'Croatian war')],
'28.3':[L(P+'28.1',E,'Croatian Serb forces and war')],
'29.0':[L(P+'26.2',H,'Bosnia population mix')],
'29.2':[L(P+'29.0',H,'Bosnian war context')],
'29.3':[L(P+'29.0',H,'Bosnian war context')],
'29.4':[L(P+'29.0',H,'Bosnian war context')],
'29.5':[L(P+'29.0',H,'war it ended'),L('geo-option-culture-identity-s6.36.2',H,'what Dayton created','low')],
'30.0':[L(P+'24.1',H,'Kosovo tension')],
'30.1':[L(P+'30.0',H,'Kosovo war')],
'30.2':[L(P+'29.4',H,'crimes the tribunal tried','low')],
}
s2={ '1.2':[L('geo-option-culture-identity-s2.5.1',H,'dialect definition')],
'5.3':[L('geo-option-culture-identity-s2.5.1',H,'dialect definition')],
'4.1':[L('geo-option-culture-identity-s2.1.0',H,'nation states built on language','low')],
'6.1':[L('geo-option-culture-identity-s2.4.0',H,'language borders dividing a state')],
'6.2':[L('geo-option-culture-identity-s2.14.b',H,'broadcasting supports languages','low')],
'7.1':[L('geo-option-culture-identity-s2.4.0',H,'language dividing a state','low')],
'25.1':[L('geo-option-culture-identity-s2.9.2',H,'Slavic languages')],
}
s3={ '8.0':[L('geo-option-culture-identity-s3.6.4',H,'the Reformation')],
'8.1':[L('geo-option-culture-identity-s3.6.1',H,'Protestant branch')],
'8.2':[L('geo-option-culture-identity-s3.6.0',H,'Catholic branch')],
'10.0':[L('geo-option-culture-identity-s3.0.1',H,'religion visible in landscape','low')],
'10.1':[L('geo-option-culture-identity-s3.13.4',H,'face-covering bans in France','low')],
'14.2':[L('geo-option-culture-identity-s3.7.4',H,'Islam growing in Europe by migration')],
'21.2':[L('geo-option-culture-identity-s3.6.3',E,'Great Schism of 1054')],
'21.0':[L('geo-option-culture-identity-s3.5.0',H,'Islam spread by empire','low')],
'25.3':[L('geo-option-culture-identity-s3.1.1',H,'faith as national identity')],
'27.0':[L('geo-option-culture-identity-s3.6.2',H,'Orthodox Christianity')],
'27.1':[L('geo-option-culture-identity-s3.0.1',H,'religion in the landscape')],
}
def key(i): return i[len(P):]
def build(path,m,cost):
    out={}
    for i in ids:
        k=key(i); d={}
        if cost: d['cost']=2 if k in cost2 else 1
        d['needs']=m.get(k,[])
        out[i]=d
    json.dump(out,open(path,'w'),ensure_ascii=False)
    j=json.load(open(path)); assert list(j)==ids
    n=sum(len(v['needs']) for v in j.values()); lo=sum(x['confidence']=='low' for v in j.values() for x in v['needs'])
    print(path.split('/')[-1],len(j),n,sum(v.get('cost')==2 for v in j.values()),lo)
    return j
a=build(G+'point-links/geo-option-culture-identity-s6.t1g1.json',own,True)
# validate ids for pkg1
pk=open(G+'packs/geo-option-culture-identity-s6.t1g1.txt').read()
for v in a.values():
    for x in v['needs']: assert '['+x['id']+']' in pk,x['id']
build(G+'point-links/geo-option-culture-identity-s6.t1g2.json',s2,False)
build(G+'point-links/geo-option-culture-identity-s6.t1g3.json',s3,False)
for f,m in (('t1g2',s2),('t1g3',s3)):
    pk=open(G+'packs/geo-option-culture-identity-s6.%s.txt'%f).read()
    for v in m.values():
        for x in v: assert '['+x['id']+']' in pk,x['id']
