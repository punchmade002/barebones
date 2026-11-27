import json,re
D='/Users/gabrielwhelan/barebones/.claude/worktrees/crunch-chem-home/drafts/crunch/chemistry/'
def L(i,s,w,c='high'): return {"id":i,"strength":s,"why":w,"confidence":c}
E,H='essential','helpful'
P='chem21-s2.'
R={
'0.b':[],
'0.0':[L('chem11-s1.4.b',H,'neutralisation of acid by base')],
'0.1':[L('chem11-s1.4.b',H,'neutralisation of acid by base')],
'0.2':[L('chem11-s1.6.4',H,'ionic equation for strong acid and alkali')],
'0.3':[],'0.4':[],
'1.b':[],
'1.0':[L('chem1-s4.1.7',H,'volumetric glassware more accurate than cylinder','low')],
'1.1':[],
'1.2':[L('chem1-s4.1.2',H,'instrument resolution','low')],
'1.3':[],'1.4':[],'1.5':[],
'1.6':[L('chem1-s4.2.0',H,'repeating reduces random error')],
'1.7':[],
'2.b':[],'2.0':[],'2.1':[],
'2.2':[L('chem1-s4.2.7',H,'percentage error','low')],
'2.3':[],'2.4':[],
'2.5':[L('chem1-s4.1.2',H,'instrument resolution')],
'2.6':[L('chem1-s4.1.7',H,'volumetric glassware accuracy')],
'2.7':[],
'3.b':[],'3.0':[],'3.1':[],'3.2':[],
'3.3':[L('chem1-s4.6.3',E,'extrapolation of a graph line')],
'3.4':[L('chem1-s4.6.3',H,'extrapolation of a graph line')],
'4.b':[],'4.0':[],
'4.1':[L('chem1-s4.0.3',H,'°C and K temperature scales')],
'4.2':[],'4.3':[],
'4.4':[L('chem1-s4.0.1',H,'convert cm³ to litres','low')],
'4.5':[],'4.6':[],
'4.7':[L('chem1-s4.2.3',H,'heat loss as systematic error','low')],
'5.b':[],
'5.0':[L('chem11-s1.6.4',E,'ionic equation for strong acid and alkali')],
'5.1':[],
'5.2':[L('chem11-s1.5.3',H,'diprotic acid reacts with two hydroxides')],
'5.3':[],'5.4':[],
'5.5':[L('chem1-s4.0.1',H,'convert cm³ to litres','low')],
'5.6':[],
'6.b':[],
'6.0':[L('chem11-s1.1.5',H,'corrosive concentrated alkalis')],
'6.1':[],
'6.2':[L('chem1-s4.2.3',E,'heat loss as systematic error')],
'6.3':[L('chem1-s4.2.2',H,'systematic error from assumption','low')],
'6.4':[L('chem1-s4.1.7',H,'volumetric glassware accuracy','low')],
'7.b':[],'7.0':[],
'7.1':[L('chem1-s4.0.3',H,'°C to K conversion'),L('chem1-s4.0.4',H,'pressure units and atmosphere')],
'7.2':[],'7.3':[],
'7.4':[L('chem1-s4.0.4',H,'IUPAC standard pressure 100 kPa')],
'7.5':[],
'8.b':[],'8.0':[],'8.1':[],'8.2':[],
'8.3':[L('chem1-s4.0.1',H,'convert cm³ to litres')],
'8.4':[],'8.5':[],'8.6':[],'8.7':[],'8.8':[],
'9.b':[],'9.0':[],'9.1':[],'9.2':[],'9.3':[],
'9.4':[L('chem1-s4.0.1',H,'convert cm³ to litres','low')],
'9.5':[],
'9.6':[L('chem1-s4.2.3',H,'heat loss as systematic error','low')],
'10.b':[],'10.0':[],'10.1':[],'10.2':[],'10.3':[],
'11.b':[],
'11.0':[L('chem1-s4.5.0',H,'graph axes and labels','low')],
'11.1':[],'11.2':[],'11.3':[],'11.4':[],'11.5':[],'11.6':[],'11.7':[],
}
R={P+k:v for k,v in R.items()}
txt=open(D+'packs/chem21-s2.t1g2.txt').read()
tids=re.findall(r'^\[(\S+?)\]',txt.split('CANDIDATES')[0],re.M)
cand=set(re.findall(r'^\[(\S+?)\]',txt.split('CANDIDATES',1)[1],re.M))
assert set(tids)==set(R) and len(tids)==len(R),set(tids)^set(R)
for i,n in R.items():
    for l in n: assert l['id'] in cand,(i,l)
json.dump({i:{"needs":R[i]} for i in tids},open(D+'point-links/chem21-s2.t1g2.json','w'),ensure_ascii=False,indent=1)
o=json.load(open(D+'point-links/chem21-s2.t1g2.json'))
print(len(o),sum(len(v['needs']) for v in o.values()),sum(l['confidence']=='low' for v in o.values() for l in v['needs']))
