# Germán Andrés Xander 2023

from machine import Pin, Timer, unique_id
import dht
import time
import json
import ubinascii
from collections import OrderedDict
from settings import SERVIDOR_MQTT
from umqtt.robust import MQTTClient

CLIENT_ID = ubinascii.hexlify(unique_id()).decode('utf-8')

mqtt = MQTTClient(CLIENT_ID, SERVIDOR_MQTT,
                  port=8883, keepalive=10, ssl=True)

led = Pin(2, Pin.OUT)
d = dht.DHT22(Pin(25))
Tmin = 20
Tmax = 30
bandera = True

while True:
    try:
        d.measure()
        temperatura = d.temperature()
        humedad = d.humidity()
        datos = json.dumps(OrderedDict([
            ('temperatura',temperatura),
            ('humedad',humedad)
        ]))
        print(datos)
        if temperatura > Tmax and bandera == True:
            print("publicando")
            mqtt.connect()
            mqtt.publish(f"aptest/{CLIENT_ID}",datos)
            mqtt.disconnect()
            bandera = False
        if temperatura < Tmin:
            bandera = True

    except OSError as e:
        print("sin sensor")
    time.sleep(5)
