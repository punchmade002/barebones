import json,re
P='bio23-s1.'
# id suffix: (cost, [(target,strength,why,conf)])
E,H='essential','helpful'
d={
'0.b':(1,[]),'0.0':(1,[]),
'0.1':(2,[('4.5',H,'seminal fluid from glands','low')]),
'0.2':(1,[]),
'0.3':(1,[('0.2',E,'seminal fluid','high')]),
'0.4':(1,[('0.2',E,'semen and seminal fluid','high')]),
'1.b':(1,[]),
'1.0':(1,[('2.0',H,'testes','low')]),
'1.1':(1,[('1.0',E,'scrotum','high')]),
'2.b':(1,[]),'2.0':(1,[]),
'2.1':(2,[('2.0',H,'testis','high')]),
'2.2':(1,[('2.1',E,'coiled seminiferous tubules','high')]),
'2.3':(2,[('2.1',H,'seminiferous tubules','low'),('bio20-s1.0.1',E,'endocrine glands release into blood','high')]),
'2.4':(1,[('2.3',H,'testosterone from interstitial cells','low')]),
'2.5':(1,[('1.0',E,'scrotum','high')]),
'2.6':(1,[('2.5',E,'testis descent','high')]),
'3.b':(1,[]),
'3.0':(1,[('2.0',H,'testis','low')]),
'3.1':(1,[('3.0',E,'epididymis','high')]),
'3.2':(1,[('3.0',H,'epididymis','high')]),
'3.3':(1,[('3.2',E,'vas deferens','high')]),
'3.4':(1,[('3.2',E,'vas deferens','high')]),
'3.5':(1,[]),
'3.6':(2,[('3.5',E,'urethra','high')]),
'3.7':(1,[('3.5',H,'urethra','high')]),
'4.b':(1,[]),
'4.0':(1,[('3.2',H,'vasa deferentia','high')]),
'4.1':(2,[('4.0',E,'seminal vesicles','high')]),
'4.2':(1,[('4.1',E,'seminal vesicle fluid','high')]),
'4.3':(1,[('3.5',H,'urethra','high')]),
'4.4':(1,[('4.3',E,'prostate','high')]),
'4.5':(1,[('4.1',E,'seminal vesicle secretion','high'),('4.4',E,'prostate secretion','high')]),
'4.6':(1,[('4.3',E,'prostate position','high')]),
'5.b':(1,[]),
'5.0':(1,[('3.5',H,'urethra','low')]),
'5.1':(2,[('5.0',H,'penis','high')]),
'5.2':(1,[('5.0',E,'penis','high')]),
'5.3':(1,[('5.2',E,'glans','high')]),
'5.4':(1,[('5.2',E,'glans','high')]),
'5.5':(1,[('5.4',E,'foreskin','high')]),
'5.6':(2,[('3.3',H,'peristalsis in vas deferens','low')]),
'5.7':(1,[('0.2',H,'semen','low')]),
'6.b':(1,[]),
'6.0':(2,[('0.1',H,'sperm pathway','low')]),
'7.b':(1,[]),
'7.0':(1,[('1.1',H,'scrotum temperature','high')]),
'7.1':(2,[('2.1',E,'seminiferous tubules and testis','high')]),
'7.2':(1,[('3.1',H,'epididymis','high')]),
'7.3':(1,[('3.3',H,'peristalsis','high')]),
'8.b':(1,[]),
'8.0':(1,[('4.1',H,'seminal vesicle fluid','high')]),
'8.1':(1,[('4.4',H,'prostate fluid','high')]),
'8.2':(1,[('3.6',H,'urethra and sphincter','high')]),
'8.3':(1,[('5.1',H,'erectile tissue','high')]),
'8.4':(1,[('5.2',H,'glans','high')]),
'8.5':(1,[('5.4',H,'foreskin','high')]),
}
out={}
for k,(c,n) in d.items():
    out[P+k]={"cost":c,"needs":[{"id":(t if t.startswith('bio') else P+t),"strength":s,"why":w,"confidence":f} for t,s,w,f in n]}
open('point-links/bio23-s1.json','w').write(json.dumps(out,indent=1))
txt=open('points/bio23-s1.txt').read()
tgt=re.findall(r'^\[(bio23-s1[^\]]*)\]',txt,re.M)
allids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
o=json.load(open('point-links/bio23-s1.json'))
assert list(o)==tgt,(set(tgt)^set(o))
l=[x for v in o.values() for x in v['needs']]
assert all(x['id'] in allids for x in l)
assert all(x['id']!=k for k,v in o.items() for x in v['needs'])
print(len(o),len(l),sum(v['cost']==2 for v in o.values()),sum(x['confidence']=='low' for x in l))
