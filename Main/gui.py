'''
TODO: 
Add description of code here
'''

import sys
import os

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

#importing tkinter from library 
from tkinter import *

#defining all the functions
def meta():
    from Meta_Defender.MetaDefenderMain import scanFile
    scanFile()
def url():
    from URL_Scan_IO.URLScanIOMain import scanURL
    scanURL()
def vtFile():
    from VirusTotal_API.VirusTotal_API_File import ScanFile
    ScanFile()
def vtUrl():
    from VirusTotal_API.VirusTotal_API_URL import scanURL
    scanURL()

#make the gui
window=Tk()
window.title("VIRUS SCANNER")
window.geometry("600x600")

#Adding a label 
Label(window, text="Choose the option u would like",font=16).grid(row=0,column=0,sticky=W)

#Add a button
Button(window,text="1.Meta Defender",width=16, command=meta).grid(row=1,column=0,sticky=W)
Button(window,text="2.Url scan",width=16, command=url).grid(row=2,column=0,sticky=W)
Button(window,text="3.virus total file",width=16, command=vtFile).grid(row=3,column=0,sticky=W)
Button(window,text="4.virus total url",width=16, command=vtUrl).grid(row=4,column=0,sticky=W)
window.mainloop()