import ipaddress
import sys
import os
import time

# Takes the cidr from the command line
cidr = sys.argv[1]

# Verifies your os type
OS_TYPE = os.name

# Sets the count modifier to the os type
COUNT = '-n' if OS_TYPE == 'nt' else '-c'

# Empty list to store ip addresses
ip_list = []

# Creates a network object
netIpv4Address = ipaddress.ip_network(cidr)

# Iterates through the network object and appends the ip addresses to the list
for i in netIpv4Address:
    ip_list.append(str(i))

# Iterates through the list of ip addresses and pings each one
start = time.time()
for ip in ip_list:
    response = os.popen(f"ping {ip} {COUNT} 1").read()
    start = time.time()
    end = time.time()
    elapsed = end - start
    if "Received = 1" in response and "Approximate" in response:
        print(f"{ip} - UP ({elapsed:.2f} seconds)")
    else:
        print(f"{ip} - DOWN (Connection timeout)")