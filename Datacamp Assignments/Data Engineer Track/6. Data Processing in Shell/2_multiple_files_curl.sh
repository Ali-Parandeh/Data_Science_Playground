# Download all 100 data files
curl -O https://s3.amazonaws.com/assets.datacamp.com/production/repositories/4180/datasets/files/datafile[001-100].txt

# Print all downloaded files to directory
ls datafile*.txt

# Bracketed characters can be used in conjunction with curl to 
# download multiple files. If you have trouble remembering what 
# each option flag does, you can always try typing curl --help or man curl