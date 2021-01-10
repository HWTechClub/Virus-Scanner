'''
TODO: 
This program uses the MetaDegfender API to scan viruses.
'''

import requests
import json
import time
import traceback

'''
Parameters (<file to scan>,<virus total api key>)
'''
def scanFile(filePath,Meta_Defender_API_key,verbose):
	try:
		binFile = open(filePath, 'rb')		# open file binary
		
		urlUpload = "https://api.metadefender.com/v4/file"
		headers = {
			'apikey': Meta_Defender_API_key,
			'content-type': 'application/octet-stream'
		}
		
		response = requests.request("POST", urlUpload, data= binFile, headers=headers)
		
		print ("\nPlease wait while your file is being scanned. This may take upto 60 seconds.")
		resDict = json.loads(response.text)
		dataID = resDict["data_id"]				# Data ID of file

		urlScan = "https://api.metadefender.com/v4/file/" + dataID	# req report link for file

		headers = {
			'apikey': Meta_Defender_API_key
		}
		
		response = requests.request("GET", urlScan, headers=headers)

		progress = response.json().get("scan_results").get("progress_percentage")	# report %
		status = True

		while status:		# true if we have not received report 

			if (progress != 100):		# check if report ready
				response = requests.request("GET", urlScan, headers=headers)
				progress = response.json().get("scan_results").get("progress_percentage")
				time.sleep(10)

			else:		# if report is ready

				scanning_threats = response.json()["scan_results"]["scan_details"]

				if verbose:				# show all scanners

					for obj in scanning_threats:

						if(scanning_threats[obj]["threat_found"] != ""):	# all scanners that detect malicious code
							print(obj + "has reported an error.")
							print(scanning_threats[obj])
							print("\n")

						else:												# scanners finding the file safe
							print(obj + "has reported the file as safe.")
							print(scanning_threats[obj])
							print("\n")

				else:	

					if (response.json()["scan_results"]["scan_all_result_a"]!= 'No Threat Detected'):	# check if threat found

						for obj in scanning_threats:

							if(scanning_threats[obj]["threat_found"] != ""):	# all scanners where threat found
								print(obj + "has reported an error.")
								print(scanning_threats[obj])
					else:
						print("No threat has been detected.")

				status = False	# break loop

	except FileNotFoundError:
		print("This file does not exist. Please check the path and try again")
	except:
		print("We ran into some errors. Please try again in a while")
		#traceback.print_exc()						#for debugging
	








