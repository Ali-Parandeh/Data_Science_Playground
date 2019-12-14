# Using subprocess Popen

# A coworker is proficient in Bash tells you that most 
# data engineering tasks should be done in the shell. 
# You mention a scripting language like Python can build 
# robust production systems that have high quality. 
# The code is often easier in practice to write and maintain, 
# even if you are directly calling shell commands. 
# You demonstrate how this works using a small Python 
# script that you write that finds all of the Python packages installed.

# Use Python, subprocess.Popen(), and the bash command pip list --format=json command, 
# to find all of the installed packages. The pip tool is a common method of installing 
# Python packages. The result will be a byte string, a Python3 construct. 
# The Popen command will use PIPE to send the JSON output to stdout.


# 1. Use the with context manager to run subprocess.Popen().
# 2. Pipe the output of subprocess.Popen() to stdout as an iterator.
# 3. Convert the JSON payload to a Python dictionary with json.loads after extracting the only element of the results list.
# 4. Print the result using the pprint function of the pprint package.


from subprocess import Popen, PIPE
import json
import pprint

# Use the with context manager to run subprocess.Popen()
with Popen(["pip","list","--format=json"], stdout=PIPE) as proc:
  # Pipe the output of subprocess.Popen() to stdout
  result = proc.stdout.read()
  
# Convert the JSON payload to a Python dictionary
# JSON is a datastructure similar to a Python dictionary
converted_result = json.loads(result)

# Display the result in the IPython terminal
pprint.pprint(converted_result)



# <script.py> output:
#     [{'name': 'asn1crypto', 'version': '0.24.0'},
#      {'name': 'asttokens', 'version': '1.1.11'},
#      {'name': 'attrs', 'version': '19.3.0'},
#      {'name': 'certifi', 'version': '2019.9.11'},
#      {'name': 'chardet', 'version': '3.0.4'},
#      {'name': 'Click', 'version': '7.0'},
#      {'name': 'cryptography', 'version': '2.1.4'},
#      {'name': 'decorator', 'version': '4.4.0'},
#      {'name': 'dill', 'version': '0.2.5'},
#      {'name': 'distro-info', 'version': '0.18'},
#      {'name': 'idna', 'version': '2.8'},
#      {'name': 'ipython', 'version': '4.2.1'},
#      {'name': 'ipython-genutils', 'version': '0.2.0'},
#      {'name': 'Jinja2', 'version': '2.10'},
#      {'name': 'jsonschema', 'version': '3.0.1'},
#      {'name': 'keyring', 'version': '10.6.0'},
#      {'name': 'keyrings.alt', 'version': '3.0'},
#      {'name': 'markdown2', 'version': '2.3.7'},
#      {'name': 'MarkupSafe', 'version': '1.1.1'},
#      {'name': 'numpy', 'version': '1.16.3'},
#      {'name': 'pandas', 'version': '0.24.1'},
#      {'name': 'pexpect', 'version': '4.7.0'},
#      {'name': 'pickleshare', 'version': '0.7.5'},
#      {'name': 'pip', 'version': '19.0.1'},
#      {'name': 'protobackend', 'version': '0.2.3'},
#      {'name': 'protowhat', 'version': '1.11.2'},
#      {'name': 'ptyprocess', 'version': '0.6.0'},
#      {'name': 'pycrypto', 'version': '2.6.1'},
#      {'name': 'pygobject', 'version': '3.26.1'},
#      {'name': 'pyrsistent', 'version': '0.15.4'},
#      {'name': 'python-apt', 'version': '1.6.3'},
#      {'name': 'python-crontab', 'version': '2.3.6'},
#      {'name': 'python-dateutil', 'version': '2.8.0'},
#      {'name': 'python-debian', 'version': '0.1.32'},
#      {'name': 'pythonbackend', 'version': '0.12.0'},
#      {'name': 'pythonwhat', 'version': '2.22.0'},
#      {'name': 'pytz', 'version': '2019.2'},
#      {'name': 'pyxdg', 'version': '0.25'},
#      {'name': 'PyYAML', 'version': '5.1'},
#      {'name': 'requests', 'version': '2.22.0'},
#      {'name': 'scikit-learn', 'version': '0.20.3'},
#      {'name': 'scipy', 'version': '1.3.1'},
#      {'name': 'SecretStorage', 'version': '2.3.1'},
#      {'name': 'setuptools', 'version': '41.4.0'},
#      {'name': 'simplegeneric', 'version': '0.8.1'},
#      {'name': 'six', 'version': '1.12.0'},
#      {'name': 'traitlets', 'version': '4.3.3'},
#      {'name': 'urllib3', 'version': '1.25.6'},
#      {'name': 'wheel', 'version': '0.30.0'}]


# Nice work finding the installed packages! Because the pip tool was able to emit JSON data, 
# you can use the built in json module to convert JSON data to a Python dictionary via 
# json.loads(). This was important because it allowed you to deserialize the output 
# and create a Python data structure and pprint it in a nicely formatted fashion.