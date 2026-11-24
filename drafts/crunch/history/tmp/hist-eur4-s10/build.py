import json,re
H='/Users/gabrielwhelan/barebones/drafts/crunch/history/'
def build(pack,out,pre,targets,c2,L):
    # targets: explicit list of suffixes; c2: set with cost 2; L: dict suffix->list of (full id or suffix,s,why,conf)
    res={}
    for t in targets:
        needs=[]
        for (i,s,w,c) in L.get(t,[]):
            needs.append({"id":i if i.startswith('hist-') else pre+i,"strength":{'e':'essential','h':'helpful'}[s],"why":w,"confidence":{'h':'high','l':'low'}[c]})
        res[pre+t]={"cost":2 if t in c2 else 1,"needs":needs}
    txt=open(H+'packs/'+pack).read()
    ids=set(re.findall(r'^\[(hist-[^\]]+)\]',txt,re.M))
    tg=set(re.findall(r'^\[(hist-[^\]]+)\]',txt.split('CANDIDATES')[0],re.M))
    assert tg==set(res) and len(res)==len(targets),(tg^set(res))
    for k,v in res.items():
        for n in v['needs']: assert n['id'] in ids and n['id']!=k,n
    json.dump(res,open(H+'point-links/'+out,'w'),indent=1)
    print(out,len(res),sum(len(v['needs']) for v in res.values()),sum(v['cost']==2 for v in res.values()),sum(n['confidence']=='l' for v in res.values() for n in v['needs']))

def T(spec): # "0:b,0-11;1:b,0-9"
    out=[]
    for part in spec.split(';'):
        a,b=part.split(':')
        for x in b.split(','):
            if x=='b': out.append(f'{a}.b')
            elif '-' in x:
                lo,hi=map(int,x.split('-')); out+= [f'{a}.{i}' for i in range(lo,hi+1)]
            else: out.append(f'{a}.{x}')
    return out

# package 1
t1=T("0:b,0-11;1:b,0-9;2:b,0-9;3:b,0-8;4:b,0-7;5:b,0-5;6:b,0-3;7:b,0-3")
c2={'0.4','0.6','0.7','0.8','0.9','0.10','1.6','2.3','2.5','2.6','2.7','2.9','3.5','4.4','4.6','6.0','6.2'}
S2='hist-eur4-s2.';S9='hist-eur4-s9.';S11='hist-eur4-s11.'
L1={
'0.1':[('0.0','h','arrest and sentence','h')],
'0.2':[(S2+'1.0','h','de-Stalinisation opened literature','h')],
'0.3':[('0.1','h','Gulag experience behind book','h')],
'0.4':[('0.3','h','Gulag Archipelago prompted expulsion','l')],
'0.6':[('0.3','h','his Gulag testimony','l')],
'0.7':[('0.1','h','camps and exile','h')],
'0.8':[(S2+'0.10','e','Khrushchev fell in 1964','h'),('0.2','h','earlier publication in Novy Mir','l')],
'0.9':[('0.3','e','Gulag Archipelago manuscript','h')],
'0.10':[('0.4','h','exile in Vermont','h')],
'0.11':[('0.4','h','return to Russia 1994','l')],
'1.b':[(S9+'0.b','h','The Second Sex as feminist treatise','h')],
'1.1':[(S9+'0.0','h','her partnership with Sartre','l')],
'1.9':[(S9+'0.0','h','her partnership with Sartre','h')],
'2.3':[(S2+'8.3','h','Prague Spring','h')],
'2.4':[('0.9','h','Solzhenitsyn expelled 1974','h')],
'2.7':[('2.2','h','Havel and Charter 77 context','l')],
'2.9':[(S2+'6.5','h','Helsinki Final Act human rights','h')],
'3.6':[('3.1','h','Camus and The Plague','l'),('3.5','h','Sartre existentialism','l')],
'3.8':[('3.0','h','Orwell Nineteen Eighty-Four','h')],
'4.1':[(S11+'0.b','h','Second Vatican Council','h'),(S11+'4.2','h','Humanae Vitae contraception ban','h')],
'5.2':[(S11+'5.1','h','Polish pope elected 1978','h')],
'5.4':[(S2+'0.b','h','Khrushchev era','l')],
'6.2':[(S11+'3.6','h','1054 excommunications lifted','h'),(S11+'0.b','h','Vatican II','h')],
'7.0':[(S2+'0.3','h','Stalin crimes exposed','l')],
'7.1':[('2.0','h','samizdat','h')],
'7.3':[('4.2','h','secularisation','h')],
}
build('hist-eur4-s10.t1g1.txt','hist-eur4-s10.t1g1.json','hist-eur4-s10.',t1,c2,L1)

