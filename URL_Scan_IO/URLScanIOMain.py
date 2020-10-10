# Found some Proof of Concept code in the documentation and just added my api key to it and changed the target site


import requests
import json
headers = {'API-Key':'','Content-Type':'application/json'}
data = {"url": "https://hwtech.club/", "visibility": "public"}
response = requests.post('https://urlscan.io/api/v1/scan/',headers=headers, data=json.dumps(data))
print(response)
print(response.json())

