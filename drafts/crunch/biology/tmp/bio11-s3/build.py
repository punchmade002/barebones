import json,re
P='/Users/gabrielwhelan/barebones/drafts/crunch/biology/'
E,H='essential','helpful'
# id: (cost, [(need, strength, why, conf)])
D={
'0.b':(1,[]),
'0.0':(1,[('bio11-s2.0.4',H,'chromosomes carry genes','high')]),
'0.1':(1,[('bio7-s3.4.2',H,'DNA copied before division','low')]),
'0.2':(2,[('bio11-s2.0.4',E,'homologous pairs','high'),('bio11-s2.2.0',E,'alleles','high'),('bio23-s3.0.1',H,'meiosis halves chromosome number','high')]),
'0.3':(1,[('bio11-s2.1.4',E,'fertilisation and zygote','high')]),
'0.4':(1,[('bio11-s2.1.5',H,'zygote divides by mitosis','high')]),
'0.5':(1,[('bio11-s2.2.2',E,'two alleles per autosomal gene','high')]),
'0.6':(1,[('bio11-s3.0.5',E,'both parents contribute equally','high'),('bio11-s2.6.4',H,'sex-linked exception','low')]),
'0.7':(2,[('bio11-s3.0.2',E,'one allele per gamete','high')]),
'1.b':(1,[]),
'1.0':(1,[('bio7-s3.2.0',H,'mitochondria','high'),('bio7-s3.3.0',H,'chloroplasts','high')]),
'1.1':(2,[('bio7-s3.6.0',H,'ribosome structure','low'),('bio7-s3.4.0',H,'histones and chromatin','high')]),
'1.2':(1,[('bio11-s3.1.1',E,'organelle DNA copies','high'),('bio11-s2.2.2',H,'two copies of nuclear gene','high')]),
'1.3':(2,[('bio7-s3.2.2',H,'aerobic respiration','high'),('bio7-s3.3.2',H,'photosynthesis','high'),('bio7-s3.6.0',H,'rRNA in ribosomes','low')]),
'1.4':(1,[('bio11-s3.1.3',H,'organelle genes code some proteins','high')]),
'1.5':(2,[('bio11-s3.1.1',E,'circular DNA and 70S ribosomes','high')]),
'1.6':(1,[('bio11-s3.1.0',H,'organelle DNA','low')]),
'2.b':(1,[]),
'2.0':(2,[('bio7-s3.1.0',H,'cytoplasm','high'),('bio11-s3.1.6',H,'organelles come from existing ones','low')]),
'2.1':(1,[('bio11-s3.2.0',E,'random sharing of organelles','high')]),
'2.2':(2,[('bio23-s3.8.4',H,'sperm mitochondria stay out','high'),('bio23-s3.5.1',H,'egg cytoplasm and mitochondria','high')]),
'2.3':(1,[('bio11-s3.2.2',E,'egg supplies mitochondria','high')]),
'2.4':(1,[('bio11-s3.2.3',E,'maternal inheritance','high')]),
'2.5':(1,[('bio11-s3.2.3',E,'maternal inheritance','high'),('bio11-s3.0.6',H,'reciprocal crosses for nuclear genes','high')]),
'2.6':(1,[('bio11-s3.2.3',E,'maternal inheritance','high')]),
'3.b':(1,[]),
'3.0':(2,[('bio7-s3.3.0',H,'chloroplasts','high'),('bio11-s3.2.3',H,'chloroplasts inherited from female','low')]),
'3.1':(1,[('bio11-s3.3.0',E,'white and green branches','high')]),
'3.2':(1,[('bio11-s3.3.1',H,'seed colour follows female branch','low')]),
'3.3':(2,[('bio11-s3.2.3',E,'maternal inheritance of chloroplasts','high')]),
'4.b':(1,[]),
'4.0':(1,[('bio11-s3.1.0',H,'organelle DNA','low')]),
'4.1':(2,[('bio7-s3.2.2',E,'aerobic respiration','high')]),
'4.2':(2,[('bio11-s3.2.3',E,'maternal inheritance','high')]),
'4.3':(2,[('bio11-s3.1.2',H,'many copies of organelle DNA','high')]),
'4.4':(2,[('bio11-s3.4.1',H,'mitochondrial disease','high')]),
'4.5':(1,[('bio11-s3.4.4',E,'mitochondrial donation','high')]),
'4.6':(1,[('bio11-s3.2.6',E,'DNA passes down female line unmixed','high')]),
'4.7':(1,[('bio11-s3.1.2',E,'many copies per cell','high')]),
'5.b':(1,[]),
'5.0':(1,[('bio11-s3.0.0',H,'nuclear genes on chromosomes','high'),('bio11-s3.1.0',H,'non-nuclear DNA','high')]),
'5.1':(1,[('bio11-s3.1.1',H,'circular DNA without histones','high')]),
'5.2':(1,[('bio11-s3.4.0',H,'37 mitochondrial genes','high')]),
'5.3':(1,[('bio11-s3.1.2',H,'many organelle DNA copies','high'),('bio11-s2.1.4',H,'diploid','low')]),
'5.4':(1,[('bio11-s3.2.3',H,'maternal inheritance','high')]),
'5.5':(2,[('bio11-s3.2.0',E,'organelles shared randomly','high')]),
'5.6':(2,[('bio11-s3.0.7',E,'Mendelian ratios','high'),('bio11-s3.2.5',E,'reciprocal crosses differ','high')]),
'5.7':(1,[('bio11-s3.0.7',H,'new allele combinations','high'),('bio11-s3.2.6',H,'changes only by mutation','high')]),
'6.b':(1,[]),
'6.0':(1,[]),
'6.1':(1,[('bio11-s3.0.1',H,'DNA copied before division','low')]),
'6.2':(1,[('bio11-s3.4.1',H,'LHON example','high')]),
'6.3':(2,[('bio11-s3.2.2',E,'egg gives mitochondria, sperm does not','high'),('bio23-s3.8.4',H,'sperm entry leaves mitochondria out','low')]),
}
out={}
for k,(c,n) in D.items():
    out['bio11-s3.'+k]={'cost':c,'needs':[{'id':i,'strength':s,'why':w,'confidence':f} for i,s,w,f in n]}
json.dump(out,open(P+'point-links/bio11-s3.json','w'),indent=1)
# validate
txt=open(P+'points/bio11-s3.txt').read()
ids=re.findall(r'^\[([^\]]+)\]',txt,re.M)
tgt=[i for i in ids if i.startswith('bio11-s3.')]
d=json.load(open(P+'point-links/bio11-s3.json'))
assert list(d)==tgt,(set(tgt)^set(d))
for v in d.values():
    for n in v['needs']: assert n['id'] in ids,n
print(len(d),sum(len(v['needs']) for v in d.values()),sum(v['cost']==2 for v in d.values()),sum(n['confidence']=='low' for v in d.values() for n in v['needs']))
