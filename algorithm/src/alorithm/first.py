#coding=utf-8
'''
Created on 2017年10月18日

@author: Administrator
'''
import time
'''
计算从一加到一千万，比较两种方法的策略，运算次数，占用内存大小
'''
def sum1(size):
    sTime=time.time()              #开始时间
    sum=0                          #执行一次
    try:                         
        for i in range(1,size+1):    #执行size次
            sum=sum+i  
        print "sum1--"+str(sum)        #执行一次
        eTime=time.time()              #结束时间
        print eTime-sTime            #总共用时
    except Exception,e:
        print e.msg
def sum2(size):
    sTime=time.time()              #开始时间
    sum=0                          #执行一次
    try:                         
        sum=(1+size)*size/2          #执行一次
        print "sum2--"+str(sum)      #执行一次
        eTime=time.time()           #结束时间
        print eTime-sTime          #总共用时
    except Exception,e:
        print e.msg
if __name__=="__main__":
    sum1(10000000)
    sum2(10000000)
    