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