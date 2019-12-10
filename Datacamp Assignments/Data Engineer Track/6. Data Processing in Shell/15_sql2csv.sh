# Practice pulling data from database

# With the powers of csvkit, we don't need to download and 
# set up fancy database management software like MS SQL Server, 
# DB2, PgAdmin, or TablePlus to be able to access the data 
# inside a SQL database. We can pull data directly from our command line using csvkit's sql2csv command.

# In this practice, let's walk through pulling data step by step, 
# by applying SQL manipulations to the table Spotify_Popularity 
# which dwells inside a SQLite database called SpotifyDatabase 
# and then saving the output of the SQL query to a local .csv file Spotify_Popularity_5Rows.csv.

# 1. Use sql2csv to access the SQLite database SpotifyDatabase and query and print all data in the table Spotify_Popularity.
# 2. Use a SQL query to print the first 5 rows in the table Spotify_Popularity. Then, preview the results using csvlook.
# 3. Save queried results to a new file Spotify_Popularity_5Rows.csv. Verify and preview the file with ls and csvlook.

# Save the csv file into a database
csvsql  --db "sqlite:///SpotifyDatabase.db" \
        --tables "Spotify_Popularity" \
        --insert datasets/Spotify_Popularity.csv

# Save query to new file Spotify_MusicAttributes_5Rows.csv
sql2csv --db "sqlite:///SpotifyDatabase.db" \
        --query "SELECT * FROM Spotify_Popularity LIMIT 5" \
        > Spotify_Popularity_5Rows.csv

# Verify newly created file
ls

# Print preview of newly created file
csvlook Spotify_Popularity_5Rows.csv

# SpotifyDatabase.db  Spotify_Popularity_5Rows.csv  backup  bin

# | track_id               | popularity |
# | ---------------------- | ---------- |
# | 118GQ70Sp6pMqn6w1oKuki |          7 |
# | 6S7cr72a7a8RVAXzDCRj6m |          7 |
# | 7h2qWpMJzIVtiP30E8VDW4 |          7 |
# | 3KVQFxJ5CWOcbxdpPYdi4o |          7 |
# | 0JjNrI1xmsTfhaiU1R6OVc |          7 |