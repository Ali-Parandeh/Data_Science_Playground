# Most shell commands will work on multiple files if you give them multiple filenames. 
# For example, you can get the first column from all of the seasonal data files at once like this:

cut -d , -f 1 seasonal/winter.csv seasonal/spring.csv seasonal/summer.csv seasonal/autumn.csv

# But typing the names of many files over and over is a bad idea: 
# it wastes time, and sooner or later you will either leave a file out 
# or repeat a file's name. To make your life better, the shell allows 
# you to use wildcards to specify a list of files with a single expression. 
# The most common wildcard is *, which means "match zero or more characters". 
# Using it, we can shorten the cut command above to this:

cut -d , -f 1 seasonal/*

# or:

cut -d , -f 1 seasonal/*.csv

# Write a single command using head to get the first three lines 
# from both seasonal/spring.csv and seasonal/summer.csv, 
# a total of six lines of data, but not from the autumn or 
# winter data files. Use a wildcard instead of spelling out the files' names in full.

$ head -n 3 seasonal/s*.csv

# ==> seasonal/spring.csv <==
# Date,Tooth
# 2017-01-25,wisdom
# 2017-02-19,canine

# ==> seasonal/summer.csv <==
# Date,Tooth
# 2017-01-11,canine
# 2017-01-18,wisdom

# Wild wildcard work! This becomes even more important if \
# your directory contains hundreds or thousands of files.

# How can I specify many files at once?
