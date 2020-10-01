from netmiko import ConnectHandler
import yaml

#f_name = input("Open yaml: ")
f = open("netmiko.yml")
data = yaml.load(f)

net_connect = ConnectHandler(**data['cisco3'])
print(net_connect.find_prompt())
net_connect.disconnect()

