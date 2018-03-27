# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 14:47:47 2018

@author: wuzw
"""

import feedparser
import re


def getwordcounts(url):
    d=feedparser.parse(url)
    wc={}
    
    for e in d.entries:
        if 'summary' in e: summary=e.summary
        else:summary=e.description
        
        words=getwords(e.title+' '+summary)
        for word in words:
            wc.setdefault(word,0)
            wc[word]+=1
    return d.feed.title,wc

def getwords(html):
    txt=re.compile(r'<[^>]+>').sub('',html)
    
    words=re.compile(r'[^A-Z^a-z]+').split(txt)
    
    return [word.lower() for word in words if word != '']

apcount={}
wordcounts={}

#读取文本
def read_txt(path):
    with open(path, 'r', encoding='utf8') as f:
        lines = f.readlines()
    return lines

#写入文本
import codecs
def writetxt(path, content, code):
    with codecs.open(path, 'a', encoding=code)as f:
        f.write(content)
    return path+' is ok!'
#read_txt(r'D:\python\comm\feedlist.txt')

feedlist=[line for line in read_txt(r'D:\python\comm\feedlist.txt')]
for feedurl in feedlist:
  try:
    title,wc=getwordcounts(feedurl)
    wordcounts[title]=wc
    for word,count in wc.items():
      apcount.setdefault(word,0)
      if count>1:
        apcount[word]+=1
  except:
    print('Failed to parse feed %s' % feedurl)

wordlist=[]
for w,bc in apcount.items():
  frac=float(bc)/len(feedlist)
  if frac>0.1 and frac<0.5:
    wordlist.append(w)

out=read_txt('blogdata1.txt','w')
out.write('Blog')
for word in wordlist: out.write('\t%s' % word)
out.write('\n')
for blog,wc in wordcounts.items():
  print(blog)
  out.write(blog)
  for word in wordlist:
    if word in wc: out.write('\t%d' % wc[word])
    else: out.write('\t0')
  out.write('\n')