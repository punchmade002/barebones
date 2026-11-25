import json,re
P='/Users/gabrielwhelan/barebones/drafts/crunch/biology/'
txt=open(P+'points/bio16-s5.txt').read()
tgt=txt.split('CANDIDATES')[0]
tids=re.findall(r'^\[(\S+?)\]',tgt,re.M)
allids=set(re.findall(r'^\[(\S+?)\]',txt,re.M))
S='bio16-s5.'
# id: (cost, [(need,strength,why,conf)])
E,H='essential','helpful'
spec={
'0.0':(1,[('bio16-s4.2.3',H,'several mutations accumulate','low')]),
'0.2':(2,[('bio16-s4.1.2',E,'proto-oncogenes','high'),('bio16-s4.1.3',E,'tumour suppressor genes','high'),('bio17-s3.0.3',H,'mutagens damage DNA','high')]),
'0.4':(1,[(S+'0.1',H,'risk factor','high')]),
'1.0':(2,[('bio16-s4.1.3',E,'tumour suppressor proteins','high'),('bio16-s4.1.5',H,'p53 function','high')]),
'1.1':(1,[(S+'1.0',H,'HPV and cervix infection','high')]),
'1.3':(2,[('bio17-s3.0.2',H,'mutation during replication','low')]),
'1.6':(2,[(S+'1.0',E,'HPV disrupting cell cycle control','high'),(S+'1.3',H,'inflammation and repair division','high')]),
'1.7':(1,[('bio16-s4.2.6',H,'immune system destroys abnormal cells','high')]),
'2.0':(2,[('bio16-s4.1.5',E,'TP53 and p53 protein','high'),(S+'0.2',H,'carcinogen causing mutations','high')]),
'3.0':(2,[('bio17-s3.0.3',H,'UV as a mutagen','high')]),
'3.2':(1,[('bio17-s3.0.3',H,'ionising radiation as mutagen','high')]),
'3.4':(1,[(S+'3.2',H,'ionising radiation damages DNA','low')]),
'4.5':(1,[('bio16-s4.2.4',H,'mutations build up with age','high')]),
'5.0':(1,[('bio17-s3.1.0',E,'somatic mutations not inherited','high')]),
'5.1':(2,[('bio16-s4.2.2',E,'both alleles must be inactivated','high')]),
'5.2':(1,[(S+'5.1',E,'one faulty copy inherited','high')]),
'5.3':(2,[('bio16-s4.1.3',E,'tumour suppressor genes','high')]),
'5.7':(1,[(S+'5.3',H,'BRCA gene testing','high')]),
'6.2':(2,[(S+'2.3',E,'dose-response relationship','high')]),
'6.4':(2,[(S+'4.0',H,'asbestos multiplies risk','high')]),
'6.5':(1,[(S+'5.3',H,'inherited BRCA mutation','high')]),
'6.7':(2,[(S+'2.2',H,'second-hand smoke','low')]),
'7.0':(2,[]),
'8.0':(1,[(S+'2.2',H,'second-hand smoke','high')]),
'8.1':(1,[(S+'3.0',H,'UV causes DNA damage','high')]),
'9.0':(2,[(S+'1.1',E,'HPV types cause cervical cancer','high')]),
'9.1':(1,[(S+'9.0',E,'HPV vaccine','high')]),
'9.2':(1,[(S+'9.0',E,'HPV vaccine','high')]),
'9.3':(1,[(S+'1.3',E,'hepatitis B causes liver cancer','high')]),
'9.4':(1,[(S+'1.3',H,'hepatitis C and liver cancer','high')]),
'9.5':(2,[]),
'10.0':(1,[('bio16-s4.5.5',H,'metastases spread','high')]),
'10.2':(2,[(S+'1.0',H,'high-risk HPV','high')]),
'10.4':(2,[]),
'10.7':(2,[]),
'11.1':(2,[(S+'3.2',H,'ionising radiation damages DNA','high')]),
'11.2':(2,[('bio16-s4.5.5',H,'spread to other sites','low')]),
'11.3':(2,[(S+'11.2',H,'chemotherapy acts on mitosis','high')]),
'11.4':(2,[(S+'11.2',E,'chemotherapy kills dividing cells','high')]),
'11.6':(2,[]),
'12.0':(2,[('bio16-s4.2.0',H,'oncogene mutated protein','low')]),
'12.1':(2,[('bio17-s3.11.2',E,'BCR-ABL fusion gene','high')]),
'12.3':(2,[('bio16-s4.2.6',H,'immune system destroys abnormal cells','high')]),
'12.4':(2,[(S+'12.3',H,'T cells and immunotherapy','high')]),
'12.5':(1,[(S+'12.3',H,'immunotherapy','high')]),
'12.6':(1,[(S+'12.0',H,'targeted drug for mutated gene','high')]),
'12.7':(2,[(S+'12.3',H,'immune system training','low')]),
'13.0':(1,[(S+'10.6',H,'biopsy','high')]),
'13.1':(1,[(S+'13.0',E,'liquid biopsy','high')]),
}
out={}
for i in tids:
    k=i[len(S):]
    c,n=spec.get(k,(1,[]))
    out[i]={'cost':c,'needs':[{'id':a,'strength':b,'why':w,'confidence':f} for a,b,w,f in n]}
for i,v in out.items():
    for n in v['needs']: assert n['id'] in allids and n['id']!=i,(i,n)
assert set(out)==set(tids) and len(tids)==len(set(tids))
json.dump(out,open(P+'point-links/bio16-s5.json','w'),indent=1)
d=json.load(open(P+'point-links/bio16-s5.json'))
print(len(d),sum(len(v['needs']) for v in d.values()),sum(v['cost']==2 for v in d.values()),sum(n['confidence']=='low' for v in d.values() for n in v['needs']))
