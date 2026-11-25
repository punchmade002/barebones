import json
P='hist-eur3-s10.'
counts={0:5,1:4,2:7,3:4,4:6,5:7,6:8,7:7,8:6,9:8,10:7,11:9,12:4,13:8,14:4,15:8,16:7,17:9,18:3,19:8}
H,L='high','low'
def n(i,s,w,c): return {"id":"hist-eur3-s6."+i,"strength":s,"why":w,"confidence":c}
links={
'12.1':[n('33.5','helpful','attentisme, wait and see','high')],
'13.6':[n('30.0','helpful','the Milice','high')],
'13.7':[n('35.0','helpful','post-liberation purges','high')],
'14.2':[n('32.0','helpful','early French resistance and intelligence','low')],
'14.3':[n('32.3','helpful','hostage shootings as reprisals','high')],
'15.0':[n('30.2','essential','STO compulsory labour service','high'),n('32.5','helpful','Jean Moulin uniting resistance','high'),n('33.0','helpful','the maquis','high')],
'15.1':[n('33.3','helpful','Oradour-sur-Glane massacre','high')],
'17.3':[n('30.2','helpful','STO sent men to Germany','high')],
'17.6':[n('30.2','helpful','compulsory labour service','high')],
'17.7':[n('33.5','helpful','attentisme, wait and see','high')],
'17.8':[n('35.3','helpful','women given the vote 1944','high')],
'19.3':[n('34.3','helpful','Provisional Government after liberation','low')],
'19.4':[n('33.5','helpful','Resistance minority, most waited','high')],
'19.6':[n('36.1','helpful','Paxton on Vichy collaboration','high')],
}
out={}
for b in range(20):
    ids=[f'{b}.b']+[f'{b}.{k}' for k in range(counts[b])]
    for i in ids: out[P+i]={"needs":links.get(i,[])}
json.dump(out,open('/Users/gabrielwhelan/barebones/.claude/worktrees/history-crunch/drafts/crunch/history/point-links/hist-eur3-s10.t1g4.json','w'),ensure_ascii=False,indent=0)
print(len(out),sum(len(v['needs']) for v in out.values()),sum(n['confidence']=='low' for v in out.values() for n in v['needs']))
