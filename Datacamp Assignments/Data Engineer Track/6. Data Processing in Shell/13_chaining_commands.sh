# Chaining commands using operators

# The more we use command-line tools, the more we start 
# stringing complex commands together. Sometimes it's for 
# convenience, but other times, the output of one command 
# can be used as input to another. Let's get some hands on 
# practice with this by filling in the correct chain 
# operators for the circumstances described in the instructions below.

# 1. Use the chain operator that allows csvlook to run first, and if it succeeds, then run csvstat.
# 2. Use the chain operator that to pass the output of csvsort as input to csvlook.
# 3. Use the 2 chain operators that takes the top 15 results from the sorted output and saves it to a new file.

# If csvlook succeeds, then run csvstat 
csvlook Spotify_Popularity.csv && csvstat Spotify_Popularity.csv

# Use the output of csvsort as input to csvlook
csvsort -c 2 Spotify_Popularity.csv | csvlook

# Take top 15 rows from sorted output and save to new file
csvsort -c 2 Spotify_Popularity.csv | head -n 15 > Spotify_Popularity_Top15.csv
# Preview the new file 
csvlook Spotify_Popularity_Top15.csv