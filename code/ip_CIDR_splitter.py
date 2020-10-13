#Written by Aaron 12/10/2020

import ipaddress
import sys

for ip in ipaddress.IPv4Network(sys.argv[1]) :
    print(ip)
