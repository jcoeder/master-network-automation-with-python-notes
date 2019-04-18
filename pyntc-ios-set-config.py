from pyntc import ntc_device as NTC

iosvl3 = NTC(host='172.31.33.201', username='cisco', password='cisco', device_type='cisco_ios_ssh')
iosvl3.open()

iosvl3.config_list['hostname Router1', 'router ospf 1', 'network 10.0.0.0 255.255.255.0 area 0.0.0.0']
