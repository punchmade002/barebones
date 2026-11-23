import json,re
P='bio35-s1.'
# id: (cost, [(need,strength,why,conf)])
E,H='essential','helpful'
S={
'0.b':(1,[]),
'0.0':(1,[('bio10-s1.4.0',H,'DNA holds genes','high')]),
'0.1':(1,[('0.0',E,'genetic modification defined','high')]),
'0.2':(1,[]),
'1.b':(1,[]),
'1.0':(2,[('bio17-s2.1.1',H,'codons specify amino acids','low')]),
'1.1':(2,[('bio17-s2.2.b',H,'transcription','high'),('bio17-s2.4.b',H,'translation','high')]),
'1.2':(1,[]),
'1.3':(1,[('1.2',E,'contrast with selective breeding','high')]),
'1.4':(2,[]),
'1.5':(1,[('3.0',H,'restriction enzymes cut DNA','high')]),
'2.b':(1,[]),
'2.0':(1,[]),
'2.1':(1,[('bio10-s1.2.0',H,'double-stranded DNA','low')]),
'2.2':(1,[('2.1',E,'plasmid defined','high')]),
'2.3':(1,[('2.1',E,'plasmid carries marker','high')]),
'2.4':(2,[('2.0',E,'vector defined','high')]),
'2.5':(1,[('2.1',H,'Ti plasmid','high')]),
'2.6':(1,[('2.0',H,'vector-free contrast','low')]),
'3.b':(1,[]),
'3.0':(1,[('bio10-s1.0.6',H,'base sequence','high')]),
'3.1':(1,[('3.0',E,'restriction enzymes','high')]),
'3.2':(2,[('3.0',E,'how enzymes cut','high')]),
'3.3':(2,[('3.2',E,'sticky ends','high'),('bio10-s1.2.1',H,'base pairing','low')]),
'3.4':(1,[('3.2',E,'sticky ends','high'),('bio10-s1.2.1',E,'complementary base pairing','high')]),
'3.5':(1,[('3.3',E,'EcoRI cut','high')]),
'4.b':(1,[]),
'4.0':(2,[('3.2',E,'sticky ends','high'),('bio10-s1.1.1',E,'sugar-phosphate backbone','high')]),
'4.1':(1,[('4.0',E,'DNA ligase','high'),('bio10-s1.2.3',H,'hydrogen bonds between bases','high')]),
'5.b':(1,[]),
'5.0':(1,[('2.1',H,'plasmid','high')]),
'5.1':(1,[('3.0',E,'restriction enzyme','high')]),
'5.2':(1,[('3.2',E,'sticky ends','high')]),
'5.3':(2,[('4.0',E,'DNA ligase','high')]),
'6.b':(1,[]),
'6.0':(1,[('5.3',H,'recombinant plasmid','high')]),
'6.1':(1,[]),
'6.2':(2,[('2.3',E,'marker gene','high')]),
'6.3':(1,[('bio33-s1.5.0',H,'binary fission','high')]),
'6.4':(1,[('1.1',E,'gene must be expressed','high')]),
'6.5':(1,[]),
'6.6':(2,[('5.3',H,'recombinant plasmid steps','high')]),
'6.7':(1,[('6.6',E,'flow chart being labelled','high')]),
'7.b':(1,[]),
'7.0':(1,[('6.4',H,'expression of inserted gene','high')]),
'7.1':(1,[]),
'7.2':(2,[('7.0',E,'GM insulin','high')]),
'7.3':(1,[('7.0',H,'engineered cells make hormone','low')]),
'7.4':(2,[]),
'7.5':(1,[('7.0',H,'yeast makes protein','low')]),
'7.6':(1,[]),
'8.b':(1,[]),
'8.0':(2,[('0.1',H,'transgenic organism','high')]),
'8.1':(1,[('8.0',E,'Bt toxin crop','high')]),
'8.2':(1,[]),
'8.3':(2,[]),
'8.4':(1,[('8.3',E,'Golden Rice','high')]),
'8.5':(1,[('8.0',H,'Bt maize','high')]),
'8.6':(1,[]),
'9.b':(1,[]),
'9.0':(1,[]),
'9.1':(1,[('9.0',E,'AquAdvantage salmon','high')]),
'9.2':(1,[]),
'9.3':(2,[('2.4',E,'viral vector','high')]),
'9.4':(1,[('9.3',E,'gene therapy','high')]),
'9.5':(1,[('9.4',H,'somatic contrast','high')]),
'10.b':(1,[]),
'10.0':(1,[]),
'10.1':(2,[('bio10-s1.2.1',H,'complementary base pairing','high')]),
'10.2':(1,[('10.1',E,'Cas9 cut','high')]),
'10.3':(1,[('10.1',E,'CRISPR mechanism','high')]),
'10.4':(1,[]),
'10.5':(1,[('10.0',H,'CRISPR treatment','high')]),
'11.b':(1,[]),
'11.0':(1,[('7.0',H,'insulin medicine example','high')]),
'11.1':(1,[('8.0',H,'Bt crops','high')]),
'11.2':(1,[]),
}
txt=open('points/bio35-s1.txt').read()
ids=re.findall(r'^\[([^\]]+)\]',txt.split('CANDIDATES')[0],re.M)
allids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
f=lambda k:k if k.startswith('bio') else P+k
out={}
for i in ids:
    c,n=S[i[len(P):]]
    out[i]={'cost':c,'needs':[{'id':f(a),'strength':s,'why':w,'confidence':q} for a,s,w,q in n]}
assert list(out)==ids and len(S)==len(ids)
for i,v in out.items():
    for n in v['needs']: assert n['id'] in allids and n['id']!=i,(i,n)
json.dump(out,open('point-links/bio35-s1.json','w'),ensure_ascii=False)
d=json.load(open('point-links/bio35-s1.json'))
nn=[n for v in d.values() for n in v['needs']]
print(len(d),len(nn),sum(v['cost']==2 for v in d.values()),sum(n['confidence']=='low' for n in nn))
