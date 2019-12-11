# Database and SQL with csvkit

# The addition of csvsql and sql2csv allows us to go throuzgh 
# an entire data workflow inside the terminal without needing 
# to install and set up additional SQL clients and software. 
# In this capstone, we will put together and pull data from a 
# SQLite database, merge this data with a locally saved file, 
# and finally, push a final merged file back to the database, 
# all without ever leaving the command line.


# 1. Download the entire table SpotifyMostRecentData from the SQLite database 
# SpotifyDatabase and save it as a csv file locally as SpotifyMostRecentData.csv.
# 2. Manipulate the two local csv files SpotifyMostRecentData.csv and Spotify201812.csv 
# by passing in the stored UNION ALL SQL query into csvsql. Save the newly created file as UnionedSpotifyData.csv.
# 3. Push the newly created csv file UnionedSpotifyData.csv back to database SpotifyDatabase as its own table.

# Store SQL for querying from SQLite database 
sqlquery_pull="SELECT * FROM SpotifyMostRecentData"

# Apply SQL to save table as local file 
sql2csv --db "sqlite:///SpotifyDatabase.db" --query "$sqlquery_pull" > SpotifyMostRecentData.csv

# Store SQL for UNION of the two local CSV files
sqlquery_union="SELECT * FROM SpotifyMostRecentData UNION ALL SELECT * FROM Spotify201812"

# Apply SQL to union the two local CSV files and save as local file
csvsql 	--query "$sqlquery_union" SpotifyMostRecentData.csv Spotify201812.csv > UnionedSpotifyData.csv

# Push UnionedSpotifyData.csv to database as a new table
csvsql --db "sqlite:///SpotifyDatabase.db" --insert UnionedSpotifyData.csv

# csvkit's ability to push and pull data from many SQL databases is one of 
# the key reasons why it is so popular with data practitioners. 
# These two tools are valuble adds to our toolkit for advanced 
# data processing on the command line!