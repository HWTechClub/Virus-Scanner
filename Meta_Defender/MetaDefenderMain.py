import requests
import sys
sys.path.append("..")
import config

url = "https://api.metadefender.com/v2/file/ZDE4MDUxMVNKTS00U0s5WFJNSDFRYlZTdGM3Uno"
headers = {
    'apikey': config.Meta_Defender_API_Key,
    'file-metadata': "1"
}

response = requests.request("GET", url, headers=headers)
print(response.text)
