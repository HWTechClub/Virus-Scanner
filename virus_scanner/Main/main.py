"""
The main file that the user runs to scan files and sites for viruses
"""


def mainfile(verbose):
    import sys
    import os
    from PyInquirer import prompt

    PACKAGE_PARENT = ".."
    SCRIPT_DIR = os.path.dirname(
        os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__)))
    )
    sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))
    sys.path.append("../")
    import config

    if os.path.isfile("config.yaml") != True:
        print("No config file")
        f = open("config.yaml", "w+")
        metakey = input("Enter API key for MetaDefender: ")
        virusscankey = input("Enter API key for VirusTotal: ")
        f.write("Meta_Defender_API_key: " + metakey + "\n")
        f.write("Virus_Total_API_key:" + virusscankey + "\n")
        f.close()
    # variable to help terminate the program
    flag = True

    from pyfiglet import Figlet

    f = Figlet(font="slant")

    choices = [
        "Meta defender File Scan",
        "Virus Total File Scan",
        "Virus Total Url Scan",
        "Exit",
    ]

    questions = [
        {
            "type": "list",
            "name": "choice",
            "message": "What do you want to do?",
            "default": 3,
            "choices": choices,
        }
    ]

    def cls():
        os.system("cls" if os.name == "nt" else "clear")

    cls()
    print(f.renderText("Virus Scanner"))
    while flag:
        answers = prompt(questions)
        choice = answers.get("choice")
        try:
            if choice == choices[0]:
                cls()
                print(f.renderText("Virus Scanner"))

                from Meta_Defender.MetaDefenderMain import scanFile

                filepath = input("Please enter the path of the file to scan: ")
                scanFile(filepath, config.Meta_Defender_API_key(), verbose)

                print("\n")
                continue

            elif choice == choices[1]:
                cls()
                print(f.renderText("Virus Scanner"))

                from VirusTotal_API.VirusTotal_API_File import ScanFile

                filepath = input("Please enter the path of the file to scan: ")
                ScanFile(filepath, config.Virus_Total_API_key(), verbose)

                print("\n")
                continue

            elif choice == choices[2]:
                cls()
                print(f.renderText("Virus Scanner"))

                from VirusTotal_API.VirusTotal_API_URL import ScanURL

                url = input("Please enter the URL of the site to scan: ")
                ScanURL(url, config.Virus_Total_API_key(), verbose)

                print("\n")
                continue

            elif choice == choices[3]:
                print("Quitting!")
                flag = False
            else:
                print("Invalid option")
        except ValueError:
            print("Please enter a valid option")
            flag = False
