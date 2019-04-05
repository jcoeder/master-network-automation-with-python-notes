#!/usr/bin/python

import telnetlib
import time

user = 'cisco'
password = 'cisco'
enable = None

file = open('routers.txt')

for line in file:
    tn = telnetlib.Telnet(line)

    tn.read_until('Username: ')
    tn.write(user + '\n')
    if password:
        tn.read_until('Password: ')
        tn.write(password + '\n')

    tn.write('enable\n')
    tn.write('terminal length 0\n')

    if enable is not None:
        tn.read_until('Password: ')
        tn.write(enable + '\n')
        tn.read_until('#')
    else:
        tn.read_until('#')

    tn.write('configure terminal\n')
    tn.read_until('(config)#')

    for i in range(10):
        tn.write('interface loopback ' + str(i) + '\n')
        tn.write('ip address 1.1.1.' + str(i) + ' 255.255.255.255\n')
        time.sleep(.2)

    tn.write('exit\n')
    tn.write('write memory\n')
