# coding=utf-8
__author__ = 'Shichao'
__updated__ = '2017-10-16'
from command import analysis
from command.test_log import setLog
from suds.client import Client
from suds.plugin import MessagePlugin
import cx_Oracle
import logging
import os



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
        os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.ZHS16GBK' 
        url = 'http://localhost:8080/localstore.wsdl'
        client = Client(url, autoblend=True)

        # 查看该service提供的方法
        # print(client+"--------------")

        argu = client.factory.create('ns0:JJSHLimsRslt_In')
        
        argu.QYBM = '31250000'
        argu.CYKSRQ = date
        argu.CYJSRQ = date

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
                # print(res[1])  # res[1]里面存的是字典列表
                for r in res[1]:
                    # FCT_LIMS_SAMPLE表里
                    POINT_ID = r["S_SAMPLING_POINT_ID"]
                    SAMPLE_ID = r["SAMPLE_ID"]  # 样本ID号
                    SAMPLE_DATE = r["CREATE_DATE"]
                    POINT_NAME = r["SP_SAMPLING_POINT"]
                    SAMPLE_NAME = r["S_SAMPLE_NAME"]  # SP_SAMPLING_POINT
                    # 测试ID号# 不知道对不对 LOCATION_STANDARD总部标准装置
                    TEST_ID = r["T_NUMBER"]
                    RESULT_NAME = r["R_NAME"]  # HGZ_COMPONENTS
                    OUT_OF_RANGE = r["R_OUT_OF_RANGE"]
                    ORDER_NUMBER = r["R_ORDER_NUMBER"]
                    RESULT_TEXT = r["R_TEXT"]
                    # T_ANALYSIS_ID分析方法ID,VA_ANALYSIS_METHOD分析方法号
                    ANALYSIS_CODE = r["VA_ANALYSIS_METHOD"]
                    S_DATE_AUTHORISED = r["S_DATE_AUTHORISED"]
 
                    REP_CONTROL = 'RPT'
                    # VA_U_ANALDESC = "硫含量" 不确定
                    PROJECT_ID = r["VA_U_ANALDESC"]
 
                    SAM_AUTH_MAN = r["S_AUTHORISER"] # T_AUTHORISER
                    #ID_TEXT = escape(r["POINT_STANDARD_CODE"]  # 样品编号 # 不确定
                    ID_TEXT =r["S_U_BATCH_NUM"]  # 样品编号 # 不确定
                    try:
                        sql = "insert into FCT_LIMS_SAMPLE(POINT_ID,SAMPLE_ID,SAMPLE_DATE,SAMPLE_NAME,TEST_ID,RESULT_NAME,OUT_OF_RANGE,ORDER_NUMBER,RESULT_TEXT,ANALYSIS_CODE,S_DATE_AUTHORISED,PROJECT_ID,SAM_AUTH_MAN,ID_TEXT,REP_CONTROL) values('" + POINT_ID + "','" + SAMPLE_ID + "',to_date('" + str(SAMPLE_DATE) + \
                            "','yyyy-mm-dd hh24:mi:ss'),'" + str(SAMPLE_NAME) + "','" + str(TEST_ID) + "','" + str(RESULT_NAME) + "','" + str(OUT_OF_RANGE) + "','" + \
                            str(ORDER_NUMBER) + "','" + str(RESULT_TEXT) + "','" + str(ANALYSIS_CODE) + \
                            "',to_date('" + str(S_DATE_AUTHORISED) + \
                            "','yyyy-mm-dd hh24:mi:ss'),'" + str(PROJECT_ID) + "','" + \
                            str(SAM_AUTH_MAN) + "','" + str(ID_TEXT) + \
                            "','"+str(REP_CONTROL)+"')"
                        cursor1.execute(sql.encode('GB2312'))
                        conn1.commit()   
                    except Exception:
                        setLog(
                            'log_exception.txt',sql+'失败')

            # 往lu_lims_analysis表里添加数据
                    analy.insert_analysis(r, cursor1, conn1)
                    analy.insert_point(r, cursor1, conn1)
                    analy.insert_location(r, cursor1, conn1)
                    analy.insert_dept(r, cursor1, conn1)
                    analy.insert_result(r, cursor1, conn1)
                    analy.insert_sample(r, cursor1, conn1)
                    analy.insert_test(r, cursor1, conn1)
                    
                     
            setLog('log_test.txt',str(i) + "执行成功")
        cursor1.close()
        conn1.close()
        # print "sql报错"
