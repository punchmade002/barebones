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
'0.b':(1,[]),'0.0':(1,[]),'0.1':(1,[]),
'0.2':(1,[]),'0.3':(1,[]),'0.4':(1,[]),'0.5':(1,[]),
'1.b':(1,[]),
'1.0':(1,[('0.2','h','Free French movement','h')]),
'1.1':(1,[('4.0','h','FLN forces','h')]),
'1.2':(1,[]),'1.3':(1,[]),
'1.4':(1,[('7.1','h','the French Community','h')]),
'1.5':(1,[('1.4','e','choice between Community and independence','h')]),
'2.b':(1,[]),'2.0':(1,[]),'2.1':(1,[]),
'2.2':(1,[('0.5','h','French Community','h')]),
'2.3':(1,[('7.1','h','Community created 1958','h')]),
'2.4':(1,[('3.1','h','about a million settlers','h')]),
'3.b':(1,[]),'3.0':(1,[]),'3.1':(1,[]),'3.2':(1,[]),
'3.3':(1,[('3.2','h','assimilation policy','h')]),
'3.4':(2,[]),'3.5':(1,[]),
'3.6':(1,[('3.1','h','settlers favoured','h')]),
'4.b':(1,[]),'4.0':(1,[]),
'4.1':(1,[('4.0','e','the FLN rising','h')]),
'4.2':(1,[('4.0','h','the FLN','h')]),
'4.3':(1,[('1.1','h','Tunisia sheltering FLN','h')]),
'4.4':(1,[('4.0','h','the FLN','h')]),
'5.b':(1,[]),'5.0':(1,[]),'5.1':(1,[]),'5.2':(1,[]),'5.3':(1,[]),'5.4':(1,[]),
'5.5':(1,[('1.1','h','Tunisia and Morocco independent','h')]),
'5.6':(1,[('1.1','h','Tunisia as FLN base','h')]),
'6.b':(1,[]),
'6.0':(1,[('0.3','h','Fourth Republic instability','h')]),
'6.1':(1,[('6.0','h','Fourth Republic weakness','l')]),
'6.2':(1,[('6.1','h','13 May revolt','h')]),
'6.3':(1,[('6.2','e','Coty calling de Gaulle','h')]),
'6.4':(1,[('6.1','h','settlers demanding French Algeria','h')]),
'6.5':(1,[('6.4','e','Vive l\'Algérie française','h')]),
'7.b':(1,[]),
'7.0':(1,[('0.3','h','Fourth Republic instability','h')]),
'7.1':(1,[]),
'7.2':(1,[('6.3','h','de Gaulle invested 1958','h')]),
'8.b':(1,[]),'8.0':(1,[]),
'8.1':(1,[('8.0','e','policy of self-determination','h')]),
'8.2':(1,[('4.0','h','talks with the FLN','h')]),
'8.3':(1,[('8.0','h','self-determination','h')]),
'8.4':(1,[('8.0','e','self-determination','h')]),
'8.5':(2,[('8.4','h','policy settlers opposed','l')]),
'8.6':(1,[('3.1','h','settlers','h')]),
'9.b':(1,[]),
'9.0':(1,[('4.0','h','the FLN','h')]),
'9.1':(1,[('9.0','e','the Évian Accords','h')]),
'9.2':(1,[('9.0','e','the Évian Accords','h')]),
'9.3':(1,[('9.2','e','1 July referendum','h')]),
'9.4':(1,[]),
'10.b':(1,[]),
'10.0':(1,[('9.0','h','Évian Accords','h')]),
'10.1':(1,[('8.6','e','the OAS','h'),('8.5','h','1961 putsch','h')]),
'10.2':(1,[('8.6','e','the OAS','h')]),
'10.3':(1,[('10.1','h','OAS prisoners','h')]),
'11.b':(1,[]),
'11.0':(1,[('9.4','e','Ben Bella as president','h')]),
'11.1':(1,[('9.1','e','Mers-el-Kébir kept by France','h')]),
'11.2':(1,[('9.1','e','Saharan oil access','h')]),
'12.b':(1,[]),
'12.0':(1,[('9.3','h','5 July independence day','h')]),
'12.1':(1,[('3.1','h','pieds-noirs settlers','h')]),
'12.2':(1,[('12.1','h','settler exodus','h')]),
'12.3':(1,[]),
'12.4':(1,[('12.3','e','the harkis','h')]),
'12.5':(1,[('12.3','e','the harkis','h')]),
'12.6':(1,[('12.3','e','the harkis','h')]),
'13.b':(1,[]),
'13.0':(1,[('0.2','h','18 June appeal','h')]),
'13.1':(2,[]),
'13.2':(2,[('7.0','h','Fifth Republic','h'),('8.0','e','1959 self-determination offer','h'),('8.1','h','Barricades Week','h'),('8.5','h','the putsch','h'),('9.0','h','Évian','h')]),
'13.3':(1,[('6.5','e','settlers\' belief he kept Algeria French','h'),('8.0','e','1959 turn','h')]),
'13.4':(1,[('8.6','h','the OAS','h')]),
'13.5':(2,[('8.0','h','step by step withdrawal','l')]),
'13.6':(1,[('2.2','e','co-operation accords','h'),('7.1','h','the Community','h')]),
'13.7':(1,[]),
'14.b':(1,[]),
'14.0':(1,[('8.0','e','self-determination','h')]),
'14.1':(1,[('12.1','h','settler exodus','h')]),
'14.2':(1,[('7.0','e','Fifth Republic constitution','h')]),
'14.3':(1,[('2.2','e','co-operation accords','h')]),
'14.4':(2,[('1.1','h','Tunisian and Moroccan independence','h'),('5.5','h','UN debates','h')]),
'14.5':(1,[('2.4','h','Britain negotiated, France fought','h')]),
'14.6':(1,[]),
'14.7':(1,[('8.5','e','1961 putsch','h'),('9.2','h','Évian referendum','h')]),
}
run('hist-eur5-s4.t1g1.txt','hist-eur5-s4.t1g1.json','hist-eur5-s4',d)
