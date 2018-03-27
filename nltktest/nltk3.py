# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 13:42:18 2018

@author: wuzw
"""

from nltk.corpus import gutenberg

f = gutenberg.fileids()

print(f)

emma = gutenberg.words('austen-emma.txt')
gutenberg.sents('austen-emma.txt')
gutenberg.words('austen-emma.txt')
gutenberg.raw('austen-emma.txt')

print(emma)

for e in emma:
    print(e)

for fileid in gutenberg.fileids():
    num_chars = len(gutenberg.raw(fileid))
    num_words = len(gutenberg.words(fileid))
    num_sents = len(gutenberg.sents(fileid))
    num_vocab = len(set([w.lower() for w in gutenberg.words(fileid)]))
    
    print(int(num_chars/num_words),int(num_words/num_sents),int(num_words/num_vocab),fileid)


from nltk.corpus import webtext
import nltk
for fileid in webtext.fileids():
    print(fileid,webtext.raw(fileid)[:65])
    print(type(webtext.words(fileid)))
    
from nltk.corpus import brown
brown.categories()

t = brown.words(categories='news')
print(t)

fdist = nltk.FreqDist([w.lower() for w in t])
fdist1 = nltk.FreqDist(t)
print(type(fdist))
print(fdist)
print(fdist1['May'])

for f in fdist.items():
    print(f)

cfd = nltk.ConditionalFreqDist((genre,word)
                                for genre in brown.categories()
                                for word in brown.words(categories = genre)
)

genres = ['news', 'religion', 'hobbies', 'science_fiction', 'romance', 'humor']
genres = brown.categories()
modals = ['can', 'could', 'may', 'might', 'must', 'will']

cfd.tabulate(conditions=genres,samples=modals)

cfd.plot()
