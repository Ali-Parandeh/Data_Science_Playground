'''
Use the information from the context to identify the packages in the directory that follow the minimal structure.


recognizing_packages
├── MY_PACKAGE
│   └── _init_.py
├── package
│   └── __init__.py
├── package_py
│   └── __init__
│       └── __init__.py
├── py_package
│   └── __init__.py
├── pyackage
│   └── init.py
└── my_script.py



'''
# Import local packages
import py_package
import package

# View the help for each package
help(py_package)
help(package)


'''
<script.py> output:
    Help on package py_package:
    
    NAME
        py_package
    
    PACKAGE CONTENTS
    
    
    FILE
        /tmp/tmp79soebxy/py_package/__init__.py
    
    
    Help on package package:
    
    NAME
        package
    
    PACKAGE CONTENTS
    
    
    FILE
        /tmp/tmp79soebxy/package/__init__.py

Great work! A minimal package skeleton requires a directory with an init.py 
inside of it (even though all of these would import without 
error when using Python version 3.3 or above).
'''
