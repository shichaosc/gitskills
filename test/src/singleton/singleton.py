#coding=utf-8
'''
Created on 2017年10月27日

@author: shicho
'''
class Singleton(object):
    def __new__(cls,*args,**kwargs):
        if not hasattr(cls, '_inst'):
            cls._inst=super(Singleton,cls).__new__(cls,*args,**kwargs)
        return cls._inst
 
if __name__=="__main__":
    class Test(Singleton):
        def __init__(self,s):
            self.s=s
    a=Test("shichao123")
    b=Test("shichao")
    print a.s
    print b.s
    
#用装饰器实现单例模式    
def singleton(cls, *args, **kw):    
    instances = {}    
    def _singleton():    
        if cls not in instances:    
            instances[cls] = cls(*args, **kw)    
        return instances[cls]    
    return _singleton    
   
@singleton    
class MyClass(object):    
    a = 1    
    def __init__(self, x=0):    
        self.x = x    
