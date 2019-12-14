# Safely find directories

# At the film studio you work at there is a need to create a tool 
# for animators to search incredibly large file systems as quickly 
# as possible and find all of the directories in them. You 
# benchmarked both regular python code and python code that 
# uses the Unix find command to see which performed better at searches. 
# You have determined for this particular problem that the Unix find 
# performs the best. One concern you have though is ensuring that the 
# command safely processes user input. In the past tools have been 
# released that accidentally deleted large sections of the file 
# server because a user accidentally put the wrong string into a tool.

# Write a tool that safely processes user input and searches a 
# file system for all directories using find and subprocess.Popen.


import subprocess

#Accepts user input
print("Enter a path to search for directories: \n")
user_input = "."
print(f"directory to process: {user_input}")

#Pass safe user input into subprocess
with subprocess.Popen(["find", user_input, "-type", "d"], stdout=subprocess.PIPE) as find:
    result = find.stdout.readlines()
    
    #Process each line and decode it and strip it
    for line in result:
        formatted_line = line.decode("utf-8").strip()
        print(f"Found Directory: {formatted_line}")


# <script.py> output:
#     Enter a path to search for directories: 
    
#     directory to process: .
#     Found Directory: .
#     Found Directory: ./mickey
#     Found Directory: ./ronny
#     Found Directory: ./movie
#     Found Directory: ./johnny


# Way to go! You were able to use a Python list to safely pass 
# arguments into the Unix find command and find all of the directories. 
# Building smalls scripts like these are an essential skill for Data Engineering.