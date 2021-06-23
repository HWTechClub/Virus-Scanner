'''
This program uses the VirusTotal API to scan files for any viruses. 
'''

import requests
import time
import traceback
'''
Parameters (<file to scan>,<virus total api key>,<verbose>)
'''
def ScanFile(filePath, Virus_Total_API_key,verbose):
	try:
		scanUrl = 'https://www.virustotal.com/vtapi/v2/file/scan'
		scanParams = {'apikey': Virus_Total_API_key}	

		files = {'file': (filePath, open(filePath, 'rb'))}							# file to be sent
		scanResp = requests.post(scanUrl, files=files, params=scanParams)	# send file along w api key

		scanID = scanResp.json().get('scan_id')

		print("\nPlease give us a moment to process your file, this may take upto 60 seconds\n")

		# report code

		reportUrl = 'https://www.virustotal.com/vtapi/v2/file/report'

		reportParams = {'apikey': Virus_Total_API_key, 'resource': scanID}		# use scanID to get file report
		time.sleep(10)								# give site breathing space, fixes simplejson error

		reportResp = requests.get(reportUrl, params=reportParams)

		status = True

		while status:			# true if we are waiting for the report

			if (reportResp.json().get("response_code") == -2):				# check response code
				reportResp = requests.get(reportUrl, params=reportParams)
				time.sleep(20)			# 20 second sleep timer due to virus scanner free api only permitting 4 scans/min

			else:			
				finalReport = reportResp.json()
				finalScans = finalReport["scans"]		# get scans from report

				if (verbose):			# show all scanners
					print ("Number of scanners which detected viruses: " + str(finalReport["positives"]))

					for scanner in finalScans:					# show all scanners
						print ("Scanner: 	" + scanner + "\n")
						print ("Detected: 	" + str(finalScans[scanner]["detected"]))
						if (str(finalScans[scanner]["result"]) == 'None'):
							print ("Result:   	Clean file")
						else:
							print ("Result:   	" + str(finalScans[scanner]["result"]))
						print("\n----------------------------------------------------------------------------\n")

					print ("Final Result : \n")

					if (finalReport["positives"] == 0):	# if no threat found
						print ("This file is safe")

					else:
						print("This file may contain malware. Proceed at your own risk")

				else:		# regular scan

					if (finalReport.get('positives') == 0):		# check if file has been flagged
						print("The file is safe!\n\n")

					else:

						for scan in finalScans:			# for each scan

							if (finalScans[scan].get('detected') == True):		# check if antivirus flagged file

								print(scan + " has flagged this as malicious!")	
								print(finalScans[scan].get('result'))
								print("\n\n")

				status =  False	# break loop				
				print("For a detailed analysis visit:\n" + finalReport.get('permalink') + "\n\n")

	except FileNotFoundError:
		print("This file does not exist. Please check the path and try again")

	except:
		#print("We ran into some errors. Please try again in a while")
		traceback.print_exc()
