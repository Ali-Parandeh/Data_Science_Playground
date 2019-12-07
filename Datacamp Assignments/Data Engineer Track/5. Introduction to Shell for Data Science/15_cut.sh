#  head and tail let you select rows from a text file. If you want to select columns, 
#  you can use the command cut. It has several options (use man cut to explore them), 

$ cut -f 2-5,8 -d , values.csv

# which means "select columns 2 through 5 and columns 8, 
#  using comma as the separator". cut uses -f (meaning "fields") 
#  to specify columns and -d (meaning "delimiter") to specify the separator. 
#  You need to specify the latter because some files may use spaces, tabs, or colons to separate columns.

# What command will select the first column (containing dates) from the file spring.csv?

# Note Adding a space after the flag is good style, but not compulsory.

$ cut -f 1 -d , seasonal/spring.csv

# Date
# 2017-01-25
# 2017-02-19
# 2017-02-24
# 2017-02-28
# 2017-03-04
# 2017-03-12
# 2017-03-14
# 2017-03-21
# 2017-04-29
# 2017-05-08
# 2017-05-20
# 2017-05-21
# 2017-05-25
# 2017-06-04
# 2017-06-13
# 2017-06-14
# 2017-07-10
# 2017-07-16
# 2017-07-23

# What is the output of 
$ cut -d : -f 2-4 
# on the line:
# first:second:third:

# Answer 
# second:third:
