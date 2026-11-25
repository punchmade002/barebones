import json,re
D='/Users/gabrielwhelan/barebones/drafts/crunch/biology/'
P='bio17-s1.'
H,E='high','essential'
spec={ # id: (cost, [(target, strength, why, conf)])
'0.b':(1,[]),'0.0':(1,[]),'0.1':(1,[]),'0.2':(1,[]),
'0.3':(1,[('bio10-s1.0.7','helpful','nucleotides carry energy','low')]),
'1.b':(1,[]),
'1.0':(2,[('bio10-s1.2.3','essential','hydrogen bonds between bases','high')]),
'1.1':(1,[('bio10-s1.2.1','essential','complementary base pairing','high')]),
'1.2':(1,[('bio10-s1.1.1','helpful','sugar-phosphate backbone','high')]),
'1.3':(1,[(P+'1.2','helpful','DNA polymerase enzyme','low')]),
'1.4':(1,[(P+'1.2','helpful','DNA polymerase joins nucleotides','high')]),
'1.5':(1,[('bio10-s1.2.5','helpful','double helix shape','high')]),
'1.6':(1,[(P+'1.5','helpful','new DNA molecules identical','low')]),
'1.7':(2,[(P+'1.0','helpful','helicase at replication fork','high'),(P+'1.2','helpful','DNA polymerase adding nucleotides','high')]),
'2.b':(1,[]),
'2.0':(1,[(P+'1.5','helpful','new molecules from template strands','high')]),
'2.1':(1,[('bio10-s1.2.1','helpful','base-pairing model','high')]),
'2.2':(1,[]),'2.3':(1,[]),
'3.b':(1,[]),'3.0':(1,[]),
'3.1':(1,[(P+'3.0','helpful','heavy versus light nitrogen','high')]),
'3.2':(2,[]),
'3.3':(1,[(P+'3.0','essential','all DNA heavy 15N','high')]),
'3.4':(2,[(P+'3.2','essential','density bands in gradient','high'),(P+'2.2','essential','conservative model prediction','high')]),
'3.5':(2,[(P+'3.2','essential','density bands in gradient','high'),(P+'2.3','essential','dispersive model prediction','high')]),
'3.6':(1,[(P+'2.0','essential','semi-conservative model','high')]),
'3.7':(1,[(P+'3.4','helpful','band positions per generation','low')]),
'4.b':(1,[]),
'4.0':(1,[('bio10-s1.2.1','essential','A-T, C-G base pairing','high')]),
'4.1':(1,[('bio10-s1.2.6','essential','complementary strand sequences','high')]),
'4.2':(1,[(P+'2.0','helpful','one old, one new strand','high')]),
'4.3':(1,[(P+'1.1','helpful','free nucleotides pair with template','low')]),
'4.4':(2,[('bio10-s1.3.0','essential','A equals T in DNA','high')]),
'4.5':(2,[('bio10-s1.3.0','essential','C equals G in DNA','high')]),
'5.b':(1,[]),
'5.0':(1,[(P+'2.0','helpful','each replication makes two molecules','low')]),
'5.1':(2,[(P+'5.0','essential','doubling per generation','high'),(P+'2.0','essential','original strands conserved','high')]),
'5.2':(1,[('bio10-s1.2.1','helpful','bases pair only with partners','high')]),
'5.3':(1,[(P+'2.0','helpful','semi-conservation old and new','high')]),
'5.4':(1,[(P+'5.2','helpful','physical model described','low')]),
'5.5':(1,[(P+'1.0','helpful','enzymes in replication','low')]),
'6.b':(1,[]),
'6.0':(2,[('bio10-s1.6.3','helpful','RNA as go-between','high')]),
'6.1':(1,[(P+'6.0','essential','flow of information','high')]),
'6.2':(2,[('bio10-s1.6.4','essential','mRNA carries gene copy','high')]),
'6.3':(1,[(P+'6.2','essential','mRNA made by transcription','high')]),
'6.4':(2,[(P+'6.2','essential','mRNA read at ribosome','high'),('bio10-s1.6.5','helpful','tRNA brings amino acids','high')]),
'6.5':(2,[(P+'6.4','essential','codons read, amino acids joined','high')]),
'6.6':(2,[(P+'6.0','helpful','DNA to mRNA to protein','high')]),
'7.b':(1,[]),
'7.0':(1,[(P+'6.2','helpful','mRNA copy made in nucleus','high')]),
'7.1':(1,[(P+'6.4','helpful','ribosomes read mRNA','high')]),
'7.2':(1,[('bio10-s1.7.4','helpful','RNA broken down after use','high')]),
'7.3':(2,[(P+'6.0','essential','normal DNA to RNA flow','high')]),
'7.4':(1,[(P+'6.0','helpful','direction of information flow','high')]),
}
txt=open(D+'points/bio17-s1.txt').read()
tgt,_,_=txt.partition('\nCANDIDATES')
ids=re.findall(r'^\[([^\]]+)\]',tgt,re.M)
allids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
out={}
for i in ids:
    c,n=spec[i[len(P):]]
    out[i]={"cost":c,"needs":[{"id":t,"strength":s,"why":w,"confidence":f} for t,s,w,f in n]}
assert len(ids)==len(set(ids))==len(spec)
for i,v in out.items():
    for n in v['needs']: assert n['id'] in allids and n['id']!=i,(i,n)
json.dump(out,open(D+'point-links/bio17-s1.json','w'),indent=1)
l=[n for v in out.values() for n in v['needs']]
print(len(out),len(l),sum(v['cost']==2 for v in out.values()),sum(n['confidence']=='low' for n in l))
