import re,json
P='/Users/gabrielwhelan/barebones/drafts/crunch/biology/points/bio32-s2.txt'
txt=open(P).read()
tgt,cand=txt.split('CANDIDATES',1)
tids=re.findall(r'^\[(\S+?)\]',tgt,re.M)
allids=set(tids)|set(re.findall(r'^\[(\S+?)\]',cand,re.M))
S='bio32-s2.'
# id suffix -> (cost, [needs "id|e/h|why|H/L"])
D={
'0.1':(1,['bio32-s1.10.1|h|records of catches|H']),
'0.2':(2,['0.0|h|abundance versus presence|H']),
'0.3':(1,['0.2|e|DAFOR scale|H']),
'0.4':(2,[]),
'0.5':(2,['0.4|e|quantitative data|H','bio31-s1.4.3|h|species diversity meaning|H']),
'1.1':(1,['1.0|h|representative sample idea|L']),
'1.2':(1,['1.1|e|random sampling|H']),
'1.3':(2,['1.2|e|grid axes laid out|H','3.0|h|quadrat|H']),
'1.4':(1,['1.3|e|coordinates to walk to|H','3.0|e|quadrat|H']),
'1.5':(1,['3.0|h|quadrat|H','1.1|h|random sampling|H']),
'2.0':(2,['1.1|h|contrast with random sampling|H','7.b|h|transect|H']),
'2.1':(1,['1.0|h|representative sample|L']),
'2.2':(1,['3.0|h|quadrat samples|H']),
'2.3':(1,['2.2|e|running mean|H']),
'3.1':(1,['3.0|e|quadrat|H']),
'3.2':(2,['3.0|h|quadrat frame|H']),
'3.3':(1,['3.0|e|quadrat|H']),
'3.4':(1,['3.0|e|quadrat|H']),
'3.5':(2,['3.0|e|quadrat|H']),
'3.6':(2,['3.1|e|gridded quadrat|H','3.2|e|point quadrat|H','1.3|h|random coordinate grid|H']),
'4.0':(2,['3.0|h|quadrat|H']),
'4.1':(1,['4.0|e|percentage frequency|H']),
'4.2':(1,['4.0|e|percentage frequency|H']),
'4.3':(1,['4.0|e|percentage frequency|H','3.0|h|quadrat size|H']),
'4.4':(1,['4.0|e|percentage frequency|H']),
'4.5':(1,['4.0|e|frequency formula|H','4.4|e|sample data|H']),
'4.6':(1,['4.5|h|results to plot|H']),
'5.1':(2,['3.1|e|gridded quadrat|H']),
'5.2':(2,['5.1|e|gridded cover method|H']),
'5.3':(2,['3.2|e|point quadrat hits|H']),
'5.4':(2,['5.3|e|point-quadrat cover formula|H']),
'5.5':(1,['5.4|e|sample data|H']),
'5.6':(2,['5.3|h|pin hits on layers|L']),
'5.7':(1,['5.1|h|grid method|H','5.3|h|point method|H']),
'5.0':(1,[]),
'6.0':(2,['3.0|h|quadrat counts|H']),
'6.1':(1,['6.0|e|density|H']),
'6.2':(1,[]),
'6.3':(1,['6.0|e|density formula|H']),
'6.4':(1,['6.3|e|sample data|H','6.0|e|density formula|H']),
'6.5':(1,['6.1|e|population estimate formula|H','6.2|h|habitat area|H']),
'6.6':(1,['6.0|h|counting individuals|H','5.0|h|percentage cover alternative|H']),
'7.0':(1,['2.0|h|systematic sampling gradient|H']),
'7.1':(1,['7.b|h|transect|H']),
'7.2':(1,['7.1|e|rope laid out|H']),
'7.3':(1,['7.2|e|recording species|H']),
'7.4':(1,['7.2|e|presence at points|H','0.6|h|distribution versus abundance|H']),
'7.5':(1,['2.0|e|systematic sampling|H']),
'7.6':(1,['7.1|h|line transect|H']),
'8.0':(2,['3.0|e|quadrat|H','7.b|h|line transect|H']),
'8.1':(1,['8.0|e|belt transect|H','4.0|h|measures recorded|L']),
'8.2':(1,['bio31-s1.2.2|e|abiotic factors|H']),
'8.3':(1,['8.0|e|belt transect|H','3.0|h|quadrat|H']),
'9.0':(1,['3.0|h|quadrats unsuited to movers|H']),
'9.1':(1,['bio32-s1.4.0|e|pitfall trap|H']),
'9.2':(1,['9.1|h|animals caught|H']),
'9.3':(1,['9.2|e|marked animals|H']),
'9.4':(1,['9.1|e|same capture method|H']),
'9.5':(2,['9.2|e|M marked count|H','9.4|e|C and R counts|H']),
'9.6':(2,['9.5|e|formula N=(M×C)/R|H']),
'9.7':(1,['9.5|e|formula N=(M×C)/R|H']),
'10.0':(2,['9.5|e|formula meaning|H']),
'10.1':(1,['9.4|e|definition of R|H']),
'10.2':(2,['9.5|e|constant population assumption|H']),
'10.3':(2,['9.5|e|random mixing assumption|H']),
'10.4':(1,['9.2|h|marking method|H']),
'10.5':(2,['9.5|e|R in the formula|H']),
'10.6':(1,['bio32-s1.7.0|h|sweep net|L','bio32-s1.4.0|h|pitfall trap|L']),
'11.0':(1,['6.2|h|finding habitat area|H']),
'11.1':(2,[]),
'11.2':(1,['0.0|e|species list|H']),
'11.3':(2,['bio31-s1.2.2|e|abiotic factors|H','8.2|h|measuring abiotic factors|L']),
'11.4':(1,['bio31-s1.2.1|e|biotic factors|H']),
'11.5':(1,['11.4|e|biotic factors|H']),
'11.6':(2,['11.1|h|map and data used|L']),
'11.7':(1,['11.b|h|model meaning|L']),
'12.1':(1,['4.6|h|bar chart of frequency|H']),
'12.2':(1,['7.b|h|transect|H','12.3|h|kite diagram|H']),
'12.3':(2,['12.2|e|abundance along transect|H','7.b|e|transect|H']),
'12.4':(1,['12.3|e|kite diagram|H']),
'13.0':(1,['0.4|h|abundance measures|H']),
'13.2':(1,['13.1|h|areas compared|H']),
'13.3':(1,['4.0|h|frequency measure|L']),
'13.4':(2,['1.2|h|random coordinates|H','3.4|h|same quadrat size|H']),
'13.5':(1,['bio32-s1.2.3|h|no true control|H']),
'13.6':(1,['13.3|h|abundance measures|H']),
'13.7':(2,['13.1|e|hypothesis|H']),
'14.0':(1,['1.1|e|representative sampling|H','1.2|h|random coordinates|H']),
'14.2':(1,['5.7|e|subjective cover estimate|H','3.5|h|edge rules|H']),
'14.3':(1,['bio32-s1.18.1|h|season affects catches|L']),
'14.4':(1,['10.3|e|capture-recapture assumptions|H']),
'14.6':(1,['2.2|h|more samples more reliable|H']),
}
out={};links=low=c2=0
for t in tids:
    suf=t[len(S):]
    cost,needs=D.get(suf,(1,[]))
    ns=[]
    for n in needs:
        i,s,w,c=n.split('|')
        if not i.startswith('bio'): i=S+i
        assert i in allids and i!=t and len(w.split())<=8,(t,i)
        ns.append({"id":i,"strength":{'e':'essential','h':'helpful'}[s],"why":w,"confidence":{'H':'high','L':'low'}[c]})
    out[t]={"cost":cost,"needs":ns}
    links+=len(ns);low+=sum(n['confidence']=='low' for n in ns);c2+=cost==2
json.dump(out,open('/Users/gabrielwhelan/barebones/drafts/crunch/biology/point-links/bio32-s2.json','w'),indent=1,ensure_ascii=False)
chk=json.load(open('/Users/gabrielwhelan/barebones/drafts/crunch/biology/point-links/bio32-s2.json'))
assert list(chk)==tids and len(set(tids))==len(tids)
print(len(tids),links,c2,low)
