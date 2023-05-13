# Germán Andrés Xander 2023

from machine import Pin
import dht

d = dht.DHT22(Pin(25))
d.measure()
temperatura=d.temperature()
print(f"la temperatura actual es de {temperatura} °C")
humedad=d.humidity()
print(f"la humedad actual es de {humedad} %")
