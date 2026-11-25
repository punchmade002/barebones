import json,re,sys
D='/Users/gabrielwhelan/barebones/drafts/crunch/biology/'
P='bio16-s1.'
E,H='essential','helpful'
def n(i,s,w,c='high'):
    return (i if '-s' in i else P+i,s,w,c)
spec={
'0.b':(1,[]),
'0.0':(1,[n('bio7-s3.5.0',H,'chromosome as DNA with genes')]),
'0.1':(1,[n('0.0',E,'chromosome structure')]),
'0.2':(2,[n('0.0',E,'chromosome')]),
'0.3':(1,[n('0.2',E,'homologous pairs')]),
'0.4':(1,[n('0.3',H,'sets of chromosomes')]),
'0.5':(1,[n('0.4',E,'haploid gametes')]),
'0.6':(1,[n('0.4',H,'haploid cells')]),
'0.7':(1,[n('0.3',H,'2n chromosome number')]),
'1.b':(1,[]),'1.0':(1,[]),
'1.1':(1,[n('1.0',H,'cell cycle growth')]),
'1.2':(1,[n('0.0',H,'chromosome being copied')]),
'1.3':(1,[n('1.2',E,'copied chromosomes shared out')]),
'1.4':(1,[n('1.2',H,'DNA synthesis in interphase')]),
'1.5':(1,[]),
'1.6':(1,[n('1.4',E,'interphase')]),
'1.7':(1,[n('0.3',H,'same chromosome number')]),
'2.b':(1,[]),
'2.0':(1,[n('1.0',H,'leaving the cell cycle')]),
'2.1':(1,[n('1.0',H,'repeated cell cycles')]),
'2.2':(2,[n('1.2',H,'DNA copying checked','low')]),
'2.3':(1,[]),
'2.4':(2,[n('1.4',E,'interphase and division'),n('4.0',H,'mitosis stages','low')]),
'3.b':(1,[]),
'3.0':(1,[n('1.1',H,'growth activity')]),
'3.1':(2,[n('1.2',E,'DNA replication')]),
'3.2':(2,[n('bio7-s3.2.2',H,'ATP as energy carrier')]),
'3.3':(1,[n('3.0',H,'G1 phase')]),
'3.4':(1,[n('0.1',E,'chromatin uncoiled'),n('bio7-s3.4.0',H,'nuclear envelope')]),
'4.b':(1,[]),
'4.0':(2,[n('6.0',H,'cytokinesis')]),
'4.1':(2,[n('0.1',E,'condensing chromosomes'),n('3.1',E,'sister chromatids'),n('bio7-s3.4.3',H,'nucleolus','low')]),
'4.2':(1,[n('4.1',H,'spindle forming')]),
'4.3':(1,[n('4.1',E,'spindle fibres')]),
'4.4':(2,[n('3.1',E,'sister chromatids'),n('4.3',H,'metaphase alignment')]),
'4.5':(1,[n('4.4',E,'chromatids separating'),n('bio7-s3.2.2',H,'ATP')]),
'4.6':(2,[n('4.1',E,'reverses prophase changes'),n('0.1',H,'chromatin')]),
'4.7':(2,[n('4.0',E,'four stages of mitosis'),n('0.2',H,'homologous pair','low')]),
'5.b':(1,[]),
'5.0':(1,[n('1.4',E,'interphase')]),
'5.1':(1,[n('4.1',E,'prophase chromosomes'),n('4.3',E,'metaphase line-up')]),
'5.2':(1,[n('4.4',E,'anaphase'),n('4.6',E,'telophase')]),
'5.3':(2,[n('4.0',H,'dividing cells')]),
'5.4':(1,[n('5.3',E,'mitotic index')]),
'6.b':(1,[]),
'6.0':(1,[n('4.0',H,'nuclear division first')]),
'6.1':(1,[n('bio7-s3.0.3',E,'cell membrane')]),
'6.2':(2,[n('bio7-s3.0.0',E,'rigid cell wall'),n('bio7-s3.8.0',H,'Golgi vesicles')]),
'6.3':(1,[n('6.2',E,'cell plate'),n('bio7-s3.0.3',H,'cell membrane','low')]),
'6.4':(1,[n('6.1',H,'cleavage furrow'),n('6.2',H,'cell plate')]),
}
txt=open(D+'points/bio16-s1.txt').read()
ids=re.findall(r'^\[([^\]]+)\]',txt,re.M)
tgt=[i for i in ids if i.startswith(P)]
out={}
for i in tgt:
    c,ns=spec[i[len(P):]]
    out[i]={'cost':c,'needs':[{'id':a,'strength':s,'why':w,'confidence':f} for a,s,w,f in ns]}
assert set(spec)=={i[len(P):] for i in tgt}
for v in out.values():
    for x in v['needs']: assert x['id'] in ids
json.dump(out,open(D+'point-links/bio16-s1.json','w'),indent=1)
l=sum(len(v['needs']) for v in out.values())
print(len(out),l,sum(v['cost']==2 for v in out.values()),sum(x['confidence']=='low' for v in out.values() for x in v['needs']))
