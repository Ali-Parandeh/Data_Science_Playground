# How can I record what I just did?

# When you are doing a complex analysis, you will often want to keep a 
# record of the commands you used. You can do this with the tools you have already seen:

# Run history.
# Pipe its output to tail -n 10 (or however many recent steps you want to save).
# Redirect that to a file called something like figure-5.history.
# This is better than writing things down in a lab notebook because 
# it is guaranteed not to miss any steps. It also illustrates the 
# central idea of the shell: simple tools that produce and consume 
# lines of text can be combined in a wide variety of ways to solve a broad range of problems.

$ history
    # 1  history
$ histry | tail -n 10 > figure-5.history
# bash: histry: command not found
$ history | tail -n 10 > figure-5.history
$ ls
# backup  bin  course.txt  figure-5.history  people  seasonal
$ cat figure-5.history
    # 1  history
    # 2  histry | tail -n 10 > figure-5.history
    # 3  history | tail -n 10 > figure-5.history


# 1. Copy the files seasonal/spring.csv and seasonal/summer.csv to your home directory.
# 2. Use grep with the -h flag (to stop it from printing filenames) and -v Tooth 
# (to select lines that don't match the header line) to select the data records 
# from spring.csv and summer.csv in that order and redirect the output to temp.csv.
# 3. Pipe history into tail -n 3 and redirect the output to steps.txt to save 
# the last three commands in a file. (You need to save three instead of just 
# two because the history command itself will be in the list.)

$ cp seasonal/s*.csv /
# cp: cannot create regular file '/spring.csv': Permission denied
# cp: cannot create regular file '/summer.csv': Permission denied
$ cp seasonal/s*.csv ~
$ grep -h -v Tooth s*csv > temp.csv
$ history | tail -n 3 > steps.txt
$ ls
# backup  course.txt        people    spring.csv  summer.csv
# bin     figure-5.history  seasonal  steps.txt   temp.csv
$ cat steps.txt
    # 7  cp seasonal/s*.csv ~
    # 8  grep -h -v Tooth s*csv > temp.csv
    # 9  history | tail -n 3 > steps.txt