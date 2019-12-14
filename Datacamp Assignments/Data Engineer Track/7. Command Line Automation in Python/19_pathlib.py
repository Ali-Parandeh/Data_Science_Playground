# Rename all of the files in the cattle directory by replacing the phrase 
# 'shorthorn' with 'longhorn'. The os and pathlib modules have been imported 
# for you. Remember that the name variable will need to be split to be renamed.

import pathlib, os

# Walk the filesystem starting at the test_dir
for root, _, files in os.walk('cattle'):
    for name in files:
      	
        # Create the full path to the file by using os.path.join()
        fullpath = os.path.join(root, name)
        print(f"Processing file: {fullpath}")
        
        # Rename file
        if "shorthorn" in name:
            p = pathlib.Path(fullpath)
            shortname = name.split("_")[0][0] # You need to split the name by underscore
            new_name = f"{shortname}_longhorn"
            print(f"Renaming file {name} to {new_name}")
            p.rename(new_name)

# <script.py> output:
#     Processing file: cattle/beefy/large/george_shorthorn
#     Renaming file george_shorthorn to g_longhorn
#     Processing file: cattle/beefy/large/john_shorthorn
#     Renaming file john_shorthorn to j_longhorn
#     Processing file: cattle/beefy/large/paul_shorthorn
#     Renaming file paul_shorthorn to p_longhorn
#     Processing file: cattle/beefy/large/ringo_shorthorn
#     Renaming file ringo_shorthorn to r_longhorn


# Yeehaw! You were able to rename an entire directory full of files using pathlib 
# just in time for the auction. Apparently this isn't your first rodeo.