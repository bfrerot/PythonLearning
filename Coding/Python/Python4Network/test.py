devices = ['switch1', 'switch2', 'switch3']
vlans = [{'id': '10', 'name': 'USERS' },{'id': '20', 'name': 'USERS'},{'id': '30', 'name': 'USERS'}]
vlan_int = [{'id': '10', 'description': 'USERS', 'ip' : '10.0.10.' },{'id': '20', 'description': 'USERS' , 'ip' : '10.0.20.'},{'id': '30', 'description': 'USERS' , 'ip' : '10.0.30.'}]

# we define vlans
def get_vlans(bobo, babar):
    global commandsvlans
    commandsvlans = []
    commandsvlans.append('interface vlan ' + bobo)
    commandsvlans.append('name ' + babar)
    return commandsvlans
def push_vlans(device, commandsvlans):
    print('ssh bfrerot@' + device)
    for cmd in commandsvlans:
        print (cmd)

def get_intvlan(boubou, bibi, papa):
    global commandsintvlan
    commandsintvlan = []
    commandsintvlan.append('interface vlan ' + boubou)
    commandsintvlan.append('description ' + bibi)
    for (element) in devices:
        bonus = str(devices.index(element) + 1)
        commandsintvlan.append('ip address ' + papa + bonus)
    return commandsintvlan
def push_intvlan(device, commandsintvlan):
    print('ssh bfrerot@' + device)
    for cmd2 in commandsintvlan:
        print (cmd2)


for toto in vlans:
    bobo = toto.get('id')
    babar = toto.get('name')
    print('\n')
    print('CONFIGURING VLAN:' + bobo)
    print('\n')
    commandsvlans = get_vlans(bobo, babar)
    for device in devices:
        push_vlans(device, commandsvlans)
        print('exit')

for tata in vlan_int:
    boubou = tata.get('id')
    bibi = tata.get('description')
    papa = tata.get('ip')
    print('\n')
    print('CONFIGURING INT VLAN:' + boubou)
    print('\n')
    commandsintvlan = get_intvlan(boubou, bibi, papa)
    for device in devices:
        push_intvlan(device, commandsintvlan)
        print('exit')   
