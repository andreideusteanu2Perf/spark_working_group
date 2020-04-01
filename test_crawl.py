# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 14:26:54 2020

@author: bankai
"""

from bs4 import BeautifulSoup
import requests as r
import pandas as pd 
"""

"""
    
urlList=['https://www.meetup.com/find/tech/?pageToken=default%7C'+str(i*100)+'&radius=Infinity'
         for i in range(1,11)]

meetupLinksFull=list()

for url in urlList:

    data=r.get(url).text
    
    soup=BeautifulSoup(data)
    
    meetupLinksList=list()
    for link in soup.find_all('a',{"class":"groupCard--photo loading nametag-photo"}):
        meetupLinksList.append(link.get('href'))
        
    meetupLinksFull.extend(meetupLinksList)
     
meetupsByCountry=list()

for eventUrl in meetupLinksFull:
    
    data=r.get(eventUrl).text

    soup=BeautifulSoup(data)
    
    meetupCityLink=soup.find('a',{'class':'groupHomeHeaderInfo-cityLink'}).get('href')
    meetupCountryCode=meetupCityLink.split('cities/')[1].split('/')[0]
    
    meetupsByCountry.append({'CountryCode':meetupCountryCode,'EventUrls':eventUrl})
    
dataMeetupsByCountry=pd.DataFrame.from_dict(meetupsByCountry)

techMeeetupsFile='D:\\DataWork\\techMeetups.csv'

dataMeetupsByCountry.to_csv(techMeeetupsFile,index=False)
 
relevantMeetups=dataMeetupsByCountry.query('CountryCode in ["us","gb","ca","au","nz"]')

   
eventLinksFull=list()
for meetupUrl in relevantMeetups['EventUrls']:
    data=r.get(meetupUrl+'events/past').text
    
    soup=BeautifulSoup(data)
    
    eventLinksList=list()
    for link in soup.find_all('a',{"class":"eventCard--link"}):
        eventLinksList.append(link.get('href'))
    
    eventLinksFull.extend(eventLinksList)
    
eventLinksFile='D:\\DataWork\\eventLinks.csv'
dataEventLinks=pd.DataFrame(eventLinksFull)
dataEventLinks.to_csv(eventLinksFile,index=False)

 
    
eventDescriptions={}
for eventUrl in eventLinksFull:
    data=r.get('https://www.meetup.com/'+eventUrl).text
    
    soup=BeautifulSoup(data)
    
    descriptionEl=(soup
                 .find('div',{'class':'event-description runningText'})
                 )
    
    if descriptionEl:
        description=descriptionEl.get_text(strip=True)
    eventDescriptions={'Event':eventUrl,'description':description}


dataEventDescriptions=pd.DataFrame(eventDescriptions,index=[0])

jsonFile='D:\\DataWork\\meetupEventsDescriptions.json'

dataEventDescriptions.to_json(jsonFile,orient='records',lines=True)
