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
import time
import datetime
import psycopg2

def fileread(fileurl,method):
    #配置文件路径
#    my_file = open(r'D:\company\日志\cocohub.20180305.131914.404.log','rb')
    my_file = open(fileurl,'rb')
    
    #把文件读进Dataframe
    data = pd.read_csv(my_file,sep='\n',encoding = 'utf8',header = None)
    print(data)
    #修改Dataframe的列名
    data.columns = ['logname']
    
#    print('改名成功')
    
    #把数据进行第一次分列
    data_split = pd.DataFrame((x.split('] ') for x in data.logname),index=data.index,columns=['createtime','type','Remark'])
#    print(data_split)
    
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
    
#    print(data_Final)
    
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
    cursor.copy_from(output,'logchecktest',null='')
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

def getTimeDiff(timeStra,timeStrb):
        if timeStra<=timeStrb:
            return 0
        ta = time.strptime(timeStra, "%Y-%m-%d %H:%M:%S")
#        print(ta)
        tb = time.strptime(timeStrb, "%Y-%m-%d %H:%M:%S")
#        print(tb)
        y,m,d,H,M,S = ta[0:6]
        dataTimea=datetime.datetime(y,m,d,H,M,S)
#        print(dataTimea)
        y,m,d,H,M,S = tb[0:6]
        dataTimeb=datetime.datetime(y,m,d,H,M,S)
#        print(dataTimeb)
        secondsDiff=(dataTimea-dataTimeb).seconds
        #两者相加得转换成分钟的时间差
        minutesDiff=round(secondsDiff/60,1)
        return minutesDiff

def get_FileSize(filePath):
    fsize=os.path.getsize(filePath)
    fsize = fsize/float(1024*1024)
    return int(fsize)

def isFileExists(fileName):
    conn = psycopg2.connect(database="postgres", user="postgres", password="123456", host="10.99.66.86", port="5432")
    cur = conn.cursor()
    cur.execute("select * from existfile where filename = '%s'"%fileName)
    rows = cur.fetchall()
    if rows:
        return 'exists'
    else:
        cur.execute("insert into existfile(filename) values ('%s')"%fileName)
        conn.commit()
        return 'not exists'
    conn.close()
#filterdata('GetAppItemTexts(String, Int32)')
#filterdata('Total')

if __name__ == '__main__':
#    path='D:/company/日志/log2'
#    files=os.listdir(path)
#    
#    for file in files:
#        print(file)
#        fileread(path+'/'+file,'Total')
   
#    paths=['D:/company/日志/log2'] #/data/MochaApi/log
#    
#    for path in paths:
#        files=os.listdir(path)
#        for file in files:
#            print(file)
#            fileread(path+'/'+file,'Total')

#   根据时间处理
#    paths=['D:/company/日志/log2'] #/data/MochaApi/log
#    for path in paths:
#        files=os.listdir(path)
#        for file in files:
#            filemt= time.localtime(os.stat(path+'/'+file).st_mtime)  
#            filetime=time.strftime("%Y-%m-%d %H:%M:%S",filemt)
#            currenttime=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
#            datediff=getTimeDiff(currenttime,filetime)
#            if(datediff < 60):
#                print('该文件为当前处理的文件，暂不导入')
#            else:
#                print(file)
#                fileread(path+'/'+file,'Total')

#   根据文件大小处理
    
    paths=['D:/company/日志/logtest'] #/data/MochaApi/log
    for path in paths:
        files=os.listdir(path)
        for file in files:
            fsize = get_FileSize(path+'/'+file) #获取文件大小
            isExists = isFileExists(file) #判断是否之前有导入过此文件
            if(fsize < 4):
                print('该文件为当前处理的文件，暂不导入')
            elif(isExists=='exists'):
                print('该文件已经导入')
            else:
                print(file)
                fileread(path+'/'+file,'Total')