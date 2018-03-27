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
import io
import pandas as pd
import os

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
    
    #整合三个Dataframe，生成最终完整的Dataframe
    data_Final=pd.concat([data_createtime,data_type,data_Remark_Json],axis=1)
    
    filterdata(method,data_Final)
    

def outsql(data_Out):
    #把Dataframe导入postgresql数据库
    engine = create_engine('postgresql://postgres:123456@10.99.66.86:5432/postgres') #create_engine说明：dialect[+driver]://user:password@host/dbname[?key=value..]

    #创建一个内存文件
    output = io.StringIO()  
    # ignore the index  
    data_Out.to_csv(output, sep='\t',index = False, header = False)  
    output.getvalue()
    # jump to start of stream  
    output.seek(0)
      
    connection = engine.raw_connection() #engine 是 from sqlalchemy import create_engine  
    cursor = connection.cursor()
    # null value become ''
    cursor.copy_from(output,'logcheck_json',null='')
    connection.commit()
    cursor.close()

def filterdata(method,data_Out):
    if method == 'Total':
        try:
            outsql(data_Out)
        except Exception as e:
            print(e)
    #通过列筛选，筛选出特定的行
    else:
        try:
            data_OutSplit=data_Out.loc[data_Out['Method']==method]
            outsql(data_OutSplit)
        except Exception as e:
            print(e)

#filterdata('GetAppItemTexts(String, Int32)')
#filterdata('Total')

path='D:/company/日志/log2'
files=os.listdir(path)

for file in files:
    print(file)
    fileread(path+'/'+file,'Total')
