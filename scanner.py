import ipaddress
import sys

cidr = sys.argv[1]

def scan(cidr):
    ip = ipaddress.ip_network(cidr)
    for i in ip.hosts():
        print(i)