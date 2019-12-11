# Preview CSV file
ls

# Apply SQL query to Spotify_MusicAttributes.csv
csvsql --query "SELECT * FROM Spotify_MusicAttributes ORDER BY duration_ms LIMIT 1" Spotify_MusicAttributes.csv

# Reformat the output using csvlook 
csvsql --query "SELECT * FROM Spotify_MusicAttributes ORDER BY duration_ms LIMIT 1" \
	Spotify_MusicAttributes.csv | csvlook


    # Re-direct output to new file: LongestSong.csv
csvsql --query "SELECT * FROM Spotify_MusicAttributes ORDER BY duration_ms LIMIT 1" \
	Spotify_MusicAttributes.csv > LongestSong.csv

    
# Preview newly created file 
csvlook LongestSong.csv


# Please remember that while this is convenient, 
# csvsql is computationally very expensive when 
# used in this manner, so it should be applied judiciously.