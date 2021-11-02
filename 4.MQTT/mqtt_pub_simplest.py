#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 20:45:24 2018

@author: user

Quelle:  https://pypi.org/project/paho-mqtt/

"""


import paho.mqtt.publish as publish


try:
    while True:
        MESSAGE = input("tcpClientA: Enter message/Enter \"exit\": ")
        print("publishing ")
        publish.single("$_abra$$cadabra/nö/Test", MESSAGE, hostname="mqtt.eclipseprojects.io")
        if MESSAGE == 'exit':
            break
finally:
    print("exiting ")

#publish.single("/$SYS/a7g5", "ON?", hostname="mqtt.eclipse.org")

#publish.single("/$SYS/a7g5", "ON?", hostname="mqtt.eclipse.org", port=1883, 
#               client_id="client-001", keepalive=60,
#               will=None, auth=None, tls=None, 
#               transport="tcp")


