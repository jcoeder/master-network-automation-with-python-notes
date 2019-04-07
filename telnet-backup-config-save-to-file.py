#!/usr/bin/python

import telnetlib
import getpass

# Prompt user for login information
user = raw_input('Enter Username: ')
password = getpass.getpass()
print('Enter "enable" password if needed: ')
enable = getpass.getpass()
if enable == '':
    enable = None

# Open file called routers.txt
routers = open('routers.txt')

# Loop over each item in routers.txt
for router in routers:

    # Strip whitespace from file
    router = router.strip()

    # Open telnet connection
    tn = telnetlib.Telnet(router)

    # Look for specific prompts and provide username and
    # password.
    tn.read_until('Username: ')
    tn.write(user + '\n')
    if password:
        tn.read_until('Password: ')
        tn.write(password + '\n')

    # Enter enable mode
    tn.write('enable\n')

    # If an enable passoword was provided, use it.
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
    print('Backing up router ' + router)
    saveoutput.write(readoutput)
    saveoutput.close
