''' 
This program uses the VirusTotal API to scan files for any viruses.
'''

import requests
import time
import json
import traceback
'''
Parameters (<url to scan>,<virus total api key>,<verbose>)
'''
def ScanURL(urlLink, Virus_Total_API_key,verbose):
	try:
		scanUrl = 'https://www.virustotal.com/vtapi/v2/url/scan'				# url to request scan from
		reportUrl = 'https://www.virustotal.com/vtapi/v2/url/report'			# url to request report from

		scanParams = {"apikey":Virus_Total_API_key, 'url' : urlLink}			# sending url to be scanned
		scanResp = requests.post(scanUrl, data=scanParams)						# scan request

		scanID = scanResp.json().get('scan_id')									# getting scan ID

		print("\nProcessing URL...")			

		reportParams = {"apikey":Virus_Total_API_key, 'resource' : scanID}
		reportResp = requests.get(reportUrl, params=reportParams)				# getting report of scan ID

		getRequest = reportResp.json()
		print("Your scan ID is " + getRequest["scan_id"] + "\n") 

		if (verbose):													# if user selected verbose scan
			print ("Number of scanners which detected viruses: " + str(getRequest["positives"]))
			scan = getRequest["scans"]

			for scanner in scan:								# show results of all scanners
				print ("Result of scanner " + scanner + '\n')
				print(scan[scanner])

			print ("Result: \n")

			if (getRequest["positives"]==0):
				print("This site is safe")

			else:
				print("This site may contain malware.Proceed at your own risk")

		else:    		# regular scan

			if (getRequest["positives"] == 0):
				print("This site is 100% safe\n")	

			else:
				print("Our scans picked up some issues with this site. Proceed with caution.More info:")
				z = getRequest["scans"]

				for obj in z:

					if (z[obj]["detected"] != False ):		# only show scanners flagged positive

						print (obj + " has detected that it may be a " + z[obj]["result"])
						print(z[obj])
		print("\n")
		print("To get more information on the scan,paste this link in your browser\n")
		print(getRequest["permalink"])
		
	except:
		print("We ran into some errors.Please try again")
		#traceback.print_exc()