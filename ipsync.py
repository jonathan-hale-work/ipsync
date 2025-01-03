import json

import socket

import cloud_log
import urllib.request

external_ipv4 = urllib.request.urlopen('https://4.ident.me').read().decode('utf8')

external_ipv6 = urllib.request.urlopen('https://6.ident.me').read().decode('utf8')
print(external_ipv4)
print(external_ipv6)

import datetime

# Get the current datetime object
now = datetime.datetime.now()

# Format the datetime object as a string
timestamp_str = now.strftime("%Y-%m-%d %H:%M:%S")

print(timestamp_str) 
ip_dict = {
        "ipv4": external_ipv4,
        "ipv6" : external_ipv6,
        "timestamp" : timestamp_str
        }
ip_json = json.dumps(ip_dict, indent=4)
with open("ipsync.json", "w") as outfile:
    outfile.write(ip_json)
