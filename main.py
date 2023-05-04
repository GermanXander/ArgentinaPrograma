# Ing. Germán Andrés Xander 2023
 
from machine import Pin
import time

print("esperando pulsador")

sw = Pin(23, Pin.IN)
led = Pin(2, Pin.OUT)

contador=0
while True:
    if sw.value():
        led.value(not led.value())
        contador += 1
        print(contador)
        time.sleep_ms(5)
