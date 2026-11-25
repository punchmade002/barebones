import json,re
P='bio16-s4.'
E,H='essential','helpful'
def n(i,s,w,c='high'):return (i,s,w,c)
d={
'0.b':(1,[]),'0.0':(1,[]),
'0.1':(1,[n(P+'0.0',H,'cancer cells lose division control')]),
'0.2':(1,[]),'0.3':(1,[]),'0.4':(1,[]),'0.5':(1,[]),
'0.6':(1,[n('bio17-s3.0.0',H,'mutation as DNA change')]),
'1.b':(1,[]),'1.0':(1,[]),
'1.1':(1,[n('bio16-s1.2.2',E,'checkpoints in the cell cycle')]),
'1.2':(2,[n(P+'1.0',H,'growth factor signals to divide')]),
'1.3':(2,[n(P+'1.1',E,'checkpoints that stop the cycle')]),
'1.4':(1,[]),
'1.5':(2,[n(P+'1.3',E,'tumour suppressor genes stop cycle')]),
'1.6':(1,[n(P+'1.5',E,'p53 protein and TP53 gene')]),
'1.7':(1,[]),
'1.8':(2,[n('bio16-s1.0.0',H,'chromosome structure','low')]),
'2.b':(1,[n(P+'1.2',H,'accelerator and brakes genes')]),
'2.0':(2,[n(P+'1.2',E,'proto-oncogenes stimulate cell cycle')]),
'2.1':(2,[n(P+'1.3',E,'tumour suppressor genes act as brakes')]),
'2.2':(2,[n(P+'2.1',E,'inactivated tumour suppressor gene')]),
'2.3':(1,[]),
'2.4':(1,[n(P+'2.3',E,'mutations build up over time')]),
'2.5':(2,[n(P+'0.6',H,'cancer cells descended from one cell')]),
'2.6':(1,[]),
'3.b':(1,[]),
'3.0':(1,[n(P+'1.0',E,'normal division needs signals')]),
'3.1':(2,[n(P+'1.4',E,'apoptosis'),n(P+'1.8',E,'telomere shortening limits division')]),
'3.2':(1,[n(P+'1.7',E,'contact inhibition in normal cells')]),
'3.3':(1,[]),'3.4':(2,[]),'3.5':(1,[]),'3.6':(1,[]),
'3.7':(1,[n(P+'3.1',H,'immortal cancer cells')]),
'3.8':(1,[n(P+'3.7',E,'HeLa cells')]),
'4.b':(1,[]),
'4.0':(1,[n(P+'0.0',H,'uncontrolled division')]),
'4.1':(1,[n(P+'4.0',H,'tumour definition')]),
'4.2':(1,[n(P+'4.1',H,'benign tumour features')]),
'4.3':(1,[n(P+'4.1',H,'contrast with benign tumour','low')]),
'4.4':(2,[n(P+'4.1',E,'benign tumour features'),n(P+'4.3',E,'malignant tumour features')]),
'4.5':(1,[n(P+'4.3',E,'malignant tumour is cancer')]),
'5.b':(1,[]),
'5.0':(1,[n(P+'0.6',H,'cancer arises from one mutated cell')]),
'5.1':(1,[n(P+'5.0',E,'clone of abnormal cells')]),
'5.2':(1,[]),
'5.3':(1,[n(P+'0.1',H,'cancer cells invade tissues')]),
'5.4':(1,[n(P+'5.3',H,'invasion precedes spread')]),
'5.5':(1,[n(P+'5.4',E,'cells carried in vessels')]),
'5.6':(2,[n(P+'5.5',E,'steps ending in metastasis')]),
'6.b':(1,[]),
'6.0':(1,[n(P+'5.5',E,'secondary tumours')]),
'6.1':(1,[n(P+'6.0',E,'metastasis')]),
'6.2':(1,[n(P+'6.0',E,'metastasis')]),
'6.3':(1,[]),
'6.4':(1,[n(P+'0.5',H,'leukaemia starts in bone marrow')]),
'6.5':(1,[]),
}
out={}
for k,(c,ns) in d.items():
    out[P+'s4.'+k if False else 'bio16-s4.'+k]={"cost":c,"needs":[{"id":i,"strength":s,"why":w,"confidence":cf} for i,s,w,cf in ns]}
json.dump(out,open('/Users/gabrielwhelan/barebones/drafts/crunch/biology/point-links/bio16-s4.json','w'),indent=1)
pkg=open('/Users/gabrielwhelan/barebones/drafts/crunch/biology/points/bio16-s4.txt').read()
ids=re.findall(r'^\[([^\]]+)\]',pkg,re.M)
tg=[i for i in ids if i.startswith('bio16-s4.')]
assert list(out)==tg,(set(tg)^set(out))
assert all(x['id'] in ids and x['id']!=k for k,v in out.items() for x in v['needs'])
print(len(out),sum(len(v['needs']) for v in out.values()),sum(v['cost']==2 for v in out.values()),sum(x['confidence']=='low' for v in out.values() for x in v['needs']))
