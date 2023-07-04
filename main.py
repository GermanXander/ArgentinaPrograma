# Germán Andrés Xander 2023

import urequests
response = urequests.get('https://iotunam.duckdns.org:10000/api/ultimos')
print(response.content)