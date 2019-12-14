# Permissions Check

# As the CTO of your small startup you often 
# have to perform many roles. Some days this means 
# being the data scientists, data engineer, DevOps 
# engineer and machine learning engineer all at once. 
# Recently you setup a large network file system in 
# your cloud deployment that all of the instances 
# that perform machine learning will communicate with. 
# You are a strong believe in IaC (Infrastructure as Code). 
# As a result you want to verify that the when the network 
# filesystem is mounted on a new system that each worker 
# node is able to create files with the correct permissions.

# Write a script that will check for this by using subprocess.Popen 
# and os.stat. Be sure to use the variables in setup in your script!


# Execute a child program in a new process.
import subprocess
# Perform a stat system call on the given path.
import os

#setup
file_location = "/tmp/file.txt"
expected_uid = 1000
#touch a file
proc = subprocess.Popen(["touch", file_location])

#check user permissions
stat = os.stat(file_location)
if stat.st_uid == expected_uid:
  print(f"File System exported properly: {expected_uid} == {stat.st_uid}")
else:
  print(f"File System NOT exported properly: {expected_uid} != {stat.st_uid}")



# Shell
# In [21]: stat
Out[21]: os.stat_result(st_mode=33188, st_ino=15123466, st_dev=1048810, st_nlink=1, st_uid=1000, st_gid=1000, st_size=34, st_atime=1576342366, st_mtime=1576342366, st_ctime=1576342366)

In [22]: stat.st_uid
# Out[22]: 1000

# You were able to touch a file using the subprocess module and then inspect the permissions on the file that was created. 
# You also learned how to use os.stat which gives you useful metadata about files.