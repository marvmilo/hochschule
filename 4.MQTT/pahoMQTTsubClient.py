#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 13:07:21 2018

@author: user

Quelle: https://www.eclipse.org/paho/clients/python/docs/
"""

import paho.mqtt.subscribe as subscribe
broker = "mqtt.eclipseprojects.io"
#topic = "$_abra$$cadabra/nö/Türe/1"
topic = "$_abra$$cadabra/+/Test"

def on_message_print(client, userdata, message):
    print("%s %s" % (message.topic, message.payload))

subscribe.callback(on_message_print, topic, hostname=broker)



#subscribe.callback(on_message_print, "$_abra$$cadabra/#", qos=0, userdata=None, 
#    hostname="mqtt.eclipseprojects.io", port=1883, client_id="96653209679634",
#     keepalive=60, will=None, auth=None, tls=None, protocol=mqtt.MQTTv311)



























   

