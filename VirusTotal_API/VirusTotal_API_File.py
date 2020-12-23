import requests
import sys
sys.path.append("..")
from config import Virus_Total_API_key

# scan code

scanUrl = 'https://www.virustotal.com/vtapi/v2/file/scan'

scanParams = {'apikey': Virus_Total_API_key()}

files = {'file': ('myfile.exe', open('myfile.exe', 'rb'))}

scanResp = requests.post(scanUrl, files=files, params=scanParams)

print(scanResp.json())


# report code

reportUrl = 'https://www.virustotal.com/vtapi/v2/file/report'

reportParams = {'apikey': Virus_Total_API_key(), 'resource': '<resource>'}

reportResp = requests.get(reportUrl, params=reportParams)

print(reportResp.json())