# Joining local CSV files using SQL

# csvsql can be used to join CSV files together even when neither of them 
# are in a database. Here, we have two CSV files Spotify_MusicAttributes.csv 
# and Spotify_Popularity.csv that are both on song level but contain different 
# attributes for each song. We can combine the two files together using a 
# SQL-like JOIN, and we can do so, through the power of csvsql.

# Store SQL query as shell variable
sql_query="SELECT ma.*, p.popularity FROM Spotify_MusicAttributes ma INNER JOIN Spotify_Popularity p ON ma.track_id = p.track_id"

# Join 2 local csvs into a new csv using the saved SQL
csvsql --query "$sql_query" Spotify_MusicAttributes.csv Spotify_Popularity.csv > Spotify_FullData.csv

# Preview newly created file
csvstat Spotify_FullData.csv

# As our SQL queries get more complex, our practice of 
# writing SQL queries into shell variables becomes more 
# important to keep the scripting cleaner and more readable.