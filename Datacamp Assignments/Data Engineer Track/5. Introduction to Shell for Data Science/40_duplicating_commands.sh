# How can one shell script do many things?

# Our shells scripts so far have had a single command or pipe, 
# but a script can contain many lines of commands. For example, 
# you can create one that tells you how many records are in the 
# shortest and longest of your data files, i.e., the range of your datasets' lengths.

# Note that in Nano, "copy and paste" is achieved by navigating to the 
# line you want to copy, pressing CTRL + K to cut the line, then CTRL + U twice to paste two copies of it.

# As a reminder, to save what you have written in Nano, type Ctrl + O 
# to write the file out, then Enter to confirm the filename, then Ctrl + X to exit the editor.

$ nano range.sh
# wc -l $@ | grep -v total | sort -n | head -n 1
# wc -l $@ | grep -v total | sort -n -r | head -n 1 
$ bash range.sh seasonal//*.csv > range.out
$ cat range.out
#   21 seasonal/autumn.csv
#   26 seasonal/winter.csv