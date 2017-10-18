# coding=utf-8
__author__ = 'Shichao'
__updated__ = '2017-09-28'

from suds.client import Client
from suds.plugin import MessagePlugin
from test_log import setLog
import analysis
import cx_Oracle
import logging




logging.basicConfig(level=logging.INFO)

#from Xzemr import settings


class MyPlugin(MessagePlugin):
    global analy
    analy = analysis.Analysis()

    def received(self, context):
        #      reply_new=re.findall("<soap:Envelope.+</soap:Envelope>",context.reply,re.DOTALL)[0]
        #        context.reply=reply_new
        pass

    def lims_data(self, date):
        url = 'http://localhost:8080/localstore.wsdl'
        client = Client(url, autoblend=True)
        print("@@@@@@@@@@@@@")
        # 查看该service提供的方法
        # print(client+"--------------")

        argu = client.factory.create('ns0:JJSHLimsRslt_In')
        
        argu.QYBM = '31250000'
        argu.CYKSRQ = date
        argu.CYJSRQ = date
        print(date)

        # 启动连接
        connStr = 'rsim/rsim@54.223.195.222:1521/XE'
        conn1 = cx_Oracle.connect(connStr)
        cursor1 = conn1.cursor()
        results = client.service.QueryLimsRslt(
            model=argu, pageSize=10, pageIndex=1)
        # results[list集合,165]
        setLog('log_test.txt', "总条数为：" + str(results[1]))
        for i in range(1, results[1] / 10 + 2):

            result = client.service.QueryLimsRslt(
                model=argu, pageSize=10, pageIndex=i)
            print("###############################################")
            for res in result[0]:  # res里面存的是列表[JJSHLimsRslt[],JJSHLimsRslt]
                lims=[]
                test=[]
                rrsult=[]
                simple=[]
                print(res)
                for r in res[1]:
                    lim=[]
                    test2017=[]
                    result2017=[]
                    simple2017=[]
                    # print(r)  # r是字典
                    # print(r["HGZ_COMPONENTS"])
                    #NUMBERS = NUMBERS + 1
                    # print("********************************")
                    # FCT_LIMS_SAMPLE表里
                    POINT_ID = r["S_SAMPLING_POINT_ID"]
                    SAMPLE_ID = r["SAMPLE_ID"]  # 样本ID号
                    SAMPLE_DATE = r["CREATE_DATE"]
 
                    SAMPLE_NAME = r["S_SAMPLE_NAME"]  # 样品名称
                    POINT_NAME=r["SP_SAMPLING_POINT"]#采样点名称
                    # 测试ID号# 不知道对不对 LOCATION_STANDARD总部标准装置
                    TEST_ID = r["T_NUMBER"]
                    RESULT_NAME = r["R_NAME"]  # HGZ_COMPONENTS
                    OUT_OF_RANGE = r["R_OUT_OF_RANGE"]
                    ORDER_NUMBER = r["R_ORDER_NUMBER"]
                    RESULT_TEXT = r["R_TEXT"]
                    # T_ANALYSIS_ID分析方法ID,VA_ANALYSIS_METHOD分析方法号
                    ANALYSIS_CODE = r["VA_ANALYSIS_METHOD"]
#                     ANALYSIS_DESC=r["VA_U_ANALDESC"]
                    S_DATE_AUTHORISED = r["S_DATE_AUTHORISED"]
 
                    REP_CONTROL = 'RPT'
                    # VA_U_ANALDESC = "硫含量" 不确定
                    PROJECT_ID = r["VA_U_ANALDESC"]
 
                    SAM_AUTH_MAN = r["S_AUTHORISER"]  # T_AUTHORISER
                    #ID_TEXT = r["POINT_STANDARD_CODE"]  # 样品编号 # 不确定
                    ID_TEXT = r["S_U_BATCH_NUM"]  # 样品编号 # 不确定
                    
