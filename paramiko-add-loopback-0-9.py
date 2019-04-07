import paramiko
import time

host = '172.31.33.201'
user = 'cisco'
password = 'cisco'
enable = None

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=host, username=user, password=password)

remote_connection = ssh_client.invoke_shell()

remote_connection.send('enable\n')
remote_connection.send('configure terminal\n')
for i in range(10):
    remote_connection.send('interface loopback ' + i + '\n')
    remote_connection.send('description looback' + i)
    remote_connection.send('ip address 10.10.200.' + i + ' 255.255.255.255\n')
remote_connection.send('exit\n')
remote_connection.send('exit\n')
remote_connection.send('write memory\n')
