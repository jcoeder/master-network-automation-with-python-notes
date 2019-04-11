import os
for i in range(255):
    response = os.system('ping -c 2 172.16.225.' + str(i))
    # print('ping -c 2 172.16.225.' + str(i))
