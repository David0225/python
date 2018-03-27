# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 15:24:50 2018

@author: wuzw
"""

from nltk.corpus import inaugural
from nltk.corpus import reuters
import nltk

inaugural.fileids()


reuters.categories('test/16574')
reuters.fileids('earn')[1000:1100]
reuters.words('test/16574')
[fileid[:4] for fileid in inaugural.fileids()]

inaugural.fileids()

file = [fileid[:4] for fileid in inaugural.fileids()]

print(file)

print(type(inaugural.fileids()))

for fileid in inaugural.fileids():
    print(fileid)
    for w in inaugural.words(fileid):
        print(w)

cfd = nltk.ConditionalFreqDist(
        (target,fileid[:4])
        for fileid in inaugural.fileids()
        for w in inaugural.words(fileid)
        for target in ['america','citizen']
        if w.lower().startswith(target)
        )
cfd.plot()
print(cfd.items())

from nltk.corpus import udhr
udhr.fileids()
ch = udhr.words('Chinese_Mandarin-GB2312')

nltk.FreqDist(ch).plot()

ch = nltk.ConditionalFreqDist(
            (lang,len(word))
            for lang in (['Chinese_Mandarin-GB2312'])
            for word in udhr.words('Chinese_Mandarin-GB2312')
        )

ch.plot(cumulative = True)

fdistch = nltk.FreqDist(ch)

import operator
d = sorted(fdistch.items(),key = operator.itemgetter(1),reverse=True)
print(d)
