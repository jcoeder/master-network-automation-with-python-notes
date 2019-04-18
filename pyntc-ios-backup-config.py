from pyntc import ntc_device as NTC

host = '172.31.33.201'

iosvl3 = NTC(host=host, username='cisco', password='cisco', device_type='cisco_ios_ssh')
iosvl3.open()

########################################################

running_config = iosvl3.running_config

saveoutput = open('Router' + host, 'w')
saveoutput.write(running_config)
saveoutput.close

########################################################
# OR
########################################################

running_config = iosvl3.backup_running_config('iosvl3.cfg')

########################################################
