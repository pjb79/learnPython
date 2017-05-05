# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 16:49:11 2017

@author: PBallant
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(10)
y = x
t = np.floor(6*np.random.uniform(low = 0, high = 1, size = 10))
fig, (ax1, ax2) = plt.subplots(1, 2)
ax1.scatter(x, y, c=t, cmap='Accent')
ax2.scatter(x, y, c=t, cmap='Accent_r')
plt.show()