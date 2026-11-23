import json,re
P='/Users/gabrielwhelan/barebones/drafts/crunch/biology/'
txt=open(P+'points/bio17-s2.txt').read()
tgt=txt.split('CANDIDATES')[0]
ids=re.findall(r'^\[([^\]]+)\]',tgt,re.M)
allids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
S='bio17-s2.'
# id: (cost, [(need, strength, why, conf)])
E,H='essential','helpful'
spec={
'0.0':(1,[('bio10-s2.0.0',H,'gene as protein code','high')]),
'0.1':(1,[('bio10-s1.2.0',H,'two DNA strands','high')]),
'0.2':(2,[('bio10-s1.2.6',E,'complementary strands','high'),('bio10-s1.0.2',H,'nucleotide structure','low')]),
'0.3':(1,[(S+'0.2',E,'RNA polymerase building strand','high')]),
'0.4':(1,[('bio10-s3.0.1',E,'codon definition','high'),('bio10-s1.6.4',H,'mRNA role','low')]),
'0.5':(1,[(S+'0.4',H,'mRNA as the copy','high')]),
'1.0':(1,[('bio8-s2.7.1',H,'amino acids','high')]),
'1.1':(2,[('bio10-s3.2.0',E,'anticodon pairs with codon','high')]),
'1.2':(1,[(S+'1.0',H,'tRNA carries amino acids','high')]),
'1.3':(1,[('bio10-s1.6.5',H,'rRNA forms ribosome','low')]),
'1.4':(1,[('bio8-s2.7.4',E,'peptide bond','high')]),
'1.5':(2,[(S+'1.3',H,'rRNA in ribosome','high'),(S+'1.1',H,'tRNA binding','low')]),
'1.6':(1,[(S+'1.5',H,'ribosome structure','high')]),
'1.7':(1,[(S+'1.5',H,'ribosome','high')]),
'2.b':(1,[('bio10-s1.2.1',E,'complementary base pairing','high')]),
'2.0':(1,[(S+'0.2',E,'RNA polymerase unwinding','high')]),
'2.1':(1,[(S+'0.1',E,'template strand','high')]),
'2.2':(2,[('bio10-s1.6.1',E,'U pairs with A','high')]),
'2.3':(1,[(S+'0.2',H,'RNA polymerase joins nucleotides','high')]),
'2.4':(1,[(S+'0.1',H,'DNA unchanged','high')]),
'2.5':(1,[(S+'2.3',H,'RNA polymerase moving','high')]),
'2.6':(1,[(S+'0.4',H,'mRNA carries code out','high')]),
'2.7':(1,[(S+'2.2',H,'labels from transcription steps','low')]),
'3.b':(1,[(S+'1.0',H,'tRNA carries amino acid','low')]),
'3.0':(2,[('bio10-s1.6.2',E,'RNA folds and base-pairs','high')]),
'3.1':(1,[(S+'3.0',H,'folded tRNA shape','high')]),
'3.2':(1,[(S+'1.0',H,'tRNA carries amino acid','high')]),
'3.3':(1,[('bio10-s3.2.0',E,'anticodon definition','high')]),
'3.4':(1,[('bio10-s3.0.1',E,'codon of three bases','high')]),
'3.5':(2,[(S+'3.2',E,'amino acid attachment site','high')]),
'3.6':(1,[(S+'3.4',H,'three-base codon reading','high')]),
'3.7':(1,[(S+'3.0',H,'tRNA structure','high')]),
'4.b':(1,[('bio8-s2.7.5',H,'polypeptide chain','high')]),
'4.0':(1,[('bio10-s3.1.0',E,'start codon AUG','high')]),
'4.1':(2,[(S+'4.0',E,'start codon pairing','high')]),
'4.2':(1,[(S+'1.1',E,'anticodon pairs with codon','high')]),
'4.3':(2,[('bio8-s2.7.4',E,'peptide bond condensation','high')]),
'4.4':(1,[(S+'4.3',H,'peptide bond joins amino acids','high')]),
'5.b':(1,[(S+'4.b',H,'translation start steps','high')]),
'5.0':(1,[(S+'4.2',H,'tRNA positions in ribosome','high')]),
'5.1':(1,[(S+'5.0',H,'ribosome move exposes codon','high')]),
'5.2':(1,[(S+'5.1',H,'repeating cycle','high')]),
'5.3':(2,[('bio10-s3.1.1',E,'stop codons','high')]),
'5.4':(1,[(S+'5.3',H,'stop codon ends translation','high')]),
'5.5':(1,[(S+'1.5',H,'ribosome translating mRNA','high')]),
'5.6':(1,[(S+'3.2',H,'ATP attaches amino acid','low')]),
'5.7':(2,[(S+'4.3',H,'peptide bond forming','low')]),
'6.b':(1,[('bio10-s2.1.1',H,'sequence determines folding','high')]),
'6.0':(1,[('bio10-s2.1.1',H,'sequence determines folding','high')]),
'6.1':(2,[('bio8-s2.8.0',H,'protein structure bonds','high')]),
'6.2':(1,[('bio8-s2.8.1',H,'quaternary structure','high')]),
'6.3':(1,[('bio10-s2.1.2',H,'shape determines function','high')]),
'6.4':(1,[(S+'6.1',E,'bonds folding the chain','high')]),
'6.5':(2,[(S+'1.7',H,'ribosomes on rough ER','high')]),
'6.6':(2,[('bio10-s1.4.3',H,'bacterial DNA in cytoplasm','low')]),
'7.b':(1,[(S+'2.b',H,'transcription base pairing','high')]),
'7.0':(1,[(S+'0.4',H,'mRNA product','high')]),
'7.1':(1,[(S+'0.1',H,'template strand','high')]),
'7.2':(1,[(S+'0.2',E,'RNA polymerase','high')]),
'7.3':(1,[('bio10-s1.7.1',H,'ribose vs deoxyribose','high')]),
'7.5':(1,[(S+'0.5',H,'mRNA broken down','high')]),
'8.0':(1,[(S+'2.2',E,'complementary RNA pairing','high')]),
'8.1':(1,[('bio10-s3.0.1',E,'codons','high')]),
'8.2':(1,[(S+'1.1',E,'anticodon pairs with codon','high')]),
'8.3':(1,[('bio10-s3.3.2',H,'using codon table','high')]),
'8.4':(1,[(S+'5.3',H,'stop codon','high')]),
'9.b':(1,[(S+'8.b',H,'five-step method','high')]),
'9.0':(2,[(S+'8.0',E,'writing mRNA from template','high')]),
'9.1':(1,[(S+'8.2',E,'anticodon method','high')]),
'9.2':(1,[(S+'8.3',H,'codon table lookup','high')]),
'9.3':(1,[(S+'4.3',H,'peptide bond count','high')]),
'10.0':(1,[(S+'2.6',H,'mRNA moves to ribosome','low')]),
'10.1':(1,[(S+'1.1',H,'tRNA anticodon and amino acid','high')]),
'10.2':(1,[(S+'4.3',H,'peptide bonds','high')]),
}
out={}
for i in ids:
    c,n=spec.get(i[len(S):],(1,[]))
    out[i]={'cost':c,'needs':[{'id':a,'strength':s,'why':w,'confidence':f} for a,s,w,f in n]}
json.dump(out,open(P+'point-links/bio17-s2.json','w'),indent=1)
d=json.load(open(P+'point-links/bio17-s2.json'))
assert list(d)==ids and len(set(ids))==len(ids)
for k,v in d.items():
    for n in v['needs']: assert n['id'] in allids and n['id']!=k,(k,n)
print(len(d),sum(len(v['needs']) for v in d.values()),sum(v['cost']==2 for v in d.values()),sum(n['confidence']=='low' for v in d.values() for n in v['needs']))
