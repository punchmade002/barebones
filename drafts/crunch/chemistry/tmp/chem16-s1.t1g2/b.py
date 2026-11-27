import json,re
D='/Users/gabrielwhelan/barebones/.claude/worktrees/crunch-chem-home/drafts/crunch/chemistry/'
P='chem16-s1.'
E,H='essential','helpful'
def L(i,s,w,c='high'): return {'id':i,'strength':s,'why':w,'confidence':c}
c8='chem8-s2.2.1'
R={
'0.b':[L('chem13-s1.0.0',H,'acid-base mole steps')],
'0.0':[L(c8,E,'n = c x V')],
'0.1':[],'0.2':[],'0.3':[],'0.4':[],
'0.5':[L('chem13-s1.1.0',H,'titration formula with coefficients')],
'0.6':[L('chem13-s1.1.1',H,'volumes in cm3 cancel')],
'0.7':[],'0.8':[],
'1.b':[],'1.0':[],'1.1':[],'1.2':[],'1.3':[],
'1.4':[L('chem8-s2.5.1',H,'ammonium iron(II) sulfate as standard')],
'1.5':[],'1.6':[],
'2.b':[],'2.0':[],'2.1':[],'2.2':[],'2.3':[],'2.4':[],'2.5':[],'2.6':[],
'3.b':[],
'3.0':[L('chem13-s1.2.3',H,'scaling up a portion titrated')],
'3.1':[],'3.2':[],'3.3':[],'3.4':[],
'3.5':[L('chem8-s2.11.0',H,'mol per litre to g per litre')],
'3.6':[L('chem8-s2.11.2',H,'g per litre to %w/v')],
'3.7':[],
'4.b':[],'4.0':[],'4.1':[],'4.2':[],'4.3':[],
'5.b':[],
'5.0':[L('chem13-s1.3.0',H,'mean of concordant titres')],
'5.1':[L('chem13-s1.3.1',H,'three significant figures with units')],
'5.2':[L('chem13-s1.3.2',H,'sense check of answer')],
'5.3':[L('chem13-s1.3.2',H,'percentage cannot exceed 100')],
'5.4':[],'5.5':[],
'6.b':[],'6.0':[],'6.1':[],'6.2':[],'6.3':[],'6.4':[],
'6.5':[L('chem13-s1.4.2',H,'plan route through moles')],
'7.b':[],'7.0':[],'7.1':[],'7.2':[],'7.3':[],
'8.b':[],'8.0':[],
'8.1':[L('chem8-s2.4.0',H,'primary standard definition')],
'8.2':[],
'9.b':[],'9.0':[],'9.1':[],'9.2':[],
'9.3':[L(c8,E,'c = n / V')],
'9.4':[L(c8,E,'n = c x V')],
'9.5':[],
'9.6':[L(c8,E,'c = n / V')],
'9.7':[L('chem8-s2.11.0',H,'mol per litre to g per litre')],
'10.b':[],'10.0':[],
'10.1':[L(c8,E,'n = c x V')],
'10.2':[],
'10.3':[L('chem13-s1.2.3',E,'scaling portion to whole sample')],
'10.4':[],'10.5':[],'10.6':[],'10.7':[],
'11.b':[],'11.0':[],'11.1':[],'11.2':[],
'11.3':[L(c8,E,'n = c x V')],
'11.4':[],'11.5':[],
'11.6':[L(c8,E,'c = n / V')],
'11.7':[L('chem8-s2.11.0',E,'mol per litre to g per litre')],
'12.b':[],'12.0':[],'12.1':[],
'12.2':[L(c8,E,'n = c x V')],
'12.3':[],
'12.4':[L(c8,E,'c = n / V')],
'12.5':[L('chem13-s1.2.1',E,'dilution factor scales concentration')],
'12.6':[],
'12.7':[L('chem8-s2.11.2',E,'g per litre to %w/v')],
'13.b':[],'13.0':[],'13.1':[],'13.2':[],
'13.3':[L(c8,E,'n = c x V')],
'13.4':[],
'13.5':[L(c8,E,'c = n / V')],
'13.6':[L('chem13-s1.2.1',H,'dilution factor scales concentration')],
'13.7':[L('chem8-s2.11.2',E,'g per litre to %w/v')],
}
txt=open(D+'packs/chem16-s1.t1g2.txt').read()
tids=re.findall(r'^\[(\S+?)\]',txt.split('CANDIDATES')[0],re.M)
allids=set(re.findall(r'^\[(\S+?)\]',txt,re.M))
assert [i[len(P):] for i in tids]==list(R),set(tids)^{P+k for k in R}
out={}
cands={i for i in allids if not i.startswith(P)}
for k,n in R.items():
    out[P+k]={'needs':n}
    for x in n: assert x['id'] in cands
json.dump(out,open(D+'point-links/chem16-s1.t1g2.json','w'),ensure_ascii=False)
print(len(out),sum(len(v['needs']) for v in out.values()),sum(x['confidence']=='low' for v in out.values() for x in v['needs']))
