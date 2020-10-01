import json

ipv4_list = []
ipv6_list = []
data_addr = []

f = open("addresses.json")
data = json.load(f)
f.close()

for intf, addr in data.items():
    if addr.get("ipv4") != None:
        for ip, mask in addr['ipv4'].items():
            ipv4_list.append(ip+"/"+str(mask['prefix_length']))
    
    if addr.get("ipv6") != None:
        for ip, mask in addr['ipv6'].items():
            ipv6_list.append(ip+"/"+str(mask['prefix_length']))

print(ipv4_list)
print("***")
print(ipv6_list)

