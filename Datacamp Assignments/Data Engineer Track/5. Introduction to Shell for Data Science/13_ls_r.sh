# In order to see everything underneath a directory, no matter 
# show deeply nested it is, you can give ls the flag -R (which means "recursive").

# To help you know what is what, ls has another flag -F that 
# prints a / after the name of every directory and a * after the name of every runnable program

#  (The order of the flags doesn't matter, but the directory name must come last.)

$ ls -R
# .:
# backup  bin  course.txt  people  seasonal

# ./backup:

# ./bin:

# ./people:
# agarwal.txt

# ./seasonal:
# autumn.csv  spring.csv  summer.csv  winter.csv

$ ls -R -F

# .:
# backup/  bin/  course.txt  people/  seasonal/

# ./backup:

# ./bin:

# ./people:
# agarwal.txt

# ./seasonal:
# autumn.csv  spring.csv  summer.csv  winter.csv