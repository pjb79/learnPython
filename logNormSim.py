# -*- coding: utf-8 -*-
"""
Created on Mon Aug  1 20:57:49 2016

@author: pjbca
"""
import numpy as np
import scipy as sp
from matplotlib import pyplot as plt


mu = np.array([0.05,0.08]);
sigma = np.array([0.07,0.18])

rho = 0.95

z = sp.randn(50000,2)
z[:,1] = rho*z[:,0]+sp.sqrt(1-rho**2)*z[:,1]

z = sp.exp(sp.log(1+mu) -0.5*sigma**2 + sigma *z)-1;

#plt.hist(z[:,0],100)

plt.scatter(z[:,0],z[:,1])

m = np.mean(z,0)

m1=np.tile(m,[1,20])

rhoMat = np.array([[1,0.9,0.5],[0.9,1,0.3],[0.5,0.3,1]])

cholMat = sp.linalg.cholesky(rhoMat).T

z1=sp.randn(5000,3)
z1corr = np.dot(cholMat, z1.T).T

c = np.corrcoef(z1corr.T)


