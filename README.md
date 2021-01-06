# Virus-Scanner
Open source virus scanner built using python and various APIs

## Install requirements 
```
pip install -r requirements.txt
//Or 
pip3 install -r requirements.txt
```

## Create config file 
Create a file called config.yaml and add the following information 
```
Meta_Defender_API_key: <api_key>
Virus_Total_API_key: <api_key>
```


## Running the program

python3 ./Main/cli.py

This is the main program, main.py is not to be used directly by the user.

## TODO 
1. Check if website exists when scanning URLs
