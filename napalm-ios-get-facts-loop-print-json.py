#!/usr/bin/python

from napalm import get_network_driver
import json

ios_driver = get_network_driver('ios')
junos_driver = get_network_driver('junos')

iosvl3_1 = ios_driver('172.31.33.201', 'cisco', 'cisco')
iosvl3_2 = ios_driver('172.31.33.202', 'cisco', 'cisco')
iosvl3_3 = ios_driver('172.31.33.203', 'cisco', 'cisco')
vmx1 = junos_driver('172.31.33.204', 'root', 'Juniper')

devices = [iosvl3_1, iosvl3_2, iosvl3_3, vmx1]


for device in devices:
    device.open()
    output = device.get_facts()
    print(json.dumps(output, indent=4))


for device in devices:
    device.open()
    output = device.get_facts()
    print(json.dumps(output, sort_keys=True, indent=4))
