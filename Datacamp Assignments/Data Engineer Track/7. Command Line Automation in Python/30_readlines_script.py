# Backwards day

# A colleague has written a Python script that reverse all lines in a 
# file and prints them out one by one. This is an integration tool for 
# some NLP (Natural Language Processing) work your department is involved in. 
# You want to call their script, reverseit.py from a python program you 
# are writing so you can use it as well. Use your knowledge of sys.argv 
# and subprocess to write a file, then pass that file to the script that processes it.

import subprocess

# Write a file
with open("input.txt", "w") as input_file:
  input_file.write("Reverse this string\n")
  input_file.write("Reverse this too!")

# runs python script that reverse strings in a file line by line
run_script = subprocess.Popen(
    ["/usr/bin/python3", "reverseit.py", "input.txt"], stdout=subprocess.PIPE)

# print out the script output
for line in run_script.stdout.readlines():
  print(line)


# <script.py> output:
#     b'\n'
#     b'gnirts siht esreveR\n'
#     b'!oot siht esreveR\n'


# Great work at reusing your colleagues code! 
# You were able to write a file then pass that file into the input of an existing Python script which processed your text file.

