import json,re
H='high';L='low';h='helpful';e='essential'
P='/Users/gabrielwhelan/barebones/drafts/crunch/history/'
def n(i,s,w,c=H): return (i,s,w,c)
# id: (cost, [links])
D=[
('0.b',1,[]),
('0.0',1,[]),
('0.1',1,[n('hist-eur3-s10.0.0',h,'the evacuation operation')]),
('0.2',1,[n('hist-eur3-s10.0.1',h,'billeting of evacuees')]),
('0.3',1,[n('hist-eur3-s9.0.3',h,'the Phoney War')]),
('0.4',2,[n('hist-eur3-s10.0.2',h,'urban poverty meeting rural hosts')]),
('0.5',1,[n('hist-eur3-s10.2.0',h,'the Blitz beginning')]),
('1.b',1,[]),
('1.0',1,[]),
('1.1',1,[]),
('1.2',2,[]),
('1.3',1,[n('hist-eur3-s10.2.9',h,'the Women\'s Land Army','low')]),
('1.4',1,[n('hist-eur3-s10.1.0',h,'rationing allowances')]),
('1.5',1,[n('hist-eur3-s10.1.0',h,'wartime rationing')]),
('2.b',1,[]),
('2.0',1,[]),
('2.1',2,[]),
('2.2',1,[]),
('2.3',1,[]),
('2.4',2,[]),
('2.5',2,[n('hist-eur3-s10.2.0',h,'the Blitz')]),
('2.6',1,[]),
('2.7',1,[n('hist-eur3-s10.0.5',h,'evacuation of children')]),
('2.8',2,[n('hist-eur3-s9.7.6',h,'Bevin in Churchill\'s coalition','low')]),
('2.9',1,[n('hist-eur3-s10.1.3',h,'the Land Army')]),
('2.10',2,[n('hist-eur3-s9.7.7',h,'Churchill\'s wartime speeches')]),
('2.11',1,[n('hist-eur3-s9.6.5',h,'V-1 and V-2 weapons')]),
('2.12',1,[n('hist-eur3-s10.3.5',h,'welfare reforms after 1945','low')]),
('3.b',1,[]),
('3.0',1,[]),
('3.1',2,[]),
('3.2',1,[]),
('3.3',1,[]),
('3.4',2,[]),
('3.5',2,[n('hist-eur3-s10.3.4',e,'the Beveridge Report')]),
('4.b',1,[]),
('4.0',1,[]),
('4.1',1,[n('hist-eur3-s3.8.1',e,'Goebbels\'s total war speech')]),
('4.2',1,[]),
('4.3',1,[n('hist-eur3-s10.4.2',h,'foreign forced labour')]),
('4.4',1,[n('hist-eur3-s10.4.2',h,'foreign workers in Germany','low')]),
('4.5',2,[n('hist-eur3-s9.6.1',h,'Allied bombing of Hamburg')]),
('5.b',1,[]),
('5.0',1,[n('hist-eur3-s9.1.0',h,'the German offensive of May 1940')]),
('5.1',2,[]),
('5.2',1,[]),
('5.3',1,[n('hist-eur3-s10.4.2',h,'forced labourers')]),
('5.4',1,[n('hist-eur3-s10.5.3',h,'displaced persons')]),
('6.b',1,[]),
('6.0',1,[]),
('6.1',1,[]),
('6.2',1,[]),
('6.3',2,[n('hist-eur3-s6.3.5',h,'Pétain\'s Vichy regime')]),
('6.4',1,[]),
('7.b',1,[]),
('7.0',2,[]),
('7.1',1,[]),
('7.2',1,[]),
('7.3',1,[]),
('7.4',1,[n('hist-eur3-s9.5.2',h,'German occupation of northern Italy')]),
('7.5',1,[n('hist-eur3-s6.6.3',h,'French Resistance activity','low')]),
('8.b',1,[]),
('8.0',1,[n('hist-eur3-s6.4.9',h,'rationing and the black market')]),
('8.1',1,[]),
('8.2',1,[n('hist-eur3-s9.5.3',h,'D-Day')]),
('8.3',1,[n('hist-eur3-s6.4.9',h,'French prisoners of war in Germany')]),
('8.4',2,[n('hist-eur3-s6.5.3',e,'compulsory labour service')]),
('8.5',1,[n('hist-eur3-s6.6.b',h,'the Resistance','low')]),
('9.b',1,[]),
('9.0',2,[n('hist-eur3-s10.3.5',h,'the Beveridge Report')]),
('9.1',1,[n('hist-eur3-s10.4.2',e,'foreign and forced labour')]),
('9.2',2,[n('hist-eur3-s10.7.1',h,'resistance bases for post-war governments','low')]),
('9.3',1,[n('hist-eur3-s10.8.5',h,'attentistes and passive civilians')]),
('9.4',1,[n('hist-eur3-s10.3.5',h,'welfare plans after the war')]),
('9.5',2,[n('hist-eur3-s6.6.10',h,'myth of a united resistance')]),
]
def run(pk,pre,D,out):
    ids=re.findall(r'^\[('+pre+r'[^\]]*)\]',open(P+'packs/'+pk).read(),re.M)
    allids=set(re.findall(r'^\[([^\]]+)\]',open(P+'packs/'+pk).read(),re.M))
    r={}
    for k,c,ls in D:
        r[pre+k]={'cost':c,'needs':[{'id':i,'strength':s,'why':w,'confidence':cf} for i,s,w,cf in ls]}
    tgt=[i for i in ids]
    assert list(r)==tgt,(set(tgt)^set(r))
    for v in r.values():
        for x in v['needs']: assert x['id'] in allids,x
    json.dump(r,open(P+'point-links/'+out,'w'),indent=1)
    nl=sum(len(v['needs']) for v in r.values())
    print(pk,len(r),nl,sum(v['cost']==2 for v in r.values()),sum(x['confidence']=='low' for v in r.values() for x in v['needs']))
run('hist-eur3-s10.t1g1.txt','hist-eur3-s10.',D,'hist-eur3-s10.t1g1.json')
