# Digital Pull Up Input Class (IX OpenPLC)

from machine import Pin

class IX_PU:
    def __init__(self, pin_num):
        self.pin = Pin(pin_num, Pin.IN, Pin.PULL_UP)
        
    def value(self):
        return self.pin.value()
