# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 13:22:14 2016

@author: PBallant
"""

import numpy as np
import h5py


f = h5py.File('C:\\bin\\test.mat',"r")

simMatrix = np.array(f['simMatrix'])
simMatrix = np.transpose(simMatrix,(2,1,0))


 

   

