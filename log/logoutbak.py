# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 14:32:51 2018

@author: wuzw
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 08:45:24 2018

@author: wuzw
"""

from sqlalchemy import create_engine
import pandas as pd

def fileread(fileurl,method):
    #配置文件路径
#    my_file = open(r'D:\company\日志\cocohub.20180305.131914.404.log','rb')
    my_file = open(fileurl,'rb')
    
    #把文件读进Dataframe
    data = pd.read_csv(my_file,sep='\n',encoding = 'utf8',header = None)
    
    #修改Dataframe的列名
    data.columns = ['logname']
    
    #把数据进行第一次分列
    data_split = pd.DataFrame((x.split('] ') for x in data.logname),index=data.index,columns=['createtime','type','Remark'])
    
    #单独生成createtime列
    data_createtime=data_split['createtime'].str.replace('[','')
    
    #单独生成Type列
    data_type=data_split['type'].str.replace('[','')
    
    #单独生成Remark的Json格式列
    data_Remark_Json=data_split['Remark']
    
    #把所有JSON转为dict存储到一张列表中
    data_list = []
    
    for i in range(len(data_Remark_Json)):
        data_list.append(eval(data_Remark_Json[i]))
    
    #把这张列表转换为dataframe
    data_Remark=pd.DataFrame(data_list)
    
    #整合三个Dataframe，生成最终完整的Dataframe
    data_Final=pd.concat([data_createtime,data_type,data_Remark],axis=1)
    
    filterdata(method,data_Final)
    

def outsql(data_Out):
    #把Dataframe导入postgresql数据库
    engine = create_engine('postgresql://postgres:123456@10.99.66.86:5432/postgres') #create_engine说明：dialect[+driver]://user:password@host/dbname[?key=value..]
    
    try:
#        data_Out.to_sql('logcheck',engine,index=False,if_exists='append',chunksize = 10000)
        pd.io.sql.to_sql(data_Out,'logcheck',engine,index=False,if_exists='append',chunksize = 10000)
    except Exception as e:
        print(e)

def filterdata(method,data_Out):
    if method == 'Total':
        outsql(data_Out)
    #通过列筛选，筛选出特定的行
    else:
        data_OutSplit=data_Out.loc[data_Out['Method']==method]
        outsql(data_OutSplit)


#filterdata('GetAppItemTexts(String, Int32)')
#filterdata('Total')


fileread('D:\company\日志\cocohub.20180305.131914.404.log','Total')
