#!/usr/bin/python

import telnetlib
import getpass

# Prompt user for login information
user = raw_input('Enter Username: ')
password = getpass()
print('Enter "enable" password if needed: ')
enable = getpass()

# Open file called routers.txt
routers = open('routers.txt')

# Loop over each item in routers.txt
for router in routers:
    # Open telnet connection
    tn = telnetlib.Telnet(router)

    # Look for specific prompts and provide username and
    # password.
    tn.read_until('Username: ')
    tn.write(user + '\n')
    if password:
        tn.read_until('Password: ')
        tn.write(password + '\n')

    tn.write('enable\n')

    # If an enable passowrd was provided, use it.
    if enable is not None:
        tn.read_until('Password: ')
        tn.write(enable + '\n')
        tn.read_until('#')
    else:
        tn.read_until('#')

    tn.write('terminal length 0\n')
    tn.write('show running-config\n')
    tn.write('exit\n')

    readoutput = tn.read_all()
    saveoutput = open('Router ' + router, 'w')
    saveoutput.write(readoutput)
    saveoutput.close
