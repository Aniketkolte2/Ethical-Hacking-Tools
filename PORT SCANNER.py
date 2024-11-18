
import pyfiglet
import socket
from datetime import datetime

# Displaying the banner
ascii_banner = pyfiglet.figlet_format("PORT SCANNER")
print(ascii_banner)

# Taking input for target IP and port range
target = input("Enter Target IP: ")
x = int(input("Enter starting port: "))
y = int(input("Enter last port: "))

if x < 0 or y < 0 or x > 65535 or y > 65535 or x > y:
        print("Invalid port range. Ports must be between 0 and 65535")
        exit()

# Iterating through the port range
for port in range(x, y + 1):  # Adding +1 to include the last port
    try:
       sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
       sock.settimeout(3)  # Timeout for each connection
       result = sock.connect_ex((target, port))  # Connect to the port
    
       if result == 0:
           print(f"Port {port} is open")  # f-string to include the variable
    
       else:
            print(f"Port {port} is closed")
             
    except socket.error as e:
        print(f"Socket error on port {port}: {e}")
        
    finally:
           sock.close()  # Closing the socket
