# coding=utf-8
__author__ = 'Shichao'
__updated__ = '2017-10-16'
'''
Created on 2017年3月7日

@author: Administrator
'''
from command.test_log import setLog

class Analysis:

    def insert_analysis(self, dir, cursor, connect):
        ANALYSIS_ID = dir["T_ANALYSIS_ID"]
        ANALYSIS_CODE = dir["VA_ANALYSIS_METHOD"]
        ANALYSIS_DESC=dir["VA_U_ANALDESC"]
        sql = "select ANALYSIS_ID from lu_lims_analysis where ANALYSIS_ID='%s'" %ANALYSIS_ID
 
        cursor.execute(sql)
        row = cursor.fetchall()
#         flag = True
#         for i in range(0, len(row)):
#             if ANALYSIS_ID == row[i][0]:
#                 flag = False
#                 break
#         if flag:
        if row==[]:
            try:
                sql2 = "insert into lu_lims_analysis(ANALYSIS_ID,ANALYSIS_CODE,ANALYSIS_DESC) values('" + \
                    ANALYSIS_ID + "','" + ANALYSIS_CODE + "','"+ANALYSIS_DESC+"')"
                cursor.execute(sql2.encode('gbk'))
                connect.commit()
                setLog('log_test.txt', "新添加了ANALYSIS_ID:" +
                       ANALYSIS_ID + "和ANALYSIS_CODE:" + ANALYSIS_CODE)
            except:
                setLog('log_exception.txt', "新添加ANALYSIS_ID:" +
                       ANALYSIS_ID + "和ANALYSIS_CODE:" + ANALYSIS_CODE+"添加失败")
    def insert_location(self, dir, cursor, connect):
        LOCATION_ID = dir["S_LOCATION_ID"]
        LOCATION_NAME = dir["L_LOCATION"]
        DEPT_NAME = dir["L_DEPT3_NAME"]  # 打印日志，往权限里加。
        DEPT_ID = dir["L_DEPT3"]
        TYPE = "装置"
        sql1 = "select LOCATION_ID from lu_lims_location LOCATION_ID='%s'" % LOCATION_ID
        cursor.execute(sql1)
        row = cursor.fetchall()
        if row==[]:
            try:
                sql2 = "insert into lu_lims_location(LOCATION_ID,LOCATION_NAME,DEPT_ID,TYPE) values('" + \
                    LOCATION_ID + "','" + LOCATION_NAME + \
                    "','" + DEPT_ID + "','" + TYPE + "')"
            # 赋予部门权限
    #         flag = True
    #         for i in range(0, len(row)):
    # 
    #             if LOCATION_ID == row[i][0]:
    #                 flag = False
    #         if flag == True:
    
                cursor.execute(sql2.encode('GB2312'))
                connect.commit()
                setLog(
                    'log_location.txt', "新添加了" + LOCATION_ID + "---" + LOCATION_NAME + "装置，部门是：" + DEPT_NAME)
            except:
                setLog(
                    'log_exception.txt', LOCATION_ID + "---" + LOCATION_NAME + "装置，部门是：" + DEPT_NAME+"添加失败")
    def insert_point(self, dir, cursor, connect):
        POINT_ID = dir["S_SAMPLING_POINT_ID"]
        POINT_NAME = dir["SP_SAMPLING_POINT"]
        LOCATION_ID = dir["S_LOCATION_ID"]
        sql1 = "select POINT_ID from lu_lims_sample_point where modified_on is null where point_id='%s'" %POINT_ID
        cursor.execute(sql1)
        row = cursor.fetchall()
        if row==[]:
            try:
                sql2 = "insert into lu_lims_sample_point(POINT_ID,POINT_NAME,LOCATION_ID) values('" + \
                    POINT_ID + "','" + POINT_NAME + "','" + LOCATION_ID + "')"
    #         for i in range(0, len(row)):
    # 
    #             if POINT_ID == row[i][0]:
    #                 flag = False
    #         if flag == True:
                
                cursor.execute(sql2.encode('GB2312'))
                connect.commit()
                setLog(
                    'log_test.txt', "新添加了" + POINT_ID + "---" + POINT_NAME + "采样点")
            except:
                setLog(
                    'log_exception.txt', POINT_ID + "---" + POINT_NAME + "采样点添加失败")

    def insert_dept(self, dir, cursor, connect):
        DEPT_ID = dir["L_DEPT3"]
        DEPT_NAME = dir["L_DEPT3_NAME"]
        
        sql1 = "select DEPT_ID from lu_lims_dept where DEPT_ID='"+DEPT_ID+"'"
        cursor.execute(sql1)
        row = cursor.fetchall()
        if row==[]:
            try:
                sql2 = "insert into lu_lims_dept(DEPT_ID,DEPT_NAME) values('" + \
                    DEPT_ID + "','" + DEPT_NAME + "')"  
    #         flag = True
    #         for i in range(0, len(row)):
    # 
    #             if DEPT_ID == row[i][0]:
    #                 flag = False
    #         if flag == True:
    
                cursor.execute(sql2.encode('gbk'))
                connect.commit()
                setLog(
                    'log_dept.txt', "新添加了" + DEPT_ID + "---" + DEPT_NAME + "部门")
            except:
                setLog(
                        'log_exception.txt', DEPT_ID + "---" + DEPT_NAME + "部门添加失败")
    def insert_result(self, r, cursor, connect):
        # FCT_LIMS_SAMPLE表里
        SAMPLE_DATE = r["CREATE_DATE"]

        # 测试ID号# 不知道对不对 LOCATION_STANDARD总部标准装置
        TEST_ID = r["T_NUMBER"]
        RESULT_NAME = r["R_NAME"]  # HGZ_COMPONENTS
        OUT_OF_RANGE = r["R_OUT_OF_RANGE"]
        ORDER_NUMBER = r["R_ORDER_NUMBER"]
        RESULT_TEXT = r["R_TEXT"]
        # T_ANALYSIS_ID分析方法ID,VA_ANALYSIS_METHOD分析方法号
        ANALYSIS_CODE = r["VA_ANALYSIS_METHOD"]
        SDATE_AUTHORISED = r["S_DATE_AUTHORISED"]

        REP_CONTROL = 'RPT'
        # VA_U_ANALDESC = "硫含量" 不确定
        PROJECT_ID = r["VA_U_ANALDESC"]

        SAM_AUTH_MAN = r["S_AUTHORISER"]  # T_AUTHORISER
        DATE_AUTHORISED = r["S_DATE_AUTHORISED"]
        try:
            sql = "insert into fct_lims_result2017(SAMPLE_DATE,TEST_ID,RESULT_NAME,OUT_OF_RANGE,ORDER_NUMBER,RESULT_TEXT,ANALYSIS_CODE,SDATE_AUTHORISED,REP_CONTROL,PROJECT_ID,SAM_AUTH_MAN,DATE_AUTHORISED) values(to_date('" + str(SAMPLE_DATE) + \
                "','yyyy-mm-dd hh24:mi:ss'),'" + str(TEST_ID) + \
                "','" + str(RESULT_NAME) + "','" + str(OUT_OF_RANGE) + "','" + str(ORDER_NUMBER) + "','" + RESULT_TEXT + "','" + ANALYSIS_CODE + "',to_date('" + str(SDATE_AUTHORISED) + "','yyyy-mm-dd hh24:mi:ss'),'" + REP_CONTROL + "','" + PROJECT_ID + \
                "','" + str(SAM_AUTH_MAN) + \
                "',to_date('" + str(DATE_AUTHORISED) + \
                "','yyyy-mm-dd hh24:mi:ss'))"  
        
            cursor.execute(sql.encode('GB2312'))
            connect.commit()
        except Exception:
            setLog('log_exception.txt', sql + '失败')
    def insert_sample(self, r, cursor, connect):
        SAMPLE_ID = r["SAMPLE_ID"]
        SAMPLE_NAME = r["S_SAMPLE_NAME"]
        SAMPLE_DATE = r["CREATE_DATE"]
        POINT_ID = r["S_SAMPLING_POINT_ID"]
        ID_TEXT = r["POINT_STANDARD_CODE"]
        DATE_AUTHORISED = r["S_DATE_AUTHORISED"]
        
        try:
            sql = "insert into fct_lims_sample2017(SAMPLE_ID,SAMPLE_NAME,SAMPLE_DATE,POINT_ID,ID_TEXT,DATE_AUTHORISED) values('" + \
                str(SAMPLE_ID) + "','" + str(SAMPLE_NAME) + "',to_date('" + str(SAMPLE_DATE) + "','yyyy-mm-dd hh24:mi:ss'),'" + POINT_ID + "','" + \
                ID_TEXT + \
                "',to_date('" + str(DATE_AUTHORISED) + \
                "','yyyy-mm-dd hh24:mi:ss'))"  

            cursor.execute(sql.encode('GB2312'))
            connect.commit()
        except Exception:
            setLog('log_exception.txt', sql + '失败')

    def insert_test(self, r, cursor, connect):
        SAMPLE_ID = r["SAMPLE_ID"]
        TEST_ID = r["T_NUMBER"]
        SAMPLE_DATE = r["CREATE_DATE"]
        SDATE_AUTHORISED = r["S_DATE_AUTHORISED"]
        try:
            sql = "insert into fct_lims_test2017(SAMPLE_ID,TEST_ID,SAMPLE_DATE,SDATE_AUTHORISED) values('" + \
                str(SAMPLE_ID) + "','" + str(TEST_ID) + \
                "',to_date('" + str(SAMPLE_DATE) + "','yyyy-mm-dd hh24:mi:ss'),to_date('" + \
                str(SDATE_AUTHORISED) + \
                "','yyyy-mm-dd hh24:mi:ss'))"
        
            cursor.execute(sql.encode('GB2312'))
            connect.commit()
        except Exception:
            setLog('log_exception.txt', sql + '失败')
            



