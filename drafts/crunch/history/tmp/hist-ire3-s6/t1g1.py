import json,re
P='/Users/gabrielwhelan/barebones/.claude/worktrees/history-crunch/drafts/crunch/history/'
E,H='essential','helpful'
def L(i,s,w,c='high'): return {"id":i,"strength":s,"why":w,"confidence":c}
p='hist-ire3-s6.'
D={
'0.b':(1,[]),
'0.0':(1,[L('hist-ire3-s4.5.0',H,'dominion status')]),
'0.1':(2,[L('hist-ire3-s4.5.2',H,'the oath of allegiance'),L('hist-ire3-s4.5.3',H,'the treaty ports')]),
'0.2':(1,[L('hist-ire3-s5.10.0',H,'joining the League of Nations')]),
'0.3':(1,[L('hist-ire3-s5.12.2',H,'the Tripartite Agreement')]),
'0.4':(2,[L(p+'0.0',H,'dominion status'),L('hist-ire3-s5.13.0',H,'Kevin O\'Higgins')]),
'0.5':(1,[L(p+'0.0',H,'dominion status')]),
'0.6':(1,[L(p+'0.1',E,'the oath, Governor-General and ports')]),
'0.7':(1,[L(p+'3.b',H,'the land annuities dispute')]),
'1.b':(1,[L(p+'0.1',H,'the Treaty symbols to remove'),L('hist-ire3-s5.0.4',H,'anti-Treaty republican stance','low')]),
'1.0':(1,[L('hist-ire3-s5.14.1',H,'founding of Fianna Fáil')]),
'1.1':(1,[L('hist-ire3-s5.8.0',H,'Cumann na nGaedheal and Cosgrave')]),
'1.2':(1,[L(p+'1.0',H,'Fianna Fáil')]),
'1.3':(1,[L(p+'1.2',H,'the 1932 election result')]),
'1.4':(1,[L(p+'1.2',H,'reliance on Labour support'),L(p+'2.b',H,'Treaty-dismantling laws','low')]),
'2.b':(1,[L(p+'0.5',E,'the Statute of Westminster')]),
'2.0':(2,[L('hist-ire3-s5.8.5',H,'McNeill as Governor-General'),L(p+'0.1',H,'the Governor-General')]),
'2.1':(2,[L(p+'0.1',E,'the oath of allegiance')]),
'2.2':(1,[L(p+'2.b',H,'Westminster basis for legislation','low')]),
'2.3':(1,[]),
'2.4':(2,[L(p+'2.0',H,'the Governor-General office'),L(p+'0.1',H,'the Crown')]),
'2.5':(1,[L(p+'2.4',E,'the Crown removed from the Constitution')]),
'2.6':(2,[L(p+'0.5',E,'the Statute of Westminster'),L(p+'2.5',H,'the 1936 External Relations Act')]),
'3.b':(1,[L(p+'0.7',H,'the land annuities')]),
'3.0':(1,[L(p+'0.7',H,'the land annuities')]),
'3.1':(1,[L(p+'0.7',E,'the 1920s annuity arrangements')]),
'3.2':(1,[L(p+'3.0',H,'the annuities withheld')]),
'3.3':(1,[L(p+'3.2',E,'British special duties')]),
'3.4':(1,[L(p+'3.2',H,'the cattle trade dispute')]),
'3.5':(1,[L(p+'3.b',H,'the Economic War'),L('hist-ire3-s5.8.0',H,'Cumann na nGaedheal','low')]),
'4.b':(1,[]),
'4.0':(1,[L('hist-ire3-s5.8.0',H,'Cumann na nGaedheal')]),
'4.1':(2,[L(p+'4.0',E,'the Army Comrades Association'),L('hist-ire3-s5.9.1',H,'O\'Duffy as Garda Commissioner')]),
'4.2':(2,[L(p+'4.1',E,'the Blueshirts under O\'Duffy')]),
'4.3':(2,[L(p+'4.2',H,'the banned National Guard'),L('hist-ire3-s5.8.0',H,'Cumann na nGaedheal')]),
'4.4':(1,[L(p+'4.1',H,'the Blueshirt challenge')]),
'4.5':(1,[L(p+'4.1',H,'Eoin O\'Duffy')]),
'5.b':(1,[L(p+'2.5',H,'the monarchy and the republic issue','low')]),
'5.0':(1,[]),
'5.1':(1,[L(p+'5.b',H,'the new constitution')]),
'5.2':(2,[L(p+'5.1',H,'the 1937 constitution')]),
'5.3':(1,[L(p+'1.3',E,'President of the Executive Council')]),
'6.b':(1,[L(p+'5.b',H,'the 1937 constitution')]),
'6.0':(2,[L('hist-ire3-s3.0.b',H,'partition and Northern Ireland')]),
'6.1':(1,[L(p+'5.b',H,'the 1937 constitution')]),
'6.2':(2,[L(p+'5.b',H,'the 1937 constitution')]),
'6.3':(1,[L(p+'6.0',H,'the Articles 2 and 3 claim','low')]),
'6.4':(1,[L(p+'5.3',H,'the office of President')]),
'7.b':(1,[L(p+'0.1',H,'the Treaty ports')]),
'7.0':(1,[L(p+'0.1',E,'the Treaty ports')]),
'7.1':(2,[L(p+'3.0',E,'the annuities dispute'),L(p+'3.b',H,'the Economic War')]),
'7.2':(1,[L(p+'3.2',E,'the special duties')]),
'7.3':(2,[L(p+'7.0',H,'giving up the ports')]),
'7.4':(1,[L('hist-ire3-s3.0.b',H,'partition'),L(p+'7.0',H,'the ports talks')]),
'7.5':(1,[L(p+'7.0',E,'Irish control of the ports')]),
'8.b':(1,[L(p+'2.5',E,'the External Relations Act')]),
'8.0':(2,[L(p+'1.4',H,'Fianna Fáil\'s majority')]),
'8.1':(1,[L(p+'2.5',E,'the External Relations Act')]),
'8.2':(1,[L(p+'8.1',H,'MacBride\'s repeal plan')]),
'8.3':(1,[L(p+'2.5',E,'the External Relations Act')]),
'8.4':(1,[L(p+'8.3',E,'Ireland leaving the Commonwealth')]),
'8.5':(1,[L('hist-ire3-s3.0.b',H,'partition'),L(p+'8.4',H,'the Ireland Act 1949')]),
'8.6':(1,[L('hist-ire3-s3.0.b',H,'partition')]),
'8.7':(2,[L(p+'7.0',H,'the 1938 settlement'),L(p+'8.3',E,'the 1949 Republic of Ireland Act')]),
'9.b':(2,[L(p+'1.3',H,'de Valera as head of government')]),
'9.0':(2,[L(p+'2.1',H,'removing the oath'),L(p+'2.2',H,'ending Privy Council appeals'),L(p+'2.4',H,'the 1936 Acts'),L(p+'4.4',H,'banning the IRA'),L(p+'5.b',H,'the 1937 constitution'),L(p+'7.0',H,'securing the ports'),L(p+'7.5',H,'wartime neutrality')]),
'9.1':(2,[L(p+'0.5',H,'the Statute of Westminster'),L(p+'2.4',H,'the 1936 abdication'),L(p+'4.b',H,'the Blueshirts'),L(p+'7.3',H,'war approaching and the ports')]),
'9.2':(1,[L(p+'1.3',E,'his External Affairs role'),L(p+'5.0',E,'drafting the 1937 constitution')]),
'9.3':(1,[L('hist-ire3-s3.0.b',H,'partition'),L(p+'3.b',H,'the Economic War')]),
'9.4':(1,[L(p+'6.1',H,'the conservative constitution','low')]),
'9.5':(2,[L(p+'4.b',H,'the Blueshirts as opponents','low')]),
'9.6':(2,[]),
'9.7':(2,[]),
'10.b':(1,[L('hist-ire3-s5.17.b',H,'Cosgrave\'s record')]),
'10.0':(2,[L('hist-ire3-s5.10.0',H,'international recognition'),L(p+'0.4',H,'use of the Commonwealth')]),
'10.1':(2,[L(p+'0.6',E,'oath, Governor-General and ports left'),L('hist-ire3-s5.12.2',H,'Boundary Commission failure')]),
'10.2':(2,[L(p+'9.0',H,'removing symbols'),L(p+'7.0',H,'the ports settlement'),L(p+'7.1',H,'the annuities settlement'),L(p+'5.b',H,'the constitution')]),
'10.3':(2,[L(p+'3.b',E,'the Economic War'),L('hist-ire3-s3.0.b',H,'partition'),L(p+'0.4',E,'Balfour groundwork'),L(p+'0.5',E,'Westminster groundwork')]),
'10.4':(1,[L(p+'9.5',H,'Fianna Fáil supporters\' view','low')]),
'10.5':(1,[L(p+'8.3',E,'the 1949 Republic Act'),L('hist-ire3-s3.0.b',H,'partition')]),
}
out={p+k:({"cost":v[0],"needs":v[1]}) for k,v in D.items()}
txt=open(P+'packs/hist-ire3-s6.t1g1.txt').read().split('\n')
ids=set(re.findall(r'^\[([^\]]+)\]',"\n".join(txt),re.M))
tg=[]
for l in txt[:83]:
    m=re.match(r'\[([^\]]+)\]',l)
    if m: tg.append(m.group(1))
assert set(tg)==set(out) and len(tg)==len(out),(set(tg)^set(out))
for k,v in out.items():
    for n in v['needs']:
        assert n['id'] in ids and n['id']!=k,(k,n)
out={k:out[k] for k in tg}
json.dump(out,open(P+'point-links/hist-ire3-s6.t1g1.json','w'),ensure_ascii=False,indent=0)
n=sum(len(v['needs']) for v in out.values())
print(len(out),n,sum(v['cost']==2 for v in out.values()),sum(x['confidence']=='low' for v in out.values() for x in v['needs']))
