# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 21:13:48 2016

@author: pjbca
"""

import numpy as np
import h5py


f = h5py.File('N:\\My Documents\\Russell\\bin\\aud_aeif.mat',"r")

simMatrix = f['simMatrix'].regionref[:,:,0]
 