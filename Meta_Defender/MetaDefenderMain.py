'''
TODO: 
This program uses the MetaDegfender API to scan viruses.
'''

import requests
import json
import time

'''
Parameters (<file to scan>,<virus total api key>)
'''
def scanFile(filePath,Meta_Defender_API_key,verbose):
	try:
		binFile = open(filePath, 'rb')
		
		urlUpload = "https://api.metadefender.com/v4/file"
		headers = {
			'apikey': Meta_Defender_API_key,
			'content-type': 'application/octet-stream'
		}
		
		response = requests.request("POST", urlUpload, data= binFile, headers=headers)
		
		print ("\nPlease wait while your file is being scanned. This may take upto 60 seconds.")
		resDict = json.loads(response.text)
		dataID = resDict["data_id"]				# Data ID of file

		urlScan = "https://api.metadefender.com/v4/file/" + dataID

		headers = {
			'apikey': Meta_Defender_API_key
		}
		
		response = requests.request("GET", urlScan, headers=headers)

		progress = response.json().get("scan_results").get("progress_percentage")
		status = True

		while status:

			if (progress != 100):
				response = requests.request("GET", urlScan, headers=headers)
				progress = response.json().get("scan_results").get("progress_percentage")
				time.sleep(3)

			else:
				scanning_threats = response.json()["scan_results"]["scan_details"]

				if (response.json()["scan_results"]["scan_all_result_a"]!= 'No Threat Detected'):
					for obj in scanning_threats:
						if(scanning_threats[obj]["threat_found"] != ""):
							print(obj + "has reported an error.")
							print(scanning_threats[obj])
				else:
					print("No threat has been detected.")

				status = False
	except FileNotFoundError:
		print("This file does not exist. Please check the path and try again")
	except:
		print("We ran into some errors. Please try again in a while")
	








