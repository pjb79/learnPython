# -*- coding: utf-8 -*-
"""
Created on Thu Aug  4 12:33:14 2016

@author: PBallant
"""

import numpy as np
import scipy as sp
from scipy import stats
import matplotlib as plt
import math

corrMat = np.array([[1,-0.3],[-0.3,1]])
cholMat = sp.linalg.cholesky(corrMat)
cholMat = cholMat.T

z = sp.randn(10000,2)
z = np.dot(cholMat,z.T).T

u = np.zeros(z.shape)*np.nan

for c in range(0,z.shape[1]):
    for r in range(0,z.shape[0]):
        u[r,c] = min(stats.percentileofscore(z[:,c],z[r,c], kind = "weak")/100,0.9999999999)


empCorr = np.corrcoef(u.T)        
#plt.pyplot.hist(u[:,1],100)

lnDist = stats.lognorm(s = 0.2, scale = math.exp(0.1))
u[:,0] = lnDist.ppf(u[:,0])-1

betaDist = stats.beta(a = 0.5, b = 0.5)
u[:,1] = betaDist.ppf(u[:,1])

#fig = plt.figure()
plt.pyplot.scatter(u[:,0],u[:,1])
empCorr = np.corrcoef(u.T)   

