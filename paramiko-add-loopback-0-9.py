#!/usr/bin/python

import paramiko
import time

host = '172.31.33.201'
user = 'cisco'
password = 'cisco'
enable = None

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=host,username=user,password=password)

remote_connection = ssh_client.invoke_shell()

remote_connection.send('enable\n')
remote_connection.send('configure terminal\n')
for i in range(10):
    remote_connection.send('interface loopback ' + str(i) + '\n')
    remote_connection.send('description looback' + str(i))
    remote_connection.send('ip address 10.10.200.' + str(i) + ' 255.255.255.255\n')
    time.sleep(.2)
remote_connection.send('exit\n')
remote_connection.send('exit\n')
remote_connection.send('write memory\n')
remote_connection.send('end\n')

time.sleep(1)
output = remote_connection.recv(65535)
print(output)

ssh_client.close()
