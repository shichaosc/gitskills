# coding=utf-8
__author__ = 'Shichao'
__updated__ = '2017-10-16'
'''
Created on 2017年3月16日

@author: Administrator
'''
from command import test_log
import cx_Oracle
import datetime
import pickle

dbfile = open(r'E:\pythonWorkSpace\dump.txt', 'rb')
li = pickle.load(dbfile)
dbfile.close()

connStr = 'rsim/rsim@54.223.195.222:1521/XE'
conn1 = cx_Oracle.connect(connStr)
cursor1 = conn1.cursor()

# 计算总条数
a = 0
# 获取昨天日期
today = datetime.date.today()
oneday = ''.join(str(today).split('-'))
mesLists=[]
for i in range(0, len(li)):
    TIME_STAMP = li[i][2]
    if TIME_STAMP or TIME_STAMP!=None:
        dayList = TIME_STAMP.strip().split()
        day = dayList[0].split('-')
        DAY_ID = ''.join(day)
        if DAY_ID!='20170831':
            continue
    
        PHD_TAG_ID = li[i][0]
        TAG_VALUE = li[i][1]
        if TAG_VALUE == None:
            TAG_VALUE = 0
        mesList=[]
        mesList.append(PHD_TAG_ID)
        mesList.append(TAG_VALUE)
        mesList.append(str(TIME_STAMP))
        CONFIDENCE = 100
        mesList.append(CONFIDENCE)
        mesList.append(int(DAY_ID))
        mesList.append(int(DAY_ID))
        mesLists.append(mesList)
    
    if DAY_ID == '20170831':
        sql = "insert into fct_mes_result2017(PHD_TAG_ID,DAY_ID,TAG_VALUE,TIME_STAMP,CONFIDENCE,DATA_TIME) values('" + \
            PHD_TAG_ID + "'," + DAY_ID + "," + str(TAG_VALUE) + ",'" + \
            str(TIME_STAMP) + "'," + str(CONFIDENCE) + "," + DAY_ID + ")"
        print(sql)
        cursor1.execute(sql)
        conn1.commit()
        a = a + 1
   
# sql = "insert into fct_mes_result2017(PHD_TAG_ID,TAG_VALUE,TIME_STAMP,CONFIDENCE,DAY_ID,DATA_TIME) values(:1,:2,:3,:4,:5,:6)"
# cursor1.executemany(sql,mesLists)
# # cursor1.execute(sql,mesList)
# conn1.commit()
cursor1.close()
conn1.close()
print("success")
# test_log.setLog('mesCount.txt', '插入mes数据' + str(len(mesLists)) + '条')
test_log.setLog('mesCount.txt', '插入mes数据' + str(a) + '条')
mesLists=[]