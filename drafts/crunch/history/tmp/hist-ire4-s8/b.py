import json,re,sys
H='/Users/gabrielwhelan/barebones/drafts/crunch/history/'
def L(i,s,w,c='high'): return {"id":i,"strength":s,"why":w,"confidence":c}
def build(pre,data,pack,out):
    txt=open(H+'packs/'+pack).read()
    tgt=[];allids=set()
    sec=None
    for ln in txt.split('\n'):
        if ln.startswith('TARGET'): sec='t'
        elif ln.startswith('CANDIDATES'): sec='c'
        m=re.match(r'\[(\S+?)\]',ln)
        if m:
            allids.add(m.group(1))
            if sec=='t': tgt.append(m.group(1))
    assert set(data)=={pre+k for k in data} or True
    d={pre+k:v for k,v in data.items()}
    assert list(d)==tgt,(set(tgt)-set(d),set(d)-set(tgt))
    res={};n=0;c2=0;lo=0
    for k,(c,needs) in d.items():
        for x in needs: assert x['id'] in allids and x['id']!=k,x
        res[k]={"cost":c,"needs":needs};n+=len(needs);c2+=c==2;lo+=sum(x['confidence']=='low' for x in needs)
    json.dump(res,open(H+'point-links/'+out,'w'),indent=1)
    json.load(open(H+'point-links/'+out))
    print(pack,len(res),n,c2,lo)
