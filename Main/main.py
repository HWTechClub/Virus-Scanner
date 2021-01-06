'''
The main file that the user runs to scan files and sites for viruses
'''

def mainfile():
    import sys
    import os

    PACKAGE_PARENT = '..'
    SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
    sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

    if (os.path.isfile("../config.yaml")!= True):
        print("No config file")
        f = open("../config.yaml","w+")
        metakey = input("Enter API key for MetaDefender: ")
        virusscankey = input ("Enter API key for VirusTotal: ")
        f.write("Meta_Defender_API_key: " + metakey + "\n")
        f.write("Virus_Total_API_key:" + virusscankey + "\n")
        f.close()
    #variable to help terminate the program
    flag = True

    from pyfiglet import Figlet
    f = Figlet(font='slant')
    print (f.renderText('Virus Scanner'))


    while flag:
        #Option menu for the users
      
        print (
            "\n1.Meta defender" +"\n"+"2.virus total file"+"\n"+"3.virus total url"+"\n"+"4.Quit"
        )


        choice =int(input("\nEnter the choice: "))

        if choice==1 :
            from Meta_Defender.MetaDefenderMain import scanFile
            scanFile()
            continue
        
        elif choice==2 :
           	from VirusTotal_API.VirusTotal_API_File import ScanFile
            ScanFile()
            continue

        elif choice==3:
            from VirusTotal_API.VirusTotal_API_URL import scanURL
            scanURL()
            continue

        elif choice==4:
            print("Quitting!")
            flag = False
        else:
            print("Invalid option")
    

