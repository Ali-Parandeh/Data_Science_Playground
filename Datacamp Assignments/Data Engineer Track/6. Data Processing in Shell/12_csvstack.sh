# Stacking files with csvkit

# SpotifyData_PopularityRank6.csv and SpotifyData_PopularityRank7.csv 
# have the same file format, column order, and overall data schema. 
# However, one file contains information for songs ranked #6, and the 
# other contains information for songs ranked #7. Combine the two files 
# together into one unified file by stacking them.

# 1. Stack SpotifyData_PopularityRank6.csv and SpotifyData_PopularityRank7.csv together. 
# 2. Re-direct the output of this stacking and save as a new file called SpotifyPopularity.csv.

# Stack the two files and save results as a new file
csvstack SpotifyData_PopularityRank6.csv SpotifyData_PopularityRank7.csv > SpotifyPopularity.csv

# Preview the newly created file 
csvlook SpotifyPopularity.csv


# | track_id               | popularity |
# | ---------------------- | ---------- |
# | 3RSMqu36JZnmMkrnNmnqyd |          6 |
# | 1o0fkWCltFHVeFIRHqvR5b |          6 |
# | 2iGShSeV6WcDbez5SLJ2bJ |          6 |
# | 2rNTo0tGUMW6rn0uHzV5er |          6 |
# | 5Egkx8edirN0pR2R58C2ME |          6 |