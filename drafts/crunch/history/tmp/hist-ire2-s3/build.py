import json,re,sys
base='/Users/gabrielwhelan/barebones/.claude/worktrees/history-crunch/drafts/crunch/history/'
def run(pack,out,pfx,data):
    txt=open(base+'packs/'+pack).read()
    allids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
    tsec=txt.split('CANDIDATES')[0]
    targets=re.findall(r'^\[([^\]]+)\]',tsec,re.M)
    res={}
    for t in targets:
        k=t[len(pfx)+1:]
        assert k in data,k
        c,l=data[k]
        needs=[]
        for (i,s,w,cf) in l:
            i=i if i.startswith('hist-') else pfx+'.'+i
            assert i in allids and i!=t,i
            needs.append({"id":i,"strength":{'e':'essential','h':'helpful'}[s],"why":w,"confidence":{'h':'high','l':'low'}[cf]})
        res[t]={"cost":c,"needs":needs}
    assert set(data)==set(k[len(pfx)+1:] for k in targets)
    json.dump(res,open(base+'point-links/'+out,'w'),indent=1)
    n=sum(len(v['needs']) for v in res.values())
    print(len(res),n,sum(v['cost']==2 for v in res.values()),sum(x['confidence']=='low' for v in res.values() for x in v['needs']))
