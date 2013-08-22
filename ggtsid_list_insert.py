#! c:/Python26/python.exe
# coding: utf-8 

from pymongo import Connection #@UnresolvedImport
from BeautifulSoup import BeautifulSoup #@UnresolvedImport
import urllib

def ggtsidlist_make():
    soup = BeautifulSoup(urllib.urlopen("http://www.google.com/intl/ja/+/project48/").read())
    lisoup=[]
    ggtsidlist = []
    for lisoup in soup.findAll("li"):
    
        try:
            ggtsidlist.append(lisoup['data-gplusid'])
        except:
            continue
    ggtsidlist.append(u'113474433041552257864') #やすす
    ggtsidlist.append(u'108897254135232129896') #よすす
    ggtsidlist.append(u'112435502021367429566') #しのぶ
    ggtsidlist.append(u'113091703821013997975') #木島
    ggtsidlist.append(u'103803814106571203433') #北川 
    ggtsidlist.append(u'105988904423141811436') #AKB Cafe&Shop
    ggtsidlist.append(u'106112762361092739156') #Nottv プロデューサー

    
    return ggtsidlist

if __name__=='__main__':
    con = Connection()
    ggts = con[u'ggts']
    con.ggts.ggtsid.remove()
    record = {}
    ggtsidlist = ggtsidlist_make()
    count = 0
    for ggtsid in ggtsidlist:
        record = {u'ggtsid':ggtsid,u'_id':ggtsid}
        print record 
        con.ggts.ggtsid.insert(record)
        count += 1
    print count
        