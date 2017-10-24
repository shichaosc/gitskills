#-*-coding:utf-8 -*-
'''
Created on 2017年9月25日

@author: shichao
'''
from channels.asgi import get_channel_layer
import os
 
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "jozzon.settings")
 
channel_layer = get_channel_layer()