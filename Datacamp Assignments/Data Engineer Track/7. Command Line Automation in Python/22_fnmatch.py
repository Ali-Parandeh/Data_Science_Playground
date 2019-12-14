# Is this pattern True?

# As the head of data science you often get called in to help a new data scientists 
# track down an important intermediate csv file that has gone missing. This has taken 
# so much time, that you have decided to write an automated script that identify all 
# csv files that are created by a user and then copy them to centralized storage. 
# As the first step to create this near line backup solution you have to write a 
# function that can filter and return only csv matches.

# Use the fnmatch.filter function to filter for csv files from a list of files. 
# Make sure you write a Python function so it can be portable code that a larger system can be built from.

import fnmatch

# List of file names to process
files = ["data1.csv", "script.py", "image.png", "data2.csv", "all.py"]

# Function that returns 
def csv_matches(list_of_files):
    """Return matches for csv files"""

    matches = fnmatch.filter(list_of_files, "*.csv")
    return matches

# Call function to find matches
matches = csv_matches(files)
print(f"Found matches: {matches}")


# <script.py> output:
#     Found matches: ['data1.csv', 'data2.csv']