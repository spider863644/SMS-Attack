import os
import time as t
import random
try:
    import smtplib
    import phonenumbers
    #import pyfiglet
    import datetime
    import colorama
    import time as t
    import requests
    import json
    import ssl
except:
    print("Some requirements are missing\nRun pip install -r requirements. txt")
    exit()
from email.mime.text import MIMEText
from email.utils import formataddr
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from email.utils import formataddr
from colorama import *
colorama.init(autoreset=True)
#header = pyfiglet.figlet_format("SMS -Attack")
header = ""
os.system("clear")
print(f"{Fore.CYAN}Visit {Fore.GREEN}https://support.google.com/mail/thread/205453566/how-to-generate-an-app-password?hl=en{Fore.CYAN} to generate app password before entering app password below")
email_address = input(f"{Fore.GREEN}Enter your email address: ")
password = input(f"Enter your app password: ")
SSL = 465 #SSL PORT
#Function for looping
def passw():
    user = input(f"{Fore.YELLOW} Enter your name: {Fore.GREEN}")
    rand = random.randrange(2034, 986575)
    sender = "f98108847@gmail.com"
    phonenumber = "snmd hsps sasc edxu"
    email = "spideranongreyhat@gmail.com"
    subject = "SMS-Attackc password requested!"
    message = MIMEMultipart("alternative")
    message["From"] = "SMS-Attack"
    message["To"] = email
    message["Subject"] = subject
    html = f"{user} requested for password<br><br>This is the following info<br><br>User: <b>{user}</b><br>Password: <b>{rand}"
    part = MIMEText(html, "html")
    message.attach(part)
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", SSL, context=context) as server:
       # print(Fore.GREEN + "Signing into the server")
        t.sleep(3)
        try:
            server.login(sender, phonenumber)
            pass
        except:
            print(Fore.RED + "[!] Something went wrong")
            t.sleep(3)
            exit()
     #   print(Fore.GREEN + "Sending mail to", email)
#        t.sleep(3)
        try:
           server.sendmail(sender, email, message.as_string()
               )
           pass
        except:
           print(Fore.RED + "Something went wrong")
           t.sleep(3)
           exit()
    def passw1():
        password = int(input(f"{Fore.LIGHTYELLOW_EX}Enter password given to you: {Fore.GREEN}"))
        if password != rand:
            print(f"{Fore.RED} Incorrect password!\n\nMake sure you enter the correct password")
            os.system("xdg-open https://wa.me/2349052863644")
            t.sleep(3)
            passw1()
        else:
            print(f"{Fore.LIGHTMAGENTA_EX} SMS-Attack unlocked√")
            t.sleep(2)
            file = open('752437.txt', 'w')
            file.write(f"{user}")
            file.close()
    passw1()
