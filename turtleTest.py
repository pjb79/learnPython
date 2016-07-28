# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 12:58:23 2016

@author: PBallant
"""

import turtle

t = turtle.Pen()
t.speed(0)

for x in range(360):
    if x%2 ==0:
        t.color('green')
        t.forward(x)
        t.right(2*x)
    else:
        t.color('blue')
        t.forward(2*x)
        t.left(x)
