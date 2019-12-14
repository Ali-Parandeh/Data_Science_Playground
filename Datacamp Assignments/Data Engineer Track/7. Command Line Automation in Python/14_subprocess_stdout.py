# Counting files in a directory tree

# After the last bad experience with corrupt backups at your company, 
# you decide to rewrite the backup script from scratch in Python. 
# One of the improvements you want to make is to audit the number of 
# files in a subdirectory and count them. You will then ensure the 
# exact same number of files exists in a directory tree before and 
# after the backup. This will create a validation step that was missing in the last script.

# Use subprocess.run to pipe the output of the find command to wc -l to print the numbers of files in the directory tree.

# 1. Use subprocess.run to run unix command find . -type f -print.
# 2. Send the output of the find command to the input of wc -l.
# 3. Decode the bytes to strings.
# 4. Strip the output of spaces and print.

import subprocess

# runs find command to search for files
find = subprocess.Popen(["find", ".", "-type", "f", "-print"], stdout=subprocess.PIPE)

# runs wc and counts the number of lines
word_count = subprocess.Popen(["wc", "-l"], stdin=find.stdout, stdout=subprocess.PIPE)

# print the decoded and formatted output
output = word_count.stdout.read()
print(output.decode('utf-8').strip())

# <script.py> output:
#     200

# Way to go, you were able to find all 200 files! 
# The find command is a powerful Unix utility and you 
# were able to leverage it to quickly search for files 
# and count them. This highlights a unique strength of 
# Python to glue the output of existing solutions into 
# existing Python workflows. This can be an invaluable skill when working with data in your career.

