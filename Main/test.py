import sys
import os

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))


#Option menu
print (
    "1.Meta defender" +"\n" +"2.Url scan "+"\n"+"3.virus total file"+"\n"+"4.virus total url"
)

choice =int(input("Enter the choice "))

#redircting to required api function or .py file

if choice==1 :
   from Meta_Defender.MetaDefenderMain import scanFile
   scanFile()
elif choice==2 :
    from URL_Scan_IO.URLScanIOMain import scanURL
    scanURL()
# elif choice == 3 or choice == 4:
#     class CallPy(object):

#     # choice = int(input("Enter your choice 3 or 4: "))
#         if choice == 3:
#             def __init__(self,path='..\VirusTotal_API\VirusTotal_API_File.py'): #../ added to go to parent directory
#                self.path=path
#         elif choice ==4:
#             def __init__(self,path='..\VirusTotal_API\VirusTotal_API_URL.py'): #../ added to go to parent directory
#                self.path=path
     
#         def call_python_file(self):
#             call(["python3","{}".format(self.path)])
	
#     if __name__=="__main__":
#         c=CallPy()
# 	    c.call_python_file()





