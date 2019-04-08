#!/usr/bin/python

from netmiko import ConnectHandler

iosv_l3 = {
    'device_type': 'cisco_ios',
    'ip': '172.31.33.201',
    'username': 'cisco',
    'password': 'cisco',
}

net_connect = ConnectHandler(**iosv_l3)

output = net_connect.send_command('show ip interface brief')
print(output)
