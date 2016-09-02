# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 16:21:50 2016

@author: PBallant
"""
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs

url = 'http://www.asx.com.au/asx/markets/priceLookup.do?by=asxCodes&asxCodes=CBA'
site = urlopen(url)
soup = bs(urlopen(url),'html.parser')

lastPrice = float(soup.find_all('td', class_='last')[0].string)

url = 'http://www.asx.com.au/asx/statistics/indexInfo.do'
site = urlopen(url)
soup = bs(urlopen(url),'html.parser')

t = soup.find_all('td', text = 'XJO')
indexVal = t[0].find_next('td').string
indexVal = float(indexVal.replace(',',''))