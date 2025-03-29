# ici on utilise python pour populer un template, c'est juste pour la demo car on ne fera pas çà en réel

# from jinja2 import Environment, FileSystemLoader
# ENV = Environment(loader=FileSystemLoader('.'))
# template = ENV.get_template("test.j2")

# interface_dict = {
#     "name": "GigabitEthernet0/1",
#     "description": "Server Port",
#     "vlan": 10,
#     "uplink": False
# }

# print(template.render(interface=interface_dict))

# interface GigabitEthernet0/1
#     description Server Port
#     switchport access vlan 10
#     switchport mode access

########

# from jinja2 import Environment, FileSystemLoader
# ENV = Environment(loader=FileSystemLoader('.'))
# template = ENV.get_template("test.j2")
# class NetworkInterface(object):
#     def __init__(self, name, description, vlan, uplink=False):
#         self.name = name
#         self.description = description
#         self.vlan = vlan
#         self.uplink = uplink

# interface_obj = NetworkInterface("GigabitEthernet0/1", "Server Port", 10)
# print(template.render(interface=interface_obj))

# interface GigabitEthernet0/1
#     description Server Port
#     switchport access vlan 10
#     switchport mode access

