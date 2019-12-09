# While curl is handy for downloading a single file, 
# it's somewhat unwieldy for handling multiple file downloads. 
# In this capstone exercise, we will use both curl and Wget to 
# download a series of monthly Spotify files, do some minor 
# processing, and consolidate all downloaded files in our local directory.


# Use curl, download and rename a single file from URL
curl -o Spotify201812.zip -L https://assets.datacamp.com/production/repositories/4180/datasets/eb1d6a36fa3039e4e00064797e1a1600d267b135/201812SpotifyData.zip

# Unzip, delete, then re-name to Spotify201812.csv
unzip Spotify201812.zip && rm Spotify201812.zip
mv 201812SpotifyData.csv Spotify201812.csv

# View url_list.txt to verify content
cat url_list.txt

# Use Wget, limit the download rate to 2500KB/s, download all files in url_list.txt
wget --limit-rate=2500k -i url_list.txt

# Take a look at all files downloaded
ls

# We downloaded 3 related data files to our local directory. 
# Remember that by default, the download rate is in Bytes per 
# second. In order to download in 2500KB/s, remember the unit KB/s is needed as well!


# HTTP request sent, awaiting response... 200 OK
# Length: 4293170 (4.1M) [text/csv]
# Saving to: 'Spotify201809.csv'

# Spotify201809.csv   100%[===================>]   4.09M  2.51MB/s    in 1.6s

# 2019-12-09 02:32:08 (2.51 MB/s) - 'Spotify201809.csv' saved [4293170/4293170]

# FINISHED --2019-12-09 02:32:08--
# Total wall clock time: 5.1s
# Downloaded: 3 files, 13M in 5.1s (2.61 MB/s)
# Spotify201809.csv  Spotify201811.csv  __MACOSX  bin
# Spotify201810.csv  Spotify201812.csv  backup    url_list.txt