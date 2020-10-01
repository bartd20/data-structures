dict_list = []

file = open("arp_table.txt")
output = file.read()
file.close()

output_lines = output.splitlines()

for line in output_lines:
    line_split = line.split()
    line_dict = {}
    if line_split[0] == 'Protocol':
        continue
    line_dict['mac_addr'] = line_split[3]
    line_dict['ip_addr'] = line_split[1]
    line_dict['interface'] = line_split[4]
    dict_list.append(line_dict)

for item in dict_list:
    print(item)

