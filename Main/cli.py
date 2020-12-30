'''
CLI (Command line interface for the virus scanner)
Parameters:
    |
    |__ Virus Scanner 
             |_ file name to scan 
             |_ URL to scan 
'''

import click

# Importing file from different folders 
import sys

# Config file 
sys.path.append('../')
from config import *

# Virus Total file and url
sys.path.append('../VirusTotal_API')
from VirusTotal_API_File import *
from VirusTotal_API_URL import *


@click.command()
@click.option('--VirusTotalFile', '-VTF')
@click.option('--VirusTotalURL', '-VTU')
def main(virustotalfile,virustotalurl):

    if virustotalfile: 
       '''
       Parameters (<file to scan>,<virus total api key>)
       '''
       ScanFile(virustotalfile,Virus_Total_API_key())
    
    if virustotalurl:
        '''
        Parameters (<url to scan>,<virus total api key>)
        '''
        ScanURL(virustotalurl,Virus_Total_API_key())

    

if __name__ == "__main__":
    main()