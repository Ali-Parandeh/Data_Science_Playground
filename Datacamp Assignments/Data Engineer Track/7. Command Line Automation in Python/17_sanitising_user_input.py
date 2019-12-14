# Directory summarizer

# Your high performance laptop with solid state drives and a 
# GPU capable of doing deep learning was a great investment. 
# One issue you have though is that your hard drive keeps filling 
# up with machine learning data. You need to write a script that 
# will calculate the total disk usage from an arbitrary amount of 
# directories you pass in. After you finish this script locally 
# you plan on using it on your work file system as well. 
# Eventually you then turn it into a sophisticated tool that 
# manages disk storage in Python or you would just use the 
# Unix du command alone. You are very concerned about accepting 
# user input that could permanently delete user data or cause a security hole.

# Use shlex and subprocess to get the total storage of a list of directories.

# 1. Use shlex.split to safely split a list of directories: pluto, mars and jupiter.
# 2. Pass the output of the shlex.split to subprocess.run.
# 3. Print out the results.
# 4. The subprocess and shlex module have been imported for you.

import subprocess
import shlex

print("Enter a list of directories to calculate storage total: \n")
user_input = "pluto mars jupiter"

# Sanitize the user input
sanitized_user_input = shlex.split(user_input)
print(f"raw_user_input: {user_input} |  sanitized_user_input: {sanitized_user_input}")

# Safely Extend the command with sanitized input
cmd = ["du", "-sh", "--total"]
cmd.extend(sanitized_user_input)
print(f"cmd: {cmd}")

# Print the totals out
disk_total = subprocess.run(cmd, stdout=subprocess.PIPE)
print(disk_total.stdout.decode("utf-8"))


# <script.py> output:
#     Enter a list of directories to calculate storage total: 
    
#     raw_user_input: pluto mars jupiter |  sanitized_user_input: ['pluto', 'mars', 'jupiter']
#     cmd: ['du', '-sh', '--total', 'pluto', 'mars', 'jupiter']
#     1.1M	pluto
#     1.1M	mars
#     1.1M	jupiter
#     3.1M	total


#  You were able use the shlex.split command to create a safely run Unix tool 
#  that calculated disk usage. The key difference in shlex.split is that 
#  it can safely quote unix strings and prevent attack vectors versus a 
#  regular string split method that doesn't have this capability.