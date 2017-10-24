#coding=utf-8
'''
Created on 2017年10月24日

@author: Administrator
'''
import json
#websocket建立连接时调用
def ws_connect(message):
    message.reply_channel.send({"accept":True})#建立一个通信通道层
#     message.reply_channel.send({"close":True})#这个连接不建立通信通道
    print "connect success"
    
#websocket发来消息时调用该方法
def ws_receive(message):
    print "receive"
    data = json.loads(json.dumps(message['text']))
    #send方法只发送dir类型数据
    message.reply_channel.send({"text":data})#把前端某一个websocket传过来的信息发送到此时建立websocket连接的所有前端
#     message.reply_channel.send({"text":"nihao"})

#websocket请求断开连接时调用会
def ws_disconnect(message):
    print "disconnect"
    message.reply_channel.send({"text":"disconnect"})