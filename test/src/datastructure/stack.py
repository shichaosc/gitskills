#coding=utf-8
'''
Created on 2017年11月6日

@author: Administrator
'''
'''
用python的list模拟栈
pop()返回栈顶元素，不过栈顶元素会从栈中删掉；
Peek():返回栈顶元素，不删除元素
Push():把一个元素添加到栈的最顶层
Stack():创建一个空栈
isEmpty():判断栈是否为空
Size():返回栈中元素的个数
'''
class Stack():
    
    def __init__(self): 
        self.items = [] 
    
    #判断一个栈是否为空    
    def isEmpty(self):
        return len(self.items)==0
    
    #往栈里添加数据
    def push(self,item):
        self.items.append(item)
        
    def pop(self):
#         pItem=self.items[len(self.items)-1]
# #         self.items.remove(self.items[len(self.items)-1])
#         del self.items[len(self.items)-1]
#         return pItem
        return self.items.pop()#列表也有pop方法。
    
    def peek(self): 
        if not self.isEmpty(): 
            return self.items[len(self.items)-1] 
 
    def size(self): 
        return len(self.items)
    
if __name__=="__main__":
    stack=Stack()
    print stack.isEmpty()
    
    stack.push("123")
    stack.push("345")
    print stack.pop()
    print stack.peek() 
    print stack