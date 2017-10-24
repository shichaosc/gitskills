#coding=utf-8
'''
Created on 2017年10月23日

@author: Administrator
'''
from channels.routing import route,include
import groupConsumer,noGroupConsumer

group_routing={
    route("websocket.connect",groupConsumer.ws_connect),
    route("websocket.receive",groupConsumer.ws_receive),
    route("websocket.disconnect",groupConsumer.ws_disconnect),    
}
# noGroup_routing={
#     route("websocket.connect",noGroupConsumer.ws_connect),
#     route("websocket.receive",noGroupConsumer.ws_receive),
#     route("websocket.disconnect",noGroupConsumer.ws_disconnect),    
# }
routing=[
    include(group_routing,path=r'/group'),
#     include(noGroup_routing,path=r'/nogroup'),
]