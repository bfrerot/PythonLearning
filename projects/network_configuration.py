## generer configuration

#devices = [{'hostname' : 'switch1' , 'ip' : '1'},{'hostname' : 'switch2' , 'ip' : '2'},{'hostname' : 'switch3' , 'ip' : '3'}]
devices = ['switch1', 'switch2', 'switch3']
vlans = [{'id': '10', 'name': 'USERS'}, {'id': '20', 'name': 'VOICE'},{'id': '30', 'name': 'WLAN'}]

def get_commands(vlan, name):
    commands = []
    commands.append('vlan ' + vlan)
    commands.append('name ' + name)
#    commands.append('exit')
#    commands.append('interface ' + vlan)
#    commands.append('ip address 10.10' + vlan + ip)

    return commands

def push_commands(device, commands):
    print('Connecting to device: ' + device)
    for cmd in commands:
        print('Sending command: ' + cmd)

for vlan in vlans:
    id = vlan.get('id')
    name = vlan.get('name')
#    ip = vars
    print('\n')
    print('CONFIGURING VLAN:' + id)
    commands = get_commands(id, name)
    for device in devices:
        push_commands(device, commands)
        print('\n')