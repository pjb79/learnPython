# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 13:40:30 2017

@author: PBallant
"""

import matlab.engine as m
import numpy as np
import copy

eng = m.start_matlab()

eng.cd('c:\\d\\f_svn\\dev\\bin - dev\\PB\\', nargout = 0)

netTR = eng.getAUDTRPython('2016-12', 'Class2', 3, 2, 'a', 20, 5000, 4, 'C:\\D\\AA_SVN\\AsiaPac-AA\\PST\\2016\\PST1 Dec 2016 Assumptions\\', 'Common Data Dec 2016.xlsx', 'cntlRussell', nargout = 1)
netTR = np.array(netTR._data, copy = True).reshape(netTR.size, order = 'F')

w = np.zeros([38,1])
w[[0,5],0] = [0.5,0.5]


portRet = np.sum(np.multiply(np.tile(np.expand_dims(w,2),[1,20,5000]),netTR), axis = 0, keepdims = True)




