import json,re
P='/Users/gabrielwhelan/barebones/drafts/crunch/biology/'
txt=open(P+'points/bio23-s4.txt').read()
allids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
tg=[]
for l in txt.split('CANDIDATES')[0].splitlines():
    m=re.match(r'\[([^\]]+)\]',l)
    if m: tg.append(m.group(1))
S='bio23-s4.';B='bio23-s2.';H='bio20-s1.';O='bio21-s2.'
E,h='essential','helpful'
D={
'0.b':(1,[]),
'0.0':(1,[(B+'6.0',h,'ovary location','high')]),
'0.1':(1,[]),'0.2':(1,[]),'0.3':(1,[]),
'0.4':(2,[(B+'6.1',E,'follicles in the ovary','high'),(B+'4.3',h,'endometrium','high')]),
'0.5':(1,[(H+'0.0',h,'hormone definition','high')]),
'0.6':(1,[]),
'1.b':(1,[(S+'0.4',h,'uterine cycle, endometrium','high')]),
'1.0':(1,[(S+'0.3',E,'days counted from day 1','high')]),
'1.1':(1,[(B+'4.5',h,'endometrium shed','high'),(B+'3.0',h,'cervix','low')]),
'1.2':(1,[(S+'1.1',h,'shedding of lining','high')]),
'2.b':(1,[(S+'0.4',h,'ovarian cycle follicles','high')]),
'2.0':(1,[(S+'0.3',h,'day counting','low')]),
'2.1':(1,[(B+'6.1',E,'follicles hold eggs','high')]),
'2.2':(1,[(B+'4.3',E,'endometrium','high')]),
'2.3':(1,[(B+'3.1',h,'cervical mucus','high')]),
'3.b':(1,[]),
'3.0':(1,[(S+'2.1',E,'Graafian follicle','high'),(B+'5.1',h,'funnel sweeps egg','low')]),
'3.1':(1,[(S+'3.0',h,'egg released','high')]),
'4.b':(1,[]),
'4.0':(1,[(S+'3.0',E,'follicle after ovulation','high')]),
'4.1':(1,[(B+'4.3',E,'endometrium','high')]),
'4.2':(2,[(S+'4.0',E,'corpus luteum','high'),(S+'1.1',h,'endometrium shed','low')]),
'4.3':(1,[(S+'4.0',E,'corpus luteum','high')]),
'5.b':(1,[]),
'5.0':(2,[(S+'4.0',E,'luteal phase length','high'),(S+'3.0',h,'ovulation','low')]),
'5.1':(1,[(S+'5.0',E,'fixed luteal phase','high')]),
'5.2':(2,[(S+'5.0',E,'14-day gap before period','high')]),
'6.b':(1,[]),
'6.0':(1,[(S+'1.0',h,'menstruation phase','high')]),
'6.1':(2,[(S+'2.0',h,'follicular phase','high')]),
'6.2':(1,[(S+'3.0',h,'ovulation','high')]),
'6.3':(2,[(S+'4.0',h,'luteal phase','high')]),
'7.b':(1,[]),
'7.0':(2,[(S+'6.3',h,'phase summary','low')]),
'8.b':(1,[]),
'8.0':(2,[(H+'1.b',h,'pituitary gland location','low')]),
'9.b':(1,[(S+'8.0',E,'which organ makes hormones','high')]),
'9.0':(1,[(S+'4.2',h,'corpus luteum breakdown','high')]),
'9.1':(2,[(S+'9.0',E,'low progesterone','high')]),
'9.2':(1,[(S+'9.1',E,'progesterone fall','high')]),
'9.3':(2,[(H+'2.0',E,'FSH stimulates follicle','high')]),
'9.4':(1,[(H+'8.2',h,'oestrogen thickens endometrium','high')]),
'9.5':(2,[(S+'9.3',E,'rising oestrogen','high'),(O+'2.0',h,'negative feedback','high')]),
'10.b':(1,[]),
'10.0':(2,[(S+'9.3',E,'oestrogen rises','high')]),
'10.1':(1,[(S+'10.0',E,'LH surge','high'),(S+'3.0',h,'ovulation','low')]),
'10.2':(1,[(S+'10.1',h,'after ovulation','low')]),
'11.b':(1,[(S+'4.0',h,'corpus luteum','high')]),
'11.0':(1,[(H+'2.1',E,'LH forms corpus luteum','high')]),
'11.1':(1,[(S+'11.0',E,'corpus luteum formed','high')]),
'11.2':(1,[(S+'11.1',E,'progesterone secretion','high')]),
'11.3':(2,[(S+'11.1',E,'high progesterone','high'),(O+'2.0',h,'inhibition feedback','high')]),
'11.4':(2,[(S+'11.3',E,'low LH','high'),(S+'4.2',h,'corpus luteum breaks down','high')]),
'11.5':(2,[(S+'11.4',E,'falling progesterone','high'),(S+'9.2',h,'FSH rises','high')]),
'11.6':(1,[(S+'4.3',E,'implantation keeps corpus luteum','high')]),
'12.b':(1,[]),
'12.0':(1,[(S+'9.2',h,'FSH rising','low')]),
'12.1':(2,[(S+'9.3',h,'follicular hormones','high')]),
'12.2':(2,[(S+'10.0',E,'LH surge','high')]),
'12.3':(2,[(S+'11.1',E,'luteal hormones','high')]),
'13.b':(1,[]),
'13.0':(1,[(O+'2.0',h,'negative feedback','high')]),
'13.1':(2,[(O+'2.0',E,'negative feedback','high'),(S+'11.3',h,'luteal inhibition','high')]),
'13.2':(2,[(S+'10.0',E,'oestrogen triggers LH surge','high'),(O+'3.0',h,'positive feedback','high')]),
'13.3':(2,[(S+'13.1',h,'feedback chain','high')]),
'13.4':(1,[(S+'10.1',E,'LH surge','high')]),
'13.5':(2,[(S+'13.1',E,'negative feedback','high')]),
'13.6':(2,[(S+'13.3',E,'hormone sequence','high')]),
'14.b':(1,[]),
'14.0':(2,[(S+'12.1',h,'FSH levels','low')]),
'14.1':(1,[(S+'10.1',h,'LH surge','high')]),
'14.2':(2,[(S+'10.0',h,'oestrogen peak','high')]),
'14.3':(1,[(S+'11.1',h,'progesterone rise','high')]),
'14.4':(1,[(S+'11.1',E,'corpus luteum secretes progesterone','high')]),
'14.5':(2,[(S+'14.2',h,'graph curves','low')]),
}
out={}
for t in tg:
    c,n=D[t.replace(S,'')]
    out[t]={'cost':c,'needs':[{'id':i,'strength':s,'why':w,'confidence':f} for i,s,w,f in n]}
assert list(out)==tg and len(D)==len(tg)
for v in out.values():
    for n in v['needs']: assert n['id'] in allids,n
json.dump(out,open(P+'point-links/bio23-s4.json','w'),indent=1)
L=[n for v in out.values() for n in v['needs']]
print(len(out),len(L),sum(v['cost']==2 for v in out.values()),sum(n['confidence']=='low' for n in L))
