from netmiko import ConnectHandler
import difflib
import re

def get_config_from_switch(device, command="show startup-config"):
    """ Récupère la configuration du switch """
    connection = ConnectHandler(**device)
    connection.enable()
    config = connection.send_command(command)
    connection.disconnect()
    return config

def filter_config(config):
    """ Filtre les lignes non pertinentes dans la configuration """
    filtered_config = []
    for line in config.splitlines():
        line = line.strip()
        # Ignorer les lignes vides, celles commençant par !, #, "Using certificate", ou des chiffres seuls
        if not line or line.startswith("!") or line.startswith("#") or "Using certificate" in line or re.match(r"^\d+$", line):
            continue
        filtered_config.append(line)
    return "\n".join(filtered_config)

def compare_configs(local_config, remote_config):
    """ Compare deux configurations et génère un rapport """
    diff = difflib.unified_diff(local_config.splitlines(), remote_config.splitlines(), lineterm='', n=0)
    differences = "\n".join(diff)
    return differences

def copy_local_to_nvram(device, local_config):
    """ Copie la configuration locale sur le switch (NVRAM) """
    connection = ConnectHandler(**device)
    connection.enable()
    
    # Envoyer les lignes de la configuration locale
    connection.send_config_set(local_config.splitlines())
    
    # Sauvegarder dans la NVRAM (startup-config)
    connection.save_config()
    
    connection.disconnect()

def generate_report(switch_name, ip, differences):
    """ Génère un rapport des différences de configurations """
    report = f"Différences détectées pour {switch_name} (IP: {ip}):\n"
    report += differences
    with open(f"diff_report_{switch_name}.txt", "w") as file:
        file.write(report)

def reboot_switch(device):
    """ Redémarre le switch """
    connection = ConnectHandler(**device)
    connection.enable()
    connection.send_command_timing("reload", delay_factor=2)
    connection.send_command_timing("\n")  # Confirme le redémarrage
    connection.disconnect()

# Informations sur le switch
device = {
    'device_type': 'cisco_ios',
    'host': '192.168.1.1',  # Remplace par l'IP du switch
    'username': 'admin',
    'password': 'password',
    'secret': 'enable_password',  # Si nécessaire
}

# Chemin du fichier de configuration local
local_config_file = "local_config.txt"

# Étape 1: Comparaison de la startup-config avec la configuration locale
startup_config = get_config_from_switch(device, "show startup-config")
with open(local_config_file, "r") as file:
    local_config = file.read()

# Filtrer les configurations
filtered_startup_config = filter_config(startup_config)
filtered_local_config = filter_config(local_config)

# Comparer les configurations
diff_startup = compare_configs(filtered_local_config, filtered_startup_config)

if diff_startup:
    print("Startup-config differs from local config. Applying local config to NVRAM.")
    copy_local_to_nvram(device, filtered_local_config)
    generate_report(device['host'], device['host'], diff_startup)
else:
    print("Startup-config is identical to local config.")

# Étape 2: Comparaison de la running-config avec la configuration locale
running_config = get_config_from_switch(device, "show running-config")
filtered_running_config = filter_config(running_config)

diff_running = compare_configs(filtered_local_config, filtered_running_config)

if diff_running:
    print("Running-config differs from local config. Rebooting the switch.")
    reboot_switch(device)
else:
    print("Running-config is identical to local config.")
