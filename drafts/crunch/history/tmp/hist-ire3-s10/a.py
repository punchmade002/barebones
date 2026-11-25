import json,re,sys
D='/Users/gabrielwhelan/barebones/.claude/worktrees/history-crunch/drafts/crunch/history/'
def N(i,s,w,c='h'): return {"id":i,"strength":{'e':'essential','h':'helpful'}[s],"why":w,"confidence":{'h':'high','l':'low'}[c]}
P='hist-ire3-s10.'
S3='hist-ire3-s3.';S6='hist-ire3-s6.'
d={
'0.b':(1,[]),
'0.0':(1,[N(S3+'1.0','h','Government of Ireland Act 1920')]),
'0.1':(1,[]),'0.2':(1,[]),'0.3':(1,[]),'0.4':(1,[]),
'1.b':(1,[]),'1.0':(1,[]),'1.1':(1,[]),'1.2':(1,[]),'1.3':(1,[]),'1.4':(1,[]),'1.5':(1,[]),
'1.6':(1,[N(S6+'5.b','h','the 1937 constitution')]),
'2.b':(2,[]),
'2.0':(1,[N(P+'1.0','h','compulsory Irish in schools')]),
'2.1':(1,[N(P+'1.3','h','the Gaeltacht defined')]),
'2.2':(1,[N(P+'1.0','h','the compulsion in schools')]),
'2.3':(1,[]),
'3.b':(1,[]),'3.0':(1,[]),'3.1':(1,[]),'3.2':(1,[]),'3.3':(1,[]),
'3.4':(1,[N(P+'4.6','h','1937 constitution on family and Church')]),
'3.5':(1,[]),
'4.b':(1,[]),'4.0':(1,[]),'4.1':(1,[]),'4.2':(1,[]),
'4.3':(2,[N(P+'4.2','e','the Censorship of Publications Act')]),
'4.4':(1,[]),'4.5':(1,[]),
'4.6':(1,[N(S6+'5.b','h','the 1937 constitution')]),
'4.7':(1,[]),
'5.b':(1,[]),'5.0':(1,[]),'5.1':(1,[]),
'5.2':(2,[]),'5.3':(1,[]),
'5.4':(1,[N(P+'0.1','e','the GAA')]),
'5.5':(1,[N(P+'5.4','e','the GAA ban on foreign games')]),
'5.6':(1,[N(P+'0.b','h','the Gaelic and Catholic ideal')]),
'6.b':(1,[N(S3+'3.b','h','Unionist government')]),
'6.0':(1,[]),
'6.1':(1,[N(P+'6.0','h','Lord Londonderry as Minister')],),
'6.2':(1,[N(P+'6.1','e','the 1923 Education Act')]),
'6.3':(1,[N(P+'6.1','h','the non-denominational state system')]),
'6.4':(2,[N(P+'6.1','e','transferred schools under the 1923 Act')]),
'6.5':(1,[N(P+'6.3','e','Catholic schools kept outside the state'),N(P+'6.4','h','the 1930 committee arrangement')]),
'7.b':(1,[]),'7.0':(1,[]),'7.1':(1,[]),
'7.2':(1,[N(P+'0.1','h','the GAA')]),
'7.3':(1,[N(S3+'2.6','e','the Special Powers Act','h')]),
'7.4':(1,[N(S3+'4.4','h','Craig 1934 statement'),N(P+'4.6','h','Catholic emphasis of the 1937 constitution')]),
'8.b':(1,[]),'8.0':(1,[]),'8.1':(1,[]),'8.2':(1,[]),'8.3':(1,[]),'8.4':(1,[]),'8.5':(1,[]),'8.6':(1,[]),'8.7':(1,[]),
'9.b':(1,[]),
'9.0':(2,[N(P+'1.4','h','An Gúm'),N(P+'5.1','h','the Abbey Theatre'),N(P+'5.2','h','Radio Éireann'),N(P+'5.3','h','the Folklore Commission')]),
'9.1':(1,[N(P+'1.0','h','compulsory Irish'),N(P+'2.1','h','Gaeltacht decline')]),
'9.2':(1,[N(P+'8.b','h','Evie Hone')]),
'9.3':(1,[N(P+'4.2','h','censorship of writers'),N(P+'0.3','h','conformity')]),
'9.4':(2,[N(P+'6.5','h','divided school system'),N(P+'7.b','h','separate cultural traditions')]),
'9.5':(1,[N(P+'0.3','h','conformist vision')]),
'9.6':(1,[]),
}
out={}
for k,(c,n) in d.items(): out[P+k]={"cost":c,"needs":n}
txt=open(D+'packs/hist-ire3-s10.t1g1.txt').read()
tg=[]; ids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M)); sec=txt.split('CANDIDATES')[0]
tg=re.findall(r'^\[([^\]]+)\]',sec,re.M)
assert set(tg)==set(out) and len(tg)==len(out),(set(tg)^set(out))
tg_ordered={k:out[k] for k in tg}
for v in tg_ordered.values():
  for n in v['needs']: assert n['id'] in ids,n
json.dump(tg_ordered,open(D+'point-links/hist-ire3-s10.t1g1.json','w'),ensure_ascii=False)
json.load(open(D+'point-links/hist-ire3-s10.t1g1.json'))
l=sum(len(v['needs']) for v in tg_ordered.values())
print(len(tg),l,sum(v['cost']==2 for v in tg_ordered.values()),sum(n['confidence']=='low' for v in tg_ordered.values() for n in v['needs']))
