import requests
import sys
sys.path.append("..")
import config

url = "https://www.virustotal.com/vtapi/v2/comments/get"

querystring = {"apikey":config.Virus_Total_API_Key}

response = requests.request("GET", url, params=querystring)

print(response.text)
