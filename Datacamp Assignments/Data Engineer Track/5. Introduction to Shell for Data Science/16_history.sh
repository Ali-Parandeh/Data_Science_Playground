# One of the biggest advantages of using the shell is that it makes it easy 
# for you to do things over again. If you run some commands, you can then 
# press the up-arrow key to cycle back through them. You can also use the 
# left and right arrow keys and the delete key to edit them. 
# Pressing return will then run the modified command.

# Even better, history will print a list of commands you have run recently. 
# Each one is preceded by a serial number to make it easy to re-run particular commands: 
# just type !55 to re-run the 55th command in your history (if you have that many). 
# You can also re-run a command by typing an exclamation mark followed by the command's name, 
# such as !head or !cut, which will re-run the most recent use of that command.

$ head summer.csv
# head: cannot open 'summer.csv' for reading: No such file or directory

$ cd seasonal/

$ !head

# head summer.csv
# Date,Tooth
# 2017-01-11,canine
# 2017-01-18,wisdom
# 2017-01-21,bicuspid
# 2017-02-02,molar
# 2017-02-27,wisdom
# 2017-02-27,wisdom
# 2017-03-07,bicuspid
# 2017-03-15,wisdom
# 2017-03-20,canine

$ history

    # 1  history
    # 2  head summer.csv
    # 3  cd seasonal/
    # 4  head summer.csv
    # 5  history

$ !head 2
# head summer.csv 2
# ==> summer.csv <==
# Date,Tooth
# 2017-01-11,canine
# 2017-01-18,wisdom
# 2017-01-21,bicuspid
# 2017-02-02,molar
# 2017-02-27,wisdom
# 2017-02-27,wisdom
# 2017-03-07,bicuspid
# 2017-03-15,wisdom
# 2017-03-20,canine