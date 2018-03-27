# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 17:59:22 2018

@author: wuzw
"""

#import psycopg2
from sqlalchemy import create_engine
#import pymssql
import pandas as pd
import io

#方法一：使用Pandas库的to_sql方法，但是效率太差
def sqlserverinsert(data):
    
#    conn=pymssql.connect(host='10.99.66.46',user='david',password='life@1234',database='LifeVc.com',charset='GBK')
#    conn=pymssql.connect(host=ip,user=user,password=password,database=database,charset=charset)
    engine = create_engine('mssql+pymssql://david:life@1234@10.99.66.46/LifeVc.com')
    
    data.to_sql('logcheck', engine, if_exists='append',index=False, chunksize=10000)
    

def outsql(data_Out):
    #把Dataframe导入sqlserver数据库
    engine = create_engine('mssql+pymssql://david:life@1234@10.99.66.46/LifeVc.com') #create_engine说明：dialect[+driver]://user:password@host/dbname[?key=value..]
#    print(data_Out)
    
#    print('test3333')
    #创建一个内存文件
    output = io.StringIO()
    
#    print(output.readline())
    
    # ignore the index  
    data_Out.to_csv(output, sep='\t',index = False, header = False)  
    output.getvalue()
    # jump to start of stream  
    output.seek(0)
      
    connection = engine.raw_connection() #engine 是 from sqlalchemy import create_engine  
    cursor = connection.cursor()
    # null value become ''
#    print('test1111')
    cursor.copy_from(output,'logcheck',null='',sep='\t')
#    print('test1112')
    connection.commit()
    cursor.close()


def pgselect():
    engine = create_engine('postgresql://postgres:123456@10.99.66.86:5432/postgres') #create_engine说明：dialect[+driver]://user:password@host/dbname[?key=value..]
    
    sql_cmd = 'select "TracerId" from logcheck'
    data = pd.read_sql(sql_cmd,engine)
    
    return data

data = pgselect()

sqlserverinsert(data)

outsql(data)
