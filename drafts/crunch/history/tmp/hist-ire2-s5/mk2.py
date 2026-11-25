import json,re,sys
H,E='helpful','essential'
def run(pack,out,pre,D):
    txt=open(pack).read()
    tg=txt.split('CANDIDATES')[0]
    tids=re.findall(r'^\[([^\]]+)\]',tg,re.M)
    allids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
    assert list(D.keys())==[pre+k for k in D_keys(D,pre)] if False else True
    res={}
    for k,(c,ns) in D.items():
        i=pre+k
        res[i]={"cost":c,"needs":[{"id":(n[0] if n[0].startswith('hist-') else pre+n[0]),"strength":n[1],"why":n[2],"confidence":n[3]} for n in ns]}
    assert list(res)==tids,(set(tids)^set(res))
    for v in res.values():
        for n in v['needs']: assert n['id'] in allids,n
    json.dump(res,open(out,'w'),indent=1)
    L=sum(len(v['needs']) for v in res.values())
    print(len(res),L,sum(v['cost']==2 for v in res.values()),sum(n['confidence']=='low' for v in res.values() for n in v['needs']))
def D_keys(*a):pass
P='/Users/gabrielwhelan/barebones/drafts/crunch/history/'
S3='hist-ire2-s3.';S4='hist-ire2-s4.'
D1={
'0.b':(1,[]),'0.0':(2,[]),'0.1':(1,[]),'0.2':(1,[]),
'0.3':(1,[(S3+'3.b',H,'Gladstone converting to Home Rule','high')]),
'0.4':(1,[]),'0.5':(1,[]),
'1.b':(1,[]),'1.0':(1,[]),
'1.1':(1,[(S3+'0.6',H,'Catholic hierarchy backing the Irish Party','high')]),
'1.2':(1,[]),'1.3':(1,[]),'1.4':(1,[]),'1.5':(1,[]),
'1.6':(1,[(S3+'4.3',H,'Chamberlain opposing the Home Rule bill','high')]),
'1.7':(1,[]),'1.8':(1,[]),
'2.b':(1,[(S3+'0.3',H,'the Irish National League','high')]),
'2.0':(1,[]),'2.1':(1,[]),
'2.2':(1,[(S3+'5.4',H,'the Belfast riots of 1886','high')]),
'2.3':(1,[('2.1',H,'the earlier unionist bodies','high')]),
'2.4':(1,[(S4+'3.0',H,'the Second Home Rule Bill','high')]),
'2.5':(1,[('2.0',H,'Orange lodges','high')]),
'2.6':(1,[]),'2.7':(1,[]),
'3.b':(1,[(S4+'4.4',H,'the Third Home Rule Bill','high')]),
'3.0':(2,[]),'3.1':(1,[]),'3.2':(1,[]),
'3.3':(1,[('4.5',H,'the Ulster Day Covenant','high'),('5.2',H,'the Provisional Government plan','high')]),
'3.4':(1,[]),
'3.5':(2,[('5.0',H,'the threat of armed resistance','low')]),
'3.6':(2,[]),'3.7':(1,[]),
'4.b':(1,[('4.0',H,'the Parliament Act of 1911','high')]),
'4.0':(1,[(S4+'4.3',E,'the Parliament Act and Lords veto','high')]),
'4.1':(1,[('3.b',H,'Carson as unionist leader','high')]),
'4.2':(1,[]),'4.3':(1,[]),'4.4':(1,[]),
'4.5':(2,[]),'4.6':(1,[]),
'4.7':(2,[('4.0',E,'the Parliament Act overriding the Lords','high')]),
'4.8':(1,[('4.5',H,'the Covenant signatures','high')]),
'4.9':(1,[]),
'5.b':(1,[]),'5.0':(1,[]),
'5.1':(1,[('5.0',E,'uses the Ulster Volunteer Force','high')]),
'5.2':(1,[('2.5',H,'the Ulster Unionist Council','high')]),
'5.3':(1,[]),
'5.4':(1,[(S4+'7.3',H,'the Irish Volunteers','high')]),
'6.b':(1,[]),
'6.0':(1,[('4.7',H,'the Home Rule Bill passing','low')]),
'6.1':(2,[]),
'6.2':(2,[('5.0',E,'uses the Ulster Volunteer Force','high')]),
'6.3':(1,[('6.2',E,'the Larne gun-running','high'),(S4+'7.5',H,'the Howth gun-running','high')]),
'6.4':(2,[]),
'6.5':(1,[('6.4',E,'the Buckingham Palace Conference','high')]),
'6.6':(1,[(S4+'4.5',H,'the Suspensory Act','high')]),
'6.7':(1,[('6.2',E,'the Larne gun-running','high')]),
'6.8':(1,[('6.0',H,'temporary exclusion of Ulster','high')]),
'7.b':(1,[]),
'7.0':(2,[(S3+'4.b',H,'the First Home Rule Bill defeat','high'),(S4+'3.b',H,'the Second Home Rule Bill defeat','high')]),
'7.1':(2,[('5.0',H,'the UVF','high'),('4.5',H,'the Covenant','high'),('4.3',H,'Conservative backing from Bonar Law','high')]),
'7.2':(1,[('4.7',H,'the Third Bill becoming law','high')]),
'7.3':(1,[('4.3',H,'the Conservative alliance','high')]),
'7.4':(1,[('5.1',H,'unionist arms and the UVF','high')]),
'7.5':(2,[('6.1',H,'closeness to civil war in 1914','low')]),
}
run(P+'packs/hist-ire2-s5.t1g1.txt',P+'point-links/hist-ire2-s5.t1g1.json','hist-ire2-s5.',D1)
