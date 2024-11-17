# Ethical-Hacking-Tools

This is a simple Python-based Port Scanner that scans the specified IP address for open ports within a range. It uses the socket library to attempt connections and outputs the status of each port.

# Features
- Scans ports from 1 to 999.  
- Displays whether ports are open or closed.  
- Customizable timeout settings.  
- ASCII banner using the pyfiglet library for a visually appealing start.

# Prerequisites
- Python 3.x installed on your system.  
- Required Python libraries:  
    pyfiglet  
    socket
  
Install the libraries using pip if not already installed:  
   *pip install pyfiglet*  

# How to Use
 Step 1: Clone the Repository  

   *git clone https://github.com/yourusername/port-scanner.git*  
   *cd port-scanner*  
   
Step 2: Run the Script
Run the script using Python:  

   *python port_scanner.py*    
   
Step 3: Input Target IP

When prompted, enter the target IP address. For example:
*Enter your target IP: 192.168.1.1*  

Step 4: View Results
The script will scan ports in the range 1-999 and display results like:

   *port 22 is open*  
   *port 23 is closed*  

# Notes

- Ensure you have permission to scan the target system. Unauthorized port scanning may violate legal or ethical guidelines.  
- Modify the port range or add additional functionality (e.g., threading for faster scans) as needed.




