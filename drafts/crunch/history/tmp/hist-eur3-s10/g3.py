import json
P='hist-eur3-s10.'
counts={0:5,1:4,2:7,3:4,4:6,5:7,6:8,7:7,8:6,9:8,10:7,11:9,12:4,13:8,14:4,15:8,16:7,17:9,18:3,19:8}
H,L='high','low'
def n(i,s,w,c): return {"id":"hist-eur3-s6."+i,"strength":s,"why":w,"confidence":c}
links={
'0.1':[n('16.0','helpful','Phoney War','high'),n('17.2','helpful','armistice of 22 June 1940','high')],
'1.3':[n('16.4','helpful','Dunkirk evacuation of troops','high')],
'2.2':[n('16.0','helpful','Phoney War','high')],
'2.3':[n('17.2','helpful','fall of France','low')],
'11.1':[n('17.0','helpful','French exodus of 1940','high')],
'11.4':[n('21.2','helpful','de Gaulle and the Free French','high')],
'12.0':[n('26.b','helpful','collaboration and collaborationism','high')],
'12.1':[n('26.b','helpful','state collaboration versus collaborationism','low')],
'12.3':[n('28.3','helpful','French volunteers in German service','low')],
'13.5':[n('26.0','helpful','Pétain meets Hitler at Montoire','high'),n('23.3','helpful','Laval head of government 1942','high')],
'13.6':[n('29.3','essential','Vel d Hiv round-up','high'),n('27.3','helpful','labour sent to Germany','low')],
'13.7':[n('23.3','helpful','Laval executed 1945','high')],
'15.0':[n('21.2','helpful','de Gaulle and Free French','high'),n('30.b','helpful','forced labour sent to Germany','low')],
'17.0':[n('17.3','essential','division of France into zones','high'),n('27.4','helpful','German occupation of south, 1942','high')],
'17.3':[n('30.b','helpful','STO labour sent to Germany','low')],
'17.4':[n('29.2','helpful','Vichy police deportations of Jews','high')],
'17.6':[n('27.4','helpful','occupation of the south 1942','high'),n('20.4','helpful','Pétain welcomed in 1940','high')],
'17.8':[n('21.2','helpful','de Gaulle leading provisional government','low')],
'18.1':[n('17.3','helpful','French defeat and division','low')],
'19.6':[n('21.4','helpful','post-war myth of resistance France','high')],
}
out={}
for b in range(20):
    ids=[f'{b}.b']+[f'{b}.{k}' for k in range(counts[b])]
    for i in ids: out[P+i]={"needs":links.get(i,[])}
json.dump(out,open('/Users/gabrielwhelan/barebones/.claude/worktrees/history-crunch/drafts/crunch/history/point-links/hist-eur3-s10.t1g3.json','w'),ensure_ascii=False,indent=0)
print(len(out),sum(len(v['needs']) for v in out.values()),sum(n['confidence']=='low' for v in out.values() for n in v['needs']))
