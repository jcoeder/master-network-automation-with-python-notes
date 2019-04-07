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
for i in range(2,21):
    remote_connection.send('vlan ' + str(i) + '\n')
    remote_connection.send('name python_vlan' + str(i))
    time.sleep(.5)
remote_connection.send('exit\n')
remote_connection.send('exit\n')
remote_connection.send('write memory\n')
remote_connection.send('end\n')

time.sleep(1)
output = remote_connection.recv(65535)
print(output)

ssh_client.close()
