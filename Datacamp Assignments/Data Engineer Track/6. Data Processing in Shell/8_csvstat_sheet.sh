# File conversion and summary statistics with csvkit
# It's common for Excel data files to have more than one worksheet (tab) of data. 
# The Excel file SpotifyData.xlsx has two sheets named Worksheet1_Popularity and 
# Worksheet2_MusicAttributes. Each sheet should be treated like its own data file, 
# so we will use csvkit's commands here to convert each sheet to its own CSV file. 
# Then, using the power of the commands we already know, print a high level summary for each column in the CSV files.


# 1. From SpotifyData.xlsx, convert the sheet "Worksheet1_Popularity" to 
# CSV and call it Spotify_Popularity.csv.
# 2. Print the high level summary statistics for 
# each column in Spotify_Popularity.csv.
# 3. From SpotifyData.xlsx, convert the tab "Worksheet2_MusicAttributes" 
# to CSV and call it Spotify_MusicAttributes.csv.
# 4. Print a preview of Spotify_MusicAttributes.csv using a 
# function in csvkit with Markdown-compatible, fixed-width format.


# Check to confirm name and location of the Excel data file
ls

# Convert sheet "Worksheet1_Popularity" to CSV
in2csv SpotifyData.xlsx --sheet "Worksheet1_Popularity" > Spotify_Popularity.csv

# Print high level summary statistics for each column
csvstat Spotify_Popularity.csv 

#   1. "track_id"

#         Type of data:          Text
#         Contains null values:  False
#         Unique values:         24
#         Longest value:         22 characters
#         Most common values:    118GQ70Sp6pMqn6w1oKuki (1x)
#                                6S7cr72a7a8RVAXzDCRj6m (1x)
#                                7h2qWpMJzIVtiP30E8VDW4 (1x)
#                                3KVQFxJ5CWOcbxdpPYdi4o (1x)
#                                0JjNrI1xmsTfhaiU1R6OVc (1x)

#   2. "popularity"

#         Type of data:          Number
#         Contains null values:  False
#         Unique values:         2
#         Smallest value:        6
#         Largest value:         7
#         Sum:                   154
#         Mean:                  6.417
#         Median:                6
#         StDev:                 0.504
#         Most common values:    6 (14x)
#                                7 (10x)

# Convert sheet "Worksheet2_MusicAttributes" to CSV
in2csv SpotifyData.xlsx --sheet "Worksheet2_MusicAttributes" > Spotify_MusicAttributes.csv

# Print preview of Spotify_MusicAttributes
csvlook Spotify_MusicAttributes.csv

# | track_id               | danceability | duration_ms | instrumentalness | loudness |    tempo | time_signature |
# | ---------------------- | ------------ | ----------- | ---------------- | -------- | -------- | -------------- |
# | 118GQ70Sp6pMqn6w1oKuki |       0.787… |     124,016 |           0.784… | -10.457… | 119.988… |              4 |
# | 6S7cr72a7a8RVAXzDCRj6m |       0.777… |     128,016 |           0.812… | -12.181… | 119.979… |              4 |
# | 7h2qWpMJzIVtiP30E8VDW4 |       0.796… |     132,742 |           0.919… |  -8.860… | 123.973… |              4 |
# | 3KVQFxJ5CWOcbxdpPYdi4o |       0.815… |     134,769 |           0.938… | -10.666… | 122.001… |              4 |
# | 0JjNrI1xmsTfhaiU1R6OVc |       0.799… |     124,016 |           0.915… |  -9.830… | 120.079… |              4 |
# | 3HjTcZt29JUHg5m60QhlMw |       0.812… |     134,769 |           0.914… | -11.598… | 121.994… |              4 |
# | 42LWRdkWxM9aWmDImWvH6C |       0.811… |     124,016 |           0.929… | -10.885… | 120.007… |              4 |
# | 32dMH9MvlTJaABrPHY52Yb |       0.746… |     127,727 |           0.966… | -16.615… | 124.032… |              4 |
# | 5RCPsfzmEpTXMCTNk7wEfQ |       0.813… |     134,769 |           0.891… | -11.058… | 122.010… |              4 |
# | 0y0mwXrdEzjUK5Nq8GDPnY |       0.812… |     124,016 |           0.944… | -11.006… | 120.014… |              4 |
# | 3RSMqu36JZnmMkrnNmnqyd |       0.814… |     134,769 |           0.738… |  -8.980… | 122.011… |              4 |
# | 1o0fkWCltFHVeFIRHqvR5b |       0.813… |     134,769 |           0.927… | -11.562… | 121.984… |              4 |
# | 2iGShSeV6WcDbez5SLJ2bJ |       0.810… |     124,016 |           0.932… |  -9.894… | 120.036… |              4 |
# | 2rNTo0tGUMW6rn0uHzV5er |       0.806… |     128,016 |           0.896… | -10.057… | 120.018… |              4 |
# | 5Egkx8edirN0pR2R58C2ME |       0.812… |     125,381 |           0.917… |  -9.331… | 123.014… |              4 |
# | 67r3lnzstENsRYlZWq6DYP |       0.802… |     131,016 |           0.915… |  -7.382… | 119.989… |              4 |
# | 4X8W9SSu9D5MujoxwIwqw6 |       0.822… |     132,742 |           0.774… |  -8.783… | 123.972… |              4 |
# | 4lncSzeN8WOH2iHEO593iZ |       0.809… |     124,016 |           0.937… | -10.081… | 119.990… |              4 |
# | 1L67mcddFQ65MfA3wO3MHV |       0.806… |     124,016 |           0.938… | -10.788… | 119.985… |              4 |
# | 21DU83QG4jB4mQKh76X32h |       0.812… |     125,381 |           0.897… |  -9.312… | 123.042… |              4 |