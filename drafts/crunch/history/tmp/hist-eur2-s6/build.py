import json,re,sys
D='/Users/gabrielwhelan/barebones/drafts/crunch/history/'
# id|cost|links  (link = target:E|H:why:H|L, ';' separated)
RAW='''
0.b|1|
0.0|1|s5.7.4:H:uses the Hindenburg Line breaking:H
0.1|2|6.2.0:E:armistice on Fourteen Points basis:H;6.0.0:H:armistice request after Ludendorff's demand:L
0.2|1|6.0.1:H:Wilson's armistice exchange:H
0.3|2|6.0.0:H:Ludendorff's role:L
0.4|1|s8.4.2:H:soviets as council model:H
0.5|2|6.0.1:H:Prince Max as Chancellor:H
0.6|1|s5.7.5:H:armistice signed at Compiegne:L
0.7|2|s5.3.4:H:Treaty of Brest-Litovsk:H;s5.5.0:H:Allied naval blockade:H
1.0|1|6.0.5:E:Ebert as head of government:H
1.1|1|
1.2|2|6.0.4:H:councils on Russian model:H;6.1.0:H:SPD leaders and elections:L
1.3|2|6.1.2:E:Spartacus League radicals:H
1.4|1|6.1.3:E:Freikorps and the rising:H;6.1.2:H:Luxemburg and Liebknecht as KPD founders:H
1.5|1|
1.6|1|6.0.0:H:army leadership asked for armistice:H
2.0|1|6.8.b:H:Wilson as president:H
2.1|2|6.2.0:E:the Fourteen Points:H
2.2|2|6.2.0:E:the Fourteen Points:H
2.3|1|6.2.0:H:Point 14 of the Fourteen Points:H;6.7.0:H:the League of Nations:H
2.4|1|6.2.0:E:Fourteen Points as armistice basis:H;6.0.1:H:Germany's October armistice request:H
2.5|1|6.2.4:E:pre-armistice agreement on Fourteen Points:H;6.4.0:H:harsh terms of Versailles:L
3.b|1|
3.0|2|
3.1|1|6.7.0:H:the League of Nations:H
3.2|1|
3.3|2|
3.4|1|s5.4.2:E:Treaty of London promises to Italy:H;6.3.0:H:Orlando as one of Big Four:H
3.5|1|
3.6|1|
3.7|1|
4.b|1|
4.0|1|6.4.6:H:reparations based on the clause:H
4.1|2|
4.2|2|6.7.0:H:League of Nations protection:H
4.3|1|6.7.0:H:League of Nations mandates:H
4.4|2|
4.5|1|
4.6|2|6.4.0:E:war guilt clause as basis:H
4.7|1|6.0.6:H:Kaiser fled to Netherlands:H;6.7.0:H:League Covenant:H
4.8|1|6.3.7:H:terms imposed without negotiation:H;6.0.5:H:Scheidemann proclaimed the republic:L
5.0|2|
5.1|1|6.5.0:H:Austria-Hungary's break-up:H
5.2|2|6.5.0:H:new states recognised:H;6.4.5:H:union with Germany forbidden:H
5.3|2|6.5.0:H:successor states of Austria-Hungary:H
5.4|1|
5.5|2|s5.4.0:H:Ottoman Empire in the war:L
5.6|1|6.4.3:H:League mandates idea:H
6.0|1|s8.8.6:H:Baltic states and Poland independence:L
6.1|2|6.4.1:H:Schleswig and territorial changes:L
6.2|1|6.4.5:H:Anschluss forbidden:H
6.3|1|6.5.2:H:South Tyrol given to Italy:H;6.5.3:H:Hungarians left outside borders:H
6.4|1|
6.5|1|6.4.3:H:colonies as mandates:H;6.3.1:H:self-determination principle:H
7.0|2|
7.1|2|6.7.0:H:the League of Nations:H
7.2|1|6.7.0:H:the League of Nations:H
7.3|1|6.8.b:H:Wilson and the League:H
7.4|2|6.7.1:E:Article 10 collective security:H;6.7.3:H:Wilson's campaign for support:L
7.5|1|6.7.4:E:Senate rejecting the treaty:H
8.b|1|
8.0|1|
8.1|1|
8.2|1|s5.5.3:H:unrestricted submarine warfare:H;s5.7.0:H:Zimmermann Telegram:H
8.3|1|6.2.0:E:the Fourteen Points:H;6.7.0:H:the League Covenant:H
8.4|2|6.4.0:H:Article 231:H;6.4.2:H:the Saar:H;6.3.5:H:Japanese gains in Shandong:H;6.7.0:H:League and mandates:L
8.5|1|6.7.4:E:Lodge and the Senate:H
8.6|1|6.3.2:H:Clemenceau as one of the Big Four:L
8.7|2|6.7.4:H:Senate handling:H;6.6.2:H:self-determination applied inconsistently:L
9.0|1|6.7.0:H:League of Nations:H;6.5.0:H:new states in Europe:H
9.1|1|6.6.4:H:minorities in new states:H
9.2|2|6.4.8:H:German resentment of the treaty:H;6.7.5:H:Britain and France enforcing alone:H
9.3|2|
9.4|2|6.4.6:E:reparations:H
9.5|2|s5.3.4:E:Treaty of Brest-Litovsk comparison:H
'''
def build(sub,RAW,pack,out):
    txt=open(D+'packs/'+pack).read()
    tgt=[]; allids=set()
    mode=None
    for l in txt.split('\n'):
        if l.startswith('TARGET'): mode='t'
        elif l.startswith('CANDIDATES'): mode='c'
        m=re.match(r'\[(\S+?)\]',l)
        if m:
            allids.add(m.group(1))
            if mode=='t': tgt.append(m.group(1))
    res={}
    for line in RAW.strip().split('\n'):
        i,c,ls=line.split('|')
        i=sub+'.'+i if not i.startswith('s') else i
        needs=[]
        for k in filter(None,ls.split(';')):
            t,s,w,cf=k.split(':')
            if t.startswith('s'): t='hist-'+sub.split('-')[1]+'-'+t if False else None
            needs.append((k,))
        res[i]=(int(c),ls)
    return tgt,allids,res
