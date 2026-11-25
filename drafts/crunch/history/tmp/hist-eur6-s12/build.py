import json,re
B='/Users/gabrielwhelan/barebones/drafts/crunch/history/'
E,H='essential','helpful'
def run(pack,out,D):
    txt=open(B+'packs/'+pack).read()
    tg=txt.split('CANDIDATES')[0]
    tids=re.findall(r'^\[([^\]]+)\]',tg,re.M)
    allids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
    assert list(D)==tids,(set(tids)^set(D))
    res={}
    for k,(c,ns) in D.items():
        res[k]={'cost':c,'needs':[{'id':i,'strength':s,'why':w,'confidence':f} for i,s,w,f in ns]}
        for n in res[k]['needs']: assert n['id'] in allids and n['id']!=k,(k,n['id'])
    json.dump(res,open(B+'point-links/'+out,'w'),indent=1)
p='hist-eur6-s12.'
S='hist-eur6-s1.'
def f(i): return i if i.startswith('hist') else p+i
D={
'0.b':(1,[]),'0.0':(1,[]),'0.1':(1,[]),
'0.2':(1,[(S+'5.0',H,'Eisenhower presidency','low')]),
'0.3':(1,[]),'0.4':(1,[]),'0.5':(1,[]),'0.6':(1,[]),
'0.7':(1,[('0.1',H,'Pledge and motto changes','high')]),
'1.b':(1,[]),'1.0':(1,[]),'1.1':(1,[]),'1.2':(1,[]),'1.3':(1,[]),'1.4':(1,[]),
'1.5':(1,[]),'1.6':(1,[]),'1.7':(1,[]),
'1.8':(2,[]),'1.9':(2,[]),
'1.10':(1,[('4.0',H,'uses the Moral Majority','high'),(S+'7.2',H,'uses Watergate','high')]),
'1.11':(2,[]),'1.12':(1,[]),
'2.b':(1,[]),'2.0':(1,[]),'2.1':(1,[]),'2.2':(1,[]),
'2.3':(1,[(S+'5.4',H,'1960 election Kennedy v Nixon','high')]),
'2.4':(1,[]),'2.5':(1,[]),
'3.b':(1,[]),'3.0':(1,[]),'3.1':(1,[]),'3.2':(1,[]),
'3.3':(1,[('3.2',E,'uses PTL televangelists','high')]),
'3.4':(1,[('3.2',H,'televangelists','high')]),
'3.5':(1,[]),
'3.6':(1,[('3.5',H,'school prayer ruling Engel','high')]),
'3.7':(1,[]),
'3.8':(1,[(S+'7.5',H,'Carter 1976 election','high')]),
'3.9':(1,[('3.2',H,'Robertson and Falwell televangelists','high')]),
'3.10':(1,[('3.3',H,'Bakker scandal damaged televangelism','high')]),
'4.b':(1,[('4.0',H,'Moral Majority','high')]),
'4.0':(1,[('3.2',H,'Falwell as televangelist','high')]),
'4.1':(1,[('4.0',E,'uses the Moral Majority','high'),(S+'8.0',H,'Reagan 1980 election','high')]),
'4.2':(1,[('4.0',E,'uses the Moral Majority','high'),('3.10',H,'late 1980s scandals','high')]),
'4.3':(2,[('4.0',H,'founding of Moral Majority','high')]),
'4.4':(2,[('4.0',H,'Moral Majority and religious right','low'),(S+'8.0',H,'Reagan 1980 campaign','high')]),
'4.5':(1,[('4.0',E,'uses the Moral Majority','high'),('3.7',H,'Roe and ERA issues','low')]),
'4.6':(1,[('4.0',E,'uses the Moral Majority','high')]),
'5.b':(1,[]),'5.0':(1,[]),
'5.1':(1,[(S+'5.4',H,'1960 Kennedy Nixon election','high')]),
'5.2':(1,[]),'5.3':(1,[]),
'5.4':(1,[(S+'7.2',H,'Watergate burglary','high')]),
'5.5':(1,[]),'5.6':(1,[]),'5.7':(1,[]),'5.8':(1,[]),
'5.9':(2,[]),
'5.10':(1,[(S+'7.2',H,'Watergate scandal','high')]),
'5.11':(1,[]),
'6.b':(1,[('6.0',H,'GI Bill','high')]),
'6.0':(1,[]),'6.1':(1,[]),'6.2':(1,[]),
'6.3':(1,[(S+'6.6',H,'Higher Education Act 1965','high')]),
'6.4':(1,[]),
'6.5':(1,[('6.4',E,'Free Speech Movement at Berkeley','high')]),
'6.6':(1,[]),
'6.7':(1,[('6.0',H,'GI Bill','high')]),
'6.8':(1,[('6.4',H,'Free Speech Movement grievances','high')]),
'6.9':(1,[('6.5',E,'Sproul Hall sit-in','high')]),
'6.10':(1,[('6.6',H,'Kent State killings','high')]),
'7.b':(1,[]),
'7.0':(2,[('0.0',H,'religious revival in 1950s','high'),('1.12',H,'Graham and King','low')]),
'7.1':(2,[('4.0',H,'religious right of the 1980s','high'),('3.2',H,'televangelism','high')]),
'7.2':(2,[('5.1',H,'Kennedy television debates','high'),('5.4',H,'Watergate press exposure','high')]),
'7.3':(2,[('6.0',H,'mass higher education growth','high'),('6.6',H,'campus unrest','high')]),
}
D={f(k):(c,[(f(i),s,w,fc) for i,s,w,fc in ns]) for k,(c,ns) in D.items()}
run('hist-eur6-s12.t1g1.txt','hist-eur6-s12.t1g1.json',D)
