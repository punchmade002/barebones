import json,re
P='hist-eur1-s9.'
def n(i,s,w,c='high'): return {"id":i if i.startswith('hist') else P+i,"strength":s,"why":w,"confidence":c}
E,H='essential','helpful'
G='hist-eur1-s8.'
D={
'0.b':(1,[]),
'0.0':(1,[]),
'0.1':(1,[]),
'0.2':(1,[n('0.1',H,'his Manchester mill work','low')]),
'0.3':(1,[]),
'0.4':(1,[n('0.3',E,'David Dale, owner of the mills'),n('0.1',H,'the Chorlton partners')]),
'0.5':(1,[n('0.2',H,'environment forms character')]),
'1.0':(1,[]),
'1.1':(1,[]),
'1.2':(1,[]),
'1.3':(1,[n('1.2',E,'the pauper children')]),
'1.4':(2,[n('0.4',H,'the earlier partners','low')]),
'1.5':(1,[n('1.4',E,'the 1813 partners')]),
'2.0':(1,[]),
'2.1':(1,[]),
'2.2':(1,[]),
'2.3':(1,[]),
'2.4':(1,[n('0.2',H,'environment forms character')]),
'2.5':(1,[n('hist-eur1-s7.4.0',H,'factory system conditions','low')]),
'3.0':(1,[n('1.2',E,'the pauper children apprentices')]),
'3.1':(1,[n('2.0',H,'the long mill day')]),
'3.2':(1,[]),
'3.3':(1,[n('2.3',E,'discipline by fines and punishment')]),
'3.4':(2,[n('3.3',H,'replacement for punishment')]),
'3.5':(1,[n('1.5',H,'profits spent on community')]),
'4.0':(1,[]),
'4.1':(1,[]),
'4.2':(1,[]),
'4.3':(1,[n('2.1',H,'poor housing and streets')]),
'4.4':(1,[]),
'4.5':(1,[n('4.0',E,'the Institute')]),
'4.6':(1,[n('4.1',E,'the infant school')]),
'5.0':(1,[n('2.4',H,'environment shapes character','low')]),
'5.1':(2,[n('1.2',H,'pauper apprentices')]),
'5.2':(1,[n('3.0',H,'his child employment reforms','low')]),
'5.3':(2,[n('5.2',E,'his campaign for a law')]),
'5.4':(1,[n('5.3',E,'the 1819 Act')]),
'5.5':(2,[]),
'5.6':(1,[]),
'6.0':(1,[n('3.1',H,'reforms like shorter hours','low')]),
'6.1':(1,[n('1.4',E,'William Allen as partner')]),
'6.2':(1,[n('7.0',E,'New Harmony')]),
'6.3':(1,[]),
'7.0':(1,[n('6.2',H,'Owen going to the United States')]),
'7.1':(1,[n('7.0',E,'New Harmony')]),
'7.2':(1,[]),
'7.3':(2,[n(G+'0.3',H,'the GNCTU')]),
'7.4':(1,[n('5.0',H,'Owen\'s writings','low')]),
'7.5':(2,[n('3.1',H,'reforms needing owner control','low')]),
'7.6':(1,[n('7.5',H,'paternalist versus co-operative','low')]),
'8.0':(2,[n(G+'1.2',H,'Owen\'s socialism','low')]),
'8.1':(1,[]),
'8.2':(1,[]),
'8.3':(2,[n('8.2',H,'reliance on Owen\'s control')]),
'8.4':(1,[]),
'8.5':(1,[]),
'9.0':(1,[n('6.0',H,'profitability under Owen')]),
'9.1':(1,[n('7.5',H,'why New Lanark was not copied')]),
'9.2':(2,[n('5.3',E,'the 1819 Act'),n('4.6',H,'the infant school'),n('7.4',H,'the co-operative movement')]),
'9.3':(2,[n('5.4',H,'weakness of the 1819 Act'),n('6.1',H,'quarrel with partners'),n('7.1',H,'New Harmony failure')]),
'9.4':(2,[n('8.0',H,'divided contemporary opinion')]),
'9.5':(2,[n('8.3',H,'historians\' debate on paternalism')]),
}
out={P+k:{"cost":c,"needs":nd} for k,(c,nd) in D.items()}
pk=open('/Users/gabrielwhelan/barebones/drafts/crunch/history/packs/hist-eur1-s9.t1g1.txt').read()
ids=set(re.findall(r'^\[([^\]]+)\]',pk,re.M))
tg=re.findall(r'^\[(hist-eur1-s9\.[^\]]+)\]',pk,re.M)
assert list(out)==tg,(set(tg)^set(out))
for k,v in out.items():
    for x in v['needs']: assert x['id'] in ids and x['id']!=k,x
json.dump(out,open('/Users/gabrielwhelan/barebones/drafts/crunch/history/point-links/hist-eur1-s9.t1g1.json','w'),indent=1)
print(len(out),sum(len(v['needs']) for v in out.values()),sum(v['cost']==2 for v in out.values()),sum(x['confidence']=='low' for v in out.values() for x in v['needs']))
