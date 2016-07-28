# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 12:58:23 2016

@author: PBallant
"""

import turtle
import scipy

t = turtle.Pen()
t.speed(0)


t.up
for x in range(360):
    angle = scipy.rand(1)
    angle = angle[0]*365
    dist = scipy.rand(1)
    dist = dist[0]*10
    
    if x%2 ==0:
        t.color('green')
        t.forward(dist)
        t.right(angle)
    else:
        t.color('blue')
        t.forward(2*x)
        t.left(x)
