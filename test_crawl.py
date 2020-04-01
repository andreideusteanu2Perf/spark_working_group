# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 14:26:54 2020

@author: bankai
"""

from bs4 import BeautifulSoup
import requests as r
import pandas as pd       
    
"""https://www.meetup.com/find/tech/?pageToken=default%7C100&allMeetups=false
&keywords=&radius=Infinity
&userFreeform=Bucharest%2C+Romania&mcId=&mcName=Bucharest%2C+RO&lat=44.435394
&lon=26.103302&sort=default&__fragment=simple_search&op="""
"""
https://www.meetup.com/find/tech/?pageToken=default%7C200&allMeetups=false
&keywords=&radius=Infinity&userFreeform=Bucharest%2C+Romania&mcId=
&mcName=Bucharest%2C+RO&lat=44.435394&lon=26.103302&sort=default&__fragment=simple_search&op=
"""


urlList=['https://www.meetup.com/find/tech/?pageToken=default%7C100&radius=Infinity'
            ,'https://www.meetup.com/find/tech/?pageToken=default%7C200&radius=Infinity']

linksFull=list()

for url in urlList:

    data=r.get(url).text
    
    soup=BeautifulSoup(data)
    
    linksList=list()
    for link in soup.find_all('a',{"class":"groupCard--photo loading nametag-photo"}):
        linksList.append(link.get('href'))
        
    linksFull.extend(linksList)
    
links=pd.Series(linksFull)
links=pd.Series(links.unique())
