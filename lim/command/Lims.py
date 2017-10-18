# coding=utf-8
__author__ = 'Shichao'
__updated__ = '2017-09-28'
'''
#Created on 2017年3月2日

@author: Administrator
'''
# from cgitb import handler
# from cookielib import logger
from django.core.management.base import BaseCommand
# from suds.client import Client
# from suds.plugin import MessagePlugin
# import cx_Oracle
import datetime
import jiujiang
# import logging



# suds是一个轻量级的Python的SOAP Web service客户端。
# 对于Python仅做为客户端调用webservice的情况，建议使用suds
class Command(BaseCommand):
    help = "Closes the specified poll for voting"
    # 将Poll应用之下的Poll model之中的数据的opened设置为False

    def handle(self, *args, **options):
        myPlugin = jiujiang.MyPlugin()

        # 获取昨天日期
        today = datetime.date.today()
        oneday = datetime.timedelta(days=1)
        yesterday = today - oneday
        myPlugin.lims_data(str(yesterday))
