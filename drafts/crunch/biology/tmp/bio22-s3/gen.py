import json,re
P='/Users/gabrielwhelan/barebones/drafts/crunch/biology/'
txt=open(P+'points/bio22-s3.txt').read()
tgt,cand=txt.split('\nCANDIDATES',1)
tids=re.findall(r'^\[(\S+?)\]',tgt,re.M)
allids=set(re.findall(r'^\[(\S+?)\]',txt,re.M))
E,H='essential','helpful'
def n(i,s,w,c='high'):return dict(id=i,strength=s,why=w,confidence=c)
S='bio22-s3.'
c2={'0.0','1.1','1.2','1.7','2.2','3.4','4.0','4.2','5.0','6.5','7.1','8.5','9.2','9.3','9.6','10.0'}
N={
'0.0':[n('bio22-s2.7.0',H,'antibodies')],
'0.1':[n('bio22-s2.9.7',E,'memory cells persist')],
'0.2':[n(S+'0.0',H,'contrast with active','low')],
'0.3':[n(S+'0.2',E,'passive immunity')],
'0.4':[n('bio22-s2.10.0',E,'primary response')],
'1.0':[n(S+'0.0',E,'active immunity, memory cells')],
'1.1':[n(S+'0.0',E,'active immunity'),n(S+'2.0',H,'vaccine contains antigens')],
'1.2':[n(S+'0.2',E,'passive immunity'),n('bio22-s2.7.0',H,'antibodies')],
'1.3':[n(S+'0.2',E,'passive immunity')],
'1.4':[n(S+'0.3',H,'passive protection short-lived')],
'1.5':[n(S+'0.2',E,'passive immunity')],
'1.6':[n(S+'1.5',H,'donor antibody injection')],
'1.7':[n(S+'0.1',E,'active immunity slow, long-lasting'),n(S+'0.3',E,'passive immunity fast, short-lived')],
'2.0':[n('bio22-s2.6.0',E,'antigen'),n(S+'0.0',H,'active immunity','low')],
'2.1':[n(S+'2.0',E,'vaccine antigens'),n('bio22-s2.10.0',H,'primary response')],
'2.2':[n('bio22-s2.10.2',E,'secondary response')],
'3.0':[n(S+'2.0',E,'vaccine presents antigen safely')],
'3.1':[n(S+'2.0',E,'vaccine presents antigen safely')],
'3.2':[n(S+'2.0',H,'vaccine presents antigen')],
'3.3':[n('bio22-s2.6.0',H,'antigen')],
'3.4':[n(S+'2.0',H,'vaccine presents antigen')],
'3.5':[n(S+'2.0',H,'vaccine presents antigen','low')],
'4.0':[n('bio22-s2.10.2',E,'secondary response'),n('bio22-s2.9.7',H,'memory cells')],
'4.1':[n(S+'0.0',E,'active immunity'),n(S+'0.2',E,'passive immunity')],
'4.2':[n(S+'2.2',H,'immunity prevents disease','low')],
'4.3':[n(S+'4.2',H,'who herd immunity protects')],
'4.4':[n(S+'4.2',E,'herd immunity')],
'5.0':[n(S+'0.0',H,'active immunity from exposure','low')],
'5.1':[n(S+'2.0',H,'vaccination','low')],
'5.2':[n(S+'4.2',E,'herd immunity')],
'5.4':[n(S+'3.0',E,'live attenuated vaccines')],
'5.5':[n(S+'4.2',E,'herd immunity')],
'7.0':[n(S+'4.2',H,'herd immunity')],
'9.1':[n(S+'9.0',H,'antibodies defined')],
'9.2':[n(S+'9.1',H,'bacterial cell wall target')],
'9.3':[n(S+'9.1',H,'bacterial-only structures')],
'9.4':[n(S+'9.2',H,'cell wall target','low'),n(S+'9.3',H,'ribosome target','low')],
'9.5':[n(S+'9.0',H,'antibiotics')],
'9.6':[n(S+'9.5',H,'antibiotic use')],
'10.1':[n(S+'10.0',E,'antivirals')],
'10.0':[n(S+'9.4',H,'virus lacks bacterial targets')],
'10.5':[n('bio22-s2.7.0',E,'antibodies')],
}
out={}
for t in tids:
    k=t.replace(S,'')
    out[t]={'cost':2 if k in c2 else 1,'needs':N.get(k,[])}
json.dump(out,open(P+'point-links/bio22-s3.json','w'),indent=1)
o=json.load(open(P+'point-links/bio22-s3.json'))
assert list(o)==tids and len(set(tids))==len(tids)
for t,v in o.items():
    for x in v['needs']: assert x['id'] in allids and x['id']!=t,(t,x)
ls=[x for v in o.values() for x in v['needs']]
print(len(o),len(ls),sum(v['cost']==2 for v in o.values()),sum(x['confidence']=='low' for x in ls))
