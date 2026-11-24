import json,re
P='/Users/gabrielwhelan/barebones/drafts/crunch/history/'
pk=open(P+'packs/hist-ire1-s3.t1g1.txt').read()
ids=set(re.findall(r'^\[([^\]]+)\]',pk,re.M))
tg=[i for i in re.findall(r'^\[([^\]]+)\]',pk.split('CANDIDATES')[0],re.M)]
E,H='essential','helpful'
def L(i,s,w,c='high'):
    i=i if i.startswith('hist-') else 'hist-ire1-s3.'+i
    return {"id":i,"strength":s,"why":w,"confidence":c}
D={
'0.b':(1,[]),'0.0':(1,[]),'0.1':(1,[]),'0.2':(1,[]),'0.3':(1,[]),'0.4':(1,[]),'0.5':(1,[]),'0.6':(1,[]),'0.7':(1,[]),
'1.0':(1,[]),'1.1':(1,[]),'1.2':(1,[]),'1.3':(1,[]),
'1.4':(1,[L('1.3',H,'potato diet')]),'1.5':(1,[L('1.3',H,'potato as staple')]),'1.6':(1,[]),
'2.0':(2,[]),'2.1':(1,[L('2.0',E,'falling prices and rents')]),
'2.2':(1,[L('0.2',H,'uses middlemen')]),'2.3':(2,[]),'2.4':(2,[]),
'2.5':(1,[L('2.2',H,'new tenants after evictions')]),
'2.6':(2,[L('0.7',H,'insecurity of tenure')]),'2.7':(1,[]),
'3.0':(1,[]),'3.1':(1,[L('3.0',E,'blight causing crop loss')]),
'3.2':(1,[L('3.0',E,'blight destroying the crop')]),
'3.3':(2,[L('3.2',H,'follows 1846 crop failure')]),
'3.4':(1,[L('3.0',H,'blight returning')]),
'3.5':(2,[]),'3.6':(1,[]),'3.7':(1,[]),'3.8':(2,[]),
'4.0':(1,[L('3.1',E,'1845 crop failure')]),
'4.1':(1,[L('4.0',E,'the maize purchase')]),
'4.2':(1,[]),'4.3':(1,[]),'4.4':(2,[]),
'4.5':(1,[L('4.0',E,"Peel's relief measures")]),
'5.0':(1,[]),'5.1':(1,[L('5.0',E,'laissez-faire policy')]),
'5.2':(2,[L('4.3',E,'public works relaunched')]),
'5.3':(2,[L('5.2',E,'the public works scheme')]),
'5.4':(1,[L('5.3',H,'wages on public works')]),
'5.5':(1,[L('5.3',E,'public works being closed')]),
'6.0':(1,[L('5.5',H,'switch to direct feeding')]),
'6.1':(1,[L('6.0',E,'the soup kitchens')]),
'6.2':(2,[L('hist-ire1-s2.2.3',H,'poor law unions and workhouses')]),
'6.3':(2,[L('6.2',E,'the Poor Law Extension Act')]),
'6.4':(1,[L('6.3',E,'the Gregory clause')]),
'6.5':(1,[L('hist-ire1-s2.2.3',H,'unions and workhouses')]),
'6.6':(2,[L('6.5',E,'bankrupt western unions')]),
'6.7':(1,[]),
'7.0':(1,[]),
'7.1':(1,[L('4.0',H,"Peel's maize"),L('4.3',H,'public works'),L('6.0',H,'soup kitchens')]),
'7.2':(1,[L('5.0',E,'Whig laissez-faire policy')]),
'7.3':(1,[L('5.0',H,'laissez-faire')]),
'7.4':(1,[]),
'7.5':(2,[L('6.0',H,'soup kitchens'),L('6.2',E,'Irish property paying via Poor Law')]),
'7.6':(1,[]),'7.7':(1,[]),
'7.8':(2,[L('7.2',H,'his role in Whig policy')]),
'8.0':(1,[L('4.0',H,"Peel's maize"),L('4.2',H,'relief committees'),L('4.3',H,'public works')]),
'8.1':(1,[L('6.1',E,'soup kitchens feeding millions')]),
'8.2':(1,[L('5.0',E,'laissez-faire'),L('5.4',H,'low public works wages')]),
'8.3':(1,[L('6.2',E,'Poor Law burden on Irish property')]),
'8.4':(1,[L('6.3',E,'the Gregory clause')]),
'8.5':(1,[]),'8.6':(1,[]),'8.7':(2,[]),
}
out={}
for t in tg:
    k=t.replace('hist-ire1-s3.','')
    c,n=D[k]; out[t]={"cost":c,"needs":n}
assert set(D)=={t.replace('hist-ire1-s3.','') for t in tg}
for v in out.values():
    for n in v['needs']: assert n['id'] in ids and True
json.dump(out,open(P+'point-links/hist-ire1-s3.t1g1.json','w'),indent=1)
r=json.load(open(P+'point-links/hist-ire1-s3.t1g1.json'))
ls=sum(len(v['needs']) for v in r.values())
print(len(r),ls,sum(v['cost']==2 for v in r.values()),sum(n['confidence']=='low' for v in r.values() for n in v['needs']))
