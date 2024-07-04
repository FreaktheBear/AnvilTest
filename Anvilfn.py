import anvil.pico
import time
import uasyncio as asyncio
from machine import Pin

# We use the LED to indicate server calls and responses.
led = Pin("LED", Pin.OUT, value=1)

# Call this function from your Anvil app:
#
#    anvil.server.call('pico_fn', 42)
#


@anvil.pico.callable_async(is_async=True, require_user=True)
async def pico_fn(n):
    # Output will go to the Pico W serial port
    print(f"Called local function with argument: {n}")

    # Blink the LED and then double the argument and return it.
    for i in range(10):
        led.toggle()
        await asyncio.sleep_ms(50)   # Sleep for 0.05 seconds
    return n * 2
