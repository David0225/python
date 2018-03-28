# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 17:59:22 2018

@author: wuzw
"""

#import psycopg2
from sqlalchemy import create_engine
import pymssql
import pandas as pd
#import io
import numpy as np
import time

#方法一：使用Pandas库的to_sql方法，但是效率太差(一个字段，8分钟46万)
def sqlserverinsert(data):

    print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    engine = create_engine('mssql+pymssql://david:life@1234@10.99.66.46/LifeVc.com')
    
    data.to_sql('logcheck', engine, if_exists='append',index=False, chunksize=10000)
    print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    
#方法二：直接通过语句导入，效率和Pandas差不多，而且语句比较复杂
def sqlserverinsertV2(data):
    #Dataframe转化为listoftuple
    train_data = np.array(data)
    train_data_list = train_data.tolist()
    
    train_data_list_tuple=[]
    for l in train_data_list:
        train_tuple=tuple((l))
        train_data_list_tuple.append(train_tuple)
    
    #连接sqlserver，并导入表
    conn=pymssql.connect(host='10.99.66.46',user='david',password='life@1234',database='LifeVc.com',charset='GBK')
    cur=conn.cursor()
    
    cur.executemany("insert into logcheck(tracerid,spanid) values (%s,%s)",train_data_list_tuple)
    
    conn.commit()

def pgselect():
    engine = create_engine('postgresql://postgres:123456@10.99.66.86:5432/postgres') #create_engine说明：dialect[+driver]://user:password@host/dbname[?key=value..]
    
    sql_cmd = 'select "TracerId" from logcheck'
    data = pd.read_sql(sql_cmd,engine)
    
    return data

data = pgselect()

sqlserverinsert(data)

sqlserverinsertV2(data)