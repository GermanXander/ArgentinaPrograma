# Germán Andrés Xander 2023

from machine import Pin
import dht
import time
import json
from collections import OrderedDict

sw = Pin(23, Pin.IN)
led = Pin(2, Pin.OUT)
d = dht.DHT22(Pin(25))
print("esperand pulsador")
contador=0

while True:
    if sw.value():
        contador+=1
        print(contador)
        led.value(not led.value())

    try:
        d.measure()
        temperatura=d.temperature()
        humedad=d.humidity()
        datos=json.dumps(OrderedDict([
            ('temperatura',temperatura),
            ('humedad',humedad)
        ]))
        print(datos)
    except OSError as e:
        print("sin sensor")

    time.sleep_ms(250)