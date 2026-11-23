import json,re
P='bio35-s4.'
H,E='helpful','essential'
d={ # id:(cost,[(need,strength,why,conf)])
'0.b':(1,[]),
'0.0':(1,[('bio10-s1.0.4',H,'the four bases','high')]),
'0.1':(1,[('bio35-s3.10.1',H,'bands separated by fragment length','high')]),
'0.2':(1,[('bio10-s1.2.1',H,'base pairs','low')]),
'0.3':(1,[(P+'0.0',H,'what a sequence is','high')]),
'0.4':(1,[]),
'1.b':(1,[]),'1.0':(1,[]),'1.1':(1,[]),
'1.2':(1,[('bio35-s3.4.0',H,'PCR copies DNA','high')]),
'1.3':(1,[('bio35-s3.4.3',H,'primers','high')]),
'1.4':(1,[('bio10-s1.0.0',H,'nucleotides','high')]),
'1.5':(2,[('bio10-s1.1.0',E,'nucleotides join sugar to phosphate','high')]),
'1.6':(2,[('bio17-s1.1.2',E,'polymerase builds complementary strand','high')]),
'1.7':(1,[(P+'1.6',E,'random chain termination','high')]),
'1.8':(2,[(P+'1.7',E,'fragments of every length','high')]),
'2.b':(1,[]),
'2.0':(2,[(P+'1.5',E,'terminator nucleotides','high')]),
'2.1':(1,[(P+'2.0',H,'identifying terminators','high')]),
'2.2':(2,[('bio35-s3.10.1',E,'gel electrophoresis separates by size','high')]),
'2.3':(2,[(P+'2.2',E,'shortest fragments move furthest','high')]),
'2.4':(1,[('bio10-s1.2.6',E,'complementary strands','high')]),
'2.5':(2,[(P+'2.3',H,'reading gel bottom to top','high')]),
'3.b':(1,[]),
'3.0':(1,[(P+'2.3',E,'shortest fragment first','high')]),
'3.1':(1,[(P+'3.0',H,'first band step','high')]),
'3.2':(1,[]),
'3.3':(1,[('bio10-s1.2.1',E,'A-T and C-G pairing','high')]),
'4.b':(1,[]),
'4.0':(1,[(P+'3.0',H,'reading bands from bottom','high')]),
'4.1':(1,[(P+'3.3',E,'finding template by complement','high')]),
'4.2':(1,[(P+'4.0',E,'lane order of bands','high')]),
'4.3':(2,[(P+'1.3',H,'primer start of strand','high')]),
'4.4':(1,[(P+'2.1',E,'fluorescent dye terminators','high')]),
'5.b':(1,[]),
'5.0':(2,[(P+'0.0',H,'what a sequence is','high')]),
'5.1':(1,[(P+'5.0',H,'next-generation methods','high')]),
'5.2':(1,[]),
'6.b':(1,[]),
'6.0':(1,[('bio17-s1.1.4',H,'point mutation','high')]),
'6.1':(1,[(P+'6.0',H,'finding base changes','low')]),
'6.2':(1,[]),'6.3':(1,[]),
}
out={P+k:{"cost":c,"needs":[{"id":i,"strength":s,"why":w,"confidence":f} for i,s,w,f in n]} for k,(c,n) in d.items()}
json.dump(out,open('point-links/bio35-s4.json','w'),indent=1)
pk=open('points/bio35-s4.txt').read()
ids=re.findall(r'^\[([^\]]+)\]',pk,re.M)
tg=[i for i in ids if i.startswith(P)]
assert list(out)==tg,(set(tg)^set(out))
assert all(n['id'] in ids and n['id']!=k for k,v in out.items() for n in v['needs'])
L=[n for v in out.values() for n in v['needs']]
print(len(out),len(L),sum(v['cost']==2 for v in out.values()),sum(n['confidence']=='low' for n in L))
