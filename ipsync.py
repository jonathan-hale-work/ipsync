import json

ip_dict = {
        "public_ip_address" : "192.168.0.1"
        }
ip_json = json.dumps(ip_dict, indent=4)

with open("ipsync.json", "w") as outfile:
    outfile.write(ip_json)

    
