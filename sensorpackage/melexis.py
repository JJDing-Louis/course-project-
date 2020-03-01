import Adafruit_GPIO.I2C as I2C
import gpiozero import Button
# I2C.require_repeated_start()

class Melexis:
    def __init__(self, address=0x5A):
        self._i2c = I2C.Device(address, busnum=1)
    '''環境溫度'''
    def readAmbient(self):
        return self._readTemp(0x06)
    '''目標溫度'''
    def readObject1(self):
        return self._readTemp(0x07)

    def readObject2(self):
        return self._readTemp(0x08)

    def _readTemp(self, reg):
        temp = self._i2c.readS16(reg)
        temp = temp * .02 - 273.15
        return temp

    def btnPress(self): #按鈕偵聽程式
        sensor = Melexis()
        t = sensor.readObject1()
        a = sensor.readAmbient()
        print("Object: {}C , Ambiant: {}C".format(round(t, 3), round(a, 3)))
        return t


# if name == "main":
sensor = Melexis()
btn = Button(2)
if btn.is_pressed: #此步驟設定按鈕偵聽量測
    temp = btnPress()
t = sensor.readObject1()
a = sensor.readAmbient()

