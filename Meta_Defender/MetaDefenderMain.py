import requests
import sys
sys.path.append("..")
import config
import argparse
import hashlib
from urllib.parse import quote
 
#parser = argparse.ArgumentParser()
#parser.add_argument("--verbosity", help="increase output verbosity")
#args = parser.parse_args()
#if args.verbosity:
# print("verbosity turned on")
file='https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png'
 
h = hashlib.md5()
h.update(file.encode('utf-8'))
print(h.hexdigest())
 
url = "https://api.metadefender.com/v4/file/{0}".format("./googlelogo_color_272x92dp.png")
headers = {
 'apikey': config.Meta_Defender_API_Key,
 'content-type': 'multipart/form-data'
}
 
response = requests.request("GET", url, headers=headers)
print(response.text)