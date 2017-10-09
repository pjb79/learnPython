# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 13:09:38 2017

@author: PBallant
"""

import requests
from bs4 import BeautifulSoup

headers = {"User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 GTB7.1 (.NET CLR 3.5.30729)", "Referer": "http://example.com"}
timeout = 20
proxyDict = {"http" : "http://10.148.78.51:8080", "https" : "http://10.148.78.51:8080"}

request = requests.get("http://www.asx.com.au/asx/share-price-research/company/BHP", headers = headers, proxies = proxyDict)
content = request.content


soup = BeautifulSoup(content, "html.parser")
element = soup.find("span", {"ng-show":"share.last_price"})
stringPrice = element.text.strip()
