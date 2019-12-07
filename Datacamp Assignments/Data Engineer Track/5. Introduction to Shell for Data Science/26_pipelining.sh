# To wrap up, you will build a pipeline to find out how many 
# records are in the shortest of the seasonal data files.

# Use wc with appropriate parameters to list the number of 
# lines in all of the seasonal data files. 
# (Use a wildcard for the filenames instead of typing them all in by hand.)
# Add another command to the previous one 
# using a pipe to remove the line containing the word "total".
# Add two more stages to the pipeline that use 
# sort -n and head -n 1 to find the file containing the fewest lines.

$ wc -l seasonal/*.csv

#   21 seasonal/autumn.csv
#   24 seasonal/spring.csv
#   25 seasonal/summer.csv
#   26 seasonal/winter.csv
#   96 total

$ wc -l seasonal/*.csv | grep -v total

#   21 seasonal/autumn.csv
#   24 seasonal/spring.csv
#   25 seasonal/summer.csv
#   26 seasonal/winter.csv

$ wc -l seasonal/*.csv | grep -v total | sort -n | head -n 1

#   21 seasonal/autumn.csv

# It turns out autumn.csv is the file with the fewest lines. 
# Rush over to chapter 4 to learn more about batch processing!