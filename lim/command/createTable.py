#coding=utf-8
from command.test_log import setLog
__author__ = 'Shichao'
from django.core.management.base import BaseCommand
import cx_Oracle
import datetime
import logging
import time
'''
创建定时任务，每年的11月份执行创建表的存储过程
'''
class Command(BaseCommand):
    def handle(self, *args, **options):
        nowYear=int(datetime.datetime.now().year)+1

        oacle_str = 'rsim/rsim@54.223.195.222:1521/XE'
        conn = cx_Oracle.connect(oacle_str)
        cur = conn.cursor()     
        # 调用存储过程 创建表(存储过程参数为下一年的年份,返回值为success创建成功，fail创建失败)
        #声名存储过程需要的参数，返回值
        year=str(nowYear)
        msg = cur.var(cx_Oracle.STRING)#存储过程返回值
        cur.callproc('CreateTableAndIndex' ,[year,msg])
        conn.commit()
        if msg.getvalue()=='fail':
            setLog('log_table',"创建表"+year+"失败")
        cur.close()
        conn.close()
    
    def setLog(self,log_filename, log_message):
        logger = logging.getLogger()
        handler = logging.FileHandler(log_filename)
        logger.addHandler(handler)
        logger.setLevel(logging.NOTSET)
        date = time.strftime('%Y-%m-%d', time.localtime())
        logger.critical(date + "--" + log_message)
        # 如果没有此句话，则会将同一个message追加到不同的log中
        logger.removeHandler(handler)       
if __name__=="__main__":
    c=Command()
    c.handle()