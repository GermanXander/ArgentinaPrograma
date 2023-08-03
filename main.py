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
estado = False
temperatura = 0
humedad = -1

def alternar(pin):
    global contador, estado, temperatura, humedad
    if sw.value():
        if not estado:
            try:
                d.measure()
                if humedad < 0:
                    temperatura = d.temperature()
                    humedad = d.humidity()
                    print("1er medicion")
                else:
                    temperatura = (temperatura + d.temperature())/2
                    humedad = (humedad + d.humidity())/2
                    print("2da medicion")
                    datos = json.dumps(OrderedDict([
                        ('temperatura',temperatura),
                        ('humedad',humedad)
                    ]))
                    print(datos)
                    humedad = -1
            except OSError as e:
                print("sin sensor")

        estado = True
    else:
        estado = False

timer1 = Timer(1)
timer1.init(period=50, mode=Timer.PERIODIC, callback=alternar)

while True:
    time.sleep(1)