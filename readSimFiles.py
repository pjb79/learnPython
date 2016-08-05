# -*- coding: utf-8 -*-
"""
Created on Fri Aug  5 20:22:17 2016

@author: pjbca
"""

import cntl_manager as cm
import sim_manager as sm
import numpy as np

simNames, vlm = cm.readCntlFile("n:/my documents/russell/cntl_ANZ_placemat.xlsx")

simMatrix = np.empty((0,600,5000))

for v in vlm:
    
    simMatrix = np.concatenate([simMatrix, sm.getSimData(v,vlm)],axis=0)

