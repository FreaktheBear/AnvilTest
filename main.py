import anvil.pico
import uasyncio as asyncio

from machine import Pin
from Secrets import secrets
from Anvilfn import pico_fn
from IO.DigInPullUp import IX_PU
from IO.DigOutput import QX
from IO.LM35 import read_temperature

UPLINK_KEY = secrets['uplink']

Button1 = IX_PU(6)
Button2 = IX_PU(7)
Relais1 = QX(14)

# Asynchronous main function
async def main():
    asyncio.create_task(anvil.pico.connect(UPLINK_KEY))
    asyncio.create_task(pico_fn())
    asyncio.create_task(read_temperature())

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



# There's lots more you can do with Anvil on your Pico W.
#
# See https://anvil.works/pico for more information

