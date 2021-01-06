'''
TODO: 
The main file that the user runs to scan files and sites for viruses
'''

def mainfile():
    import sys
    import os

    PACKAGE_PARENT = '..'
    SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
    sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

    #variable to help terminate the program
    flag = True

    from pyfiglet import Figlet
    f = Figlet(font='slant')
    print (f.renderText('Virus Scanner'))

    while flag:
        #Option menu for the users
        print (
            "\n1.Meta defender" +"\n" +"2.Url scan "+"\n"+"3.virus total file"+"\n"+"4.virus total url"+"\n"+"5.Quit"
        )


        choice =int(input("\nEnter the choice: "))

        if choice==1 :
            from Meta_Defender.MetaDefenderMain import scanFile
            scanFile()
            continue
        
        elif choice==2 :
            from URL_Scan_IO.URLScanIOMain import scanURL
            scanURL()
            continue

        elif choice==3:
            from VirusTotal_API.VirusTotal_API_File import ScanFile
            ScanFile()
            continue

        elif choice==4:
            from VirusTotal_API.VirusTotal_API_URL import scanURL
            scanURL()
            continue

        elif choice==5:
            print("Quitting!")
            flag = False
    

