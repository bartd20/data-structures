from netmiko import ConnectHandler
from ciscoconfparse import CiscoConfParse

cisco4 = {
    'host': 'cisco4.lasthop.io',
    'username': 'pyclass',
    'password': 'PASSWORD',
    'device_type': 'cisco_ios'
}

net_connect = ConnectHandler(**cisco4)
output = net_connect.send_command("show run")
net_connect.disconnect()

parsed = CiscoConfParse(output.splitlines())

intf = parsed.find_objects_w_child(parentspec=r"^interface", childspec=r"^\s+ip address")

for x in intf:
    print(x.text)
    child = x.re_search_children(r"^\s+ip address")
    for y in child:
        print(y.text)
    print("***")






