import pyfiglet
import sys
import socket
from datetime import datetime

ascii_banner = pyfiglet.figlet_format("PORT SCANNER")
print(ascii_banner)



s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = input("Enter your target IP :")

def portscanner(port):
    if socket.connect_ex((host , port)):
        print("port %d is closed" % (port))
        
    else:
        print("port %d is open" % (port))
        
for port in range(1,1000):
    portscanner(port)
