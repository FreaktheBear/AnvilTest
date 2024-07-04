# Digital Output Class (QX OpenPLC)

"""
# Example usage:
output_pin = QX(4)  # Assuming GPIO pin 4 is used
output_pin.on()  # Set the pin to high
output_pin.off()  # Set the pin to low
output_pin.toggle()  # Toggle the pin state
print(output_pin.value())  # Print the current value of the pin (1 or 0)
"""

from machine import Pin

class QX:
    def __init__(self, pin_num):
        self.pin = Pin(pin_num, Pin.OUT)
        self.off()  # Initialize the pin to a low state
    
    def on(self):
        self.pin.on()
    
    def off(self):
        self.pin.off()
    
    def toggle(self):
        self.pin.value(not self.pin.value())
    
    def value(self, val=None):
        if val is None:
            return self.pin.value()
        else:
            self.pin.value(val)
