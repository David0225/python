# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 11:38:51 2018

@author: wuzw
"""
from sklearn.datasets import load_iris
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns



from sklearn.model_selection import train_test_split

iris_data =load_iris()
iris_data.keys()

iris_df = pd.DataFrame(iris_data['data'],columns=iris_data.feature_names)
iris_df['Target'] = pd.DataFrame(iris_data['target'],columns=['Target'])
iris_df['Target_name'] = pd.DataFrame(iris_df['Target']).apply(lambda x:iris_data['target_names'][x])

iris_df.sample(5)

iris_data['target_names']

pd.DataFrame(iris_df['Target'])