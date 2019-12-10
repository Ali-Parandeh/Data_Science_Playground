# Filtering data by column with csvkit

# Let's get some hands-on practice for filtering data column 
# using the csvkit command csvcut. Remember that we can filter columns 
# by referring to the position of the column (e.g. 1st column, 2nd column) 
# or by referring to the exact name of the column as it appears in the data file.

# 1. Print the first column in Spotify_MusicAttributes.csv by referring to the column by its position in the file.
# 2. Print the first, third, and fifth column in Spotify_MusicAttributes.csv by referring to them by position.
# 3. Print the first column in Spotify_MusicAttributes.csv by referring to the column by its name.
# 4. Print the first, third, and fifth column in Spotify_MusicAttributes.csv by referring to them by name.

# Remember that although csvkit is written in Python, 
# which is zero based, csvkit itself is one based, so first column is in position one, not zero!

# Print a list of column headers in the data 
csvcut -n Spotify_MusicAttributes.csv

# Print the first column, by position
csvcut -c 1 Spotify_MusicAttributes.csv

# Print the first, third, and fifth column, by position
csvcut -c 1,3,5 Spotify_MusicAttributes.csv

# Print the first column, by name
csvcut -c "track_id" Spotify_MusicAttributes.csv
# Print the track id, song duration, and loudness, by name 
csvcut -c "track_id","duration_ms","loudness" Spotify_MusicAttributes.csv

# track_id,duration_ms,loudness
# 118GQ70Sp6pMqn6w1oKuki,124016.0,-10.457
# 6S7cr72a7a8RVAXzDCRj6m,128016.0,-12.181
# 7h2qWpMJzIVtiP30E8VDW4,132742.0,-8.86
# 3KVQFxJ5CWOcbxdpPYdi4o,134769.0,-10.6659999999999
# 0JjNrI1xmsTfhaiU1R6OVc,124016.0,-9.83