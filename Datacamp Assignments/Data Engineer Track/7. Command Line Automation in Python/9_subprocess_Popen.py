# Reading a creepy AI poem

# As a mad scientists working on AGI (Artificial General Intelligence) 
# in your underground bunker in Siberia, you have come up with a program 
# that appears to show signs of human level intelligence. Your program was 
# trained to write poems and initially showed signs of true brilliance. 
# You read one of the poems and it seemed a bit creepy and repetitive. 
# You need to write a script that inspects some of the output of the 
# computer generated poems it is writing. The Unix command head will 
# read the first few lines. The Unix command wc -w will count the 
# total number of words. The name of the poem is called poem.txt.

# Use subprocess.Popen to run each of these shell commands print 
# the results. You must pass stdout=subprocess.PIPE into Popen to capture the output of wc.

# 1. Print the first few lines of poem.txt using head.
# 2. Count the total words in poem.txt using wc -w and print out the total.
# 3. Safely execute these commands by passing them in as items in a list.


import subprocess

# Execute Unix command `head` safely as items in a list
with subprocess.Popen(["head", "poem.txt"], stdout=subprocess.PIPE) as head:
  
  # Print each line of list returned by `stdout.readlines()`
  for line in head.stdout.readlines():
    print(line)

# <script.py> output:
#     b'All work and no play makes Jack a dull boy.\n'
#     b'All work and no play makes Jack a dull boy.\n'
#     b'All work and no play makes Jack a dull boy.\n'
#     b'All work and no play makes Jack a dull boy.\n'
#     b'All work and no play makes Jack a dull boy.\n'
#     b'All work and no play makes Jack a dull boy.\n'
#     b'All work and no play makes Jack a dull boy.\n'
#     b'All work and no play makes Jack a dull boy.\n'
#     b'All work and no play makes Jack a dull boy.\n'
#     b'All work and no play makes Jack a dull boy.\n'
    
# Execute Unix command `wc -w` safely as items in a list
with subprocess.Popen(["wc", "-w", "poem.txt"], stdout=subprocess.PIPE) as word_count:
  
  # Print the string output of standard out of `wc -c`
  print(word_count.stdout.read())


# <script.py> output:
#     b'10000 poem.txt\n'


# You were able to safely run two Unix commands in subprocess.Popen and potentially prevent AI from taking over the world. 
# The head command was used to print the first use lines. The wc -w command was used to count words.