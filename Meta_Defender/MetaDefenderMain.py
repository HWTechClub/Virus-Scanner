from urllib.parse import quote
import requests
import sys
sys.path.append("..")
import config
import hashlib
import json
import time

def scanFile():
	 
	print("Enter the file path of the file you would like to scan:")
	file = input()

	 
	urlUpload = "https://api.metadefender.com/v4/file"
	headers = {
		'apikey': config.Meta_Defender_API_Key,
		'content-type': 'application/octet-stream'
	}
	 
	response = requests.request("POST", urlUpload, data=file, headers=headers)
	print(response.text)	# Upload Response

	resDict = json.loads(response.text)
	dataID = resDict["data_id"]

	print(dataID)		# Data ID of file

	time.sleep(5)

	urlScan = "https://api.metadefender.com/v4/file/bzIwMTEwNGk5dTVaUHo4c0FQbmpvNGlrUi0"

	headers = {
		'apikey': config.Meta_Defender_API_Key
	}

	response = requests.request("GET", urlScan, headers=headers)
	print(response.text)		# Scan Response


scanFile()