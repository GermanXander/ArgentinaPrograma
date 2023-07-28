# Germán Andrés Xander 2023
 
from machine import Pin, Timer
import time
time.sleep(2)

led = Pin(2, Pin.OUT)
contador=0

def latir(nada):
  global contador
  print(contador)
  if contador > 3:
    pulsos.deinit()
    contador=0
    return
  led.value(not led.value())
  contador +=1

def heartbeat(nada):
  pulsos.init(period=150, mode=Timer.PERIODIC, callback=latir)

periodo = Timer(0)
periodo.init(period=1000, mode=Timer.PERIODIC, callback=heartbeat)
pulsos = Timer(3)
