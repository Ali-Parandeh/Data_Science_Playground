# Detecting duplicate files with subprocess

# Imagine you are a new data scientist at a startup, and you have 
# been tasked with doing machine learning on Terabytes of data. 
# The CEO has mentioned they have a small budget to train your model. 
# You notice many duplicate files when manually inspecting. If you can 
# identify the duplicate files before you begin training, this 
# potentially saves 50% of the cost of training.

# In this exercise, you will find duplicate files by using the subprocess.Popen() 
# module and capturing the output of the md5sum command. The md5sum utility is a 
# shell command that finds the unique hash of each file. There is a list of files 
# available via the files variable that you can iterate over. Popen and PIPE have 
# already been imported for you from the subprocess module. ['file_8.csv'...]

from subprocess import (Popen, PIPE)

checksums = {}
duplicates = []
files  = ['test_dir/file_2.csv',
 'test_dir/file_0.csv',
 'test_dir/file_9.csv',
 'test_dir/file_7.csv',
 'test_dir/file_1.csv',
 'test_dir/file_5.csv',
 'test_dir/file_3.csv',
 'test_dir/file_4.csv',
 'test_dir/file_8.csv',
 'test_dir/file_6.csv']

# Iterate over the list of files filenames
for filename in files:
  	# Use Popen to call the md5sum utility
    with Popen(["md5sum", filename], stdout=PIPE) as proc:
        checksum, _ = proc.stdout.read().split()
        
        # Append duplicate to a list if the checksum is found
        if checksum in checksums:
            duplicates.append(filename)
        checksums[checksum] = filename

print(f"Found Duplicates: {duplicates}")

# <script.py> output:
#     Found Duplicates: ['test_dir/file_0.csv', 'test_dir/file_9.csv', 
#     'test_dir/file_7.csv', 'test_dir/file_1.csv', 'test_dir/file_5.csv', 
#     'test_dir/file_3.csv', 'test_dir/file_4.csv', 'test_dir/file_8.csv', 'test_dir/file_6.csv']


# There can be too much of a good thing. You used the md5sum utility running inside of 
# Popen to figure out which files had the same digital signature. Now you can decide 
# what you want to do with these duplicate files. Delete them? Archive them?