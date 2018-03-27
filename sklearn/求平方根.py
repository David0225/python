# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 08:57:35 2018

@author: wuzw
"""

def sqrt(x):
    y = 1.0
    while abs(y*y-x) >1e-6:
        y = (y+x/y)/2
    return y

sqrt(0.1)

print('test')