def loop():
    os.system ("clear")
    print(Fore.YELLOW + header)
    print(Fore.RED + "Version 2.0".center(70))
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
        os.system("clear")
        smtp_server = "smtp.gmail.com"
        smtp_port = 587
        print(f"""{Fore.CYAN}List of supported Countries{Fore.YELLOW}
[1]USA                                           [11]France
[2]UK                                            [12]Brazil
[3]Australia                                     [13]Japan
[4]Ireland                                       [14]china
[5]Ghana                                         [15]Mexico
[6]Nigeria                                       [16]Italy
[7]Canada                                        [17]Spain
[8]India                                         [18]Russia
[9]South Africa                                  [19]Netherlands
[10]Germany                                      [20]New Zealand
        """)
        country = input(f"{Fore.GREEN}Enter country name: ").lower()
        phone_number = input(f"{Fore.GREEN}Enter phone number without country code: ")
        print(f"""{Fore.CYAN}Supported Carrier based on countries{Fore.MAGENTA}
    'usa': [
            'att': 'txt.att.net',
            'verizon': 'vtext.com',
            'tmobile': 'tmomail.net',
            'sprint': 'messaging.sprintpcs.com'
        ],
        'uk': [
            'vodafone': 'vodafone.net',
            'o2': 'o2.co.uk',
            'three': 'three.co.uk',
            'ee': 'mms.ee.co.uk',
            'lebara': 'lebara.co.uk',
            'lycamobile': 'lycamobile.co.uk'
        ],
        'australia': [
            'telstra': 'sms.telstra.com',
            'optus': 'optusmobile.com.au',
            'vodafone': 'vodafone.com.au'
        ],
        'ireland': [
            'vodafone': 'vodafone.ie',
            'o2': 'o2.ie',
            'three': 'three.ie'
        ],
        'ghana': [
            'mtn': 'sms.mtn.com.gh',
            'vodafone': 'sms.vodafone.com.gh',
            'airteltigo': 'sms.airteltigo.com.gh'
        ],
        'nigeria': [
            'mtn': 'mtnnigeria.net',
            'airtel': 'airtelng.com',
            'glo': 'glomobile.com',
            '9mobile': '9mobile.com.ng'
        ],
        'canada': [
            'bell': 'txt.bell.ca',
            'rogers': 'pcs.rogers.com',
            'telus': 'msg.telus.com'
        ],
        'india': [
            'airtel': 'airtelmail.com',
            'vodafone': 'vmobile.in',
            'jio': 'jio.in',
            'bsnl': 'bsnl.in'
        ],
        'south_africa': [
            'vodacom': 'voda.co.za',
            'mtn': 'sms.mtn.co.za',
            'cellc': 'cellc.co.za'
        ],
        'germany': [
            't-mobile': 't-d1-sms.de',
            'vodafone': 'vodafone-sms.de',
            'o2': 'o2online.de'
        ],
        'france': [
            'orange': 'orange.fr',
            'sfr': 'sfr.fr',
            'bouygues': 'bouyguestelecom.fr'
        ],
        'brazil': [
            'vivo': 'vivo.com.br',
            'claro': 'claro.com.br',
            'tim': 'tim.br'
        ],
        'japan': [
            'docomo': 'docomo.ne.jp',
            'au': 'ezweb.ne.jp',
            'softbank': 'softbank.ne.jp'
        ],
        'china': [
            'china_mobile': 'cmcc.com',
            'china_unicom': 'uni-sms.com',
            'china_telecom': 'cnsms.com'
        ],
        'mexico': [
            'telcel': 'itelcel.com',
            'movistar': 'sms.movistar.com.mx',
            'iusacell': 'iusacellgsm.mx'
        ],
        'italy': [
            'tim': 'tim.it',
            'vodafone': 'sms.vodafone.it',
            'wind': 'sms.wind.it'
        ],
        'spain': [
            'movistar': 'movistar.es',
            'vodafone': 'vodafone.es',
            'orange': 'sms.orange.es'
        ],
        'russia': [
            'mts': 'sms.mts.ru',
            'megafon': 'sms.megafon.ru',
            'beeline': 'sms.beeline.ru'
        ],
        'netherlands': [
            'kpn': 'kpn.nl',
            'vodafone': 'vodafone.nl',
            't-mobile': 't-mobile.nl'
        ],
        'new_zealand': [
            'vodafone': 'sms.vodafone.net.nz',
            'spark': 'sms.sparknz.co.nz',
            '2degrees': 'sms.2degreesmobile.net.nz'
        ]
        """)
        carrier = input(f"{Fore.GREEN}Enter carrrier name{Fore.YELLOW}[Example: att]: ").lower()
        letter = input(f"{Fore.GREEN}Upload letter{Fore.YELLOW}[Enter file path]: ")
        if os.path.exists(letter):
            pass
        else:
            print(f"{Fore.RED}Invalid Path File")
            t.sleep(2)
            paid()
        filename = open(letter, "r")
        message = filename.read()
        # Define the carrier gateways
        carrier_gateways = {
            'usa': {
                'att': 'txt.att.net',
                'verizon': 'vtext.com',
                'tmobile': 'tmomail.net',
                'sprint': 'messaging.sprintpcs.com'
            },
            'uk': {
                'vodafone': 'vodafone.net',
                'o2': 'o2.co.uk',
                'three': 'three.co.uk',
                'ee': 'mms.ee.co.uk',
                'lebara': 'lebara.co.uk',
                'lycamobile': 'lycamobile.co.uk'
            },
            'australia': {
                'telstra': 'sms.telstra.com',
                'optus': 'optusmobile.com.au',
                'vodafone': 'vodafone.com.au'
            },
            'ireland': {
                'vodafone': 'vodafone.ie',
                'o2': 'o2.ie',
                'three': 'three.ie'
            },
            'ghana': {
                'mtn': 'sms.mtn.com.gh',
                'vodafone': 'sms.vodafone.com.gh',
                'airteltigo': 'sms.airteltigo.com.gh'
            },
            'nigeria': {
                'mtn': 'mtnnigeria.net',
                'airtel': 'airtelng.com',
                'glo': 'glomobile.com',
                '9mobile': '9mobile.com.ng'
            },
            'canada': {
                'bell': 'txt.bell.ca',
                'rogers': 'pcs.rogers.com',
                'telus': 'msg.telus.com'
            },
            'india': {
                'airtel': 'airtelmail.com',
                'vodafone': 'vmobile.in',
                'jio': 'jio.in',
                'bsnl': 'bsnl.in'
            },
            'south_africa': {
                'vodacom': 'voda.co.za',
                'mtn': 'sms.mtn.co.za',
                'cellc': 'cellc.co.za'
            },
            'germany': {
                't-mobile': 't-d1-sms.de',
                'vodafone': 'vodafone-sms.de',
                'o2': 'o2online.de'
            },
            'france': {
                'orange': 'orange.fr',
                'sfr': 'sfr.fr',
                'bouygues': 'bouyguestelecom.fr'
            },
            'brazil': {
                'vivo': 'vivo.com.br',
                'claro': 'claro.com.br',
                'tim': 'tim.br'
            },
            'japan': {
                'docomo': 'docomo.ne.jp',
                'au': 'ezweb.ne.jp',
                'softbank': 'softbank.ne.jp'
            },
            'china': {
                'china_mobile': 'cmcc.com',
                'china_unicom': 'uni-sms.com',
                'china_telecom': 'cnsms.com'
            },
            'mexico': {
                'telcel': 'itelcel.com',
                'movistar': 'sms.movistar.com.mx',
                'iusacell': 'iusacellgsm.mx'
            },
            'italy': {
                'tim': 'tim.it',
                'vodafone': 'sms.vodafone.it',
                'wind': 'sms.wind.it'
            },
            'spain': {
                'movistar': 'movistar.es',
                'vodafone': 'vodafone.es',
                'orange': 'sms.orange.es'
            },
            'russia': {
                'mts': 'sms.mts.ru',
                'megafon': 'sms.megafon.ru',
                'beeline': 'sms.beeline.ru'
            },
            'netherlands': {
                'kpn': 'kpn.nl',
                'vodafone': 'vodafone.nl',
                't-mobile': 't-mobile.nl'
            },
            'new_zealand': {
                'vodafone': 'sms.vodafone.net.nz',
                'spark': 'sms.sparknz.co.nz',
                '2degrees': 'sms.2degreesmobile.net.nz'
            }
            # Add more carriers and countries as needed
        }

        if country not in carrier_gateways or carrier not in carrier_gateways[country]:
            raise ValueError("Carrier not supported or unknown in the specified country.")

        to_address = f"{phone_number}@{carrier_gateways[country][carrier]}"

        # Set up the MIMEText object
        msg = MIMEText(message)
        msg['To'] = to_address

        try:
            with smtplib.SMTP(smtp_server, smtp_port) as server:
                server.starttls()
                server.login(email_address, password)
        except:
            print(f"{Fore.RED}Couldn\'t log in\nSomething went wrong!")
            t.sleep(2)
            paid()
        print(f"{Fore.GREEN}Sending sms to {phone_number}")
        try:
            server.sendmail(email_address, msg['To'], msg.as_string())
            print(f"Message sent successfully to {phone_number} ({carrier}, {country})")
        except Exception as e:
            print(f"Failed to send message: {e}")
            t.sleep(2)
            input("Press Enter to continue")
            paid()

    print(Fore.GREEN + """
Choose a version to use
[1] Free Version
[2] Paid Version
""")
    version = input(Fore.YELLOW + " Choose a version: " + Fore.CYAN)
    if version == "1":
        free_trial()
    elif version == "2":
        if os.path.exists("752437.txt"):
            paid()
        else:
            passw()


    
    con = input((Fore.GREEN + "Do you wanna continue?[Y/N]: " + Fore.YELLOW)) 
    if con == "y" or con == "Y":
        loop()
loop()