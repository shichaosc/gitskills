#!D:\python27\python32.exe
# coding=utf-8
__author__ = 'Shichao'
__updated__ = '2017-09-25'
'''
Created on 2017年3月16日

@author: Administrator
'''
import os
import pickle
import pyodbc
conn = pyodbc.connect('DSN=RTDB;PWD=')
print(conn)
cur = conn.cursor()
if os.path.isfile('E:\pythonWorkSpace\dump.txt'): 
    os.remove('E:\pythonWorkSpace\dump.txt')
cur.execute(
    "SELECT NAME AS TAG, ip_input_value AS V, CAST(ip_value_time AS CHAR FORMAT 'YYYY-MM-DD HH:MI:SS') AS DT FROM IP_AnalogDef")
rows = cur.fetchall()
mylist2 = []
for i in range(1, len(rows)):
    mylist1 = []
    mylist1.append(rows[i][0])
    mylist1.append(rows[i][1])
    mylist1.append(rows[i][2])
    # print(mylist1)
    mylist2.append(mylist1)
f = open('E:\pythonWorkSpace\dump.txt', 'wb')
pickle.dump(mylist2, f)
f.close()
print('success')
cur.close()
conn.close()