p='hist-ire4-s8.'
A={
'0.b':(1,[L(p+'0.0','helpful','stage Irishman stereotype')]),
'0.0':(1,[]),
'0.1':(2,[L(p+'0.0','essential','uses the stage Irishman')]),
'0.2':(2,[]),
'0.3':(1,[L(p+'0.2','helpful','John Ford as director')]),
'0.4':(1,[]),'0.5':(1,[]),'0.6':(1,[]),'0.7':(1,[]),
'1.b':(1,[]),
'1.0':(2,[L(p+'0.2','helpful','John Ford'),L(p+'2.b','helpful','Maureen O\'Hara')]),
'1.1':(1,[L(p+'1.0','helpful','the film The Quiet Man')]),
'1.2':(1,[L(p+'0.2','helpful','Ford as director')]),
'1.3':(1,[L(p+'1.1','helpful','Cong filming locations')]),
'1.4':(1,[L(p+'0.0','helpful','comic drunken stereotype')]),
'1.5':(1,[L(p+'1.3','helpful','visitors drawn by film locations')]),
'1.6':(1,[L(p+'4.0','helpful','the tourist board'),L('hist-ire4-s2.6.3','helpful','mass emigration in the 1950s')]),
'2.b':(1,[]),'2.0':(1,[]),'2.1':(1,[]),'2.2':(1,[]),
'2.3':(2,[L(p+'0.2','helpful','John Ford')]),
'2.4':(1,[]),
'2.5':(1,[L(p+'0.0','helpful','screen Irish stereotypes','low')]),
'2.6':(1,[]),
'3.b':(1,[]),
'3.0':(2,[]),'3.1':(1,[]),
'3.2':(1,[L(p+'3.1','helpful','McCormack as a tenor')]),
'3.3':(1,[]),'3.4':(1,[]),'3.5':(2,[]),'3.6':(2,[]),
'4.b':(1,[]),'4.0':(1,[]),'4.1':(1,[]),'4.2':(1,[]),
'4.3':(1,[L(p+'4.2','helpful','Shannon Airport')]),
'4.4':(1,[]),'4.5':(1,[]),
'4.6':(1,[L(p+'4.5','helpful','heritage tourism')]),
'4.7':(1,[L('hist-ire4-s2.6.6','helpful','late-1950s economic planning')]),
'5.0':(1,[]),'5.1':(1,[]),'5.2':(1,[]),'5.3':(1,[]),'5.4':(1,[]),
'6.b':(1,[]),
'6.0':(2,[L('hist-ire4-s2.0.b','helpful','emigration after the Famine')]),
'6.1':(2,[L('hist-ire4-s3.3.5','essential','Al Smith 1928 defeat')]),
'6.2':(1,[]),'6.3':(1,[]),
'6.4':(1,[L(p+'6.2','helpful','the 1963 visit')]),
'6.5':(1,[L(p+'6.0','helpful','Kennedy\'s Irish ancestry')]),
'6.6':(1,[]),
'6.7':(1,[L('hist-ire4-s2.6.6','essential','Lemass government and economic opening')]),
'6.8':(1,[L('hist-ire4-s3.5.b','helpful','Joe Kennedy\'s career')]),
'7.b':(1,[]),'7.0':(1,[]),'7.1':(1,[]),'7.2':(1,[]),'7.3':(1,[]),'7.4':(1,[]),
'8.0':(2,[L(p+'4.b','helpful','tourism attracting visitors','low')]),
'8.1':(2,[L(p+'0.4','helpful','rural Catholic Hollywood image')]),
'8.2':(2,[L(p+'1.4','helpful','Irish critics\' stereotype objections')]),
'8.3':(2,[L(p+'6.7','helpful','Kennedy visit and Lemass confidence','low')]),
'8.4':(2,[L(p+'3.6','helpful','1960s folk revival')]),
}
build(p,A,'hist-ire4-s8.t1g1.txt','hist-ire4-s8.t1g1.json')
q='hist-ire3-s8.'
B={
'0.b':(1,[]),'0.0':(1,[]),'0.1':(1,[]),'0.2':(1,[]),
'0.3':(1,[L('hist-ire3-s6.5.0','essential','Treaty ports returned in 1938')]),
'0.4':(1,[]),'0.5':(1,[]),'0.6':(2,[]),'0.7':(1,[]),
'1.b':(1,[]),
'1.0':(1,[L(q+'0.0','helpful','the Emergency declaration')]),
'1.1':(1,[L(q+'1.0','helpful','emergency powers and censorship')]),
'1.2':(1,[]),'1.3':(1,[]),'1.4':(1,[]),'1.5':(1,[]),'1.6':(1,[]),
'2.b':(1,[]),'2.0':(1,[]),
'2.1':(1,[L(q+'2.0','helpful','army expansion')]),
'2.2':(1,[]),'2.3':(1,[]),
'2.4':(1,[L('hist-ire3-s6.3.4','helpful','IRA banned in 1936')]),
'2.5':(1,[]),
'2.6':(1,[L(q+'2.5','helpful','IRA campaign background')]),
'2.7':(1,[L(q+'2.4','helpful','Offences Against the State Act')]),
'2.8':(1,[]),
'3.b':(1,[]),
'3.0':(1,[L('hist-ire3-s7.4.b','helpful','Lemass as minister')]),
'3.1':(1,[]),'3.2':(1,[]),'3.3':(1,[]),'3.4':(1,[]),'3.5':(1,[]),'3.6':(1,[]),
'3.7':(2,[]),'3.8':(1,[]),
'4.b':(1,[]),
'4.0':(2,[L(q+'0.2','helpful','partition and Northern Ireland')]),
'4.1':(1,[L(q+'4.0','essential','the MacDonald offer')]),
'4.2':(1,[L('hist-ire3-s6.5.0','essential','return of the Treaty ports')]),
'4.3':(1,[L(q+'4.2','helpful','Britain\'s interest in the ports')]),
'4.4':(1,[L(q+'3.b','helpful','wartime supply shortages')]),
'4.5':(1,[]),
'4.6':(2,[L(q+'4.5','helpful','American pressure on neutrality')]),
'4.7':(1,[L(q+'4.6','essential','the American Note')]),
'5.b':(1,[]),'5.0':(1,[]),'5.1':(1,[]),'5.2':(1,[]),'5.3':(1,[]),'5.4':(1,[]),
'5.5':(2,[L(q+'5.4','helpful','German bombing of Ireland')]),
'5.6':(1,[L(q+'5.5','essential','the North Strand bombing')]),
'5.7':(1,[]),
'6.b':(1,[]),'6.0':(1,[]),
'6.1':(1,[L(q+'6.0','helpful','de Valera\'s condolence visit')]),
'6.2':(1,[L(q+'6.0','essential','the Hempel visit')]),
'6.3':(1,[L(q+'0.3','helpful','Churchill and the ports')]),
'6.4':(2,[L(q+'6.3','essential','Churchill\'s victory broadcast')]),
'6.5':(1,[L(q+'6.4','essential','de Valera\'s reply broadcast')]),
'7.b':(1,[]),'7.0':(1,[]),'7.1':(1,[]),'7.2':(1,[]),
'7.3':(1,[L(q+'1.b','helpful','emergency powers and censorship')]),
'7.4':(1,[]),
'7.5':(1,[L(q+'5.3','helpful','Irish serving in British forces')]),
'8.b':(1,[]),'8.0':(1,[]),
'8.1':(1,[L(q+'0.5','helpful','Civil War divisions')]),
'8.2':(1,[L(q+'1.b','helpful','censorship and controls')]),
'8.3':(1,[L(q+'6.b','helpful','isolation at war\'s end','low')]),
'8.4':(1,[L(q+'6.4','helpful','Churchill\'s criticism')]),
'8.5':(2,[]),
}
build(q,B,'hist-ire3-s8.t1g1.txt','hist-ire3-s8.t1g1.json')
