import yaml

devices = {}

devices[0] = {
    'device_name': 'cisco3',
    'hostname': 'cisco3.lasthop.io',
    'username': 'pyclass',
    'password': 'PASSWORD'
}

devices[1] = {
    'device_name': 'arista1',
    'hostname': 'arista1.lasthop.io',
    'username': 'pyclass',
    'password': 'PASSWORD'
}

devices[2] = {
    'device_name': 'srx2',
    'hostname': 'srx2.lasthop.io',
    'username': 'pyclass',
    'password': 'PASSWORD'
}

devices[3] = {
    'device_name': 'nxos1',
    'hostname': 'nxos1.lasthop.io',
    'username': 'pyclass',
    'password': 'PASSWORD'
}

f = open('devices.yaml', 'w')
yaml.dump(devices, f)
f.close()

