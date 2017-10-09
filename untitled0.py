# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 13:10:43 2017

@author: PBallant
"""

import sys  
from pyqt.QtGui import *  
from pyqt.QtCore import *  
from pyqt.QtWebKit import *  
from lxml import html 

#Take this class for granted.Just use result of rendering.
class Render(QWebPage):  
  def __init__(self, url):  
    self.app = QApplication(sys.argv)  
    QWebPage.__init__(self)  
    self.loadFinished.connect(self._loadFinished)  
    self.mainFrame().load(QUrl(url))  
    self.app.exec_()  
  
  def _loadFinished(self, result):  
    self.frame = self.mainFrame()  
    self.app.quit()  

url = 'http://www.asx.com.au/asx/share-price-research/company/BHP'  
r = Render(url)  
result = r.frame.toHtml()
#This step is important.Converting QString to Ascii for lxml to process
#archive_links = html.fromstring(str(result.toAscii()))
#print archive_links