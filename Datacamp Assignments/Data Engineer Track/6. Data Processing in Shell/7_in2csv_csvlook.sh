# Converting and previewing data with csvkit
# csvkit is written to process only CSV files. 
# Therefore, the first thing we do is to convert our raw data file into CSV format.

# After conversion, it's good practice to take a 
# quick peak into the content of the file for a quick sanity check.

# Use ls to find the name of the zipped file
ls

# SpotifyData.zip  backup  bin

# Use Linux's built in unzip tool to unpack the zipped file 
unzip SpotifyData.zip

# Check to confirm name and location of unzipped file
ls

# Convert SpotifyData.xlsx to csv
in2csv SpotifyData.xlsx > SpotifyData.csv

# Print a preview in console using a csvkit suite command 
csvlook SpotifyData.csv 

# Archive:  SpotifyData.zip
#   inflating: SpotifyData.xlsx

# SpotifyData.xlsx  SpotifyData.zip  backup  bin
# | track_id               | popularity |
# | ---------------------- | ---------- |
# | 118GQ70Sp6pMqn6w1oKuki |          7 |
# | 6S7cr72a7a8RVAXzDCRj6m |          7 |
# | 7h2qWpMJzIVtiP30E8VDW4 |          7 |
# | 3KVQFxJ5CWOcbxdpPYdi4o |          7 |
# | 0JjNrI1xmsTfhaiU1R6OVc |          7 |
# | 3HjTcZt29JUHg5m60QhlMw |          7 |
# | 42LWRdkWxM9aWmDImWvH6C |          7 |
# | 32dMH9MvlTJaABrPHY52Yb |          7 |
# | 5RCPsfzmEpTXMCTNk7wEfQ |          7 |
# | 0y0mwXrdEzjUK5Nq8GDPnY |          7 |
# | 3RSMqu36JZnmMkrnNmnqyd |          6 |
# | 1o0fkWCltFHVeFIRHqvR5b |          6 |
# | 2iGShSeV6WcDbez5SLJ2bJ |          6 |
# | 2rNTo0tGUMW6rn0uHzV5er |          6 |
# | 5Egkx8edirN0pR2R58C2ME |          6 |
# | 67r3lnzstENsRYlZWq6DYP |          6 |
# | 4X8W9SSu9D5MujoxwIwqw6 |          6 |
# | 4lncSzeN8WOH2iHEO593iZ |          6 |
# | 1L67mcddFQ65MfA3wO3MHV |          6 |
# | 21DU83QG4jB4mQKh76X32h |          6 |
# | 08nyEVO684j7pcTAhEY2zJ |          6 |
# | 4LMVmlX8WXPu8OyPwzkNpR |          6 |
# | 7JYCpIzpoidDOnnmxmHwtj |          6 |
# | 0mmFibEg5NuULMwTVN2tRU |          6 |