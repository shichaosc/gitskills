#coding=utf-8
'''
Created on 2016年11月3日

@author: shichao
'''

import cx_Oracle
import datetime

#调用删除重复数据存储过程
def call_delete():
    conn_str = 'rsim/rsim@54.223.195.222:1521/XE'
    conn = cx_Oracle.connect(conn_str)
    cur = conn.cursor() 
    nowYear=str(datetime.datetime.now().year)
    msg = cur.var(cx_Oracle.STRING)#存储过程返回值
    #列表的形式表示存储过程的输入输出参数，nowYear是输入参数，msg是输出参数
    cur.callproc('pro_del' ,[nowYear,msg])
    conn.commit()
    print msg.getvalue()#打印存储过程的输出参数的值
    
if __name__=="__main__":
    call_delete()