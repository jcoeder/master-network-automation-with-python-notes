from napalm import get_network_driver

driver = get_network_driver('ios')
iosvl3 = driver('172.31.33.201', 'cisco', 'cisco')
iosvl3.open()

iosvl3.load_merge_candidate(filename='access-list.cfg')
iosvl3.commit_config()
iosvl3.close()
