#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 16:54:31 2018

@author: user

Quelle: https://pypi.org/project/paho-mqtt/
"""

import paho.mqtt.publish as publish
# msgs - typles or dict
msgs = [{'topic':"$_abra$$cadabra/nö/Test", 'payload':"simple publisching"},
    ("$_abra$$cadabra/MM/Test", "multiple publisching", 0, False)]
publish.multiple(msgs, hostname="mqtt.eclipseprojects.io")