#coding=utf-8
'''
Created on 2017年10月23日

@author: Administrator
'''
from channels import Group
from channels.sessions import channel_session
import json
#websocket建立连接时调用
def ws_connect(message):
    prefix, label = message['path'].strip('/').split('/')#laber是区分各个组的
#     message.channel_session['test_room']=label
    message.reply_channel.send({"accept":True})
    print label
    Group(label).add(message.reply_channel)#message.reply_channel是一个通道对象
    
#websocket发来消息时调用该方法
def ws_receive(message):
#     laber=message.channel_session['test_room']
    prefix, label = message['path'].strip('/').split('/')
    print label
    data = json.loads(json.dumps(message['text']))
    Group(label).send({"text":data})#向myRoom频道下的所有连接发送消息
    
#websocket请求断开连接时调用会
def ws_disconnect(message):
    prefix, label = message['path'].strip('/').split('/')
    print label
#     laber=message.channel_session['test_room']
    Group(label).discard(message.reply_channel)
    
#前台写了一个简单的js:
# @channel_session  #加这个装饰器以后，message就有channel_session属性了，相当于一个session,从中取出laber
'''
<html>
<head>
<script src="reconnecting-websocket.min.js"></script>   //websocket的js
<script>
// Note that the path doesn't matter right now; any WebSocket
// connection gets bumped over to WebSocket consumers
socket = new WebSocket("ws://127.0.0.1:8000/myRoom/");  //创建一个websocket
    //ws是websocket的协议,websocket的协议是ws(http)或wss(https)====================
socket.onmessage = function(e) { //websocket接收数据函数
    alert(e.data);
}
socket.onopen = function() {
    socket.send("hello world"); //websocket发送数据
}
// Call onopen directly if socket is already open
if (socket.readyState == WebSocket.OPEN) socket.onopen();
</script>
</head>
</html>
'''
#执行顺序就是连接到myRoom，myRoom是组名，这个websocket是连接到myRoom这个组，
#然后会发送到这个组的所有连接。只有同组才能互相传