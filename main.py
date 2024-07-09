#import anvil.pico
import uasyncio as asyncio
from machine import Pin
from Anvilfn import anvilconnect
from IO.DigInPullUp import IX_PU
from IO.DigOutput import QX
from IO.LM35 import read_temperature


Button1 = IX_PU(6)
Button2 = IX_PU(7)
Relais1 = QX(14)

# Asynchronous main function
async def main():
    asyncio.create_task(read_temperature())
    asyncio.create_task(anvilconnect())

    while True:
        try:
            if Button1.pin() != 1:
                Button1.pin(1)
                print("Input 0 active")
                # Pulse Output 0
                Relais1.on()
                await asyncio.sleep_ms(100)   # Sleep for 0.1 seconds 
                Relais1.off()
                await asyncio.sleep_ms(100)   # Sleep for 0.1 seconds
        except OSError as e:
            print('Main error')
        await asyncio.sleep_ms(100)   # Sleep for 0.1 seconds

try:
    asyncio.run(main())  # Run the main asynchronous function
except OSError as e:
    print('Runtime error')
finally:
    asyncio.new_event_loop() #Create a new event loop


"""
import anvil.pico
import uasyncio as a
from machine import Pin
from Secrets import secrets

# This is an example Anvil Uplink script for the Pico W.
# See https://anvil.works/pico for more information

UPLINK_KEY = secrets['uplink']

# We use the LED to indicate server calls and responses.
led = Pin("LED", Pin.OUT, value=1)


# Call this function from your Anvil app:
#
#    anvil.server.call('pico_fn', 42)
#

@anvil.pico.callable(is_async=True)
async def pico_fn(n):
    # Output will go to the Pico W serial port
    print(f"Called local function with argument: {n}")

    # Blink the LED and then double the argument and return it.
    for i in range(10):
        led.toggle()
        await a.sleep_ms(50)
    return n * 2

# Connect the Anvil Uplink. In MicroPython, this call will block forever.

anvil.pico.connect(UPLINK_KEY)


# There's lots more you can do with Anvil on your Pico W.
#
# See https://anvil.works/pico for more information
"""

