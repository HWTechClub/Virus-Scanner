import urllib.request as urlreq
import requests
import json
import sys
sys.path.append("..") 		# Get access to config file with API keys
from config import URL_Scan_IO_API_key
import time

def scanURL():
	
	print("Enter the URL you would like to scan:")
	url = input()

	# Send req w url to scan along w API key
	headers = {'API-Key':URL_Scan_IO_API_key(),'Content-Type':'application/json'}
	data = {"url": url, "visibility": "public"}
	
	response = requests.post('https://urlscan.io/api/v1/scan/',headers=headers, data=json.dumps(data))		# send req to server

	start = str(response).find("[") + len("[")	
	end = str(response).find("]")
	respCode = str(response)[start:end]			# Get response code

	if(respCode != "200"):
		print("Error in URL, it may be blacklisted or entered incorrectly.")		# if site returns error
		exit()

	try:

		print("Processing request... (May take upto 20 seconds)\n")

		time.sleep(20)						# Allow time for scanning
		
		resultUrl = response.json().get("api")		# Get result url

		urlResp = requests.get(resultUrl)	# Get JSON data from result link
		print("URL: " + url)
		print("IP: " + urlResp.json().get('page').get('ip'))
		print("Server: " + urlResp.json().get('page').get('server'))
		print("Ads Detected: " + str(urlResp.json().get('stats').get('adBlocked')))
		print("Malicious: " + str(urlResp.json().get('verdicts').get('overall').get('malicious')))	# print info

		print("\n\nFor more detailed results visit: " + resultUrl + "\n")

	except:
		print("Error something went wrong!")		# incase error occurs during result retrieval
