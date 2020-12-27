from urllib.parse import quote
import requests
import sys
sys.path.append("..")
from config import Meta_Defender_API_key
import hashlib
import json
import time

def scanFile():
	 
	print("Enter the file path of the file you would like to scan:")
	file = input()

	 
	urlUpload = "https://api.metadefender.com/v4/file"
	headers = {
		'apikey': Meta_Defender_API_key(),
		'content-type': 'application/octet-stream'
	}
	 
	response = requests.request("POST", urlUpload, data=file, headers=headers)
	print(response.text)	# Upload Response

	resDict = json.loads(response.text)
	dataID = resDict["data_id"]

	#print(dataID)		# Data ID of file

	time.sleep(5)

	urlScan = "https://api.metadefender.com/v4/file/bzIwMTEwNGk5dTVaUHo4c0FQbmpvNGlrUi0"

	headers = {
		'apikey': Meta_Defender_API_key()
	}

	response = requests.request("GET", urlScan, headers=headers)
	# print(response.text)		# Scan Response

	scanning_threats = response.json()["scan_results"]["scan_details"]
	if (response.json()["scan_results"]["scan_all_result_a"]!= 'No Threat Detected'):
		for obj in scanning_threats:
			if(scanning_threats[obj]["threat_found"] != ""):
				print(obj + "has reported an error.")
				print(z[obj])
	else:
		print("No threat has been detected.")

scanFile()





