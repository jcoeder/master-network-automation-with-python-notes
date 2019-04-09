#!/usr/bin/python

from napalm import get_network_driver

driver = get_network_driver('ios')
iosvl3 = driver('172.31.33.201', 'cisco', 'cisco')
iosvl3.open()

ios_output = iosvl3.get_facts()
print(ios_output)