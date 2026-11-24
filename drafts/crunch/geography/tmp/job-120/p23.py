from build import *
H='H'
def run(name,links):
    import re
    txt=open(P+'packs/'+name+'.txt').read()
    ids=[re.match(r'\[geo-region-ireland-s2\.(\S+?)\]',l).group(1) for l in txt.split('\n\n')[0].split('\n') if l.startswith('[')]
    miss=[i for i in ids if i not in links]
    assert not miss,miss
    pack(name,[(i,links[i]) for i in ids],False)
