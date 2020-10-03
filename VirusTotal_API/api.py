import requests

url = "https://www.virustotal.com/vtapi/v2/comments/get"

querystring = {"apikey":"2482ba034d4adb1f76c247737491bcc3672d1884aafca71810a82e787d16e553"}

response = requests.request("GET", url, params=querystring)

print(response.text)