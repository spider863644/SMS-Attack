import urllib.parse
try:
    import urllib.request
except:
    os.system("pip install --upgrade pip")
    os.system("pip install urllib2")
try:
   
    from infobip_api_client.api_client import ApiClient, Configuration
except:
    print("Error: \nSome requirements are missing\n\nRun pip install -r requirements.txt")
    exit()
from infobip_api_client.model.sms_advanced_textual_request import SmsAdvancedTextualRequest
from infobip_api_client.model.sms_destination import SmsDestination
from infobip_api_client.model.sms_response import SmsResponse
from infobip_api_client.model.sms_textual_message import SmsTextualMessage
from infobip_api_client.api.send_sms_api import SendSmsApi
from infobip_api_client.exceptions import ApiException
try:
    import phonenumbers
    import os
    import datetime
    import time as t
    import colorama
    from colorama import *
    colorama.init(autoreset=True)
    import requests
    import json
except:
    print("Some requirements are missing\nRun pip install -r requirements. txt")
    exit()
header = """

          _____                    _____                    _____                    _____                _____                _____                    _____                    _____                    _____          
         /\    \                  /\    \                  /\    \                  /\    \              /\    \              /\    \                  /\    \                  /\    \                  /\    \         
        /::\    \                /::\____\                /::\    \                /::\    \            /::\    \            /::\    \                /::\    \                /::\    \                /::\____\        
       /::::\    \              /::::|   |               /::::\    \              /::::\    \           \:::\    \           \:::\    \              /::::\    \              /::::\    \              /:::/    /        
      /::::::\    \            /:::::|   |              /::::::\    \            /::::::\    \           \:::\    \           \:::\    \            /::::::\    \            /::::::\    \            /:::/    /         
     /:::/\:::\    \          /::::::|   |             /:::/\:::\    \          /:::/\:::\    \           \:::\    \           \:::\    \          /:::/\:::\    \          /:::/\:::\    \          /:::/    /          
    /:::/__\:::\    \        /:::/|::|   |            /:::/__\:::\    \        /:::/__\:::\    \           \:::\    \           \:::\    \        /:::/__\:::\    \        /:::/  \:::\    \        /:::/____/           
    \:::\   \:::\    \      /:::/ |::|   |            \:::\   \:::\    \      /::::\   \:::\    \          /::::\    \          /::::\    \      /::::\   \:::\    \      /:::/    \:::\    \      /::::\    \           
  ___\:::\   \:::\    \    /:::/  |::|___|______    ___\:::\   \:::\    \    /::::::\   \:::\    \        /::::::\    \        /::::::\    \    /::::::\   \:::\    \    /:::/    / \:::\    \    /::::::\____\________  
 /\   \:::\   \:::\    \  /:::/   |::::::::\    \  /\   \:::\   \:::\    \  /:::/\:::\   \:::\    \      /:::/\:::\    \      /:::/\:::\    \  /:::/\:::\   \:::\    \  /:::/    /   \:::\    \  /:::/\:::::::::::\    \ 
/::\   \:::\   \:::\____\/:::/    |:::::::::\____\/::\   \:::\   \:::\____\/:::/  \:::\   \:::\____\    /:::/  \:::\____\    /:::/  \:::\____\/:::/  \:::\   \:::\____\/:::/____/     \:::\____\/:::/  |:::::::::::\____\
\:::\   \:::\   \::/    /\::/    / ~~~~~/:::/    /\:::\   \:::\   \::/    /\::/    \:::\  /:::/    /   /:::/    \::/    /   /:::/    \::/    /\::/    \:::\  /:::/    /\:::\    \      \::/    /\::/   |::|~~~|~~~~~     
 \:::\   \:::\   \/____/  \/____/      /:::/    /  \:::\   \:::\   \/____/  \/____/ \:::\/:::/    /   /:::/    / \/____/   /:::/    / \/____/  \/____/ \:::\/:::/    /  \:::\    \      \/____/  \/____|::|   |          
  \:::\   \:::\    \                  /:::/    /    \:::\   \:::\    \               \::::::/    /   /:::/    /           /:::/    /                    \::::::/    /    \:::\    \                    |::|   |          
   \:::\   \:::\____\                /:::/    /      \:::\   \:::\____\               \::::/    /   /:::/    /           /:::/    /                      \::::/    /      \:::\    \                   |::|   |          
    \:::\  /:::/    /               /:::/    /        \:::\  /:::/    /               /:::/    /    \::/    /            \::/    /                       /:::/    /        \:::\    \                  |::|   |          
     \:::\/:::/    /               /:::/    /          \:::\/:::/    /               /:::/    /      \/____/              \/____/                       /:::/    /          \:::\    \                 |::|   |          
      \::::::/    /               /:::/    /            \::::::/    /               /:::/    /                                                         /:::/    /            \:::\    \                |::|   |          
       \::::/    /               /:::/    /              \::::/    /               /:::/    /                                                         /:::/    /              \:::\____\               \::|   |          
        \::/    /                \::/    /                \::/    /                \::/    /                                                          \::/    /                \::/    /                \:|   |          
         \/____/                  \/____/                  \/____/                  \/____/                                                            \/____/                  \/____/                  \|___|          
                                                                                                                                                                                                                         
"""
def loop():
    os.system ("clear")
    print(Fore.GREEN + header)
    print(Fore.RED + "Version 1.2".center(70))
    print(Fore.CYAN + """
  Coded by: Spider Anongreyhat & TheNooB
  Team: TermuxHackz Society
  WhatsApp: +2349052863644 & +233245222358
  GitHub: spider863644
""")
    def free_trial():
        print(Fore.RED + "Note:\n If you are finding it hard to send SMS, kindly make use of a strong VPN")
        country_code = input(Fore.GREEN + " \n\nEnter target country code: " + Fore.YELLOW)
        if "+" not in country_code:
            print (Fore.RED + "Error:\nAdd + to country code!")
            t.sleep (3)
            free_trial()
        elif len(country_code) >= 5 or len( country_code) < 1:
            print (Fore.RED + "\tError\n\tInvalid country code...\n\n\tCountry codes are generally 1-3 digits...\n")
            t.sleep (3)
            free_trial()
        phone_number = input(Fore.GREEN + " Enter target phone number without country code: " + Fore.YELLOW)
        if len(phone_number) <= 6:
            print(Fore.RED + '\n\nInvalid Phone Number..\n')
            t.sleep (3)
            free_trial()
        elif country_code in phone_number:
            print (Fore.RED + "\nError:\nI told you not to add country code, you fool 🙄🙄\n\n\n\n")
            t.sleep(3)
            free_trial()
        pa = phonenumbers.parse(country_code + phone_number)
        Phone_Number = phonenumbers.is_valid_number(pa)
        if Phone_Number is True:
            pass
        else:
            print(Fore.RED + str(pa) + " is not a valid number")
            t.sleep(3.5)
            loop()
        
        message = input (Fore.GREEN + "\n\nBuild your scam letter" + Fore.CYAN + "[Note: Letters are not in html format] \n Type your messages: " + Fore.YELLOW)
        number = country_code + phone_number
        resp = requests.post('https://textbelt.com/text', {
     
          'phone': country_code + phone_number,
          'message': message,
          'key': 'textbelt',
        })
        print(resp.json())
    def paid():
        BASE_URL = "https://mpvr96.api.infobip.com"
        BASE_URL = ""
        API_KEY = "2d86b648c363a5e6562e74e84a832fb4-ab0a6e77-7860-4b6f-95ea-aee61aab437f"
        API_KEY = ""
        SENDER = input(Fore.GREEN + "Enter sender name: " + Fore.YELLOW)
        RECIPIENT = input(Fore.GREEN + "Enter target phone number with country code: " + Fore.YELLOW)
        MESSAGE_TEXT = input(Fore.GREEN + "Build your scam letter: " + Fore.YELLOW) 
        client_config = Configuration(
            host= BASE_URL,
            api_key={"APIKeyHeader": API_KEY},
            api_key_prefix={"APIKeyHeader": "App"},
    )

        api_client = ApiClient(client_config)

        sms_request = SmsAdvancedTextualRequest(
                messages=[
                    SmsTextualMessage(
                        destinations=[
                            SmsDestination(
                                to=RECIPIENT,
                            ),
                        ],
                        _from=SENDER,
                        text=MESSAGE_TEXT,
                    )
                ])

        api_instance = SendSmsApi(api_client)

        try:
            api_response: SmsResponse = api_instance.send_sms_message(sms_advanced_textual_request=sms_request)
            print(api_response)
        except ApiException as ex:
            print("Error occurred while trying to send SMS message.")
            print(ex)
            
    print(Fore.GREEN + """
Choose a version to use
[1] Free Version
[2] Paid Version
""")
    version = input(Fore.YELLOW + " Choose a version: " + Fore.CYAN)
    if version == "1":
        free_trial()
    elif version == "2":
        activation_code = input(Fore.BLUE + "Enter activation Code: " + Fore.BLACK)
        if activation_code  != "TheNooB":
            print(Fore.RED + " Incorrect activation code!\nContacting the owner for activation code in five seconds")
            t.sleep(5.5)
            mess = {'text' : """Hello Spider, please i need sms attack activation code"""}
            data = urllib.parse.urlencode(mess)
            os.system ("xdg-open https://wa.me/+2349052863644?" + data)
            loop()
        else:
            paid()


    
    con = input((Fore.GREEN + "Do you wanna continue?[Y/N]: " + Fore.YELLOW)) 
    if con == "y" or con == "Y":
        loop()
loop()
