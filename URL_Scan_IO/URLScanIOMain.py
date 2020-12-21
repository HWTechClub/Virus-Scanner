# Found some Proof of Concept code in the documentation and just added my api key to it and changed the target site
import urllib.request as urlreq
import requests
import json
import sys
sys.path.append("..") 		# Get access to config file with API keys
import config
import time

def scanURL():
	print("Enter the URL you would like to scan:")
	url = input()

	# Send req w url to scan along w API key
	headers = {'API-Key':config.URL_Scan_IO_API_Key,'Content-Type':'application/json'}
	data = {"url": url, "visibility": "public"}
	
	response = requests.post('https://urlscan.io/api/v1/scan/',headers=headers, data=json.dumps(data))
	print(response)

	time.sleep(20)						# Allow time for scanning
	
	resultUrl = response.json().get("api")		# Get result url
	print(resultUrl)

	urlResp = requests.get(resultUrl)	# Get JSON data from result link
	print(urlResp.json().get(data))


scanURL()