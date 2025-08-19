########## pip ##########



### 2 * basic entities have to be established and kept in motion: 

#       a centralized repository of all available software packages = PyPI = Python Package Index
#               maintained by Packaging Working Group
#               https://wiki.python.org/psf/PackagingWG + https://pypi.org/

#       a tool allowing users to access the repository = pip
#               pip means “pip installs packages”, and the pip inside “pip installs packages” means “pip installs packages” and ...etc
#               pip can discover, identify, and resolve all dependencies
#               It can do it in the cleverest way avoiding any unnecessary downloads and reinstalls

# Both these entities already exist and can be used at any time.


### useful commands

## pip help

# PS C:\PythonLearning> pip help

# Usage:
#   pip <command> [options]

# Commands:
#   install                     Install packages.
#   lock                        Generate a lock file.
#   download                    Download packages.
#   uninstall                   Uninstall packages.
#   freeze                      Output installed packages in requirements format.
#   inspect                     Inspect the python environment.
#   list                        List installed packages.
#   show                        Show information about installed packages.
#   check                       Verify installed packages have compatible dependencies.
#   config                      Manage local and global configuration.
#   search                      Search PyPI for packages.
  

## pip list

# PS C:\PythonLearning> pip list
# Package                   Version
# ------------------------- --------------
# ..
# Jinja2                    3.1.6
# json5                     0.12.0
# jsonpointer               3.0.0
# jsonschema                4.23.0
# jsonschema-specifications 2025.4.1
# jupyter_client            8.6.3
# jupyter_core              5.7.2
# jupyter-events            0.12.0
# jupyter-lsp               2.2.5
# jupyter_server            2.16.0
# jupyter_server_terminals  0.5.3
# jupyterlab                4.4.2
# jupyterlab_pygments       0.3.0
# jupyterlab_server         2.27.3
# ..
# matplotlib                3.10.3
# matplotlib-inline         0.1.7
# ..
# numpy                     2.2.6
# ..
# pandas                    2.2.3
# pandocfilters             1.5.1
# ..


## pip search [anything]

# The anystring you provide will be searched in:

# the names of all the packages;
# the summary strings of all the packages.


## pip install -U [package_name]

# pour updater les packages et avoir la dernière version
# pip install package_name==package_version
# pip install pygame==1.9.2


## pip uninstall package_name

# pour désinstaller les packages


## pip show [package]

# pour les infos liées à un package

'''
pip show  # manque le package
WARNING: ERROR: Please provide a package name or names.

pip show numpy
Name: numpy
Version: 2.2.6
Summary: Fundamental package for array computing in Python
Home-page: https://numpy.org
Author: Travis E. Oliphant et al.
Author-email:
License: Copyright (c) 2005-2024, NumPy Developers.
 All rights reserved.
etc
etc
'''