#coding=utf-8
'''
Created on 2017年9月30日

@author: Administrator
'''


from command import test_log
import cx_Oracle
def insertOil():
    try:
        connStr = 'yykp/yykp@10.124.2.60/orcl'
        conn1 = cx_Oracle.connect(connStr)
        cursor1 = conn1.cursor()
        connStr2 = 'rsim/rsim@54.223.195.222:1521/XE'
        conn2 = cx_Oracle.connect(connStr2)
        cursor2 = conn2.cursor()
        insertBaesData(cursor1,cursor2,conn1,conn2)
        #由于原油性质表数据有三百多万条，所以按每次抽取id相隔一万条来抽取
        insertQuality3(cursor1,cursor2,conn1,conn2)
        insertBaseQuality(cursor1,cursor2,conn1,conn2)
        cursor1.close()
        cursor2.close()
        conn2.close()
        conn1.close()
    except:
        test_log.setLog("log_oil", "插入原油快评数据失败")

#F_OIL_BASEDATA表中抽取数据
def insertBaesData(cursor1,cursor2,conn1,conn2):
    #把表中的最大id查出来
    try:
        cursor2.execute("select max(id) from F_OIL_BASEDATA")#如果没有数据，抽取出来的是None
        ids=cursor2.fetchall()
        maxId=ids[0][0]
        if maxId==None:
            maxId=0
        print(maxId)
    except:
        maxId=0
    # ------------------------------
    #每次从九江抽取项目数据库的最大id之后的数据
    cursor1.execute('select * from cut_oilbasedata where id>'+str(maxId))
    rows=cursor1.fetchall()
    list1=[]
    for row in rows:
        list2=[]
        for r in row:
            if r==None:
                r=''
            list2.append(str(r))
        list1.append(list2)
    sql1="insert into F_OIL_BASEDATA values(:1,:2,:3,to_date(:4,'yyyy-mm-dd hh24:mi:ss'),to_date(:5,'yyyy-mm-dd hh24:mi:ss'),:6,:7,:8,:9,:10,:11,:12,:13,:14,:15)"
    cursor2.executemany(sql1,list1)
    conn2.commit()
#     cursor1.close()
#     cursor2.close()
# def insertQuality1(cursor1,cursor2,conn1,conn2):
#     print(cursor1)
#     cursor1.execute("select max(id) from cut_propertydata")
#     ids=cursor1.fetchall()
#     maxId=ids[0][0]
#     for i in range(maxId/10000):
#         try: 
#             sql='select * from cut_propertydata where '+str((i)*10000)+'<=id and id<'+str((i+1)*10000)
#             print(sql)
#             cursor1.execute(sql)
#             rows=cursor1.fetchall()
#             print(rows)
#             if rows==[]:
#                 break;
#             list1=[]
#             for row in rows:
#                 list2=[]
#                 for r in row:
#                     list2.append(str(r))
#                 list1.append(list2)
#             sql2="insert into F_OIL_QUALITY(ID,OILID,CODE,VALUE,IVT,FVT) values(:1,:2,:3,:4,:5,:6)"
#             cursor2.executemany(sql2,list1)
#             conn2.commit()
#         except:
#             pass
#     
#     cursor1.close()
#     cursor2.close()
# 
# def insertQuality2(cursor1,cursor2,conn1,conn2):
#     cursor2.execute("select max(id) from F_OIL_QUALITY")
#     ids=cursor2.fetchall()
#     maxId1=ids[0][0]
#     print(maxId1)
#     cursor1.execute("select max(id) from cut_propertydata")
#     ids=cursor1.fetchall()
#     maxId2=ids[0][0]
#     print(maxId2)
#     for i in range((maxId2-maxId1)/10000+1):
#         cursor1.execute('select * from cut_propertydata where id>'+str(maxId1+i*10000)+'and id<='+str(maxId1+(i+1)*10000))
# #         cursor1.execute('select * from cut_propertydata where id>'+str(maxId+i)+'and id<='+str(maxId+i+1))
#         rows=cursor1.fetchall()
#         if rows==[]:
# #             break
#             continue
#         list1=[]
#         for row in rows:
# #                 list2=[]
# #                 for r in row:
# #                     if r==None:
# #                         r=0
# #                     list2.append(str(r))
# #                 list1.append(list2)
#             try:
#                 sql2="insert into F_OIL_QUALITY(ID,OILID,CODE,VALUE,IVT,FVT) values("+str(row[0])+","+str(row[1])+",'"+str(row[2])+"',"+str(row[3])+",'"+str(row[4])+"','"+str(row[5])+"')"
#                 cursor2.execute(sql2.encode('gbk'))
#                 conn2.commit()
#             except:
#                 print(row)


#往f_oil_quality原油性质表中抽取数据
def insertQuality3(cursor1,cursor2,conn1,conn2):
    cursor2.execute("select max(id) from F_OIL_QUALITY")
    ids=cursor2.fetchall()
    maxId1=ids[0][0]
    if maxId1==None:
        maxId1=0
    print(maxId1)
    cursor1.execute("select max(id) from cut_propertydata")
    ids=cursor1.fetchall()
    maxId2=ids[0][0]
    print(maxId2)
    for i in range((maxId2-maxId1)/10000+1):
        cursor1.execute('select * from cut_propertydata where id>'+str(maxId1+i*10000)+'and id<='+str(maxId1+(i+1)*10000))
        rows=cursor1.fetchall()
        print(rows)
        if rows==[]:
#             break
            continue
        list1=[]
        for row in rows:
            list2=[]
            for r in row:
                if r==None:
                    r=0
                list2.append(str(r))
            list1.append(list2)
        try:
            sql2="insert into F_OIL_QUALITY(ID,OILID,CODE,VALUE,IVT,FVT) values(:1,:2,:3,:4,:5,:6)"
            cursor2.executemany(sql2,list1)
            conn2.commit()
        except:
            for r in row:
                if r==None:
                    continue
                try:
                    sql2="insert into F_OIL_QUALITY(ID,OILID,CODE,VALUE,IVT,FVT) values("+str(row[0])+","+str(row[1])+",'"+str(row[2])+"',"+str(row[3])+",'"+str(row[4])+"','"+str(row[5])+"')"
                    cursor2.execut(sql2)
                    conn2.commit()
                except:
                    print(row)

#抽取原油物性基础表                    
def insertBaseQuality(cursor1,cursor2,conn1,conn2):
    cursor2.execute("select max(id) from D_OIL_QUALITY")
    ids=cursor2.fetchall()
    maxId=ids[0][0]
    if maxId==None:
        maxId=0
    print(maxId)
    cursor1.execute("select distinct id,code,enname,name,unit,min,max,description from CUT_PROPERTY where id>"+str(maxId))
    rows=cursor1.fetchall()
    for r in rows:
        row=[]
        for rr in r:
            if rr==None:
                row.append("")
            else:
                row.append(str(rr))
        try:
            print("@22")
            sql="insert into d_OIL_QUALITY(id,code,enname,name,unit,min,max,description) values(%s,'%s','%s','%s','%s','%s','%s','%s')" %(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7])
            print(sql)
            cursor2.execute(sql.encode('gbk'))
            conn2.commit()
        except[Exception]:
            print(Exception.message)


if __name__ == '__main__':
    insertOil()

