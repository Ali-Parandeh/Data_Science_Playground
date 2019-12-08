# How can I re-use pipes?

# A file full of shell commands is called a *shell script, or sometimes just a "script" 
# for short. Scripts don't have to have names ending in .sh, but this lesson will 
# use that convention to help you keep track of which files are scripts.

# Scripts can also contain pipes. For example, if all-dates.sh contains this line:

cut -d , -f 1 seasonal/*.csv | grep -v Date | sort | uniq

# then:

bash all-dates.sh > dates.out

# will extract the unique dates from the seasonal data files and save them in dates.out.

$ nano all-dates.sh
$ ls
# all-dates.sh  backup  bin  course.txt  people  seasonal  teeth.sh  test.sh
$ bash all-dates.sh > dates.out
$ ls
# all-dates.sh  bin         dates.out  seasonal  test.sh
# backup        course.txt  people     teeth.sh
$ head dates.out
# 2017-01-03
# 2017-01-05
# 2017-01-11
# 2017-01-17
# 2017-01-18
# 2017-01-21
# 2017-01-25
# 2017-02-01
# 2017-02-02
# 2017-02-05

# Assignment
# 1. A file teeth.sh in your home directory has been prepared for you, but contains some blanks. 
# Use Nano to edit the file and replace the two ____ placeholders with seasonal/*.csv and -c 
# so that this script prints a count of the number of times each tooth name appears 
# in the CSV files in the seasonal directory.
# 2. Use bash to run teeth.sh and > to redirect its output to teeth.out.
# 3. Run cat teeth.out to inspect your results.

$ nano teeth.sh
# cut -d , -f 2 seasonal/*.csv | grep -v Tooth | sort | uniq -c
$ bash teeth.sh > teeth.out
$ cat teeth.out
    #  15 bicuspid
    #  31 canine
    #  18 incisor
    #  11 molar
    #  17 wisdo