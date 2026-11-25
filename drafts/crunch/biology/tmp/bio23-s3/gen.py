import json,re
P='bio23-s3.'
txt=open('points/bio23-s3.txt').read()
tgt=txt.split('CANDIDATES')[0]
ids=re.findall(r'^\[([^\]]+)\]',tgt,re.M)
allids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
def L(i,s,w,c='high'):return {"id":i,"strength":s,"why":w,"confidence":c}
E,H='essential','helpful'
c2={'1.1','2.0','2.5','3.0','3.3','4.5','5.1','5.3','7.1','7.5','8.3','9.0','9.4'}
n={
'0.1':[L('bio16-s2.1.0',H,'meiosis halves chromosome number')],
'0.2':[L(P+'0.0',H,'haploid gametes')],
'0.3':[L('bio16-s2.1.0',H,'meiosis')],
'0.4':[L('bio16-s2.0.0',H,'mitosis keeps chromosome number')],
'1.1':[L('bio16-s2.1.0',E,'meiosis after mitosis'),L('bio23-s1.2.1',H,'seminiferous tubule walls make sperm','low')],
'1.2':[L('bio16-s2.1.0',H,'meiosis gives four cells')],
'1.3':[L('bio16-s2.1.1',H,'chromosome pair separation in meiosis','low')],
'1.4':[L('bio23-s1.3.1',H,'epididymis stores and matures sperm')],
'1.6':[L('bio23-s1.1.1',H,'scrotum keeps testes cooler')],
'2.0':[L('bio23-s2.6.1',H,'follicles hold immature eggs')],
'2.1':[L('bio16-s2.1.0',E,'meiosis')],
'2.3':[L(P+'2.0',H,'fixed egg supply at birth')],
'2.4':[L('bio23-s2.6.1',H,'follicle and ovulation')],
'2.5':[L(P+'2.1',E,'meiosis stopped part-way')],
'3.0':[L('bio16-s2.1.0',E,'meiosis gives four cells')],
'3.1':[L(P+'3.0',E,'one egg from meiosis')],
'3.2':[L(P+'3.0',H,'polar bodies leave egg cytoplasm')],
'3.3':[L('bio16-s2.1.1',H,'chromosome separation in meiosis'),L(P+'2.3',H,'eggs formed before birth','low')],
'3.4':[L(P+'3.3',H,'egg ageing and errors')],
'4.1':[L(P+'0.0',H,'haploid nucleus')],
'4.5':[L(P+'4.1',H,'head, acrosome, nucleus')],
'5.1':[L(P+'0.0',H,'haploid nucleus')],
'5.3':[L(P+'5.2',H,'zona pellucida and follicle cells')],
'6.0':[L(P+'4.0',H,'sperm size'),L(P+'5.0',H,'egg size')],
'6.1':[L('bio23-s2.5.2',H,'cilia move egg along tube')],
'6.3':[L(P+'5.1',H,'egg cytoplasm food reserves')],
'6.4':[L(P+'1.3',E,'sperm carry X or Y')],
'6.5':[L(P+'1.2',H,'four sperm per meiosis'),L(P+'3.1',H,'one egg per meiosis')],
'7.0':[L('bio23-s1.0.2',H,'semen')],
'7.1':[L('bio23-s2.3.2',E,'cervical mucus thins at ovulation')],
'7.5':[L(P+'7.3',E,'sperm survival time'),L(P+'7.4',E,'egg survival time')],
'8.0':[L(P+'0.2',H,'haploid gametes fuse to zygote')],
'8.1':[L('bio23-s2.5.3',H,'fertilisation in fallopian tube','low')],
'8.2':[L(P+'5.2',E,'follicle cells around egg')],
'8.3':[L(P+'4.1',E,'acrosome enzymes'),L(P+'5.2',E,'zona pellucida')],
'8.4':[L(P+'4.2',H,'sperm mitochondria in middle piece')],
'8.5':[L(P+'5.2',E,'zona pellucida')],
'8.6':[L(P+'2.5',E,'meiosis completed after sperm entry')],
'8.7':[L(P+'8.0',H,'fusion of nuclei to zygote')],
'9.0':[L(P+'1.3',E,'sperm carry X or Y'),L(P+'5.1',H,'egg always carries X')],
'9.1':[L(P+'0.2',E,'zygote diploid, gametes haploid')],
'9.2':[L('bio16-s2.1.5',H,'meiosis and random fertilisation variation')],
'9.3':[L('bio16-s2.0.0',H,'zygote divides by mitosis')],
'9.4':[L(P+'8.3',H,'acrosome digests zona pellucida')],
'10.0':[L(P+'8.0',H,'zygote')],
'10.1':[L(P+'8.0',H,'fertilisation of eggs')],
}
out={i:{"cost":2 if i[len(P):] in c2 else 1,"needs":n.get(i[len(P):],[])} for i in ids}
for v in out.values():
    for x in v['needs']:assert x['id'] in allids,x
for i,v in out.items():
    for x in v['needs']:assert x['id']!=i
json.dump(out,open('point-links/bio23-s3.json','w'),indent=1)
d=json.load(open('point-links/bio23-s3.json'))
nl=sum(len(v['needs']) for v in d.values())
print(len(d),len(ids),nl,sum(v['cost']==2 for v in d.values()),sum(x['confidence']=='low' for v in d.values() for x in v['needs']))
