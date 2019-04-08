#!/usr/bin/python

from netmiko import ConnectHandler

iosv_l3 = {
    'device_type': 'cisco_ios',
    'ip': '172.31.33.201',
    'username': 'cisco',
    'password': 'cisco',
}

net_connect = ConnectHandler(**iosv_l3)

for i in range(2,21):
    config_commands = ['vlan ' + str(i), 'name Python_VLAN' + str(i)]
    output = net_connect.send_config_set(config_commands)
    print(output)
