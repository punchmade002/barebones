import json,re
B='/Users/gabrielwhelan/barebones/.claude/worktrees/history-crunch/drafts/crunch/history/'
H,E='helpful','essential'
def L(i,s,w,c='high'): return {"id":i,"strength":s,"why":w,"confidence":c}
def run(pkg,out,prefix,spec):
    txt=open(B+'packs/'+pkg).read()
    tgt=[]; ids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
    for l in txt.split('\n'):
        if l.startswith('CANDIDATES'): break
        m=re.match(r'\[([^\]]+)\]',l)
        if m: tgt.append(m.group(1))
    res={}
    for t in tgt:
        k=t[len(prefix)+1:]
        assert k in spec,t
        c,n=spec[k]; res[t]={"cost":c,"needs":[L(prefix+'-'+a if False else a,s,w,cf) for a,s,w,cf in n]}
    assert len(spec)==len(tgt),(len(spec),len(tgt))
    for t,v in res.items():
        for n in v['needs']: assert n['id'] in ids and n['id']!=t,(t,n)
    json.dump(res,open(B+'point-links/'+out,'w'),indent=1)
    nl=sum(len(v['needs']) for v in res.values())
    print(out,len(res),nl,sum(v['cost']==2 for v in res.values()),sum(n['confidence']=='low' for v in res.values() for n in v['needs']))
S='hist-ire2-s10.'
def l(i,s,w,c='high'): return (i,s,w,c)
sp={}
def a(k,c,*n): sp[k]=(c,list(n))
for k in ['0.b','0.0','0.1','0.2','0.3','0.4']: a(k,1)
sp['0.6']=(2,[]); sp['0.5']=(1,[l(S+'0.2',H,'Hyde\'s approach')])
a('0.7',1,l('hist-ire2-s9.3.3',H,'GAA founding meeting at Thurles'))
a('1.b',1); a('1.0',1,l(S+'6.0',H,'National Literary Society'))
a('1.1',2,l(S+'0.2',E,'anglicisation'))
a('1.2',1,l(S+'0.2',H,'anglicisation and de-anglicisation'))
a('1.3',1,l(S+'2.1',H,'League welcoming all creeds'))
a('1.4',1,l(S+'0.0',H,'Famine decline of Irish'))
a('1.5',1,l('hist-ire2-s9.3.3',H,'GAA founded 1884'),l(S+'2.0',H,'founding of Gaelic League'))
a('2.b',1); a('2.0',1); a('2.1',1,l(S+'0.3',H,'unionists'))
for k in ['2.2','2.3','2.4','2.5','2.6','2.7','3.b']: a(k,1)
a('3.0',1); a('3.1',1); a('3.2',1,l(S+'2.1',H,'League non-political stance'))
a('3.3',1); a('3.4',1,l(S+'2.6',E,'compulsory Irish for NUI'))
a('4.b',1); a('4.0',1); a('4.1',1,l(S+'6.1',H,'Casadh an tSúgáin staged 1901'))
a('4.2',1,l(S+'1.0',H,'the 1892 lecture'),l(S+'2.0',H,'founding the League'))
a('4.3',1,l(S+'3.1',E,'IRB politicising the League'))
a('4.4',2,l(S+'0.5',H,'Irish Ireland critics'),l(S+'3.1',H,'League turning political'))
a('4.5',1); a('4.6',1)
a('5.b',1); a('5.0',1,l(S+'0.5',H,'Irish Ireland')); a('5.1',1,l(S+'0.3',H,'Anglo-Irish label'),l(S+'6.b',H,'Literary Revival'))
a('5.2',1,l(S+'0.5',H,'Irish Ireland'))
a('5.3',1); a('5.4',1); a('5.5',1,l(S+'2.1',H,'Hyde\'s inclusive League'))
a('6.b',1,l(S+'0.3',H,'Anglo-Irish label')); a('6.0',1); a('6.1',2); a('6.2',1); a('6.3',2,l(S+'6.1',H,'Yeats, Gregory and the theatre'))
a('6.4',1,l(S+'0.3',H,'Anglo-Irish'),l(S+'6.3',H,'Abbey directors')); a('6.5',1,l(S+'6.3',H,'the Abbey Theatre'))
a('7.b',1); a('7.0',1); a('7.1',1); a('7.2',1,l(S+'6.0',H,'National Literary Society'),l(S+'6.1',H,'Irish Literary Theatre'),l(S+'6.3',H,'the Abbey'))
a('7.3',2,l(S+'8.0',E,'Countess Cathleen controversy'),l(S+'8.1',E,'Playboy riots'),l(S+'8.2',E,'Hugh Lane dispute'))
a('7.4',2,l(S+'8.2',E,'Hugh Lane dispute'))
a('7.5',1,l(S+'8.0',H,'Catholic attack on Countess Cathleen'),l(S+'5.1',H,'Moran\'s attacks'))
a('7.6',1); a('7.7',1)
a('8.b',1); a('8.0',1,l(S+'6.1',E,'The Countess Cathleen staged')); a('8.1',2,l(S+'6.5',E,'Synge\'s Playboy'))
a('8.2',2); a('8.3',1,l(S+'8.2',E,'Lane dispute'))
a('8.4',1,l(S+'5.2',H,'Gaelic and Catholic nation')); a('8.5',1,l(S+'8.4',H,'two visions'))
a('9.b',1); a('9.0',2,l(S+'0.6',E,'Cullen\'s reform of Catholic practice'))
for k in ['9.1','9.2','9.4','9.5']: a(k,1)
a('9.3',1,l('hist-ire2-s9.4.5',H,'priests in GAA clubs'))
a('10.b',1); a('10.0',1); a('10.1',1); a('10.2',1,l(S+'0.6',H,'Church and Home Rule'))
a('10.3',2,l('hist-ire2-s4.2.1',E,'bishops condemned Parnell'),l(S+'10.0',H,'Ne Temere'))
a('11.b',1); a('11.0',1,l('hist-ire2-s9.8.2',E,'Parnell split'))
a('11.1',1,l('hist-ire2-s9.5.3',E,'foreign games ban'),l('hist-ire2-s9.7.0',H,'IRB in the GAA'))
a('11.2',1); a('11.3',1,l(S+'3.0',H,'League membership')); a('11.4',1,l(S+'2.1',H,'League non-political'))
a('11.5',1,l('hist-ire2-s9.2.5',H,'Cusack and Davin'))
a('12.b',1); a('12.0',1); a('12.1',1,l(S+'3.3',H,'language did not revive'))
a('12.2',1,l(S+'5.1',H,'Moran on Anglo-Irish literature')); a('12.3',1)
run('hist-ire2-s10.t1g1.txt','hist-ire2-s10.t1g1.json','hist-ire2-s10',{k:v for k,v in sp.items()})
