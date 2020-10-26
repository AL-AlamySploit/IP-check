#IP-check V 1.1
#Official YouTube Channel: https://www.youtube.com/channel/UCQuGjfmo04jDd6zlBscslGQ
#channel Telegram: https://t.me/ALAlamyTube
#github: https://github.com/AL-AlamySploit/IP-check
# a7y Team
########################################################################################
import socket
import sys
From time import *
From datetime import datetime
########################################################################################
ip = input ("Your IP to start: ")
A1 = datetime.now()
print ("sanning start..%S please wait..!"%ip)
sleep (1)
########################################################################################
try:
     for port in range (1,6553):
     s = socket.socket.AF.INET,socket.SOCK_STREAM))
     if(s,sonnect.ex((ip,port))==0):
     try:
         serv = socket.getservbyport(port)
         except socket.getservice:
             serv = "Unknown service"
             print ("port %s open service:%s"%(port,serv))
             A2 datetime.now()
             A3 = A2-A1
             print ("scanning completed on %s"A3)
   except keyboardInterrupt:
          print ("see you soon...!"
#######################################################################################
