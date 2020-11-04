from urllib.parse import quote
import requests
import sys
sys.path.append("..")
import config
import argparse
import hashlib
import json
import time
 
#parser = argparse.ArgumentParser()
#parser.add_argument("--verbosity", help="increase output verbosity")
#args = parser.parse_args()
#if args.verbosity:
# print("verbosity turned on")
file='https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png'

localFile = "/home/pc/Documents/TechClub/Virus-Scanner/Meta_Defender/googlelogo_color_272x92dp.png"
# Replace this w value from argparse

h = hashlib.md5()
h.update(file.encode('utf-8'))
print(h.hexdigest())
 
urlUpload = "https://api.metadefender.com/v4/file"
headers = {
	'apikey': config.Meta_Defender_API_Key,
	'content-type': 'application/octet-stream'
}
 
response = requests.request("POST", urlUpload, data=localFile, headers=headers)
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