H='h';E='e'
d={
'0.b':(1,[]),'0.0':(1,[]),
'0.1':(1,[('hist-ire2-s1.3.4','h','Home Rule League founded 1873','h')]),
'0.2':(2,[('hist-ire2-s1.8.1','h','Kilmainham imprisonment and No Rent','h'),('hist-ire2-s1.10.1','h','Irish National League','h')]),
'0.3':(1,[('hist-ire2-s2.2.b','h','Land War and coercion','h')]),
'0.4':(1,[('hist-ire2-s1.9.0','h','Phoenix Park murders','h')]),
'0.5':(1,[]),'0.6':(1,[]),'0.7':(1,[]),
'1.b':(1,[]),'1.0':(1,[]),
'1.1':(1,[('1.0','h','Third Reform Act widened vote','h')]),
'1.2':(1,[]),
'1.3':(1,[('1.2','e','single-member constituencies','h'),('hist-ire2-s1.10.1','h','Irish National League','h')]),
'1.4':(1,[]),
'1.5':(1,[('hist-ire2-s1.3.2','h','secret ballot','h')]),
'1.6':(1,[]),
'2.b':(1,[]),'2.0':(1,[]),'2.1':(1,[]),
'2.2':(1,[('2.1','e','Maamtrasna murders','h'),('0.3','h','Liberal coercion','h')]),
'2.3':(1,[('2.1','e','Maamtrasna case','h')]),
'2.4':(1,[('2.3','h','Irish-Conservative co-operation','l')]),
'3.b':(1,[]),
'3.0':(1,[('0.3','h','Crimes Act of 1882','h')]),
'3.1':(1,[]),
'3.2':(1,[('hist-ire2-s1.8.2','h','O\'Shea as go-between','h')]),
'3.3':(1,[]),
'3.4':(1,[('0.3','h','Liberal coercion 1881-82','h'),('5.0','h','Hawarden Kite reversal','h')]),
'4.b':(1,[]),'4.0':(1,[]),
'4.1':(1,[('4.0','e','the 85 seats won','h')]),
'4.2':(1,[('0.7','h','Ulster religious geography','h')]),
'4.3':(2,[('4.0','h','Irish Party 86 MPs','h')]),
'4.4':(1,[('4.3','e','seat totals of the parties','h'),('2.b','h','balance of power','h')]),
'4.5':(1,[('3.4','e','Parnell manifesto','h')]),
'4.6':(1,[('4.0','h','85 Irish seats','h')]),
'5.b':(1,[]),'5.0':(1,[]),
'5.1':(2,[('2.4','h','Salisbury minority ministry','h'),('5.0','h','Gladstone move to Home Rule','l')]),
'5.2':(1,[('0.6','h','Hartington, Whig wing','h'),('3.2','h','Chamberlain radical','h')]),
'5.3':(2,[('5.0','h','Hawarden Kite','l')]),
'6.b':(1,[]),'6.0':(1,[]),'6.1':(1,[]),
'6.2':(1,[('6.0','h','Government of Ireland Bill','h')]),
'6.3':(1,[]),
'6.4':(1,[('3.1','h','tenant purchase loans','h')]),
'6.5':(1,[('6.0','e','the bill','h'),('6.2','h','financial terms','h')]),
'7.b':(1,[]),
'7.0':(1,[('6.0','e','the Government of Ireland Bill','h')]),
'7.1':(1,[('5.2','h','Chamberlain and Hartington opposing','h')]),
'7.2':(1,[('6.0','h','the bill','h')]),
'7.3':(1,[('6.0','h','the bill','h')]),
'7.4':(1,[('0.3','h','coercion','h')]),
'7.5':(1,[('6.0','h','the bill','h')]),
'7.6':(1,[('7.0','e','the defeat of the bill','h')]),
'8.b':(1,[]),
'8.0':(1,[('0.7','h','Ulster Protestants','h')]),
'8.1':(1,[('8.0','h','Churchill in Belfast 1886','h')]),
'8.2':(1,[]),
'8.3':(1,[('0.0','h','Union and repeal','l')]),
'8.4':(1,[('7.0','h','defeat of the bill','l')]),
'8.5':(1,[('8.4','e','the Belfast riots','h')]),
'9.b':(1,[]),
'9.0':(1,[('7.1','e','Liberal Unionists','h'),('7.6','h','1886 dissolution','h')]),
'9.1':(1,[('7.1','e','Liberal Unionist support','h')]),
'9.2':(1,[('4.0','h','85 seats in 1885','h')]),
'9.3':(1,[('5.1','h','Gladstone adopting Home Rule','h')]),
'9.4':(1,[('0.5','e','Lords could reject a bill','h'),('7.1','h','Liberal split','h')]),
'9.5':(1,[('8.0','h','Ulster unionist resistance','h')]),
'9.6':(1,[]),
'10.b':(1,[]),'10.0':(1,[]),
'10.1':(1,[('1.4','e','pledge and conventions','h')]),
'10.2':(1,[('3.0','e','bargain with Carnarvon','h'),('3.4','e','the manifesto','h')]),
'10.3':(1,[('hist-ire2-s1.8.2','h','Captain O\'Shea','h')]),
'10.4':(1,[('7.1','h','Liberal split','h')]),
'10.5':(1,[('4.6','h','national mandate','h')]),
'10.6':(2,[('1.4','h','pledge','h'),('10.3','h','imposing O\'Shea','h')]),
'10.7':(1,[('5.2','h','Liberal split','h')]),
'11.b':(1,[]),
'11.0':(1,[('4.6','h','1885 result as mandate','h')]),
'11.1':(1,[('8.2','h','Irish Loyal and Patriotic Union','h')]),
'11.2':(1,[('7.4','h','Gladstone\'s arguments','h')]),
'11.3':(1,[('7.1','e','Liberal Unionists','h')]),
'11.4':(1,[]),'11.5':(1,[]),
'11.6':(2,[('5.3','h','same historians\' debate','h')]),
'12.b':(1,[]),
'12.0':(1,[('4.6','h','national mandate','h')]),
'12.1':(1,[('7.1','h','Liberal split','h')]),
'12.2':(1,[('7.0','h','narrow defeat','h')]),
'12.3':(1,[('4.2','h','Ulster unionist seats','h')]),
'12.4':(1,[('7.1','h','Liberal Unionists','h')]),
'12.5':(1,[('9.5','h','Ulster question origin','h')]),
}
run('hist-ire2-s3.t1g1.txt','hist-ire2-s3.t1g1.json','hist-ire2-s3',{k:(c,[(i if i.startswith('hist-') else i,s,w,cf) for i,s,w,cf in l]) for k,(c,l) in d.items()})
