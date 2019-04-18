import json
from pyntc import ntc_device as NTC

iosvl3 = NTC(host='172.31.33.201', username='cisco', password='cisco', device_type='cisco_ios_ssh')
iosvl3.open()

ios_output = iosvl3.facts
print(json.dumps(ios_output, indent=4))
