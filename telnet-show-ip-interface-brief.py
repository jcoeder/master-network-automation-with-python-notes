#!/usr/bin/python

import telnetlib
import sys
import time

host = '172.31.33.201'
user = 'cisco'
password = 'cisco'
enable = None

tn = telnetlib.Telnet(host)

tn.read_until('Username: ')
tn.write(user + '\n')
if password:
    tn.read_until('Password: ')
    tn.write(password + '\n')

tn.write('enable\n')

if enable is not None:
    tn.read_until('Password: ')
    tn.write(enable + '\n')
    tn.read_until('#')
else:
    tn.read_until('#')

tn.write('terminal length 0\n')

tn.write('show ip interface brief\n')
time.sleep(1)
print(tn.read_very_eager())
