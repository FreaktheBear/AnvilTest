#############################################
# Provide your Wifi connection details here #
#############################################

WIFI_SSID = "My Wireless Network Name"
WIFI_PASSWORD = "password_goes_here"

#############################################

import network
from time import sleep
from machine import Pin
import ntptime
from Secrets import secrets

sleep(1) # Without this, the USB handshake seems to break this script and then fail sometimes.

led = Pin("LED", Pin.OUT, value=1)

# Set up Wifi connection details
ssid = secrets['ssid']
password = secrets['pw']
ip = secrets['ip']
netmask = secrets['netmask']
gateway = secrets['gateway']
dns = secrets['dns']

wlan = None
while not wlan or wlan.status() != 3:
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    wlan.ifconfig((ip, netmask, gateway, dns))

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

