import json
from napalm import get_network_driver

driver = get_network_driver('ios')
iosvl3 = driver('172.31.33.201', 'cisco', 'cisco')
iosvl3.open()

iosvl3.load_merge_candidate(filename='access-list.cfg')

diffs = iosvl3.compare_config()
if len(diffs) > 0:
    print(diffs)
    iosvl3.commit_config()
else:
    print('No changes required.')
    iosvl3.discard_config()

 iosvl3.load_merge_candidate(filename='ospf.cfg')

diffs = iosvl3.compare_config()
if len(diffs) > 0:
    print(diffs)
    iosvl3.commit_config()
else:
    print('No changes required.')
    iosvl3.discard_config()

iosvl3.close()
