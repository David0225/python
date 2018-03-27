# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 11:44:51 2018

@author: wuzw
"""

import pymssql


conn=pymssql.connect(host='10.99.66.46',user='david',password='life@1234',database='LifeVc.com',charset='GBK')
''''' 
如果和本机数据库交互，只需修改链接字符串 
conn=pymssql.connect(host='.',database='Michael') 
''' 

cur=conn.cursor()

#cur.execute('select top 5 GoodsId,GoodsName from dbo.a_goodsinfo with(nolock)')  
##如果update/delete/insert记得要conn.commit()  
##否则数据库事务无法提交  
#print (cur.fetchall())

cur.execute("select top 5 GoodsId,GoodsName from dbo.a_goodsinfo with(nolock)")

data=cur.fetchall()

for GoodsId,GoodsName in data:
    print(GoodsId,GoodsName)

cur.close()
conn.close()