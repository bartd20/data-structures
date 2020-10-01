import json

arp_dict = {}

f = open("arp.json")
data = json.load(f)
f.close()

for x in data['ipV4Neighbors']:
    arp_dict[x['address']] = x['hwAddress']

print(arp_dict)
 
