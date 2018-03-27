# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 17:31:05 2017

@author: wuzw
"""

saying = ['After', 'all','is','said','and','done','more','is','said','than','done']
tokens = set(saying)
tokens = sorted(tokens)
tokens[-2:]

from nltk.book import *

fdist1 = FreqDist(text1)
type(fdist1)

fdist1.N()

fdist1['whale']

for w in text1:
    print(type(w))

vocabulary1 = list(fdist1.keys())
type(vocabulary1)

vocabulary1[:50]
vocabulary1

import operator
d = sorted(fdist1.items(),key = operator.itemgetter(1),reverse=True)

def sortedbyDesc(text):
    print(type(text))
    print(sorted(text.items(),key = operator.itemgetter(1),reverse=True))


sortedbyDesc(fdist5)

d[:50]

V = set(text1)
long_words = [w for w in V if len(w)>15]
sorted(long_words)
long_words


fdist5 = FreqDist(text5)
sorted(w for w in set(text5) if len(w) > 7 and fdist5[w] > 7)

fdist5

text1.collocations()

fdist1.max()
fdist5.tabulate()
fdist5.plot()
fdist5.keys()
fdist5.items()

print([w for w in sent7 if len(w) == 4])
print(type(text1))
text1[1]

textl = list(text1)

print(type(textl))

print(textl)

for w in sent7:
    print(w,w.startswith('t'))
    print(type(w))

tt = 'start'
tt.startswith('s')

babelize_shell()
