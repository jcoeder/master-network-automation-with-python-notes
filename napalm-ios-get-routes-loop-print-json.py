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
    output = device.get_arp_table()
    print(json.dumps(output, sort_keys=True, indent=4))

for device in devices:
    device.open()
    output = device.get_route_to(destination=u'10.0.0.0/24')
    print(json.dumps(output, sort_keys=True, indent=4))

for device in devices:
    device.open()
    output = device.get_route_to(destination=u'0.0.0.0/0')
    print(json.dumps(output, sort_keys=True, indent=4))
