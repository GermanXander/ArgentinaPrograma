# Germán Andrés Xander 2023

import urequests

response = urequests.get('https://www.smn.gob.ar/')
inicio=response.content.decode('UTF-8').find("localStorage.setItem('token', ")
fin=response.content.decode('UTF-8').find("'",inicio+32)
token=response.content.decode('UTF-8')[inicio+31:fin]
encabezado={'Authorization': f'JWT {token}'}
datos=urequests.get('https://ws1.smn.gob.ar/v1/weather/location/9743', headers=encabezado)
print(datos.json())
temperatura=f"{datos.json()['temperature']}".replace('.', ',')
print(f"Temperatura {temperatura} C")