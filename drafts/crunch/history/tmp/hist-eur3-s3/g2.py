import json,re
P='hist-eur3-s3.'
def L(i,w,c='high'): return {"id":i,"strength":"helpful","why":w,"confidence":c}
D={k:[] for k in """0.b 0.0 0.1 0.2 0.3 0.4 1.b 1.0 1.1 1.2 1.3 1.4 1.5 1.6 2.b 2.0 2.1 2.2 2.3 2.4 3.b 3.0 3.1 3.2 3.3 3.4 3.5 3.6 4.b 4.0 4.1 4.2 4.3 4.4 5.b 5.0 5.1 5.2 5.3 5.4 5.5 6.b 6.0 6.1 6.2 6.3 7.b 7.0 7.1 7.2 7.3 8.b 8.0 8.1 8.2 8.3 8.4 8.5 8.6 9.b 9.0 9.1 9.2 9.3 9.4 9.5 10.b 10.0 10.1 10.2 10.3 10.4 10.5 10.6 11.b 11.0 11.1 11.2 11.3 11.4 11.5 11.6 11.7 12.b 12.0 12.1 12.2 12.3 12.4 12.5 12.6 12.7 13.b 13.0 13.1 13.2 13.3 13.4 13.5 13.6 14.b 14.0 14.1 14.2 14.3 14.4 14.5 14.6 15.b 15.0 15.1 15.2 15.3 15.4 15.5 15.6 16.b 16.0 16.1 16.2 16.3 17.b 17.0 17.1 17.2 17.3 17.4 17.5 18.b 18.0 18.1 18.2 18.3 18.4 18.5 18.6 18.7 19.b 19.0 19.1 19.2 19.3 19.4 19.5 19.6 19.7""".split()}
D['4.2']=[L('hist-eur3-s1.3.1','personality cult of the leader')]
D['4.4']=[L('hist-eur3-s1.3.0','definition of dictatorship')]
D['11.0']=[L('hist-eur3-s1.0.4','role of the League of Nations','low')]
D['11.2']=[L('hist-eur3-s1.11.2','Mussolini at the Brenner Pass')]
D['11.5']=[L('hist-eur3-s1.12.0','Italy invading Abyssinia'),L('hist-eur3-s1.11.3','Italy joining the Stresa Front')]
D['12.2']=[L('hist-eur3-s1.13.1','Mussolini and the Rome-Berlin Axis')]
D['12.3']=[L('hist-eur3-s1.13.0','joint intervention for Franco','low')]
D['13.3']=[L('hist-eur3-s1.13.3','Mussolini at Munich')]
D['15.2']=[L('hist-eur3-s1.3.2','totalitarianism defined')]
D['19.0']=[L('hist-eur3-s1.3.2','totalitarianism defined'),L('hist-eur3-s1.3.3','limits to totalitarian control','low')]
txt=open('packs/hist-eur3-s3.t1g2.txt').read()
tgt=[];allids=set();sec=None
for l in txt.split('\n'):
    if l.startswith('TARGET'): sec='t'
    elif l.startswith('CANDIDATES'): sec='c'
    m=re.match(r'\[(\S+?)\]',l)
    if m:
        allids.add(m.group(1))
        if sec=='t': tgt.append(m.group(1))
assert [t[len(P):] for t in tgt]==list(D) , 'order'
out={t:{"needs":D[t[len(P):]]} for t in tgt}
for v in out.values():
    for n in v['needs']: assert n['id'] in allids and len(n['why'].split())<=8
json.dump(out,open('point-links/hist-eur3-s3.t1g2.json','w'),ensure_ascii=False,indent=0)
print(len(out),sum(len(v['needs']) for v in out.values()),sum(n['confidence']=='low' for v in out.values() for n in v['needs']))
