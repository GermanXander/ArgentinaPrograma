from machine import Pin, Timer, unique_id
import dht
import time
import json
import ubinascii
from collections import OrderedDict
import urequests
from settings import TOKEN, CHATID, SERVIDOR_MQTT
from umqtt.robust import MQTTClient

CLIENT_ID = ubinascii.hexlify(unique_id()).decode('utf-8')

mqtt = MQTTClient(CLIENT_ID, SERVIDOR_MQTT,
                  port=8883, keepalive=10, ssl=True)

sw = Pin(23, Pin.IN)
led = Pin(2, Pin.OUT)
d = dht.DHT22(Pin(25))

print("esperand pulsador")
contador=0
estado=False
datos={}

def alternar(pin):
    global contador, estado
    if sw.value():
        if not estado:
            contador+=1
            print(contador)
            led.value(not led.value())
            try:
                data = {'chat_id': CHATID, 'text': datos}
                response = urequests.post("https://api.telegram.org/bot" + TOKEN + '/sendMessage', json=data)
                response.close()
                print("envio correcto a telegram")
            except:
                print("fallo en el envio a telegram")
            estado = True
        else:
            estado = False

def transmitir(pin):
    mqtt.connect()
    mqtt.publish(f"ap/{CLIENT_ID}",datos)
    mqtt.disconnect()

timer1 = Timer(1)
timer1.init(period=50, mode=Timer.PERIODIC, callback=alternar)
timer2 = Timer(2)
timer2.init(period=30000, mode=Timer.PERIODIC, callback=transmitir)

while True:
    inicio=time.time_ns()
    try:
        d.measure()
        try:
            temperatura=d.temperature()
            try:
                humedad=d.humidity()
                datos=json.dumps(OrderedDict([
                    ('temperatura',temperatura),
                    ('humedad',humedad)
                ]))
                print(datos)
            except OSError as e:
                print("sin sensor temperatura")
        except OSError as e:
            print("sin sensor humedad")
    except OSError as e:
        print("sin sensor")
    time.sleep(5)
    print('duracion: ',(time.time_ns()-inicio)/1000000, ' ms')