#                     sql = "insert into FCT_LIMS_SAMPLE(POINT_ID,SAMPLE_ID,SAMPLE_DATE,SAMPLE_NAME,TEST_ID,RESULT_NAME,OUT_OF_RANGE,ORDER_NUMBER,RESULT_TEXT,ANALYSIS_CODE,S_DATE_AUTHORISED,PROJECT_ID,SAM_AUTH_MAN,ID_TEXT) values('" + POINT_ID + "','" + SAMPLE_ID + "',to_date('" + str(SAMPLE_DATE) + \
#                         "','yyyy-mm-dd hh24:mi:ss'),'" + str(SAMPLE_NAME) + "','" + str(TEST_ID) + "','" + str(RESULT_NAME) + "','" + str(OUT_OF_RANGE) + "','" + \
#                         str(ORDER_NUMBER) + "','" + str(RESULT_TEXT) + "','" + str(ANALYSIS_CODE) + \
#                         "',to_date('" + str(S_DATE_AUTHORISED) + \
#                         "','yyyy-mm-dd hh24:mi:ss'),'" + str(PROJECT_ID) + "','" + \
#                         str(SAM_AUTH_MAN) + "','" + str(ID_TEXT) + \
#                         "')"                    
                         
                  #  FCT_LIMS_SAMPLE批量插入用到
                    lim.append(POINT_ID)
                    lim.append(SAMPLE_ID)
                    lim.append(str(SAMPLE_DATE))
                    lim.append(SAMPLE_NAME)
                    lim.append(str(TEST_ID))
                    lim.append(RESULT_NAME)
                    lim.append(str(OUT_OF_RANGE))
                    lim.append(str(ORDER_NUMBER))
                    lim.append(RESULT_TEXT)
                    lim.append(ANALYSIS_CODE)
                    lim.append(str(S_DATE_AUTHORISED))
                    lim.append(PROJECT_ID)
                    lim.append(SAM_AUTH_MAN)
                    lim.append(ID_TEXT)
                    
                    lims.append(lim)
                    
                #fct_lims_test2017批量插入用到
                    test2017.append(str(SAMPLE_ID))
                    test2017.append(str(TEST_ID))
                    test2017.append(str(SAMPLE_DATE))
                    test2017.append(str(S_DATE_AUTHORISED))
                    test.append(test2017)
                
                #fct_lims_sample2017批量插入用到
                    simple2017.append(str(SAMPLE_ID))
                    simple2017.append(SAMPLE_NAME)
                    simple2017.append(str(SAMPLE_DATE))
                    simple2017.append(str(POINT_ID))
                    simple2017.append(ID_TEXT)
                    simple2017.append(str(S_DATE_AUTHORISED))
                    simple.append(simple2017)
                
#                 #fct_lims_result2017批量插入用到  
                    result2017.append(str(SAMPLE_DATE))
                    result2017.append(str(TEST_ID))
                    result2017.append(str(RESULT_NAME))
                    result2017.append(str(OUT_OF_RANGE))
                    result2017.append(str(ORDER_NUMBER))
                    result2017.append(str(RESULT_TEXT))
                    result2017.append(str(ANALYSIS_CODE))
                    result2017.append(str(S_DATE_AUTHORISED))
                    result2017.append(str(REP_CONTROL))
                    result2017.append(str(PROJECT_ID))
                    result2017.append(str(SAM_AUTH_MAN))
                    result2017.append(str(S_DATE_AUTHORISED))
                    rrsult.append(result2017)#批量插入报错
#                     analy.insert_result(r, cursor1, conn1)
#                     conn1.commit()
                sql = "insert into FCT_LIMS_SAMPLE(POINT_ID,SAMPLE_ID,SAMPLE_DATE,SAMPLE_NAME,TEST_ID,RESULT_NAME,OUT_OF_RANGE,ORDER_NUMBER,RESULT_TEXT,ANALYSIS_CODE,S_DATE_AUTHORISED,PROJECT_ID,SAM_AUTH_MAN,ID_TEXT) values(:1,:2,to_date(:3,'yyyy-mm-dd hh24:mi:ss'),:4,:5,:6,:7,:8,:9,:10,to_date(:11,'yyyy-mm-dd hh24:mi:ss'),:12,:13,:14)"
                sql1 = "insert into fct_lims_test2017(SAMPLE_ID,TEST_ID,SAMPLE_DATE,SDATE_AUTHORISED) values(:1,:2,to_date(:3,'yyyy-mm-dd hh24:mi:ss'),to_date(:4,'yyyy-mm-dd hh24:mi:ss'))"
                sql2 = "insert into fct_lims_sample2017(SAMPLE_ID,SAMPLE_NAME,SAMPLE_DATE,POINT_ID,ID_TEXT,DATE_AUTHORISED) values(:1,:2,to_date(:3,'yyyy-mm-dd hh24:mi:ss'),:4,:5,to_date(:6,'yyyy-mm-dd hh24:mi:ss'))"
                sql3 = "insert into fct_lims_result2017(SAMPLE_DATE,TEST_ID,RESULT_NAME,OUT_OF_RANGE,ORDER_NUMBER,RESULT_TEXT,ANALYSIS_CODE,SDATE_AUTHORISED,REP_CONTROL,PROJECT_ID,SAM_AUTH_MAN,DATE_AUTHORISED) values(to_date(:1,'yyyy-mm-dd hh24:mi:ss'),:2,:3,:4,:5,:6,:7,to_date(:8,'yyyy-mm-dd hh24:mi:ss'),:9,:10,:11,to_date(12,'yyyy-mm-dd hh24:mi:ss'))"
                cursor1.executemany(sql,lims)
                cursor1.executemany(sql1,test)
                cursor1.executemany(sql2,simple)
                cursor1.executemany(sql3,rrsult)
                conn1.commit()
            # 往lu_lims_analysis表里添加数据
#                     analy.insert_analysis(r, cursor1, conn1)
#                     analy.insert_point(r, cursor1, conn1)
#                     analy.insert_location(r, cursor1, conn1)
#                     analy.insert_dept(r, cursor1, conn1)
#                     analy.insert_result(r, cursor1, conn1)
#                     analy.insert_sample(r, cursor1, conn1)
#                     analy.insert_test(r, cursor1, conn1)
            setLog('log_test.txt',str(i) + "执行成功")
        cursor1.close()
        conn1.close()
        # print "sql报错"
