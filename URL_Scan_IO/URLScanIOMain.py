'''
TODO: 
Add description of code here
'''

import requests
import json
import time

'''
Parameters (<url to scan>,<virus total api key>)
'''
def scanURL(urlLink, URL_Scan_IO_API_key):
	
	# Send req w url to scan along w API key
	headers = {'API-Key':URL_Scan_IO_API_key,'Content-Type':'application/json'}
	data = {"url": urlLink, "visibility": "public"}
	
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
