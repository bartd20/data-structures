from ciscoconfparse import CiscoConfParse

bgp = []

file = open("bgp_config.txt")
output = file.read()
file.close() 

parsed = CiscoConfParse(output.splitlines())

bgp_conf = parsed.find_objects(r"^router bgp")
bgp_peer = bgp_conf[0].re_search_children(r"^\s+neighbor")

for x in bgp_peer:
    print(x.text)
    remote_as = x.re_search_children(r"^\s+remote-as")
    print(remote_as[0].text)
    print("***")
    bgp.append((x.text,remote_as[0].text))

print(bgp)






