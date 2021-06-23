#-------------------------------------------------------------------------------------------------------------------------------------
# The config file is a .gitignore file to ensure that your API key stays a secret
# demonstrates to:
#   - returns data from config.yaml file 
# -------------------------------------------------------------------------------------------------------------------------------------
import yaml

# ------------------------------------------------- Reads config.yaml file ------------------------------------------------------------

def read_config():
    with open('config.yaml') as f:
      return yaml.load(f, Loader=yaml.FullLoader)

# ---------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------ Returns Meta Defender API Key ---------------------------------------------------------

def Meta_Defender_API_key():
    data = read_config()
    try:
       return data["Meta_Defender_API_key"]
    except:
        print("Error Meta Defender API key not found/invalid")
        exit()

# ----------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------ Returns Virus Total API Key ---------------------------------------------------------

def Virus_Total_API_key():
    data = read_config()
    try:
        return data["Virus_Total_API_key"]
    except:
        print("Error Virus Total API key not found/invalid")
        exit()
   

