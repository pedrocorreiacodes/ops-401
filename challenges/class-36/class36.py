#!/usr/bin/python

# Author
# Date Created
# Description
# Last Revised

import os
import subprocess

# Declare Variables

target = "scanme.nmap.org"
port = "22"

# Declare functions


def printbanner():
    print('''
 ____                                             ______                          
/\  _`\                                          /\__  _\__                       
\ \ \L\ \     __      ___     ___      __    _ __\/_/\ \/\_\    ___ ___      __   
 \ \  _ <'  /'__`\  /' _ `\ /' _ `\  /'__`\ /\`'__\ \ \ \/\ \ /' __` __`\  /'__`\ 
  \ \ \L\ \/\ \L\.\_/\ \/\ \/\ \/\ \/\  __/ \ \ \/   \ \ \ \ \/\ \/\ \/\ \/\  __/ 
   \ \____/\ \__/.\_\ \_\ \_\ \_\ \_\ \____\ \ \_\    \ \_\ \_\ \_\ \_\ \_\ \____\ 
    \/___/  \/__/\/_/\/_/\/_/\/_/\/_/\/____/  \/_/     \/_/\/_/\/_/\/_/\/_/\/____/
                                                                                 
                                                                                 
     ''')

# Main


printbanner()
target = input("Enter target:")
print("Target is: " + target)
port = input("Enter port:")
print("Port is: " + port)
print("Begin scan...")
command = "nc " + target + " " + port
os.system("nc " + target + " " + port)
os.system("/n")
os.system("telnet " + target + " " + port)
os.system("nmap -sV " + target)
print("Scan complete.")

# resources: https://www.instructables.com/Netcat-in-Python/
# End
