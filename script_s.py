# web scrapping code made by Rishabh Bhardwaj
# follow me at http://www.knoobypie.com/about-me/
# folow me on linkedin @https://www.linkedin.com/in/rishabh-bhardwaj-791903171/
# github https://github.com/rishabh3354

# <<<<<<<<-pre-requestie->>>>>>>>>>>>>>>>
# install the following python module:
# pip install requests
# pip install bs4
# output will be in html format, Recommended to save file in html format


import requests
from bs4 import BeautifulSoup
import sys
import pandas as pd
import os

def getschools():

    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'}

    soup = BeautifulSoup(open("school.htm"))
    mm = str(soup)

    c = mm.count("<div>")
    pos = 0

    mydata = ""

    mydata = soup.find_all("a", class_="links fl")
    #print(mydata+'print')

    #cleantext = BeautifulSoup(mydata, "html.parser")
    #cleantext=cleantext.get_text()
    sys.stdout.flush()
    print(mydata)

    school_nr = []
    for repElem in mydata:
        print("Processing repElem...")
        repElemName = repElem.get('href')
        school_nr.append(repElemName[-6:])
        print("Attribute name = %s" % repElemName)

    return school_nr
    #return re.split(r'',mydata,flag=re.IGNORECASE,maxsplit=)


if __name__ == '__main__':
    url = ""
    # sys.stdout.flush()
    dir = os.getcwd()
    print("-----------------------------------------------")
    print(dir)
    getdata = getschools()

    res = pd.DataFrame(getdata)
    res.rename(columns={0:'Schulnummer'}, inplace=True)
    print(res.head())
    res['Schulnummer']= pd.to_numeric(res['Schulnummer'])
    df = pd.read_csv('schuldaten.csv', sep=';')
    res= res.join(df.set_index('Schulnummer'), on='Schulnummer')
    res = res[['PLZ','Ort','Strasse']]
    print(res.Ort.value_counts())
    res = res.Ort.value_counts()
    print(res.to_string())
    # sys.stdout.flush()