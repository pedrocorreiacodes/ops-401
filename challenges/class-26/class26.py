#!/usr/bin/env python3

# Import libraries
import logging
import os

# Declare variables
user_input = "~/scripts/bash/ops401-demo/class-26/soln/demodir"

# Declare functions


def file_crawler(dir_name):
    for (root, dirs, files) in os.walk(dir_name):
        # Add a print command here to print ==root==
        print("==root==")
        print(root)
        # Add a print command here to print ==dirs==
        print("==dirs==")
        print(dirs)
        # Add a print command here to print ==files==
        print("==files")
        print(files)


# Main
logging.basicConfig(filename='./soln.log', level=logging.ERROR,
                    format='%(asctime)s:%(levelname)s:%(message)s')
print('Logging started')
logging.debug('Something to debug...')
logging.info('This is purely informational')
logging.warning('Warning! Warning!')
# logging.error('An error has occured...')
logging.critical('There is a critical issue here')

try:
    file_crawler()  # Inducing an intentional error by omitting the variable "user_input"

except Exception as msg:
    print(msg)
    logging.exception(msg)

print('Logging completed')
# End
