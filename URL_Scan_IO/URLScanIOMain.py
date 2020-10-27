# Found some Proof of Concept code in the documentation and just added my api key to it and changed the target site
import requests
import json
import sys
sys.path.append("..")
import config
import argparse 
parser=argparse.ArgumentParser()
parser.add_argument("--url",help="enter the url")
args=parser.parse_args()
headers = {'API-Key':config.URL_Scan_IO_API_Key,'Content-Type':'application/json'}
data = {"url": args.url, "visibility": "public"}
response = requests.post('https://urlscan.io/api/v1/scan/',headers=headers, data=json.dumps(data))
print(response)
print(response.json())

