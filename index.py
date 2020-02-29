#!/usr/bin/python3.7
from sensorpackage.melexis import *

sensor = Melexis() #建立seneor物件
t = sensor.readObject1() #讀取目標溫度
a = sensor.readAmbient() #讀取環境溫度