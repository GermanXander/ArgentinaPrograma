# Germán Andrés Xander 2023

from machine import Pin, Timer
import dht
import time
import json
from collections import OrderedDict

sw = Pin(23, Pin.IN)
led = Pin(2, Pin.OUT)
d = dht.DHT22(Pin(25))
print("esperand pulsador")
contador=0
estado=False

def alternar(pin):
    global contador, estado
    if sw.value():
        if not estado:
            contador+=1
            print(contador)
            led.value(not led.value())
        estado = True
    else:
        estado = False

timer1 = Timer(1)
timer1.init(period=50, mode=Timer.PERIODIC, callback=alternar)

while True:
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
    time.sleep(5)