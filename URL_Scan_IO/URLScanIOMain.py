# Found some Proof of Concept code in the documentation and just added my api key to it and changed the target site


import requests
import json
headers = {'API-Key':'5ebb7b3c-3ec1-44c6-8aaa-ecaac5b81951','Content-Type':'application/json'}
data = {"url": "https://hwtech.club/", "visibility": "public"}
response = requests.post('https://urlscan.io/api/v1/scan/',headers=headers, data=json.dumps(data))
print(response)
print(response.json())

