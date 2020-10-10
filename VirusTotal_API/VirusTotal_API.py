import requests

url = "https://www.virustotal.com/vtapi/v2/comments/get"

querystring = {"apikey":""}

response = requests.request("GET", url, params=querystring)

print(response.text)
