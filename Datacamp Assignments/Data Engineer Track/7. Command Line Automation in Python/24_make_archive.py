# Archive Users

# At your university they have hired you to be an assistance for 
# the machine learning course. It has been a very rewarding job, 
# but some parts of the job are frustrating. You get frequent requests 
# to retrieve items from a user's project after the course is over. 
# This has consumed much of your time. You believe you can write an 
# automation script that will archive all user folders and email them 
# the archived copy. If you can do this, it will eliminate about 80% 
# of the work you perform each semester. You are hoping to spend the 
# recovered time helping the lead instructor deliver machine learning 
# content. Use the shutil.archive function to archive a user directory. 
# You will create two archive types: gztar and zip. make_archive and 
# rmtree have been imported for you.

# 1. apath is the path where the tree is archived and string arguments 
# "zip" and "gztar" can create the two archives.
# 2. Archive the user folder copied to the location /tmp/user1.
# 3. Create a tar and gzipped archive and a zip archive.
# 4. Print both archive files out using os.listdir().

import os
from shutil import make_archive

username = "user1"
root_dir = "/tmp"
# archive root
apath = "/tmp/archive"
# archive base
final_archive_base = f"{apath}/{username}"

# create tar and gzipped archive
make_archive(final_archive_base, "gztar", apath)

# create zip archive
make_archive(final_archive_base, "zip", apath)

# print out archives
print(os.listdir(apath))

# <script.py> output:
#     ['user1.tar.gz', 'user1.zip']

# You used the built-in make_archive function to automate 
# your job and create two different types of archives: zip and tar.gz