# coding=utf-8
__author__ = 'Shichao'
__updated__ = '2017-03-28'
'''
Created on 2017年3月13日

@author: Administrator
'''
import os
import subprocess
import jpype

# # 调用javaAPI
# jvmPath = jpype.getDefaultJVMPath()  # 得到java虚拟机路径
# print(jvmPath)

# classpath = "D:\\LiclipseWorkSpace\\lim\\command\\cn\\zkjz\\odbc"
# print(classpath)
# jvmArg = "-Djava.class.path=" + classpath
jvmPath = r"D:\Java\jre\bin\client"
print(jvmPath)
if not jpype.isJVMStarted():  # test whether the JVM is started

    jpype.startJVM(jvmPath)

print(jpype.isJVMStarted())

javaClass = jpype.JClass("TestOdbc")
odbc = javaClass()
print(odbc.test())
# print(javaClass.add(1, 9))
# jpype.java.lang.System.out.println("hello world!")
# 调用java的jar包  没有成功
# jarPath = os.path.join(os.path.abspath('.'), 'E:\\')
# print(jarPath)
# jpype.startJVM(jpype.getDefaultJVMPath(), "-ea",
#                "-Djava.class.path=%s" % r'D:\LiclipseWorkSpace\lim\command\123.jar')
# JDClass = JClassUtil('cn.zkjz.odbc.TestOdbc.class')
# jd = JDClass()
# print(jd)

# javaClass = jpype.JClass('Testodbc')
# value = 'oldvalue'
# javaInstance = javaClass(value)
# print(javaInstance.getValue())
# javaInstance.setValue('newvalue')
# print(javaInstance.getValue())
#os.system('javac TestOdbc.java')


# os.system('java TestOdbc')
# print(os.getcwd())

# subprocess.Popen('javac TestOdbc.java', shell=True)
# subprocess.Popen('java TestOdbc', shell=True)
