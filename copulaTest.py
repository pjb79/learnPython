# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 21:43:04 2016

@author: pjbca
"""

import numpy as np
import scipy as sp
from scipy import stats

mu = np.array([0.05,0.08]);
sigma = np.array([0.07,0.18])

rhoMat = np.array([[1,0.9],[0.9,1]])
cholMat = sp.linalg.cholesky(rhoMat).T


z1=sp.randn(5000,2)
z1 = np.dot(cholMat, z1.T).T

u = np.zeros([5000,2])
for c in range(0,z1.shape[1]):
    for r in range(0,z1.shape[0]):    
        u[r,c] = stats.percentileofscore(z1[:,c],z1[r,c],kind='weak')/100
        
        
z2 = z1.copy

z2[:,0] = stats.lognorm.ppf(Z1[:,0])