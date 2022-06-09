supported = ['alyrics']

import requests
from bs4 import BeautifulSoup
import sys
import pandas as pd
from urllib.parse import urlparse


def getschools(string):

    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'}

    soup = BeautifulSoup(open("bookmarks.html", encoding="utf8"))
    mm = str(soup)
    mydata = soup.find_all("a")

    #for d in range(0,len(mydata)):
    #    if string in mydata[d]:
    #        i = d
    #print(mydata[i])
    #mydata = soup.contents#.find_all("a")
    #print(mydata)

    #cleantext = BeautifulSoup(mydata, "html.parser")
    #cleantext=cleantext.get_text()
    #sys.stdout.flush()
    #print(mydata)

    domains = []
    for repElem in mydata:
        print("Processing repElem...")
        repElemName = repElem.get('href')
        tmp = urlparse(repElemName).netloc
        if(string in tmp ):
            domains.append(tmp)
        print("domain = %s" % repElemName)

    return domains
    #return re.split(r'',mydata,flag=re.IGNORECASE,maxsplit=)


if __name__ == '__main__':
    url = ""
    # sys.stdout.flush()
    
    getdata = getschools("lyrics")

    res = pd.DataFrame(getdata)
    res.rename(columns={0:'url'}, inplace=True)
    print(res.head())
    print(res.url.value_counts())
    res = res.url.value_counts()
    print(res.sort_values(ascending=False).head())
    # sys.stdout.flush()