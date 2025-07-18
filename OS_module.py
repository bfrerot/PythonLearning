##########  OS MODULE ##########

# os module enables you to:
#   get information about the operating system
#   manage processes
#   operate on I/O streams using file descriptors



### Getting information about the operating system

# os module provides a function called uname which returns an object containing the following attributes:

# systemname = stores the name of the operating system
# nodename = stores the machine name on the network
# release = stores the operating system release
# version = stores the operating system version
# machine = stores the hardware identifier


## os.name()
import os
print(os.name)
# nt



### Creating directories in Python

## os.mkdir()
# crée un dossier

import os
os.mkdir("my_first_directory")
print(os.listdir())
# ['.git', '.vscode', 'ascii.pdf', 'bac-à-sable.py', 'Books', 'Boolean&Comparatifs.py', 'Break-Continue.py', 'data.txt', 'data_engineer_skills.txt', 
#  'Dictionnaries.py', 'file.bin', 'file.bin.bck', 'Files.py', 'For.py', 'Functions-BUILT-IN.py', 'Functions.py', 'Generators-Iterators.py', 'If-Else.py', 
#  'Lambda.py', 'List.py', 'Logical-Bitwise.py', 'Methods-DICTIONARIES.py', 'Methods-FILE.py', 'Methods-LIST.py', 'Methods-NUMBER.py', 'Methods-SET.py', 
#  'Methods-STRING.py', 'Methods-TUPLE.py', 'Module-Test', 'Module.py', 'Modules-BUILT-IN.py', 'my_first_directory', 'newtext.txt', 'Numbers.py', 'Numpy-ARRAYS.py', 
#  'Numpy-FUNCTIONS.py', 'Numpy.py', 'OOP.py', 'os_module.py', 'Package.py', 'Pip.py', 'Print.py', 'processus.xlsx', 'projects', 'Python-key-words.py', 
#  'Python_error_tree.mmd', 'Score Report.pdf', 'Set.py', 'Strings.py', 'text.txt', 'Try&Except.py', 'Tuples.py', 'Variables.py', 'While.py']


## os.listdir(projects)
# crée une list des sous-réperoires et files du répertoire courant ou celui indiqué comme argument

print(os.listdir("projects"))
# ['AP-wifi.svg', 'caesar_cipher.py', 'calcul BMI.py', 'calcul heure fin de reunion.py', 'calcul investissement intéret.py', 
#  'calcul_moyenne_classe.py', 'classer&compter.py', 'configuration réseau.py', 'copy_paste.py', 'créer un hostname.py', 
#  'créer_video_image_fixe.py', 'Derminer si on a un triangle.py', 'Find prime numbers.py', 'Fuel-consumption-conversion.py', 
#  'gérer_anniversaires_amis.py', 'IBAN_validator', 'inventaire_produits.py', 'investment_calculator.py', 'Leap or Common year.py', 
#  'LIST_vs_GENERATOR_for_file_anlalysis', 'lyrics into chart.py', 'Numbers of days in any year-month pair.py', 
#  'number_processor.py', 'python_error-branch.py', 'Somme produit factoriel.py', 'Suite de Fibonacci.py', 'Tax_calculator.py', 
#  'Temperature_convertor.py', 'TicTacToe.py', 'time-calculator.py', 'volume.py']


## os.makedirs("dir1/"dir2"/../"dirX")
# permet de créer des dossiers et sous-dossiers de façon récursive

import os
os.makedirs("my_first_directory/my_second_directory")
# créée 2 dossiers: my_first_directory et my_second_directory


## os.chdir("dir1")
# permet de changer de directory

import os
os.chdir("my_first_directory")
print(os.listdir())
# ['my_second_directory']


## os.getcwd()
# = pwd = permet de savoir dans  quel répertoire courrant on se situe

import os
os.makedirs("my_first_directory/my_second_directory")
os.chdir("my_first_directory")
print(os.getcwd())
# C:\PythonLearning\my_first_directory
os.chdir("my_second_directory")
print(os.getcwd())
# C:\PythonLearning\my_first_directory\my_second_directory


## os.rmdir("dirX")
# permet de supprimer un dossier vide

import os
os.makedirs("my_first_directory/my_second_directory")
os.rmdir("my_first_directory")

# si repertoire en contient d'autres:
# OSError: [WinError 145] Le répertoire n’est pas vide: 'my_first_directory'
    

## os.removedirs("dir1/"dir2"/../"dirX")
# permet de supprimer une chaine de dosssiers

import os
os.removedirs("my_first_directory/my_second_directory")

 