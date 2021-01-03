'''
TODO: 
The main file that the user runs to scan files and sites for viruses
'''

import sys
import os

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

#variable to help terminate the program
flag = True
	

# Function gets URL or File path from user based off of option they select
def getInput(inputType):			
	
	if(inputType == "file"):

		print("Enter the path of the file you would like to scan: ")
		filePath = input()

		return filePath
	
	elif (inputType == "url"):

		print("Enter the URL you would like to scan: ")
		urlLink = input()

		return urlLink


from pyfiglet import Figlet
f = Figlet(font='slant')
print (f.renderText('Virus Scanner'))

while flag:
    #Option menu for the users
    print (
        "\n1. Meta defender File Scan" +"\n" +"2. Url Scan IO"+"\n"+
        "3. Virus Total File Scan"+"\n"+"4. Virus Total Url Scan"+"\n"+"5. Quit"
    )


    choice =int(input("\nEnter the choice: "))

    if choice==1 :

        from Meta_Defender.MetaDefenderMain import scanFile
        from config import Meta_Defender_API_key

        filePath = getInput("file")
        scanFile(filePath, Meta_Defender_API_key())
        continue
    
    elif choice==2 :

        from URL_Scan_IO.URLScanIOMain import scanURL
        from config import URL_Scan_IO_API_key

        urlLink = getInput("url")
        scanURL(urlLink, URL_Scan_IO_API_key())
        continue

    elif choice==3:

        from VirusTotal_API.VirusTotal_API_File import scanFile
        from config import Virus_Total_API_key

        filePath = getInput("file")
        scanFile(filePath, Virus_Total_API_key())
        continue

    elif choice==4:

        from VirusTotal_API.VirusTotal_API_URL import scanURL
        from config import Virus_Total_API_key

        urlLink = getInput("url")
        scanURL(urlLink, Virus_Total_API_key())
        continue

    elif choice==5:

        print("Quitting!")
        flag = False
 
