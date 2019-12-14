# Use SList fields to parse shell output

# A Data Scientist who you highly respect at 
# work mentioned that IPython has a powerful data 
# type called SList that enables a user to perform 
# powerful operations on shell commands. In particular 
# they mention that there were able to easily extract 
# fields from the output of the df command. In this 
# exercise you investigate what you can accomplish 
# with the SList data type. You will start from this command: disk_space = !df -h

# Using the .fields method on the df variable, select the column that shows total size of the mounted volumes.

In [1]: !df -h
# Filesystem      Size  Used Avail Use% Mounted on
# overlay         335G  232G  103G  70% /
# tmpfs            64M     0   64M   0% /dev
# tmpfs           7.7G     0  7.7G   0% /sys/fs/cgroup
# /dev/nvme0n1p1  335G  232G  103G  70% /etc/hosts
# shm              64M   24K   64M   1% /dev/shm
# tmpfs           7.7G     0  7.7G   0% /proc/acpi
# tmpfs           7.7G     0  7.7G   0% /sys/firmware

In [3]: disk_space = !df -h

In [4]: disk_space.fields(1)
# Out[4]: ['Size', '335G', '64M', '7.7G', '335G', '64M', '7.7G', '7.7G']

In [5]: disk_space.fields(2)
# Out[5]: ['Used', '233G', '0', '0', '233G', '24K', '0', '0']

In [6]: disk_space.fields(3)
# Out[6]: ['Avail', '103G', '64M', '7.7G', '103G', '64M', '7.7G', '7.7G']

In [7]: disk_space.fields(0)
# Out[7]: 
# ['Filesystem',
#  'overlay',
#  'tmpfs',
#  'tmpfs',
#  '/dev/nvme0n1p1',
#  'shm',
#  'tmpfs',
#  'tmpfs']


# The second column of whitespace-separated fields is the Size. 
# Mastering the IPython and Jupyter filtering techniques for shell output can save many lines of code.