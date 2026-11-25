import json,re
P='/Users/gabrielwhelan/barebones/drafts/crunch/biology/'
txt=open(P+'points/bio35-s6.txt').read()
allids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
targets=re.findall(r'^\[(bio35-s6\.[^\]]+)\]',txt,re.M)
H,E='helpful','essential'
def n(i,s,w,c='high'):return {"id":i,"strength":s,"why":w,"confidence":c}
c2={'6.5','7.2','7.5','7.6','7.7','8.1'}
L={
'0.b':[n('bio35-s2.0.0',H,'DNA profile definition')],
'0.0':[n('bio35-s2.5.0',H,'match rule for profiles')],
'0.1':[n('bio35-s3.9.b',H,'gel electrophoresis setup','low')],
'0.2':[n('bio35-s2.1.2',H,'repeat numbers set band size','low')],
'0.3':[n('bio35-s2.5.1',H,'exclusion from a differing band')],
'1.1':[n('bio35-s2.4.2',H,'band position shows size')],
'1.3':[n('bio35-s3.9.4',H,'DNA ladder')],
'1.4':[n('bio35-s3.9.2',H,'loading dye','low')],
'2.1':[n('bio35-s3.9.1',H,'tank, wells, buffer')],
'2.2':[n('bio35-s3.9.2',H,'loading dye')],
'2.3':[n('bio35-s3.10.3',H,'staining colourless DNA')],
'3.b':[n('bio35-s3.9.b',H,'gel set-up')],
'3.0':[n('bio35-s3.9.0',H,'agarose gel')],
'3.1':[n('bio35-s3.9.1',H,'wells at negative end')],
'3.2':[n('bio35-s2.4.1',E,'DNA negatively charged')],
'3.3':[n('bio35-s3.9.3',H,'micropipette loading')],
'3.4':[n('bio35-s3.9.4',H,'DNA ladder')],
'4.b':[n('bio35-s3.10.b',H,'running and visualising bands')],
'4.0':[n('bio35-s3.10.0',H,'DNA moves to positive electrode')],
'4.1':[n('bio35-s3.10.2',H,'stop before dye runs off')],
'4.2':[n('bio35-s3.10.3',H,'staining DNA')],
'4.3':[n('bio35-s2.4.2',H,'band position shows size')],
'5.2':[n('bio35-s3.10.4',H,'ethidium bromide is mutagen')],
'6.b':[n('bio35-s2.4.2',H,'more repeats, nearer wells'),n('bio35-s2.1.2',H,'repeat number varies at locus','low')],
'6.1':[n('bio35-s2.5.0',E,'strict match rule')],
'6.2':[n('bio35-s2.5.1',E,'one differing band excludes')],
'6.3':[n('bio35-s2.2.1',E,'same alleles give one band')],
'6.5':[n('bio35-s2.5.1',E,'differing band excludes')],
'6.6':[n('bio35-s2.5.0',H,'matching every band')],
'6.7':[n('bio35-s2.3.1',H,'many loci make match reliable')],
'7.b':[n('bio35-s2.2.2',E,'child gets one band per parent')],
'7.0':[n('bio35-s2.2.2',E,'one band from each parent')],
'7.1':[n('bio35-s2.2.2',E,'other band from father')],
'7.2':[n('bio35-s2.5.2',E,'paternity exclusion logic')],
'7.5':[n('bio35-s6.7.2',E,'steps for finding paternal bands')],
'7.6':[n('bio35-s6.7.2',E,'exclusion rule for fathers')],
'7.7':[n('bio35-s6.7.1',H,'maternal and paternal bands')],
'7.8':[n('bio35-s6.7.7',H,'gel diagram drawing')],
'8.0':[n('bio35-s3.11.0',H,'comparing bands with ladder')],
'8.1':[n('bio35-s3.9.4',H,'ladder of known sizes')],
'8.2':[n('bio35-s6.6.2',H,'one mismatch excludes')],
'8.3':[n('bio35-s2.3.1',E,'chance match between unrelated people')],
'8.4':[n('bio35-s2.0.2',H,'identical twins same DNA')],
'8.5':[n('bio35-s2.2.2',H,'one band from each parent','low')],
'8.6':[n('bio35-s2.2.2',E,'one allele from each parent')],
'9.0':[n('bio35-s6.1.4',H,'no-DNA negative control')],
'9.2':[n('bio35-s3.10.2',H,'stop before fragments run off')],
'9.5':[n('bio35-s3.9.4',H,'ladder compares gels','low')],
}
out={}
for t in targets:
    k=t.replace('bio35-s6.','')
    out[t]={"cost":2 if k in c2 else 1,"needs":L.get(k,[])}
json.dump(out,open(P+'point-links/bio35-s6.json','w'),ensure_ascii=False)
d=json.load(open(P+'point-links/bio35-s6.json'))
assert list(d)==targets and len(set(targets))==len(targets)
nl=[x for v in d.values() for x in v['needs']]
assert all(x['id'] in allids for x in nl)
assert all(x['id']!=t for t,v in d.items() for x in v['needs'])
print(len(d),len(nl),sum(v['cost']==2 for v in d.values()),sum(x['confidence']=='low' for x in nl))
