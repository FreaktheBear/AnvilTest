#############################################
# Provide your Wifi connection details here #
#############################################



#############################################

import network
import rp2
from time import sleep
from machine import Pin
from Secrets import secrets
import ntptime

sleep(1) # Without this, the USB handshake seems to break this script and then fail sometimes.

led = Pin("LED", Pin.OUT, value=1)

# Set up Wifi connection details
ssid = secrets['ssid']
password = secrets['pw']
rp2.country('NZ')            # change to <your> country code
ip = secrets['ip']
netmask = secrets['netmask']
gateway = secrets['gateway']
dns = secrets['dns']

wlan = None
while not wlan or wlan.status() != 3:
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    wlan.ifconfig((ip,netmask,gateway,dns))

    # Blink LED slowly until the Wifi is connected.

    while True:
        print(wlan)
        led.toggle()
        sleep(0.2)
        if wlan.status() in [-1, -2, 3]:
            break

# Set the RTC to the current time
for i in range(10):
    try:
        print("Setting system time...")
        ntptime.settime()
        print(f"System time set to {ntptime.time()}")
        break
    except Exception as e:
        print(f"Failed to set system time: {e}")
        sleep(1)

# Solid LED means we're connected and ready to go
led.on()
print(wlan)

