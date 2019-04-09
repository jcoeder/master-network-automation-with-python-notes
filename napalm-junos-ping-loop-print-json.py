#!/usr/bin/python

from napalm import get_network_driver
import json

junos_driver = get_network_driver('junos')

vmx1 = junos_driver('172.31.33.204', 'root', 'Juniper')
vmx2 = junos_driver('172.31.33.205', 'root', 'Juniper')
vmx3 = junos_driver('172.31.33.206', 'root', 'Juniper')

devices = [vmx1, vmx2, vmx3]

for device in devices:
    device.open()
    output = device.ping('10.0.0.1')
    print(json.dumps(output, sort_keys=True, indent=4))