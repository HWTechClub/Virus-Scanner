import requests
import sys
sys.path.append("..")
from config import Virus_Total_API_key

url = "https://www.virustotal.com/vtapi/v2/comments/get"

querystring = {"apikey":Virus_Total_API_key()}

response = requests.request("GET", url, params=querystring)

print(response.text)
