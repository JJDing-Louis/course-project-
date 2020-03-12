#!evn01/Scripts/python3.8
""" docString"""


from gpiozero import Button
from sensorpackage.Melexis import Melexis  #0309修改過

button = Button(18)
while True:
    sensor = Melexis()
    if button.is_pressed:
        temp=Melexis.btnPress()


