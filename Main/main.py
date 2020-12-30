import sys
import os

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

#variable to help terminate the program
flag = True

while flag:
    #Option menu for the users
    print (
        "1.Meta defender" +"\n" +"2.Url scan "+"\n"+"3.virus total file"+"\n"+"4.virus total url"+"\n"+"5.Quit"+"\n"
    )

    choice =int(input("Enter the choice: "))

    if choice==1 :
        from Meta_Defender.MetaDefenderMain import scanFile
        scanFile()
    elif choice==2 :
        from URL_Scan_IO.URLScanIOMain import scanURL
        scanURL()

    elif choice==3:
        from VirusTotal_API.VirusTotal_API_File import ScanFile
        ScanFile()
        
    elif choice==4:
        from VirusTotal_API.VirusTotal_API_URL import scanURL
        scanURL()

    elif choice==5:
        print("Quitting!")
        flag = False
 
