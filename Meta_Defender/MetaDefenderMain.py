import requests

url = "https://api.metadefender.com/v2/file/ZDE4MDUxMVNKTS00U0s5WFJNSDFRYlZTdGM3Uno"
headers = {
    'apikey': "a627fd093f3890c31b13d85b8955c644",
    'file-metadata': "1"
}

response = requests.request("GET", url, headers=headers)
print(response.text)
