# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 11:19:22 2018

@author: wuzw
"""

from sklearn import svm

#年龄
X=[[34],[33],[32],[31],[30],[30],[25],[23],[22],[18]]
#质量
y=[1,0,1,0,1,1,0,1,0,1]

#把训练集数据和对应的分类放入分类器中进行训练
#使用rbf
clf=svm.SVC(kernel='rbf').fit(X,y)

p=[[25]]
print(clf.predict(p))