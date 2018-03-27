# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 14:30:02 2018

@author: wuzw
"""

from sklearn.naive_bayes import GaussianNB
import numpy as np

data_table=[["data",'weather'],[1,0],[2,1],[3,2],[4,1],[5,2],[6,0],[7,0],[8,3],[9,1],[10,1]]

x=[]
#data_table[1:5,1]
#
#a=np.array(data_table,dtype=int)
#a[1:,1:2]
#
#b=a[:,1:2]

def printlist(listin):
    for i in listin[1:]:
        print(i)
        if isinstance(i,list):
            printlist(i)
        else:
            z=[]
            z.append(i)
            x.append(z)

printlist(data_table)

#x=[[0],[1],[2],[1],[2],[0],[0],[3],[1]]
y=[1,2,1,2,0,0,3,1,1]

clf=GaussianNB().fit(x,y)

p=[[1]]
print(clf.predict(p))
