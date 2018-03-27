# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 11:02:19 2018

@author: wuzw
"""

import numpy as np
from numpy import arange

jin=['近','斤','今','金','尽']
jin_per = [0.3,0.2,0.1,0.06,0.03]

jintian=['天','填','田','甜','添']
jintian_per=[
    [0.001,0.001,0.001,0.001,0.001],
    [0.001,0.001,0.001,0.001,0.001],
    [0.990,0.001,0.001,0.001,0.001],
    [0.002,0.001,0.850,0.001,0.001],
    [0.001,0.001,0.001,0.001,0.001]
        ]

wo = ['我','窝','喔','握','卧']
wo_per=[0.400,0.150,0.090,0.050,0.030]

women=['们','门','闷','焖','扪']
women_per=[
    [0.970,0.001,0.003,0.001,0.001],
    [0.001,0.001,0.001,0.001,0.001],
    [0.001,0.001,0.001,0.001,0.001],
    [0.001,0.001,0.001,0.001,0.001],
    [0.001,0.001,0.001,0.001,0.001],
    [0.001,0.001,0.001,0.001,0.001],
        ]

N=5

def found_from_oneword(oneword_per):
    index=[]
    values=[]
    a=np.array(oneword_per)
    for v in np.argsort(a)[::-1][:N]:
        index.append(v)
        values.append(oneword_per[v])
    return index,values

def found_from_twoword(oneword_per,twoword_per):
    last=0
    for i in range(len(oneword_per)):
        current=np.multiply(oneword_per[i],twoword_per[i])
        if i==0:
            last=current
#            print(last)
        else:
            last=np.concatenate((last,current),axis=0)
    
    index=[]
    values=[]
    for v in np.argsort(last)[::-1][:N]:
        index.append([int(v/5),v%5])
        values.append(last[v])
    
#    print(index,values)
    return index,values

def predict(word):
    if word=='jin':
        for i in found_from_oneword(jin_per)[0]:
            print(jin[i])
    elif word=='jintian':
        for i in found_from_twoword(jin_per,jintian_per)[0]:
            print(jin[i[0]]+jintian[i[1]])
    elif word=='wo':
        for i in found_from_oneword(wo_per)[0]:
            print(wo[i])
    elif word=='women':
        for i in found_from_twoword(wo_per,women_per)[0]:
            print(i)
            print(wo[i[0]]+women[i[1]])
    else:
        pass
    

predict('women')
