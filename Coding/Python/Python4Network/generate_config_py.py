import os
import jinja2

# Charger le modèle Jinja2
template_loader = jinja2.FileSystemLoader(searchpath="d:/devops/Coding/Python/Python4Network")
template_env = jinja2.Environment(loader=template_loader)
template_file = "interface_template.j2"
template = template_env.get_template(template_file)

# Données de configuration pour le switch
switch_config = {
    'hostname': 'SW-BOU-RG-01',

    'banner_motd': ''' 
 ____                                             _   _      _                      _        
| __ )  ___  _   _ _ __   ___  _   _  __ _ _ __  | \ | | ___| |___      _____  _ __| | _____ 
|  _ \ / _ \| | | | '_ \ / _ \| | | |/ _` | '__| |  \| |/ _ \ __\ \ /\ / / _ \| '__| |/ / __|
| |_) | (_) | |_| | | | | (_) | |_| | (_| | |    | |\  |  __/ |_ \ V  V / (_) | |  |   <\__ \\
|____/ \___/ \__,_|_| |_|\___/ \__,_|\__,_|_|    |_| \_|\___|\__| \_/\_/ \___/|_|  |_|\_\___/ ''',

    # ip domain name
    'domain_name': 'boubou.com',

    # default route
    'next_hop': '10.37.1.254',

    # Liste des comptes admin
    'admin_accounts': [
        {'username': 'admin', 'privilege': '15', 'password': 'admin123'},
        {'username': 'backup', 'privilege': '5', 'password': 'backup123'}
    ],

    # Liste des serveurs DNS
    'dns_servers': ['172.16.1.1', '172.16.1.2'],

    # Liste des serveurs NTP
    'ntp_servers': ['10.100.1.1'],

    # Configuration des VLANs
    'vlans': [
        {'vlan_id': '12', 'name': 'DATA'},
        {'vlan_id': '13', 'name': 'RF'},
        {'vlan_id': '30', 'name': 'MECA'},
        {'vlan_id': '100', 'name': 'MPLS'},
        {'vlan_id': '101', 'name': 'INET-FO'},
        {'vlan_id': '102', 'name': 'INET-SL'},
        {'vlan_id': '37', 'name': 'ADMIN'}
    ],

    # Configuration des interfaces physiques
    'interfaces': [
        {
            'name': 'GigabitEthernet1/1/1',
            'description': 'Uplink to FW-BOU-RG-1',
            'mode': 'trunk',
            'allowed_vlans': '12,13,30,100,101,102,237',
            'duplex': 'auto',
            'speed': '1000',
            'shutdown': False
        },
        {
            'name': 'GigabitEthernet1/1/2',
            'description': 'Uplink to SW-BOU-RG-2',
            'mode': 'trunk',
            'allowed_vlans': '12,13,30,100,101,102,237',
            'duplex': 'auto',
            'speed': '1000',
            'shutdown': False
        },
        {
            'name': 'range GigabitEthernet1/0/1-40',
            'description': 'DATA',
            'mode': 'access',
            'vlan': '12',
            'duplex': 'full',
            'speed': '100',
            'shutdown': False
        },
        {
            'name': 'range GigabitEthernet1/0/41-42',
            'description': 'MECA',
            'mode': 'access',
            'vlan': '30',
            'duplex': 'full',
            'speed': '100',
            'shutdown': False
        },
		{
            'name': 'GigabitEthernet1/0/43',
            'description': 'MPLS',
            'mode': 'access',
            'vlan': '100',
            'duplex': 'full',
            'speed': '1000',
            'shutdown': False
        },
		{
            'name': 'GigabitEthernet1/0/44',
            'description': 'INET-FO',
            'mode': 'access',
            'vlan': '101',
            'duplex': 'full',
            'speed': '1000',
            'shutdown': False
        },
		{
            'name': 'range GigabitEthernet1/0/44-48',
            'description': 'BIN',
            'mode': 'access',
            'vlan': '666',
            'duplex': 'full',
            'speed': '1000',
            'shutdown': True
        }
    ],

    # Configuration des interfaces VLAN
    'vlan_interfaces': [
        {
            'vlan_id': '37',
            'description': 'VLAN 237 Interface',
            'ip_address': '10.37.1.253',
		    'subnet_mask': '255.255.255.0',
            'shutdown': False
        }
    ]
}

# Générer la configuration du switch à partir des données
config_output = template.render(switch_config)
# print(config_output)

# Définir le répertoire où sauvegarder le fichier
output_directory = "d:/devops/Coding/Python/Python4Network"  # Remplace par le chemin réel du répertoire

# Vérifier si le répertoire existe, sinon le créer
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Générer un fichier de configuration avec le hostname comme nom de fichier dans le répertoire spécifié
filename = f"{switch_config['hostname']}.conf"
file_path = os.path.join(output_directory, filename)

with open(file_path, 'w') as config_file:
    config_file.write(config_output)

print(f"Le fichier de configuration a été généré : {file_path}")
													
# Générer un fichier de configuration avec le hostname comme nom de fichier
filename = f"{switch_config['hostname']}.conf"
													

with open(filename, 'w') as config_file:
    config_file.write(config_output)

print(f"Le fichier de configuration a été généré : {filename}")
