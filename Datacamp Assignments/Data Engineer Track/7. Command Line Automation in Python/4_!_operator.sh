# Using the ! operator in IPython

# You have a directory full of files you want the size of. 
# You need a technique that will allow you to filter patterns. 
# You want to do this in Python. Use the ! operator to create a 
# command that sums the total size of the files in a directory. 
# The piped command will use this awk snippet awk '{ SUM+=$5} END {print SUM}'. 
# Awk is a tool that is used often on the Unix command line because it 
# understands how to deal with whitespace delimited output from shell commands. 
# The awk command works well at grabbing fields from a string

In [19]: !ls -l | awk '{SUM+=$5} END {print SUM}'
# 4096
