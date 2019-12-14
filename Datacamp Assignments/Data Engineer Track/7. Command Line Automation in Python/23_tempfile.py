# Goons over my shammy

# You are many light years from earth. Python programming aliens (Goons) 
# abducted you and are forcing you to wash computer monitors. Goons keep 
# stepping on your shammy (towel) and stopping you from working. You tell 
# the Goons if they quit stepping on your shammy, you will write a Python 
# script that programmatically creates self-destructing files and directories.

# One of the uses for self-destructing files is to create integration tests. 
# Integration tests can use temporary directory and files as a way of validating 
# that processes in an application is doing what is expected. They tell you, 
# "you had us at self-destruction". The tempfile and os module have been 
# imported for you. Remember that tempfile.NameTemporaryFile object has 
# many useful methods on it including .name.

# 1. Use tempfile.NamedTemporaryFile to create a named temporary file.
# 2. Write a message to it and verify it was written.
# 3. Verify temporary file was destroyed using os.path.exists.

import tempfile, os
# Create a self-destructing temporary file
with tempfile.NamedTemporaryFile() as exploding_file:
  	# This file will be deleted automatically after the with statement block
    print(f"Temp file created: {exploding_file.name}")
    exploding_file.write(b"This message will self-destruct in 5....4...\n")
    
    # Get to the top of the file
    exploding_file.seek(0)

    #Print the message
    print(exploding_file.read())

# Check to sure file self-destructed
if not os.path.exists(exploding_file.name): 
    print(f"self-destruction verified: {exploding_file.name}")

# <script.py> output:
#     Temp file created: /tmp/tmp1mlb5v4j
#     b'This message will self-destruct in 5....4...\n'
#     self-destruction verified: /tmp/tmp1mlb5v4j

# You used the tempfile module to programatically create self-destructing temporary files in a directory tree