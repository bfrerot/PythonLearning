########## CONFIG PARSER MODULE ##########


## This module provides functionality to parse configuration files using the configparser library
import configparser


## example of ini authentifixation configuration file
'''
[DEFAULT]
host = localhost # This is a comment.

[mariadb]
name = hello
user = user
password = password

[redis]
port = 6379
db = 0
'''


## read configuration file

import configparser # importing the configparser module

config = configparser.ConfigParser() # creating a ConfigParser object
print(config.read('config.ini')) # reading the configuration file named 'config.ini'

print('Sections:', config.sections(),'\n') # printing the sections available in the configuration file

print('mariadb section:')
print('Host:', config['mariadb']['host']) # accessing the 'host' value from the 'mariadb' section
print('Database:', config['mariadb']['name']) # accessing the 'name' value from the 'mariadb' section
print('Username:', config['mariadb']['user']) # accessing the 'user' value from the 'mariadb' section
print('Password:', config['mariadb']['password'], '\n') # accessing the 'password' value from the 'mariadb' section

print('redis section:')
print('Host:', config['redis']['host'])
print('Port:', int(config['redis']['port']))
print('Database number:', int(config['redis']['db']))

'''
['config.ini']
Sections: ['mariadb', 'redis']

mariadb section:
Host: localhost # This is a comment.
Database: hello
Username: user
Password: password

redis section:
Host: localhost # This is a comment.
Port: 6379
Database number: 0
'''

# => DEFAULT section doesn't appear in the list of returned sections
#    This is the default behavior of the sections method



## using get() method to access values

import configparser # importing the configparser module

config = configparser.ConfigParser() # creating a ConfigParser object
config.read('config.ini') # reading the configuration file named 'config.ini'

print('Host:', config.get('mariadb', 'host')) # accessing the 'host' value from the 'mariadb' section using get() method
'''
Host: localhost # This is a comment.
'''


## reading data from a dictionnary

import configparser

config = configparser.ConfigParser()

dict = { # key-value pairs representing configuration sections and their options
    'DEFAULT': {
        'host': 'localhost'
    },
    'mariadb': {
        'name': 'hello',
        'user': 'root',
        'password': 'password'
    },
    'redis': {
        'port': 6379,
        'db': 0
    }
}

config.read_dict(dict) # method to read from a dictionnary

print('Sections:', config.sections(),'\n')

print('mariadb section:')
print('Host:', config['mariadb']['host'])
print('Database:', config['mariadb']['name'])
print('Username:', config['mariadb']['user'])
print('Password:', config['mariadb']['password'], '\n')

print('redis section:')
print('Host:', config['redis']['host'])
print('Port:', int(config['redis']['port']))
print('Database number:', int(config['redis']['db']))

'''
Sections: ['mariadb', 'redis'] 

mariadb section:
Host: localhost
Database: hello
Username: root
Password: password

redis section:
Host: localhost
Port: 6379
Database number: 0
'''



## read_file() method to read from a file




## read_string() method to read from a string



## write() method to write configuration to a file

import configparser

config = configparser.ConfigParser()

config['DEFAULT'] = {'host': 'localhost'}
config['mariadb'] = {'name': 'hello',
                     'user': 'root',
                     'password': 'password'}
config['redis'] = {'port': 6379,
                   'db': 0}

with open('config2.ini', 'w') as configfile:
    config.write(configfile)

# The above code creates a configuration file named 'config2.ini' with the specified sections and options.
'''
[DEFAULT]
host = localhost

[mariadb]
name = hello
user = root
password = password

[redis]
port = 6379
db = 0
'''


## changing values in the configuration file

config.read('config.ini')

config['redis']['db'] = '1'

with open('config.ini', 'w') as configfile:
    config.write(configfile)
    
    

## interpolating values

'''
[DEFAULT]
host = localhost

[mariadb]
name = hello
user = user
password = password

[redis]
port = 6379
db = 0
dsn = redis://%(host)s # interpolated value between % and s = redis://localhost
'''