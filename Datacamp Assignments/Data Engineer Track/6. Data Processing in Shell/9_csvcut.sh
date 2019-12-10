# Printing column headers with csvkit

# There are many ways to preview the data within csvkit alone
# (e.g. csvlook, csvstat, etc). However, if all we want is to find 
# the position and name of the columns in our data, it is easier to 
# simply print a string of column headers. Let's print the column 
# headers for the data file Spotify_MusicAttributes.csv.


# Check to confirm name and location of data file
ls

# Print a list of column headers in data file 
csvcut -n Spotify_MusicAttributes.csv

# Spotify_MusicAttributes.csv  backup  bin
#   1: track_id
#   2: danceability
#   3: duration_ms
#   4: instrumentalness
#   5: loudness
#   6: tempo
#   7: time_signature