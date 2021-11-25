import smtplib
import datetime
import time
import os
from getpass import getpass

# Declare variables
up = " Network is ACTIVE"
down = " Network is DOWN"
last = 0
ping_result = 0
email = input("Enter your email: ")
password = getpass()
ip = input("What address would you like to monitor?")


# Send the mail (two options)
def send_upAlert():
    now = datetime.datetime.now()
    timestamp = now.strftime('%m-%d-%Y %H:%M:%S %p')
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(email, password)
    msg1 = "Hello! \nYour system has recovered.\n %s" % timestamp
    server.sendmail('mailbot@myserver.com', email, msg1)
    server.quit()


def send_downAlert():
    now = datetime.datetime.now()
    timestamp = now.strftime('%m-%d-%Y %H:%M:%S %p')
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(email, password)
    msg2 = "Oh dear! \nYour system has gone DOWN.\n %s" % timestamp
    server.sendmail('mailbot@myserver.com', email, msg2)
    server.quit()


def ping():
    now = datetime.datetime.now()
    timestamp = now.strftime('%m-%d-%Y %H:%M:%S %p')

    global ping_result
    global last

    if ((ping_result != last) and (ping_result == up)):
        last = up
        send_upAlert()
    elif ((ping_result != last) and (ping_result == down)):
        send_downAlert()
        last = down

    response = os.system("ping -c 1 " + ip)
    if response == 0:
        ping_result = up
    else:
        ping_result = down
    print(timestamp + ping_result + " to " + ip)


while True:
    ping()
    time.sleep(2)
