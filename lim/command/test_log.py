# coding=utf-8
__author__ = 'Shichao'
__updated__ = '2017-09-28'
'''
Created on 2017年3月8日

@author: Administrator
'''
import logging
import time


def setLog(log_filename, log_message):
    logger = logging.getLogger()
    handler = logging.FileHandler(log_filename)
    logger.addHandler(handler)
    logger.setLevel(logging.NOTSET)
    date = time.strftime('%Y-%m-%d', time.localtime())
    logger.critical(date + "--" + log_message)
    # 如果没有此句话，则会将同一个message追加到不同的log中
    logger.removeHandler(handler)
