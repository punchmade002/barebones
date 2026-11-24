import re,json
P='/Users/gabrielwhelan/barebones/drafts/crunch/geography/'
S='geo-option-culture-identity-s6.'
def L(i,s,w,c='high'): return {"id":i,"strength":s,"why":w,"confidence":c}
H='helpful'
jobs={
'g4':{
'3.2':[L('geo-option-culture-identity-s5.10.0',H,'federalism and autonomy')],
'4.0':[L('geo-option-culture-identity-s5.5.3',H,'Schengen removing passport checks')],
'4.1':[L('geo-option-culture-identity-s5.0.3',H,'nation defined by identity')],
'7.1':[L('geo-option-culture-identity-s5.0.6',H,'multinational state','low')],
'17.0':[L('geo-option-culture-identity-s5.2.2',H,'cultural boundaries follow language/religion')],
'19.0':[L('geo-option-culture-identity-s5.10.0',H,'federalism gives regions control')],
'19.1':[L('geo-option-culture-identity-s5.10.2',H,'power-sharing among groups')],
'22.1':[L('geo-option-culture-identity-s5.1.1',H,'empire break-up created nation states','low')],
'23.3':[L('geo-option-culture-identity-s5.10.0',H,'autonomy of regions')],
'24.0':[L('geo-option-culture-identity-s5.1.0',H,'nationalism defined')],
'24.1':[L('geo-option-culture-identity-s5.10.0',H,'autonomy removed','low')],
'26.0':[L('geo-option-culture-identity-s5.5.1',H,'minorities created by boundaries','low')],
'28.b':[L('geo-option-culture-identity-s5.5.5',H,'changing boundaries create new minorities')],
},
'g5':{
'12.b':[L('geo-option-culture-identity-s4.3.1',H,'UNESCO intangible heritage list')],
'12.0':[L('geo-option-culture-identity-s4.3.1',H,'UNESCO intangible heritage list')],
'12.2':[L('geo-option-culture-identity-s4.3.1',H,'UNESCO intangible heritage list')],
'14.2':[L('geo-option-culture-identity-s4.4.0',H,'migrants bring religion and customs')],
},
'g6':{
'0.0':[L('geo-option-culture-identity-s1.0.1',H,'ethnic group definition')],
'25.b':[L('geo-option-culture-identity-s1.0.0',H,'race versus culture')],
'25.3':[L('geo-option-culture-identity-s1.0.1',H,'ethnicity as cultural identity')],
'15.0':[L('geo-option-culture-identity-s1.12.1',H,'guest workers settling')],
'15.1':[L('geo-region-european-s3.12.0',H,'single market free movement of labour','low')],
'18.0':[L('geo-region-european-s3.12.0',H,'EU single market membership','low')],
'3.4':[L('geo-region-european-s3.2.3',H,'power-sharing government','low')],
'19.1':[L('geo-region-european-s3.2.3',H,'power-sharing among groups')],
'23.0':[L('geo-option-culture-identity-s1.29.2',H,'Roma targeted in Holocaust','low')],
'29.4':[L('geo-option-culture-identity-s1.1.4',H,'genocide defined')],
'28.b':[L('geo-region-european-s3.10.0',H,'mismatched cultural/political regions cause tension')],
}}
for k,links in jobs.items():
    p=f'{P}packs/geo-option-culture-identity-s6.t1{k}.txt'
    txt=open(p).read()
    tg,cd=txt.split('CANDIDATES',1)
    ids=re.findall(r'^\[(\S+?)\]',tg,re.M); cids=set(re.findall(r'^\[(\S+?)\]',cd,re.M))
    out={}
    for i in ids:
        n=[x for x in links.get(i[len(S):],[])]
        for x in n: assert x['id'] in cids
        out[i]={"needs":n}
    assert all(S+a in out for a in links)
    json.dump(out,open(f'{P}point-links/geo-option-culture-identity-s6.t1{k}.json','w'),ensure_ascii=False)
    chk=json.load(open(f'{P}point-links/geo-option-culture-identity-s6.t1{k}.json'))
    nl=sum(len(v['needs']) for v in chk.values()); lo=sum(x['confidence']=='low' for v in chk.values() for x in v['needs'])
    print(k,len(chk),nl,lo)
