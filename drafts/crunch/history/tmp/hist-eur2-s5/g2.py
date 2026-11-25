import json,re
H='/Users/gabrielwhelan/barebones/.claude/worktrees/history-crunch/drafts/crunch/history/'
def n(i,s,w,c='high'): return {"id":"hist-eur2-s2."+i,"strength":s,"why":w,"confidence":c}
Hh='helpful'
D={k:[] for k in []}
# every target id listed explicitly below; empty list = judged no link
ids=['0.b','0.0','0.1','0.2','0.3','0.4','0.5','1.b','1.0','1.1','1.2','1.3','1.4','1.5','2.b','2.0','2.1','2.2','2.3','3.b','3.0','3.1','3.2','3.3','3.4','4.b','4.0','4.1','4.2','4.3','4.4','5.b','5.0','5.1','5.2','6.b','6.0','6.1','6.2','6.3','7.b','7.0','7.1','7.2','7.3','7.4','7.5','8.b','8.0','8.1','8.2','9.b','9.0','9.1','9.2','9.3','10.b','10.0','10.1','10.2','10.3','11.b','11.0','11.1','11.2','11.3','11.4','12.b','12.0','12.1','12.2','13.b','13.0','13.1','13.2','13.3','13.4','14.b','14.0','14.1','14.2','14.3','14.4','14.5','15.b','15.0','15.1','15.2','16.b','16.0','16.1','16.2','16.3','16.4','17.b','17.0','17.1','17.2','17.3','17.4','17.5','17.6','18.b','18.0','18.1','18.2','19.b','19.0','19.1','19.2','19.3','20.b','20.0','20.1','20.2','20.3','20.4','21.b','21.0','21.1','21.2','21.3','21.4','21.5','21.6','21.7','21.8','22.b','22.0','22.1','22.2','22.3','22.4','22.5','23.b','23.0','23.1','23.2','23.3','23.4','24.b','24.0','24.1','24.2','24.3']
D={i:[] for i in ids}
D['0.0']=[n('3.3',Hh,'uses the Triple Entente')]
D['1.b']=[n('1.5',Hh,"uses Germany's plan against a two-front war",'low')]
D['14.0']=[n('3.4',Hh,'uses unreliable Italy in the Triple Alliance','low')]
D['14.5']=[n('7.2',Hh,'uses German colonies in Africa')]
D['15.1']=[n('2.0',Hh,"uses Germany's naval build-up")]
D['21.1']=[n('10.2',Hh,'uses Omdurman 1898'),n('11.0',Hh,'uses the Boer War')]
txt=open(H+'packs/hist-eur2-s5.t1g2.txt').read()
allids=set(re.findall(r'^\[(\S+?)\]',txt,re.M))
tgt=re.findall(r'^\[(\S+?)\]',txt.split('CANDIDATES')[0],re.M)
assert [ 'hist-eur2-s5.'+i for i in ids]==tgt
out={t:{"needs":D[t.replace('hist-eur2-s5.','')]} for t in tgt}
for t,v in out.items():
    for x in v['needs']: assert x['id'] in allids
json.dump(out,open(H+'point-links/hist-eur2-s5.t1g2.json','w'))
c=json.load(open(H+'point-links/hist-eur2-s5.t1g2.json'))
print(len(c),sum(len(v['needs']) for v in c.values()),sum(x['confidence']=='low' for v in c.values() for x in v['needs']))
