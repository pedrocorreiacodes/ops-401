#!/usr/bin/env python3

import os, time, datetime;


def check_ping(target):

    response = os.system("ping -c 1 " + target)
    # and then check the response...
    if response == 0:
        pingstatus = "Network Active"
    else:
        pingstatus = "Network Error"

    return pingstatus


pingstatus = check_ping("8.8.8.8")


while True:
    now = datetime.datetime.now()
    print(str(now) + " " + pingstatus + " to 8.8.8.8")
    time.sleep(2)