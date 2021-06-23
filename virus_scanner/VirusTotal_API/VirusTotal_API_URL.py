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
#        try:
#            if urlLink.startswith('http://') or urlLink.startswith('https://'):
#                request = requests.get(urlLink)
#            else:
#                request = requests.get('http://' + urlLink)
#            if (request.status_code == 200):
#                pass
#            else:
#                print("This site may not exist or may be offline. If you are sure it exists, please copy the full link.If you own this site, please contact your network administrator or check if your site is online")
#                exit()
#        except:
#            print("This site may not exist or may be offline. If you are sure it exists, please copy the full link.If you own this site, please contact your network administrator or check if your site is online")
#            exit()
        scanUrl = 'https://www.virustotal.com/vtapi/v2/url/scan'				# url to request scan from
        reportUrl = 'https://www.virustotal.com/vtapi/v2/url/report'			# url to request report from

        scanParams = {"apikey":Virus_Total_API_key, 'url' : urlLink}			# sending url to be scanned
        scanResp = requests.post(scanUrl, data=scanParams)						# scan request

        scanID = scanResp.json().get('scan_id')									# getting scan ID

        print("\nProcessing URL...")			

        reportParams = {"apikey":Virus_Total_API_key, 'resource' : scanID}
        reportResp = requests.get(reportUrl, params=reportParams)				# getting report of scan ID

        time.sleep(10)                                                          #gives site breathing space        

        getRequest = reportResp.json()
        print("Your scan ID is " + getRequest["scan_id"] + "\n") 

        if (verbose):													# if user selected verbose scan
            print ("Number of scanners which detected viruses: " + str(getRequest["positives"]))
            scan = getRequest["scans"]

            for scanner in scan:								# show results of all scanners
                print ("Scanner:    " + scanner + '\n') 
                print("Detected:    " + str(scan[scanner]["detected"]) + "\n")
                print("Result:      " + scan[scanner]["result"] + "\n")
                print("\n----------------------------------------------------------------------------\n")

            print ("Final Result: \n")

            if (getRequest["positives"]==0):
                print("This site is safe")

            else:
                print("This site may contain malware.Proceed at your own risk")

        else:    		# regular scan

            if (getRequest["positives"] == 0):
                print("This site is 100% safe\n")	

            else:
                print("Our scans picked up some issues with this site. Proceed with caution.More info:")
                scan = getRequest["scans"]

                for scanner in scan:

                    if (scan[scanner]["detected"] != False ):		# only show scanners flagged positive

                        print (scanner + " has detected that it may be a " + scan[scanner]["result"])
                        print(scan[scanner])
        print("\n")
        print("To get more information on the scan,paste this link in your browser\n")
        print(getRequest["permalink"])
		
    except:
        #print("We ran into some errors.Please try again")
        traceback.print_exc()                      #for debugging