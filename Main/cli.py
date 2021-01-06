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
from main import *
from os import path
# Config file 
sys.path.append('../')
#checks if user has created a config file. If no config is present, it prompts the user for the API keys
if (path.isfile("../config.yaml")!= True):
    print("No config file")
    f = open("../config.yaml","w+")
    metakey = input("Enter API key for MetaDefender: ")
    virusscankey = input ("Enter API key for VirusTotal: ")
    urlscankey = input("Enter API key for URL Scan: ")
    f.write("Meta_Defender_API_key: " + metakey + "\n")
    f.write("Virus_Total_API_key:" + virusscankey + "\n")
    f.write("URL_Scan_IO_API_key: " + urlscankey + "\n")
    f.close()
 
from config import *
 
# Virus Total file and url
#sys.path.append('../VirusTotal_API')
#from VirusTotal_API_File import *
#from VirusTotal_API_URL import *
import main as m
sys.path.append('../')
import Meta_Defender.MetaDefenderMain as meta
import VirusTotal_API.VirusTotal_API_File as vfile
import VirusTotal_API.VirusTotal_API_URL as vurl
 
@click.group()
def main():
    pass
 
@main.command()
 
@click.option('--VirusTotalFile', '-VTF', help = 'Scan a file using the VirusTotal API')
@click.option('--VirusTotalURL', '-VTU', help = 'Scan a website using the VirusTotal API')
@click.option('--MetaDefender', '-M', help= 'Scan a file using the MetaDefender API' )
#@click.option('-i' , help= 'Opens in interactive command line mode')
def main(virustotalfile,virustotalurl,metadefender):
    """This is a CLI application to scan a file or a website using multiple scanners to check for any form of malware"""
    if virustotalfile: 
       '''
       Parameters (<file to scan>,<virus total api key>)
       '''
       vfile.ScanFile(virustotalfile,Virus_Total_API_key())
    
    elif virustotalurl:
        '''
        Parameters (<url to scan>,<virus total api key>)
        '''
        vurl.ScanURL(virustotalurl,Virus_Total_API_key())
    elif metadefender:
        meta.scanFile(metadefender,Meta_Defender_API_key())
   #elif interactive:
    #    m.mainfile()
    else:                                                                                          #shows help options if no options are input
        ctx = click.get_current_context()
        click.echo(ctx.get_help())
    
 
if __name__ == "__main__":
    main()