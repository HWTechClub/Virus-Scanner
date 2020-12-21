import requests, json

'''
result =  requests.get("http://www.threatcrowd.org/searchApi/v2/email/report/", params = {"email": "william19770319@yahoo.com"})
print result.text

j = json.loads(result.text)
print j['domains'][0]
'''

print("Enter the URL you would like to scan:")
url = input()


print (requests.get("http://www.threatcrowd.org/searchApi/v2/domain/report/", {"domain": url}).text)
"""
print (requests.get("http://www.threatcrowd.org/searchApi/v2/ip/report/", {"ip": "188.40.75.132"}).text)

print (requests.get("http://www.threatcrowd.org/searchApi/v2/antivirus/report/", {"antivirus" :"plugx"}).text)
"""
