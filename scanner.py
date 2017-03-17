import socket
import sys 
print '''
                                            

                       /$$$$$$ 
                      /$$__  $$
 /$$$$$$/$$$$        | $$  \ $$
| $$_  $$_  $$       | $$$$$$$$
| $$ \ $$ \ $$       | $$__  $$
| $$ | $$ | $$       | $$  | $$
| $$ | $$ | $$       | $$  | $$
|__/ |__/ |__//$$$$$$|__/  |__/
              |______/         
'''
from  time import sleep
host=raw_input("please insert your host ip: ")
ports=[21,23,22,80,135,3389,445]
portd={21:"FTP",23:"TELNET",22:"SSH",80:"HTTP",135:"",3389:"RDP",445:"SMB"}
for item in range(7):
	sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	sock.settimeout(0.5)
	result = sock.connect_ex((host,ports[item])) 
	sock.close()
	if result==0:
	    print "PORT " ,ports[item],": ",portd[ports[item]] ," : open"
	
	    
print("\n"+"Finish :)")    
a=input();