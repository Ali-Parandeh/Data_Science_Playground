# How does the shell store information?
# Like other programs, the shell stores information in variables. 
# Some of these, called environment variables, are available all the time. 
# Environment variables' names are conventionally written in upper case, 
# and a few of the more commonly-used ones are shown below.

# Variable	Purpose	Value
# HOME	User's home directory	/home/repl
# PWD	Present working directory	Same as pwd command
# SHELL	Which shell program is being used	/bin/bash
# USER	User's ID	repl
# To get a complete list (which is quite long), you can type set in the shell.




$ set | grep HISTFILESIZE
# HISTFILESIZE=2000
