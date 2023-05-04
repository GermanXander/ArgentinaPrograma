# Ing. Germán Andrés Xander 2023

from machine import Pin
import time

sw = Pin(23, Pin.IN)
led = Pin(2, Pin.OUT)

while True:
    if sw.value():
        led.value(not led.value())
        time.sleep_ms(5)
