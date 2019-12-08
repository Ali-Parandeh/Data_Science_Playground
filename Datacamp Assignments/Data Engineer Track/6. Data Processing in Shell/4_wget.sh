# Fill in the two option flags 
wget -c -b https://assets.datacamp.com/production/repositories/4180/datasets/eb1d6a36fa3039e4e00064797e1a1600d267b135/201812SpotifyData.zip

# Verify that the Spotify file has been downloaded
ls 

# Preview the log file 
cat wget-log

#   1700K .......... .......... .......... .......... .......... 89%  402M 0s
#   1750K .......... .......... .......... .......... .......... 92%  365M 0s
#   1800K .......... .......... .......... .......... .......... 95%  373M 0s
#   1850K .......... .......... .......... .......... .......... 97%  407M 0s
#   1900K .......... .......... .......... .......... ....      100%  379M=0.01s

# 2019-12-08 13:20:11 (195 MB/s) - '201812SpotifyData.zip' saved [1991618/1991618]


# Because we asked wget to download in the background using 
# option flag -b, we should always take a 
# peak at the download log in case anything goes amiss.