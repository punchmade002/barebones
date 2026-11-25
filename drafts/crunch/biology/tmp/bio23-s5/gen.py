import json,re
P='/Users/gabrielwhelan/barebones/drafts/crunch/biology/'
txt=open(P+'points/bio23-s5.txt').read()
allids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
tgt=[]
for l in txt.split('\n'):
    if l.startswith('CANDIDATES'):break
    m=re.match(r'\[([^\]]+)\]',l)
    if m:tgt.append(m.group(1))
E,H='essential','helpful'
# id:(cost,[(need,strength,why,conf)])
d={
'0.0':(1,[('bio23-s3.8.0',H,'zygote from fertilisation','high')]),
'0.1':(1,[('bio23-s5.0.0',H,'zygote as starting cell','high')]),
'0.2':(1,[('bio23-s5.0.1',E,'repeated division of the ball','high')]),
'0.3':(1,[('bio23-s5.0.1',H,'journey along the tube','high')]),
'0.4':(2,[('bio23-s4.0.1',H,'endometrium as uterus lining','high')]),
'1.0':(1,[('bio23-s4.11.2',E,'progesterone maintains endometrium','high')]),
'1.1':(2,[('bio23-s4.11.6',E,'embryo hormone keeps corpus luteum','high')]),
'1.2':(1,[('bio23-s5.1.1',E,'embryo hormone hCG','high')]),
'1.3':(1,[('bio23-s5.0.4',H,'implantation in uterus','high')]),
'2.0':(1,[('bio23-s5.0.4',H,'implantation into endometrium','high')]),
'2.1':(1,[('bio23-s5.2.0',E,'villi','high')]),
'2.2':(1,[('bio23-s5.2.1',E,'placenta structure','high')]),
'2.3':(1,[]),
'3.0':(1,[('bio23-s5.2.1',H,'placenta','high')]),
'3.1':(2,[('bio23-s5.3.0',E,'umbilical cord','high')]),
'3.2':(1,[('bio23-s5.3.0',E,'umbilical cord','high')]),
'3.3':(2,[('bio23-s5.3.2',E,'vein carries oxygenated blood','high')]),
'4.0':(1,[('bio23-s5.2.1',H,'villi and placenta','high')]),
'4.1':(2,[('bio23-s5.4.0',E,'barrier between bloods','high')]),
'4.2':(2,[('bio25-s1.1.6',E,'factors affecting diffusion rate','high')]),
'4.3':(2,[('bio25-s1.1.7',H,'steep gradient kept by blood flow','high')]),
'4.4':(2,[('bio25-s1.1.5',E,'facilitated diffusion','high')]),
'5.0':(1,[('bio23-s5.4.4',H,'substances crossing the barrier','low')]),
'5.1':(1,[('bio23-s5.5.0',H,'placenta exchange role','high')]),
'5.2':(2,[]),
'5.3':(1,[('bio23-s4.8.0',H,'progesterone and oestrogen source','high')]),
'5.4':(1,[('bio23-s5.4.1',H,'barrier to blood cells','low')]),
'6.0':(1,[('bio23-s5.5.4',H,'placenta as barrier','low')]),
'6.1':(1,[('bio23-s5.5.0',H,'oxygen supply via placenta','high')]),
'6.2':(1,[]),
'6.3':(2,[]),
'6.4':(1,[]),
'7.0':(1,[]),
'7.1':(1,[('bio23-s5.7.0',E,'amniotic sac','high')]),
'7.2':(1,[('bio23-s5.7.0',H,'amniotic fluid','high')]),
'8.0':(2,[('bio23-s5.2.1',H,'placenta','high'),('bio23-s5.3.1',H,'cord arteries and vein','high'),('bio23-s5.7.0',H,'amnion','high'),('bio23-s5.14.2',H,'mucus plug','low')]),
'9.0':(1,[('bio23-s5.0.1',H,'mitosis of the zygote','high')]),
'9.1':(2,[('bio23-s4.0.3',H,'day 1 of the period','high')]),
'9.2':(1,[('bio23-s5.9.1',H,'length of pregnancy','low')]),
'9.3':(1,[('bio23-s5.9.2',H,'trimesters','low')]),
'9.4':(1,[]),'9.5':(1,[]),'9.6':(1,[]),
'9.7':(1,[('bio23-s5.9.3',H,'organs forming early','high')]),
'10.0':(1,[('bio23-s3.8.0',H,'zygote formed at fertilisation','high')]),
'10.1':(2,[('bio23-s5.10.0',H,'zygote divides','high')]),
'10.2':(1,[('bio23-s5.10.1',E,'morula','high')]),
'10.3':(1,[('bio23-s5.10.1',H,'ball of cells','high')]),
'10.4':(2,[('bio23-s5.10.3',E,'blastocyst','high')]),
'10.5':(2,[('bio23-s5.10.4',E,'trophoblast','high')]),
'10.6':(1,[('bio23-s5.10.4',E,'inner cell mass','high')]),
'10.7':(2,[('bio23-s5.10.1',H,'morula','high'),('bio23-s5.10.4',H,'blastocyst parts','high')]),
'11.0':(1,[('bio23-s5.10.4',E,'inner cell mass','high')]),
'11.1':(2,[('bio23-s5.11.0',E,'germ layers','high')]),
'11.2':(2,[('bio23-s5.11.0',E,'germ layers','high')]),
'11.3':(2,[('bio23-s5.11.0',E,'germ layers','high')]),
'11.4':(1,[('bio23-s5.11.1',H,'layer contents','high')]),
'12.0':(1,[('bio23-s5.0.4',H,'implantation','high')]),
'12.1':(1,[('bio23-s5.12.0',H,'embryo stage','high')]),
'12.2':(1,[('bio23-s5.12.0',E,'embryo stage','high')]),
'12.3':(1,[('bio23-s5.12.2',E,'foetus definition','high')]),
'12.4':(2,[('bio23-s5.10.5',H,'blastocyst implants','high'),('bio23-s5.11.0',H,'germ layers','high')]),
'13.0':(1,[]),'13.1':(1,[]),
'13.2':(2,[('bio23-s4.13.2',H,'positive feedback','high')]),
'14.0':(1,[('bio23-s5.13.0',H,'labour','high')]),
'14.1':(1,[('bio23-s5.14.0',E,'contractions','high')]),
'14.2':(1,[('bio23-s5.7.0',E,'amnion and fluid','high')]),
'14.3':(1,[('bio23-s5.14.1',H,'cervix dilation','low')]),
'15.0':(1,[('bio23-s5.14.1',H,'cervix dilated','high')]),
'15.1':(1,[('bio23-s5.3.0',E,'umbilical cord','high')]),
'15.2':(2,[('bio23-s5.5.0',H,'placenta supplies oxygen','high')]),
'16.0':(1,[('bio23-s5.2.1',E,'placenta','high')]),
'16.1':(1,[('bio23-s5.16.0',E,'placenta detaches','high')]),
'16.2':(1,[('bio23-s5.2.1',H,'placenta position','low')]),
}
out={}
for t in tgt:
    k=t.split('.',1)[1] if t.count('.')>=1 else t
    k=t[len('bio23-s5.'):]
    if k.endswith('.b'):
        out[t]={'cost':1,'needs':[]};continue
    c,n=d[k]
    out[t]={'cost':c,'needs':[{'id':i,'strength':s,'why':w,'confidence':f} for i,s,w,f in n]}
json.dump(out,open(P+'point-links/bio23-s5.json','w'),indent=1)
o=json.load(open(P+'point-links/bio23-s5.json'))
assert list(o)==tgt and len(set(tgt))==len(tgt)
links=[n for v in o.values() for n in v['needs']]
assert all(n['id'] in allids for n in links)
assert all(n['id']!=k for k,v in o.items() for n in v['needs'])
print(len(o),len(links),sum(v['cost']==2 for v in o.values()),sum(n['confidence']=='low' for n in links))
