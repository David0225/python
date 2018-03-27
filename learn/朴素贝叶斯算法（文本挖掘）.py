# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 08:25:31 2018

@author: wuzw
"""
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from pprint import pprint

newsgroups_train = fetch_20newsgroups(subset='train')
pprint(list(newsgroups_train.target_names))

#选取4个主题
categories = ['alt.atheism','comp.graphics','sci.med','soc.religion.christian']

#下载这4个主题里的文件
twenty_train = fetch_20newsgroups(subset='train',categories=categories)


#文件内容在twenty_train.data这个变量里，现在对内容进行分词和向量化操作
count_vect=CountVectorizer()
X_train_counts = count_vect.fit_transform(twenty_train.data)

#接着对向量化之后的结果做TF-IDF转换
tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)

from sklearn.naive_bayes import MultinomialNB

clf = MultinomialNB().fit(X_train_tfidf,twenty_train.target)

docs_new = ['God is love','OpenGL on the GPU is fast']
X_new_counts = count_vect.transform(docs_new)
X_new_tfidf = tfidf_transformer.transform(X_new_counts)

predicted = clf.predict(X_new_tfidf)

 
for doc,category in zip(docs_new,predicted):
    print('%r=>%s'%(doc,twenty_train.target_names[category]))
