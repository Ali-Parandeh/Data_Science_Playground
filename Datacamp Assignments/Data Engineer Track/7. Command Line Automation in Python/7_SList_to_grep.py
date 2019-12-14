# Using SList to grep

# You get woken up in the middle of the night by a 
# frantic phone call from a co-worker. There is a rogue process 
# running in production that is generating hundreds of extra 
# backup files. It was discovered when your co-worker tried to 
# restore from backup, but found hundreds of backup files that 
# are corrupt. You need to write a script to isolate the correct backup file.

# Use the SList object to find all files with the number 2 in them and print 
# out their full path so the backups can be inspected. The reason 2 is so 
# important is this corresponds to the second day of the week Tuesday. 
# This is the last time the backups worked properly.

In [1]: ls test_dir/
# backup_0.csv  backup_2.csv  backup_4.csv  backup_6.csv  backup_8.csv
# backup_0.txt  backup_2.txt  backup_4.txt  backup_6.txt  backup_8.txt
# backup_1.csv  backup_3.csv  backup_5.csv  backup_7.csv  backup_9.csv
# backup_1.txt  backup_3.txt  backup_5.txt  backup_7.txt  backup_9.txt

# Use the results of an SList object
root = "test_dir"

# Find the backups with "_2" in them
result = slist_out.grep("_2")

# Extract the filenames
for res in result:
	filename = res.split()[-1]
    
	# Create the full path
	fullpath = os.path.join(root, filename)
	print(f"fullpath of backup file: {fullpath}")

# <script.py> output:
#     fullpath of backup file: test_dir/backup_2.csv
#     fullpath of backup file: test_dir/backup_2.txt

# you found the uncorrupted backup files. The SList object with 
# grep created a powerful search mechanism that was used to filter from a large list of potential files.