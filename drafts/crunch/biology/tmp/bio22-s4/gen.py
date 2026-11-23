import json,re
P='/Users/gabrielwhelan/barebones/drafts/crunch/biology/'
txt=open(P+'points/bio22-s4.txt').read()
allids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
tgt=[i for i in re.findall(r'^\[([^\]]+)\]',txt.split('CANDIDATES')[0],re.M)]
S='bio22-s4.'
E,H='essential','helpful'
spec={
'0.b':(1,[('bio6-s1.0.0',H,'obligate intracellular parasite','high')]),
'0.0':(1,[('bio6-s1.0.1',E,'viruses lack ribosomes and enzymes','high')]),
'0.1':(2,[(S+'0.0',E,'virus cannot make anything itself','high'),('bio10-s1.0.0',H,'nucleotides as nucleic acid units','low'),('bio17-s2.1.5',H,'ribosomes build proteins','low')]),
'1.b':(1,[(S+'0.1',H,'host cell makes viral parts','low')]),
'1.0':(1,[('bio6-s1.1.2',E,'capsid proteins bind host receptors','high'),('bio6-s1.1.3',H,'envelope structure','low')]),
'1.1':(1,[(S+'1.0',E,'receptor binding in attachment','high')]),
'1.2':(1,[('bio6-s1.2.5',E,'bacteriophage structure','high')]),
'1.3':(2,[('bio6-s1.1.3',E,'viral envelope from host membrane','high'),(S+'1.0',H,'attachment before entry','low')]),
'1.4':(1,[('bio6-s1.1.1',E,'capsid protein coat','high')]),
'2.b':(1,[(S+'1.4',H,'nucleic acid free after uncoating','low')]),
'2.0':(2,[('bio17-s2.0.4',E,'mRNA carries gene code','high'),('bio17-s2.1.5',E,'ribosomes translate mRNA','high')]),
'2.1':(1,[(S+'2.0',H,'viral synthesis stage','low')]),
'2.2':(1,[(S+'2.0',E,'capsid proteins made in stage 4','high')]),
'2.3':(2,[('bio6-s1.1.3',E,'envelope from host membrane','high')]),
'2.4':(1,[(S+'2.3',E,'release of new viruses','high')]),
'2.5':(2,[(S+'3.0',E,'lytic cycle','high'),(S+'2.3',H,'cell bursting release','low')]),
'2.6':(2,[(S+'1.3',E,'endocytosis and fusion entry','high'),(S+'2.3',E,'budding release','high')]),
'3.b':(1,[(S+'2.3',H,'lysis as release','low')]),
'3.0':(1,[(S+'2.3',E,'lysis release','high')]),
'3.1':(2,[(S+'3.0',H,'contrast with lytic cycle','high'),('bio10-s1.4.1',H,'DNA copied before cell division','low')]),
'3.2':(1,[(S+'3.1',E,'lysogenic inserted DNA','high')]),
'3.3':(1,[(S+'3.1',E,'lysogenic DNA in chromosome','high'),(S+'3.0',H,'lytic cycle restarts','low')]),
'3.4':(1,[(S+'3.1',H,'hidden inactive viral DNA','low')]),
'3.5':(1,[(S+'3.4',E,'latency in human viruses','high')]),
'3.6':(1,[(S+'3.4',E,'latency and reactivation','high')]),
'3.7':(1,[(S+'3.4',E,'latent virus inactive','high'),(S+'2.0',H,'viral proteins made in replication','low')]),
'4.b':(1,[]),
'4.0':(1,[(S+'2.3',E,'lysis destroys cells','high')]),
'4.1':(1,[(S+'0.1',E,'host machinery used for viruses','high')]),
'4.2':(1,[(S+'1.1',H,'HIV binds CD4 on helper T cells','low')]),
'4.3':(2,[(S+'4.2',E,'helper T cell destruction','high')]),
'4.4':(1,[(S+'4.3',E,'AIDS weakens immune system','high')]),
'4.5':(2,[('bio6-s1.5.2',H,'HPV causes cervical cancer','low')]),
'4.6':(1,[]),
'5.b':(1,[]),
'5.0':(1,[]),
'5.1':(1,[(S+'5.0',E,'DNA virus definition','high')]),
'5.2':(1,[(S+'5.0',E,'RNA virus definition','high')]),
'5.3':(2,[(S+'5.0',H,'DNA virus genetic material','low'),('bio17-s2.0.2',E,'RNA polymerase makes mRNA','high')]),
'5.4':(1,[(S+'5.3',E,'contrast with usual DNA virus site','high')]),
'5.5':(2,[(S+'5.0',E,'RNA virus genetic material','high')]),
'5.6':(2,[(S+'5.5',E,'RNA-copying enzyme','high'),(S+'5.3',H,'host polymerases proofread','low')]),
'5.7':(2,[(S+'5.6',E,'high mutation rate of RNA viruses','high'),('bio6-s1.3.3',H,'viral mutation and evolution','low')]),
'6.b':(1,[('bio17-s2.0.4',H,'mRNA translated into proteins','low')]),
'6.0':(1,[('bio17-s2.0.4',E,'RNA acting as mRNA','high'),('bio17-s2.1.5',H,'host ribosomes translate','low')]),
'6.1':(2,[(S+'5.5',E,'RNA-dependent RNA polymerase copies RNA','high'),('bio17-s2.0.4',H,'complementary strand acts as mRNA','low')]),
'6.2':(1,[(S+'5.6',E,'DNA viruses mutate slower','high')]),
'6.3':(1,[(S+'5.6',H,'mutation rate of viruses','low')]),
'7.b':(1,[('bio17-s2.2.b',H,'normal DNA to RNA flow','low')]),
'7.0':(2,[('bio17-s2.2.b',H,'usual DNA to RNA direction','low')]),
'7.1':(1,[(S+'1.1',E,'CD4 receptor binding','high')]),
'7.2':(1,[(S+'1.3',E,'enveloped virus entry by fusion','high')]),
'7.3':(2,[(S+'7.0',E,'reverse transcriptase function','high')]),
'7.4':(2,[(S+'7.3',E,'viral DNA made from RNA','high'),(S+'3.1',H,'DNA inserted into host chromosome','low')]),
'7.5':(2,[(S+'7.4',E,'provirus in host chromosome','high'),('bio17-s2.2.b',E,'transcription makes mRNA','high')]),
'7.6':(1,[(S+'2.3',E,'budding release with envelope','high')]),
'7.7':(2,[(S+'7.0',E,'reverse transcriptase','high'),(S+'5.6',H,'copying errors cause mutation','low')]),
'7.8':(2,[(S+'7.6',E,'six HIV steps','high')]),
'8.b':(1,[(S+'2.b',H,'replication stages targeted','low')]),
'8.0':(1,[(S+'2.0',H,'viral proteins made','low')]),
'8.1':(1,[(S+'5.3',E,'DNA polymerase','high')]),
'8.2':(1,[(S+'2.3',E,'release of new viruses','high')]),
'8.3':(1,[(S+'7.0',E,'reverse transcriptase','high')]),
'8.4':(2,[(S+'2.0',E,'viral proteins made as stage 4','low')]),
'8.5':(1,[(S+'8.3',H,'HIV drug types','low')]),
'8.6':(2,[(S+'7.4',E,'provirus in host DNA','high')]),
'8.7':(2,[(S+'7.7',H,'HIV mutates quickly','low')]),
'9.b':(1,[(S+'1.b',H,'six stages','high')]),
'9.0':(2,[(S+'1.b',E,'six stages of cycle','high')]),
'9.1':(1,[(S+'9.0',E,'stages being modelled','high')]),
'9.2':(2,[(S+'5.5',E,'RNA virus replication','high'),(S+'7.0',E,'retrovirus','high')]),
'9.3':(1,[(S+'8.0',E,'antiviral drug targets','high')]),
'9.4':(1,[(S+'2.3',H,'budding','low')]),
'9.5':(1,[(S+'9.0',H,'model of cycle','low')]),
'9.6':(1,[(S+'9.5',H,'model limitations','low')]),
'9.7':(1,[(S+'2.2',H,'many viruses per cell','low')]),
'9.8':(1,[(S+'9.0',E,'stages in flow chart','high')]),
}
out={}
for t in tgt:
    c,n=spec[t[len(S):]]
    out[t]={'cost':c,'needs':[{'id':i,'strength':s,'why':w,'confidence':f} for i,s,w,f in n]}
assert set(spec)=={t[len(S):] for t in tgt},set(spec)^{t[len(S):] for t in tgt}
for t,v in out.items():
    for n in v['needs']: assert n['id'] in allids and n['id']!=t,(t,n['id'])
json.dump(out,open(P+'point-links/bio22-s4.json','w'),indent=1)
n=sum(len(v['needs']) for v in out.values())
print(len(out),n,sum(v['cost']==2 for v in out.values()),sum(x['confidence']=='low' for v in out.values() for x in v['needs']))
