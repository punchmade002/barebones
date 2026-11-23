import json,re
P='/Users/gabrielwhelan/barebones/drafts/crunch/biology/'
txt=open(P+'points/bio31-s3.txt').read()
tgt=txt.split('CANDIDATES')[0]
tids=re.findall(r'^\[([^\]]+)\]',tgt,re.M)
allids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
E,H='essential','helpful'
# id: (cost, [(need, strength, why, conf)])
S='bio31-s3.'
D={
'0.0':(2,[]),
'0.1':(1,[('0.0',H,'list of activities','high')]),
'0.6':(2,[('0.5',E,'richness and evenness','high')]),
'1.2':(1,[('bio2-s2.0.1',E,'independent variable','high')]),
'1.3':(1,[('bio2-s2.0.2',E,'dependent variable','high'),('0.5',H,'species number and cover','high')]),
'1.4':(2,[('bio2-s2.0.3',E,'controlled variables','high')]),
'1.5':(1,[('bio2-s2.2.1',E,'control set-up','high')]),
'1.6':(2,[('bio32-s2.3.1',H,'gridded quadrat','high')]),
'2.1':(1,[('bio32-s2.1.1',H,'random sampling','high')]),
'2.2':(1,[('bio32-s2.2.1',H,'more samples more reliable','high')]),
'2.3':(2,[('bio32-s2.5.1',H,'percentage cover method','high')]),
'2.4':(1,[('1.7',H,'soil compaction measure','high')]),
'2.5':(1,[('2.3',E,'quadrat counts to average','high')]),
'2.6':(1,[('bio2-s2.5.2',H,'repeats and means','high')]),
'2.7':(2,[('bio32-s2.8.0',E,'belt transect','high')]),
'3.0':(1,[('bio2-s2.7.0',H,'risk assessment','low')]),
'3.1':(1,[('bio2-s2.9.5',H,'avoid damaging habitats','high')]),
'4.0':(1,[('2.5',H,'mean and range','high')]),
'4.1':(1,[('2.5',H,'mean and range','high')]),
'4.2':(1,[('bio32-s2.12.1',H,'bar charts compare groups','low')]),
'4.3':(1,[('4.2',E,'bar chart described','high')]),
'5.0':(1,[('1.1',H,'hypothesis tested','low')]),
'5.1':(2,[('5.0',H,'path species pattern','high')]),
'5.2':(2,[('5.0',H,'fewer species on path','high')]),
'5.3':(1,[('5.2',E,'trampling effects','high'),('0.5',H,'richness and evenness','high')]),
'5.4':(2,[('4.0',E,'untrampled results','high'),('4.1',E,'path results','high'),('1.1',H,'hypothesis','high')]),
'5.5':(1,[('1.5',E,'areas alike except trampling','high')]),
'6.1':(1,[('bio2-s2.0.1',H,'independent variable','high'),('8.0',E,'indicator species','high')]),
'6.2':(1,[('bio2-s2.0.3',E,'controlled variables','high'),('7.1',H,'kick-sampling','high')]),
'7.5':(1,[('bio2-s2.5.2',H,'repeats','high')]),
'7.6':(1,[('bio2-s2.9.2',H,'return wild organisms','high')]),
'7.7':(1,[('bio2-s2.7.0',H,'risk assessment','low')]),
'8.1':(1,[('8.0',E,'indicator species','high')]),
'8.2':(1,[('8.0',E,'indicator species','high')]),
'8.3':(1,[('8.0',E,'indicator species','high')]),
'8.4':(2,[('8.1',E,'sensitive species upstream','high'),('8.3',E,'tolerant species downstream','high')]),
'8.5':(2,[('8.4',H,'downstream results explained','high')]),
'8.6':(2,[('8.5',E,'oxygen depletion','high'),('8.3',H,'tolerant species','high')]),
'9.b':(1,[('0.3',H,'primary vs secondary data','high')]),
'9.1':(1,[('8.0',E,'indicator species','high'),('9.0',E,'Q-value','high')]),
'9.2':(1,[('9.0',E,'Q-value','high'),('0.3',H,'primary vs secondary','high')]),
'10.0':(2,[('bio2-s2.5.0',E,'reliability','high'),('bio2-s2.5.4',H,'sample size','high')]),
'10.1':(1,[('bio2-s2.3.0',E,'validity','high')]),
'10.2':(1,[('10.1',E,'confounding variables','high')]),
'10.3':(1,[('bio32-s2.1.1',H,'random sampling','high')]),
'10.4':(1,[('bio32-s2.5.7',H,'subjective cover estimates','high')]),
'11.0':(2,[('5.2',H,'soil compaction mechanism','high'),('8.5',H,'oxygen depletion mechanism','high')]),
'11.1':(2,[('0.3',E,'secondary data','high')]),
'11.2':(1,[('10.0',H,'sample size reliability','high')]),
'11.3':(1,[('10.2',H,'abiotic confounders','high')]),
'11.4':(1,[('0.6',E,'Simpson index','high')]),
'12.0':(1,[('7.1',H,'kick-sampling','high')]),
'12.1':(1,[('12.0',E,'kick sample data','high')]),
'12.2':(1,[('12.0',E,'kick sample data','high')]),
'12.3':(2,[('12.1',E,'upstream data','high'),('12.2',E,'downstream data','high'),('8.5',H,'low oxygen cause','low')]),
'12.4':(1,[('12.2',E,'downstream data','high')]),
}
out={}
for i in tids:
    k=i[len(S):]
    c,n=D.get(k,(1,[]))
    out[i]={'cost':c,'needs':[{'id':(x if x.startswith('bio') else S+x),'strength':s,'why':w,'confidence':f} for x,s,w,f in n]}
json.dump(out,open(P+'point-links/bio31-s3.json','w'),indent=1)
o=json.load(open(P+'point-links/bio31-s3.json'))
assert list(o)==tids and len(set(tids))==len(tids)
ls=[n for v in o.values() for n in v['needs']]
for i,v in o.items():
    for n in v['needs']: assert n['id'] in allids and n['id']!=i,(i,n)
print(len(o),len(ls),sum(v['cost']==2 for v in o.values()),sum(n['confidence']=='low' for n in ls))
