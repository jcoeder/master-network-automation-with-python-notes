#!/usr/bin/python

from netmiko import ConnectHandler

iosv_l3_1 = {
    'device_type': 'cisco_ios',
    'ip': '172.31.33.201',
    'username': 'cisco',
    'password': 'cisco',
}

iosv_l3_2 = {
    'device_type': 'cisco_ios',
    'ip': '172.31.33.202',
    'username': 'cisco',
    'password': 'cisco',
}

iosv_l3_3 = {
    'device_type': 'cisco_ios',
    'ip': '172.31.33.203',
    'username': 'cisco',
    'password': 'cisco',
}

iosv_l3_4 = {
    'device_type': 'cisco_ios',
    'ip': '172.31.33.204',
    'username': 'cisco',
    'password': 'cisco',
}

devices = [iosv_l3_1, iosv_l3_2, iosv_l3_3, iosv_l3_4]
with open('switch-interface-configuration.txt') as file:
    lines = file.read().splitlines()

for device in devices:
    net_connect = ConnectHandler(**device)
    for line in lines:
        output = net_connect.send_config_set(line)
        print(output)
