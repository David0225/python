# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 10:57:09 2018

@author: wuzw
"""
import numpy as np
import matplotlib.pyplot as plt

x=[1,2,3,4,5,6,7,8,9]
y=[0.199,0.389,0.580,0.783,0.980,1.177,1.380,1.575,1.771]
#x=[11,23,34,45,56,67,78,89,90]
#y=[0.199,0.589,0.780,0.683,0.980,1.877,1.980,1.575,1.771]


A=np.vstack([x,np.ones(len(x))]).T

#调用最小二乘法函数
a,b=np.linalg.lstsq(A,y)[0]

#转换成numpy array
x=np.array(x)
y=np.array(y)

plt.plot(x,y,'o',label='Original data',markersize=10)
plt.plot(x,a*x+b,'r',label='Fitted line')
plt.show()