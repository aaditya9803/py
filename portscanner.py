#!/bin/python3
#python 3 scanner.py <ip>

import sys
import socket
from datetime import datetime

#Defining target
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])
    #translating hostname to ipv4
else:
    print('Invalid amount of arguments')
    print('syntax: python3 scanner.py <ip>')

#pretty banner
print('scanning target' + target)
print('started time + str(datetime.now())')

try:
    for port in range(50,85):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target,port)) #gives error
        if result ==0:
            print('port {} is open'.format(port))
            s.close()
expect KeyboardInterrupt:
    print("\n Existing program")
    sys.exit()
expect socket.gaierror:
    print("Hostname cant be resolved")
    sys.exit()
expect socket.error:
    print("No connection to server")
    sys.exit()
