# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 15:37:06 2018

@author: wuzw
"""
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd

iris_data = load_iris()
iris_data.keys()

X_train,X_test,y_train,y_test = train_test_split(iris_data['data'],iris_data['target'],random_state=0)
list(map(len,[X_train,X_test,y_train,y_test]))

print(y_train)
print(X_train)

from sklearn.neighbors import KNeighborsClassifier

knn=KNeighborsClassifier(n_neighbors=1)
knn.fit(X_train,y_train)
y_pred = knn.predict(X_test)
print(y_pred)
knn.score(X_test,y_test)

def diff_k(s,k):
    knn=KNeighborsClassifier(n_neighbors=k)
    X_train,X_test,y_train,y_test=train_test_split(iris_data['data'],iris_data['target'],test_size=s,random_state=0)
    knn.fit(X_train,y_train)
    y_pred=knn.predict(X_test)
    #print('k={},s={},score={}'.format(k,s,np.mean(y_pred==y_test)))
    print('k={},s={},score={}'.format(k,s,knn.score(X_test,y_test)))
    
sizes=[0.1,0.2,0.3,0.4,0.5]
neighbirs=[1,2,3,4,5]
for s in sizes:
    for k in neighbirs:
        diff_k(s,k)
        
iris_df = pd.DataFrame(iris_data['data'],columns=iris_data.feature_names)
iris_df['Target'] = pd.DataFrame(iris_data['target'],columns=['Target'])
iris_df['Target_name'] = pd.DataFrame(iris_df['Target']).apply(lambda x:iris_data['target_names'][x])

iris_df.iloc[2]

print(iris_df)

X_new = np.array([[6.3,2.5,5,1.9]])
X_new = np.array([[4.7,3.2,1.3,0.2]])
knn.predict(X_new)

iris_data['data']
iris_data['target']
