# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 16:44:36 2018

@author: wuzw
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


X=[]
f=open('City.txt',encoding='utf-8')
for v in f:
    X.append([float(v.split(',')[2]),float(v.split(',')[3])])


X=np.array(X)

n_clusters=5

cls=KMeans(n_clusters).fit(X)

cls.labels_


markers = ['^','x','o','*','+']

for i in range(n_clusters):
    members=cls.labels_==i
#    print(members)
    print(X[members,0])
    plt.scatter(X[members,0],X[members,1],s=60,marker=markers[i],c='b',alpha=0.5)
    
plt.title('')
plt.show()
