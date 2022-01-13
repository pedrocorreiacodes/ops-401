#!/usr/bin/env python3

# Import libraries
from sys import platform
import os
import time


# Declare functions

# check Os
def checkOs():
    if platform == "linux" or platform == "linux2":
        return 'Linux'
    elif platform == "win32":
        return 'Windows'


def askUserFile():
    file = input("Specify a file for searching:\n")
    return file


def askUserDir():
    dir = input("Enter the search directory:\n")
    return dir

# search a linux os


def linuxSearch():
    whichFile = askUserFile()
    directory = askUserDir()
    # count and print number of files searched
    os.system("ls " + str(directory) + " | echo \"Searched $(wc -l) files.\"")
    # count and print number of files found
    os.system("find " + str(directory) + ' -name ' + str(whichFile) +
              " -print | echo \"Found $(grep -c /) files that matched:\"")
    print("")
    os.system("find " + str(directory) + ' -name ' + str(whichFile))
    print("")

# search a windows os


def windowsSearch():
    whichFile = askUserFile()
    directory = askUserDir()
    # count number of files searched, store in variable
    searchCount = os.popen("dir /a:-d /s /b " +
                           str(directory) + " | find /c \":\\\"").read()
    print("Files searched: " + searchCount)
    # count number of files found, store in variable
    foundCount = os.popen("dir /b/s " + str(directory) +
                          "\\" + str(whichFile) + " | find /c \":\\\"").read()
    print("Files found: " + foundCount)
    os.system("dir /b/s " + str(directory) + "\\" + str(whichFile))

# Main


# determine OS and run appropriate function
os = checkOs()

if os == "Linux":
    linuxSearch()
elif os == "Windows":
    windowsSearch()

# resource: https://stackoverflow.com/questions/8220108/how-do-i-check-the-operating-system-in-python/8220141
# resource: https://github.com/codefellows/ops-401-cybersecurity-guide/blob/main/curriculum/class-31/solution/challenge/soln.py

# End