# package 2
t2=T("0:b,0-6;1:b,0-5;2:b,0-6;3:b,0-6;4:b,0-5;5:b,0-6;6:b,0-11;7:b,0-5;8:b,0-7;9:b,0-5")
c2b={'0.0','0.3','0.5','2.0','2.4','2.5','3.0','3.2','3.5','4.4','5.2','5.5','6.5','6.7','6.10','6.11','7.4','7.5','1.1'}
L2={
'0.2':[('0.0','h','the President','h')],
'0.6':[('0.5','h','reparations from Versailles','h')],
'1.1':[('1.0','h','Freikorps','l')],
'1.3':[('1.2','h','right-wing political murders','l')],
'1.4':[('0.6','h','reparations demands','h')],
'1.5':[('1.4','e','Ruhr occupation','h')],
'2.b':[('1.5','e','passive resistance','h')],
'2.3':[('1.5','e','passive resistance in Ruhr','h')],
'2.4':[('2.3','h','end of passive resistance','h')],
'2.5':[('1.4','h','Ruhr occupation','h')],
'2.6':[('2.5','e','Dawes Plan loans','h')],
'3.1':[('3.0','h','NSDAP','h')],
'3.2':[('3.0','e','Hitler and NSDAP','h'),('3.1','h','Nazi supporters and SA','l')],
'3.3':[('3.2','e','Munich Putsch','h')],
'3.4':[('3.3','h','imprisonment at Landsberg','h')],
'3.5':[('3.2','e','banned after the putsch','h')],
'3.6':[('4.3','e','Young Plan','h')],
'4.0':[('0.5','h','revision of Versailles','h')],
'4.1':[('4.0','h','Stresemann policy','h')],
'4.3':[('2.5','h','Dawes Plan reparations','h')],
'4.5':[('4.0','h','Stresemann policies','h')],
'5.0':[('2.6','h','American loans withdrawn','h')],
'5.1':[('4.4','h','unemployment insurance','h')],
'5.2':[('0.2','e','Article 48 decrees','h'),('5.1','h','1930 coalition collapse','h')],
'5.3':[('5.2','e','Brüning deflationary decrees','h')],
'5.5':[('0.6','h','reparations','h'),('5.2','h','Brüning policy','l')],
'6.0':[('3.5','h','1928 result of 12 seats','h')],
'6.1':[('0.5','h','Versailles settlement','l')],
'6.3':[('3.1','h','SA','h')],
'6.4':[('6.0','h','earlier Nazi vote','l')],
'6.6':[('0.4','h','Hindenburg as President','h')],
'6.7':[('6.3','h','SA','h'),('5.2','h','Brüning as Chancellor','l')],
'6.8':[('6.7','h','Papen government','h')],
'6.9':[('6.4','h','July 1932 result','h')],
'6.10':[('6.9','h','Nazi decline late 1932','l')],
'6.11':[('6.10','h','Schleicher resignation','h'),('6.7','h','Papen','l')],
'7.1':[('3.0','h','German Workers Party','h')],
'7.2':[('3.0','h','NSDAP','h')],
'7.3':[('3.2','e','Munich Putsch','h')],
'7.4':[('6.11','h','Papen and Hindenburg appointment','h')],
'7.5':[('6.11','h','Hitler appointed Chancellor','h')],
'8.2':[('2.4','e','Rentenmark','h'),('2.3','h','end of passive resistance','h')],
'8.3':[('4.4','h','1927 unemployment insurance','h')],
'8.4':[('5.2','h','Brüning decrees','h')],
'8.6':[('8.5','h','Voluntary Labour Service','l')],
'8.7':[('6.3','h','SA recruitment','h')],
'9.0':[('0.1','h','proportional representation','h'),('0.2','h','Article 48','h')],
'9.1':[('0.5','h','Treaty of Versailles','h')],
'9.2':[('4.b','h','Stresemann era','h')],
'9.3':[('5.0','h','Depression unemployment','h')],
'9.4':[('6.11','h','appointment of Hitler','h')],
}
build('hist-eur3-s2.t1g1.txt','hist-eur3-s2.t1g1.json','hist-eur3-s2.',t2,c2b,L2)
