import json,re
P='/Users/gabrielwhelan/barebones/drafts/crunch/geography/'
S='geo-rocks-weathering-s6.'
def n(i,s,w,c='high'): return {"id":S+i,"strength":s,"why":w,"confidence":c}
E,H='essential','helpful'
d={
'0.b':(1,[]),'0.0':(1,[]),'0.1':(1,[]),'1.b':(1,[]),
'1.0':(1,[]),'1.1':(1,[]),'1.2':(1,[]),
'2.b':(1,[]),'2.0':(1,[]),'2.1':(1,[]),
'2.2':(1,[n('2.1',H,'uses saltating grains')]),
'3.b':(1,[n('1.0',H,'uses deflation')]),
'3.0':(1,[n('1.0',E,'formed by deflation')]),
'3.1':(1,[n('3.0',E,'example of deflation hollow')]),
'3.2':(1,[n('1.0',E,'left after deflation')]),
'3.3':(1,[n('1.1',E,'cut by sandblasting abrasion')]),
'3.4':(2,[n('3.0',E,'draws deflation hollow'),n('3.2',E,'draws desert pavement')]),
'4.b':(1,[n('1.1',H,'uses abrasion')]),
'4.0':(1,[n('1.1',E,'abraded by wind-blown sand')]),
'4.1':(2,[n('1.1',E,'cut by abrasion')]),
'4.2':(1,[n('4.1',E,'stages of zeugen formation')]),
'4.3':(1,[n('1.1',E,'undercut by sandblasting abrasion')]),
'4.4':(1,[n('4.3',E,'stages of mushroom rock')]),
'4.5':(2,[n('4.0',E,'draws yardangs'),n('4.1',E,'draws zeugen'),n('4.3',E,'draws mushroom rock')]),
'5.b':(1,[]),'5.0':(1,[]),'5.1':(1,[]),
'5.2':(2,[n('5.0',H,'deposition when wind slows')]),
'5.3':(1,[]),'5.4':(1,[]),
'5.5':(1,[n('5.2',E,'draws barchan dune')]),
'6.b':(1,[]),
'6.0':(2,[n('1.0',H,'bare soil blown away: deflation','low')]),
'6.1':(1,[n('6.0',E,'follows from Dust Bowl')]),
'6.2':(1,[]),
}
txt=open(P+'packs/geo-rocks-weathering-s6.t1g1.txt').read()
tg=re.findall(r'^\[(geo-rocks-weathering-s6\.[^\]]+)\]',txt.split('CANDIDATES')[0],re.M)
allids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
assert [S+k for k in d]==tg,(set(tg)^{S+k for k in d})
out={S+k:{"cost":c,"needs":l} for k,(c,l) in d.items()}
for v in out.values():
    for x in v['needs']: assert x['id'] in allids
json.dump(out,open(P+'point-links/geo-rocks-weathering-s6.t1g1.json','w'),indent=1)
print(len(out),sum(len(v['needs']) for v in out.values()),sum(v['cost']==2 for v in out.values()),sum(x['confidence']=='low' for v in out.values() for x in v['needs']))
