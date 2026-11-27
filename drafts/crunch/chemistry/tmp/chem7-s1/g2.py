import json,re
from g1 import R,run,D
H='helpful'
L={
'9.b':[('chem6-s1.0.0',H,'electronegativity defined','high')],
'9.2':[('chem6-s1.1.2',H,'electronegativity trend explanation','high')],
'11.3':[('chem6-s1.6.4',H,'giant covalent high melting point','high')],
'11.4':[('chem6-s1.4.3',H,'molecular substances low melting points','high')],
'11.6':[('chem6-s1.9.3',H,'London forces grow with size','high')],
'3.4':[('chem14-s1.0.0',H,'oxidation as adding oxygen','low')],
'1.2':[('chem14-s1.6.0',H,'tarnishing is oxidation','low')],
'4.4':[('chem6-s1.5.0',H,'covalent substances do not conduct','low')],
}
# every target explicitly listed (suffix, links); ids from the same explicit list as g1
R2=[(s,0,L.get(s,[])) for s,_,_ in R]
txt=open(D+'point-links/chem7-s1.t1g1.json').read()
import io,sys
run('chem7-s1.t1g2.txt','chem7-s1.t1g2.json','chem7-s1.',R2)
d=json.load(open(D+'point-links/chem7-s1.t1g2.json'))
for v in d.values(): del v['cost']
json.dump(d,open(D+'point-links/chem7-s1.t1g2.json','w'),indent=1)
