'''
TODO: 
Add description of code here
'''

import requests
import time
import json

'''
Parameters (<url to scan>,<virus total api key>)
'''
def scanURL(urlLink, Virus_Total_API_key):

    scanUrl = 'https://www.virustotal.com/vtapi/v2/url/scan'				# url to request scan from
    reportUrl = 'https://www.virustotal.com/vtapi/v2/url/report'			# url to request report from

    scanParams = {"apikey":Virus_Total_API_key, 'url' : urlLink}			# sending url to be scanned
    scanResp = requests.post(scanUrl, data=scanParams)						# scan request

    scanID = scanResp.json().get('scan_id')									# getting scan ID

    print("\nProcessing URL...")			

    reportParams = {"apikey":Virus_Total_API_key, 'resource' : scanID}
    reportResp = requests.get(reportUrl, params=reportParams)				# getting report of scan ID

    x = reportResp.json()
    print("Your scan ID is " + x["scan_id"] + "\n") 
    if (x["positives"] == 0):
        print("This site is 100% safe\n")	
    else:
        print("Our scans picked up some issues with this site. Proceed with caution.More info:")
        z = x["scans"]
        for obj in z:
            if (z[obj]["detected"] != False ):
                print (obj + " has detected that it may be a " + z[obj]["result"])
                print(z[obj])
    print("\n")
    print("To get more information on the scan,paste this link in your browser\n")
    print(x["permalink"])

