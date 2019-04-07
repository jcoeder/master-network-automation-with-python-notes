from netmiko import ConnectHandler

iosv_l3 = {
    'device_type': 'cisco_ios',
    'ip': '172.31.33.201',
    'username': 'cisco',
    'password': 'cisco',
}

net_connect = ConnectHandler(**iosv_l3)

for i in range(10):
    config_commands = ['interface loopback  ' + str(i), 'ip address 1.1.1.' + str(i) + ' 255.255.255.255']
    output = net_connect.send_config_set(config_commands)
    print(output)
