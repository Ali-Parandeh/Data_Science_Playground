# Running a click application from subprocess

# You are building many click command line applications and you 
# realize that it would be powerful to automate their execution by not 
# only humans but other scripts. Take an existing script that performs 
# KMeans clustering and execute it with two different options: 
# help and num. Run this inside of subprocess.run and print both outputs to standard out.

import subprocess

# run help for click tool
help_out = subprocess.run(["/usr/bin/python3.6", "./cluster.py", "--help"],
                     stdout=subprocess.PIPE)

# run cluster
cluster2 = subprocess.run(["/usr/bin/python3.6", "./cluster.py", "--num", "2"],
                     stdout=subprocess.PIPE)

# print help
print(help_out.stdout)

# print cluster output
print(cluster2.stdout)

# <script.py> output:
#     b'Usage: cluster.py [OPTIONS]\n\nOptions:\n  --num INTEGER  Number of clusters\n  --help         
#     Show this message and exit.\n'
#     b'Cluster assignments: [1 1 0 1 1 0 1 0 0 1] for total clusters [2]\n'

# Woohoo! You were able to fully exercise the click application by running the 
# --help option and the --num option. This will allow you to take your automation project to the next phase.

