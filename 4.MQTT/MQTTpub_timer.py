#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 13:04:50 2018

@author: user
"""

from threading import Timer
import time
import datetime
import socket
import paho.mqtt.publish as publish

zaeler = 0
zaelerBekannt = 0

class myTimer():

   def __init__(self,t,hFunction):
      self.t=t
      self.hFunction = hFunction
      self.thread = Timer(self.t,self.handle_function)

   def handle_function(self):
      self.hFunction()
      self.thread = Timer(self.t,self.handle_function)
      self.thread.start()

   def start(self):
      self.thread.start()

   def cancel(self):
      self.thread.cancel()

def printer():
    topic = "$_abra$$cadabra/MM/Test"

    currentDT = datetime.datetime.now()
    host = socket.gethostbyname(socket.gethostname())
    msg = 'Hallo von 1. ' + host + '! Jetzt ist es ' + str(currentDT)
    print ('send: ' + msg)
    #publish.single(topic, msg, hostname="mqtt.eclipseprojects.io")
    publish.single(topic, msg, hostname="test.mosquitto.org")


t = myTimer(15,printer)
t.start()


time.sleep(60)
t.cancel()









