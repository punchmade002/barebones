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
    r=json.load(open(B+'point-links/'+out))
    print(out,len(r),sum(len(v['needs']) for v in r.values()),sum(v['cost']==2 for v in r.values()),sum(n['confidence']=='low' for v in r.values() for n in v['needs']))
p='hist-ire5-s3.'
D={
'0.b':(1,[]),
'0.0':(1,[]),
'0.1':(1,[]),
'0.2':(1,[]),
'0.3':(1,[]),
'0.4':(1,[('0.3',H,'Derry nationalists claim for university','high')]),
'0.5':(1,[('5.3',H,'west of the Bann grievance','high')]),
'0.6':(1,[]),
'1.b':(1,[]),
'1.0':(1,[('0.1',H,'Robbins expansion, second university','low')]),
'1.1':(1,[]),
'1.2':(1,[]),
'1.3':(1,[('0.0',H,'Magee College as existing college','high')]),
'1.4':(1,[('1.0',E,'uses the Lockwood Committee','high')]),
'1.5':(1,[('1.4',E,'protest against Lockwood decision','high')]),
'1.6':(1,[('1.0',H,'evidence heard by Lockwood Committee','high')]),
'2.b':(1,[('1.4',H,'Lockwood recommendation','high')]),
'2.0':(1,[('1.4',E,'Lockwood recommended Coleraine','high')]),
'2.1':(1,[('2.0',H,'choice of Coleraine','high')]),
'2.2':(1,[('2.0',H,'vote on Coleraine decision','high')]),
'2.3':(1,[('2.0',H,'government choice of Coleraine','high')]),
'2.4':(1,[('2.0',E,'Coleraine decision','high')]),
'2.5':(1,[('2.0',H,'Coleraine decision','high')]),
'3.b':(1,[('1.1',H,'University for Derry Committee','high')]),
'3.0':(1,[]),
'3.1':(1,[('1.1',H,'University for Derry Committee','high')]),
'3.2':(1,[('1.5',H,'1965 protests','low')]),
'3.3':(1,[]),
'3.4':(1,[('3.1',H,'Hume chaired the campaign','high')]),
'3.5':(1,[]),
'3.6':(1,[]),
'3.7':(1,[('s2.5.5'.replace('s2','hist-ire5-s2'),H,'Derry Citizens Action Committee','high')]),
'4.0':(1,[('0.1',E,'Robbins Report','high'),('1.0',H,'Lockwood Committee','high')]),
'4.1':(1,[('1.0',H,'Lockwood Committee','high'),('1.1',H,'University for Derry Committee','high')]),
'4.2':(1,[('1.4',E,'Lockwood report','high'),('1.5',H,'motorcade to Stormont','high')]),
'4.3':(1,[('2.0',H,'Stormont accepted Coleraine','high')]),
'4.4':(1,[('2.0',H,'Coleraine university decision','high')]),
'4.5':(1,[('2.0',H,'Coleraine university','high')]),
'4.6':(1,[('hist-ire5-s2.5.0',E,'uses the Derry march 5 October','high'),('hist-ire5-s2.5.5',H,'Derry Citizens Action Committee','high')]),
'5.b':(1,[('2.0',H,'Coleraine decision','high')]),
'5.0':(1,[('1.1',H,'Derry campaign','high')]),
'5.1':(1,[('2.3',H,'government case for Coleraine','high')]),
'5.2':(1,[('6.2',H,'Craigavon drawing investment east','high')]),
'5.3':(1,[]),
'5.4':(1,[('5.3',H,'west of the Bann grievance','high')]),
'5.5':(1,[('hist-ire5-s2.4.0',H,'civil rights movement','low')]),
'6.b':(1,[]),
'6.0':(1,[]),
'6.1':(1,[('6.0',E,'Derry Road closure','high')]),
'6.2':(1,[('hist-ire5-s2.0.1',H,'Matthew Report and Craigavon','high')]),
'6.3':(1,[]),
'6.4':(1,[('hist-ire5-s1.3.3',E,'Londonderry Corporation 1936 boundaries','high')]),
'6.5':(1,[('hist-ire5-s1.3.2',H,'council housing allocation','low')]),
'6.6':(1,[('2.0',H,'university decision','high')]),
'7.0':(1,[('2.0',H,'Coleraine decision','high')]),
'7.1':(1,[('3.1',H,'Hume chaired the campaign','high')]),
'7.2':(1,[('hist-ire5-s2.4.0',H,'civil rights movement in Derry','low')]),
'7.3':(1,[]),
'7.4':(1,[('hist-ire5-s2.0.5',H,'modernising programme','high')]),
'7.5':(1,[]),
'7.6':(1,[('0.0',H,'Magee College','high')]),
'8.0':(2,[('1.3',H,'Derry campaign arguments','high')]),
'8.1':(2,[('2.3',H,'government case for Coleraine','high')]),
'8.2':(2,[('2.1',E,'faceless men allegation','high')]),
'8.3':(2,[('2.0',H,'choice of Coleraine','high')]),
'8.4':(2,[('2.1',H,'nationalist view of decision','high')]),
'8.5':(2,[('5.4',H,'wider public investment inequality','high')]),
'8.6':(1,[]),
}
D={(k if k.startswith('hist') else p+k):(c,[(i if i.startswith('hist') else p+i,s,w,f) for i,s,w,f in ns]) for k,(c,ns) in D.items()}
run('hist-ire5-s3.t1g1.txt','hist-ire5-s3.t1g1.json',D)
