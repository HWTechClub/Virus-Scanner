'''
TODO: 
Add description of code here
'''

import requests
import sys
import time
#sys.path.append("..")
#from config import Virus_Total_API_key

'''
Parameters (<file to scan>,<virus total api key>)
'''
def ScanFile(filepath, Virus_Total_API_key):
	# scan code
	#print("Enter the file path of the file you would like to scan:")
	file = filepath


	scanUrl = 'https://www.virustotal.com/vtapi/v2/file/scan'

	scanParams = {'apikey': Virus_Total_API_key}	

	files = {'file': (file, open(file, 'rb'))}							# file to be sent
	scanResp = requests.post(scanUrl, files=files, params=scanParams)	# send file along w api key

	scanID = scanResp.json().get('scan_id')

	print("\nProcessing File...")
	time.sleep(30)					# allow for processing time	

	# report code

	reportUrl = 'https://www.virustotal.com/vtapi/v2/file/report'

	reportParams = {'apikey': Virus_Total_API_key, 'resource': scanID}		# use scanID to get file report
	reportResp = requests.get(reportUrl, params=reportParams)

	finalReport = reportResp.json()
	finalScans = finalReport['scans']		# get scans from report

	if (finalReport.get('positives') == 0):		# check if file has been flagged
		print("The file is safe!\n")

	else:
		for scan in finalScans:			# for each scan

			if (finalScans[scan].get('detected') == True):		# check if antivirus flagged file

				print(scan + " has flagged this as malicious!")	
				print(finalScans[scan].get('result'))
				print("\n\n")

	print("For a detailed analysis visit:\n" + finalReport.get('permalink') + "\n\n")

