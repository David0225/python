# -*- coding: utf-8 -*-
"""
Created on Mon Dec 25 11:38:55 2017

@author: wuzw
"""
import nltk

nltk.download()


from nltk.book import *

text1.concordance('monstrous')

text1.similar("monstrous")

text4.dispersion_plot(["citizens", "democracy", "freedom", "duties", "America"])

text3.generate()

len(text3)

print(type(sorted(set(text3))))


from __future__ import division
len(text3)/len(set(text3))

text1.count("monstrous")

text5.count("lol")

print(type(text1))

text5.count("lol")*100/len(text5)

help(text1)

dicttext = text1.__dict__
print(type(dicttext))

print(type(sent1))
sent2

ex1 = ["test1","test2","test","test"]
len(ex1)
ex1.count("test2")
print(type(ex1))

print(type(text1))

text1.count("the")

text1.index("call")



try:
    sent1.index('call')
except:
    print('11111')


